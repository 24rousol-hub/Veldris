"""Route 1 (VeldrisRoute1, 60x25): Palladium's Route 29 mirrored left-right (author 2026-10-01) so it runs east
from Hollowbrook. The Route 46 gatehouse at the top is replaced with forest."""
import numpy as np
from g4lib import U, G, mirror, WALK, BLOCK, MB_NORMAL, MB_TALL_GRASS, MB_JUMP_SOUTH

g = [row[:] for row in G["r29"]]
H, W = len(g), len(g[0])
# --- gatehouse (x24-29, rows 0-7) -> forest, copied from the forest block at x16-21
for y in range(0, 6):
    for x in range(24, 30):
        g[y][x] = g[y][x - 8]
for x in range(24, 30):
    g[6][x] = 142 if x % 2 == 0 else 143
    g[7][x] = 135 if x % 2 == 0 else 136
# the trees beside the gate had their sides shaded against it; make them plain forest
for y in range(0, 5):
    g[y][23] = {117: 115, 126: 122}.get(g[y][23], g[y][23])
    g[y][30] = {114: 116, 121: 123}.get(g[y][30], g[y][30])

TREES = {114, 115, 116, 117, 121, 122, 123, 124, 125, 126, 130, 131, 144, 155, 174}
TALL = {154, 159, 160}
LEDGE = {166, 167, 168, 169}
WALL = {150, 172, 173, 176, 180}

ART = [[mirror(U[g[y][W - 1 - x]]) for x in range(W)] for y in range(H)]
SRC = [[g[y][W - 1 - x] for x in range(W)] for y in range(H)]
COLL = [[BLOCK if (t in TREES or t in WALL or t in LEDGE) else WALK for t in row] for row in SRC]
BEH = [[MB_TALL_GRASS if t in TALL else MB_JUMP_SOUTH if t in LEDGE else MB_NORMAL for t in row] for row in SRC]
SEC = [[False] * W for _ in range(H)]
# path to Hollowbrook leaves the west edge on rows 11-13 (top edge, middle, bottom edge)
WEST_PATH_ROWS = (11, 12, 13)

# --- colour-match to New Bark Town: Route 29 is the same art in a brighter palette. Learn the map from tile pairs that
# have identical structure (pines, grass, paths) and shift the remaining colours by their nearest learned neighbour.
def _struct(t):
    cols = {}; return np.array([[cols.setdefault(tuple(p), len(cols)) for p in row] for row in t])
_nb = set(v for r in G["nbt"] for v in r); _r29 = set(v for r in G["r29"] for v in r) - _nb
CMAP = {}
for _a in sorted(_nb):
    for _b in sorted(_r29):
        if (_struct(U[_a]) == _struct(U[_b])).all() and not (U[_a] == U[_b]).all():
            for pa, pb in zip(U[_a].reshape(-1, 3), U[_b].reshape(-1, 3)):
                CMAP[tuple(int(v) for v in pb)] = tuple(int(v) for v in pa)
def _recol(c):
    if c in CMAP: return CMAP[c]
    k = min(CMAP, key=lambda m: sum((p - q) ** 2 for p, q in zip(m, c)))
    return tuple(max(0, min(248, v + (t - s))) for v, s, t in zip(c, k, CMAP[k]))
_lut = {}
for row in ART:
    for t in row:
        flat = t.reshape(-1, 3)
        for i, p in enumerate(flat):
            c = (int(p[0]), int(p[1]), int(p[2]))
            if c not in _lut: _lut[c] = _recol(c)
            flat[i] = _lut[c]

# --- sign posts (New Bark Town's sign, composited onto the route's ground); the sign events are in map.json
from g4lib import composite as _comp
import hollowbrook_g4 as _hb
SIGNS = {"west": (10, 11), "east": (50, 11), "field": (22, 8)}
for _x, _y in SIGNS.values():
    ART[_y][_x] = _comp(U[G["nbt"][8][8]], _hb.nb_bg(8, 8), ART[_y][_x])
    COLL[_y][_x] = BLOCK
