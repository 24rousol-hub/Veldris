"""Smeltham Gym (Gym 4, Steel), the one layout of the 'gym_smeltham' family: an assembly hall with four conveyor lanes.

The plan is the tile map of design/maps/detail/smeltham.md section 5 (13 x 20, from the Olivine City Gym render), so the
card's coordinates hold: door (6, 19), HAGANE (6, 3), steps (5, 5), Hiker (11, 13), Black Belt (1, 11), Guitarist (1, 9),
crucibles (3, 16) and (9, 16). It is built on `gTileset_Building` plus `gTileset_TrickHousePuzzle`, as the card says:
that set has the only usable walk-speed arrow tiles in the tree (metatiles 608 and 609, MB_WALK_EAST and MB_WALK_WEST;
the unused placeholder set `gTileset_Unused2` has arrows but no finished art), so the conveyor belts are vanilla and no
art is drawn. The Facility, Mossdeep and Lavaridge gym sets have no forced-movement tile at all (the Mossdeep and
Lavaridge arrows are warp pads); Sootopolis, Trainer Hill and the FRLG gym sets have slides or spinners but no floor
that fits a hall of belts.

The puzzle needs no gate: all four lanes are open in the shipped grid, and the player picks the one true gap in each
machine row. The other gaps are presses, drawn as gold hazard stripes (the card's clue): floor cells that a `coord_event`
turns into a warp back to the hall. So the initial grid is also the solved grid and no script changes a block.
`check_puzzle` proves the card's route with a belt-aware walk (belts carry the player on until a rest cell, a press sends
him back to the hall).

Changes to the card: lane B's west stretch (x 2 to 4) is plain floor, not belts. Belts there would carry the player
west into the Black Belt's own cell; belts only run one way and walls close the lane, so he would be boxed in for good.
`check_puzzle` runs the card's version and proves that soft-lock. And the terrace, which the card leaves empty, gets a
gold plate under HAGANE and two gold ingot racks in its back corners (decoration; the walkable terrace is unchanged
except for those six cells).

How the pictures are made, so the builder stays free of magic numbers:
  * a machine bar is the tileset's wooden bar, one cell tall: a left end (bolt), middle planks and a right end (bolt),
    with a cream lip along its top. The floor cell under a bar takes the shadow variant, belt plates keep their frame;
  * the terrace floor is the cream platform tile and its front edge is the same bar, so the bar's cream lip reads as the
    platform's top edge; the steps cut through the bar;
  * the back wall is the tan wall with a cream ledge in its lower half (that ledge is the terrace's first strip of
    cream); two round lamps and a tool rack hang in its top row;
  * the gold plate (three cells, rivet at each end) is one piece used twice: walkable under HAGANE, solid as an ingot rack.
Run `python3 layoutkit.py fam_gym_smeltham OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

from collections import deque
from typing import NamedTuple

import numpy as np

from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_TrickHousePuzzle"

# ---------------------------------------------------------------- metatile ids (secondary index + 512)
FLOOR = 520                    # plain green carpet floor
FLOOR_SHADOW = 602             # floor in the shade of the bar above it
PLATFORM = 633                 # plain cream platform top: the terrace floor
STEPS = 618                    # cream steps, horizontal bands
HAZARD = 653                   # gold diagonal hatching, the nearest thing to a hazard stripe: marks a press
BELT_EAST, BELT_WEST = 608, 609   # red arrow plates in a gold frame, MB_WALK_EAST and MB_WALK_WEST (walk speed)
BAR = (547, 548, 549)          # wooden bar with a cream lip: left end (bolt), planks, right end (bolt)
PLATE = (641, 642, 643)        # gold riveted plate: left end, middle, right end
SIDE_WALL = 551                # plain wood panel: the side walls and the corner posts of the front wall
WALL_TOP = 513                 # back wall row 0: white band over tan wall
LAMP = 517                     # row 0: round lamp hanging in the tan wall
RACK = (514, 515, 516)         # row 0: three-wide tool rack on the tan wall
LEDGE = 563                    # back wall row 1: tan wall over a cream ledge
CRUCIBLE = 532                 # grey urn with a dark mouth, standing in for the card's Poke Ball statues
MAT = (529, 530)               # the set's own exit mat: grey plate in a gold frame, SOUTH_ARROW_WARP

# ---------------------------------------------------------------- the plan (the card's tile map, 13 x 20)
# =  back wall (rows 0-1; the lamps and the rack are placed by `_back_wall`)
# w  side wall panel, blocked          b  machine bar, or the bar-shaped front edge of the terrace, blocked
# .  floor (the cream platform on the terrace rows), walkable
# <  >  conveyor belt, carries west / east (forced walk)
# G  the true gap in a machine row, floor      X  a press: hazard-striped floor whose coord_event warps back to the hall
# S  steps up to the terrace, walkable         s  crucible, blocked
# L  HAGANE, T  a gym trainer: objects on floor cells, so the player cannot enter them
# p  gold plate under HAGANE, walkable         i  gold ingot rack, blocked           M  exit mat, two tiles
LANE_B_CARD = "wT<<<.<<.<<.w"      # lane B as the card draws it: belts all along (x 2-4 feed the Black Belt's cell)
PLAN = (
    "=============",   # y0  lamps at x3 and x9, rack at x5-7
    "=============",   # y1
    "wiii.....iiiw",   # y2  terrace x1-11, an ingot rack in each back corner
    "w....pLp....w",   # y3  HAGANE (6, 3) on his plate
    "w...........w",   # y4  the player talks to him from (6, 4)
    "wbbbbSbbbbbbw",   # y5  the terrace's front edge, steps (5, 5)
    "wXbbbGbbXbbXw",   # y6  machine row 4: presses x1 x8 x11, TRUE gap x5
    "w.<<<.<<.<<.w",   # y7  lane D, belts carry west
    "wbbbbXbbXbbGw",   # y8  machine row 3: presses x5 x8, TRUE gap x11
    "wT>>>.>>.>>.w",   # y9  lane C, belts carry east; Guitarist (1, 9)
    "wXbbbGbbbbbXw",   # y10 machine row 2: presses x1 x11, TRUE gap x5
    "wT....<<.<<.w",   # y11 lane B, belts carry west from x 9 on; Black Belt (1, 11)
    "wbbbbXbbGbbXw",   # y12 machine row 1: presses x5 x11, TRUE gap x8
    "w.>>>.>>.>>Tw",   # y13 lane A, belts carry east; Hiker (11, 13)
    "w...........w",   # y14 the start hall
    "w...........w",   # y15
    "w..s.....s..w",   # y16 crucibles (3, 16) and (9, 16)
    "w...........w",   # y17
    "w...........w",   # y18
    "wbbbbbMMbbbbw",   # y19 front wall with the exit mat (6, 19) and (7, 19)
)
LANE_B_ROW = 11
BACK_WALL_ROWS = 2                 # rows 0-1
TERRACE_ROWS = range(2, 5)         # the cream platform: y 2 to 4
LAMP_X = (3, 9)                    # the two lamps, symmetric about HAGANE's column
RACK_X = 5                         # left cell of the tool rack, centred on HAGANE's column

# Object spots from the card (the author places the objects, warps and triggers in Porymap).
LEADER = (6, 3)                    # HAGANE, facing down
LEADER_TALK = (6, 4)               # the player talks to him from here
DOORS = ((6, 19), (7, 19))         # the exit mat; both cells warp to Smeltham (card: arrival (6, 19))
RESTART = (6, 18)                  # a press warps the player here (card: warpteleport MAP_SMELTHAM_GYM, 6, 18)
STATUE_VIEW = ((3, 17), (9, 17))   # the cell in front of each crucible, where its sign is read from
LUNCHBOXES = ((2, 15), (10, 15), (6, 17))   # the card's bg_event lunchboxes: plain floor, no art
TRUE_GAPS = ((8, 12), (5, 10), (11, 8), (5, 6))   # the card's true gap of lane A, B, C and D, in the order walked


class Trainer(NamedTuple):
    """A gym trainer: where he stands, which way he faces (dx), how far he sees, and the cell he must see the player on."""
    name: str
    pos: tuple[int, int]
    facing: int
    sight: int
    stop: tuple[int, int]


TRAINERS = (
    Trainer("Hiker", (11, 13), -1, 3, (8, 13)),         # sees x 8-10; the player stands on (8, 13) to take the gap above
    Trainer("Black Belt", (1, 11), 1, 4, (5, 11)),      # sees x 2-5; the player ends lane B's belts on (5, 11)
    Trainer("Guitarist", (1, 9), 1, 4, (5, 9)),         # sees x 2-5; the player enters lane C on (5, 9)
)

BELTS = {">": (1, 0), "<": (-1, 0)}            # plan char -> the step a belt forces
SOLID = frozenset("=wbsiLT")                   # plan chars the player cannot enter
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


# ---------------------------------------------------------------- builder
def _cell(plan: tuple[str, ...], x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan counts as wall."""
    return plan[y][x] if 0 <= x < len(plan[0]) and 0 <= y < len(plan) else "w"


