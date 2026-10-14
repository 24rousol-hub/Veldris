"""Primrose Vale Gym (Gym 8, Fairy), the one layout of the 'gym_primrose' family: a flower hall with five buds.

The plan is the tile map of design/maps/detail/primrose-vale.md section 6.2 (14 x 19), so the card's coordinates hold:
door mats (6, 18) and (7, 18), SUZURAN (6, 2), hedge door (6, 3), Beauty (6, 5), Black Belt (9, 9), Parasol Lady (3, 11),
Hiker (5, 14), guide (10, 17), statues (4, 17) and (9, 17), buds at (3, 6), (10, 6), (2, 12), (11, 12) and (11, 15), and the
petal trail on y 16. It is built on `gTileset_Building` plus `gTileset_PrettyPetalFlowerShop`, the card's own fallback.
The card's first choice (`gTileset_General` + `gTileset_Petalburg`) cannot draw the room: the General set has one flower
patch (peach blooms on grass) and the Petalburg set has none, so the flower beds would be one flower repeated and the five
buds could not be told apart. The flower shop set has the beds, the potted ferns, the vases and the
display stands that the vanilla Pretty Petal Flower Shop uses. (The Fortree Gym set has round shrubs but no flowers, and
it is already the Briarwick Gym.) The price is the card's outdoors: no grass, no sand, no round trees. The hall is a
greenhouse instead, and the picture of it is the flower shop's: a pale tiled floor under a cream wall.

What stands in for the card's pieces (nothing is drawn, every tile is the vanilla flower shop's):
  * the greenhouse back wall is the shop's cream wall over its green skirting, with four framed windows (x 3-4 and 9-10)
    and two framed flower pictures for the flower emblem (x 6-7). The windows are square, not arched;
  * a flower bed is the shop's mixed-bouquet bed. SUZURAN's bed row (y 2) and the hedge row (y 3) together are a bed
    two cells tall, and the hedge door (6, 3) is the gap in its lower row: a low flower box until it opens;
  * the 'round trees' of the side walls are the shop's potted fern stands, three racks of four per side (x 0-1, 12-13);
  * the sand cross is the shop's all-over shade tile laid as a path on the pale floor. It reads as a grey carpet;
  * the lawn is the shop's pale tiled floor, shaded the way the shop does it (see the shading rule below);
  * a bud is a fern stand two cells tall (an upper and a lower cell). When it blooms its lower fern becomes a basket or
    vase of flowers, and the petal trail on y 16 shows the five flower pieces in the order they must bloom. The set has
    no piece for pure pink, yellow or blue, so pink is a vase of tulips, yellow a yellow and a blue flower, blue the
    bed (see BLOOMS); the author may repaint them later;
  * a gym statue is the shop's wooden stool, a barrel on three legs: a complete piece one cell tall, so it cannot be
    mistaken for a bud or a petal (both are two cells tall). The shop has no statue and no plaque; the statue signs
    are written by the author over this stand-in.

Initial state (what this module ships): the hedge door cell is a flower box, every bud is a fern stand. In the solved
state (`SOLVED`) the five buds are flowers and the door cell is floor. `check_puzzle` proves the stages on temporary
grids and checks every trainer's line of sight; only the initial grid is shipped.

How the pictures are made, so the builder stays free of magic numbers:
  * every solid cell shades the floor to its right and below it by half a tile (light from the upper left). The shop has
    one floor tile per case, and `FLOOR_SHADE` maps (blocked above, blocked left, blocked above-left) to it. A cell
    directly under the back wall, and every path cell, is shaded all over, as under the shop's wall;
  * a vertical run of beds is bed cells ending in a box; a vertical run of ferns is a top, middles and a base. The two
    letters F and G stand for two fern racks one above the other, so each rack gets its own legs.
Run `python3 layoutkit.py fam_gym_primrose OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

import numpy as np

import layoutkit as K
from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_PrettyPetalFlowerShop"

# ---------------------------------------------------------------- metatile ids (secondary index + 512)
FLOOR = 513                  # pale tiled floor, no shade
FLOOR_ALL_SHADE = 514        # the whole cell in shade: the floor under the back wall, and the path of the cross
FLOOR_TOP_SHADE = 515        # shaded along the top half (a blocked cell above)
FLOOR_LEFT_SHADE = 524       # shaded along the left half (a blocked cell to the left)
FLOOR_TOP_LEFT_SHADE = 523   # shaded along the top and left halves (blocked above and to the left)
FLOOR_CORNER_SHADE = 520     # only the top-left quarter shaded (the blocked cell is diagonal)
WALL_TOP = 531               # back wall row 0: cream wall
WALL_FACE = 539              # back wall row 1: cream wall over green skirting
WALL_POST = (528, 536)       # left end of the back wall: row 0, row 1
WALL_POST_RIGHT = (530, 538)  # right end of the back wall: row 0, row 1
WINDOW = (533, 541)          # framed window: row 0, row 1
EMBLEM = (532, 540)          # framed picture of a red flower: row 0, row 1
BED = 558                    # flower bed, mixed bouquet (every cell of a bed but the lowest)
BED_BOX = 566                # flower bed, lowest cell: the bouquet in its wooden box
FERN_TOP, FERN_MID, FERN_BASE = 549, 557, 565   # potted fern on a green stand: top, middle, base (the base has legs)
VASE_PINK = (535, 543)       # a vase of pink tulips against a cream panel: upper cell, lower cell
VASES_YELLOW = (542, 550)    # a yellow and a blue flower in two vases against a cream panel
BASKET_WHITE = 571           # a basket of white blooms on a green stand (replaces the fern base)
BASKET_RED = 572             # a basket of red blooms on a green stand (replaces the fern base)
STOOL = 581                  # the shop's wooden stool (a barrel on three legs), one complete cell on a floor background
MAT = (6, 7)                 # primary tiles: the two halves of the orange door mat
ID_MASK = 0x03FF             # bits 0-9 of a map block are the metatile id (the top six bits are collision and elevation)

BUD_CLOSED = (FERN_TOP, FERN_BASE)   # a closed bud, upper and lower cell: a fern stand two cells tall
STATUE = STOOL                       # a gym statue stand-in: one whole cell, unlike the two-cell buds and petals
BLOOMS = (                   # the five buds in the order they bloom: (colour, upper cell, lower cell); also the petals
    ("white", FERN_TOP, BASKET_WHITE),
    ("pink", *VASE_PINK),
    ("yellow", *VASES_YELLOW),
    ("blue", BED, BED_BOX),
    ("red", FERN_TOP, BASKET_RED),
)

# Shade by (blocked above, blocked to the left, blocked above-left); the cell to the lower right is never shaded.
FLOOR_SHADE = {
    (0, 0, 0): FLOOR, (1, 0, 0): FLOOR_TOP_SHADE, (1, 0, 1): FLOOR_TOP_SHADE, (1, 1, 0): FLOOR_TOP_LEFT_SHADE,
    (1, 1, 1): FLOOR_TOP_LEFT_SHADE, (0, 1, 0): FLOOR_LEFT_SHADE, (0, 1, 1): FLOOR_LEFT_SHADE, (0, 0, 1): FLOOR_CORNER_SHADE,
}

# ---------------------------------------------------------------- the plan (the card's tile map, 14 x 19)
# =  back wall (rows 0-1; windows and emblem are placed by `_wall`)
# B  flower bed cell, blocked (the lowest cell of a run is the box)      H  the hedge door: a bed cell until it opens
# L  SUZURAN's cell, floor      .  lawn floor      :  path floor (the cross)
# F, G  potted fern stand, blocked (F and G racks are separate, so a G rack under an F rack gets its own legs)
# 1-5  bud, lower cell, blocked (the closed fern stand until it blooms)      a-e  petal piece of the trail, lower cell
# u  the upper cell of the bud or petal piece below it      s  statue, blocked      M  door mat, two tiles
PLAN = (
    "==============",   # y0
    "==============",   # y1  windows at x 3-4 and 9-10, flower emblem at x 6-7
    "BBBBBBLBBBBBBB",   # y2  SUZURAN (6, 2), her bed row
    "BBBBBBHBBBBBBB",   # y3  the hedge row, hedge door (6, 3)
    "BB....::....BB",   # y4  path x 6-7 starts
    "BB.u..::..u.BB",   # y5  Beauty (6, 5); upper cells of buds 1 and 2
    "FF.1..::..2.FF",   # y6  bud 1 (3, 6), bud 2 (10, 6)
    "FF....::....FF",   # y7  stand for bud 1 (3, 7) and bud 2 (10, 7)
    "FF....::....FF",   # y8
    "FF....::....FF",   # y9  Black Belt (9, 9)
    "GG::::::::::GG",   # y10 the cross arm
    "GGu::::::::uGG",   # y11 Parasol Lady (3, 11); upper cells of buds 3 and 4
    "GG3...::...4GG",   # y12 bud 3 (2, 12), bud 4 (11, 12)
    "GG....::....GG",   # y13
    "FF....::...uFF",   # y14 Hiker (5, 14); upper cell of bud 5
    "FFuuu.::.uu5FF",   # y15 bud 5 (11, 15); upper cells of the petals
    "FFabc.::.de.FF",   # y16 petals: white, pink, yellow | blue, red; stand for bud 5 (11, 16)
    "FF..s.::.s..FF",   # y17 statues (4, 17) and (9, 17), guide (10, 17)
    "......MM......",   # y18 door mat (6, 18) and (7, 18)
)
WIDTH, HEIGHT = len(PLAN[0]), len(PLAN)
WALL_ROWS = 2                      # rows 0-1 are the back wall
WINDOW_X = (3, 4, 9, 10)           # the four windows
EMBLEM_X = (6, 7)                  # the two framed flower pictures
DOORS = ((6, HEIGHT - 1), (7, HEIGHT - 1))
BUD_CHARS, PETAL_CHARS = "12345", "abcde"

# Object spots from the card (the author places the objects in Porymap); `check_puzzle` proves the plan agrees with them.
LEADER = (6, 2)                    # SUZURAN, facing down
HEDGE_DOOR = (6, 3)                # shut at first; the player talks to SUZURAN from here once it opens
BEAUTY = (6, 5)                    # facing down, sight 2: sees (6, 6) and (6, 7)
BLACK_BELT = (9, 9)                # facing left, sight 3: sees (8, 9), (7, 9) and (6, 9)
PARASOL_LADY = (3, 11)             # facing down, sight 2: sees (3, 12) and (3, 13), the stand for bud 3
HIKER = (5, 14)                    # facing right, sight 2: sees (6, 14) and (7, 14)
GUIDE = (10, 17)                   # facing left, next to the right statue
GUIDE_TALKS = ((10, 18), (11, 17))  # where the player can stand to talk to the guide (its other two sides are blocked)
BUDS = ((3, 6), (10, 6), (2, 12), (11, 12), (11, 15))        # lower cell of each bud, in blooming order
BUD_STANDS = ((3, 7), (10, 7), (3, 12), (10, 12), (11, 16))  # where the player stands, facing the bud
PETALS = ((2, 16), (3, 16), (4, 16), (9, 16), (10, 16))      # lower cell of each petal piece, in blooming order
STATUES = ((4, 17), (9, 17))
STATUE_VIEWS = ((3, 17), (5, 17), (4, 18), (8, 17), (9, 18))  # where each statue's sign can be read: beside and below it
SIGHT = {                          # cells each trainer sees, from the card
    "Beauty": ((6, 6), (6, 7)), "Black Belt": ((8, 9), (7, 9), (6, 9)),
    "Parasol Lady": ((3, 12), (3, 13)), "Hiker": ((6, 14), (7, 14)),
}
OBJECT_SPOTS = (BEAUTY, BLACK_BELT, PARASOL_LADY, HIKER, GUIDE) + GUIDE_TALKS + BUD_STANDS + STATUE_VIEWS


# ---------------------------------------------------------------- builder
def _cell(plan: tuple[str, ...], x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan counts as wall."""
    return plan[y][x] if 0 <= x < WIDTH and 0 <= y < HEIGHT else "="


