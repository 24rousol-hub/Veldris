"""Three Crestfall concepts in LeoB General + Petalburg. Renders only, nothing is installed."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw
from leob_town import Town
OUT = Path(__file__).parent

# ---------------- renderer (General + Petalburg)
V = Path("/home/claude/veldris")
def read_pal(p):
    t = Path(p).read_text().split(); n = int(t[2]); return [tuple(int(x) for x in t[3+i*3:6+i*3]) for i in range(n)]
def tiles(p):
    a = np.array(Image.open(p)) & 15
    return [a[y*8:(y+1)*8, x*8:(x+1)*8] for y in range(a.shape[0]//8) for x in range(a.shape[1]//8)]
prim, sec = V / "data/tilesets/primary/general", V / "data/tilesets/secondary/petalburg"
pt, st = tiles(prim / "tiles.png"), tiles(sec / "tiles.png")
pals = {i: read_pal(prim / f"palettes/{i:02d}.pal") for i in range(6)}
pals.update({i: read_pal(sec / f"palettes/{i:02d}.pal") for i in range(6, 13)})
pm = np.frombuffer((prim / "metatiles.bin").read_bytes(), "<u2"); sm = np.frombuffer((sec / "metatiles.bin").read_bytes(), "<u2")
cache = {}
def meta(mid):
    if mid in cache: return cache[mid]
    ent = (pm if mid < 512 else sm)[(mid if mid < 512 else mid - 512) * 8:][:8]
    img = np.zeros((16, 16, 3), np.uint8)
    for g in range(2):
        for k in range(4):
            e = int(ent[g * 4 + k]); idx, hf, vf, pal = e & 0x3FF, (e >> 10) & 1, (e >> 11) & 1, e >> 12
            t = pt[idx] if idx < 512 else (st[idx - 512] if idx - 512 < len(st) else np.zeros((8, 8), np.uint8))
            if hf: t = t[:, ::-1]
            if vf: t = t[::-1]
            ox, oy = (k % 2) * 8, (k // 2) * 8
            for y in range(8):
                for x in range(8):
                    if t[y, x]: img[oy + y, ox + x] = pals[pal][t[y, x]]
    cache[mid] = img; return img
HEDGE = True
def render(t, g, name, title):
    H, W = g.shape
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y*16:y*16+16, x*16:x*16+16] = meta(int(g[y, x]) & 0x3FF)
    S = 2
    im = Image.fromarray(img).resize((W * 16 * S, H * 16 * S), Image.NEAREST)
    d = ImageDraw.Draw(im)
    for label, (x, y) in t.doors.items():
        d.rectangle([x*32+1, y*32+1, x*32+30, y*32+30], outline=(255, 230, 0), width=2)
    for x, y, txt in t.notes:
        d.rectangle([x*32, y*32, x*32 + 7*len(txt) + 6, y*32 + 14], fill=(0, 0, 0)); d.text((x*32 + 3, y*32 + 1), txt, fill=(255, 255, 255))
    bar = Image.new("RGB", (im.width, 40), (25, 25, 25)); ImageDraw.Draw(bar).text((8, 12), title, fill=(255, 255, 255))
    out = Image.new("RGB", (im.width, im.height + 40)); out.paste(bar, (0, 0)); out.paste(im, (0, 40))
    out.save(OUT / name); print(name, W, H, "size check", (W + 15) * (H + 14))

# ---------------- A: the map card (Azalea plan): long street, gym south, Center/Mart north, crop field in place of the barn
def concept_a():
    t = Town(48, 32)
    t.road(0, 21, 12, 22)                 # Route 1 lane from the west
    t.road(8, 16, 40, 18)                 # main sand street
    t.road(12, 16, 14, 26); t.road(12, 24, 30, 26)   # vertical lane and the south loop
    t.road(33, 0, 35, 16)                 # Route 3 north
    t.road(40, 16, 47, 18)                # Route 2 east
    t.stamp("gym", 15, 19)                # door (18, 23)
    t.road(17, 24, 19, 24)
    t.stamp("house5", 15, 8, "houseA"); t.road(16, 12, 18, 15)
    t.stamp("pc", 22, 12); t.road(22, 16, 25, 16)
    t.stamp("mart", 28, 7); t.road(28, 11, 30, 15)
    t.stamp("house4", 27, 20, "houseB"); t.road(27, 24, 30, 24)
    t.crops(2, 12, 9, 14)                 # the farm field where the barn was
    t.crops(13, 4, 18, 5)                 # tomato rows north of House A
    t.open(1, 10, 10, 15); t.open(12, 3, 19, 7)
    t.open(21, 19, 26, 23); t.flowers([(22, 20), (23, 20), (25, 20), (26, 20), (22, 22), (26, 22)])   # market square
    t.sign(10, 20); t.sign(21, 23); t.sign(36, 15); t.sign(26, 19)
    t.open(36, 8, 46, 15); t.pond(39, 9, 44, 13)
    t.notes += [(0, 20, "R1"), (44, 15, "R2"), (31, 0, "R3"), (14, 18, "gym"), (2, 11, "fields"), (21, 18, "market")]
    render(t, t.build(), "crestfall_A_card.png", "A - the map card: long main street, gym on the south loop, Center/Mart north, fields west, pond by the R3 junction")

# ---------------- B: village green: everything faces a square, gym at its head
def concept_b():
    t = Town(40, 32)
    t.road(0, 15, 13, 16)                 # Route 1 from the west
    t.road(26, 15, 39, 16)                # Route 2 east
    t.road(14, 11, 25, 21)                # the square
    t.unroad(16, 13, 23, 19)              # grass island in the middle of the square
    t.pond(17, 14, 22, 17)                # pond on the island
    t.flowers([(16, 13), (18, 13), (21, 13), (23, 13), (16, 15), (23, 15), (16, 17), (23, 17), (16, 19), (18, 19), (21, 19), (23, 19)])
    t.road(27, 0, 28, 14)                 # Route 3 straight down to the main road
    t.stamp("gym", 17, 5)                 # head of the square, door (20, 9)
    t.road(19, 10, 21, 10)
    t.stamp("house4", 2, 11, "houseA")    # door (3, 14) onto the road
    t.stamp("pc", 8, 11)                  # door (9, 14) onto the road
    t.stamp("mart", 30, 11)               # door (31, 14) onto the road; one grass tile before House B
    t.stamp("house4", 35, 11, "houseB")   # door (36, 14) onto the road
    t.crops(16, 24, 23, 27)               # field on the grass south of the square
    t.open(14, 22, 25, 28)
    t.bench(15, 22); t.bench(22, 22)      # benches looking over the field
    t.fence(14, 25, 23)                   # fence along the top of the field: no walking down there
    t.flowers([(14, 10), (25, 10), (12, 17), (27, 17)])
    t.sign(1, 17)                         # town sign at the Route 1 entrance, beside the road
    t.sign(22, 10)                        # gym sign beside the gym's door path
    t.sign(26, 2)                         # Route 3 sign beside its lane
    t.sign(38, 17)                        # Route 2 sign at the east exit
    t.open(0, 17, 2, 18); t.open(37, 17, 39, 18)
    t.notes += [(0, 14, "R1"), (36, 18, "R2"), (25, 0, "R3"), (16, 4, "gym"), (17, 23, "fields")]
    render(t, t.build(), "crestfall_B_green.png", "B - village green: buildings round a square with a pond, gym at its head, fields south")

# ---------------- C: farm road: one long road through fields, gym at the far end by Route 2
def concept_c():
    t = Town(56, 26)
    t.road(0, 12, 55, 13)                 # the farm road, west to east
    t.road(36, 0, 37, 11)                 # Route 3 north from the middle
    t.stamp("pc", 6, 7); t.road(7, 11, 7, 11)
    t.stamp("mart", 12, 7); t.road(13, 11, 13, 11)
    t.stamp("house4", 20, 15, "houseA"); t.road(21, 14, 21, 14)
    t.stamp("house5", 28, 6, "houseB"); t.road(30, 10, 30, 11)
    t.stamp("gym", 46, 6)                 # door (49, 10)
    t.road(48, 11, 50, 11)
    t.crops(4, 17, 15, 20)                # big field south-west
    t.crops(27, 16, 38, 20)               # field south-east of the road
    t.crops(19, 4, 24, 7)                 # small patch north
    t.open(2, 15, 17, 22); t.open(25, 15, 40, 22); t.open(17, 3, 26, 9); t.open(40, 15, 53, 22)
    t.pond(43, 16, 50, 20)
    t.flowers([(5, 14), (11, 14), (24, 11), (33, 11), (44, 11), (52, 11)])
    t.sign(2, 11); t.sign(51, 11); t.sign(35, 11)
    t.notes += [(0, 11, "R1"), (52, 14, "R2"), (34, 0, "R3"), (45, 5, "gym"), (5, 16, "fields"), (28, 15, "fields")]
    render(t, t.build(), "crestfall_C_road.png", "C - farm road: one road through the fields, Center/Mart at the gate, gym at the far end by Route 2")

import sys
if len(sys.argv) > 1 and sys.argv[1] == "open":
    import leob_town
    _orig = leob_town.Town.crops
    leob_town.Town.crops = lambda self, *a, **k: _orig(self, *a, hedge=False)
    _r = render
    concept_b.__globals__["render"] = lambda t, g, name, title: _r(t, g, name.replace(".png", "_open.png"), title + " (fields without hedges)")
    concept_b()
else:
    concept_a(); concept_b(); concept_c()
