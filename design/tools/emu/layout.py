"""Where things live in the built game, found out from the build itself.

Nothing here is a hand-typed address or offset:

* Symbol addresses (gMain, gSaveBlock1Ptr, ...) come from `arm-none-eabi-nm`
  on pokeemerald.elf.
* Struct field offsets, struct sizes, bitfield positions and every FLAG_, VAR_,
  ITEM_, SPECIES_, MOVE_, MAP_ and TRAINER_ constant come from the compiler:
  a tiny C file is generated, compiled with the same flags the Makefile uses
  against the repo's own headers, and the numbers are read back out of the
  object file. This is the same trick the Linux kernel uses for asm-offsets.
* The answers are cached in a JSON file next to the ELF and redone whenever
  the ELF changes (size or modification time).
"""

import difflib
import hashlib
import json
import os
import re
import shlex
import subprocess
import tempfile
from pathlib import Path

CACHE_VERSION = 5
CROSS = "arm-none-eabi-"

# Used only if `make -n` cannot be run. They match the Makefile on 2026-10-09.
FALLBACK_CPPFLAGS = ["-iquote", "include", "-Wno-trigraphs", "-DMODERN=1", "-DTESTING=0", "-DEMERALD", "-std=gnu17"]
FALLBACK_CFLAGS = ["-mthumb", "-mthumb-interwork", "-mabi=apcs-gnu", "-mtune=arm7tdmi", "-march=armv4t", "-std=gnu17"]

# Headers the generated C file includes ("script.h" and the generated script_commands.h are optional extras).
INCLUDES = ["global.h", "main.h", "task.h", "palette.h", "pokemon.h", "siirtc.h", "event_data.h", "load_save.h",
            "script.h"]
OPTIONAL_INCLUDES = ["constants/script_commands.h", "constants/metatile_behaviors.h", "fieldmap.h",
                     "constants/map_event_ids.h"]

# (struct, field, optional #if guard). The compiler gives the byte offset.
FIELDS = [
    ("Coords16", ["x", "y"]),
    ("WarpData", ["mapGroup", "mapNum", "warpId", "x", "y"]),
    ("SaveBlock1", ["pos", "location", "continueGameWarp", "dynamicWarp", "lastHealLocation", "weather",
                    "playerPartyCount", "playerParty", "money", "bag", "flags", "vars", "gameStats"]),
    ("SaveBlock2", ["playerName", "playerGender", "playTimeHours", "playTimeMinutes", "playTimeSeconds",
                    "optionsButtonMode", "encryptionKey"]),
    ("SaveBlock3", ["fakeRTC"], "OW_USE_FAKE_RTC"),
    ("SiiRtcInfo", ["year", "month", "day", "dayOfWeek", "hour", "minute", "second", "status"]),
    ("Bag", ["items", "keyItems", "pokeBalls", "TMsHMs", "berries"]),
    ("ItemSlot", ["itemId", "quantity"]),
    ("BoxPokemon", ["personality", "otId", "nickname", "secure"]),
    ("Pokemon", ["box", "status", "level", "hp", "maxHP"]),
    ("Main", ["callback1", "callback2", "savedCallback", "vblankCounter1", "vblankCounter2",
              "heldKeysRaw", "newKeysRaw", "heldKeys", "newKeys", "state"]),
    ("Task", ["func", "isActive", "prev", "next", "priority", "data"]),
    ("PlayerAvatar", ["flags", "transitionFlags", "tileTransitionState", "spriteId", "objectEventId",
                      "preventStep", "gender"]),
    ("ObjectEvent", ["graphicsId", "localId", "mapNum", "mapGroup", "initialCoords", "currentCoords",
                     "previousCoords", "movementActionId", "spriteId"]),
    ("ScriptContext", ["stackDepth", "mode", "comparisonResult", "nativePtr", "scriptPtr"]),
    ("BackupMapLayout", ["width", "height", "map"]),
    ("MapLayout", ["width", "height", "primaryTileset", "secondaryTileset"]),
    ("Tileset", ["metatileAttributes"]),
    ("MapHeader", ["mapLayout", "events", "mapLayoutId", "regionMapSectionId", "weather", "mapType"]),
    ("MapEvents", ["objectEventCount", "warpCount", "coordEventCount", "bgEventCount", "warps", "coordEvents"]),
    ("WarpEvent", ["x", "y", "elevation", "warpId", "mapNum", "mapGroup"]),
    ("CoordEvent", ["x", "y", "elevation", "trigger", "index", "script"]),
]

