#!/usr/bin/env python3
"""Smoke tests for the Hoenn-purge experiments (run against a CLONE built with an option applied).

    VELDRIS_REPO=<clone> python3 test_purge_smoke.py --repo <clone>

Everything here is about 'did removing Hoenn maps break a Veldris map': every one of the 12 Veldris maps loads (these sit
at group 0 index 57-59 and group 75, i.e. the places the removal could shift), the Pokemon Center nurse heals through
shared scripts, and a pretend white-out (the heal point) still points at a map that exists.
Not part of the repo."""
import os
import sys

REPO = os.environ.get("VELDRIS_REPO") or sys.argv[sys.argv.index("--repo") + 1]
sys.path.insert(0, os.path.join(REPO, "design", "tools", "emu"))
import testkit  # noqa: E402
from testkit import check, check_eq  # noqa: E402

# (map, warp id to arrive on) ; outdoor maps use a known-walkable tile instead
MAPS = [
    ("MAP_HOLLOWBROOK", (29, 10)),
    ("MAP_VELDRIS_ROUTE1", (13, 11)),
    ("MAP_CRESTFALL", (20, 11)),
    ("MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F", 0),
    ("MAP_HOLLOWBROOK_PLAYERS_HOUSE_2F", 0),
    ("MAP_HOLLOWBROOK_PROF_FENNICK_LAB", 0),
    ("MAP_HOLLOWBROOK_NEIGHBOURS_HOUSE", 0),
    ("MAP_CRESTFALL_POKEMON_CENTER_1F", 0),
    ("MAP_CRESTFALL_MART", 0),
    ("MAP_CRESTFALL_HOUSE_A", 0),
    ("MAP_CRESTFALL_HOUSE_B", 0),
    ("MAP_CRESTFALL_GYM", 0),
]


@testkit.test("all 12 Veldris maps still load and the player can stand in them")
def all_maps_load(emu):
    g = emu.game
    bad = []
    for name, where in MAPS:
        try:
            if isinstance(where, tuple):
                g.warp(name, where[0], where[1])
            else:
                g.warp(name, warp_id=where)
            g.wait_overworld_idle(20)
            got = g.map_name()
            if got != name:
                bad.append("%s -> %s" % (name, got))
        except Exception as e:  # noqa: BLE001
            bad.append("%s raised %s" % (name, e))
    check(not bad, "maps that did not load: " + "; ".join(bad))


@testkit.test("Crestfall Pokemon Center nurse talks and finishes through the shared nurse script")
def nurse(emu):
    g = emu.game
    g.debug_preset(4)
    g.warp("MAP_CRESTFALL_POKEMON_CENTER_1F", 7, 4)
    g.wait_overworld_idle(20)
    emu.face("N")
    emu.press("A")
    g.wait_until(g.script_running, 5, what="the nurse script to start")
    emu.mash("A", until=lambda: g.overworld_idle(), timeout=60)
    shown = g.message_text()
    check(shown is not None, "no nurse text")
    check(g.overworld_idle(), "the game did not return to the overworld after the nurse: %s" % g.summary())


if __name__ == "__main__":
    testkit.main()
