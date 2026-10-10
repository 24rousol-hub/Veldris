#!/usr/bin/env python3
"""Hollowbrook story gates (review fixes, 2026-10-09): the town's east exit is shut while the player has no starter, and
the lab's whole 4-tile doorway runs the Troglodyte scene (states 0 and 1) or the exit blocker (state 2).
See design/interiors.md and design/flags.md (VAR_HOLLOWBROOK_STATE)."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check, check_eq

TOWN = "MAP_HOLLOWBROOK"
LAB = "MAP_HOLLOWBROOK_PROF_FENNICK_LAB"


@testkit.test("Hollowbrook east exit is gated until the player has a starter")
def east_exit_gate(emu):
    g = emu.game
    # State 1 (Mom woke the player, no starter yet): stepping onto (30,10) must start the gate script and push back.
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)
    g.warp(TOWN, 29, 10)
    ok, _ = emu.walk("R")
    check(ok, "could not step east from (29,10); at %s" % (g.player_pos(),))
    g.wait_until(g.script_running, 5, what="the east gate script to start")
    emu.mash("A", until=lambda: g.overworld_idle(), timeout=60)
    check_eq(g.map_name(), TOWN, "map after the gate")
    check(g.player_pos()[0] <= 29, "player was not pushed back from the exit: at %s" % (g.player_pos(),))
    # State 4 (starter chosen and Troglodyte beaten outside): the same step must not trigger anything. (State 3 would start
    # Troglodyte's own scene outside the lab, which is a different trigger.)
    g.var_set("VAR_HOLLOWBROOK_STATE", 4)
    g.warp(TOWN, 29, 10)
    emu.walk("R")
    time.sleep(1.0)
    check(not g.script_running(), "the gate fired although VAR_HOLLOWBROOK_STATE was 4")
    check_eq(g.player_pos()[0], 30, "x after stepping east at state 4")


@testkit.test("Lab: both side tiles of the doorway row start the Troglodyte scene")
def lab_side_triggers(emu):
    g = emu.game
    for x, step in ((5, "D"), (8, "D")):
        g.var_set("VAR_HOLLOWBROOK_STATE", 1)
        g.warp(LAB, x, 9)
        ok, _ = emu.walk(step)
        check(ok, "could not step onto (%d,10); at %s" % (x, g.player_pos()))
        g.wait_until(g.script_running, 5, what="the lab scene to start from x=%d" % x)
        # The scene sets state 2 near its start (before the apology), which is the proof that it ran.
        emu.mash("A", until=lambda: g.var_get("VAR_HOLLOWBROOK_STATE") == 2, timeout=60)
        check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 2, "state after the scene from x=%d" % x)
        emu.mash("A", until=lambda: g.overworld_idle(), timeout=90)  # let the scene finish so the next warp starts clean


@testkit.test("Lab: the exit is blocked at state 2")
def lab_exit_blocker(emu):
    g = emu.game
    g.var_set("VAR_HOLLOWBROOK_STATE", 2)
    g.warp(LAB, 6, 10)
    emu.walk("D")
    g.wait_until(g.script_running, 5, what="the exit blocker to start")
    emu.mash("A", until=lambda: g.overworld_idle(), timeout=60)
    check_eq(g.map_name(), "MAP_HOLLOWBROOK_PROF_FENNICK_LAB", "map after trying to leave at state 2")


def _heal_map(g):
    """(mapGroup, mapNum) of gSaveBlock1Ptr->lastHealLocation, i.e. where a white-out would send the player."""
    base = g.sb1() + g.off("SaveBlock1", "lastHealLocation")
    return g.u8(base + g.off("WarpData", "mapGroup")), g.u8(base + g.off("WarpData", "mapNum"))


@testkit.test("Respawn point: set once at the start, and walking into Hollowbrook does not overwrite a later one")
def respawn_not_reset(emu):
    g = emu.game
    town = g.L.const(TOWN)
    check_eq(_heal_map(g), (town >> 8, town & 0xFF), "heal location at the start of a new game")
    # Pretend a Pokemon Center in Crestfall became the respawn point, then enter the town again (its OnTransition runs).
    crestfall = g.L.const("MAP_CRESTFALL")
    base = g.sb1() + g.off("SaveBlock1", "lastHealLocation")
    g.gdb.write(base + g.off("WarpData", "mapGroup"), bytes([crestfall >> 8]))
    g.gdb.write(base + g.off("WarpData", "mapNum"), bytes([crestfall & 0xFF]))
    g.var_set("VAR_HOLLOWBROOK_STATE", 4)
    g.warp(TOWN, 9, 21)
    time.sleep(0.5)
    check_eq(_heal_map(g), (crestfall >> 8, crestfall & 0xFF), "heal location after entering Hollowbrook")


if __name__ == "__main__":
    testkit.main()
