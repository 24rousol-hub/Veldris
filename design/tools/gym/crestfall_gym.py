"""Crestfall Gym (author 2026-10-08): the green-B layout on the vanilla Petalburg Gym tiles. A railed aisle up the
middle whose two centre gates open once Greta is beaten; a pen on each side with a gym trainer by its gap
(the player must beat one, the other is optional). Writes the layout, map, scripts and the Crestfall door warp."""
import json
import numpy as np
from pathlib import Path
V = Path(__file__).resolve().parents[3]
B, F = 0x0400, 0x3000
FLOOR, EDGE = 513, 521
VR, VR_TOP, VR_BOT, VR_JR, VR_JL = 736, 737, 738, 739, 740
MATS = {"orange": 577, "green": 673, "blue": 705}
def mat(g, x, y, col):
    for r in range(4):
        for i in range(7): g[y + r, x + i] = F | (MATS[col] + r * 8 + i)
def railing(g, y, x0, x1, gaps=()):
    for x in range(x0, x1 + 1): g[y, x] = (F | FLOOR) if x in gaps else (B | (560 if (x - x0) % 2 == 0 else 561))
GATES = [(6, 11), (7, 11), (8, 11), (6, 16), (7, 16), (8, 16)]
JOINS = [(5, 11), (9, 11), (5, 16), (9, 16)]
def layout():
    W, H = 15, 23
    g = np.full((H, W), F | FLOOR, np.uint16); g[:, 0] = F | EDGE
    g[0, :] = B | 515; g[0, 0] = B | 514; g[0, W - 1] = B | 516
    g[1, :] = B | 523; g[1, 0] = B | 522; g[1, W - 1] = B | 524
    g[2, :] = F | 531; g[2, 0] = F | 530; g[2, W - 1] = F | 532
    for i, m in enumerate((541, 542, 543)): g[0, 6 + i] = B | m
    for x0 in (1, 11):
        for i, (a, b) in enumerate(((592, 600), (672, 680), (688, 696))): g[0, x0 + i] = B | a; g[1, x0 + i] = B | b
    mat(g, 4, 3, "blue")
    for x in (5, 9):
        for y in range(8, 20): g[y, x] = B | VR
        g[8, x] = B | VR_TOP; g[19, x] = B | VR_BOT
    railing(g, 11, 6, 8); railing(g, 16, 6, 8)
    for x, y in JOINS: g[y, x] = B | (VR_JR if x == 5 else VR_JL)
    railing(g, 13, 0, 4, gaps=(4,)); railing(g, 15, 10, 14, gaps=(10,))
    for y in range(20, H):
        g[y, :] = F | 555; g[y, 0] = F | 556
    for x in (3, 11): g[20, x] = B | 576; g[21, x] = B | 584
    g[H - 1, 7] = F | 6; g[H - 1, 8] = F | 7
    return g

def obj(gfx, x, y, move, script, ttype="TRAINER_TYPE_NONE", sight="0", local=None):
    o = {"graphics_id": gfx, "x": x, "y": y, "elevation": 3, "movement_type": move, "movement_range_x": 0, "movement_range_y": 0,
         "trainer_type": ttype, "trainer_sight_or_berry_tree_id": sight, "script": script, "flag": "0"}
    return {"local_id": local, **o} if local else o

