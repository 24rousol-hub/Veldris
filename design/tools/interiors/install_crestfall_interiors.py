"""Crestfall interiors (author asked for the maps to be built, 2026-10-08): Center 1F/2F and Mart on the vanilla
shared layouts, two houses on new shared layouts H1 (cottage) and H5 (bedroom house), door warps, fly point."""
import json, re
from pathlib import Path
import numpy as np
import houses
V = Path("/home/claude/veldris")
def jl(p): return json.load(open(V / p))
def jd(p, o): open(V / p, "w").write(json.dumps(o, indent=2, ensure_ascii=False) + "\n")

# ---- shared house layouts
L = jl("data/layouts/layouts.json")
NEW = {"LAYOUT_VELDRIS_HOUSE_COTTAGE": ("VeldrisHouse_Cottage", houses.h1()),
       "LAYOUT_VELDRIS_HOUSE_BEDROOM": ("VeldrisHouse_Bedroom", houses.h5())}
border = (V / "data/layouts/Hollowbrook_NeighboursHouse/border.bin").read_bytes()
for lid, (folder, g) in NEW.items():
    d = V / "data/layouts" / folder; d.mkdir(exist_ok=True)
    g.astype("<u2").tofile(d / "map.bin"); (d / "border.bin").write_bytes(border)
    entry = {"id": lid, "name": folder + "_Layout", "width": int(g.shape[1]), "height": int(g.shape[0]),
             "primary_tileset": "gTileset_Building", "secondary_tileset": "gTileset_Gen4Interior",
             "border_filepath": f"data/layouts/{folder}/border.bin", "blockdata_filepath": f"data/layouts/{folder}/map.bin",
             "layout_version": "emerald"}
    L["layouts"] = [l for l in L["layouts"] if l["id"] != lid] + [entry]
jd("data/layouts/layouts.json", L)

# ---- maps
def obj(gfx, x, y, move, script, local=None, flag="0"):
    o = {"graphics_id": gfx, "x": x, "y": y, "elevation": 3, "movement_type": move, "movement_range_x": 1 if "WANDER" in move else 0,
         "movement_range_y": 1 if "WANDER" in move else 0, "trainer_type": "TRAINER_TYPE_NONE", "trainer_sight_or_berry_tree_id": "0",
         "script": script, "flag": flag}
    if local: o = {"local_id": local, **o}
    return o
def warp(x, y, dest, wid, elev=0): return {"x": x, "y": y, "elevation": elev, "dest_map": dest, "dest_warp_id": str(wid)}
def mapjson(name, mid, layout, music, objs, warps, bgs=(), show=False):
    return {"id": mid, "name": name, "layout": layout, "music": music, "region": "REGION_HOENN", "region_map_section": "MAPSEC_CRESTFALL",
            "requires_flash": False, "weather": "WEATHER_NONE", "map_type": "MAP_TYPE_INDOOR", "allow_cycling": False,
            "allow_escaping": False, "allow_running": False, "show_map_name": show, "battle_scene": "MAP_BATTLE_SCENE_NORMAL",
            "connections": None, "object_events": list(objs), "warp_events": list(warps), "coord_events": [], "bg_events": list(bgs)}
