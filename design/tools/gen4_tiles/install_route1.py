"""Install Route 1 (map, layout, scripts, trainers, flags, wild Pokemon) and the Hollowbrook <-> Route 1 connection."""
import json, re
from pathlib import Path
V = Path("/home/claude/veldris")

def jload(p): return json.load(open(V / p))
def jdump(p, d): open(V / p, "w").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

# ---- layouts.json
L = jload("data/layouts/layouts.json")
for l in L["layouts"]:
    if l["id"] == "LAYOUT_HOLLOWBROOK":
        l["primary_tileset"], l["secondary_tileset"] = "gTileset_Gen4Outdoor", "gTileset_Gen4Hollowbrook"
if not any(l["id"] == "LAYOUT_VELDRIS_ROUTE1" for l in L["layouts"]):
    i = next(i for i, l in enumerate(L["layouts"]) if l["id"] == "LAYOUT_HOLLOWBROOK")
    L["layouts"].insert(i + 1, {"id": "LAYOUT_VELDRIS_ROUTE1", "name": "VeldrisRoute1_Layout", "width": 60, "height": 25,
        "primary_tileset": "gTileset_Gen4Outdoor", "secondary_tileset": "gTileset_Gen4Hollowbrook",
        "border_filepath": "data/layouts/VeldrisRoute1/border.bin", "blockdata_filepath": "data/layouts/VeldrisRoute1/map.bin",
        "layout_version": "emerald"})
jdump("data/layouts/layouts.json", L)

# ---- map_groups.json
MG = jload("data/maps/map_groups.json")
grp = MG["gMapGroup_TownsAndRoutes"]
if "VeldrisRoute1" not in grp: grp.insert(grp.index("Hollowbrook") + 1, "VeldrisRoute1")
jdump("data/maps/map_groups.json", MG)

# ---- event_scripts.s include (exactly once)
es = V / "data/event_scripts.s"; s = es.read_text()
inc = '\t.include "data/maps/VeldrisRoute1/scripts.inc"\n'
if inc not in s: es.write_text(s.rstrip("\n") + "\n" + inc)

# ---- Hollowbrook: connection, tilesets moved to Gen 4, laundry woman out of the neighbour's new house footprint
H = jload("data/maps/Hollowbrook/map.json")
H["connections"] = [{"map": "MAP_VELDRIS_ROUTE1", "offset": -2, "direction": "right"}]
for o in H["object_events"]:
    if (o["x"], o["y"]) == (20, 20): o["x"] = 21
jdump("data/maps/Hollowbrook/map.json", H)

# ---- Route 1 map.json
def obj(lid, gfx, x, y, mv, script, trainer=False, sight=0, rx=0, ry=0, flag="0"):
    return {"local_id": lid, "graphics_id": gfx, "x": x, "y": y, "elevation": 3, "movement_type": mv,
            "movement_range_x": rx, "movement_range_y": ry,
            "trainer_type": "TRAINER_TYPE_NORMAL" if trainer else "TRAINER_TYPE_NONE",
            "trainer_sight_or_berry_tree_id": str(sight), "script": script, "flag": flag}
R = {
    "id": "MAP_VELDRIS_ROUTE1", "name": "VeldrisRoute1", "layout": "LAYOUT_VELDRIS_ROUTE1", "music": "MUS_ROUTE101",
    "region": "REGION_HOENN", "region_map_section": "MAPSEC_VELDRIS_ROUTE_1", "requires_flash": False,
    "weather": "WEATHER_SUNNY", "map_type": "MAP_TYPE_ROUTE", "allow_cycling": True, "allow_escaping": False,
    "allow_running": True, "show_map_name": True, "battle_scene": "MAP_BATTLE_SCENE_NORMAL",
    "connections": [{"map": "MAP_HOLLOWBROOK", "offset": 2, "direction": "left"}],
    "object_events": [
        obj("LOCALID_VELDRIS_ROUTE1_GUIDE", "OBJ_EVENT_GFX_MAN_2", 12, 12, "MOVEMENT_TYPE_FACE_LEFT", "VeldrisRoute1_EventScript_Guide"),
        obj("LOCALID_VELDRIS_ROUTE1_YOUNGSTER", "OBJ_EVENT_GFX_YOUNGSTER", 24, 13, "MOVEMENT_TYPE_FACE_LEFT", "VeldrisRoute1_EventScript_Youngster", True, 4),
        obj("LOCALID_VELDRIS_ROUTE1_LASS", "OBJ_EVENT_GFX_LASS", 38, 15, "MOVEMENT_TYPE_FACE_LEFT", "VeldrisRoute1_EventScript_Lass", True, 3),
        obj("LOCALID_VELDRIS_ROUTE1_FARMER", "OBJ_EVENT_GFX_HIKER", 46, 14, "MOVEMENT_TYPE_FACE_LEFT", "VeldrisRoute1_EventScript_Farmer", True, 4),
        obj("LOCALID_VELDRIS_ROUTE1_SIGHTING", "OBJ_EVENT_GFX_MAN_4", 32, 9, "MOVEMENT_TYPE_WANDER_AROUND", "VeldrisRoute1_EventScript_Sighting", rx=1, ry=1),
    ],
    "warp_events": [], "coord_events": [],
    "bg_events": [
        {"type": "sign", "x": 10, "y": 11, "elevation": 0, "player_facing_dir": "BG_EVENT_PLAYER_FACING_ANY", "script": "VeldrisRoute1_EventScript_SignWest"},
        {"type": "sign", "x": 50, "y": 11, "elevation": 0, "player_facing_dir": "BG_EVENT_PLAYER_FACING_ANY", "script": "VeldrisRoute1_EventScript_SignEast"},
        {"type": "hidden_item", "x": 27, "y": 13, "elevation": 3, "item": "ITEM_POTION", "flag": "FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_POTION"},
        {"type": "hidden_item", "x": 44, "y": 17, "elevation": 3, "item": "ITEM_REPEL", "flag": "FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_REPEL"},
    ],
}
d = V / "data/maps/VeldrisRoute1"; d.mkdir(exist_ok=True)
jdump("data/maps/VeldrisRoute1/map.json", R)

