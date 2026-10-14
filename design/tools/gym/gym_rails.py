"""Adds north-south railing metatiles to gTileset_PetalburgGym (author approved 2026-10-08), drawn the Gen 3 way
(post tops seen from above, like Route 117's fence) from the gym railing's own colours (palette 6).
Re-runnable: trims the tileset back to its vanilla 224 metatiles / 148 tiles first.
New metatile ids: 736 straight, 737 top end, 738 bottom end (front post), 739 join to a railing on the right,
740 join to a railing on the left."""
import re
import numpy as np
from pathlib import Path
from PIL import Image
import vrail
from mrender import TS
V = Path(__file__).resolve().parents[3]
D = V / "data/tilesets/secondary/petalburg_gym"
BASE_META, BASE_TILES, PAL = 224, 148, 6
ts = TS("gTileset_Building", "gTileset_PetalburgGym")
floor, rail = ts.meta(513), ts.meta(560)
imgs = [vrail.mid(floor), vrail.end_top(floor), vrail.end_bottom(rail, floor), vrail.junction(floor, rail, "r"), vrail.junction(floor, rail, "l")]
pal = [tuple(int(x) for x in l.split()) for l in (D / f"palettes/{PAL:02d}.pal").read_text().split("\n")[3:19] if l.strip()]
lut = {c: i for i, c in enumerate(pal)}
tiles_img = Image.open(D / "tiles.png"); spal = tiles_img.getpalette()
a = np.array(tiles_img).copy()
meta = list(np.frombuffer((D / "metatiles.bin").read_bytes(), "<u2")[: BASE_META * 8])
attr = list(np.frombuffer((D / "metatile_attributes.bin").read_bytes(), "<u2")[:BASE_META])
new, index = [], {}
def tile_id(t):
    k = t.tobytes()
    if k not in index:
        index[k] = BASE_TILES + len(new); new.append(t)
    return 512 + index[k]
for img in imgs:
    ix = np.array([[lut[tuple(int(c) for c in p)] for p in row] for row in img], np.uint8)
    ent = [(PAL << 12) | tile_id(ix[(k // 2) * 8:(k // 2) * 8 + 8, (k % 2) * 8:(k % 2) * 8 + 8]) for k in range(4)]
    meta += ent + [0, 0, 0, 0]; attr.append(0)
total = BASE_TILES + len(new)
rows = (total + 15) // 16
if a.shape[0] < rows * 8: a = np.concatenate([a, np.zeros((rows * 8 - a.shape[0], 128), np.uint8)])
for i in range(BASE_TILES, a.shape[0] // 8 * 16):
    a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = 0
for i, t in enumerate(new):
    n = BASE_TILES + i; a[(n // 16) * 8:(n // 16) * 8 + 8, (n % 16) * 8:(n % 16) * 8 + 8] = t
out = Image.fromarray(a, "P"); out.putpalette(spal); out.save(D / "tiles.png")
np.array(meta, "<u2").tofile(D / "metatiles.bin"); np.array(attr, "<u2").tofile(D / "metatile_attributes.bin")
g = V / "src/data/tilesets/graphics.h"; s = g.read_text()
s = re.sub(r'(petalburg_gym/tiles\.png", "\.4bpp\.fastSmol", "-num_tiles )\d+', lambda m: m.group(1) + str(total), s)
g.write_text(s)
print("metatiles", len(meta) // 8, "tiles", total)
