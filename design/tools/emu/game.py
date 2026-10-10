"""Read and change the running game through its memory.

Everything here goes through `Gdb` (memory peek and poke) and `Layout`
(addresses and struct offsets taken from the build), so nothing is hand typed.
The save blocks move around in memory (the game randomises their position),
so every access reads `gSaveBlock1Ptr` and friends fresh.
"""

import functools
import re
import time
from collections import deque

from gdbclient import GdbError

DIRS = {"S": "DIR_SOUTH", "N": "DIR_NORTH", "W": "DIR_WEST", "E": "DIR_EAST"}
# GBA key register bits (the same numbers as A_BUTTON, B_BUTTON ... in include/gba/io_reg.h)
BUTTON_BITS = {"A": 0x001, "B": 0x002, "SELECT": 0x004, "START": 0x008, "RIGHT": 0x010, "LEFT": 0x020, "UP": 0x040,
               "DOWN": 0x080, "R": 0x100, "L": 0x200}
DIR_STEP = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


class GameError(Exception):
    pass


class Timeout(GameError):
    pass


def _bits(value, shift, width):
    return (value >> shift) & ((1 << width) - 1)


# Bytes after an FC control code (COLOR takes 1, COLOR_HIGHLIGHT_SHADOW 3, ...), from charmap.txt. Only used to skip them.
_FC_ARGS = {0x01: 1, 0x02: 1, 0x03: 1, 0x04: 3, 0x05: 1, 0x06: 1, 0x07: 0, 0x08: 1, 0x09: 0, 0x0A: 0, 0x0B: 2, 0x0C: 1,
            0x0D: 1, 0x0E: 1, 0x0F: 0, 0x10: 2, 0x11: 1, 0x12: 1, 0x13: 1, 0x14: 1, 0x15: 0, 0x16: 0, 0x17: 0, 0x18: 0,
            0x19: 1, 0x1A: 1, 0x1B: 1, 0x1C: 3}


def load_charmap(path):
    """{byte: text} for the one-byte characters in charmap.txt (letters, digits, punctuation, \\n \\l \\p)."""
    table = {}
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.match(r"^'(\\[nlp]|.)'\s*=\s*([0-9A-Fa-f]{2})\s*(?:@.*)?$", line.rstrip("\n"))
        if m:
            table.setdefault(int(m.group(2), 16), m.group(1))
    table.pop(0xFF, None)  # '$' is the string terminator, not a character
    return table


def decode_text(raw, table):
    """Game text bytes to a readable string. Stops at the 0xFF terminator. Line breaks show as \\n, \\l, \\p."""
    out = []
    i = 0
    while i < len(raw) and raw[i] != 0xFF:
        b = raw[i]
        if b == 0xFC:
            code = raw[i + 1] if i + 1 < len(raw) else 0
            i += 2 + _FC_ARGS.get(code, 0)
            continue
        if b == 0xFD:  # a placeholder that was not expanded
            out.append("{?}")
            i += 2
            continue
        out.append(table.get(b, "\\x%02x" % b))
        i += 1
    return "".join(out)


def atomic(fn):
    """Run the method with the game stopped, so everything it reads or writes belongs to one moment.

    Reads and single writes do not need this (the stub answers them while the game runs, each packet is one
    consistent snapshot). It is for read-modify-write, for several writes that must land together, and for decoding
    big structures such as the party. Each stop costs the emulator about 30 ms of game time, so do not use it on
    anything a test polls in a loop. Calls nest freely: only the outermost one stops and restarts the game.
    """
    @functools.wraps(fn)
    def wrapper(self, *a, **kw):
        with self.gdb.halted():
            return fn(self, *a, **kw)
    return wrapper


