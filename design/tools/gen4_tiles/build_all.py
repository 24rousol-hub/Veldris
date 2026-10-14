"""Compile the Gen 4 outdoor primary + Hollowbrook secondary from both maps, write tilesets and map blocks into the repo."""
import numpy as np, json
from pathlib import Path
import g4lib, hollowbrook_g4 as hb, route1_g4 as r1

V = Path("/home/claude/veldris")
maps = [("Hollowbrook", hb), ("VeldrisRoute1", r1)]

prim, sec = {}, {}          # (art bytes, beh) -> local index
prim_arts, prim_beh, sec_arts, sec_beh = [], [], [], []
def reg(art, beh, is_sec):
    k = (art.tobytes(), beh)
    if k in prim: return prim[k]
    if not is_sec:
        prim[k] = len(prim_arts); prim_arts.append(art); prim_beh.append(beh); return prim[k]
    if k not in sec:
        sec[k] = 512 + len(sec_arts); sec_arts.append(art); sec_beh.append(beh)
    return sec[k]

# primary first: every non-building tile of every map
ids = {}
for name, m in maps:
    for y in range(len(m.ART)):
        for x in range(len(m.ART[0])):
            if not m.SEC[y][x]: reg(m.ART[y][x], m.BEH[y][x], False)
for name, m in maps:
    H, W = len(m.ART), len(m.ART[0])
    ids[name] = [[reg(m.ART[y][x], m.BEH[y][x], m.SEC[y][x]) | m.COLL[y][x] for x in range(W)] for y in range(H)]
print("metatiles: primary", len(prim_arts), "secondary", len(sec_arts))
assert len(prim_arts) <= 512 and len(sec_arts) <= 512

P, S, pe, se, pals = g4lib.compile_pair(prim_arts, sec_arts)
print("8x8 tiles: primary", len(P.tiles), "secondary", len(S.tiles), "palettes", [len(p) for p in pals])
attr = lambda b: b | (0 << 12)   # layer type normal
g4lib.write_tileset(V / "data/tilesets/primary/gen4_outdoor", P, pe, [attr(b) for b in prim_beh], pals, range(0, 6))
g4lib.write_tileset(V / "data/tilesets/secondary/gen4_hollowbrook", S, se, [attr(b) for b in sec_beh], pals, range(6, 13))

# borders: forest, matching GetBorderBlockAt's ((x+1)&1, (y+1)&1) indexing. NBT pines for Hollowbrook, R29 trees for the route
def border(m, ys, xs, name):
    b = []
    for y in ys:
        for x in xs: b.append(ids[name][y][x])
    return b
for name, m in maps:
    d = V / f"data/layouts/{name}"; d.mkdir(parents=True, exist_ok=True)
    np.array([v for row in ids[name] for v in row], "<u2").tofile(d / "map.bin")
# border = a 2x2 forest block taken from a fully forested corner, aligned so (x+1)&1/(y+1)&1 continues the map's own pattern
hbg = ids["Hollowbrook"]; np.array([hbg[26][0], hbg[26][1], hbg[27][0], hbg[27][1]], "<u2").tofile(V / "data/layouts/Hollowbrook/border.bin")
rg = ids["VeldrisRoute1"]; np.array([rg[24][0], rg[24][1], rg[23][0], rg[23][1]], "<u2").tofile(V / "data/layouts/VeldrisRoute1/border.bin")
json.dump({"prim": len(prim_arts), "sec": len(sec_arts)}, open(Path(__file__).parent / "counts.json", "w"))
