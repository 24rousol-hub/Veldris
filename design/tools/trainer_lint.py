#!/usr/bin/env python3
"""Trainer-id reuse lint (proposed hack tool). Run from the repo root: python3 design/tools/trainer_lint.py

Checks, in order:
 1. every '=== TRAINER_X ===' header in src/data/trainers.party is a PRIMARY name (a #define with a number)
 2. no two Veldris script fights resolve to the same trainer id (they would share one defeated flag)
 3. every TRAINER_TROGLODYTE_* used by a map script has a row in VELDRIS_TROGLODYTE_FIGHTS (include/veldris_journal.h)
 4. no trainerbattle_earlyrival uses a TROGLODYTE id (it sets the defeated flag on a LOSS)
 5. every Pokemon in a Veldris-owned block has an IVs line (a missing line means 31)
 6. every Veldris-owned block's AI: line uses only the allowed flags (no Smart Trainer, Prediction, Omniscient and so on)
 7. the 16 ladder trainers carry exactly the rung in LADDER below (flag order and case do not matter; bundles are not expanded)
 8. every Veldris-owned block has an AI: line (no line means no flags, so every move scores the same and play is random)
 9. no TRAINER_TROGLODYTE* block carries Ace Pokemon (his party order is random, so the flag would hold back a random Pokemon)
"""
import re, sys, glob, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_BASE = "d946dc6515e11b0aa85d2e11824eceb31e8cff1a"  # design/engine-edits.md, 'Upstream baseline'

# The AI ladder. The author asked on 2026-10-12 for a 'short AI ladder weak to better but not crazy good'; the rungs and who
# stands on which are my applied reading of that, and stay changeable. LADDER is the one machine-checked table;
# design/ai-ladder.md explains it. Dim, Basic and Sharp are the three rungs. Leaders 3 to 9, the Elite Four and Cynthia add
# Ace Pokemon. Troglodyte never does (his party order is random). Greta and Hachimel are pinned at Basic (no Ace). Greta's
# two gym trainers and the Route 1 trio are not in the table: they stay as built (Basic or Check Bad Move) and only the
# allowed-set check below applies to them. To move someone, edit this table, their AI: line and test/veldris.c together.
DIM = "Check Bad Move"
BASIC = "Basic Trainer"
SHARP = "Basic Trainer / Hp Aware / Try To 2hko"
ACE = " / Ace Pokemon"
LADDER = {
    "TRAINER_TROGLODYTE_HOLLOWBROOK": DIM,
    "TRAINER_TROGLODYTE_CRESTFALL": DIM,
    "TRAINER_CRESTFALL_GRETA": BASIC,
    "TRAINER_HACHIMEL": BASIC,
    "TRAINER_SANZUFORD": BASIC + ACE,
    "TRAINER_HAGANE": SHARP + ACE,
    "TRAINER_WAKASAGI": SHARP + ACE,
    "TRAINER_TOBIN": SHARP + ACE,
    "TRAINER_ASEBY": SHARP + ACE,
    "TRAINER_SUZURAN": SHARP + ACE,
    "TRAINER_MIZZLE": SHARP + ACE,
    "TRAINER_OSSIAN": SHARP + ACE,
    "TRAINER_HYACINTH": SHARP + ACE,
    "TRAINER_DRAYDEN": SHARP + ACE,
    "TRAINER_DUNMORE": SHARP + ACE,
    "TRAINER_CYNTHIA": SHARP + ACE,
}
# Every Veldris-owned block may use only these flags ('not crazy good'). SMART_AI adds nothing to the rule: it only gives the
# likely slips a clearer message. A smarter rung later means editing these two lists on purpose.
ALLOWED_AI = "Check Bad Move / Basic Trainer / Check Viability / Try To Faint / Hp Aware / Try To 2hko / Ace Pokemon"
SMART_AI = ("Smart Trainer / Prediction / Predict Switch / Predict Incoming Mon / Predict Move / Omniscient / "
            "Know Opponent Party / Smart Switching / Smart Mon Choices")


def ai_flags(line):
    """'Basic Trainer / hp aware' -> {'BASIC_TRAINER', 'HP_AWARE'}: the names trainerproc builds, so order and case do not matter."""
    out = set()
    for f in line.split("/"):
        f = f.strip()
        if f.startswith("AI_FLAG_"):  # trainerproc keeps a written-out constant as it is
            f = f[len("AI_FLAG_"):]
        if f:
            out.add(re.sub(r"[^0-9A-Za-z]", "_", f).upper())
    return out


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

# 6 + 7: AI ladder. Read the AI: lines on their own (with line numbers) so a message can say where to look
ai_lines, cur = {}, None
for ln, line in enumerate(party.split("\n"), 1):
    m = re.match(r"=== (TRAINER_\w+) ===\s*$", line)
    if m:
        cur = m.group(1)
        continue
    m = re.match(r"AI:\s*(.*?)\s*$", line)
    if m and cur:
        ai_lines.setdefault(cur, []).append((ln, m.group(1)))
allowed, smart = ai_flags(ALLOWED_AI), ai_flags(SMART_AI)
defined = set(re.findall(r"^#define\s+AI_FLAG_(\w+)", (ROOT / "include/constants/battle_ai.h").read_text(), re.M))
for line in [ALLOWED_AI, SMART_AI, *LADDER.values()]:  # a typo in a table would make a check pass or fail for the wrong reason
    for f in ai_flags(line) - defined:
        errors.append(f"trainer_lint.py: '{f}' (in '{line}') is not an AI_FLAG_* in include/constants/battle_ai.h")
for n in LADDER:
    if n not in names:
        errors.append(f"trainer_lint.py: LADDER lists {n}, which has no '=== {n} ===' block in trainers.party")
for n in names:
    if resolve(n) not in veld_ids:
        continue
    for ln, line in ai_lines.get(n, []):
        for f in sorted(ai_flags(line) - allowed):
            why = "a smart flag ruled out by 'not crazy good'" if f in smart else "not in the allowed set"
            errors.append(f"trainers.party:{ln}: {n} has 'AI: {line}', and {f} is {why}; allowed are '{ALLOWED_AI}'"
                          " (a smarter rung needs an explicit edit of ALLOWED_AI in design/tools/trainer_lint.py)")
for n in names:
    if resolve(n) in veld_ids and not ai_lines.get(n):
        errors.append(f"trainers.party: {n} has no AI: line (no line means no flags, so its moves would be random)")
    if n.startswith("TRAINER_TROGLODYTE") and "ACE_POKEMON" in {f for _, line in ai_lines.get(n, []) for f in ai_flags(line)}:
        errors.append(f"trainers.party: {n} has Ace Pokemon; Troglodyte never gets it (his party order is random)")
for n, want in LADDER.items():
    found = ai_lines.get(n, [])
    if len(found) != 1:
        errors.append(f"trainers.party: {n} has {len(found)} AI lines, the ladder expects exactly one: 'AI: {want}'")
    elif ai_flags(found[0][1]) != ai_flags(want):
        errors.append(f"trainers.party:{found[0][0]}: {n} has 'AI: {found[0][1]}' but the ladder expects 'AI: {want}'")

for e in errors:
    print("ERROR", e)
print(f"{len(names)} party blocks ({checked} Veldris-owned, IVs and AI lines checked), {len(use)} Veldris trainer ids in scripts, "
      f"{len(LADDER)} ladder trainers, {len(errors)} error(s)")
sys.exit(1 if errors else 0)