def _floor_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Floor cell: cream platform on the terrace rows, shaded floor under a bar, plain floor anywhere else."""
    if y in TERRACE_ROWS:
        return PLATFORM
    return FLOOR_SHADOW if _cell(plan, x, y - 1) == "b" else FLOOR


def _end_tile(plan: tuple[str, ...], x: int, y: int, joins: str, pieces: tuple[int, int, int]) -> int:
    """Left end, middle or right end of a horizontal piece: a cell is an end where its neighbour is not in `joins`."""
    open_left = _cell(plan, x - 1, y) not in joins
    open_right = _cell(plan, x + 1, y) not in joins
    if open_left and open_right:
        raise ValueError(f"the piece at ({x}, {y}) is one cell wide; the tileset has no single-cell version")
    return pieces[0] if open_left else pieces[2] if open_right else pieces[1]


def _back_wall(g: np.ndarray) -> None:
    """Rows 0-1: the tan wall with its cream ledge, two lamps and a tool rack hanging in row 0."""
    g[0, :] = W_ | WALL_TOP
    for x in LAMP_X:
        g[0, x] = W_ | LAMP
    for i, mid in enumerate(RACK):
        g[0, RACK_X + i] = W_ | mid
    g[1, :] = W_ | LEDGE


def build(plan: tuple[str, ...] = PLAN) -> np.ndarray:
    """The map blocks of `plan` (the shipped state; the puzzle needs no second state). Bars join bars and side walls,
    the plate under HAGANE and the ingot racks join their own kind and HAGANE's cell."""
    g = np.zeros((len(plan), len(plan[0])), np.uint16)
    _back_wall(g)
    for y in range(BACK_WALL_ROWS, len(plan)):
        for x, ch in enumerate(plan[y]):
            if ch in ".GT":
                g[y, x] = F_ | _floor_tile(plan, x, y)
            elif ch == "L":
                g[y, x] = F_ | PLATE[1]              # HAGANE stands on the middle of his plate
            elif ch == "X":
                g[y, x] = F_ | HAZARD
            elif ch == "w":
                g[y, x] = W_ | SIDE_WALL
            elif ch == "b":
                g[y, x] = W_ | _end_tile(plan, x, y, "bw", BAR)
            elif ch == "p":
                g[y, x] = F_ | _end_tile(plan, x, y, "pL", PLATE)
            elif ch == "i":
                g[y, x] = W_ | _end_tile(plan, x, y, "i", PLATE)
            elif ch == "<":
                g[y, x] = F_ | BELT_WEST
            elif ch == ">":
                g[y, x] = F_ | BELT_EAST
            elif ch == "S":
                g[y, x] = F_ | STEPS
            elif ch == "s":
                g[y, x] = W_ | CRUCIBLE
            elif ch == "M":
                g[y, x] = F_ | MAT[x - plan[y].index("M")]
    return g


