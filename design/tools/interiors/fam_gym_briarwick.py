"""Briarwick Gym (Gym 2, Bug), the one layout of the 'gym_briarwick' family: a hedge garden with two silk webs.

The plan is the tile map of design/maps/detail/briarwick.md section 3.3 (13 x 17, traced from azaleagym20yp), so every
coordinate on the card holds: door (6, 16), HACHIMEL (6, 4), webs (6, 10) and (6, 7), Bug Catcher (2, 11), Aroma Lady
(10, 8), statues (4, 14) and (8, 14). It is built on `gTileset_Building` plus `gTileset_FortreeGym`, whose round
green shrubs are the nearest existing thing to the card's hedges (the card asks for new art; none is drawn here).

Initial state (what this module ships): both webs are shut, so the player can only reach the hall, the corridor up to
(6, 11) and the west alcove. Beating the Bug Catcher opens the web at (6, 10), beating the Aroma Lady opens the web at
(6, 7). `SOLVED_CHANGES` gives the floor metatile that scripts put on each web cell; `check_puzzle` proves the three
stages on temporary grids (only the initial grid is shipped).

How the pictures are made, so the builder stays free of magic numbers:
  * a shrub is a barrel whose crown is drawn in the bottom of the cell above it. So every hedge column has a crown cell
    on top (floor with a crown, or the wall's fence tile with a crown), then a top, middle or bottom shrub cell;
  * the floor carries a shadow cast by whatever blocks the cell above or to the left (light from the upper left).
    The tileset has one floor tile per case; `PLAIN_FLOOR` and `CROWN_FLOOR` map (blocked above, blocked left, blocked
    above-left) to the tile, the same rule the vanilla Fortree Gym follows (read off its map).
Run `python3 layoutkit.py fam_gym_briarwick OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

import numpy as np

import layoutkit as K
from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_FortreeGym"

# ---------------------------------------------------------------- metatile ids (secondary index + 512)
FLOOR = 514                 # plain pale floor, no shadow
BAND_FLOOR = 513            # floor shadowed along the top, the shadow thinning out towards the left
BAND_FLOOR_FULL = 515       # floor shadowed along the top
BOTH_FLOOR = 516            # floor shadowed along the top and the left
STRIP_FLOOR_FULL = 517      # floor shadowed along the left
STRIP_FLOOR_TOP_FADE = 519  # floor shadowed along the left, the shadow thinning out upwards
CORNER_FLOOR = 518          # floor with a corner shadow thinning out downwards (only the cell above-left is blocked)
CROWN = 521                 # floor with a shrub crown in its lower half, no shadow
CROWN_BAND = 549            # crown, shadowed along the top, thinning out to the left
CROWN_BAND_FULL = 546       # crown, shadowed along the top
CROWN_STRIP_FULL = 547      # crown, shadowed along the left
CROWN_STRIP_TOP_FADE = 555  # crown, shadowed along the left, thinning out upwards
CROWN_CORNER = 548          # crown with a corner shadow
SHRUB_TOP = 556             # top shrub of a column: dark foot, next crown at the bottom
SHRUB_MID = 544             # middle shrub of a column: next crown at the bottom
SHRUB_BASE = 529            # bottom shrub of a column (or a lone shrub): dark foot, rounded base
WALL_BAND = 527             # wall row 0: green and white banded cornice
WALL_FENCE = 531            # wall rows 1-2: green fence panel with a dark foot strip
WALL_FENCE_CROWN = 526      # fence panel with a shrub crown in its lower half (the wall row over a hedge)
WALL_CREST = 533            # fence panel with the blue emblem; the nearest thing to the card's ladybug crest
WINDOW_TOP = (566, 567)     # black window, left and right (wall row 0)
WINDOW_SILL = (574, 575)    # window frame (wall row 1)
WINDOW_BOX = (582, 583)     # inset fence panel under the window (wall row 2)
PODIUM_BACK = (539, 540, 541, 542, 543)    # leader's stage, back row: round end, rug (3 tiles), round end
PODIUM_FRONT = (576, 577, 578, 579, 580)   # front row, with the stage's front edge
STATUE_HEAD = 551           # guide statue: orb on a pedestal (top cell)
STATUE_PLAQUE = 559         # guide statue: pedestal with a plaque (bottom cell)
WEB = 563                   # trellis of round-leafed lattice, filling the whole cell: stands in for the silk web
MAT = (6, 7)                # primary tiles: the two halves of the orange door mat
ID_MASK = 0x03FF            # bits 0-9 of a map block are the metatile id (the top six bits are collision and elevation)

PLAIN_FLOOR = {  # (blocked above, blocked to the left, blocked above-left) -> floor tile
    (0, 0, 0): FLOOR, (1, 0, 0): BAND_FLOOR, (1, 0, 1): BAND_FLOOR_FULL, (1, 1, 0): BOTH_FLOOR, (1, 1, 1): BOTH_FLOOR,
    (0, 1, 1): STRIP_FLOOR_FULL, (0, 1, 0): STRIP_FLOOR_TOP_FADE, (0, 0, 1): CORNER_FLOOR,
}
CROWN_FLOOR = {  # the same cases for a cell that has a shrub below it. The tileset has no crown with both shadows
    (0, 0, 0): CROWN, (1, 0, 0): CROWN_BAND, (1, 0, 1): CROWN_BAND_FULL, (1, 1, 0): CROWN_BAND_FULL, (1, 1, 1): CROWN_BAND_FULL,
    (0, 1, 1): CROWN_STRIP_FULL, (0, 1, 0): CROWN_STRIP_TOP_FADE, (0, 0, 1): CROWN_CORNER,
}

# ---------------------------------------------------------------- the plan (the card's tile map, 13 x 17)
# =  wall (rows 0-2: cornice, fence, windows and crest are placed by `_wall`)
# h  hedge shrub, blocked (the frame at x 0 and 12 and the bottom wall are hedge too)
# .  floor (HACHIMEL, the trainers and the plaque are objects on floor cells)
# W  web, blocked until its trainer is beaten
# P  stage end cap, blocked      p  stage tile, walkable (the leader stands on the front row)
# s  statue head, blocked        S  statue plaque, blocked      M  door mat, two tiles
PLAN = (
    "=============",   # y0
    "=============",   # y1  windows at x 4-5 and 7-8, crest at (6, 1)
    "=============",   # y2
    "hhhhPpppPhhhh",   # y3  hedge border and the leader's stage (back row)
    "h...PpppP...h",   # y4  HACHIMEL (6, 4)
    "h...........h",   # y5  talk to HACHIMEL from (6, 5)
    "hhhhhh.hhhhhh",   # y6
    "hhhhhhWhhhhhh",   # y7  second web (6, 7)
    "hhhhhh.....hh",   # y8  east alcove x 7-10, Aroma Lady (10, 8)
    "hhhhhh.hhhhhh",   # y9
    "hhhhhhWhhhhhh",   # y10 first web (6, 10)
    "hh.....hhhhhh",   # y11 west alcove x 2-5, Bug Catcher (2, 11)
    "hhhhhh.hhhhhh",   # y12 gap (6, 12), hint plaque on the hedge at (5, 12)
    "h...s...s...h",   # y13 statue heads
    "h...S...S...h",   # y14 statue plaques (bg events at (4, 14) and (8, 14))
    "h...........h",   # y15
    "hhhhhhMMhhhhh",   # y16 door mat (6, 16) and (7, 16)
)
WIDTH, HEIGHT = len(PLAN[0]), len(PLAN)
WALL_ROWS = 3                      # rows 0-2 are the back wall: cornice, fence, and the fence row that carries crowns
CORRIDOR_X = 6                     # the central corridor and the door (the card's x 6)
WEBS = ((CORRIDOR_X, 10), (CORRIDOR_X, 7))   # first web (Bug Catcher), second web (Aroma Lady)
DOORS = ((CORRIDOR_X, 16), (CORRIDOR_X + 1, 16))
WINDOW_X = (4, 7)                  # left cell of each two-wide window
CREST = (6, 1)
PODIUM_X = 4                       # left cell of the stage (5 wide, rows 3-4)
PODIUM_Y = 3

# Object spots from the card (the author places the objects in Porymap).
LEADER = (6, 4)                    # HACHIMEL, facing down; the player talks from (6, 5)
LEADER_TALK = (6, 5)
BUG_CATCHER = (2, 11)              # facing east, sight 3: sees (3-5, 11), not the corridor cell (6, 11)
AROMA_LADY = (10, 8)               # facing west, sight 3: sees (7-9, 8), not the junction (6, 8)
STATUE_VIEW = ((4, 15), (8, 15))   # the cell in front of each statue plaque, where its sign is read from
PLAQUE_VIEW = (6, 12)              # the gap cell next to the hint plaque on the hedge at (5, 12)
SIGHT = 3


# ---------------------------------------------------------------- builder
def _cell(plan: tuple[str, ...], x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan counts as wall."""
    return plan[y][x] if 0 <= x < WIDTH and 0 <= y < HEIGHT else "="