SIZEOF = ["SaveBlock1", "SaveBlock2", "SaveBlock3", "Pokemon", "BoxPokemon", "ObjectEvent", "Task",
          "ItemSlot", "Main", "PlayerAvatar", "PaletteFadeControl", "SiiRtcInfo",
          "PokemonSubstruct0", "PokemonSubstruct1", "PokemonSubstruct2", "PokemonSubstruct3",
          "SaveBlock1ASLR", "SaveBlock2ASLR", "ScriptContext", "WarpEvent", "CoordEvent", "WarpData", "Coords16"]

# Bitfields (offsetof does not work on them). The compiler is asked to build a
# value with only that field set to all ones; the bytes tell us where it is.
BITFIELDS = [
    ("ObjectEvent", ["active", "heldMovementActive", "heldMovementFinished", "frozen", "invisible",
                     "isPlayer", "facingDirection", "movementDirection"]),
    ("PaletteFadeControl", ["active"]),
    ("Main", ["inBattle"]),
    ("PokemonSubstruct0", ["species", "heldItem", "experience"]),
    ("PokemonSubstruct1", ["move1", "move2", "move3", "move4"]),
    ("PokemonSubstruct3", ["isEgg"]),
]

# Constants always compiled in, on top of the names found in the headers.
EXTRA_CONSTANTS = ["PARTY_SIZE", "BAG_ITEMS_COUNT", "BAG_KEYITEMS_COUNT", "BAG_POKEBALLS_COUNT", "BAG_TMHM_COUNT",
                   "BAG_BERRIES_COUNT", "OBJECT_EVENTS_COUNT", "MAP_OFFSET", "MAP_OFFSET_W", "MAP_OFFSET_H", "NUM_FLAG_BYTES", "VARS_COUNT",
                   "NUM_SUBSTRUCT_BYTES", "NUM_TASKS", "MAX_BATTLE_TRAINERS", "WARP_ID_NONE",
                   "MAPGRID_METATILE_ID_MASK", "MAPGRID_COLLISION_MASK", "MAPGRID_ELEVATION_MASK",
                   "MAPGRID_COLLISION_SHIFT", "MAPGRID_ELEVATION_SHIFT", "METATILE_ATTR_BEHAVIOR_MASK",
                   "NUM_METATILES_IN_PRIMARY", "SCR_OP_END", "SCR_OP_WARP", "SCR_OP_WARPSILENT", "SCR_OP_WAITSTATE",
                   "SCR_OP_SETVAR", "SCR_OP_SETFLAG", "SCR_OP_CLEARFLAG", "SCR_OP_NOP",
                   "DIR_SOUTH", "DIR_NORTH", "DIR_WEST", "DIR_EAST"]

# Symbols that must exist (a quick "is this the right ELF" check).
REQUIRED_SYMBOLS = ["gMain", "gSaveBlock1Ptr", "gSaveBlock2Ptr", "gSaveBlock3Ptr", "gTasks", "gParties",
                    "gPartiesCount", "gObjectEvents", "gPlayerAvatar", "gSpecialVars", "gPaletteFade",
                    "gPlayerPartyPtr", "CB2_Overworld"]

# struct name -> the ELF symbol that is one instance (or array) of it, for the sanity check.
SIZE_CHECKS = {"SaveBlock1ASLR": "gSaveblock1", "SaveBlock2ASLR": "gSaveblock2", "SaveBlock3": "gSaveblock3",
               "Main": "gMain", "PlayerAvatar": "gPlayerAvatar", "PaletteFadeControl": "gPaletteFade"}
ARRAY_SIZE_CHECKS = {"ObjectEvent": ("gObjectEvents", "OBJECT_EVENTS_COUNT"), "Task": ("gTasks", "NUM_TASKS")}


class LayoutError(Exception):
    pass


def _spec_hash():
    """Changes whenever the lists above change, so an old cache is not reused with a new harness."""
    blob = json.dumps([CACHE_VERSION, FIELDS, SIZEOF, BITFIELDS, EXTRA_CONSTANTS, INCLUDES, OPTIONAL_INCLUDES])
    return hashlib.sha1(blob.encode()).hexdigest()[:12]