P = "Crestfall_Gym"
OPEN_GATES = "".join(f"\tsetmetatile {x}, {y}, {FLOOR}, FALSE\n" for x, y in GATES) + "".join(f"\tsetmetatile {x}, {y}, {VR}, TRUE\n" for x, y in JOINS)
SCRIPTS = f"""{P}_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, {P}_OnLoad
	.byte 0

@ The centre gates stay shut until Greta is beaten (author, 2026-10-08).
{P}_OnLoad:
	call_if_set FLAG_BADGE01_GET, {P}_EventScript_OpenGates
	end

{P}_EventScript_OpenGates::
{OPEN_GATES}	return

{P}_EventScript_Greta::
	trainerbattle_single TRAINER_CRESTFALL_GRETA, {P}_Text_GretaIntro, {P}_Text_GretaDefeat, {P}_EventScript_GretaDefeated, NO_MUSIC
	goto_if_unset FLAG_RECEIVED_HM_CUT, {P}_EventScript_GiveCut
	goto_if_unset FLAG_RECEIVED_TM_CRUNCH, {P}_EventScript_GiveCrunch
	msgbox {P}_Text_GretaAfterBadge, MSGBOX_DEFAULT
	release
	end

{P}_EventScript_GretaDefeated::
	message {P}_Text_ReceivedBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox {P}_Text_GretaBadgeInfo, MSGBOX_DEFAULT
	setflag FLAG_BADGE01_GET
	settrainerflag TRAINER_CRESTFALL_GYM_1
	settrainerflag TRAINER_CRESTFALL_GYM_2
	call {P}_EventScript_OpenGates
	special DrawWholeMapView
	goto {P}_EventScript_GiveCut
	end

{P}_EventScript_GiveCut::
	giveitem ITEM_HM_CUT
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_HM_CUT
	goto {P}_EventScript_GiveCrunch
	end

{P}_EventScript_GiveCrunch::
	giveitem ITEM_TM_CRUNCH
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_TM_CRUNCH
	msgbox {P}_Text_GretaGifts, MSGBOX_DEFAULT
	release
	end

@ Gym trainers. Beating Greta marks both as beaten, so an unbeaten one just chats afterwards (author: one required).
{P}_EventScript_Dale::
	trainerbattle_single TRAINER_CRESTFALL_GYM_1, {P}_Text_DaleIntro, {P}_Text_DaleDefeat
	msgbox {P}_Text_DaleAfter, MSGBOX_AUTOCLOSE
	end

{P}_EventScript_Wren::
	trainerbattle_single TRAINER_CRESTFALL_GYM_2, {P}_Text_WrenIntro, {P}_Text_WrenDefeat
	msgbox {P}_Text_WrenAfter, MSGBOX_AUTOCLOSE
	end

{P}_EventScript_Statue::
	lockall
	goto_if_set FLAG_BADGE01_GET, {P}_EventScript_StatueCertified
	msgbox {P}_Text_Statue, MSGBOX_DEFAULT
	releaseall
	end

{P}_EventScript_StatueCertified::
	msgbox {P}_Text_StatueCertified, MSGBOX_DEFAULT
	releaseall
	end

@ Greta's lines are the earlier drafts in design/dialogue/crestfall.inc (PROPOSED); the gym trainers' lines are
@ reworded from that draft because the hay maze is gone.
{P}_Text_GretaIntro:
	.string "Well, hello. You must be {{PLAYER}}.\\n"
	.string "The whole town has been talking.\\p"
	.string "I'm GRETA. Crestfall's gym leader.\\n"
	.string "Yes, I know. I look too young.\\p"
	.string "I get that a lot. Usually right\\n"
	.string "before I win.\\p"
	.string "Normal types. Don't look so\\n"
	.string "disappointed. Normal is reliable.\\p"
	.string "Flashy gets you a cool entrance.\\n"
	.string "Reliable gets you badges.\\p"
	.string "Try to keep up. No pressure.$"

{P}_Text_GretaDefeat:
	.string "Wow. Okay. That was good.\\n"
	.string "Really good.$"

{P}_Text_ReceivedBadge:
	.string "{{PLAYER}} received the STANDARD\\n"
	.string "BADGE from GRETA!$"

{P}_Text_GretaBadgeInfo:
	.string "That badge means you've met the\\n"
	.string "standard to start the gym\\l"
	.string "challenge. The real work begins.\\p"
	.string "It also lets you use CUT. Here,\\n"
	.string "take these as well.$"

{P}_Text_GretaGifts:
	.string "CUT clears small trees. CRUNCH\\n"
	.string "bites hard. Use both wisely.\\p"
	.string "And the gates are open now, so\\n"
	.string "come back any time.$"

{P}_Text_GretaAfterBadge:
	.string "That Goldsworth boy? Bit of a\\n"
	.string "mess, honestly. Not wicked.\\p"
	.string "He's just never been told ‘no.’\\n"
	.string "So you'd be doing the region a\\l"
	.string "favour, every time you beat him.$"

{P}_Text_DaleIntro:
	.string "Pick a side, pick a fight!\\n"
	.string "You picked mine. Come on, then!$"

{P}_Text_DaleDefeat:
	.string "Fair's fair. Go on through.$"

{P}_Text_DaleAfter:
	.string "GRETA's tougher than she looks.\\n"
	.string "Also tougher than she sounds.$"

{P}_Text_WrenIntro:
	.string "Ah, a challenger! This side of\\n"
	.string "the hall is mine. Shall we?$"

{P}_Text_WrenDefeat:
	.string "Splendid. Truly splendid.$"

{P}_Text_WrenAfter:
	.string "I've watched GRETA climb the\\n"
	.string "ranks. She'll go far. So may you.$"

{P}_Text_Statue:
	.string "CRESTFALL POKéMON GYM$"

{P}_Text_StatueCertified:
	.string "CRESTFALL POKéMON GYM\\p"
	.string "GRETA'S CERTIFIED TRAINERS:\\n"
	.string "{{PLAYER}}$"
"""
if __name__ == "__main__":
    def jl(p): return json.load(open(V / p))
    def jd(p, o): open(V / p, "w").write(json.dumps(o, indent=2, ensure_ascii=False) + "\n")
    g = layout(); d = V / "data/layouts/Crestfall_Gym"; d.mkdir(exist_ok=True)
    g.astype("<u2").tofile(d / "map.bin")
    pbl = {l["id"]: l for l in jl("data/layouts/layouts.json")["layouts"]}["LAYOUT_PETALBURG_CITY_GYM"]
    (d / "border.bin").write_bytes((V / pbl["border_filepath"]).read_bytes())
    L = jl("data/layouts/layouts.json")
    L["layouts"] = [l for l in L["layouts"] if l["id"] != "LAYOUT_CRESTFALL_GYM"] + [{"id": "LAYOUT_CRESTFALL_GYM", "name": "Crestfall_Gym_Layout",
        "width": 15, "height": 23, "primary_tileset": "gTileset_Building", "secondary_tileset": "gTileset_PetalburgGym",
        "border_filepath": "data/layouts/Crestfall_Gym/border.bin", "blockdata_filepath": "data/layouts/Crestfall_Gym/map.bin", "layout_version": "emerald"}]
    jd("data/layouts/layouts.json", L)
    M = {"id": "MAP_CRESTFALL_GYM", "name": P, "layout": "LAYOUT_CRESTFALL_GYM", "music": "MUS_GYM", "region": "REGION_HOENN",
         "region_map_section": "MAPSEC_CRESTFALL", "requires_flash": False, "weather": "WEATHER_NONE", "map_type": "MAP_TYPE_INDOOR",
         "allow_cycling": False, "allow_escaping": False, "allow_running": True, "show_map_name": False, "battle_scene": "MAP_BATTLE_SCENE_GYM",
         "connections": None,
         "object_events": [obj("OBJ_EVENT_GFX_LASS", 7, 4, "MOVEMENT_TYPE_FACE_DOWN", f"{P}_EventScript_Greta", local="LOCALID_CRESTFALL_GRETA"),
                           obj("OBJ_EVENT_GFX_GENTLEMAN", 1, 12, "MOVEMENT_TYPE_FACE_RIGHT", f"{P}_EventScript_Wren", "TRAINER_TYPE_NORMAL", "3"),
                           obj("OBJ_EVENT_GFX_YOUNGSTER", 13, 14, "MOVEMENT_TYPE_FACE_LEFT", f"{P}_EventScript_Dale", "TRAINER_TYPE_NORMAL", "3")],
         "warp_events": [{"x": 7, "y": 22, "elevation": 3, "dest_map": "MAP_CRESTFALL", "dest_warp_id": "4"},
                         {"x": 8, "y": 22, "elevation": 3, "dest_map": "MAP_CRESTFALL", "dest_warp_id": "4"}],
         "coord_events": [],
         "bg_events": [{"type": "sign", "x": x, "y": 21, "elevation": 0, "player_facing_dir": "BG_EVENT_PLAYER_FACING_NORTH", "script": f"{P}_EventScript_Statue"} for x in (3, 11)]}
    (V / f"data/maps/{P}").mkdir(exist_ok=True); jd(f"data/maps/{P}/map.json", M); (V / f"data/maps/{P}/scripts.inc").write_text(SCRIPTS)
    MG = jl("data/maps/map_groups.json")
    if P not in MG["gMapGroup_IndoorVeldris"]: MG["gMapGroup_IndoorVeldris"].append(P)
    jd("data/maps/map_groups.json", MG)
    es = V / "data/event_scripts.s"; s = es.read_text(); inc = f'\t.include "data/maps/{P}/scripts.inc"\n'
    if inc not in s: es.write_text(s.rstrip("\n") + "\n" + inc)
    C = jl("data/maps/Crestfall/map.json")
    C["warp_events"] = [w for w in C["warp_events"] if w["dest_map"] != "MAP_CRESTFALL_GYM"] + [{"x": 20, "y": 9, "elevation": 0, "dest_map": "MAP_CRESTFALL_GYM", "dest_warp_id": "0"}]
    jd("data/maps/Crestfall/map.json", C)
    f = V / "include/constants/flags.h"; s = f.read_text()
    if "FLAG_RECEIVED_TM_CRUNCH" not in s:
        s = s.replace("#define FLAG_RECEIVED_TM_ROCK_TOMB           0xA5", "#define FLAG_RECEIVED_TM_ROCK_TOMB           0xA5\n#define FLAG_RECEIVED_TM_CRUNCH              FLAG_RECEIVED_TM_ROCK_TOMB // Veldris: Greta's TM (Rustboro's gym is unused)")
        f.write_text(s)
    print("ok")
