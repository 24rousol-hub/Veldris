#!/usr/bin/env python3
"""Crestfall's townsfolk (placed 2026-10-13, design/crestfall.md 'Townsfolk'): every one says the right line before and
after the story moves on.

Two passes over the town, the Center and House A: 'before' (VAR_CRESTFALL_STATE 0, no badge) and 'after' (state 1,
FLAG_BADGE01_GET set). For each NPC the robot walks up, presses A and compares the first box with the label's text in
scripts.inc, so rewording a line does not break the test, but a script that picks the wrong line does.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from testkit import check

# (map, folder, tile, label before, label after)
NPCS = [
    ("MAP_CRESTFALL", "Crestfall", (20, 21), "Crestfall_Text_Farmhand", "Crestfall_Text_FarmhandAfter"),
    ("MAP_CRESTFALL", "Crestfall", (24, 21), "Crestfall_Text_OldFarmer", "Crestfall_Text_OldFarmerAfter"),
    ("MAP_CRESTFALL", "Crestfall", (19, 18), "Crestfall_Text_PondKid", "Crestfall_Text_PondKidAfter"),
    ("MAP_CRESTFALL", "Crestfall", (3, 17), "Crestfall_Text_HardHatKid", "Crestfall_Text_HardHatKid"),
    ("MAP_CRESTFALL", "Crestfall", (28, 17), "Crestfall_Text_CommonsFan", "Crestfall_Text_CommonsFanAfter"),
    ("MAP_CRESTFALL", "Crestfall", (12, 17), "Crestfall_Text_Sceptic", "Crestfall_Text_ScepticAfter"),
    ("MAP_CRESTFALL", "Crestfall", (27, 6), "Crestfall_Text_Traveller", "Crestfall_Text_TravellerAfter"),
    ("MAP_CRESTFALL", "Crestfall", (23, 15), "Crestfall_Text_Fisherman", "Crestfall_Text_Fisherman"),
    ("MAP_CRESTFALL_HOUSE_A", "Crestfall_HouseA", (3, 5), "Crestfall_HouseA_Text_Wife", "Crestfall_HouseA_Text_WifeAfter"),
    ("MAP_CRESTFALL_POKEMON_CENTER_1F", "Crestfall_PokemonCenter_1F", (3, 5),
     "Crestfall_PokemonCenter_1F_Text_CommonsVisitor", "Crestfall_PokemonCenter_1F_Text_CommonsVisitor"),
]


def run_pass(emu, after):
    g = emu.game
    g.debug_preset(4)
    g.var_set("VAR_CRESTFALL_STATE", 1 if after else 0)
    (g.flag_set if after else g.flag_clear)("FLAG_BADGE01_GET")
    for map_name, folder, tile, before_label, after_label in NPCS:
        # NPCs only exist near the player, so arrive on the tile just above (outdoors; right of the fisherman, whose
        # upper tile is the pond's edge) or at the door (indoors)
        if map_name == "MAP_CRESTFALL":
            g.warp(map_name, tile[0] + (1 if tile == (23, 15) else 0), tile[1] - (0 if tile == (23, 15) else 1))
        else:
            g.warp(map_name, warp_id=0)
        label = after_label if after else before_label
        want = facts.script_text(g.L.repo, folder, label)
        check(want, "no %s in %s/scripts.inc" % (label, folder))
        shown = emu.talk_to(tile)
        check(shown, "%s at %s said nothing" % (label, tile))
        check(facts.same_text(shown[0], want), "%s at %s: expected %r, the game showed %r" % (label, tile, want[:40], shown[0][:40]))
        check(g.overworld_idle(), "the player should be free after talking to %s" % (tile,))


@testkit.test("Crestfall townsfolk: the line before the scheme and the badge")
def townsfolk_before(emu):
    run_pass(emu, after=False)


@testkit.test("Crestfall townsfolk: the line after the scheme and the badge")
def townsfolk_after(emu):
    run_pass(emu, after=True)


if __name__ == "__main__":
    testkit.main()
