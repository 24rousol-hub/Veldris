"""Hemlock Reach Gym (Gym 7, Poison; ASEBY), the one layout of the 'gym_hemlock' family: a chemical works with four vats.

The plan is the tile map of design/maps/detail/hemlock-reach.md section 6.2 (15 x 22), so every card coordinate holds:
the exit mats (7, 21) and (8, 21), ASEBY (7, 3), the Pokemaniac (4, 7), the Expert (3, 10), the Collector (11, 10), the
Aroma Lady (7, 16), the gym guide (10, 20), the statues (4, 20) and (9, 20), the plaque (5, 14), the three gas curtains
(7, 14), (7, 9) and (7, 5), and the four vats: red (1, 11), yellow (12, 11), blue (1, 17), green (12, 17). It is built on
`gTileset_Building` plus the vanilla `gTileset_Facility` (the Aqua Hideout set), as the card says: pale green mesh floor,
grey walls under a white cornice, window panes, wall cabinets, tank-and-console units and lattice pipe rails.

The gas curtains are shut in the shipped grid, so the hall is cut into four rooms by three pipe rails. Each rail is a row
of the set's lattice railing (solid) with a one-cell gap holding the set's lavender haze tile (solid): the gas. A script
turns a gap into plain floor with `setmetatile` when its valve has run (the card: the green valve drops curtain 1, the red
one curtain 2, the yellow one curtain 3). `CURTAINS` lists the three cells and `OPEN_METATILE` the floor each becomes.
`check_puzzle` proves the four stages on temporary grids (only the initial grid is shipped).

Where this layout differs from the card, each change forced by the tileset's art:
  * the back wall is two rows (cornice, wall face), not three: the Facility set has no three-row wall. Row 2 is the first
    floor row, so ASEBY keeps his card cell (7, 3) with floor behind him;
  * the card's pipe cells at x 0 and x 14 are the white side wall columns, so the rails run from wall to wall and the
    vats stand against the wall. The card's x 0 and x 14 hold no object spot, so none moves;
  * the bottom row is a front wall (cornice over wall face in one tile) with the card's two-cell exit mat in it, so the
    hall does not float in the black border;
  * the card's heart emblem is the set's hazard diamond placard, and its barred windows are plain blue panes;
  * the four vats are four different Facility pieces chosen for their colour, because the set has no recoloured copy of
    one tank (colour table in `VATS`). No new art is drawn.

How the pictures are made, so the builder stays free of magic numbers:
  * the floor is the pale mesh, dark under the back wall and beside the left wall (light from the upper left);
  * a rail piece is a lattice railing with an end post where the rail meets a wall or a gap;
  * a tank unit is the set's three-row tank-and-console and a wall unit is a cabinet on the wall face over its foot cell;
    both are made solid here (the vanilla foot cells are walkable), so the front of each is a walkable cell.
Run `python3 layoutkit.py fam_gym_hemlock OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

from typing import NamedTuple

import numpy as np

import layoutkit as K
from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_Facility"
ID_MASK = 0x03FF            # bits 0-9 of a map block are the metatile id (the top six bits are collision and elevation)

# ---------------------------------------------------------------- metatile ids (secondary index + 512)
FLOOR = 552                 # pale green mesh floor
FLOOR_DARK = 553            # the same floor in shade: under the back wall and beside the left wall
CORNICE = 537               # white cornice over grey wall face in one tile: the back wall's top row and the front wall
FACE = 545                  # grey wall face: the back wall's second row
CORNER = 529                # white cornice corner: the top left and top right of the frame
SIDE = 522                  # white wall column: the left and right wall
WINDOW = 768                # blue window pane in the wall face
EMBLEM = 996                # hazard diamond placard on pale grey: stands in for the card's heart emblem
RAIL_LEFT, RAIL, RAIL_RIGHT = 605, 617, 606   # lattice pipe railing: left end post, straight, right end post
NOTICE = (524, 525)         # white notice board with pink writing: the card's plaque (left half, right half)
HAZE = 944                  # lavender haze: the gas curtain (945 is a second pattern of the same haze)
TANK = ((603, 604), (611, 612), (619, 620))   # tank (left) and control console (right), three rows
WALL_UNITS = {562: 570, 561: 569}   # wall cabinet on the face row (drawers, appliance) -> its foot cell on the floor row
STATUE = 644                # round grey drum with a dark mouth on mesh floor: stands in for the Poke Ball statue
MAT = (518, 519)            # the set's own exit mat: orange pad in a blue-grey frame, SOUTH_ARROW_WARP

# The four vats, 2 x 2 each (top row over bottom row). The set has no recoloured tank, so each colour is the nearest bulky
# piece of that colour: red and green are two-pipe bundles, yellow is hazard-banded drums, blue is a pair of globes.
VATS = {
    "r": ((551, 551), (559, 559)),     # red: two bundles of rust-red pipes
    "y": ((758, 758), (769, 769)),     # yellow: grey drums banded in hazard yellow
    "b": ((993, 993), (1000, 1000)),   # blue: two blue-dotted glass globes in gold cradles over grey consoles
    "g": ((779, 779), (795, 795)),     # green: two fat green pipes
}
VAT_ORIGIN = {"r": (1, 11), "y": (12, 11), "b": (1, 17), "g": (12, 17)}   # top left cell of each vat (the card's)

# ---------------------------------------------------------------- the plan (the card's tile map, 15 x 22)
# =  back wall (rows 0-1), built by `_back_wall`           |  side wall column, solid       F  front wall, solid
# .  floor, walkable. Objects stand on floor cells: L ASEBY, M Pokemaniac, E Expert, C Collector, A Aroma Lady, G guide
# P  lattice rail, solid        N  notice board (two cells in the rail at y14), solid      1 2 3  gas curtain 1, 2, 3, solid
# r y b g  vat, 2 x 2, solid    s  statue, solid        D  exit mat, walkable
PLAN = (
    "|=============|",   # y0
    "|=============|",   # y1
    "|.............|",   # y2  the leader's hall: tank units at x 2-3 and 11-12, wall cabinets, the emblem
    "|......L......|",   # y3  ASEBY (7, 3)
    "|.............|",   # y4  the player talks to him from (7, 4)
    "|PPPPPP3PPPPPP|",   # y5  rail 3, curtain 3 at (7, 5)
    "|.............|",   # y6  upper hall
    "|...M.........|",   # y7  Pokemaniac (4, 7), facing east, sees (5, 7) to (7, 7)
    "|.............|",   # y8
    "|PPPPPP2PPPPPP|",   # y9  rail 2, curtain 2 at (7, 9)
    "|..E.......C..|",   # y10 Expert (3, 10) and Collector (11, 10), both facing south
    "|rr.........yy|",   # y11 red vat (1, 11), yellow vat (12, 11)
    "|rr.........yy|",   # y12 valves: red (2, 12) read from (3, 12), yellow (12, 12) read from (11, 12)
    "|.............|",   # y13
    "|PPPNNP1PPPPPP|",   # y14 rail 1, curtain 1 at (7, 14), the plaque on the notice board (5, 14)
    "|.............|",   # y15 the plaque is read from (5, 15)
    "|......A......|",   # y16 Aroma Lady (7, 16), facing south, sees (7, 17) and (7, 18)
    "|bb.........gg|",   # y17 blue vat (1, 17), green vat (12, 17)
    "|bb.........gg|",   # y18 valves: blue (2, 18) read from (3, 18), green (12, 18) read from (11, 18)
    "|.............|",   # y19
    "|...s....sG...|",   # y20 statues (4, 20) and (9, 20), the gym guide (10, 20)
    "|FFFFFFDDFFFFF|",   # y21 front wall with the exit mat (7, 21) and (8, 21)
)
WIDTH, HEIGHT = len(PLAN[0]), len(PLAN)
CORNICE_ROW, FACE_ROW = 0, 1       # the back wall; row 2 is the first floor row
WINDOW_X = (1, 4, 10, 13)          # the four windows of the card's back wall
EMBLEM_X = 7                       # the emblem hangs over ASEBY's column
TANK_X = (2, 11)                   # left column of each tank unit in the leader's hall; a unit fills rows 1-3
WALL_UNIT_X = {5: 562, 6: 561, 8: 561, 9: 562}   # wall cabinets, mirrored about the emblem
SOLID = frozenset("=|PN123rybgsF")           # plan characters the player cannot enter
FLOOR_CHARS = frozenset(".LMECAG")           # plan characters drawn as floor (the objects stand on them)
CURTAIN_CHARS = "123"              # curtain 1 (y14), 2 (y9) and 3 (y5): the bottom one is the first to drop

# Object and sign spots from the card (the author places the objects, warps, signs and valves in Porymap).
LEADER = (7, 3)                    # ASEBY, facing down
LEADER_TALK = (7, 4)               # the player talks to him from here
GUIDE = (10, 20)
DOORS = ((7, 21), (8, 21))         # the exit mat; both cells warp to Hemlock Reach (card: exterior tile (21, 14))
STATUES = ((4, 20), (9, 20))
STATUE_VIEW = tuple((x, y - 1) for x, y in STATUES)   # the cell in front of each statue, where its sign is read from
PLAQUE = (5, 14)                   # bg_event on the notice board
PLAQUE_VIEW = (5, 15)              # read from here, facing north
CURTAINS = ((7, 14), (7, 9), (7, 5))   # curtain 1, 2, 3: the cells a script turns into floor
# Valves, in the order they are pressed: (vat cell carrying the bg_event, the cell the player stands on, the room it is in).
VALVES = {
    "blue": ((2, 18), (3, 18), 0),     # stage 0 to 1 (COOL), lower hall
    "green": ((12, 18), (11, 18), 0),  # stage 1 to 2 (VENT), lower hall; curtain 1 drops
    "red": ((2, 12), (3, 12), 1),      # stage 2 to 3 (SEAL), middle hall; curtain 2 drops
    "yellow": ((12, 12), (11, 12), 1),  # stage 3 to 4 (DRAIN), middle hall; curtain 3 drops
}


class Trainer(NamedTuple):
    """A gym trainer: where he stands, which way he faces, how far he sees, the cells the card says he sees, his letter."""
    name: str
    pos: tuple[int, int]
    facing: tuple[int, int]
    sight: int
    sees: tuple[tuple[int, int], ...]
    letter: str


TRAINERS = (
    Trainer("Aroma Lady", (7, 16), (0, 1), 2, ((7, 17), (7, 18)), "A"),
    Trainer("Expert", (3, 10), (0, 1), 2, ((3, 11), (3, 12)), "E"),
    Trainer("Collector", (11, 10), (0, 1), 2, ((11, 11), (11, 12)), "C"),
    Trainer("Pokemaniac", (4, 7), (1, 0), 3, ((5, 7), (6, 7), (7, 7)), "M"),
)
OBJECTS = (LEADER, GUIDE) + tuple(t.pos for t in TRAINERS)    # cells an object stands on: 6 of the 15 object slots


# ---------------------------------------------------------------- builder
def _cell(plan: tuple[str, ...], x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan counts as side wall."""
    return plan[y][x] if 0 <= x < WIDTH and 0 <= y < HEIGHT else "|"