def find_repo():
    """The repo root: $VELDRIS_REPO if set, else the folder above design/tools/emu."""
    env = os.environ.get("VELDRIS_REPO")
    if env:
        return Path(env).resolve()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "Makefile").exists() and (parent / "include" / "constants").is_dir():
            return parent
    raise LayoutError("cannot find the repo root; set VELDRIS_REPO")


def run(cmd, cwd=None, check=True):
    p = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and p.returncode != 0:
        raise LayoutError("command failed: %s\n%s" % (" ".join(map(shlex.quote, cmd)), p.stderr[-3000:]))
    return p


# ---- compile flags ----------------------------------------------------------

def _make_stamp(repo):
    """Changes only when the Makefile (and the files it includes) change: the compile flags depend on nothing else."""
    out = []
    for name in ("Makefile", "config.mk", "make_tools.mk"):
        try:
            st = (Path(repo) / name).stat()
            out.append([name, st.st_size, st.st_mtime_ns])
        except OSError:
            out.append([name, None, None])
    return out


def compile_flags(repo, previous=None):
    """CPP and C flags exactly as the Makefile would use them.

    Asks `make -n` to print the compile line for one source file. In a tree that has been built this changes nothing
    (make only prints; on a tree that is out of date make may also regenerate its own generated headers, the same ones
    the next build would). If make is unavailable, or EMU_NO_MAKE=1 is set, the built-in copy above is used.
    """
    if os.environ.get("EMU_NO_MAKE"):
        return list(FALLBACK_CPPFLAGS), list(FALLBACK_CFLAGS), "built-in fallback (EMU_NO_MAKE)"
    if previous and previous.get("flag_source") == "make -n" and previous.get("make_stamp") == _make_stamp(repo) \
            and previous.get("cpp") and previous.get("cc"):
        return previous["cpp"], previous["cc"], "make -n"  # asked once; the Makefile has not changed since
    try:
        p = run(["make", "-n", "-B", "build/emerald/src/load_save.o"], cwd=repo, check=False)
        cpp = cc = None
        for line in p.stdout.splitlines():
            if "arm-none-eabi-cpp" in line and "cc1" in line:
                m = re.search(r"arm-none-eabi-cpp\s+(.*?)\s+src/load_save\.c", line)
                n = re.search(r"cc1\s+-quiet\s+(.*?)\s+-o\s+-\s+-", line)
                if m and n:
                    cpp = shlex.split(m.group(1))
                    cc = shlex.split(n.group(1))
                    break
        if cpp and cc:
            drop = {"-Werror", "-O2", "-O1", "-Og", "-O3", "-Os"}
            cc = [f for f in cc if f not in drop and not f.startswith("-Wno-error")]
            return cpp, cc, "make -n"
    except (OSError, LayoutError):
        pass
    return list(FALLBACK_CPPFLAGS), list(FALLBACK_CFLAGS), "built-in fallback"


# ---- names found in headers -------------------------------------------------

def _scan(path, pattern):
    try:
        text = Path(path).read_text(errors="replace")
    except OSError:
        return []
    return re.findall(pattern, text, re.M)


def collect_constant_names(repo):
    inc = Path(repo) / "include" / "constants"
    names = []
    # object-like macros with a value (not function-like, not an empty include guard)
    for f in ("flags.h", "vars.h", "opponents.h", "map_event_ids.h"):
        names += _scan(inc / f, r"^\s*#\s*define\s+([A-Z][A-Z0-9_]*)[ \t]+[^\s/]")
    # enumerators
    for f, prefix in (("items.h", "ITEM_"), ("species.h", "SPECIES_"), ("moves.h", "MOVE_"), ("map_groups.h", "MAP_"),
                      ("metatile_behaviors.h", "MB_")):
        names += _scan(inc / f, r"^\s*(%s[A-Z0-9_]+)\s*(?:=|,)" % prefix)
    names += EXTRA_CONSTANTS
    seen, out = set(), []
    for n in names:
        if n not in seen and not n.startswith("GUARD_"):
            seen.add(n)
            out.append(n)
    return out


# ---- the generated C file ---------------------------------------------------

def _include_lines():
    lines = ['#include "%s"' % h for h in INCLUDES]
    for h in OPTIONAL_INCLUDES:
        lines.append('#if defined(__has_include)\n#if __has_include("%s")\n#include "%s"\n#endif\n#endif' % (h, h))
    return lines


