"""Shared helpers: Palladium art loading, compositing, and a dual-layer tileset compiler (flat art -> pokeemerald files)."""
import numpy as np, json
from pathlib import Path
from PIL import Image
from tiles import grid

HERE = Path(__file__).parent
U = np.load(HERE / "uniq.npy").astype(np.uint8)          # unique 16x16 metatile art, 5-bit quantised
G = json.load(open(HERE / "grids.json"))                  # 'nbt' and 'r29' index grids into U
REMAP = {}
if (HERE / "remap.json").exists():                        # near-identical colours merged to fit the palettes
    REMAP = {tuple(json.loads(k)): tuple(v) for k, v in json.load(open(HERE / "remap.json")).items()}
    for a, b in REMAP.items():
        U[(U == np.array(a, np.uint8)).all(-1)] = b

# behaviours (value = enum index in include/constants/metatile_behaviors.h)
MB_NORMAL, MB_TALL_GRASS, MB_POND_WATER, MB_JUMP_SOUTH, MB_NON_ANIMATED_DOOR = 0, 2, 16, 59, 96
WALK, BLOCK = 0x3000, 0x3400                               # elevation 3, collision 0 / 1

def composite(obj, obj_bg, target_bg):
    """Keep the pixels where obj differs from the background it was drawn on; fill the rest from target_bg."""
    mask = (obj != obj_bg).any(2)
    out = target_bg.copy(); out[mask] = obj[mask]
    return out

def mirror(a): return a[:, ::-1].copy()

# ---------------------------------------------------------------- compiler
def tiles8(m):
    return [m[y:y+8, x:x+8] for y in (0, 8) for x in (0, 8)]

def colkey(t):
    return frozenset(map(tuple, t.reshape(-1, 3)))

def pack_palettes(colsets, npal, start=0, existing=None):
    """Try greedy packing in many orders, then agglomerative merging; return the first that fits."""
    import random
    sets = list(set(colsets))
    try:
        return _pack(sets, npal, existing)
    except SystemExit:
        pass
    fixed = [set(p) for p in (existing or [])]
    rest = [s for s in sets if not any(s <= p for p in fixed)]
    # agglomerative: merge the pair with the smallest union until few enough
    cl = [set(s) for s in rest]
    cl = [c for c in cl if not any(c < d for d in cl)]
    while len(cl) > npal:
        best = None
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                u = len(cl[i] | cl[j])
                if u <= 15:
                    score = u - max(len(cl[i]), len(cl[j]))
                    if best is None or score < best[0]: best = (score, i, j)
        if best is None: break
        _, i, j = best
        cl[i] |= cl[j]; del cl[j]
    if len(cl) <= npal:
        return fixed + cl, {}
    rng = random.Random(1)
    base = sorted(rest, key=lambda c: (-len(c), sorted(c)))
    for attempt in range(4000):
        # randomised agglomerative merging
        cl = [set(c) for c in base]
        cl = [c for c in cl if not any(c < d for d in cl)]
        while len(cl) > npal:
            cands = []
            for i in range(len(cl)):
                for j in range(i + 1, len(cl)):
                    u = len(cl[i] | cl[j])
                    if u <= 15: cands.append((u - max(len(cl[i]), len(cl[j])) + rng.random() * (attempt % 7), i, j))
            if not cands: break
            _, i, j = min(cands)
            cl[i] |= cl[j]; del cl[j]
        if len(cl) <= npal:
            return fixed + cl, {}
    raise SystemExit(f"palette overflow: need more than {npal} palettes")

def _pack(colsets, npal, existing=None, keep_order=False):
    """Greedy bin packing of colour sets into palettes of <=15 colours. Returns list of palettes (sets) and assignment."""
    pals = [set(p) for p in (existing or [])]
    fixed = len(pals)
    assign = {}
    for cs in (colsets if keep_order else sorted(set(colsets), key=lambda s: -len(s))):
        if any(cs <= pals[i] for i in range(fixed)):      # fits an existing (read-only) palette
            continue
        best, bestadd = None, 99
        for i, p in enumerate(pals):
            if i < fixed: continue
            add = len(cs - p)
            if len(p | cs) <= 15 and add < bestadd:
                best, bestadd = i, add
        if best is None:
            if len(pals) - fixed >= npal:
                raise SystemExit(f"palette overflow: need more than {npal} palettes")
            pals.append(set(cs)); best = len(pals) - 1
        else:
            pals[best] |= cs
        assign[cs] = best
    return pals, assign