def _floor_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Floor cell: shaded under the back wall and beside the left wall, plain anywhere else."""
    return FLOOR_DARK if _cell(plan, x, y - 1) == "=" or _cell(plan, x - 1, y) == "|" else FLOOR


def _rail_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Rail cell: an end post where the rail meets a wall or a curtain, the straight railing anywhere else."""
    if _cell(plan, x - 1, y) not in "PN":
        return RAIL_LEFT
    return RAIL_RIGHT if _cell(plan, x + 1, y) not in "PN" else RAIL


def _back_wall(g: np.ndarray) -> None:
    """Rows 0-1: the cornice over the wall face with four windows and the emblem. The leader's hall furniture stands
    against it: two tank units (rows 1-3) and four wall cabinets (rows 1-2), mirrored about the emblem."""
    g[CORNICE_ROW, :] = W_ | CORNICE
    g[FACE_ROW, :] = W_ | FACE
    for x in WINDOW_X:
        g[FACE_ROW, x] = W_ | WINDOW
    g[FACE_ROW, EMBLEM_X] = W_ | EMBLEM
    for x, head in WALL_UNIT_X.items():
        g[FACE_ROW, x] = W_ | head
        g[FACE_ROW + 1, x] = W_ | WALL_UNITS[head]
    for x in TANK_X:
        for dy, row in enumerate(TANK):
            for dx, mid in enumerate(row):
                g[FACE_ROW + dy, x + dx] = W_ | mid