# ---------------------------------------------------------------- the puzzle, proved on the plan
def _blocked(plan: tuple[str, ...], x: int, y: int) -> bool:
    """True where the player cannot step: walls, machines, the crucibles and the cells objects stand on."""
    return _cell(plan, x, y) in SOLID


def _press(plan: tuple[str, ...], cell: tuple[int, int], dx: int, dy: int) -> tuple[int, int] | None:
    """Where the player stands still after one key press on `cell`, or None if he cannot move. Stepping onto a belt
    carries him on along it until a cell that is not a belt, or until the next cell is blocked (a wall or an object);
    stepping into a press sends him back to RESTART."""
    x, y = cell[0] + dx, cell[1] + dy
    if _blocked(plan, x, y):
        return None
    while _cell(plan, x, y) in BELTS:
        bx, by = BELTS[plan[y][x]]
        if _blocked(plan, x + bx, y + by):
            break
        x, y = x + bx, y + by
    return RESTART if _cell(plan, x, y) == "X" else (x, y)


def _walk(plan: tuple[str, ...]) -> dict[tuple[int, int], set[tuple[int, int]]]:
    """Every cell the player can stand still on from RESTART, with the cells one key press leads to."""
    edges: dict[tuple[int, int], set[tuple[int, int]]] = {}
    queue = deque([RESTART])
    while queue:
        cell = queue.popleft()
        if cell in edges:
            continue
        edges[cell] = set()
        for dx, dy in DIRECTIONS:
            target = _press(plan, cell, dx, dy)
            if target is not None and target != cell:
                edges[cell].add(target)
                queue.append(target)
    return edges