class Tileset:
    def __init__(self, base_tile=0, base_pal=0, max_tiles=512, max_pals=6):
        self.tiles = []          # 8x8 index arrays (uint8)
        self.tile_lookup = {}    # bytes -> (index, hflip, vflip)
        self.base_tile, self.base_pal = base_tile, base_pal
        self.max_tiles, self.max_pals = max_tiles, max_pals
        self.pals = []
        self.add_blank()

    def add_blank(self):
        z = np.zeros((8, 8), np.uint8)
        self.tiles.append(z); self.tile_lookup[z.tobytes()] = (0, 0, 0)

    def find_or_add(self, idx8, lookups):
        for lk in lookups:
            for hf in (0, 1):
                for vf in (0, 1):
                    t = idx8
                    if hf: t = t[:, ::-1]
                    if vf: t = t[::-1]
                    k = np.ascontiguousarray(t).tobytes()
                    if k in lk.tile_lookup:
                        i, h0, v0 = lk.tile_lookup[k]
                        return lk.base_tile + i, hf ^ h0, vf ^ v0
        self.tiles.append(idx8.copy())
        i = len(self.tiles) - 1
        if i >= self.max_tiles: raise SystemExit("tile overflow")
        self.tile_lookup[idx8.tobytes()] = (i, 0, 0)
        return self.base_tile + i, 0, 0

def to_index(t8, pal):
    order = pal
    lut = {c: i + 1 for i, c in enumerate(order)}
    return np.array([[lut[tuple(px)] for px in row] for row in t8], np.uint8)

def compile_pair(prim_arts, sec_arts):
    """prim_arts / sec_arts: lists of 16x16x3 arrays. Returns (primary, secondary, prim_entries, sec_entries, palettes)."""
    p_sets = [colkey(t) for m in prim_arts for t in tiles8(m)]
    p_pals, _ = pack_palettes(p_sets, 6)
    s_sets = [colkey(t) for m in sec_arts for t in tiles8(m)]
    # secondary tiles may use primary palettes when they fit, otherwise palettes 6-12
    all_pals, _ = pack_palettes([s for s in s_sets], 7, existing=p_pals)
    pals = [sorted(p) for p in all_pals]
    while len(pals) < 6: pals.insert(len(p_pals), [])
    def best_pal(cs, allowed):
        for i in allowed:
            if cs <= set(pals[i]): return i
        raise SystemExit("no palette fits a tile")
    prim = Tileset(0, 0, 512, 6); sec = Tileset(512, 6, 512, 7)
    def entries(arts, ts, lookups, allowed):
        out = []
        for m in arts:
            e = []
            for t in tiles8(m):
                pi = best_pal(colkey(t), allowed)
                idx8 = to_index(t, pals[pi])
                ti, hf, vf = ts.find_or_add(idx8, lookups)
                e.append(ti | (hf << 10) | (vf << 11) | (pi << 12))
            e += [0 | (0 << 12)] * 4                     # top layer: transparent tile 0
            out.append(e)
        return out
    pe = entries(prim_arts, prim, [prim], range(len(p_pals)))
    se = entries(sec_arts, sec, [prim, sec], range(len(pals)))
    return prim, sec, pe, se, pals

def write_tileset(dirpath, ts, entries, attrs, pals, pal_range, num_tiles_pad=None):
    d = Path(dirpath); (d / "palettes").mkdir(parents=True, exist_ok=True)
    n = len(ts.tiles)
    rows = (n + 15) // 16
    if num_tiles_pad: rows = max(rows, (num_tiles_pad + 15) // 16)
    img = np.zeros((rows * 8, 128), np.uint8)
    for i, t in enumerate(ts.tiles):
        y, x = divmod(i, 16); img[y*8:y*8+8, x*8:x*8+8] = t
    im = Image.fromarray(img, "P")
    gray = []
    for i in range(16): gray += [i * 17] * 3
    im.putpalette(gray + [0] * (768 - 48)); im.save(d / "tiles.png")
    for i in range(16):
        cols = [(0, 0, 0)] * 16
        if i in pal_range and i < len(pals):
            cols = [(255, 0, 255)] + [tuple(int(v) for v in c) for c in pals[i]] + [(0, 0, 0)] * (15 - len(pals[i]))
        with open(d / "palettes" / f"{i:02d}.pal", "w", newline="\r\n") as f:
            f.write("JASC-PAL\n0100\n16\n" + "".join(f"{r} {g} {b}\n" for r, g, b in cols))
    np.array(entries, "<u2").tofile(d / "metatiles.bin")
    np.array(attrs, "<u2").tofile(d / "metatile_attributes.bin")
    return n
