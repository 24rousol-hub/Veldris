"""Route 1 in LeoB ORAS tiles (General + Petalburg), author 2026-10-01. Same layout as before: Palladium's Route 29
mirrored left-right, gatehouse turned into forest. Every piece is a vanilla metatile id used the same way in Route102."""
import json, pickle, sys
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "gen4_tiles"))
import route1_g4 as r                       # mirrored Route 29 source ids (r.SRC), signs
V = Path("/home/claude/veldris")
HB = {int(k): v for k, v in json.load(open(Path(__file__).parent / "hibits.json")).items()}   # metatile id -> collision/elevation bits
H, W = len(r.SRC), len(r.SRC[0])
SRC = r.SRC
TREES = {114, 115, 116, 117, 121, 122, 123, 124, 125, 126, 130, 131, 144, 155, 174}
TALL = {154, 159, 160}
LEDGE = {166, 167, 168}
WALL = {150, 172, 173, 176, 169, 180}
PATH = {177, 178, 181, 182, 184, 185, 156, 157, 158, 163, 164, 165, 170, 171, 175, 183, 186}

grid = np.full((H, W), 0x3000 | 1, np.uint16)
def put(x, y, mid): grid[y, x] = HB.get(mid, 0x3000) | mid

# --- trees on the mirrored 2x2 cells (rows 2k+1..2k+2, cols 2k..2k+1); a cell is a tree if its lower-left tile is
tops = set()
for cy in range(-1, H // 2 + 1):
    for cx in range(0, W, 2):
        ly = 2 * cy + 2
        if 0 <= ly < H and SRC[ly][cx] in TREES: tops.add((cx, 2 * cy + 1))
T = set()
for bx, by in tops: T |= {(bx, by), (bx + 1, by), (bx, by + 1), (bx + 1, by + 1)}
def tree(x, y): return (x, y) in T or not (0 <= x < W and 0 <= y < H)

# --- ground: path, tall grass, ledges, walls
P = {(x, y) for y in range(H) for x in range(W) if SRC[y][x] in PATH}
for y in range(H):
    for x in range(W):
        if SRC[y][x] == 184 or SRC[y][x] == 185: P.discard((x, y))      # west path: 2 rows (11-12) to meet Hollowbrook's 2-row exit
for x in range(54, W): P.discard((x, 9))                           # east path: 2 rows (10-11) to meet Crestfall's road
def p(x, y): return (x, y) in P or (x < 0 and (0, y) in P) or (x >= W and (W - 1, y) in P)
for x, y in P:
    n, s, w, e = p(x, y - 1), p(x, y + 1), p(x - 1, y), p(x + 1, y)
    mid = 473
    if not n: mid = 464 if not w else (466 if not e else 465)
    elif not s: mid = 480 if not w else (482 if not e else 481)
    elif not w: mid = 472
    elif not e: mid = 474
    elif not p(x - 1, y - 1): mid = 625 if False else 473
    put(x, y, mid)
for y in range(H):
    for x in range(W):
        t = SRC[y][x]
        if t in TALL: put(x, y, 13)
        elif t in LEDGE:
            l, rr = SRC[y][x - 1] in LEDGE if x > 0 else False, SRC[y][x + 1] in LEDGE if x < W - 1 else False
            put(x, y, 135 if (l and rr) else (213 if not l else 214))
        elif t in WALL:
            up = y > 0 and SRC[y - 1][x] in WALL
            down = y < H - 1 and SRC[y + 1][x] in WALL
            put(x, y, 134 if (up and down) else (255 if not up else 635))

# --- trees (LeoB autotiling, as in Hollowbrook)
for bx, by in tops:
    for dx, side in ((0, -1), (1, 2)):
        x = bx + dx
        if 0 <= by < H and 0 <= x < W:
            put(x, by, (468 if dx == 0 else 469) if tree(bx + side, by) else (470 if dx == 0 else 471))
        y = by + 1
        if 0 <= y < H and 0 <= x < W:
            if tree(x, by + 2): put(x, y, 476 if dx == 0 else 477)
            else: put(x, y, (484 if dx == 0 else 485) if tree(bx + side, y) else (486 if dx == 0 else 487))
# tips over grass / tall grass
for bx, by in tops:
    for dx in (0, 1):
        x, y = bx + dx, by - 1
        if 0 <= y < H and 0 <= x < W and (x, y) not in T:
            cur = int(grid[y, x]) & 0x3FF
            if cur == 1: put(x, y, 462 + dx)
            elif cur == 13: put(x, y, 454 + dx)

for x, y in r.SIGNS.values(): put(x, y, 3)
GRID = grid
if __name__ == "__main__":
    d = V / "data/layouts/VeldrisRoute1"
    grid.astype("<u2").tofile(d / "map.bin")
    (d / "border.bin").write_bytes((V / "data/layouts/Route102/border.bin").read_bytes())
    print("written", W, H)
