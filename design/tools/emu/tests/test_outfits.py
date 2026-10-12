#!/usr/bin/env python3
"""Player outfits (design/player-customization.md): every outfit and gender uses its own sprite for each pose.

For Emerald (recoloured), Ruby/Sapphire and Diamond/Pearl, as Brendan and as May, at Crestfall's pond:
* Surf: the Cut/Surf pose, then surfing (both go through GetPlayerAvatarGraphicsIdByStateIdAndGender).
* Mach Bike and Acro Bike, used with SELECT (registeredItem is poked, so no bag menu driving).
* Old Rod, cast at the pond.
* The Costume Box with SELECT opens the picker.
The expected sprite for each pose comes from the OBJ_EVENT_GFX_VELDRIS_* / OBJ_EVENT_GFX_BRENDAN_* constants, so the
test follows the outfit tables. Underwater (Dive) is not tested: every outfit uses Emerald's sprite there on purpose.
"""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check

# VAR_VELDRIS_LOOK: bits 0-1 outfit, then skin, hair, top, accent (3 bits each). "EM" uses non-default colours.
LOOKS = {"EM": 0 | (4 << 2) | (2 << 5) | (1 << 8) | (3 << 11), "RS": 1, "DP": 2}
POND_EDGE = (18, 13)   # walk down one tile to (18,14): the pond is below


def expected(g, look, gender, state):
    if look == "EM":
        return g.L.const("OBJ_EVENT_GFX_%s_%s" % ("BRENDAN" if gender == 0 else "MAY", state))
    return g.L.const("OBJ_EVENT_GFX_VELDRIS_%s_%s_%s" % (look, "M" if gender == 0 else "F", state))


def watch(g, emu, seconds, press_a=False):
    """Player sprite ids seen over `seconds` (pressing A now and then to get through prompts)."""
    gid = lambda: g.u16(g._player_object() + g.off("ObjectEvent", "graphicsId"))
    seen, t0, last_a = set(), time.time(), 0.0
    while time.time() - t0 < seconds:
        seen.add(gid())
        if press_a and time.time() - last_a > 0.5:
            emu.press("A"); last_a = time.time()
    return seen


@testkit.test("outfits: each outfit and gender uses its own sprite for surf, bikes and fishing", slow=True, timeout=900)
def outfits(emu):
    g = emu.game
    g.debug_preset(4)
    # All badges, plus the Swampert and Tropius test dummies (Swampert is the Surf learner; they are debug-menu dummies, not
    # starters and not tied to the starter choice); the script ends with a message.
    g.run_rom_script("Veldris_Debug_Preset8")
    for _ in range(30):
        time.sleep(0.5)
        if not g.script_running() and g.overworld_idle():
            break
        emu.press("A")
    op = g._op
    code = b""
    for item in ("ITEM_MACH_BIKE", "ITEM_ACRO_BIKE", "ITEM_OLD_ROD"):
        code += bytes([op("SCR_OP_ADDITEM")]) + g.L.const(item).to_bytes(2, "little") + (1).to_bytes(2, "little")
    g.run_script(code + bytes([op("SCR_OP_END")]), wait_done=True)
    reg = g.off("SaveBlock1", "registeredItem")
    gender_off = g.off("SaveBlock2", "playerGender")

    def select(item):
        g.wait_overworld_idle()
        g.gdb.put_u16(g.sb1() + reg, g.L.const(item))
        emu.press("SELECT")

    for gender in (0, 1):
        for look in ("EM", "RS", "DP"):
            who = "%s %s" % (look, "Brendan" if gender == 0 else "May")
            g.gdb.put_u8(g.sb2() + gender_off, gender)
            g.var_set("VAR_VELDRIS_LOOK", LOOKS[look])
            # bikes
            g.warp("MAP_CRESTFALL", 18, 11)
            for item, state in (("ITEM_MACH_BIKE", "MACH_BIKE"), ("ITEM_ACRO_BIKE", "ACRO_BIKE")):
                select(item)
                seen = watch(g, emu, 1.5)
                check(expected(g, look, gender, state) in seen, "%s: %s sprite never shown (saw %s)" % (who, state, sorted(seen)))
                select(item)                       # get off again
                time.sleep(1.0)
            # fishing
            g.warp("MAP_CRESTFALL", *POND_EDGE); emu.walk("D"); emu.press("DOWN"); time.sleep(0.3)
            select("ITEM_OLD_ROD")
            seen = watch(g, emu, 2.0)
            check(expected(g, look, gender, "FISHING") in seen, "%s: fishing sprite never shown (saw %s)" % (who, sorted(seen)))
            for _ in range(10):
                if g.overworld_idle() and not g.script_running():
                    break
                emu.press("A"); time.sleep(0.5)
            # surf (starts with the Cut/Surf pose)
            g.warp("MAP_CRESTFALL", *POND_EDGE); emu.walk("D"); emu.press("DOWN"); time.sleep(0.3)
            seen = watch(g, emu, 6.0, press_a=True)
            for state in ("FIELD_MOVE", "SURFING"):
                check(expected(g, look, gender, state) in seen, "%s: %s sprite never shown (saw %s)" % (who, state, sorted(seen)))
            for _ in range(10):
                if g.overworld_idle() and not g.script_running():
                    break
                emu.press("A"); time.sleep(0.5)

    # the Costume Box from SELECT opens the picker
    g.var_set("VAR_VELDRIS_LOOK", 0)
    g.warp("MAP_CRESTFALL", 18, 11)
    select("ITEM_COSTUME_BOX")
    g.wait_until(lambda: "Task_LookMenu" in g.task_names(), 5.0, what="the Costume Box picker to open")
    emu.press("B")


if __name__ == "__main__":
    testkit.main()