def _stuck(edges: dict[tuple[int, int], set[tuple[int, int]]]) -> set[tuple[int, int]]:
    """Cells the player can reach but cannot leave for RESTART again (a soft-lock)."""
    back: dict[tuple[int, int], set[tuple[int, int]]] = {cell: set() for cell in edges}
    for cell, targets in edges.items():
        for target in targets:
            back[target].add(cell)
    free, queue = {RESTART}, deque([RESTART])
    while queue:
        for prev in back[queue.popleft()] - free:
            free.add(prev)
            queue.append(prev)
    return set(edges) - free


def _with_cell(plan: tuple[str, ...], cell: tuple[int, int], ch: str) -> tuple[str, ...]:
    """The plan with one cell replaced."""
    x, y = cell
    return plan[:y] + (plan[y][:x] + ch + plan[y][x + 1:],) + plan[y + 1:]


def _cells(plan: tuple[str, ...], ch: str) -> list[tuple[int, int]]:
    """Every cell of the plan holding `ch`, bottom to top and left to right."""
    return sorted(((x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c == ch), key=lambda p: (-p[1], p[0]))


def check_puzzle() -> list[str]:
    """Problems with the puzzle of the card; an empty list means it works as designed.
    The plan agrees with the card's object spots and its plain-floor spots; the route reaches HAGANE and every true gap
    is needed (walling any one off cuts him off); no cell is a soft-lock; every trainer sees the cell the route makes
    the player stop on; and the checker itself catches the card's lane B."""
    problems: list[str] = []
    if _cells(PLAN, "G") != list(TRUE_GAPS):
        problems.append(f"plan gaps {_cells(PLAN, 'G')} differ from the card's {list(TRUE_GAPS)}")
    if _cells(PLAN, "T") != sorted((t.pos for t in TRAINERS), key=lambda p: (-p[1], p[0])) or _cell(PLAN, *LEADER) != "L":
        problems.append("plan objects differ from the card's HAGANE and trainers")
    if _cells(PLAN, "M") != sorted(DOORS, key=lambda p: (-p[1], p[0])):
        problems.append("plan mat differs from DOORS")
    problems += [f"{spot} should be plain floor" for spot in STATUE_VIEW + LUNCHBOXES + (LEADER_TALK, RESTART)
                 if _cell(PLAN, *spot) != "."]
    edges = _walk(PLAN)
    if LEADER_TALK not in edges:
        problems.append(f"HAGANE's talk cell {LEADER_TALK} cannot be reached from {RESTART}")
    for gap in TRUE_GAPS:
        if LEADER_TALK in _walk(_with_cell(PLAN, gap, "b")):
            problems.append(f"HAGANE can be reached without the true gap {gap}")
    if _stuck(edges):
        problems.append(f"soft-lock cells (the player cannot leave them): {sorted(_stuck(edges))}")
    for t in TRAINERS:
        seen = [(t.pos[0] + t.facing * d, t.pos[1]) for d in range(1, t.sight + 1)]
        if t.stop not in seen or any(_blocked(PLAN, *c) for c in seen):
            problems.append(f"the {t.name} does not see the cell {t.stop} on a clear line")
        if t.stop not in edges:
            problems.append(f"the player never stands on {t.stop}, where the {t.name} looks")
    card_lane_b = PLAN[:LANE_B_ROW] + (LANE_B_CARD,) + PLAN[LANE_B_ROW + 1:]
    if not _stuck(_walk(card_lane_b)):
        problems.append("the checker no longer sees the soft-lock in the card's lane B")
    return problems


# ---------------------------------------------------------------- the spec
def _spec(grid: np.ndarray, **fields) -> Spec:
    """The Spec of the gym around `grid`, with the layout id, folder, tilesets and door fixed."""
    return Spec("LAYOUT_SMELTHAM_GYM", "Smeltham_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, **fields)


def smeltham_gym() -> Spec:
    """Smeltham Gym 13 x 20; see the module docstring and the notes below."""
    presses = ", ".join(str(c) for c in sorted(_cells(PLAN, "X"), key=lambda p: (p[1], p[0])))
    return _spec(
        build(),
        npc=(LEADER, LEADER_TALK) + tuple(t.pos for t in TRAINERS) + STATUE_VIEW + LUNCHBOXES,
        title="Smeltham Gym: assembly hall, four conveyor lanes, leader's terrace",
        uses="Smeltham Gym (Gym 4, Steel; HAGANE, RIVET BADGE). Used by that one building only.",
        notes=(
            "Trick House puzzle secondary on the Building primary. The card's tile map is kept cell for cell except: lane "
            "B's west stretch (y 11, x 2-4) is plain floor instead of belts (the card's belts would carry the player into "
            "the Black Belt's cell and box him in, a soft-lock proved by check_puzzle); the exit mat is the set's own "
            "two-tile mat (6, 19) and (7, 19), both warp to Smeltham; the terrace has a gold plate under HAGANE and an "
            "ingot rack in each back corner (x 1-3 and 9-11 on y 2, blocked). No gate and no switch: the shipped grid is "
            "also the solved grid, so no script calls setmetatile and Spec.closed is empty. The puzzle is the choice of "
            "gap in each machine row (y 12, 10, 8, 6): true gaps (8, 12), (5, 10), (11, 8), (5, 6), then the steps (5, 5) "
            "up to the terrace. Every other gap is a press, drawn with the hatched gold tile 653 (the card's hazard "
            "stripe; paint 520 over it for a harder, unmarked puzzle, nothing else changes): put a coord_event (no var) "
            f"on each of {presses} that plays the clang and warpteleports to (6, 18); (1, 10) is walled in by the two "
            "trainers, so it is only decoration. Belts: 608 is MB_WALK_EAST and 609 MB_WALK_WEST already in the tileset "
            "(walk speed; the blue SLIDE arrows 612 and 613 would be faster), nothing to set. Every belt chain ends on a "
            "rest cell (x 1, 5, 8 or 11) and no belt feeds a wall or an object except the Hiker's: the player carried into "
            "(10, 13) stands beside him and steps south into the hall; (11, 11) can only be entered through presses, so "
            "nobody ever stands there. check_puzzle runs a belt-aware walk to prove the "
            "route, that walling off any true gap cuts HAGANE off, and that no cell is a soft-lock. Objects: HAGANE "
            "(6, 3) facing down, talk from (6, 4); Hiker (11, 13) facing west, sight 3, sees (8, 13); Black Belt (1, 11) "
            "facing east, sight 4, sees (5, 11); Guitarist (1, 9) facing east, sight 4, sees (5, 9). That is 4 objects "
            "(a trainer's sight is checked when the player has stopped: if one misses him on his cell, put a coord_event "
            "there to start the fight, as the card says). Crucibles at (3, 16) and (9, 16) are the card's statues: put a sign bg_event on each, read from (3, 17) and "
            "(9, 17); the tile carries MB_TRASH_CAN, which the sign overrides. Lunchbox bg_events on plain floor at "
            "(2, 15), (10, 15), (6, 17) (no art). Look compromises: the tileset is green and gold, not grey; bars are "
            "wooden with bolts; the Poke Ball statues are grey urns; the crusher presses are hatched floor, not machines."
        ),
    )


SPECS = [smeltham_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Smeltham Gym puzzle check failed: " + "; ".join(_PROBLEMS))
