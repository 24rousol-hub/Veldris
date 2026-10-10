#!/usr/bin/env python3
"""Static check for walk-up NPCs (see design/npc-walkup.md). OPTIONAL: not wired into any hook.

A 'walker' is an object event with trainer_type NORMAL or SEE_ALL_DIRECTIONS whose script does not start with a
trainerbattle (after leading flag checks). The game lets such an NPC spot the player, walk up and run the script
(src/trainer_see.c). The three traps that a map.json plus scripts.inc can show by themselves:

  ERROR  the NPC has no way to stop (no cant_see_if_*, no goto_if_set/unset guard, no hide flag):
         he walks up and talks every time the player is in his line
  ERROR  the guard's 'done' label starts with something visible (msgbox, lock, ...): the same endless loop
  ERROR  a coord_event tile lies inside his sight line: the first step onto it is taken over by the NPC, so the
         cutscene is skipped (tested). A warp tile there is only a WARN (same code path, not run)
  WARN   sight range longer than what the screen shows (7 sideways, 4 down, 5 up), so the '!' can start off screen,
         or movement_type is not FACE_* (the line follows his facing)

Usage:  python3 design/tools/walkup_lint.py [repo root]       exit code 1 if there is any ERROR
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
FACE = {"MOVEMENT_TYPE_FACE_UP": (0, -1), "MOVEMENT_TYPE_FACE_DOWN": (0, 1),
        "MOVEMENT_TYPE_FACE_LEFT": (-1, 0), "MOVEMENT_TYPE_FACE_RIGHT": (1, 0)}
ALL4 = list(FACE.values())
# commands that never show anything or change the save (the game's look-ahead runs straight through them)
QUIET = ("checkflag", "compare", "goto_if", "cant_see", "nop")

errors, warns = [], []


def label_body(text, label):
    """Command lines of `label` up to the next global label, comments and blanks removed. None if not found."""
    m = re.search(r"^%s::?\s*$" % re.escape(label), text, re.M)
    if not m:
        return None
    out = []
    for line in text[m.end():].splitlines():
        if re.match(r"^\w+::", line):
            break
        line = line.split("@")[0].strip()
        if line and not line.endswith(":") and not line.startswith("."):
            out.append(line)
    return out


def first_effect(lines):
    """(first command that shows something or writes the save, the guards before it).

    'end' counts as quiet-and-final (the look-ahead sees an NPC that does nothing). An unconditional goto cannot be
    followed here, so it returns '?'."""
    guards = []
    for ln in lines:
        cmd = ln.split()[0]
        if cmd == "end":
            return "end", guards
        if cmd == "goto":
            return "?", guards
        if ln.startswith(QUIET):
            if ln.startswith(("cant_see", "goto_if_set", "goto_if_unset", "goto_if_eq", "goto_if_ne")):
                m = re.search(r",\s*(\w+)\s*$", ln)
                guards.append((cmd, m.group(1) if m else None))
            continue
        return cmd, guards
    return None, guards


for mj in sorted((ROOT / "data/maps").glob("*/map.json")):
    m = json.loads(mj.read_text())
    sinc = mj.parent / "scripts.inc"
    if not sinc.exists():
        continue
    text = sinc.read_text(errors="replace")
    steps = {(c["x"], c["y"]): "coord_event" for c in m.get("coord_events", []) if c.get("type") == "trigger"}
    steps.update({(w["x"], w["y"]): "warp" for w in m.get("warp_events", [])})
    for o in m.get("object_events", []):
        if o.get("trainer_type") not in ("TRAINER_TYPE_NORMAL", "TRAINER_TYPE_SEE_ALL_DIRECTIONS"):
            continue
        lines = label_body(text, o["script"])
        if lines is None:
            continue
        cmd, guards = first_effect(lines)
        if cmd == "?" or (cmd and cmd.startswith("trainerbattle")):
            continue  # an ordinary trainer, or a script this check cannot follow
        where = "%s %s (%s)" % (mj.parent.name, o["local_id"], o["script"])
        rng = int(str(o.get("trainer_sight_or_berry_tree_id", "0")), 0)
        has_stop = any(g[0].startswith(("cant_see", "goto_if_set", "goto_if_unset")) for g in guards) \
            or o.get("flag", "0") not in ("0", 0)
        if not has_stop:
            errors.append("%s: no cant_see_if_*, no guard and no hide flag, he will walk up every time" % where)
        for kind, target in guards:
            if kind.startswith("goto_if") and target:
                body = label_body(text, target)
                if body is not None and not any("VAR_LAST_TALKED" in b for b in body):
                    c2, _ = first_effect(body)
                    if c2 not in (None, "end") and not any(g[0].startswith("cant_see") for g in guards):
                        errors.append("%s: the 'done' label %s starts with %r (visible): endless walk-up loop, "
                                      "use cant_see_if_set first" % (where, target, c2))
        # the screen shows 7 tiles left and right, 4 above and 5 below the player; the NPC is created up to
        # 9 left, 10 right, 7 above and 9 below (the '!' can then start off screen)
        shown = {(0, 1): 4, (0, -1): 5, (1, 0): 7, (-1, 0): 7}   # direction the NPC looks -> tiles on screen
        look = ALL4 if o["trainer_type"] == "TRAINER_TYPE_SEE_ALL_DIRECTIONS" else \
            ([FACE[o["movement_type"]]] if o["movement_type"] in FACE else [])
        for d in look:
            if rng > shown[d]:
                warns.append("%s: sight range %d towards %s, only %d tiles are on screen, the '!' may start off screen"
                             % (where, rng, {(0, 1): "down", (0, -1): "up", (1, 0): "right", (-1, 0): "left"}[d], shown[d]))
        dirs = ALL4 if o["trainer_type"] == "TRAINER_TYPE_SEE_ALL_DIRECTIONS" else \
            ([FACE[o["movement_type"]]] if o["movement_type"] in FACE else [])
        if o["trainer_type"] == "TRAINER_TYPE_NORMAL" and o["movement_type"] not in FACE:
            warns.append("%s: movement_type %s is not FACE_*, the sight line follows his facing" % (where, o["movement_type"]))
        for dx, dy in dirs:
            for i in range(1, rng + 1):
                t = (o["x"] + dx * i, o["y"] + dy * i)
                if steps.get(t) == "coord_event":
                    errors.append("%s: a coord_event at %s lies in his sight line (distance %d): the first step onto it is "
                                  "taken over by the NPC and the cutscene does not run (tested)" % (where, t, i))
                elif steps.get(t) == "warp":
                    warns.append("%s: a warp at %s lies in his sight line (distance %d): same code path as a coord_event, "
                                 "so the first step onto it is probably taken over too (not run)" % (where, t, i))

for w in warns:
    print("WARN  " + w)
for e in errors:
    print("ERROR " + e)
print("walk-up lint: %d error(s), %d warning(s)" % (len(errors), len(warns)))
sys.exit(1 if errors else 0)