def _blocked(ch: str) -> bool:
    """Cells that stop the player and shade the floor next to them."""
    return ch not in ".:LM"


def _where(plan: tuple[str, ...], ch: str) -> list[tuple[int, int]]:
    """Every (x, y) holding `ch` in the plan, row by row."""
    return [(x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c == ch]


def _floor_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Floor cell: the path and the cells under the back wall are shaded all over, the others by their neighbours."""
    if _cell(plan, x, y) == ":" or _cell(plan, x, y - 1) == "=":
        return FLOOR_ALL_SHADE
    key = tuple(int(_blocked(_cell(plan, x + dx, y + dy))) for dx, dy in ((0, -1), (-1, 0), (-1, -1)))
    return FLOOR_SHADE[key]


def _run_tile(plan: tuple[str, ...], x: int, y: int, same: str, ends: tuple[int, int, int]) -> int:
    """Tile of a vertical run of the cells in `same`: ends is (top, middle, bottom); a lone cell takes the bottom."""
    if _cell(plan, x, y + 1) not in same:
        return ends[2]
    return ends[1] if _cell(plan, x, y - 1) in same else ends[0]


def _bud_cells(index: int, bloomed: int) -> tuple[int, int]:
    """(upper, lower) metatiles of bud `index` (0-4) when the first `bloomed` buds have bloomed."""
    return BLOOMS[index][1:] if index < bloomed else BUD_CLOSED


def _wall(g: np.ndarray) -> None:
    """Rows 0-1: cream wall over green skirting, a post at each end, four windows and the flower emblem."""
    for y in range(WALL_ROWS):
        g[y, :] = W_ | (WALL_TOP, WALL_FACE)[y]
        g[y, 0], g[y, WIDTH - 1] = W_ | WALL_POST[y], W_ | WALL_POST_RIGHT[y]
    for x in WINDOW_X:
        for y in range(WALL_ROWS):
            g[y, x] = W_ | WINDOW[y]
    for x in EMBLEM_X:
        for y in range(WALL_ROWS):
            g[y, x] = W_ | EMBLEM[y]


def build(opened: bool = False, bloomed: int = 0) -> np.ndarray:
    """The map blocks of `PLAN`. `opened` makes the hedge door cell floor, `bloomed` (0-5) makes the first buds bloom."""
    rows = [list(r) for r in PLAN]
    if opened:
        x, y = HEDGE_DOOR
        rows[y][x] = "."
    plan = tuple("".join(r) for r in rows)
    g = np.zeros((HEIGHT, WIDTH), np.uint16)
    _wall(g)
    for y in range(WALL_ROWS, HEIGHT):
        for x in range(WIDTH):
            ch = plan[y][x]
            if ch in ".:L":
                g[y, x] = F_ | _floor_tile(plan, x, y)
            elif ch in "BH":
                g[y, x] = W_ | _run_tile(plan, x, y, "BH", (BED, BED, BED_BOX))
            elif ch in "FG":
                g[y, x] = W_ | _run_tile(plan, x, y, ch, (FERN_TOP, FERN_MID, FERN_BASE))
            elif ch in BUD_CHARS:
                g[y, x] = W_ | _bud_cells(BUD_CHARS.index(ch), bloomed)[1]
            elif ch in PETAL_CHARS:
                g[y, x] = W_ | BLOOMS[PETAL_CHARS.index(ch)][2]
            elif ch == "u":
                below = plan[y + 1][x]
                if below in BUD_CHARS:
                    g[y, x] = W_ | _bud_cells(BUD_CHARS.index(below), bloomed)[0]
                elif below in PETAL_CHARS:
                    g[y, x] = W_ | BLOOMS[PETAL_CHARS.index(below)][1]
                else:
                    raise ValueError(f"the upper cell ({x}, {y}) has no bud or petal under it")
            elif ch == "s":
                g[y, x] = W_ | STATUE
            elif ch == "M":
                g[y, x] = F_ | MAT[x - plan[y].index("M")]
    return g


def _spec(grid: np.ndarray, **fields) -> Spec:
    """The gym's Spec around `grid`; the other fields (npc, closed, notes...) come from the caller."""
    return Spec("LAYOUT_PRIMROSE_VALE_GYM", "PrimroseVale_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, **fields)


# ---------------------------------------------------------------- what scripts change, and the proof that it works
INITIAL = build()
SOLVED = build(opened=True, bloomed=len(BLOOMS))     # temporary, never shipped: every bud bloomed, the hedge door open


def _id(grid: np.ndarray, x: int, y: int) -> int:
    """The metatile id at (x, y) of `grid`, without the collision and elevation bits."""
    return int(grid[y, x]) & ID_MASK


HEDGE_DOOR_OPEN = _id(SOLVED, *HEDGE_DOOR)           # floor metatile a script sets on the hedge door cell
BLOOM_CHANGES = {                                    # bud number (1-5) -> ((x, y, bloomed id), ...): upper cell, then lower
    k + 1: ((bx, by - 1, BLOOMS[k][1]), (bx, by, BLOOMS[k][2])) for k, (bx, by) in enumerate(BUDS)
}


def check_puzzle() -> list[str]:
    """Problems with the card's rules; an empty list means the layout works as designed.
    The plan holds the card's coordinates. Initial grid: every bud stand, statue view and trainer cell is reachable and
    SUZURAN's cell is not. Stages: bud k blooming changes the cells of bud k only, a petal never changes, and no stage
    changes what the player can reach. Solved grid: it differs from the initial one in the hedge door and the bud cells
    only, and it lints clean with SUZURAN's cell and her talking cell reserved. Every cell a trainer sees is floor, and
    only bud 3's stand is in a trainer's sight."""
    problems: list[str] = []
    for name, want, found in (
        ("SUZURAN", (LEADER,), _where(PLAN, "L")), ("the hedge door", (HEDGE_DOOR,), _where(PLAN, "H")),
        ("the buds", BUDS, [_where(PLAN, c)[0] for c in BUD_CHARS]),
        ("the petals", PETALS, [_where(PLAN, c)[0] for c in PETAL_CHARS]),
        ("the statues", STATUES, _where(PLAN, "s")), ("the door", DOORS, _where(PLAN, "M")),
    ):
        if tuple(found) != tuple(want):
            problems.append(f"{name} are at {found} in the plan, the card says {want}")
    reached = K.reachable(_spec(INITIAL))
    problems += [f"initial: {c} should be reachable" for c in OBJECT_SPOTS if c not in reached]
    problems += [f"initial: {c} should not be reachable" for c in (LEADER, HEDGE_DOOR) if c in reached]
    expected = {HEDGE_DOOR} | {
        (x, y) for cells in BLOOM_CHANGES.values() for x, y, mid in cells if _id(INITIAL, x, y) != mid
    }
    changed = {(int(x), int(y)) for y, x in np.argwhere(INITIAL != SOLVED)}
    if changed != expected:
        problems.append(f"the solved grid differs from the initial one in {sorted(changed)}, expected {sorted(expected)}")
    for k in range(1, len(BLOOMS) + 1):
        stage, before = build(bloomed=k), build(bloomed=k - 1)
        cells = {(int(x), int(y)) for y, x in np.argwhere(stage != before)}
        if not cells <= {(x, y) for x, y, mid in BLOOM_CHANGES[k]}:
            problems.append(f"bud {k} blooming changes {sorted(cells)}, more than its own cells")
        if K.reachable(_spec(stage)) != reached:
            problems.append(f"bud {k} blooming changes what the player can reach")
    pieces = {(BLOOMS[k][1], BLOOMS[k][2]) for k in range(len(BLOOMS))}
    if len(pieces) != len(BLOOMS) or BUD_CLOSED in pieces:
        problems.append("the five blooms and the closed bud must be six different pictures")
    if STATUE in {mid for piece in pieces | {BUD_CLOSED} for mid in piece}:
        problems.append("the statue must not be a cell of a bud or a petal piece")
    errors, warnings = K.lint(_spec(SOLVED, npc=OBJECT_SPOTS + (LEADER, HEDGE_DOOR)))
    problems += [f"solved grid: {m}" for m in errors + warnings]
    seen = {c for cells in SIGHT.values() for c in cells}
    for name, cells in SIGHT.items():
        problems += [f"the {name} sees {c}, which is not floor" for c in cells if not K.passable(INITIAL[c[1], c[0]])]
    problems += [f"bud stand {s} is in a trainer's sight" for k, s in enumerate(BUD_STANDS) if k != 2 and s in seen]
    if BUD_STANDS[2] not in seen:
        problems.append("the Parasol Lady should see the stand for bud 3")
    for bud, stand in zip(BUDS, BUD_STANDS):
        if K.passable(INITIAL[bud[1], bud[0]]) or K.passable(INITIAL[bud[1] - 1, bud[0]]):
            problems.append(f"bud {bud} and the cell above it should be solid")
        if abs(bud[0] - stand[0]) + abs(bud[1] - stand[1]) != 1:
            problems.append(f"the stand {stand} is not next to its bud {bud}")
    return problems


def _swap_calls(cells: tuple[tuple[int, int, int], ...], solid: bool) -> str:
    """The `setmetatile` lines that put `cells` (x, y, id) on the map; solid pieces keep their collision."""
    return "; ".join(f"setmetatile {x}, {y}, {mid}, {'TRUE' if solid else 'FALSE'}" for x, y, mid in cells)


def _notes() -> str:
    """The text for Spec.notes: how the layout differs from the card, and what the scripts and the author must do."""
    closed = tuple((bx, by + dy, BUD_CLOSED[dy + 1]) for bx, by in BUDS for dy in (-1, 0))
    blooms = " | ".join(f"bud {k} {BLOOMS[k - 1][0]}: {_swap_calls(cells, True)}" for k, cells in BLOOM_CHANGES.items())
    return (
        "Flower shop secondary, not the card's General + Petalburg pair (no flower beds there, see the module docstring). "
        "The card's tile map is kept cell for cell, with these changes: (1) the bed row y2 and the hedge row y3 are one "
        "bed two cells tall, SUZURAN's cell (6, 2) is a floor cell in it and the hedge door (6, 3) is its lower box; "
        "(2) every bud and every petal piece is two cells tall, its upper cell on the row above the card's cell; "
        "(3) bud 5's stand is (11, 16) facing north, not the card's (10, 15), because the red petal's upper cell stands "
        "on (10, 15): the puzzle table of the card (primrose-vale.md 6.2, row 5) must be updated to match; "
        "(4) the card's wall row y18 is plain floor with the two mat tiles in it, as in every vanilla interior (the set has "
        "no front-wall piece); (5) a statue is the shop's wooden stool (581), a whole one-cell piece. "
        "INITIAL STATE (shipped): the hedge door (6, 3) is a solid flower box, the five buds are fern stands (549 over "
        "565), and SUZURAN's cell (6, 2) is walkable but sealed (Spec.closed). "
        "SOLVED STATE (proved by check_puzzle on a temporary grid, never shipped): bud k blooms in order with "
        + blooms + ". A wrong bud puts every bud back with "
        + _swap_calls(closed, True) + ". When the fifth blooms, "
        + _swap_calls(((*HEDGE_DOOR, HEDGE_DOOR_OPEN),), False)
        + f" opens the hedge door (restore it with setmetatile 6, 3, {BED_BOX}, TRUE), then special DrawWholeMapView. "
        "No neighbour cell changes: every swapped piece has the footprint of the one it replaces, so no floor shade moves. "
        "setmetatile keeps a cell's elevation (0 on the shipped solid pieces), which is harmless (Crestfall's gates do the "
        "same). MAP_SCRIPT_ON_LOAD should rebuild the bloomed buds and the open door from the stage var, because the "
        "shipped grid is the closed one. The petal trail is the five bloomed pieces on (2, 16), (3, 16), (4, 16), (9, 16) "
        "and (10, 16) (upper cells above), so each bud turns into the picture of its petal. "
        "OBJECTS (6 of 15): SUZURAN (6, 2) down; Beauty (6, 5) down, sees only (6, 6) and (6, 7), so the lane's x 7 column "
        "walks past her (make her sight wider if she must be fought); Black Belt (9, 9) left, sees (8, 9), (7, 9), (6, 9); "
        "Parasol Lady (3, 11) down, sees (3, 12) and (3, 13), the stand for bud 3; Hiker (5, 14) right, sees (6, 14) and "
        "(7, 14); guide (10, 17) left, talk from (10, 18) or (11, 17). Black Belt and Hiker see both lane columns. "
        "SIGNS (author, in Porymap): a bg_event on each bud's lower cell (3, 6), (10, 6), (2, 12), (11, 12), (11, 15) (the "
        "upper cell too if A on it should also work), read from the stands (3, 7), (10, 7), (3, 12), (10, 12), (11, 16); "
        "statue signs on (4, 17) and (9, 17), read from (3, 17), (5, 17), (4, 18) and (8, 17), (9, 18). The exit mat is two "
        "tiles, (6, 18) and (7, 18): put a warp on each, both to PrimroseVale warp 6. "
        "Look compromises: the card's lawn, sand, trees and arched windows do not exist in this set (pale floor, a darker "
        "path, fern racks, square windows); the five blooms are the closest pictures to white, pink, yellow, blue and red "
        "(pink is tulips, yellow is a yellow and a blue flower, blue is the mixed bed; the tulips and the vases stand "
        "against a small cream panel, because the set only has them as wall vases); the statues are wooden stools; the "
        "petals are standing pieces, not floor tiles. No new art is drawn."
    )


def primrose_vale_gym() -> Spec:
    """Primrose Vale Gym 14 x 19 in its initial state (hedge door shut, buds closed); see the module docstring."""
    solved_only = sorted(K.reachable(_spec(SOLVED)) - K.reachable(_spec(INITIAL)))
    return _spec(
        INITIAL,
        npc=OBJECT_SPOTS,
        closed=tuple(c for c in solved_only if K.passable(INITIAL[c[1], c[0]])),
        title="Primrose Vale Gym: flower hall, five buds, hedge door",
        uses="Primrose Vale Gym (Gym 8, Fairy; SUZURAN). Used by that one building only.",
        notes=_notes(),
    )


SPECS = [primrose_vale_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Primrose Vale Gym puzzle check failed: " + "; ".join(_PROBLEMS))