def build(opened: tuple = ()) -> np.ndarray:
    """The map blocks of `PLAN`; every curtain cell listed in `opened` is floor instead (a later stage of the puzzle).
    The walls, rails, vats, statues and notice board are solid; the objects stand on floor; the mat is walkable."""
    rows = [list(r) for r in PLAN]
    for x, y in opened:
        rows[y][x] = "."
    plan = tuple("".join(r) for r in rows)
    g = np.zeros((HEIGHT, WIDTH), np.uint16)
    for y in range(HEIGHT):
        for x, ch in enumerate(plan[y]):
            if ch in FLOOR_CHARS:
                g[y, x] = F_ | _floor_tile(plan, x, y)
            elif ch == "|":
                g[y, x] = W_ | SIDE
            elif ch == "F":
                g[y, x] = W_ | CORNICE
            elif ch == "P":
                g[y, x] = W_ | _rail_tile(plan, x, y)
            elif ch == "N":
                g[y, x] = W_ | NOTICE[0 if _cell(plan, x - 1, y) != "N" else 1]
            elif ch in CURTAIN_CHARS:
                g[y, x] = W_ | HAZE
            elif ch in VATS:
                vx, vy = VAT_ORIGIN[ch]
                g[y, x] = W_ | VATS[ch][y - vy][x - vx]
            elif ch == "s":
                g[y, x] = W_ | STATUE
            elif ch == "D":
                g[y, x] = F_ | MAT[x - plan[y].index("D")]
    _back_wall(g)
    g[CORNICE_ROW, 0] = g[CORNICE_ROW, WIDTH - 1] = W_ | CORNER
    return g


