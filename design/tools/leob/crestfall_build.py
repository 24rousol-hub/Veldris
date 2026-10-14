"""Crestfall (40x32), layout B 'village green' approved by the author 2026-10-01. LeoB General + Petalburg.
Writes the layout and the map; doors get warps once the interiors exist."""
import json, sys
import numpy as np
from pathlib import Path
from leob_town import Town
V = Path("/home/claude/veldris")

def layout():
    t = Town(40, 32)
    t.road(0, 15, 13, 16)                 # Route 1 from the west
    t.road(26, 15, 39, 16)                # Route 2 east (to Wendlebury)
    t.road(14, 11, 25, 21)                # the square
    t.unroad(16, 13, 23, 19)              # grass island in the middle of the square
    t.pond(17, 14, 22, 17)
    t.flowers([(16, 13), (18, 13), (21, 13), (23, 13), (16, 15), (23, 15), (16, 17), (23, 17), (16, 19), (18, 19), (21, 19), (23, 19)])
    t.road(27, 0, 28, 14)                 # Route 3 north (to Briarwick, closed for now)
    t.stamp("gym", 17, 5)                 # door (20, 9)
    t.road(19, 10, 21, 10)
    t.stamp("house4", 2, 11, "houseA")    # door (3, 14)
    t.stamp("pc", 8, 11)                  # door (9, 14)
    t.stamp("mart", 30, 11)               # door (31, 14)
    t.stamp("house4", 35, 11, "houseB")   # door (36, 14)
    t.crops(16, 24, 23, 27)               # the field
    t.open(14, 22, 25, 28)
    t.bench(15, 22); t.bench(22, 22)
    t.fence(14, 25, 23)
    t.flowers([(14, 10), (25, 10), (12, 17), (27, 17)])
    t.open(0, 17, 2, 18); t.open(37, 17, 39, 18)
    # Route 1's grass path runs in to x 1, then blends into the town's sand (path_blend.py tiles in Petalburg)
    for x in (0, 1): t.put(x, 15, 465); t.put(x, 16, 481)
    t.put(2, 15, 656); t.put(3, 15, 657); t.put(2, 16, 660); t.put(3, 16, 661)
    SIGNS = {"town": (1, 17), "gym": (22, 10), "route3": (26, 2), "route2": (38, 17), "farm": (19, 22)}
    for x, y in SIGNS.values(): t.sign(x, y)
    return t, SIGNS

if __name__ == "__main__":
    t, SIGNS = layout()
    g = t.build()
    d = V / "data/layouts/Crestfall"; d.mkdir(parents=True, exist_ok=True)
    g.astype("<u2").tofile(d / "map.bin")
    (d / "border.bin").write_bytes((V / "data/layouts/Route102/border.bin").read_bytes())

    def jload(p): return json.load(open(V / p))
    def jdump(p, o): open(V / p, "w").write(json.dumps(o, indent=2, ensure_ascii=False) + "\n")
    L = jload("data/layouts/layouts.json")
    if not any(l["id"] == "LAYOUT_CRESTFALL" for l in L["layouts"]):
        i = next(i for i, l in enumerate(L["layouts"]) if l["id"] == "LAYOUT_VELDRIS_ROUTE1")
        L["layouts"].insert(i + 1, {"id": "LAYOUT_CRESTFALL", "name": "Crestfall_Layout", "width": 40, "height": 32,
            "primary_tileset": "gTileset_General", "secondary_tileset": "gTileset_Petalburg",
            "border_filepath": "data/layouts/Crestfall/border.bin", "blockdata_filepath": "data/layouts/Crestfall/map.bin",
            "layout_version": "emerald"})
        jdump("data/layouts/layouts.json", L)
    MG = jload("data/maps/map_groups.json"); grp = MG["gMapGroup_TownsAndRoutes"]
    if "Crestfall" not in grp: grp.insert(grp.index("VeldrisRoute1") + 1, "Crestfall"); jdump("data/maps/map_groups.json", MG)
    es = V / "data/event_scripts.s"; s = es.read_text(); inc = '\t.include "data/maps/Crestfall/scripts.inc"\n'
    if inc not in s: es.write_text(s.rstrip("\n") + "\n" + inc)

    sign = lambda x, y, scr: {"type": "sign", "x": x, "y": y, "elevation": 0, "player_facing_dir": "BG_EVENT_PLAYER_FACING_ANY", "script": scr}
    M = {"id": "MAP_CRESTFALL", "name": "Crestfall", "layout": "LAYOUT_CRESTFALL", "music": "MUS_PETALBURG",
         "region": "REGION_HOENN", "region_map_section": "MAPSEC_CRESTFALL", "requires_flash": False, "weather": "WEATHER_SUNNY",
         "map_type": "MAP_TYPE_TOWN", "allow_cycling": True, "allow_escaping": False, "allow_running": True, "show_map_name": True,
         "battle_scene": "MAP_BATTLE_SCENE_NORMAL",
         "connections": [{"map": "MAP_VELDRIS_ROUTE1", "offset": 5, "direction": "left"}],
         "object_events": [], "warp_events": [], "coord_events": [],
         "bg_events": [sign(*SIGNS["town"], "Crestfall_EventScript_TownSign"), sign(*SIGNS["gym"], "Crestfall_EventScript_GymSign"),
                       sign(*SIGNS["route3"], "Crestfall_EventScript_Route3Sign"), sign(*SIGNS["route2"], "Crestfall_EventScript_Route2Sign"),
                       sign(*SIGNS["farm"], "Crestfall_EventScript_FarmSign")]}
    (V / "data/maps/Crestfall").mkdir(exist_ok=True)
    jdump("data/maps/Crestfall/map.json", M)
    R = jload("data/maps/VeldrisRoute1/map.json")
    R["connections"] = [c for c in R["connections"] if c["map"] != "MAP_CRESTFALL"] + [{"map": "MAP_CRESTFALL", "offset": -5, "direction": "right"}]
    jdump("data/maps/VeldrisRoute1/map.json", R)
    print("doors", t.doors)
