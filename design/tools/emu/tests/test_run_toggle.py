#!/usr/bin/env python3
"""L flips FLAG_SYS_RUN_BY_DEFAULT, but only once the Running Shoes (FLAG_SYS_B_DASH) are owned (src/veldris_run.c)."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check

RUN = "FLAG_SYS_RUN_BY_DEFAULT"
SHOES = "FLAG_SYS_B_DASH"


@testkit.test("L toggles run-by-default only after the shoes")
def run_toggle(emu):
    g = emu.game
    check(g.flag_get(RUN) and not g.flag_get(SHOES), "new game should start with run on and no shoes")
    # no shoes: L does nothing (but make sure the game really saw the key, or this check proves nothing)
    check(emu.press("L"), "the game never saw the L key")
    time.sleep(0.5)
    check(g.flag_get(RUN), "L flipped the run flag before the shoes were given")
    # give the shoes (poke the flag) and press L: run turns off, then back on
    g.flag_set(SHOES)
    emu.press_until("L", lambda: not g.flag_get(RUN))
    emu.press_until("L", lambda: g.flag_get(RUN))
    # take the shoes away again: L is dead again
    g.flag_clear(SHOES)
    check(emu.press("L"), "the game never saw the L key")
    time.sleep(0.5)
    check(g.flag_get(RUN), "L flipped the run flag after the shoes were removed")


if __name__ == "__main__":
    testkit.main()
