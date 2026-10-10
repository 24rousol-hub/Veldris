#!/usr/bin/env python3
"""Checks on the test harness itself: memory reads and writes, flag and var maths, party decoding, script injection.

If one of these fails, the harness (or the build layout) is wrong, not the game.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from testkit import check, check_eq


@testkit.test("harness: memory read, write and the game keeps running", boot="title")
def memory_roundtrip(emu):
    g = emu.game
    gdb = g.gdb
    check_eq(gdb.read(0x080000A0, 12), b"POKEMON EMER", "ROM header")
    scratch = g.a("gStringVar4")  # a text buffer nobody uses on the title screen
    pattern = bytes(range(1, 65))
    gdb.write(scratch, pattern)
    check_eq(gdb.read(scratch, 64), pattern, "EWRAM write then read (64 bytes)")
    # IWRAM: free space between the variables and the stacks. Put back what was there afterwards.
    iwram = gdb.read(0x03000000 + 0x7000, 4)
    gdb.write(0x03000000 + 0x7000, b"\xDE\xAD\xBE\xEF")
    check_eq(gdb.u32(0x03000000 + 0x7000), 0xEFBEADDE, "IWRAM u32")
    gdb.write(0x03000000 + 0x7000, iwram)
    big = gdb.read(0x02000000, 4096)
    check_eq(len(big), 4096, "4 KiB read")
    frames = g.u32(g.a("gMain") + g.off("Main", "vblankCounter2"))
    g.wait_until(lambda: g.u32(g.a("gMain") + g.off("Main", "vblankCounter2")) > frames + 20, 10, what="frames to advance")


@testkit.test("harness: flags, vars and special vars")
def flags_and_vars(emu):
    g = emu.game
    # a normal flag, a TEMP flag (first bytes of the flag array) and a special flag (own array)
    for name in ("FLAG_SYS_B_DASH", "FLAG_TEMP_5", "FLAG_HIDE_MAP_NAME_POPUP"):
        before = g.flag_get(name)
        g.flag_set(name, not before)
        check_eq(g.flag_get(name), not before, name + " after flip")
        g.flag_set(name, before)
        check_eq(g.flag_get(name), before, name + " restored")
    # neighbouring bits must not be disturbed
    base = g.flag_id("FLAG_SYS_RUN_BY_DEFAULT")
    check(g.flag_get(base), "run-by-default should still be set")
    g.flag_set("FLAG_SYS_B_DASH")
    check(g.flag_get(base), "setting one flag changed its neighbour")
    g.flag_clear("FLAG_SYS_B_DASH")
    # saved var
    g.var_set("VAR_HOLLOWBROOK_STATE", 3)
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 3, "VAR_HOLLOWBROOK_STATE")
    g.var_set("VAR_HOLLOWBROOK_STATE", 0)
    # special var: must land in the real gSpecialVar_0x8004
    g.var_set("VAR_0x8004", 0x1234)
    check_eq(g.u16(g.a("gSpecialVar_0x8004")), 0x1234, "gSpecialVar_0x8004 in RAM")
    check_eq(g.var_get("VAR_0x8004"), 0x1234, "VAR_0x8004 through the pointer table")
    # names are checked
    try:
        g.flag_get("FLAG_DOES_NOT_EXIST")
    except Exception as e:
        check("did you mean" in str(e) or "unknown constant" in str(e), "unhelpful error for a bad flag name: %s" % e)
    else:
        check(False, "a made-up flag name should raise an error")


@testkit.test("harness: positions, map and script injection")
def positions_and_scripts(emu):
    g = emu.game
    repo = g.L.repo
    start_map, start_x, start_y = facts.new_game_start(repo)
    check_eq(g.map_name(), start_map, "map at game start (src/new_game.c)")
    check_eq(g.player_pos(), (start_x, start_y), "tile at game start (src/new_game.c)")
    check_eq(g.saved_pos(), g.player_pos(), "SaveBlock1 pos vs the player's object")
    mid = g.L.const(start_map)
    check_eq(g.map_id(), (mid >> 8, mid & 255), "map id")
    # the map grid: size from layouts.json, and every warp in map.json shows up as a warp tile in the game
    mj = facts.map_json(repo, "Hollowbrook_PlayersHouse_2F")
    check_eq(g.map_size(), facts.layout_size(repo, mj["layout"]), "map size (layouts.json)")
    special = g.special_tiles()
    for w in mj["warp_events"]:
        check_eq(special.get((w["x"], w["y"])), "warp", "warp tile (%d,%d) from map.json" % (w["x"], w["y"]))
    check_eq(g.player_facing(), "S", "facing at game start")
    # script injection: setvar + setflag + end, run by the game's own script engine
    code = bytes([g._op("SCR_OP_SETVAR")]) + g.var_id("VAR_HOLLOWBROOK_STATE").to_bytes(2, "little") + (2).to_bytes(2, "little")
    code += bytes([g._op("SCR_OP_SETFLAG")]) + g.flag_id("FLAG_TEMP_5").to_bytes(2, "little")
    code += bytes([g._op("SCR_OP_END")])
    g.run_script(code, wait_done=True)
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 2, "var set by the injected script")
    check(g.flag_get("FLAG_TEMP_5"), "flag set by the injected script")
    check(g.overworld_idle(), "the game should be idle again after the script")
    # warp injection and back
    g.warp("MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F", 10, 3)
    check_eq(g.player_pos(), (10, 3), "position after warp")
    check_eq(g.map_name(), "MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F", "map after warp")


@testkit.test("harness: party and bag decoding (debug preset 4)")
def party_decoding(emu):
    g = emu.game
    g.debug_preset(4)  # Veldris_Debug_Preset4: Mudkip L8, stock of items, outside the house
    party = g.party()
    check_eq(len(party), 1, "party size after preset 4")
    mon = party[0]
    check_eq(mon["species_id"], g.L.const("SPECIES_MUDKIP"), "species (SPECIES_MUDKIP)")
    check_eq(mon["level"], 8, "level")
    check(mon["hp"] > 0 and mon["hp"] == mon["max_hp"], "Mudkip should be at full health: %s" % mon)
    check(len(mon["moves"]) >= 1, "Mudkip should know a move")
    check_eq(g.map_name(), "MAP_HOLLOWBROOK", "map after preset 4")
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 4, "story state after preset 4")
    check(g.bag_count("ITEM_POTION") >= 10, "preset 4 stocks 10 Potions, bag has %d" % g.bag_count("ITEM_POTION"))
    check_eq(g.bag_count("ITEM_EXP_SHARE"), 1, "Exp. Share is never duplicated by a preset")


if __name__ == "__main__":
    testkit.main()