def _c_source(constants):
    lines = ['#include <stddef.h>']
    lines += _include_lines()
    lines.append("")
    lines.append("/* generated by design/tools/emu/layout.py: do not edit */")
    lines.append("const unsigned int veldris_values[] = {")
    keys = []
    for entry in FIELDS:
        struct, fields = entry[0], entry[1]
        guard = entry[2] if len(entry) > 2 else None
        for f in fields:
            keys.append("offsetof:%s.%s" % (struct, f))
            if guard:
                lines.append("#if %s" % guard)
            lines.append("  offsetof(struct %s, %s)," % (struct, f))
            if guard:
                lines.append("#else\n  0xFFFFFFFFu,\n#endif")
    for s in SIZEOF:
        keys.append("sizeof:%s" % s)
        lines.append("  sizeof(struct %s)," % s)
    for c in constants:
        keys.append("const:%s" % c)
        lines.append("  (unsigned int)(%s)," % c)
    lines.append("};")
    # bitfield probes: one const object each
    probes = []
    for struct, fields in BITFIELDS:
        for f in fields:
            sym = "veldris_bf_%s_%s" % (struct, f)
            probes.append((struct, f, sym))
            lines.append("const struct %s %s = { .%s = ~0 };" % (struct, sym, f))
    return "\n".join(lines) + "\n", keys, probes


def _compile(repo, src_text, cpp, cc, workdir):
    c = Path(workdir) / "gen.c"
    o = Path(workdir) / "gen.o"
    c.write_text(src_text)
    cmd = [CROSS + "gcc"] + cpp + cc + ["-w", "-O0", "-fno-lto", "-c", str(c), "-o", str(o)]
    return run(cmd, cwd=repo, check=False), o


