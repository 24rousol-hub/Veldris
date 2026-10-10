"""Tiny LeoB (General + Petalburg) town builder for concept renders. Pieces are raw copies of vanilla Petalburg/Oldale."""
import json, pickle
import numpy as np
from pathlib import Path
V = Path("/home/claude/veldris")
HB = {int(k): v for k, v in json.load(open(Path(__file__).parent / "hibits.json")).items()}   # metatile id -> collision/elevation bits
L = {l["id"]: l for l in json.load(open(V / "data/layouts/layouts.json"))["layouts"]}
def raw(lid):
    l = L[lid]; return np.frombuffer((V / l["blockdata_filepath"]).read_bytes(), "<u2").reshape(l["height"], l["width"])
PB, OL = raw("LAYOUT_PETALBURG_CITY"), raw("LAYOUT_OLDALE_TOWN")
# name: (source, x, y, w, h, door offset (dx, dy) inside the stamp)
PIECES = {
    "gym":    (PB, 12, 4, 6, 5, (3, 4)),
    "house5": (PB, 5, 2, 5, 4, (2, 3)),
    "house4": (PB, 9, 16, 4, 4, (1, 3)),
    "houseO": (OL, 4, 4, 4, 4, (1, 3)),
    "pc":     (PB, 19, 13, 4, 4, (1, 3)),
    "mart":   (OL, 13, 3, 4, 4, (1, 3)),
}

class Town:
    def __init__(s, W, H):
        s.W, s.H = W, H
        s.clear = np.zeros((H, W), bool)          # not forest
        s.path = np.zeros((H, W), bool)
        s.grid = np.full((H, W), 0x3000 | 1, np.uint16)
        s.over = {}                                # (x,y) -> block, applied last
        s.doors = {}
        s.notes = []
    def put(s, x, y, m): s.over[(x, y)] = HB.get(m, 0x3000) | m
    def open(s, x0, y0, x1, y1): s.clear[y0:y1 + 1, x0:x1 + 1] = True
    def road(s, x0, y0, x1, y1):
        s.open(x0, y0, x1, y1); s.path[y0:y1 + 1, x0:x1 + 1] = True
    def unroad(s, x0, y0, x1, y1): s.path[y0:y1 + 1, x0:x1 + 1] = False
    def stamp(s, name, x, y, label=None):
        src, sx, sy, w, h, (dx, dy) = PIECES[name]
        s.open(x, y - 1, x + w - 1, y + h)
        for j in range(h):
            for i in range(w): s.over[(x + i, y + j)] = int(src[sy + j, sx + i])
        if name == "mart": s.over[(x + 3, y)] = HB.get(43, 0x3000) | 43   # clean roof corner (Oldale's 645 has a tree in it)
        s.doors[label or name] = (x + dx, y + dy)
        return (x + dx, y + dy)
    def pond(s, x0, y0, x1, y1):
        s.open(x0 - 1, y0 - 1, x1 + 1, y1 + 1)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if y == y0: m = 176 if x == x0 else (178 if x == x1 else 177)
                elif y == y1: m = 2
                else: m = 184 if x == x0 else (186 if x == x1 else 161)
                s.put(x, y, m)
    def crops(s, x0, y0, x1, y1, hedge=False):
        """Crop beds (tile 7). hedge=True: Petalburg's garden hedge, 2 tiles tall on top (572-574 over 580-582),
        sides running down (588) with end caps (596), open at the bottom like vanilla. hedge=False: plain beds on grass."""
        top = 2 if hedge else 0
        s.open(x0 - 1, y0 - 1 - top, x1 + 1, y1 + 1)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1): s.put(x, y, 7)
        if hedge:
            for x in range(x0, x1 + 1): s.put(x, y0 - 2, 573); s.put(x, y0 - 1, 581)
            s.put(x0 - 1, y0 - 2, 572); s.put(x1 + 1, y0 - 2, 574)
            s.put(x0 - 1, y0 - 1, 580); s.put(x1 + 1, y0 - 1, 582)
            for y in range(y0, y1 + 1):
                for x in (x0 - 1, x1 + 1): s.put(x, y, 596 if y == y1 else 588)
    def bench(s, x, y):             # LeoB's 3-tile wooden bench, solid
        for i, m in enumerate((520, 521, 522)): s.over[(x + i, y)] = 0x3400 | m
    def fence(s, x0, x1, y):        # Petalburg's white fence: end posts and rails, solid
        for x in range(x0, x1 + 1): s.over[(x, y)] = 0x3400 | (328 if x == x0 else (330 if x == x1 else 329))
    def flowers(s, pts):
        for x, y in pts: s.put(x, y, 4)
    def sign(s, x, y): s.put(x, y, 3)
    def build(s):
        W, H = s.W, s.H
        # trees on a 2x2 grid where nothing is cleared
        tops = set()
        for by in range(0, H, 2):
            for bx in range(0, W, 2):
                if not s.clear[by:by + 2, bx:bx + 2].any(): tops.add((bx, by))
        T = set()
        for bx, by in tops: T |= {(bx, by), (bx + 1, by), (bx, by + 1), (bx + 1, by + 1)}
        tree = lambda x, y: (x, y) in T or not (0 <= x < W and 0 <= y < H)
        g = s.grid
        def put(x, y, m):
            if 0 <= x < W and 0 <= y < H: g[y, x] = HB.get(m, 0x3000) | m
        for bx, by in tops:
            put(bx, by, 468 if tree(bx - 1, by) else 470); put(bx + 1, by, 469 if tree(bx + 2, by) else 471)
            put(bx, by + 1, 476 if tree(bx, by + 2) else (484 if tree(bx - 1, by + 1) else 486))
            put(bx + 1, by + 1, 477 if tree(bx + 1, by + 2) else (485 if tree(bx + 2, by + 1) else 487))
        P = s.path
        def p(x, y):
            cx, cy = min(max(x, 0), W - 1), min(max(y, 0), H - 1)
            return bool(P[cy, cx])
        for y in range(H):
            for x in range(W):
                if not P[y, x]: continue
                n, so, w, e = p(x, y - 1), p(x, y + 1), p(x - 1, y), p(x + 1, y)
                m = 289
                if not n: m = 280 if not w else (282 if not e else 281)
                elif not so: m = 296 if not w else (298 if not e else 297)
                elif not w: m = 288
                elif not e: m = 290
                put(x, y, m)
        for bx, by in tops:
            for dx in (0, 1):
                x, y = bx + dx, by - 1
                if 0 <= y < H and (x, y) not in T and (int(g[y, x]) & 0x3FF) == 1: put(x, y, 462 + dx)
        for (x, y), v in s.over.items():
            if 0 <= x < W and 0 <= y < H: g[y, x] = v
        return g
