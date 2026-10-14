"""Shared one-floor house layouts H1 (cottage 9x8) and H5 (bedroom house 11x8), Gen 4 Interior.
Every piece is copied from the built Hollowbrook interiors (same ids, same collision and elevation)."""
import numpy as np
W_, F_ = 0x0400, 0x3000          # wall/furniture: collision 1, elevation 0; floor: elevation 3
WALLTOP, WALL, WALLFOOT, WOOD, TILE = 518, 526, 529, 528, 520
STOVE  = ((602, 603), (608, 609))
FRIDGE = ((936, 940), (944, 948))
SHELF  = ((538, 539), (953, 954))
TV     = ((622, 623), (630, 631))
WINDOW = ((548, 549), (556, 557))      # row 0 and row 1, row 2 is WALLFOOT
BED    = ((812, 813), (820, 821), (828, 829))
TABLE  = ((572, 573), (588, 589), (564, 565))
CUSHION, PLANT = 605, (582, 590)
MAT = (536, 513, 537)
def blank(w, h):
    g = np.full((h, w), F_ | WOOD, np.uint16)
    g[0, :] = W_ | WALLTOP; g[1, :] = W_ | WALL; g[2, :] = F_ | WALLFOOT
    return g
def put(g, x, y, piece, solid=True):
    for dy, row in enumerate(piece):
        for dx, m in enumerate(row): g[y + dy, x + dx] = (W_ if solid else F_) | m
def wallpiece(g, x, piece):      # a 2-row piece against the back wall (rows 1-2)
    put(g, x, 1, piece)
def mat(g, x):
    for i, m in enumerate(MAT): g[g.shape[0] - 1, x - 1 + i] = F_ | m

def h1():
    """Cottage 9x8: stove and fridge on a tiled kitchen floor (left), bookshelf, TV,
    flower table with a cushion each side facing the TV, plant, door mat (2,7)."""
    g = blank(9, 8)
    g[3:, 0:4] = F_ | TILE
    wallpiece(g, 0, STOVE); wallpiece(g, 2, FRIDGE); wallpiece(g, 4, SHELF); wallpiece(g, 7, TV)
    put(g, 6, 4, TABLE); g[5, 5] = F_ | CUSHION; g[5, 8] = F_ | CUSHION
    put(g, 4, 5, ((PLANT[0],), (PLANT[1],)))
    mat(g, 2)
    return g

def h5():
    """Bedroom house 11x8: bed in the top-left corner, TV with the flower table and cushions,
    kitchen (stove, fridge) on a tiled floor on the right, plant, door mat (8,7) on the tiles."""
    g = blank(11, 8)
    g[3:, 7:11] = F_ | TILE
    put(g, 1, 1, BED); wallpiece(g, 4, TV); wallpiece(g, 7, STOVE); wallpiece(g, 9, FRIDGE)
    put(g, 4, 4, TABLE); g[5, 3] = F_ | CUSHION; g[5, 6] = F_ | CUSHION
    put(g, 0, 5, ((PLANT[0],), (PLANT[1],)))
    mat(g, 8)
    return g
LAYOUTS = {"H1_Cottage": h1, "H5_BedroomHouse": h5}
if __name__ == "__main__":
    import sys
    from mrender import TS, render
    ts = TS("gTileset_Building", "gTileset_Gen4Interior")
    for name, f in LAYOUTS.items():
        g = f(); render(g, ts, 3).save(f"{name}.png"); render(g, ts, 3, ids=False, coll=True).save(f"{name}_coll.png")
        print(name, g.shape)