MAPS = {}
P = "Crestfall_PokemonCenter_1F"
MAPS[P] = (mapjson(P, "MAP_CRESTFALL_POKEMON_CENTER_1F", "LAYOUT_POKEMON_CENTER_1F", "MUS_POKE_CENTER",
    [obj("OBJ_EVENT_GFX_NURSE", 7, 2, "MOVEMENT_TYPE_FACE_DOWN", f"{P}_EventScript_Nurse", "LOCALID_CRESTFALL_NURSE"),
     obj("OBJ_EVENT_GFX_HIKER", 10, 6, "MOVEMENT_TYPE_FACE_LEFT", f"{P}_EventScript_Visitor")],
    [warp(7, 8, "MAP_CRESTFALL", 1, 3), warp(6, 8, "MAP_CRESTFALL", 1, 3), warp(1, 6, "MAP_CRESTFALL_POKEMON_CENTER_2F", 0, 4)]),
f"""{P}_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, {P}_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, CableClub_OnResume
	.byte 0

{P}_OnTransition:
	setrespawn HEAL_LOCATION_CRESTFALL
	end

{P}_EventScript_Nurse::
	setvar VAR_0x800B, LOCALID_CRESTFALL_NURSE
	call Common_EventScript_PkmnCenterNurse
	waitmessage
	waitbuttonpress
	release
	end

{P}_EventScript_Visitor::
	msgbox {P}_Text_Visitor, MSGBOX_NPC
	end

{P}_Text_Visitor:
	.string "I came here to see the gym.\\n"
	.string "I stayed for the tomatoes.$"
""")
P2 = "Crestfall_PokemonCenter_2F"
MAPS[P2] = (mapjson(P2, "MAP_CRESTFALL_POKEMON_CENTER_2F", "LAYOUT_POKEMON_CENTER_2F", "MUS_POKE_CENTER",
    [obj("OBJ_EVENT_GFX_TEALA", 6, 2, "MOVEMENT_TYPE_FACE_DOWN", "Common_EventScript_UnionRoomAttendant"),
     obj("OBJ_EVENT_GFX_TEALA", 2, 2, "MOVEMENT_TYPE_FACE_DOWN", "Common_EventScript_WirelessClubAttendant"),
     obj("OBJ_EVENT_GFX_TEALA", 10, 2, "MOVEMENT_TYPE_FACE_DOWN", "Common_EventScript_DirectCornerAttendant")],
    [warp(1, 6, "MAP_CRESTFALL_POKEMON_CENTER_1F", 2, 4), warp(5, 1, "MAP_UNION_ROOM", 0, 3), warp(9, 1, "MAP_TRADE_CENTER", 0, 3)]),
f"""{P2}_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, CableClub_OnFrame
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, CableClub_OnWarp
	map_script MAP_SCRIPT_ON_LOAD, CableClub_OnLoad
	map_script MAP_SCRIPT_ON_TRANSITION, CableClub_OnTransition
	.byte 0
""")
M = "Crestfall_Mart"
MAPS[M] = (mapjson(M, "MAP_CRESTFALL_MART", "LAYOUT_MART", "MUS_POKE_MART",
    [obj("OBJ_EVENT_GFX_MART_EMPLOYEE", 1, 3, "MOVEMENT_TYPE_FACE_RIGHT", f"{M}_EventScript_Clerk", "LOCALID_CRESTFALL_MART_CLERK"),
     obj("OBJ_EVENT_GFX_MAN_2", 5, 5, "MOVEMENT_TYPE_FACE_DOWN", f"{M}_EventScript_Shopkeeper")],
    [warp(3, 7, "MAP_CRESTFALL", 2), warp(4, 7, "MAP_CRESTFALL", 2)]),
f"""{M}_MapScripts::
	.byte 0

{M}_EventScript_Clerk::
	lock
	faceplayer
	message {M}_Text_Clerk
	waitmessage
	pokemart {M}_Pokemart
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
{M}_Pokemart:
	.2byte ITEM_POKE_BALL
	.2byte ITEM_POTION
	.2byte ITEM_ANTIDOTE
	.2byte ITEM_PARALYZE_HEAL
	.2byte ITEM_AWAKENING
	pokemartlistend

{M}_EventScript_Shopkeeper::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, {M}_EventScript_ShopkeeperAfter
	msgbox {M}_Text_ShopkeeperBefore, MSGBOX_DEFAULT
	release
	end

{M}_EventScript_ShopkeeperAfter::
	msgbox {M}_Text_ShopkeeperAfter, MSGBOX_DEFAULT
	release
	end

{M}_Text_Clerk:
	.string "Welcome! Hay is not for sale.\\n"
	.string "Everything else is.$"

{M}_Text_ShopkeeperBefore:
	.string "I stock POTIONS, POKé BALLS,\\n"
	.string "and a few things for hay fever.\\p"
	.string "I'd advise a few POTIONS.\\n"
	.string "GRETA's SKITTY hits harder\\l"
	.string "than it purrs.$"

{M}_Text_ShopkeeperAfter:
	.string "A STANDARD BADGE! Fine work.\\n"
	.string "I'll say what I tell everyone:\\p"
	.string "The next town is further than\\n"
	.string "it looks. Bring more POTIONS.$"
""")
A = "Crestfall_HouseA"
MAPS[A] = (mapjson(A, "MAP_CRESTFALL_HOUSE_A", "LAYOUT_VELDRIS_HOUSE_COTTAGE", "MUS_PETALBURG",
    [obj("OBJ_EVENT_GFX_OLD_MAN", 8, 4, "MOVEMENT_TYPE_FACE_DOWN", f"{A}_EventScript_Husband"),
     obj("OBJ_EVENT_GFX_SKITTY", 1, 3, "MOVEMENT_TYPE_LOOK_AROUND", f"{A}_EventScript_Skitty")],
    [warp(2, 7, "MAP_CRESTFALL", 0)]),
f"""{A}_MapScripts::
	.byte 0

{A}_EventScript_Husband::
	msgbox {A}_Text_Husband, MSGBOX_NPC
	end

{A}_EventScript_Skitty::
	lock
	faceplayer
	waitse
	playmoncry SPECIES_SKITTY, CRY_MODE_NORMAL
	msgbox {A}_Text_Skitty, MSGBOX_DEFAULT
	waitmoncry
	release
	end

{A}_Text_Husband:
	.string "My SKITTY sleeps on the warm\\n"
	.string "spot by the stove. I sleep\\l"
	.string "on the cold spot.\\p"
	.string "We've agreed not to discuss it.$"

{A}_Text_Skitty:
	.string "SKITTY: Mew!$"
""")
B = "Crestfall_HouseB"
MAPS[B] = (mapjson(B, "MAP_CRESTFALL_HOUSE_B", "LAYOUT_VELDRIS_HOUSE_BEDROOM", "MUS_PETALBURG",
    [obj("OBJ_EVENT_GFX_YOUNGSTER", 3, 4, "MOVEMENT_TYPE_FACE_DOWN", f"{B}_EventScript_Trainer")],
    [warp(8, 7, "MAP_CRESTFALL", 3)]),
f"""{B}_MapScripts::
	.byte 0

{B}_EventScript_Trainer::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, {B}_EventScript_TrainerAfter
	msgbox {B}_Text_TrainerBefore, MSGBOX_DEFAULT
	release
	end

{B}_EventScript_TrainerAfter::
	msgbox {B}_Text_TrainerAfter, MSGBOX_DEFAULT
	release
	end

{B}_Text_TrainerBefore:
	.string "I was going to challenge\\n"
	.string "GRETA today. Really.\\p"
	.string "Then I saw her MILTANK.\\n"
	.string "I'm going to have lunch first.$"

{B}_Text_TrainerAfter:
	.string "You won! Wow.\\n"
	.string "I'll challenge her next year.\\p"
	.string "Or the year after. Or I'll\\n"
	.string "become a farmer. It's a nice\\l"
	.string "life. Mostly.$"
""")
MG = jl("data/maps/map_groups.json"); grp = MG["gMapGroup_IndoorVeldris"]
es = (V / "data/event_scripts.s").read_text()
for name, (mj, scr) in MAPS.items():
    d = V / "data/maps" / name; d.mkdir(exist_ok=True)
    jd(f"data/maps/{name}/map.json", mj); (d / "scripts.inc").write_text(scr)
    if name not in grp: grp.append(name)
    inc = f'\t.include "data/maps/{name}/scripts.inc"\n'
    if inc not in es: es = es.rstrip("\n") + "\n" + inc