def _casts_shadow(ch: str) -> bool:
    """Walls, hedges, stage ends and statues shade the floor to their right and below. Webs do not (they are lattice,
    and leaving them out means the floor next to a web needs no change when it opens)."""
    return ch in "=hPsS"


def _floor_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Floor cell: the shadow from the cells above and to the left, and a crown when a shrub stands below it."""
    key = tuple(int(_casts_shadow(_cell(plan, x + dx, y + dy))) for dx, dy in ((0, -1), (-1, 0), (-1, -1)))
    table = CROWN_FLOOR if _cell(plan, x, y + 1) == "h" else PLAIN_FLOOR
    return table[key]


def _shrub_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Hedge cell: bottom of its column, or top or middle when more shrubs stack below it."""
    if _cell(plan, x, y + 1) != "h":
        return SHRUB_BASE
    return SHRUB_MID if _cell(plan, x, y - 1) == "h" else SHRUB_TOP


def _wall(g: np.ndarray, plan: tuple[str, ...]) -> None:
    """Rows 0-2: cornice, fence, and over every hedge column a fence cell that carries the crown of the shrub below.
    Two windows (three rows tall, with the black pane in the cornice) and the crest sit over the leader's stage."""
    g[0, :] = W_ | WALL_BAND
    g[1, :] = W_ | WALL_FENCE
    for x in range(WIDTH):
        g[2, x] = W_ | (WALL_FENCE_CROWN if _cell(plan, x, WALL_ROWS) == "h" else WALL_FENCE)
    for left in WINDOW_X:
        for dx in (0, 1):
            g[0, left + dx] = W_ | WINDOW_TOP[dx]
            g[1, left + dx] = W_ | WINDOW_SILL[dx]
            g[2, left + dx] = W_ | WINDOW_BOX[dx]
    g[CREST[1], CREST[0]] = W_ | WALL_CREST


