#!/usr/bin/env python3
"""Talking to an NPC: the emulator walks up to Mom, presses A and writes down what the game showed.

Two checks on the player's house (design/running-shoes.md). The wording is never typed into the test: it is read from
data/maps/Hollowbrook_PlayersHouse_1F/scripts.inc, so rewriting a line does not break anything, but a script that
picks the wrong line for the story state does.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from testkit import check, check_eq

HOUSE_1F = "MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F"
FOLDER = "Hollowbrook_PlayersHouse_1F"
MOM = "LOCALID_HOLLOWBROOK_MOM"


@testkit.test("Mom picks her line from the story state")
def mom_line_follows_state(emu):
    g = emu.game
    repo = g.L.repo
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)  # scene done, Pokemon not chosen yet: she sends you to the lab
    g.warp(HOUSE_1F, warp_id=1)  # arrive from the stairs
    shown = emu.talk_to(MOM)
    want = facts.script_text(repo, FOLDER, "Hollowbrook_Text_MomIdleBefore")
    check(want, "could not find Hollowbrook_Text_MomIdleBefore in scripts.inc")
    check(shown, "Mom said nothing")
    check(facts.same_text(shown[0], want), "state 1: expected %r, the game showed %r" % (want[:40], shown[0][:40]))
    check(g.overworld_idle(), "the player should be free after the conversation")


@testkit.test("Mom's talk path hands over the Running Shoes (no walk-up scene)")
def mom_talk_path_gives_shoes(emu):
    g = emu.game
    repo = g.L.repo
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 0, "new game state")
    check(not g.flag_get("FLAG_SYS_B_DASH"), "no shoes yet in a new game")
    # The stairs open next to the trigger tile (10,2), which starts the walk-up scene while the state is 0. So walk
    # to Mom with the state at 1 (the trigger is dead then) and put the state back to 0 just before pressing A.
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)
    g.warp(HOUSE_1F, warp_id=1)
    emu.approach(MOM)
    g.var_set("VAR_HOLLOWBROOK_STATE", 0)
    emu.press("A")
    shown = emu.read_dialogue()
    want = facts.script_text(repo, FOLDER, "Hollowbrook_Text_MomWakeUp")
    check(shown and facts.same_text(shown[0], want), "state 0: expected the wake-up line %r, got %r" % (want[:40], shown[:1]))
    check(g.flag_get("FLAG_SYS_B_DASH"), "talking to Mom at state 0 should hand over the Running Shoes")
    check(g.flag_get("FLAG_SYS_RUN_BY_DEFAULT"), "run-by-default should be on after the gift")
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 1, "VAR_HOLLOWBROOK_STATE after Mom's scene")
    check(len(shown) >= 3, "expected the wake-up line, the gift and the instructions; the game showed %d messages" % len(shown))


if __name__ == "__main__":
    testkit.main()