jd("data/maps/map_groups.json", MG); (V / "data/event_scripts.s").write_text(es)

# ---- Crestfall: door warps and the visited flag
C = jl("data/maps/Crestfall/map.json")
C["warp_events"] = [warp(3, 14, "MAP_CRESTFALL_HOUSE_A", 0), warp(9, 14, "MAP_CRESTFALL_POKEMON_CENTER_1F", 0),
                    warp(31, 14, "MAP_CRESTFALL_MART", 0), warp(36, 14, "MAP_CRESTFALL_HOUSE_B", 0)]
jd("data/maps/Crestfall/map.json", C)
cs = (V / "data/maps/Crestfall/scripts.inc").read_text()
if "Crestfall_OnTransition" not in cs:
    cs = re.sub(r"Crestfall_MapScripts::\n(\t\.byte 0\n)?", "Crestfall_MapScripts::\n\tmap_script MAP_SCRIPT_ON_TRANSITION, Crestfall_OnTransition\n\t.byte 0\n\nCrestfall_OnTransition:\n\tsetflag FLAG_VISITED_CRESTFALL\n\tend\n", cs, count=1)
    (V / "data/maps/Crestfall/scripts.inc").write_text(cs)

# ---- fly point
f = V / "include/constants/flags.h"; s = f.read_text()
s = s.replace("#define FLAG_UNUSED_0x021    0x21 // Unused Flag", "#define FLAG_VISITED_CRESTFALL 0x21")
f.write_text(s)
H = jl("src/data/heal_locations.json")
if not any(h["id"] == "HEAL_LOCATION_CRESTFALL" for h in H["heal_locations"]):
    H["heal_locations"].append({"id": "HEAL_LOCATION_CRESTFALL", "map": "MAP_CRESTFALL", "x": 9, "y": 15,
        "respawn_map": "MAP_CRESTFALL_POKEMON_CENTER_1F", "respawn_npc": "LOCALID_CRESTFALL_NURSE"})
jd("src/data/heal_locations.json", H)
f = V / "src/data/veldris_fly_towns.h"; s = f.read_text()
anchor = "#define VELDRIS_FLY_TOWNS(X) \\\n    X(MAPSEC_HOLLOWBROOK, FLAG_VISITED_HOLLOWBROOK, MAP_HOLLOWBROOK, HEAL_LOCATION_HOLLOWBROOK)\n"
if "X(MAPSEC_CRESTFALL" not in s and anchor in s:   # add the row to the table, not to the example comment
    s = s.replace(anchor, anchor.rstrip("\n") + " \\\n    X(MAPSEC_CRESTFALL, FLAG_VISITED_CRESTFALL, MAP_CRESTFALL, HEAL_LOCATION_CRESTFALL)\n", 1)
f.write_text(s)
f = V / "src/data/region_map/region_map_layout.h"; s = f.read_text()
rows = s.split("\n"); n = 0
for i, line in enumerate(rows):
    if line.strip().startswith("{MAPSEC_"):
        if n == 12:
            cells = line.strip().rstrip(",").strip("{}").split(", ")
            if cells[6] == "MAPSEC_NONE": cells[6] = "MAPSEC_CRESTFALL"
            rows[i] = line[:len(line) - len(line.lstrip())] + "{" + ", ".join(cells) + "},"
        n += 1
f.write_text("\n".join(rows))
print("done")
