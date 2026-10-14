#!/usr/bin/env python3
"""Poke a story var and watch the game react: Mom's wake-up scene is gated by VAR_HOLLOWBROOK_STATE (design/running-shoes.md)."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check, check_eq

HOUSE_1F = "MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F"


@testkit.test("Mom's scene only fires while VAR_HOLLOWBROOK_STATE is 0")
def mom_scene_gated_by_state(emu):
    g = emu.game
    # 1. Pretend the scene already happened: stepping on the trigger tile (10,2) must do nothing.
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)
    g.warp(HOUSE_1F, 10, 3)
    ok, _ = emu.walk("U")
    check(ok and g.player_pos() == (10, 2), "could not step onto the trigger tile (10,2); at %s" % (g.player_pos(),))
    time.sleep(1.0)  # give a wrongly firing trigger time to start
    check(not g.script_running(), "the trigger fired although VAR_HOLLOWBROOK_STATE was 1")
    check(not g.flag_get("FLAG_SYS_B_DASH"), "shoes appeared without the scene")
    # 2. Put the state back to 0 and walk off and on again: now the scene must start and end with the shoes.
    check(emu.walk("D")[0], "could not step back down")
    g.var_set("VAR_HOLLOWBROOK_STATE", 0)
    emu.walk("U")
    g.wait_until(g.script_running, 5, what="Mom's trigger to start a script")
    emu.mash("A", until=lambda: g.overworld_idle() and g.var_get("VAR_HOLLOWBROOK_STATE") != 0, timeout=120)
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 1, "VAR_HOLLOWBROOK_STATE after the scene")
    check(g.flag_get("FLAG_SYS_B_DASH"), "Mom's scene should hand over the Running Shoes (FLAG_SYS_B_DASH)")


if __name__ == "__main__":
    testkit.main()
