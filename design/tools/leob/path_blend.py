"""Grass path (pale green, General palette 2) to sand path (General palette 5) blend metatiles, added to the end of
gTileset_Petalburg (author asked 2026-10-01). Both source paths are vanilla/LeoB General metatiles; the blend is made
pixel by pixel from them along a ragged edge, with a darker sand rim where sand meets the grass path.

The two paths use different palettes, so the blend tiles use the Petalburg secondary's empty palette 11, filled
with the colours of both paths (10 of 15 slots).

Re-runnable: it trims Petalburg back to its original 144 metatiles / 160 tiles before appending.

Metatile ids (secondary ids start at 512):
  horizontal road, grass path on the WEST, sand on the EAST (2 wide: A then B)
    656/657 top edge, 658/659 middle, 660/661 bottom edge
  the same mirrored (sand WEST, grass path EAST): 662/663, 664/665, 666/667  (A then B, west to east)
  vertical road, grass path NORTH, sand SOUTH (2 tall: A above B)
    668/669 west edge, 670/671 middle, 672/673 east edge   (each pair: upper, lower)
  the same flipped (sand NORTH, grass path SOUTH): 674/675, 676/677, 678/679
"""
import json, sys
import numpy as np
from pathlib import Path
from PIL import Image

V = Path(__file__).resolve().parents[3]
PRIM, SEC = V / "data/tilesets/primary/general", V / "data/tilesets/secondary/petalburg"
BASE_META, BASE_TILES, PAL = 144, 160, 11

def read_pal(p):
    t = Path(p).read_text().split(); n = int(t[2]); return [tuple(int(x) for x in t[3 + i * 3:6 + i * 3]) for i in range(n)]
ptiles = np.array(Image.open(PRIM / "tiles.png")) & 15
pmeta = np.frombuffer((PRIM / "metatiles.bin").read_bytes(), "<u2")
ppals = {i: read_pal(PRIM / f"palettes/{i:02d}.pal") for i in range(6)}