class Game:
    def __init__(self, gdb, layout):
        self.gdb = gdb
        self.L = layout
        self._sym = {}
        self._substruct_table = None
        self._charmap = None
        # private enums of src/script.c, read from the source
        self.CONTEXT_RUNNING = layout.source_enum("src/script.c", "CONTEXT_RUNNING")
        self.CONTEXT_SHUTDOWN = layout.source_enum("src/script.c", "CONTEXT_SHUTDOWN")
        self.SCRIPT_MODE_BYTECODE = layout.source_enum("src/script.c", "SCRIPT_MODE_BYTECODE")

    # ---- plumbing ---------------------------------------------------------

    def a(self, name):
        """Symbol address, cached."""
        v = self._sym.get(name)
        if v is None:
            v = self._sym[name] = self.L.addr(name)
        return v

    # Small readers. Each is one packet and costs the game nothing; wrap several in `with game.gdb.halted():` only if
    # they must all belong to one instant.
    def u8(self, addr):
        return self.gdb.u8(addr)

    def u16(self, addr):
        return self.gdb.u16(addr)

    def u32(self, addr):
        return self.gdb.u32(addr)

    def s16(self, addr):
        v = self.gdb.u16(addr)
        return v - 0x10000 if v & 0x8000 else v

    def s8(self, addr):
        v = self.gdb.u8(addr)
        return v - 0x100 if v & 0x80 else v

    def sb1(self):
        return self.u32(self.a("gSaveBlock1Ptr"))

    def sb2(self):
        return self.u32(self.a("gSaveBlock2Ptr"))

    def sb3(self):
        return self.u32(self.a("gSaveBlock3Ptr"))

    def off(self, struct, field):
        return self.L.off(struct, field)

    def wait_until(self, predicate, timeout=10.0, interval=0.03, what="condition", settle=1):
        """Poll until predicate() is truthy (`settle` times in a row). Raises Timeout with a state summary.

        Polling is cheap (a read takes under a millisecond and costs the game nothing), so the default interval is
        30 ms. `settle=3` asks for three true answers in a row, which rules out a state that is true for one frame
        only (for example the gap between two scripts).
        """
        end = time.time() + timeout
        streak = 0
        while True:
            last = predicate()
            streak = streak + 1 if last else 0
            if streak >= settle:
                return last
            if time.time() >= end:
                raise Timeout("timed out after %.0f s waiting for %s. %s" % (timeout, what, self.summary()))
            time.sleep(interval)

    def read_bitfield(self, addr, struct, field):
        """Value of a bitfield of the struct that starts at `addr` (position comes from the compiler)."""
        _, _, width, shift = self.L.bitfield(struct, field)
        first = shift // 8
        nbytes = (shift % 8 + width + 7) // 8
        raw = int.from_bytes(self.gdb.read(addr + first, nbytes), "little")
        return _bits(raw, shift % 8, width)

    def keys_held(self):
        """Buttons the game sees held right now, for example {'L'} (gMain.heldKeysRaw, read straight from the pad)."""
        raw = self.u16(self.a("gMain") + self.off("Main", "heldKeysRaw"))
        return {name for name, bit in BUTTON_BITS.items() if raw & bit}

    # ---- flags and vars ---------------------------------------------------

    def flag_id(self, flag):
        if isinstance(flag, int):
            return flag
        if not flag.startswith("FLAG_"):
            raise GameError("flag names start with FLAG_, got %r" % flag)
        return self.L.const(flag)

    def var_id(self, var):
        if isinstance(var, int):
            return var
        if not var.startswith("VAR_"):
            raise GameError("var names start with VAR_, got %r" % var)
        return self.L.const(var)

    def _flag_ptr(self, fid):
        """(address, bit) like GetFlagPointer in event_data.c, or None for flag 0."""
        if fid == 0:
            return None
        if fid < self.L.const("SPECIAL_FLAGS_START"):
            return self.sb1() + self.off("SaveBlock1", "flags") + fid // 8, fid % 8
        return self.a("sSpecialFlags") + (fid - self.L.const("SPECIAL_FLAGS_START")) // 8, fid % 8

    def flag_get(self, flag):
        p = self._flag_ptr(self.flag_id(flag))
        if p is None:
            return False
        return bool(self.u8(p[0]) & (1 << p[1]))

    @atomic
    def flag_set(self, flag, value=True):
        p = self._flag_ptr(self.flag_id(flag))
        if p is None:
            raise GameError("flag 0 cannot be set")
        b = self.u8(p[0])
        self.gdb.put_u8(p[0], (b | (1 << p[1])) if value else (b & ~(1 << p[1]) & 0xFF))

    def flag_clear(self, flag):
        self.flag_set(flag, False)

    def _var_ptr(self, vid):
        """Address of a var like GetVarPointer in event_data.c, or None for 'not a var'."""
        if vid < self.L.const("VARS_START"):
            return None
        if vid < self.L.const("SPECIAL_VARS_START"):
            return self.sb1() + self.off("SaveBlock1", "vars") + 2 * (vid - self.L.const("VARS_START"))
        return self.u32(self.a("gSpecialVars") + 4 * (vid - self.L.const("SPECIAL_VARS_START")))

    def var_get(self, var):
        p = self._var_ptr(self.var_id(var))
        if p is None:
            raise GameError("%r is not a var id" % (var,))
        return self.u16(p)

    def var_set(self, var, value):
        p = self._var_ptr(self.var_id(var))
        if p is None:
            raise GameError("%r is not a var id" % (var,))
        self.gdb.put_u16(p, value)

    # ---- bag --------------------------------------------------------------

    def _bag_pockets(self):
        return [("items", "BAG_ITEMS_COUNT"), ("keyItems", "BAG_KEYITEMS_COUNT"), ("pokeBalls", "BAG_POKEBALLS_COUNT"),
                ("TMsHMs", "BAG_TMHM_COUNT"), ("berries", "BAG_BERRIES_COUNT")]

    @atomic
    def bag(self):
        """{pocket name: {ITEM_NAME or id: quantity}} for everything in the bag."""
        L = self.L
        sb1 = self.sb1()
        key = self.u32(self.sb2() + self.off("SaveBlock2", "encryptionKey")) & 0xFFFF  # quantities are XORed with it
        slot = L.sizeof("ItemSlot")
        qoff = self.off("ItemSlot", "quantity")
        out = {}
        for pocket, count_name in self._bag_pockets():
            base = sb1 + self.off("SaveBlock1", "bag") + self.off("Bag", pocket)
            n = L.const(count_name)
            raw = self.gdb.read(base, n * slot)
            items = {}
            for i in range(n):
                iid = int.from_bytes(raw[i * slot:i * slot + 2], "little")
                if iid == 0:
                    continue
                qty = int.from_bytes(raw[i * slot + qoff:i * slot + qoff + 2], "little") ^ key
                items[L.name_of("ITEM_", iid) or iid] = qty
            out[pocket] = items
        return out

    def bag_where(self, item):
        """Name of the pocket that holds the item ('items', 'keyItems', 'pokeBalls', 'TMsHMs', 'berries') or None."""
        iid = item if isinstance(item, int) else self.L.const(item)
        name = self.L.name_of("ITEM_", iid) or iid
        for pocket, items in self.bag().items():
            if name in items:
                return pocket
        return None

    def bag_count(self, item):
        """How many of an item the bag holds (0 if none). `item` is ITEM_NAME or an id."""
        iid = item if isinstance(item, int) else self.L.const(item)
        name = self.L.name_of("ITEM_", iid) or iid
        total = 0
        for items in self.bag().values():
            total += items.get(name, 0)
        return total

    # ---- party ------------------------------------------------------------

    def _substruct_offsets(self):
        if self._substruct_table is None:
            raw = self.gdb.read(self.a("sSubstructOffsets"), 4 * 24)
            self._substruct_table = [list(raw[i * 24:(i + 1) * 24]) for i in range(4)]
        return self._substruct_table

    def _decode_mon(self, raw):
        L = self.L
        box = L.off("Pokemon", "box")
        pers = int.from_bytes(raw[box + L.off("BoxPokemon", "personality"):][:4], "little")
        otid = int.from_bytes(raw[box + L.off("BoxPokemon", "otId"):][:4], "little")
        sec = box + L.off("BoxPokemon", "secure")
        size = L.const("NUM_SUBSTRUCT_BYTES")
        secure = bytearray(raw[sec:sec + 4 * size])
        key = pers ^ otid
        for i in range(0, len(secure), 4):
            w = int.from_bytes(secure[i:i + 4], "little") ^ key
            secure[i:i + 4] = w.to_bytes(4, "little")
        table = self._substruct_offsets()

        def sub(kind):
            slot = table[kind][pers % 24]
            return int.from_bytes(secure[slot * size:(slot + 1) * size], "little")

        def field(kind, struct, name):
            _, _, width, shift = L.bitfield(struct, name)
            return _bits(sub(kind), shift, width)

        species = field(0, "PokemonSubstruct0", "species")
        moves = [field(1, "PokemonSubstruct1", "move%d" % i) for i in (1, 2, 3, 4)]
        return {
            "species_id": species,
            "species": L.name_of("SPECIES_", species),
            "held_item": L.name_of("ITEM_", field(0, "PokemonSubstruct0", "heldItem")) or None,
            "moves": [L.name_of("MOVE_", m) for m in moves if m],
            "level": raw[L.off("Pokemon", "level")],
            "hp": int.from_bytes(raw[L.off("Pokemon", "hp"):][:2], "little"),
            "max_hp": int.from_bytes(raw[L.off("Pokemon", "maxHP"):][:2], "little"),
            "personality": pers,
            "exp": field(0, "PokemonSubstruct0", "experience"),
        }

    def _party_at(self, ptr_symbol, count_symbol):
        """Decode a party. The game keeps pointers to the party and its count in ROM (gPlayerPartyPtr and friends)."""
        L = self.L
        base = self.u32(self.a(ptr_symbol))
        count = self.u8(self.u32(self.a(count_symbol)))
        size = L.sizeof("Pokemon")
        raw = self.gdb.read(base, size * L.const("PARTY_SIZE"))
        return [self._decode_mon(raw[i * size:(i + 1) * size]) for i in range(min(count, L.const("PARTY_SIZE")))]

    @atomic
    def party(self):
        """The player's party as a list of dicts (species, level, hp, moves, ...)."""
        return self._party_at("gPlayerPartyPtr", "gPlayerPartyCountPtr")

    @atomic
    def enemy_party(self):
        """The opponent's party. For a wild battle it is filled in before the battle screen appears."""
        return self._party_at("gEnemyPartyPtr", "gEnemyPartyCountPtr")

    # ---- map, position and the avatar ------------------------------------

    def map_id(self):
        """(group, number) of the current map."""
        loc = self.sb1() + self.off("SaveBlock1", "location")
        raw = self.gdb.read(loc, self.L.sizeof("WarpData"))  # one packet: group and number belong together
        return (raw[self.off("WarpData", "mapGroup")] ^ 0x80) - 0x80, (raw[self.off("WarpData", "mapNum")] ^ 0x80) - 0x80

    def map_name(self):
        g, n = self.map_id()
        return self.L.name_of("MAP_", (g << 8) | n) or "MAP(%d,%d)" % (g, n)

    def _player_object(self):
        L = self.L
        idx = self.u8(self.a("gPlayerAvatar") + self.off("PlayerAvatar", "objectEventId"))
        return self.a("gObjectEvents") + idx * L.sizeof("ObjectEvent")

    def _coords(self, addr):
        """A Coords16 at `addr` as (x, y), read as one packet."""
        raw = self.gdb.read(addr, self.L.sizeof("Coords16"))
        x, y = self.off("Coords16", "x"), self.off("Coords16", "y")
        return int.from_bytes(raw[x:x + 2], "little", signed=True), int.from_bytes(raw[y:y + 2], "little", signed=True)

    def player_pos(self):
        """(x, y) in map tiles, from the player's object (always exact)."""
        x, y = self._coords(self._player_object() + self.off("ObjectEvent", "currentCoords"))
        mo = self.L.const("MAP_OFFSET")  # object coordinates include the 7-tile border
        return x - mo, y - mo

    def saved_pos(self):
        """(x, y) from gSaveBlock1Ptr->pos (what the save file stores; follows the camera)."""
        return self._coords(self.sb1() + self.off("SaveBlock1", "pos"))

    def player_facing(self):
        """'S', 'N', 'W' or 'E'."""
        v = self.read_bitfield(self._player_object(), "ObjectEvent", "facingDirection")
        for k, name in DIRS.items():
            if self.L.const(name) == v:
                return k
        return "?"

    def avatar_moving(self):
        return self.u8(self.a("gPlayerAvatar") + self.off("PlayerAvatar", "tileTransitionState")) != 0

    # ---- clock ------------------------------------------------------------

    def clock(self):
        """The fake clock: dict(day, hour, minute, second, weekday). Needs OW_USE_FAKE_RTC."""
        if not self.L.has_field("SaveBlock3", "fakeRTC"):
            raise GameError("this build has no fake clock (OW_USE_FAKE_RTC is off)")
        raw = self.gdb.read(self.sb3() + self.off("SaveBlock3", "fakeRTC"), self.L.sizeof("SiiRtcInfo"))

        def f(n):
            return raw[self.off("SiiRtcInfo", n)]

        return {"day": f("day"), "hour": f("hour"), "minute": f("minute"), "second": f("second"), "weekday": f("dayOfWeek")}

    @atomic
    def set_clock(self, hour, minute=0, second=0):
        """Jump the fake clock to a time of day. The game keeps ticking from there (20 game seconds per real second)."""
        base = self.sb3() + self.off("SaveBlock3", "fakeRTC")
        self.gdb.put_u8(base + self.off("SiiRtcInfo", "hour"), hour)
        self.gdb.put_u8(base + self.off("SiiRtcInfo", "minute"), minute)
        self.gdb.put_u8(base + self.off("SiiRtcInfo", "second"), second)

    # ---- what is the game doing? -----------------------------------------

    def callback2(self):
        """Name of the main callback function (CB2_Overworld, BattleMainCB2, ...)."""
        addr = self.u32(self.a("gMain") + self.off("Main", "callback2"))
        return self.L.symbol_at(addr) or "0x%08x" % addr

    def tasks(self):
        """Active tasks as [(id, function name)]."""
        L = self.L
        size = L.sizeof("Task")
        n = L.const("NUM_TASKS")
        raw = self.gdb.read(self.a("gTasks"), size * n)
        out = []
        for i in range(n):
            t = raw[i * size:(i + 1) * size]
            if t[L.off("Task", "isActive")]:
                fn = int.from_bytes(t[L.off("Task", "func"):][:4], "little")
                out.append((i, L.symbol_at(fn) or "0x%08x" % fn))
        return out

    def task_names(self):
        return [name for _, name in self.tasks()]

    def fading(self):
        return bool(self.read_bitfield(self.a("gPaletteFade"), "PaletteFadeControl", "active"))

    def in_battle(self):
        return bool(self.read_bitfield(self.a("gMain"), "Main", "inBattle"))

    def battle_pending(self):
        """True from the moment a battle has been triggered (the swirl is playing) until it ends."""
        names = self.task_names()
        return self.in_battle() or "Task_BattleStart" in names or "Task_BattleTransition" in names or \
            self.callback2() in ("BattleMainCB2", "CB2_InitBattle")

    def busy(self):
        """None if the player is free, else 'battle' or 'script' (something took control away from the player)."""
        if self.battle_pending():
            return "battle"
        if self.script_running():
            return "script"
        return None

    def script_status(self):
        """0 running, 1 waiting, 2 not running (the script engine's own numbers)."""
        return self.u8(self.a("sGlobalScriptContextStatus"))

    def script_running(self):
        """True while a script holds the player (running, or waiting with the field controls locked).

        A script that is 'waiting' but has let go of the controls is dead: the wall clock's view screen reloads the
        field and the script never resumes, yet the player can walk and talk again. That is not counted here.
        """
        return self.script_status() != self.CONTEXT_SHUTDOWN and self.field_locked()

    def field_locked(self):
        return bool(self.u8(self.a("sLockFieldControls")))

    def in_overworld(self):
        return self.callback2() == "CB2_Overworld"

    def overworld_idle(self):
        """True when the player could press a button and the field would respond."""
        return (self.in_overworld() and not self.fading() and not self.script_running()
                and not self.field_locked() and not self.avatar_moving())

    def wait_overworld_idle(self, timeout=20.0):
        return self.wait_until(self.overworld_idle, timeout, what="the overworld to be idle")

    def state(self):
        """A short label: 'title', 'overworld', 'overworld+script', 'battle', or the name of the main callback."""
        cb = self.callback2()
        if cb == "CB2_Overworld":
            return "overworld+script" if self.script_running() else "overworld"
        if "Task_TitleScreenPhase3" in self.task_names():
            return "title"
        if cb in ("BattleMainCB2", "CB2_InitBattle") or self.in_battle():
            return "battle"
        return cb

    def summary(self):
        """One line describing where the game is, for failure messages."""
        try:
            with self.gdb.halted():
                return "[state=%s map=%s pos=%s script=%s tasks=%s]" % (
                    self.state(), self.map_name(), self.player_pos(), self.script_status(), ",".join(self.task_names()[:6]))
        except (GdbError, GameError, KeyError) as e:
            return "[state unavailable: %s]" % e

    # ---- text on screen -----------------------------------------------------

    def message_text(self):
        """The text of the last message box the game opened (it lives in gStringVar4), as readable text.

        Names are already expanded; line breaks show as \\n (new line), \\l (scroll) and \\p (new box).
        """
        if self._charmap is None:
            self._charmap = load_charmap(self.L.repo / "charmap.txt")
        return decode_text(self.gdb.read(self.a("gStringVar4"), self.L.size("gStringVar4")), self._charmap)

    # ---- injecting a script ----------------------------------------------

    def _point_script_at(self, addr):
        """Aim the global script context at `addr` and switch it on (what ScriptContext_SetupScript does)."""
        ctx = self.a("sGlobalScriptContext")
        with self.gdb.halted():
            if self.script_running():
                raise GameError("a script is already running; wait for it to finish")
            self.gdb.put_u8(ctx + self.off("ScriptContext", "stackDepth"), 0)
            self.gdb.put_u8(ctx + self.off("ScriptContext", "mode"), self.SCRIPT_MODE_BYTECODE)
            self.gdb.put_u32(ctx + self.off("ScriptContext", "nativePtr"), 0)
            self.gdb.put_u32(ctx + self.off("ScriptContext", "scriptPtr"), addr)
            self.gdb.put_u8(self.a("sLockFieldControls"), 1)
            self.gdb.put_u8(self.a("sGlobalScriptContextStatus"), self.CONTEXT_RUNNING)

    def run_script(self, code, wait_done=False, timeout=10.0):
        """Run a few script commands (bytes) in the game's own script engine.

        The bytes go into the text buffer gStringVar4 and the global script context is pointed at them, exactly as
        ScriptContext_SetupScript would. It refuses to run while another script is going. End with SCR_OP_END.
        """
        buf = self.a("gStringVar4")
        if len(code) > self.L.size("gStringVar4"):
            raise GameError("script too long")
        with self.gdb.halted():
            if self.script_running():
                raise GameError("a script is already running; wait for it to finish")
            self.gdb.write(buf, bytes(code))
            self._point_script_at(buf)
        if wait_done:
            self.wait_until(lambda: not self.script_running(), timeout, what="the injected script to finish")

    def _op(self, name):
        return self.L.const(name) & 0xFF

    def warp(self, map_name, x=None, y=None, warp_id=None, timeout=30.0, check_tile=True):
        """Teleport with the game's own warp command and wait until the new map is idle.

        `map_name` is a MAP_ constant, for example 'MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F'. Give either x and y (map tiles)
        or the number of one of that map's warps. Needs the overworld and no script running. If you give x and y and
        the tile is a wall, it raises (the player would be stuck inside the scenery); `ascii_map()` shows free tiles.
        """
        if warp_id is None and (x is None or y is None):
            raise GameError("warp() needs x and y, or warp_id")
        mid = self.L.const(map_name)
        if warp_id is None:
            tail = bytes([0xFF]) + x.to_bytes(2, "little") + y.to_bytes(2, "little")
        else:
            tail = bytes([warp_id]) + b"\xff\xff\xff\xff"
        code = bytes([self._op("SCR_OP_WARP"), mid >> 8, mid & 0xFF]) + tail + \
            bytes([self._op("SCR_OP_WAITSTATE"), self._op("SCR_OP_END")])
        if not self.overworld_idle():
            self.wait_overworld_idle(timeout)
        self.run_script(code)
        self.wait_until(lambda: self.map_name() == map_name and self.overworld_idle(), timeout,
                        what="the warp to %s to finish" % map_name, settle=3)
        pos = self.player_pos()
        if check_tile and warp_id is None:
            tile = self.read_map()["tiles"].get(pos)
            if tile is None or tile[1] != 0:
                raise GameError("warped onto a blocked tile (%d, %d) of %s: pick a free tile (see Game.ascii_map())"
                                % (pos[0], pos[1], map_name))
        return pos

    def run_rom_script(self, label, timeout=30.0):
        """Run a script that is already in the ROM, by its label (for example 'Veldris_Debug_Preset4').

        This is what the debug menu does for its Scripts entries. Returns at once; use wait_overworld_idle() afterwards
        (some scripts ask for A presses).
        """
        addr = self.a(label)
        if not self.overworld_idle():
            self.wait_overworld_idle(timeout)
        self._point_script_at(addr)

    def debug_preset(self, number, timeout=60.0):
        """Run the debug menu's Scripts preset 1 to 8 (data/scripts/veldris_debug.inc) and wait until the game is idle."""
        self.run_rom_script("Veldris_Debug_Preset%d" % number)
        self.wait_until(lambda: not self.script_running() and self.overworld_idle(), timeout,
                        what="debug preset %d to finish" % number)

    # ---- the map grid -----------------------------------------------------

    def _grid(self):
        """(width, height, [u16 blocks]) of the loaded map including its border (MAP_OFFSET_W / MAP_OFFSET_H extra)."""
        base = self.a("gBackupMapLayout")
        with self.gdb.halted():
            w = self.u32(base + self.off("BackupMapLayout", "width"))
            h = self.u32(base + self.off("BackupMapLayout", "height"))
            ptr = self.u32(base + self.off("BackupMapLayout", "map"))
            raw = self.gdb.read(ptr, 2 * w * h)
        return w, h, [int.from_bytes(raw[i:i + 2], "little") for i in range(0, len(raw), 2)]

    @atomic
    def map_size(self):
        """(width, height) of the current map in tiles, without the border."""
        w, h, _ = self._grid()
        return w - self.L.const("MAP_OFFSET_W"), h - self.L.const("MAP_OFFSET_H")

    def _behavior_table(self):
        """Reader for metatile behaviour: returns f(metatile_id) -> behaviour number."""
        L = self.L
        with self.gdb.halted():
            layout = self.u32(self.a("gMapHeader") + self.off("MapHeader", "mapLayout"))
            prim = self.u32(layout + self.off("MapLayout", "primaryTileset"))
            sec = self.u32(layout + self.off("MapLayout", "secondaryTileset"))
            pa = self.u32(prim + self.off("Tileset", "metatileAttributes"))
            sa = self.u32(sec + self.off("Tileset", "metatileAttributes"))
            nprim = L.const("NUM_METATILES_IN_PRIMARY")
            # attributes are u16 each; read generously (a tileset never has more than 1024 metatiles)
            prim_raw = self.gdb.read(pa, 2 * nprim)
            sec_raw = self.gdb.read(sa, 2 * (1024 - nprim))
        mask = L.const("METATILE_ATTR_BEHAVIOR_MASK")

        def behavior(mid):
            if mid < nprim:
                return int.from_bytes(prim_raw[2 * mid:2 * mid + 2], "little") & mask
            i = mid - nprim
            return int.from_bytes(sec_raw[2 * i:2 * i + 2], "little") & mask

        return behavior

    @atomic
    def read_map(self):
        """Snapshot of the current map: dict with width, height, and per tile (x, y) -> (behaviour, collision, elevation).

        Coordinates are map tiles (the same numbers Porymap shows).
        """
        L = self.L
        mo = L.const("MAP_OFFSET")  # the map sits 7 tiles in from the left and top of the grid (the right border is 8)
        w, h, blocks = self._grid()
        map_w, map_h = w - L.const("MAP_OFFSET_W"), h - L.const("MAP_OFFSET_H")
        beh = self._behavior_table()
        idmask, colmask, elmask = (L.const("MAPGRID_METATILE_ID_MASK"), L.const("MAPGRID_COLLISION_MASK"),
                                   L.const("MAPGRID_ELEVATION_MASK"))
        cs, es = L.const("MAPGRID_COLLISION_SHIFT"), L.const("MAPGRID_ELEVATION_SHIFT")
        tiles = {}
        for y in range(map_h):
            for x in range(map_w):
                b = blocks[(y + mo) * w + (x + mo)]
                tiles[(x, y)] = (beh(b & idmask), (b & colmask) >> cs, (b & elmask) >> es)
        return {"width": map_w, "height": map_h, "tiles": tiles}

    def ascii_map(self, snapshot=None):
        """The current map as text, one character per tile, with a row/column ruler.

        `#` blocked, `.` free, `g` tall grass, `~` water, `W` warp, `T` trigger tile, `N` NPC, `@` the player.
        Coordinates are map tiles (what Porymap shows).
        """
        snap = snapshot or self.read_map()
        special = self.special_tiles()
        npcs = {(o["x"], o["y"]) for o in self.objects()}
        me = self.player_pos()
        w, h = snap["width"], snap["height"]
        rows = ["    " + "".join(str(x // 10 % 10) if x % 10 == 0 else " " for x in range(w)),
                "    " + "".join(str(x % 10) for x in range(w))]
        for y in range(h):
            line = []
            for x in range(w):
                beh, collision, _ = snap["tiles"][(x, y)]
                name = self.behavior_name(beh)
                ch = "#" if collision else "."
                if "GRASS" in name:
                    ch = "g"
                elif "WATER" in name and not collision:
                    ch = "~"
                if (x, y) in special:
                    ch = "W" if special[(x, y)] == "warp" else "T"
                if (x, y) in npcs:
                    ch = "N"
                if (x, y) == me:
                    ch = "@"
                line.append(ch)
            rows.append("%3d %s" % (y, "".join(line)))
        return "\n".join(rows)

    def behavior_name(self, number):
        return self.L.name_of("MB_", number) or str(number)

    @atomic
    def find_tiles(self, behavior_name, snapshot=None):
        """All (x, y) whose metatile behaviour is MB_<name> (for example 'MB_TALL_GRASS'), in reading order."""
        snap = snapshot or self.read_map()
        want = self.L.const(behavior_name)
        return sorted(((x, y) for (x, y), (b, _, _) in snap["tiles"].items() if b == want), key=lambda p: (p[1], p[0]))

    @atomic
    def special_tiles(self):
        """Tiles that fire something when stepped on: warps and coord-event triggers of the current map."""
        L = self.L
        with self.gdb.halted():
            ev = self.u32(self.a("gMapHeader") + self.off("MapHeader", "events"))
            out = {}
            for kind, count_f, ptr_f, struct in (("warp", "warpCount", "warps", "WarpEvent"),
                                                  ("trigger", "coordEventCount", "coordEvents", "CoordEvent")):
                n = self.u8(ev + self.off("MapEvents", count_f))
                ptr = self.u32(ev + self.off("MapEvents", ptr_f))
                if not n or not ptr:
                    continue
                size = L.sizeof(struct)
                raw = self.gdb.read(ptr, n * size)
                for i in range(n):
                    e = raw[i * size:(i + 1) * size]
                    x = int.from_bytes(e[self.off(struct, "x"):][:2], "little", signed=True)
                    y = int.from_bytes(e[self.off(struct, "y"):][:2], "little", signed=True)
                    out.setdefault((x, y), kind)
        return out

    def objects(self, include_player=False):
        """The objects (NPCs, items, trainers, Pokemon followers) of the current map.

        A list of dicts: local_id, graphics_id, x, y (map tiles), facing ('N', 'S', 'W', 'E'), invisible, index.
        Objects that are switched off (an NPC hidden by a flag) are not listed.
        """
        L = self.L
        size = L.sizeof("ObjectEvent")
        n = L.const("OBJECT_EVENTS_COUNT")
        raw = self.gdb.read(self.a("gObjectEvents"), size * n)
        group, num = self.map_id()
        mo = L.const("MAP_OFFSET")
        facing_names = {L.const(name): key for key, name in DIRS.items()}
        out = []
        for i in range(n):
            o = raw[i * size:(i + 1) * size]
            bits = int.from_bytes(o, "little")

            def bit(field):
                _, _, width, shift = L.bitfield("ObjectEvent", field)
                return _bits(bits, shift, width)

            if not bit("active") or (bit("isPlayer") and not include_player):
                continue
            c = L.off("ObjectEvent", "currentCoords")
            out.append({
                "index": i,
                "local_id": o[L.off("ObjectEvent", "localId")],
                "graphics_id": int.from_bytes(o[L.off("ObjectEvent", "graphicsId"):][:2], "little"),
                "x": int.from_bytes(o[c:c + 2], "little", signed=True) - mo,
                "y": int.from_bytes(o[c + 2:c + 4], "little", signed=True) - mo,
                "facing": facing_names.get(bit("facingDirection"), "?"),
                "invisible": bool(bit("invisible")),
                "player": bool(bit("isPlayer")),
                "map": (o[L.off("ObjectEvent", "mapGroup")], o[L.off("ObjectEvent", "mapNum")]),
            })
        here = (group & 0xFF, num & 0xFF)
        return [o for o in out if o["player"] or o["map"] == here]

    def object(self, target):
        """One object of the current map, or None. `target` is a local id (int), a name such as
        'LOCALID_HOLLOWBROOK_MOM', or a tile (x, y)."""
        objs = self.objects()
        if isinstance(target, tuple):
            found = [o for o in objs if (o["x"], o["y"]) == target]
        else:
            lid = target if isinstance(target, int) else self.L.const(target)
            found = [o for o in objs if o["local_id"] == lid]
        return found[0] if found else None

    def npc_tiles(self):
        """Tiles occupied by non-player objects (NPCs, items, trainers)."""
        return {(o["x"], o["y"]) for o in self.objects()}

    def find_path(self, goal, start=None, snapshot=None, avoid_special=True):
        """Shortest walk from the player (or `start`) to `goal` as a string of U/D/L/R, or None.

        Walls come from the map's collision bits; NPCs are avoided, and so are warp tiles and trigger tiles (the goal
        itself may be one). `avoid_special="warps"` avoids only the warp tiles (use it when the triggers are switched
        off by a var), `False` avoids neither. Ledges ('JUMP' behaviours) count as walls. Elevation differences are not
        modelled: if the real game refuses a step, `Emulator.walk` reports where it stopped.
        """
        snap = snapshot or self.read_map()
        start = start or self.player_pos()
        blocked = set(self.npc_tiles())
        if avoid_special == "warps":
            special = {p for p, kind in self.special_tiles().items() if kind == "warp"}
        else:
            special = set(self.special_tiles()) if avoid_special else set()
        tiles = snap["tiles"]

        def ok(p):
            t = tiles.get(p)
            if t is None or t[1] != 0:
                return False
            if "JUMP" in self.behavior_name(t[0]) or "IMPASSABLE" in self.behavior_name(t[0]):
                return False
            return p not in blocked and (p == goal or p not in special)

        prev = {start: None}
        q = deque([start])
        while q:
            cur = q.popleft()
            if cur == goal:
                break
            for d, (dx, dy) in DIR_STEP.items():
                nxt = (cur[0] + dx, cur[1] + dy)
                if nxt in prev or not ok(nxt):
                    continue
                prev[nxt] = (cur, d)
                q.append(nxt)
        if goal not in prev:
            return None
        path = []
        cur = goal
        while prev[cur] is not None:
            cur, d = prev[cur]
            path.append(d)
        return "".join(reversed(path))
