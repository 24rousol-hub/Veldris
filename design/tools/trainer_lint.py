#!/usr/bin/env python3
"""Trainer-id reuse lint (proposed hack tool). Run from the repo root: python3 design/tools/trainer_lint.py

Checks, in order:
 1. every '=== TRAINER_X ===' header in src/data/trainers.party is a PRIMARY name (a #define with a number)
 2. no two Veldris script fights resolve to the same trainer id (they would share one defeated flag)
 3. every TRAINER_TROGLODYTE_* used by a map script has a row in VELDRIS_TROGLODYTE_FIGHTS (include/veldris_journal.h)
 4. no trainerbattle_earlyrival uses a TROGLODYTE id (it sets the defeated flag on a LOSS)
 5. every Pokemon in a Veldris-owned block has an IVs line (a missing line means 31)
"""
import re, sys, glob, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_BASE = "d946dc6515e11b0aa85d2e11824eceb31e8cff1a"  # design/engine-edits.md, 'Upstream baseline'


def vanilla_maps():
    """Map folders that exist upstream. Every other folder under data/maps is a Veldris map, so a new town or
    route is linted without editing this file. Falls back to a name prefix list if the baseline commit is missing."""
    try:
        out = subprocess.check_output(["git", "ls-tree", "-d", "--name-only", UPSTREAM_BASE, "data/maps/"],
                                      cwd=ROOT, stderr=subprocess.DEVNULL, text=True)
        return {Path(x).name for x in out.split()}
    except (subprocess.CalledProcessError, OSError):
        print("note: baseline commit not found, treating Hollowbrook/Crestfall/VeldrisRoute*/Wendlebury* as the Veldris maps")
        return None


VANILLA = vanilla_maps()


def is_veldris_map(name):
    if VANILLA is not None:
        return name not in VANILLA
    return name.startswith(("Hollowbrook", "Crestfall", "VeldrisRoute", "Wendlebury"))

opp = (ROOT / "include/constants/opponents.h").read_text()
defs = dict(re.findall(r"^#define\s+(TRAINER_\w+)\s+(\w+)", opp, re.M))


def resolve(name, depth=0):
    v = defs.get(name)
    if v is None or depth > 8:
        return None
    return int(v) if v.isdigit() else resolve(v, depth + 1)


errors = []
party = (ROOT / "src/data/trainers.party").read_text()
blocks = re.split(r"^=== (TRAINER_\w+) ===\s*$", party, flags=re.M)
names, bodies = blocks[1::2], blocks[2::2]
for n in names:
    if not defs.get(n, "").isdigit():
        errors.append(f"trainers.party: header {n} is not a primary #define (rename the header to the primary name)")

# 2 + 3 + 4: scripts
use = {}
journal = (ROOT / "include/veldris_journal.h").read_text()
rows = {resolve(n) for n in re.findall(r"X\((TRAINER_\w+)\)", journal)}
trog = {resolve(n) for n in defs if "TROGLODYTE" in n}
for p in sorted(glob.glob(str(ROOT / "data/maps/*/scripts.inc"))):
    mapname = Path(p).parent.name
    if not is_veldris_map(mapname):
        continue
    for ln, line in enumerate(open(p, encoding="utf-8"), 1):
        m = re.match(r"\s*(trainerbattle_\w+)\s+(TRAINER_\w+)", line)
        if not m:
            continue
        kind, name = m.groups()
        tid = resolve(name)
        use.setdefault(tid, set()).add((mapname, name))
        if tid in trog:
            if kind == "trainerbattle_earlyrival":
                errors.append(f"{mapname}:{ln}: {name} uses trainerbattle_earlyrival (sets the flag on a loss)")
            if tid not in rows:
                errors.append(f"{mapname}:{ln}: {name} has no row in VELDRIS_TROGLODYTE_FIGHTS")
for tid, who in use.items():
    if len({w[0] for w in who}) > 1 or len({w[1] for w in who}) > 1:
        errors.append(f"trainer id {tid} is fought as {sorted(who)} (one defeated flag for all of them)")

# 5: IVs. Veldris-owned blocks are the ones a Veldris script fights, plus every block whose id has a Veldris alias or name
veld_ids = set(use)
for n in defs:
    if n.startswith(("TRAINER_VELDRIS_", "TRAINER_CRESTFALL_", "TRAINER_HOLLOWBROOK_", "TRAINER_TROGLODYTE")):
        veld_ids.add(resolve(n))
by_id = {}
for n in defs:
    if resolve(n) is not None:
        by_id.setdefault(resolve(n), []).append(n)
for tid, ns in by_id.items():  # a second name for one id is how a reused Hoenn id is kept (CLAUDE.md, 'Reusing a vanilla id')
    if len(ns) > 1 and any(not n.startswith(("TRAINER_PARTNER",)) for n in ns):
        veld_ids.add(tid)
checked = 0
for n, body in zip(names, bodies):
    if resolve(n) in veld_ids:
        checked += 1
        mons = len(re.findall(r"^Level:", body, re.M))
        ivs = len(re.findall(r"^IVs:", body, re.M))
        if mons != ivs:
            errors.append(f"trainers.party: {n} has {mons} Pokemon but {ivs} IVs lines")

for e in errors:
    print("ERROR", e)
print(f"{len(names)} party blocks ({checked} Veldris-owned, IVs checked), {len(use)} Veldris trainer ids in scripts, {len(errors)} error(s)")
sys.exit(1 if errors else 0)