# ---- scripts.inc: the draft's code (header comment dropped) + the dialogue texts
draft = (V / "design/scripts/route1_scripts.inc").read_text()
code = draft[draft.index("VeldrisRoute1_MapScripts::"):]
code = code.replace("FLAG_ROUTE1_GUIDE_POTIONS", "FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS")
texts = (V / "design/dialogue/route1.inc").read_text()
blocks = re.findall(r"^(VeldrisRoute1_Text_\w+::\n(?:\t\.string .*\n)+)", texts, re.M)
(d / "scripts.inc").write_text(code.rstrip("\n") + "\n\n" + "\n".join(b.replace("::\n", ":\n", 1) for b in blocks))

# ---- flags
F = V / "include/constants/flags.h"; s = F.read_text()
for old, new in [("FLAG_UNUSED_0x265  0x265 // Unused Flag", "FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_POTION 0x265"),
                 ("FLAG_UNUSED_0x266  0x266 // Unused Flag", "FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_REPEL 0x266"),
                 ("FLAG_UNUSED_0x496                                           0x496 // Unused Flag",
                  "FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS                           0x496")]:
    if old in s: s = s.replace(old, new)
    else: assert new in s, old
F.write_text(s)

# ---- trainers: reuse three vanilla Route 102 entries (no new ids)
TP = V / "src/data/trainers.party"; s = TP.read_text()
def block(old, name, cls, pic, gender, music, mons):
    body = f"=== {old} ===\nName: {name}\nClass: {cls}\nPic: {pic}\nGender: {gender}\nMusic: {music}\nDouble Battle: No\nAI: Check Bad Move\n"
    for sp, lv in mons:
        body += f"\n{sp}\nLevel: {lv}\nIVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe\n"
    return body + "\n"
def replace_block(s, old, new):
    i = s.index(f"=== {old} ===")
    j = s.index("\n=== ", i + 5) + 1
    return s[:i] + new + s[j:]
for old, new in [("TRAINER_ALLEN", block("TRAINER_ALLEN", "TOBY", "Youngster", "Youngster", "Male", "Male", [("Lillipup", 3)])),
                 ("TRAINER_TIANA", block("TRAINER_TIANA", "MAISIE", "Lass", "Lass", "Female", "Female", [("Zigzagoon", 3), ("Skitty", 3)])),
                 ("TRAINER_RICK", block("TRAINER_RICK", "DALE", "Hiker", "Hiker", "Male", "Hiker", [("Zigzagoon", 4), ("Skitty", 4)]))]:
    s = replace_block(s, old, new)
TP.write_text(s)
O = V / "include/constants/opponents.h"; s = O.read_text()
if "TRAINER_VELDRIS_ROUTE1_YOUNGSTER" not in s:
    s = s.replace("#define TRAINER_RICK                        615\n", "#define TRAINER_RICK                        615\n")
    add = ("\n// Veldris Route 1 trainers reuse vanilla Route 102 entries (design/trainer-roster.md)\n"
           "#define TRAINER_VELDRIS_ROUTE1_YOUNGSTER TRAINER_ALLEN\n"
           "#define TRAINER_VELDRIS_ROUTE1_LASS      TRAINER_TIANA\n"
           "#define TRAINER_VELDRIS_ROUTE1_FARMER    TRAINER_RICK\n")
    k = s.rindex("#endif")
    s = s[:k] + add + "\n" + s[k:]
O.write_text(s)

# ---- wild encounters (design/route1.md)
W = jload("src/data/wild_encounters.json")
g = W["wild_encounter_groups"][0]
g["encounters"] = [e for e in g["encounters"] if e.get("map") != "MAP_VELDRIS_ROUTE1"]
slots = [("ZIGZAGOON", 2, 3), ("LILLIPUP", 2, 3), ("BIDOOF", 2, 3), ("SENTRET", 2, 3), ("ZIGZAGOON", 3, 3), ("LILLIPUP", 3, 3),
         ("BIDOOF", 3, 4), ("SENTRET", 3, 4), ("SKITTY", 3, 4), ("SKITTY", 4, 4), ("SLAKOTH", 4, 4), ("MILTANK", 4, 4)]
entry = {"map": "MAP_VELDRIS_ROUTE1", "base_label": "gVeldrisRoute1",
         "land_mons": {"encounter_rate": 20, "mons": [{"min_level": a, "max_level": b, "species": f"SPECIES_{sp}"} for sp, a, b in slots]}}
i = next(i for i, e in enumerate(g["encounters"]) if e.get("map") == "MAP_ROUTE101")
g["encounters"].insert(i, entry)
jdump("src/data/wild_encounters.json", W)
print("installed")