# ---------------------------------------------------------------- the puzzle, proved on temporary grids
SOLVED = build(CURTAINS)
OPEN_METATILE = {(x, y): int(SOLVED[y, x]) & ID_MASK for x, y in CURTAINS}   # the floor a script sets on each curtain cell


def _spec(grid: np.ndarray, **fields) -> Spec:
    """The Spec of the gym around `grid`, with the layout id, folder, tilesets and door fixed."""
    return Spec("LAYOUT_HEMLOCK_REACH_GYM", "HemlockReach_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, **fields)


def _reach(opened: tuple) -> set[tuple[int, int]]:
    """The cells the player can walk to from the door once the curtains in `opened` are open."""
    return K.reachable(_spec(build(opened)))


def _cells(plan: tuple[str, ...], ch: str) -> list[tuple[int, int]]:
    """Every cell of the plan holding `ch`, top to bottom and left to right."""
    return [(x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c == ch]


def _check_plan() -> list[str]:
    """The plan against the card's spots: objects, statues, mat, curtains, plaque and the four 2 x 2 vats."""
    problems: list[str] = []
    for ch, spot in (("L", LEADER), ("G", GUIDE)):
        if _cells(PLAN, ch) != [spot]:
            problems.append(f"the one '{ch}' cell should be {spot}, the plan has {_cells(PLAN, ch)}")
    problems += [f"the {t.name} {t.pos} is not on a plan cell holding '{t.letter}'" for t in TRAINERS
                 if PLAN[t.pos[1]][t.pos[0]] != t.letter]
    if _cells(PLAN, "s") != list(STATUES) or _cells(PLAN, "D") != list(DOORS):
        problems.append("statues or door mats differ from the card")
    if [c for ch in CURTAIN_CHARS for c in _cells(PLAN, ch)] != list(CURTAINS):
        problems.append("the curtains differ from CURTAINS")
    if PLAN[PLAQUE[1]][PLAQUE[0]] != "N" or PLAN[PLAQUE_VIEW[1]][PLAQUE_VIEW[0]] != ".":
        problems.append("the plaque or its view cell is not where the card puts it")
    for ch, (ox, oy) in VAT_ORIGIN.items():
        if _cells(PLAN, ch) != [(ox + dx, oy + dy) for dy in (0, 1) for dx in (0, 1)]:
            problems.append(f"vat '{ch}' is not the 2 x 2 block at {(ox, oy)}")
    return problems


def _check_valves(stages: list[set[tuple[int, int]]]) -> list[str]:
    """Each valve is a solid vat cell with a walkable stand cell beside it, in the room the card puts it in: the lower
    hall's valves can be pressed at stage 0, the middle hall's only once curtain 1 is open."""
    vat_cells = {c for ch in VATS for c in _cells(PLAN, ch)}
    problems: list[str] = []
    for name, (vat, stand, room) in VALVES.items():
        if vat not in vat_cells:
            problems.append(f"the {name} valve cell {vat} is not a vat cell")
        if abs(vat[0] - stand[0]) + abs(vat[1] - stand[1]) != 1:
            problems.append(f"the {name} valve is not beside its stand cell {stand}")
        if stand not in stages[room]:
            problems.append(f"the {name} valve stand {stand} should be reachable at stage {room}")
        if room and stand in stages[room - 1]:
            problems.append(f"the {name} valve stand {stand} is reachable before curtain {room} opens")
    return problems


def _check_stages(stages: list[set[tuple[int, int]]]) -> list[str]:
    """What each stage opens (stage k has curtains 1 to k open): the lower hall at 0, the middle hall at 1, the upper hall
    at 2, ASEBY's hall at 3. A cell just beyond a curtain is not reachable before it opens."""
    expect = (
        ((GUIDE, PLAQUE_VIEW, TRAINERS[0].pos) + STATUE_VIEW, ((7, 13), (3, 12), (7, 8), LEADER_TALK)),
        (((7, 13), (3, 12), (11, 12), TRAINERS[1].pos, TRAINERS[2].pos), ((7, 8), TRAINERS[3].pos, LEADER_TALK)),
        (((7, 8), TRAINERS[3].pos, (7, 6)), (LEADER_TALK, LEADER)),
        ((LEADER_TALK, LEADER, (7, 2)), ()),
    )
    problems: list[str] = []
    for stage, (want, avoid) in enumerate(expect):
        problems += [f"stage {stage}: {c} should be reachable" for c in want if c not in stages[stage]]
        problems += [f"stage {stage}: {c} should not be reachable" for c in avoid if c in stages[stage]]
    return problems


def check_puzzle() -> list[str]:
    """Problems with the card's puzzle; an empty list means the layout works as designed.
    The plan agrees with the card's spots; each stage opens exactly the next room; every valve is in its room; every
    trainer sees his cells on a clear line; and the solved grid lints clean with every object, talk and valve spot reserved
    (so the path from the door to ASEBY exists once the curtains are open)."""
    stages = [_reach(CURTAINS[:k]) for k in range(len(CURTAINS) + 1)]
    problems = _check_plan() + _check_valves(stages) + _check_stages(stages)
    for t in TRAINERS:
        line = [(t.pos[0] + t.facing[0] * d, t.pos[1] + t.facing[1] * d) for d in range(1, t.sight + 1)]
        if not all(c in line for c in t.sees) or any(PLAN[y][x] in SOLID for x, y in line):
            problems.append(f"the {t.name} does not see {t.sees} on a clear line")
    spots = OBJECTS + (LEADER_TALK, PLAQUE_VIEW) + STATUE_VIEW + tuple(stand for _vat, stand, _room in VALVES.values())
    errors, warnings = K.lint(_spec(SOLVED, npc=spots))
    return problems + [f"solved grid: {m}" for m in errors + warnings]


# ---------------------------------------------------------------- the spec
def hemlock_gym() -> Spec:
    """Hemlock Reach Gym 15 x 22 in its initial state (all three curtains shut); see the module docstring and the notes."""
    initial = build()
    shut = _reach(())
    opened_only = sorted(_reach(CURTAINS) - shut, key=lambda c: (c[1], c[0]))
    opens = [f"setmetatile {x}, {y}, {mid}, FALSE" for (x, y), mid in OPEN_METATILE.items()]
    used = ", ".join(str(m) for m in sorted({int(v) & ID_MASK for v in initial.flatten()}))
    return _spec(
        initial,
        npc=tuple(c for c in (TRAINERS[0].pos, GUIDE, PLAQUE_VIEW) + STATUE_VIEW + (VALVES["blue"][1], VALVES["green"][1])
                  if c in shut),
        closed=tuple(opened_only),
        title="Hemlock Reach Gym: chemical works, three pipe rails with gas curtains, four vats",
        uses="Hemlock Reach Gym (Gym 7, Poison; ASEBY, VIAL BADGE). Used by that one building only.",
        notes=(
            "Facility secondary on the Building primary (the card's pair). INITIAL STATE: all three curtains shut. A "
            "curtain is the haze tile 944, solid (collision 1, elevation 0), in a one-cell gap of a pipe rail. SOLVED "
            f"STATE: the script sets each curtain cell to plain floor: curtain 1 (green valve, stage 1 to 2) {opens[0]}; "
            f"curtain 2 (red valve, stage 2 to 3) {opens[1]}; curtain 3 (yellow valve, stage 3 to 4) {opens[2]}; then "
            "special DrawWholeMapView. No neighbour cell changes (nothing here casts a shadow into a gap). setmetatile "
            "keeps the cell's elevation (0 on the shipped curtain), which is harmless: elevation 0 matches any level "
            "(Crestfall's gates do the same). On MAP_SCRIPT_ON_LOAD re-open curtain 1 when VAR_HEMLOCK_GYM_VALVES >= 2, "
            "curtain 2 when >= 3, curtain 3 when >= 4. Spec.closed lists the walkable cells that stay cut off until the "
            "curtains open (everything above the lowest rail); Spec.npc holds only the spots reachable from the door in "
            "the initial state (the lint rejects the others); check_puzzle proves the four stages on temporary grids and "
            "lints the solved grid with every spot reserved, so the path from the door to ASEBY exists once all three "
            "curtains are open. "
            "ROOMS: lower hall y15-20 (blue and green valves, Aroma Lady, guide, statues), middle hall y10-13 (red and "
            "yellow valves, Expert, Collector), upper hall y6-8 (Pokemaniac), ASEBY's hall y2-4. "
            f"OBJECTS (suggested spots, 6 of 15): ASEBY {LEADER} facing south, talked to from {LEADER_TALK}; Aroma Lady "
            "(7, 16) facing south, sight 2, sees (7, 17) and (7, 18); Expert (3, 10) facing south, sight 2, sees (3, 11) "
            "and (3, 12), the red valve's stand cell; Collector (11, 10) facing south, sight 2, sees (11, 11) and "
            "(11, 12), the yellow valve's stand cell; Pokemaniac (4, 7) facing east, sight 3, sees (5, 7) to (7, 7), "
            f"where the player comes out of curtain 2; gym guide {GUIDE}. The Aroma Lady only sees column x 7, so the "
            "player can walk round her (row y15 is open) and she is optional unless the author adds a trigger. "
            "VALVES (bg_event on the vat cell, facing any; the player stands on the walkable cell): blue (2, 18) from "
            "(3, 18) facing west; green (12, 18) from (11, 18) facing east; red (2, 12) from (3, 12) facing west; yellow "
            "(12, 12) from (11, 12) facing east. PLAQUE: the notice board is two cells, (4, 14) and (5, 14); put the "
            "PROCEDURE 4 sign on both, read from (4, 15) or (5, 15) facing north. STATUES: the grey drums at (4, 20) and "
            "(9, 20), a sign on each, read from (4, 19) and (9, 19) (or from either side). "
            f"WARPS: one on each mat tile, {DOORS[0]} and {DOORS[1]}, both to HemlockReach (card: warp 6, exterior tile "
            "(21, 14)). Other furniture: two tank units (x 2-3 and x 11-12, rows 1-3) and four wall cabinets (x 5, 6, 8, "
            "9, rows 1-2) flank the emblem at (7, 1); all are solid with a walkable front row (y4 for the tanks, y3 for "
            "the cabinets), so a sign or behaviour on any of them can be read. "
            "VAT COLOURS (no recoloured tank exists, so each is the nearest bulky piece of its colour, all 2 x 2 solid): "
            "blue = two blue-dotted globes in gold cradles over grey consoles (993 over 1000, at (1, 17)); green = two "
            "fat green pipes (779 over 795, at (12, 17)); red = two bundles of rust-red pipes (551 over 559, at (1, 11)); "
            "yellow = grey drums banded in hazard yellow (758 over 769, at (12, 11)). "
            "Behaviours the pieces already carry: the notice board 524 and 525 is MB_BLUEPRINT and the statue drum 644 "
            "is MB_TRASH_CAN (a bg_event sign on the cell overrides both; without one the stock blueprint or trash can "
            "line plays); the cornice 537 is MB_COUNTER (harmless on a wall); the mat 518 and 519 is "
            "MB_SOUTH_ARROW_WARP. "
            "Look compromises: the card's three-row back wall is two rows plus a floor row; the heart emblem is a hazard "
            "diamond placard; the barred windows are plain panes; the pink Fuchsia floor is the pale green mesh; the "
            "gas is one static lavender haze tile; the statue is a grey drum on a floor patch a shade darker than the "
            f"mesh. Used metatile ids (secondary ids are 512 + index; no primary tile): {used}."
        ),
    )


SPECS = [hemlock_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Hemlock Reach Gym puzzle check failed: " + "; ".join(_PROBLEMS))
