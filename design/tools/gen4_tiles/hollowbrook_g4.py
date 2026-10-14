"""Hollowbrook (32x28) in Gen 4 tiles cut from Palladium's New Bark Town. Same layout as the LeoB version
(author 2026-10-01): doors (13,10) lab, (22,12) Goldsworth, (9,20) player, (17,21) neighbour.
Pine forest is auto-tiled on 2x2 cells (rows 2k+1..2k+2, cols 2k..2k+1, as in New Bark Town).
Buildings, signs, flowers and the pond are composited onto the ground computed under them."""
import numpy as np
from collections import Counter
from g4lib import U, G, composite, mirror, WALK, BLOCK, MB_NORMAL, MB_POND_WATER, MB_NON_ANIMATED_DOOR

NB = G["nbt"]; NW, NH = 32, 28
W, H = 32, 28

# ------------------------------------------------------------------ pine forest rules (learned from New Bark Town)
def tree_tile(left, upper, N, S, E, Wc, NE):
    if upper:
        if left: return 2 if (N and Wc) else (91 if (not N and not Wc) else 18)
        return 3 if (E and NE) else 12
    if left: return (0 if Wc else 58) if S else (4 if Wc else 79)
    return (1 if E else 19) if S else (5 if E else 54)

def grass_tile(left, upper, N, S):
    if upper: return 13 if N else (32 if left else 33)
    return (87 if left else 88) if S else (20 if left else 21)

# ------------------------------------------------------------------ path rules, learned from New Bark Town by 8-neighbour context
PATH = {59, 60, 61, 62, 63, 64, 71, 72, 80, 85, 86, 96, 97, 102, 110, 113}
PATHISH = PATH | {89, 90, 92, 93, 94, 95, 98, 99, 100, 101, 107, 111, 49, 75}
def nb_isp(x, y):
    x = min(max(x, 0), NW - 1); y = min(max(y, 0), NH - 1)
    return NB[y][x] in PATHISH
OFF8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
k8, k4 = {}, {}
for y in range(NH):
    for x in range(NW):
        t = NB[y][x]
        if t not in PATH: continue
        key = tuple(nb_isp(x + dx, y + dy) for dx, dy in OFF8)
        k8.setdefault(key, Counter())[t] += 1
        k4.setdefault((key[1], key[3], key[4], key[6]), Counter())[t] += 1

def path_tile(isp, x, y):
    key = tuple(isp(x + dx, y + dy) for dx, dy in OFF8)
    if key in k8: return k8[key].most_common(1)[0][0]
    # inner corners missing from the sample: interior with one diagonal gap
    k = (key[1], key[3], key[4], key[6])
    if k in k4: return k4[k].most_common(1)[0][0]
    return 62

def ground(x, y, tree, isp):
    if isp(x, y): return path_tile(isp, x, y)
    cy, upper = (y - 1) // 2, (y - 1) % 2 == 0
    cx, left = x // 2, x % 2 == 0
    if tree(cx, cy):
        return tree_tile(left, upper, tree(cx, cy - 1), tree(cx, cy + 1), tree(cx + 1, cy), tree(cx - 1, cy), tree(cx + 1, cy - 1))
    return grass_tile(left, upper, tree(cx, cy - 1), tree(cx, cy + 1))

# New Bark Town's own semantics, used to predict what was under each building in the source picture
def nb_tree(cx, cy):
    if not (0 <= cx < 16 and 0 <= cy < 14): return True
    return NB[2 * cy + 1][2 * cx] in {2, 3, 12, 18, 91, 108}
def nb_bg(x, y): return U[ground(x, y, nb_tree, lambda a, b: False)]

# ------------------------------------------------------------------ Hollowbrook semantics
TREE_CELLS = set()
for cx in range(16):
    for cy in range(-1, 14):
        t = (cy <= 1 or cx in (0, 1) or (cx == 2 and cy in (2, 3)) or (cx in (12, 13) and cy in (2, 3))
             or (cx in (14, 15) and (cy <= 3 or cy >= 8)) or (cx == 13 and cy >= 8) or cy >= 12
             or (cy == 11 and not 4 <= cx <= 9))
        if t: TREE_CELLS.add((cx, cy))
def tree(cx, cy):
    if not (0 <= cx < 16 and -1 <= cy < 14): return True
    return (cx, cy) in TREE_CELLS