def _nm(path):
    out = run([CROSS + "nm", "-S", "--defined-only", str(path)]).stdout
    syms = {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 4:
            syms.setdefault(parts[3], []).append((int(parts[0], 16), int(parts[1], 16), parts[2]))
        elif len(parts) == 3:
            syms.setdefault(parts[2], []).append((int(parts[0], 16), 0, parts[1]))
    return syms


def _generate(repo, elf, previous=None):
    repo = Path(repo)
    cpp, cc, flag_source = compile_flags(repo, previous)
    constants = collect_constant_names(repo)
    with tempfile.TemporaryDirectory(prefix="veldris_layout_") as tmp:
        for _ in range(8):
            src, keys, probes = _c_source(constants)
            p, obj = _compile(repo, src, cpp, cc, tmp)
            if p.returncode == 0:
                break
            # drop names the compiler does not know (header lists are approximate) and retry
            bad = set(re.findall(r"'([A-Za-z0-9_]+)' undeclared", p.stderr))
            bad |= set(re.findall(r"error: ‘([A-Za-z0-9_]+)’ undeclared", p.stderr))
            fixable = [n for n in constants if n in bad]
            if not fixable:
                raise LayoutError("could not compile the layout probe:\n" + p.stderr[-3000:])
            constants = [n for n in constants if n not in bad]
        else:
            raise LayoutError("layout probe kept failing to compile")
        binpath = Path(tmp) / "gen.bin"
        run([CROSS + "objcopy", "-O", "binary", "-j", ".rodata", str(obj), str(binpath)])
        blob = binpath.read_bytes()
        syms = _nm(obj)
        base = syms["veldris_values"][0][0]
        vals = {}
        for i, k in enumerate(keys):
            v = int.from_bytes(blob[base + 4 * i: base + 4 * i + 4], "little")
            vals[k] = None if v == 0xFFFFFFFF and k.startswith("offsetof:") else v
        bitfields = {}
        for struct, f, sym in probes:
            addr, size, _ = syms[sym][0]
            data = blob[addr:addr + size]
            bits = int.from_bytes(data, "little")
            if bits == 0:
                raise LayoutError("bitfield probe %s.%s came out empty" % (struct, f))
            shift = (bits & -bits).bit_length() - 1
            width = bits.bit_length() - shift
            if bits != ((1 << width) - 1) << shift:
                raise LayoutError("bitfield %s.%s is not contiguous (%#x)" % (struct, f, bits))
            bitfields["%s.%s" % (struct, f)] = [shift // 8, shift % 8, width, shift]
    out = {
        "cache_version": CACHE_VERSION,
        "flag_source": flag_source,
        "make_stamp": _make_stamp(repo),
        "cpp": cpp,
        "cc": cc,
        "offsetof": {k.split(":", 1)[1]: v for k, v in vals.items() if k.startswith("offsetof:")},
        "sizeof": {k.split(":", 1)[1]: v for k, v in vals.items() if k.startswith("sizeof:")},
        "const": {k.split(":", 1)[1]: v for k, v in vals.items() if k.startswith("const:")},
        "bitfield": bitfields,
    }
    return out


# ---- the public object ------------------------------------------------------

class Layout:
    """Symbols plus compiler-derived layout for one built ELF."""

    def __init__(self, repo, elf=None, rebuild_cache=False, verbose=False):
        self.repo = Path(repo)
        self.elf = Path(elf) if elf else self.repo / "pokeemerald.elf"
        if not self.elf.exists():
            raise LayoutError("no %s. Build the game first (make -j4)." % self.elf)
        self.cache_path = self.elf.with_name(self.elf.name + ".emu-layout.json")
        self.verbose = verbose
        self.symbols = _nm(self.elf)
        missing = [s for s in REQUIRED_SYMBOLS if s not in self.symbols]
        if missing:
            raise LayoutError("these symbols are not in %s (wrong ELF?): %s" % (self.elf.name, ", ".join(missing)))
        previous = self._read_cache_file()
        self.data = None if rebuild_cache else self._load_cache()
        if self.data is None:
            self.data = _generate(self.repo, self.elf, previous)
            self._save_cache()
            self.regenerated = True
        else:
            self.regenerated = False
        self._extra = {}  # constants looked up on demand
        self._check_sizes()

    # -- cache --
    def _stamp(self):
        st = self.elf.stat()
        return {"elf_size": st.st_size, "elf_mtime_ns": st.st_mtime_ns, "spec": _spec_hash()}

    def _read_cache_file(self):
        try:
            return json.loads(self.cache_path.read_text())
        except (OSError, ValueError):
            return None

    def _load_cache(self):
        d = self._read_cache_file()
        if d is None:
            return None
        if d.get("cache_version") != CACHE_VERSION or d.get("stamp") != self._stamp():
            return None
        return d

    def _save_cache(self):
        self.data["stamp"] = self._stamp()
        try:
            self.cache_path.write_text(json.dumps(self.data, indent=0))
        except OSError:
            pass  # read-only checkout: still works, just regenerates next time

    def _check_sizes(self):
        """The headers must describe the ELF. If sizes disagree, say so loudly."""
        for struct, sym in SIZE_CHECKS.items():
            want = self.data["sizeof"][struct]
            have = self.symbols[sym][0][1]
            if want != have:
                raise LayoutError(
                    "sizeof(struct %s) is %d from the headers but %s is %d bytes in the ELF. "
                    "The headers have changed since the ELF was built: run make -j4 again." % (struct, want, sym, have))
        for struct, (sym, count) in ARRAY_SIZE_CHECKS.items():
            want = self.data["sizeof"][struct] * self.data["const"][count]
            have = self.symbols[sym][0][1]
            if want != have:
                raise LayoutError("sizeof(%s) x %s is %d but %s is %d bytes in the ELF: rebuild the game."
                                  % (struct, count, want, sym, have))

    # -- symbols --
    def addr(self, name):
        """Address of a global or static symbol. Raises if missing or ambiguous."""
        entries = self.symbols.get(name)
        if not entries:
            close = difflib.get_close_matches(name, self.symbols.keys(), n=4)
            raise LayoutError("no symbol %r in the ELF%s" % (name, (" (did you mean %s?)" % ", ".join(close)) if close else ""))
        addrs = {a for a, _, _ in entries}
        if len(addrs) > 1:
            raise LayoutError("symbol %r is ambiguous (%d copies); use addrs(%r)" % (name, len(addrs), name))
        return entries[0][0]

    def addrs(self, name):
        return sorted({a for a, _, _ in self.symbols.get(name, [])})

    def size(self, name):
        return self.symbols[name][0][1]

    def has_symbol(self, name):
        return name in self.symbols

    def symbol_at(self, addr):
        """Name of the code symbol at an address (thumb bit ignored); used to read callbacks."""
        addr &= ~1
        return self._by_addr().get(addr)

    def _by_addr(self):
        if not hasattr(self, "_addr_map"):
            m = {}
            for name, entries in self.symbols.items():
                for a, _, t in entries:
                    if t in "TtWw":
                        m.setdefault(a, name)
            self._addr_map = m
        return self._addr_map

    # -- structs --
    def off(self, struct, field):
        v = self.data["offsetof"].get("%s.%s" % (struct, field), "missing")
        if v == "missing":
            raise LayoutError("no offset recorded for %s.%s (add it to FIELDS in layout.py)" % (struct, field))
        if v is None:
            raise LayoutError("%s.%s does not exist in this build" % (struct, field))
        return v

    def has_field(self, struct, field):
        return self.data["offsetof"].get("%s.%s" % (struct, field)) is not None

    def sizeof(self, struct):
        return self.data["sizeof"][struct]

    def bitfield(self, struct, field):
        """(byte offset, bit shift inside that byte, width, absolute bit shift) from the start of the struct."""
        try:
            return tuple(self.data["bitfield"]["%s.%s" % (struct, field)])
        except KeyError:
            raise LayoutError("no bitfield recorded for %s.%s (add it to BITFIELDS in layout.py)" % (struct, field))

    # -- constants --
    def const(self, name):
        """Value of a FLAG_, VAR_, ITEM_, SPECIES_, MOVE_, MAP_, TRAINER_ (or other) constant."""
        c = self.data["const"]
        if name in c:
            return c[name]
        if name in self._extra:
            return self._extra[name]
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            raise LayoutError("not a constant name: %r" % name)
        # not in the cache: ask the compiler about just this one
        val = self._ask_compiler(name)
        if val is None:
            close = difflib.get_close_matches(name, list(c.keys()), n=4)
            raise LayoutError("unknown constant %r%s" % (name, (" (did you mean %s?)" % ", ".join(close)) if close else ""))
        self._extra[name] = val
        return val

    def _ask_compiler(self, name):
        cpp, cc = self.data.get("cpp"), self.data.get("cc")
        if not cpp or not cc:
            cpp, cc, _ = compile_flags(self.repo)
        src = "\n".join(_include_lines()) + "\nconst unsigned int veldris_one = (unsigned int)(%s);\n" % name
        with tempfile.TemporaryDirectory(prefix="veldris_const_") as tmp:
            p, obj = _compile(self.repo, src, cpp, cc, tmp)
            if p.returncode != 0:
                return None
            binpath = Path(tmp) / "one.bin"
            run([CROSS + "objcopy", "-O", "binary", "-j", ".rodata", str(obj), str(binpath)])
            return int.from_bytes(binpath.read_bytes()[:4], "little")

    def source_enum(self, relpath, member):
        """Value of an enumerator that is private to a .c file (not visible to other code).

        Used for the script engine's CONTEXT_* and SCRIPT_MODE_* values: it reads the `enum { ... }` block in the
        source that names `member` and counts. Plain enumerators only (no '= value').
        """
        text = (self.repo / relpath).read_text(errors="replace")
        text = re.sub(r"//.*", "", text)
        for block in re.findall(r"enum\s*\{([^}]*)\}", text):
            names = [n.strip() for n in block.split(",") if n.strip()]
            if any("=" in n for n in names):
                continue
            if member in names:
                return names.index(member)
        raise LayoutError("enumerator %s not found in %s" % (member, relpath))

    def constants(self, prefix=""):
        return {k: v for k, v in self.data["const"].items() if k.startswith(prefix)}

    def name_of(self, prefix, value):
        """First constant (in header order) with this prefix and value: name_of('SPECIES_', 258) -> 'SPECIES_MUDKIP'.

        Several names can share a value (aliases); compare numbers, not names, when it matters.
        """
        rev = self.__dict__.setdefault("_rev", {})
        table = rev.get(prefix)
        if table is None:
            table = rev[prefix] = {}
            for k, v in self.data["const"].items():
                if k.startswith(prefix):
                    table.setdefault(v, k)
        return table.get(value)


if __name__ == "__main__":
    import sys
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lay = Layout(find_repo(), args[0] if args else None, rebuild_cache="--rebuild" in sys.argv)
    print("flags from:", lay.data["flag_source"], "| regenerated:", lay.regenerated)
    print("SaveBlock1.flags at", lay.off("SaveBlock1", "flags"), "| FLAG_SYS_B_DASH =", hex(lay.const("FLAG_SYS_B_DASH")))
    print("gMain @ %#x" % lay.addr("gMain"), "| constants:", len(lay.data["const"]))
