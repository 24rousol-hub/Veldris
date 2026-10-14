#!/usr/bin/env python3
"""The wall clock in the player's room (design/time-of-day.md): the stopped-clock branch is only reachable by clearing
FLAG_SYS_CLOCK_SET, which a new game never does, so it was never run by hand. This test clears the flag with a poke,
reads the message the game actually put on screen, and goes through the YES branch to the set screen and back.
"""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check

CLOCK_SET = "FLAG_SYS_CLOCK_SET"


def press_clock(emu, expect):
    """Press A at the wall clock and wait until the game shows a message containing `expect` and its YES/NO box."""
    g = emu.game
    emu.press("A")
    g.wait_until(lambda: expect in g.message_text() and "Task_HandleYesNoInput" in g.task_names(), 10,
                 what="the message %r with a YES/NO box (last text: %r)" % (expect, g.message_text()))


@testkit.test("wall clock: running, stopped, and set again")
def wall_clock(emu):
    g = emu.game
    check(emu.walk_to(3, 2), "could not walk to the tile below the wall clock, at %s" % (g.player_pos(),))
    check(g.player_facing() == "N", "should be facing the wall")
    # 1. A new game has a running clock: the game offers to reset it. NO shows the clock face; B leaves it.
    press_clock(emu, "keeps its own")
    emu.press("B")  # B on the YES/NO box answers NO: the clock face opens
    g.wait_until(lambda: g.callback2() == "CB2_WallClock", 20, what="the clock face to open")
    emu.mash("B", until=g.overworld_idle, timeout=60)  # B closes it again
    check(g.flag_get(CLOCK_SET), "looking at a running clock must not stop it")
    # 2. Stop the clock (flag poke): the game now offers to start it. NO leaves it stopped.
    g.flag_clear(CLOCK_SET)
    press_clock(emu, "has stopped")
    emu.press("B")  # NO
    g.wait_until(g.overworld_idle, 20, what="the game to be idle after NO")
    check(not g.flag_get(CLOCK_SET), "answering NO must leave the clock stopped")
    # 3. Ask again and say YES: the set screen opens; A accepts the time it shows; the clock runs again.
    press_clock(emu, "has stopped")
    emu.press("A")  # YES (the cursor starts on YES)
    # The set screen: A accepts hour and minute as shown, then asks 'Is this the correct time?' with the cursor on NO,
    # so UP moves it to YES. Keep going until the game is back in the room and says the clock is ticking.
    end = time.time() + 90
    while not (g.overworld_idle() and "ticking" in g.message_text()):
        check(time.time() < end, "the set-clock screen did not finish. %s" % g.summary())
        if "Task_SetClock_HandleConfirmInput" in g.task_names():
            emu.press("UP")
        emu.press("A")
        time.sleep(0.3)
    check(g.flag_get(CLOCK_SET), "FLAG_SYS_CLOCK_SET should be set after the set screen")


if __name__ == "__main__":
    testkit.main()