P = set()
def rect(x0, x1, y0, y1):
    for yy in range(y0, y1 + 1):
        for xx in range(x0, x1 + 1): P.add((xx, yy))
rect(6, 25, 13, 14); rect(12, 14, 11, 12); rect(24, 25, 9, 12); rect(24, 31, 9, 11); rect(12, 14, 15, 21); rect(8, 18, 22, 23); rect(8, 10, 21, 21)
DOORS = {"player": (9, 20), "lab": (13, 10), "neighbour": (17, 21), "goldsworth": (22, 12)}
def isp(x, y):
    x = min(max(x, 0), W - 1); y = min(max(y, 0), H - 1)
    return (x, y) in P or (x, y) in DOORS.values()

ART = [[U[ground(x, y, tree, isp)].copy() for x in range(W)] for y in range(H)]
BG = [[a.copy() for a in row] for row in ART]
COLL = [[BLOCK if (not isp(x, y) and tree(x // 2, (y - 1) // 2)) else WALK for x in range(W)] for y in range(H)]
BEH = [[MB_NORMAL] * W for _ in range(H)]
SEC = [[False] * W for _ in range(H)]

def stamp(sx, sy, w, rows, tx, ty, flip=False, ring_only=True, door=None, sec=True, block=True, beh=MB_NORMAL):
    """Copy New Bark Town tiles (cols sx..sx+w-1, the listed source rows) to (tx, ty). Outer ring is composited."""
    for j, ry in enumerate(rows):
        for i in range(w):
            si = (w - 1 - i) if flip else i
            obj, objbg = U[NB[ry][sx + si]], nb_bg(sx + si, ry)
            if flip: obj, objbg = mirror(obj), mirror(objbg)
            x, y = tx + i, ty + j
            ring = j == 0 or i == 0 or i == w - 1
            ART[y][x] = composite(obj, objbg, BG[y][x]) if (ring or not ring_only) else obj.copy()
            COLL[y][x] = BLOCK if block else WALK
            BEH[y][x] = beh
            SEC[y][x] = sec
    if door:
        dx, dy = door; COLL[dy][dx] = WALK; BEH[dy][dx] = MB_NON_ANIMATED_DOOR

stamp(9, 4, 7, [4, 5, 6, 7, 8], 10, 6, door=DOORS["lab"])                         # Prof. Fennick's lab
stamp(19, 6, 5, [6, 7, 8, 9, 10], 19, 8, flip=True, door=DOORS["goldsworth"])     # Goldsworth house (locked)
stamp(19, 6, 5, [6, 7, 8, 9, 10], 6, 16, flip=True, door=DOORS["player"])         # player's house
stamp(19, 6, 5, [6, 7, 8, 10], 16, 18, door=DOORS["neighbour"])                  # neighbour's house
BEH[12][22] = MB_NORMAL; COLL[12][22] = BLOCK                                    # Goldsworth door is locked (sign event)

# pond: NBT x26-31 rows 11-16 -> rows 12-16 here (rim, 3 water rows, rocky rim with the trees' tips)
for j, ry in enumerate([11, 12, 13, 14, 16]):
    for i in range(6):
        x, y = 26 + i, 12 + j
        obj = U[NB[ry][26 + i]]
        if j == 0 or i == 0: ART[y][x] = composite(obj, nb_bg(26 + i, ry), BG[y][x])
        else: ART[y][x] = obj.copy()
        COLL[y][x] = BLOCK; BEH[y][x] = MB_POND_WATER if (0 < j < 4 and i > 0) else MB_NORMAL

def small(src, x, y, block):
    sx, sy = src
    ART[y][x] = composite(U[NB[sy][sx]], nb_bg(sx, sy), BG[y][x])
    COLL[y][x] = BLOCK if block else WALK
for x, y in [(6, 8), (7, 8), (6, 9), (17, 10), (5, 15), (5, 16), (11, 17), (11, 18), (21, 19), (22, 20), (20, 15), (21, 16)]:
    if not isp(x, y) and COLL[y][x] == WALK: small((4, 19), x, y, False)        # red flowers
SIGNS = {"town": (15, 16), "lab": (8, 10), "goldsworth": (18, 12), "player": (11, 20)}
for x, y in SIGNS.values(): small((8, 8), x, y, True)
EXIT_ROWS = (9, 10, 11)