def build(opened: tuple = ()) -> np.ndarray:
    """The map blocks of `PLAN`; every web cell listed in `opened` is floor instead (the solved or half-solved state)."""
    rows = [list(r) for r in PLAN]
    for x, y in opened:
        rows[y][x] = "."
    plan = tuple("".join(r) for r in rows)
    g = np.zeros((HEIGHT, WIDTH), np.uint16)
    _wall(g, plan)
    for y in range(WALL_ROWS, HEIGHT):
        for x in range(WIDTH):
            ch = plan[y][x]
            if ch == ".":
                g[y, x] = F_ | _floor_tile(plan, x, y)
            elif ch == "h":
                g[y, x] = W_ | _shrub_tile(plan, x, y)
            elif ch == "W":
                g[y, x] = W_ | WEB
            elif ch in "Pp":
                stage = PODIUM_BACK if y == PODIUM_Y else PODIUM_FRONT
                g[y, x] = (W_ if ch == "P" else F_) | stage[x - PODIUM_X]
            elif ch == "s":
                g[y, x] = W_ | STATUE_HEAD
            elif ch == "S":
                g[y, x] = W_ | STATUE_PLAQUE
            elif ch == "M":
                g[y, x] = F_ | MAT[x - plan[y].index("M")]
    return g


def _spec(grid: np.ndarray, **fields) -> Spec:
    return Spec("LAYOUT_BRIARWICK_GYM", "Briarwick_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, **fields)


# ---------------------------------------------------------------- the puzzle, proved on the solved grid
SOLVED = build(opened=WEBS)
SOLVED_CHANGES = {(x, y): int(SOLVED[y, x]) & ID_MASK for x, y in WEBS}   # floor metatile a script sets on each web cell
OBJECT_SPOTS = (LEADER, LEADER_TALK, BUG_CATCHER, AROMA_LADY, PLAQUE_VIEW) + STATUE_VIEW


def _reach(opened: tuple) -> set[tuple[int, int]]:
    return K.reachable(_spec(build(opened=opened)))


def check_puzzle() -> list[str]:
    """Problems with the three stages of the card; an empty list means the puzzle works as designed.
    Stage 0: hall, corridor and west alcove only. Stage 1 (first web open): the junction and east alcove, not the dais.
    Stage 2 (both open): everything, and the solved grid lints clean with every object spot reserved."""
    problems: list[str] = []
    first, second = WEBS
    behind_first = (first[0], first[1] - 1)       # (6, 9), the corridor cell just beyond the first web
    junction = (first[0], first[1] - 2)           # (6, 8), where the east alcove opens
    below_dais = (second[0], second[1] - 1)       # (6, 6), the corridor cell just beyond the second web
    stage0, stage1, stage2 = _reach(()), _reach((first,)), _reach(WEBS)
    for label, reached, want, avoid in (
        ("stage 0", stage0, (BUG_CATCHER, PLAQUE_VIEW) + STATUE_VIEW, (AROMA_LADY, behind_first, LEADER_TALK)),
        ("stage 1", stage1, (AROMA_LADY, junction), (second, below_dais, LEADER_TALK)),
        ("stage 2", stage2, (LEADER_TALK, LEADER, below_dais), ()),
    ):
        problems += [f"{label}: {c} should be reachable" for c in want if c not in reached]
        problems += [f"{label}: {c} should not be reachable" for c in avoid if c in reached]
    errors, warnings = K.lint(_spec(SOLVED, npc=OBJECT_SPOTS))
    problems += [f"solved grid: {m}" for m in errors + warnings]
    # A trainer must not see the corridor, or the fight would start before the player steps into the alcove.
    for name, (x, y), step in (("Bug Catcher", BUG_CATCHER, 1), ("Aroma Lady", AROMA_LADY, -1)):
        if (CORRIDOR_X, y) in {(x + step * d, y) for d in range(1, SIGHT + 1)}:
            problems.append(f"the {name} would see the corridor cell ({CORRIDOR_X}, {y})")
    return problems


def briarwick_gym() -> Spec:
    """Briarwick Gym 13 x 17 in its initial state (both webs shut); see the module docstring and the notes below."""
    initial = build()
    opened_only = sorted(K.reachable(_spec(SOLVED)) - K.reachable(_spec(initial)))
    return _spec(
        initial,
        npc=(BUG_CATCHER, PLAQUE_VIEW) + STATUE_VIEW,
        closed=tuple(opened_only),
        title="Briarwick Gym: hedge garden, two webs, leader's stage",
        uses="Briarwick Gym (Gym 2, Bug; HACHIMEL). Used by that one building only.",
        notes=(
            "Fortree Gym secondary. Card tile map kept cell for cell, except that the card's 11-planter row at y3 is "
            "split in two by the leader's stage (x4-8, y3-4) and the door mat is two tiles wide. Initial state: webs "
            "shut. Solved state: scripts call "
            + "; ".join(f"setmetatile {x}, {y}, {mid}, FALSE" for (x, y), mid in SOLVED_CHANGES.items())
            + " (the Bug Catcher's web (6, 10) first, the Aroma Lady's (6, 7) second), then special DrawWholeMapView. "
            "No neighbour cell needs changing: webs cast no shadow. Webs are blocked in the shipped grid, so the gym is safe "
            "even if the OnLoad script is missing; OnLoad re-opens a web when its trainer's flag is set. `closed` lists the "
            "walkable cells that are cut off until the webs open; Spec.npc holds only the object spots reachable from the "
            "door in the initial state (the lint rejects the others), the leader's and the Aroma Lady's spots are checked "
            "on the solved grid by check_puzzle. HACHIMEL (6, 4); Bug Catcher (2, 11) facing east; Aroma Lady (10, 8) "
            "facing west; both sight 3. Statue signs at (4, 14) and (8, 14), read from (4, 15) and (8, 15); hint plaque "
            "sign on the hedge cell (5, 12), read from (6, 12). Door mat is two tiles (6, 16) and (7, 16): put a warp "
            "on each, both to Briarwick. setmetatile keeps the cell's elevation (0 on the shipped web), which is harmless "
            "(Crestfall's gates do the same). Look compromises: hedges are the Fortree gym's round shrubs, the web is its "
            "trellis tile (563), the crest is its blue emblem (533), the statues are its orb pedestals; no new art."
        ),
    )


SPECS = [briarwick_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Briarwick Gym puzzle check failed: " + "; ".join(_PROBLEMS))
