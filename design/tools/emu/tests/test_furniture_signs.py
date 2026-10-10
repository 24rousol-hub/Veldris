#!/usr/bin/env python3
"""The player's fridge (filler pass, 2026-10-09): the pet used to stand on its only facing tile, so it could never be read.
The wording is read from the script, not typed here."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from testkit import check

HOUSE_1F = "MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F"
FOLDER = "Hollowbrook_PlayersHouse_1F"


def _press_a_facing(emu, direction):
    emu.face(direction)
    emu.press("A")
    return emu.read_dialogue()


@testkit.test("The player's fridge can be read (the Zigzagoon no longer blocks its only facing tile)")
def fridge_readable(emu):
    g = emu.game
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)
    g.warp(HOUSE_1F, 4, 3)
    shown = _press_a_facing(emu, "U")
    check(shown, "pressing A at (4,3) facing the fridge showed nothing")
    # Whatever the fridge says, it is not Mom or the Zigzagoon: it must come from the fridge script.
    want = facts.script_text(g.L.repo, FOLDER, "Hollowbrook_Text_PlayerFridgeBefore")
    check(want, "could not find Hollowbrook_Text_PlayerFridgeBefore in scripts.inc")
    check(facts.same_text(shown[0], want), "expected the fridge text %r, got %r" % (want[:40], shown[0][:40]))


if __name__ == "__main__":
    testkit.main()