def tile(i): return ptiles[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8]
def meta_rgb(mid):
    """16x16 RGB of a primary metatile's bottom layer."""
    out = np.zeros((16, 16, 3), np.uint8)
    for k in range(4):
        e = int(pmeta[mid * 8 + k]); t = tile(e & 0x3FF)
        if (e >> 10) & 1: t = t[:, ::-1]
        if (e >> 11) & 1: t = t[::-1]
        pal = ppals[e >> 12]
        out[(k // 2) * 8:(k // 2) * 8 + 8, (k % 2) * 8:(k % 2) * 8 + 8] = np.array([pal[c] for c in t.flatten()]).reshape(8, 8, 3)
    return out

# palette 11: both paths' colours. Sand palette 5 index 15 is the same green as grass index 13.
P11 = [(24, 41, 82),
       (148, 198, 175), (73, 165, 126), (16, 135, 54), (33, 125, 86), (4, 112, 32),        # grass path + grass
       (206, 189, 115), (201, 158, 94), (185, 142, 78), (229, 221, 147)]                   # sand
P11 += [(0, 0, 0)] * (16 - len(P11))
LUT = {c: i for i, c in enumerate(P11)}
GRASSPATH, SAND = {(148, 198, 175)}, {(206, 189, 115), (229, 221, 147)}
RIM = (201, 158, 94)

rng = np.random.default_rng(7)
def edge_profile(n, lo, hi):
    """A wavy, ragged boundary between lo and hi, one value per row. One full wave over 16 rows, so the edge
    tiles line up with each other on a road of any height."""
    mid, amp = (lo + hi) / 2, (hi - lo) / 2 - 2
    return [int(round(mid + amp * np.sin(2 * np.pi * y / n + 0.6) + rng.integers(-1, 2))) for y in range(n)]

def blend(pale, sand, prof):
    """pale/sand: H x W RGB strips (west to east). prof[y] = first sand column in row y."""
    H, W, _ = pale.shape
    sand_mask = np.zeros((H, W), bool)
    for y in range(H): sand_mask[y, prof[y]:] = True
    img = np.where(sand_mask[..., None], sand, pale).copy()
    # a few stray grains each side of the edge
    for y in range(H):
        for dx in (-6, -5, -4, -3, -2, 2, 3, 4):
            x = prof[y] + dx
            chance = 0.45 if abs(dx) <= 3 else 0.2
            if 0 <= x < W and rng.random() < chance:
                src = sand if dx < 0 else pale
                if tuple(src[y, x]) in (SAND if dx < 0 else GRASSPATH) and tuple(img[y, x]) in (GRASSPATH | SAND):
                    img[y, x] = src[y, x]
    # darker sand rim where sand touches the grass path
    out = img.copy()
    for y in range(H):
        for x in range(W):
            if tuple(img[y, x]) in SAND:
                for ny, nx in ((y, x - 1), (y - 1, x), (y + 1, x), (y, x + 1)):
                    if 0 <= ny < H and 0 <= nx < W and tuple(img[ny, nx]) in GRASSPATH:
                        if rng.random() < 0.55: out[y, x] = RIM
                        break
    return out

def strip(ids):
    return np.concatenate([meta_rgb(m) for m in ids], axis=1)

# horizontal: roles (pale metatile, sand metatile). Two tiles wide: pale|pale -> blend -> sand|sand.
H_ROLES = [(465, 281), (473, 289), (481, 297)]
V_ROLES = [(472, 288), (473, 289), (474, 290)]
h_prof = edge_profile(16, 8, 24)                        # same edge for every role so they line up
v_prof = edge_profile(16, 8, 24)
pieces = []                                              # 16x32 (h) or 32x16 (v) images in the order of the ids above
for pm_, sm_ in H_ROLES:
    pieces.append(("h", blend(strip([pm_, pm_]), strip([sm_, sm_]), h_prof)))
for pm_, sm_ in V_ROLES:
    a = strip([pm_, pm_]).transpose(1, 0, 2); b = strip([sm_, sm_]).transpose(1, 0, 2)   # not used directly
    pale = np.concatenate([meta_rgb(pm_), meta_rgb(pm_)], axis=0).transpose(1, 0, 2)    # 16 wide x 32 tall -> rows as columns
    sand = np.concatenate([meta_rgb(sm_), meta_rgb(sm_)], axis=0).transpose(1, 0, 2)
    pieces.append(("v", blend(pale, sand, v_prof).transpose(1, 0, 2)))

# ---- write: tiles, metatiles, attributes, palette
st = Image.open(SEC / "tiles.png"); spal = st.getpalette()
sa = np.array(st)[: BASE_TILES // 16 * 8]
smeta = list(np.frombuffer((SEC / "metatiles.bin").read_bytes(), "<u2")[: BASE_META * 8])
sattr = list(np.frombuffer((SEC / "metatile_attributes.bin").read_bytes(), "<u2")[:BASE_META])
new_tiles = []
def add_tile(t8):
    new_tiles.append(t8); return 512 + BASE_TILES + len(new_tiles) - 1
def to_idx(rgb): return np.array([[LUT[tuple(p)] for p in row] for row in rgb], np.uint8)
def metatile_entries(img16):
    """4 bottom-layer entries for a 16x16 image (new tiles), 4 empty top entries."""
    ix = to_idx(img16); ent = []
    for k in range(4):
        ent.append((PAL << 12) | add_tile(ix[(k // 2) * 8:(k // 2) * 8 + 8, (k % 2) * 8:(k % 2) * 8 + 8]))
    return ent + [0, 0, 0, 0]
def flipped(ent, h, v):
    """Same tiles, metatile flipped: swap quadrant order and set the tile flip bits."""
    q = ent[:4]
    if h: q = [q[1], q[0], q[3], q[2]]
    if v: q = [q[2], q[3], q[0], q[1]]
    return [e ^ ((h << 10) | (v << 11)) for e in q] + [0, 0, 0, 0]

H_out, Hm, V_out, Vm = [], [], [], []
for kind, img in pieces:
    if kind == "h":
        A, B = metatile_entries(img[:, :16]), metatile_entries(img[:, 16:])
        H_out += [A, B]; Hm += [flipped(B, 1, 0), flipped(A, 1, 0)]          # mirrored: west to east
    else:
        A, B = metatile_entries(img[:16]), metatile_entries(img[16:])
        V_out += [A, B]; Vm += [flipped(B, 0, 1), flipped(A, 0, 1)]          # flipped: upper, lower
for ent in H_out + Hm + V_out + Vm:
    smeta += ent; sattr.append(0)                       # plain walkable ground, like the paths

rows = (len(new_tiles) + 15) // 16
add = np.zeros((rows * 8, 128), np.uint8)
for i, t in enumerate(new_tiles): add[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
out = Image.fromarray(np.concatenate([sa, add]), "P"); out.putpalette(spal); out.save(SEC / "tiles.png")
np.array(smeta, "<u2").tofile(SEC / "metatiles.bin")
np.array(sattr, "<u2").tofile(SEC / "metatile_attributes.bin")
(SEC / f"palettes/{PAL:02d}.pal").write_text("JASC-PAL\n0100\n16\n" + "".join(f"{r} {g} {b}\n" for r, g, b in P11))
print("metatiles", len(smeta) // 8, "tiles", BASE_TILES + len(new_tiles))
