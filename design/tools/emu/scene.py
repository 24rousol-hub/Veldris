#!/usr/bin/env python3
"""Look at the game without writing a test: start it, do a few things, print what happened and save pictures.

    python3 design/tools/emu/scene.py preset:4 map shot:start.png
    python3 design/tools/emu/scene.py preset:4 warp:MAP_VELDRIS_ROUTE1,13,11 clock:22:00 map shot:route1.png
    python3 design/tools/emu/scene.py var:VAR_HOLLOWBROOK_STATE=1 warp:MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F,#1 \\
        talk:LOCALID_HOLLOWBROOK_MOM

The game starts as a new game in the bedroom. The steps run in the order given. `python3 scene.py --help` lists them.
Pictures go to /tmp/veldris_emu_shots (change with --out). Nothing here touches the repo or the ROM: a copy runs.
"""
import argparse
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emulator import Emulator  # noqa: E402
from game import GameError  # noqa: E402

STEPS = """steps (words separated by spaces; arguments after a colon):
  preset:N                 debug-menu Scripts preset 1 to 8 (see design/debug-presets.md)
  var:VAR_NAME=VALUE       set a var            flag:FLAG_NAME      set a flag     flag:FLAG_NAME=0   clear it
  warp:MAP_NAME,X,Y        teleport (map tiles)  warp:MAP_NAME,#N    use the map's warp number N (arrive on its door)
  clock:HH:MM              set the fake clock (it keeps ticking, 20 game seconds a second)
  walk:RRUUDL              walk tile by tile (U D L R) at normal speed
  walkto:X,Y               walk to a tile along a path the map allows
  talk:LOCALID_NAME        walk up to an NPC, press A, click through the dialogue and print what it said
  press:BUTTON             hold one button briefly (A B START SELECT L R UP DOWN LEFT RIGHT)
  mash:BUTTON              press it every 0.35 s until the player is free again
  wait:SECONDS             let the game run
  shot:NAME.png            save a picture of the game window
  state                    print where the game is      objects   list the NPCs      map   draw the map as text
  items                    print the bag                party     print the party
  realtime / turbo         switch the game speed (it starts in turbo, about 8 times real time)
"""


def run_step(emu, step, outdir):
    g = emu.game
    name, _, arg = step.partition(":")
    if name == "preset":
        g.debug_preset(int(arg))
    elif name == "var":
        var, _, value = arg.partition("=")
        g.var_set(var, int(value, 0))
    elif name == "flag":
        flag, _, value = arg.partition("=")
        g.flag_set(flag, value not in ("0", "false", "off"))
    elif name == "warp":
        parts = arg.split(",")
        if len(parts) == 2 and parts[1].startswith("#"):
            g.warp(parts[0], warp_id=int(parts[1][1:]))
        else:
            g.warp(parts[0], int(parts[1]), int(parts[2]))
    elif name == "clock":
        hh, _, mm = arg.partition(":")
        g.set_clock(int(hh), int(mm or 0), 0)
    elif name == "walk":
        ok, done = emu.walk(arg)
        print("   walked %d of %d steps%s" % (done, len(arg), "" if ok else " (blocked)"))
    elif name == "walkto":
        x, y = arg.split(",")
        print("   arrived" if emu.walk_to(int(x), int(y)) else "   did not arrive")
    elif name == "talk":
        for i, text in enumerate(emu.talk_to(arg), 1):
            print("   [%d] %s" % (i, text.replace("\\p", "  //  ").replace("\\n", " / ").replace("\\l", " / ")))
    elif name == "press":
        emu.press(arg)
    elif name == "mash":
        emu.mash(arg or "A")
    elif name == "wait":
        time.sleep(float(arg))
    elif name == "shot":
        path = Path(arg) if os.path.isabs(arg) else Path(outdir) / arg
        path.parent.mkdir(parents=True, exist_ok=True)
        print("   picture: %s" % emu.screenshot(path))
    elif name == "state":
        print("   " + g.summary())
        print("   clock %s  flags: run-by-default=%s shoes=%s" % (g.clock() if g.L.has_field("SaveBlock3", "fakeRTC") else "-",
                                                              g.flag_get("FLAG_SYS_RUN_BY_DEFAULT"), g.flag_get("FLAG_SYS_B_DASH")))
    elif name == "objects":
        for o in g.objects():
            print("   local id %-3d at (%d, %d) facing %s%s" % (o["local_id"], o["x"], o["y"], o["facing"], " (hidden)" if o["invisible"] else ""))
    elif name == "map":
        print(g.ascii_map())
    elif name == "items":
        for pocket, items in g.bag().items():
            print("   %-9s %s" % (pocket, ", ".join("%s x%d" % (k, v) for k, v in items.items()) or "-"))
    elif name == "party":
        for m in g.party():
            print("   %-18s L%-3d HP %d/%d  %s" % (m["species"], m["level"], m["hp"], m["max_hp"], ", ".join(m["moves"])))
    elif name == "realtime":
        emu.turbo(False)
    elif name == "turbo":
        emu.turbo(True)
    else:
        raise GameError("unknown step %r (run with --help)" % step)


def main():
    ap = argparse.ArgumentParser(description=__doc__, epilog=STEPS, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("steps", nargs="*", help="what to do, in order (see below)")
    ap.add_argument("--out", default="/tmp/veldris_emu_shots", help="folder for pictures (default %(default)s)")
    ap.add_argument("--title", action="store_true", help="stop at the title screen instead of starting a new game")
    ap.add_argument("--rom", help="ROM to run (default: pokeemerald.gba in the repo)")
    ap.add_argument("--repo", help="repo root (default: found from this file, or $VELDRIS_REPO)")
    args = ap.parse_args()
    t0 = time.time()
    with Emulator(rom=args.rom, repo=args.repo) as emu:
        emu.boot_to_title()
        if not args.title:
            emu.quickstart()
        print("game ready after %.1f s: %s" % (time.time() - t0, emu.game.summary()))
        for step in args.steps:
            print("> " + step)
            try:
                run_step(emu, step, args.out)
            except Exception as e:  # show what went wrong and where the game was, keep the picture
                print("   FAILED: %s: %s" % (type(e).__name__, e))
                try:
                    print("   picture: %s" % emu.screenshot(Path(args.out) / "failed.png"))
                except Exception:
                    pass
                return 1
        print("done in %.1f s" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
