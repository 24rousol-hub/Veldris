#!/usr/bin/env python3
"""A brand new game starts with the things the author asked for (design/exp-share.md, running-shoes.md, time-of-day.md)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check, check_eq


@testkit.test("new game defaults")
def new_game_defaults(emu):
    g = emu.game
    check_eq(g.map_name(), "MAP_HOLLOWBROOK_PLAYERS_HOUSE_2F", "start map")
    check_eq(g.player_pos(), (2, 4), "start tile")
    # Exp. Share is in the bag (Key Items) and switched on
    check_eq(g.bag_count("ITEM_EXP_SHARE"), 1, "Exp. Share in the bag")
    check_eq(g.bag_where("ITEM_EXP_SHARE"), "keyItems", "pocket holding the Exp. Share")
    check(g.flag_get("FLAG_SYS_EXP_SHARE_ON"), "FLAG_SYS_EXP_SHARE_ON should start set")
    # running: switched on by default, but the shoes themselves come from Mom
    check(g.flag_get("FLAG_SYS_RUN_BY_DEFAULT"), "FLAG_SYS_RUN_BY_DEFAULT should start set")
    check(not g.flag_get("FLAG_SYS_B_DASH"), "the Running Shoes must not be owned before Mom's scene")
    # the fake clock starts at 10:00 on a running clock (it ticks, so allow a little drift)
    check(g.flag_get("FLAG_SYS_CLOCK_SET"), "FLAG_SYS_CLOCK_SET should start set")
    c = g.clock()
    check(c["hour"] == 10 and c["minute"] < 30, "fake clock should read about 10:00, got %02d:%02d" % (c["hour"], c["minute"]))
    # story and party start empty
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 0, "VAR_HOLLOWBROOK_STATE")
    check_eq(len(g.party()), 0, "party size")


if __name__ == "__main__":
    testkit.main()
