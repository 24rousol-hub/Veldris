"""Beaconmouth Lighthouse Gym (Gym 9, Water), the three layouts of the 'gym_beaconmouth' family: 1F the Pump Room, 2F the
Gallery and 3F the Lamp Room of a flooded lighthouse. The player climbs by turning valve wheels in the right order; every
right turn lowers the water and a strip of sand or mesh walkway appears.

The plans are the three tile maps of design/maps/detail/beaconmouth.md section 6.3 (15 x 21, 15 x 21 and 15 x 19), so the
card's coordinates hold: exit mats (6, 20) and (7, 20); 1F wheels Brass (0, 18), Red (0, 11) and Blue (14, 11), logbook
(3, 18), statues (5, 19) and (8, 19), Corrin (7, 13) and Marlo (10, 9); 2F wheels Blue (0, 14) and Red (14, 16), the
permanent gap (1, 9) to (1, 10), Ivo (12, 10) and Hobb (10, 4); 3F lever (13, 15), guide (13, 14), MIZZLE (8, 3), the
platform (6 to 10, 3 to 5) and the catwalk that winds round to it. Every strip of every step is where the card has it.

Tilesets: `gTileset_General` plus `gTileset_Facility`, the pair of the vanilla Slateport Harbor (a railed indoor pool) and
the Aqua Hideout (indoor pools, white pipe walls). The card paints on a 'Sewer tileset' that is not in the tree, and the
Building primary that the gyms use has 8 metatiles and no water. The General primary has the sea water and sand, and the
Facility secondary has the rest of a pump room: steel walls and windows, white pipes, hex tile floor, stairs, orange mats.
Palladium's Water panel is not available offline, so the look follows the card's text: a pale blue-green tile floor, a
deep pool, cream sand, steel mesh walkways, brass lamps.

What stands in for the card's pieces (nothing is drawn, every tile is vanilla):
  * the steel mesh gantry is the Mt. Pyre floor mesh (743), the water is the General sea water (368, in shade 369), the
    sandbars and the drained strips are plain sand (289);
  * a valve wheel is a wall fitting in the white pipe wall: Brass is the brass cylinder (538), Red the orange hose coil
    (546), Blue the valve pipe (604); the 3F lever is the control panel with a slot (561). The set has no wheel art;
  * the gym statues are the white ring buoy (517, the set's bin art, MB_TRASH_CAN: the statue's bg_event overrides the
    'empty bin' line); the keeper's lectern is the desk with a notepad (548);
  * the central pump is the lower 4 x 3 pieces of the Slateport shipyard boiler: the card's 3 wide P is 4 wide (x 6 to 9)
    because that art is 4 wide;
  * the brass lamp is a 2 x 2 block of the Aqua Hideout porthole lamp (735) and the four porthole lamps are single ones,
    at x 3, 5, 10 and 12 (the card has 3, 6, 9 and 12, which would touch the big lamp);
  * the card's brick wall with arched alcoves is the steel wall with windows and drain pipes (1F, 2F) or portholes (3F).
Where the plans differ from the card:
  * the stairs are two tiles wide because the stair art is: (6, 1) and (7, 1) on 1F and 2F, above the card's (7, 1). They
    lead to the two-wide stair block at the foot of the next floor, (6, 20) and (7, 20) on 2F, so a player who goes up
    arrives in the column he left, and (11, 18) and (12, 18) on 3F. The 3F entrance corridor is two wide (x 11 to 12,
    y 15 to 17) so that both stair tiles have floor above them;
  * the 2F top walkway has a three-row wall above it, so the gallery (6 to 8, 2) is a niche in it;
  * the platform is the card's 5 x 3 block, not a cross (the plan has the block, the cross is in the Palladium picture);
  * the card's FACE_DOWN for Hobb is wrong: his alcove (10, 4) lies south of the walkway cell (10, 3) he guards, so he
    faces up;
  * Corrin's and Marlo's sight is 1, not 4 (see below).

Initial state is what ships: every strip is water. `check_puzzle` builds each stage on temporary grids and proves the
card's order of play: what each step makes reachable, that the strips are the only cells that change, that the wheels can
be reached at every stage from cells that never flood, that the stairs and the leader are reachable only at the end, and
that the solved floor lints clean with every object spot reserved.

Trainers walk up to a player they see and then stay where they stopped. The card gives Corrin and Marlo a sight of 4
down a one-tile strip: each would stop ON the strip and shut it for good (a gym has no Dig and no Escape Rope).
`check_puzzle` tries every cell a trainer can notice the player on, with the trainer standing where he would stop, and
fails the card's sight 4 on 1F. Sight 1 at the card's cells works: Corrin (7, 13) sees only (7, 14), the one cell where
strip A meets his island, and Marlo (10, 9) sees only (10, 10), the one cell where strip B meets hers. Neither has to
move, both fights are forced, and no trainer's sight can be walked round. 2F's alcove trainers have sight 1 as the card
has them.

Run `python3 layoutkit.py fam_gym_beaconmouth OUT_DIR` from this folder to lint and draw the three layouts.
"""
from __future__ import annotations

from typing import NamedTuple

import numpy as np

import layoutkit as K
from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_General", "gTileset_Facility"
Cell = tuple[int, int]
ID_MASK, FLAG_MASK = 0x03FF, 0xFC00   # bits 0-9 of a map block are the metatile id; the top six are collision and elevation

# ---------------------------------------------------------------- metatile ids (General < 512, Facility = index + 512)
WATER = 368                  # open water with ripples (General): MB_OCEAN_WATER, blocked here by the collision bit
WATER_SHADE = 369            # the same water in shade: under a raised cell, or right of one
SAND = 289                   # plain cream sand (General): sandbars and drained strips
HEX_FLOOR = 514              # pale teal hex tile
HEX_FLOOR_SHADE = 530        # the same tile with the shadow of the wall above it
MESH = 743                   # steel mesh gantry (the Mt. Pyre floor): MB_CAVE, so keep wild encounters off this map
CAP = 537                    # top of a wall: white coping (MB_COUNTER, harmless: no one stands behind it)
BODY = 946                   # plain steel wall
FOOT = 545                   # foot of a wall: a light line over a dark skirting
WINDOW_TOP = 760             # window in the top row of a wall, coping above the glass
WINDOW_SILL = 768            # window, glass over the sill
DRAIN = 544                  # vertical drain pipe down the wall
SIDE = 522                   # white pipe: the side walls
LEDGE = 888                  # dark ledge: the bottom wall, and the edge of the dark mass behind the 3F pool
VOID = 513                   # black
UP = (808, 809)              # stairs up, two tiles wide (MB_NORTH_ARROW_WARP)
DOWN = (816, 817)            # stairs down, two tiles wide (MB_SOUTH_ARROW_WARP)
MAT = (518, 519)             # orange exit mat, two tiles wide (MB_SOUTH_ARROW_WARP)
PORTHOLE = 735               # round white lamp in a brass frame (the Aqua Hideout warp pad art, MB_AQUA_HIDEOUT_WARP): solid
WHEEL_BRASS, WHEEL_RED, WHEEL_BLUE = 538, 546, 604   # brass cylinder, orange hose coil, valve pipe
LEVER = 561                  # control panel with a slot
BUOY = 517                   # white ring on teal tile: the gym statue (MB_TRASH_CAN)
LECTERN = 548                # desk with a notepad: the keeper's logbook
PUMP = ((579, 580, 581, 582), (587, 588, 589, 590), (WATER, 597, 598, WATER))   # shipyard boiler, lower half; solid
LAMP = ((PORTHOLE, PORTHOLE), (PORTHOLE, PORTHOLE))

# ---------------------------------------------------------------- the plans (the card's tile maps)
# #  wall: top rows, white side pipes, the ledge along the bottom       x  dark mass behind the 3F pool
# .  teal hex floor   m  steel mesh gantry   s  sand (sandbar or sand catwalk)   ~  open water, blocked
# 1 2 3 4 5  water that a script turns into sand (1F, 3F) or mesh (2F) at that step: the card's numbering
# P  the central pump, blocked      U  stairs up (2 wide)      D  stairs down (2 wide)      M  exit mat (2 wide)
PLAN_1F = (
    "###############",   # y0   top wall: coping, then the foot
    "######UU#######",   # y1   stairs up (6, 1) and (7, 1)
    "##...........##",   # y2   the north gallery
    "##...........##",   # y3
    "##~~~~~~3~~~~##",   # y4   strip C (8, 4) to (8, 7)
    "##~~~~~~3~~~~##",
    "##~~~~~~3~~~~##",
    "##~~~~~~3~~~~##",
    "#m~~~~~~ssss~m#",   # y8   island 2 (8-11, 8-10); the catwalks x 1 and x 13 start here
    "#m~~~~~~ssss~m#",
    "#m~~~~~~ssss~m#",
    "#m~~~~~~~~2~~m#",   # y11  strip B (10, 11) to (10, 13); the Red and Blue wheel stands (1, 11) and (13, 11)
    "#m~~~sssss2~~m#",   # y12  island 1 (5-9, 12-14)
    "#m~~~sssss2~~m#",
    "#m~~~sssss~~~m#",
    "#m~~~~~1~~~~~m#",   # y15  strip A (7, 15) and (7, 16)
    "#m~~~~~1~~~~~m#",
    "#m...........m#",   # y17  the south hall
    "#m...........m#",   # y18  the Brass wheel stand (1, 18)
    "#m...........m#",
    "######MM#######",   # y20  exit mats (6, 20) and (7, 20)
)
PLAN_2F = (
    "###############",
    "######UU#######",   # y1   stairs up (6, 1) and (7, 1)
    "######...######",   # y2   the gallery niche (6-8, 2)
    "#mmmmmmmmmmmmm#",   # y3   the top walkway
    "#m~~~~~~~~m~~m#",   # y4   Hobb's alcove (10, 4)
    "#m~~~~~~~~~~~m#",
    "#m~~~~~~~~~~~m#",
    "#m~~~~~~~~~~~5#",   # y7   gap GB (13, 7) and (13, 8)
    "#m~~~~~~~~~~~5#",
    "#~~~~~PPPP~~~m#",   # y9   the permanent gap (1, 9) and (1, 10); the pump
    "#~~~~~PPPP~~mm#",   # y10  Ivo's alcove (12, 10)
    "#m~~~~~PP~~~~m#",
    "#m~~~~~~~~~~~4#",   # y12  gap GA (13, 12) and (13, 13)
    "#m~~~~~~~~~~~4#",
    "#m~~~~~~~~~~~m#",   # y14  the Blue wheel stand (1, 14)
    "#m~~~~~~~~~~~m#",
    "#m~~~~~~~~~~~m#",   # y16  the Red wheel stand (13, 16)
    "#m~~~~~~~~~~~m#",
    "#m...........m#",   # y18  the arrival platform
    "#m...........m#",
    "######DD#######",   # y20  stairs down (6, 20) and (7, 20)
)
PLAN_3F = (
    "###############",
    "###############",
    "###############",   # y0-2 back wall: lamp and portholes
    "#~~~~~sssss~~~#",   # y3   the platform (6-10, 3-5), MIZZLE at (8, 3)
    "#~~~~~sssss~~~#",
    "#~~~~~sssss~~~#",
    "#~~~~~~~~~1~~~#",   # y6   the sluice strip (10, 6) and (10, 7)
    "#~~~~~~~~~1~~~#",
    "#~~~~~~~~~s~~~#",
    "#~~~~~~~~~s~~~#",
    "#~~~sssssss~~~#",   # y10  the catwalk east along y10
    "#~~~s~~~~~~~~~#",
    "#~~~s~~~~~~~~~#",
    "#~~~s~~~~~~~~~#",
    "#~~~sssssssss.#",   # y14  the catwalk west along y14; the guide's alcove (13, 14)
    "#~~~~~~~~~~ss##",   # y15  the lever stand (12, 15)
    "xxxxxxxxxx#ss##",
    "xxxxxxxxxx#ss##",
    "xxxxxxxxxx#DD##",   # y18  stairs down (11, 18) and (12, 18)
)


# ---------------------------------------------------------------- what stands where
class Wheel(NamedTuple):
    """A valve wheel or lever: a bg_event on a wall tile that the player reads from `stand`, facing the wall."""
    name: str
    wall: Cell
    stand: Cell
    piece: int


class Actor(NamedTuple):
    """A person on the floor: where he stands, which way he faces and how far he sees (0 for one who is only talked to).
    `card_sight` is the sight the card gives him."""
    name: str
    pos: Cell
    facing: Cell
    sight: int
    card_sight: int


class Floor(NamedTuple):
    """One floor: the plan, the fittings that are not in the plan, and the actors."""
    layout_id: str
    folder: str
    plan: tuple[str, ...]
    wall_rows: int               # rows of wall across the top: the 1F wall is thin, the others have a body row
    drained: str                 # plan character that a strip becomes: sand or mesh
    doors: tuple[Cell, ...]      # the exit mats or the stairs down at the foot
    stairs_up: tuple[Cell, ...]
    goal: Cell                   # where the floor leads: the stairs up, or the cell in front of the leader
    wheels: tuple[Wheel, ...]    # in the order they are turned
    actors: tuple[Actor, ...]
    props: dict[Cell, int]       # other solid fittings
    views: tuple[Cell, ...] = ()       # cells in front of the props that carry a sign (statues, lectern)
    windows: tuple[int, ...] = ()      # columns of the back wall with a window
    drains: tuple[int, ...] = ()       # columns of the back wall with a drain pipe
    water_gaps: tuple[Cell, ...] = ()  # cells that must be water in every state


def _block(x: int, y: int, rows: tuple[tuple[int, ...], ...]) -> dict[Cell, int]:
    """The cells of a piece whose top left cell is (x, y), as {cell: metatile}."""
    return {(x + dx, y + dy): m for dy, row in enumerate(rows) for dx, m in enumerate(row)}


UP_FACING, DOWN_FACING, LEFT_FACING, RIGHT_FACING = (0, -1), (0, 1), (-1, 0), (1, 0)
STAIRS_UP = ((6, 1), (7, 1))     # 1F and 2F: the card's (7, 1) and the cell beside it
FLOOR_1F = Floor(
    "LAYOUT_BEACONMOUTH_GYM_1F", "Beaconmouth_Gym_1F", PLAN_1F, 2, "s", ((6, 20), (7, 20)), STAIRS_UP, (7, 1),
    wheels=(Wheel("Brass", (0, 18), (1, 18), WHEEL_BRASS), Wheel("Red", (0, 11), (1, 11), WHEEL_RED),
            Wheel("Blue", (14, 11), (13, 11), WHEEL_BLUE)),
    actors=(Actor("Corrin", (7, 13), DOWN_FACING, 1, 4), Actor("Marlo", (10, 9), DOWN_FACING, 1, 4)),
    props={(3, 18): LECTERN, (5, 19): BUOY, (8, 19): BUOY},
    views=((3, 17), (5, 18), (8, 18)),
    windows=(2, 11), drains=(4, 9),
)
FLOOR_2F = Floor(
    "LAYOUT_BEACONMOUTH_GYM_2F", "Beaconmouth_Gym_2F", PLAN_2F, 3, "m", ((6, 20), (7, 20)), STAIRS_UP, (7, 1),
    wheels=(Wheel("Blue", (0, 14), (1, 14), WHEEL_BLUE), Wheel("Red", (14, 16), (13, 16), WHEEL_RED)),
    actors=(Actor("Ivo", (12, 10), RIGHT_FACING, 1, 1), Actor("Hobb", (10, 4), UP_FACING, 1, 1)),
    props=_block(6, 9, PUMP),
    windows=(2, 11), drains=(4, 9),
    water_gaps=((1, 9), (1, 10)),
)
FLOOR_3F = Floor(
    "LAYOUT_BEACONMOUTH_GYM_3F", "Beaconmouth_Gym_3F", PLAN_3F, 3, "s", ((11, 18), (12, 18)), (), (8, 4),
    wheels=(Wheel("Lever", (13, 15), (12, 15), LEVER),),
    actors=(Actor("Mizzle", (8, 3), DOWN_FACING, 0, 0), Actor("Guide", (13, 14), LEFT_FACING, 0, 0)),
    props={**_block(7, 1, LAMP), **{(x, 2): PORTHOLE for x in (3, 5, 10, 12)}},
)
FLOORS = (FLOOR_1F, FLOOR_2F, FLOOR_3F)
STEP_CHARS = "12345"
WALL_COLUMNS = {1: (CAP,), 2: (CAP, FOOT), 3: (CAP, BODY, FOOT)}   # a wall column by its height in rows


# ---------------------------------------------------------------- builder
def _strips(floor: Floor) -> dict[str, tuple[Cell, ...]]:
    """Step character -> the cells that become sand or mesh when that step is done, in reading order."""
    return {ch: tuple((x, y) for y, row in enumerate(floor.plan) for x, c in enumerate(row) if c == ch)
            for ch in STEP_CHARS if any(ch in row for row in floor.plan)}


def _wall_height(floor: Floor, x: int) -> int:
    """Rows of wall at the top of column x: the run of '#' from the top, at most `wall_rows`."""
    height = 0
    while height < floor.wall_rows and floor.plan[height][x] == "#":
        height += 1
    return height


def _paint_wall(g: np.ndarray, floor: Floor) -> None:
    """The back wall and its fittings: coping, body and foot by column height, windows, drain pipes."""
    for x in range(g.shape[1]):
        height = _wall_height(floor, x)
        for y, m in enumerate(WALL_COLUMNS[height] if height else ()):
            g[y, x] = W_ | m
    for x in floor.windows:
        g[0, x], g[1, x] = W_ | WINDOW_TOP, W_ | WINDOW_SILL
    for x in floor.drains:
        for y in range(1, _wall_height(floor, x)):
            g[y, x] = W_ | DRAIN


def _paint_cell(floor: Floor, x: int, y: int, ch: str) -> int:
    """The map block of one plan cell, apart from the back wall."""
    plan = floor.plan
    if ch == "#":
        return W_ | (LEDGE if y == len(plan) - 1 else SIDE)
    if ch == "x":   # the dark mass: a ledge where it faces the pool above, black elsewhere
        return W_ | (LEDGE if plan[y - 1][x] not in "x#" else VOID)
    if ch == ".":
        return F_ | (HEX_FLOOR_SHADE if plan[y - 1][x] == "#" else HEX_FLOOR)
    if ch in "ms":
        return F_ | (MESH if ch == "m" else SAND)
    if ch in "~P":
        return W_ | WATER
    if ch in "UDM":
        return F_ | {"U": UP, "D": DOWN, "M": MAT}[ch][x - plan[y].index(ch)]
    raise ValueError(f"unknown plan character {ch!r} at ({x}, {y})")


def _shade_water(g: np.ndarray) -> None:
    """Light from the upper left: water under a raised cell (wall, floor, mesh, a fitting) or right of one is in shade.
    Sand is level with the water, so it casts none."""
    raised = lambda v: (int(v) & ID_MASK) not in (WATER, WATER_SHADE, SAND)
    for y in range(g.shape[0]):
        for x in range(g.shape[1]):
            if (int(g[y, x]) & ID_MASK) == WATER and ((y and raised(g[y - 1, x])) or (x and raised(g[y, x - 1]))):
                g[y, x] = (int(g[y, x]) & FLAG_MASK) | WATER_SHADE


def build(floor: Floor, steps: str = "") -> np.ndarray:
    """The map blocks of a floor with the steps in `steps` done ('' is the initial state that ships, '123' the solved 1F).
    A strip is solid water until its step is done; a drained strip is walkable sand or mesh."""
    g = np.zeros((len(floor.plan), len(floor.plan[0])), np.uint16)
    for y, row in enumerate(floor.plan):
        for x, ch in enumerate(row):
            if ch in STEP_CHARS:
                ch = floor.drained if ch in steps else "~"
            g[y, x] = _paint_cell(floor, x, y, ch)
    _paint_wall(g, floor)
    for wheel in floor.wheels:
        g[wheel.wall[1], wheel.wall[0]] = W_ | wheel.piece
    for (x, y), m in floor.props.items():
        g[y, x] = W_ | m
    _shade_water(g)
    return g


# ---------------------------------------------------------------- the proof: what each step makes reachable
class Stage(NamedTuple):
    """The floor after the steps in `steps` are done: cells that must be reachable from the door, and cells that must not."""
    steps: str
    reach: tuple[Cell, ...]
    cut: tuple[Cell, ...]


STAGES = {
    FLOOR_1F.folder: (
        Stage("", ((7, 17), (1, 8), (13, 8)), ((7, 14), (10, 10), (8, 8), (8, 3), (7, 1))),
        Stage("1", ((7, 14), (7, 13), (9, 13), (5, 12)), ((10, 10), (8, 8), (8, 3), (7, 1))),
        Stage("12", ((10, 10), (10, 9), (8, 8), (11, 8)), ((8, 3), (7, 1))),
        Stage("123", ((8, 3), (4, 2), (12, 3), (7, 2), (6, 1), (7, 1)), ()),
    ),
    FLOOR_2F.folder: (
        Stage("", ((7, 19), (1, 11), (13, 14)), ((1, 8), (13, 11), (12, 10), (13, 6), (13, 3), (10, 3), (7, 3), (7, 1))),
        Stage("4", ((13, 13), (13, 11), (13, 10), (12, 10), (13, 9)), ((13, 6), (13, 3), (10, 3), (7, 3), (7, 1))),
        Stage("45", ((13, 7), (13, 3), (10, 3), (10, 4), (7, 3), (1, 3), (1, 8), (7, 2), (6, 1), (7, 1)), ()),
    ),
    FLOOR_3F.folder: (
        Stage("", ((12, 14), (13, 14), (4, 14), (4, 10), (10, 10), (10, 8)), ((10, 5), (8, 4), (8, 3))),
        Stage("1", ((10, 6), (10, 5), (8, 4), (8, 3), (6, 3)), ()),
    ),
}
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def _spec(floor: Floor, grid: np.ndarray, **fields) -> Spec:
    return Spec(floor.layout_id, floor.folder, grid, PRIMARY, SECONDARY, doors=floor.doors, **fields)


def _all_steps(floor: Floor) -> str:
    return "".join(_strips(floor))


def _cells(plan: tuple[str, ...], chars: str) -> tuple[Cell, ...]:
    """Every cell of the plan holding one of `chars`, in reading order."""
    return tuple((x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c in chars)


def _front(actor: Actor) -> Cell:
    """The cell the actor faces: where the player stands to talk to one who is only talked to."""
    return actor.pos[0] + actor.facing[0], actor.pos[1] + actor.facing[1]


def _spots(floor: Floor) -> tuple[Cell, ...]:
    """The cells an object or the player must be able to stand on: actors, the cell in front of each one who is only
    talked to, wheel stands, and the cells in front of the signs."""
    return (tuple(a.pos for a in floor.actors) + tuple(_front(a) for a in floor.actors if not a.sight)
            + tuple(w.stand for w in floor.wheels) + floor.views)


def _flood(grid: np.ndarray, start: Cell, blocked: frozenset[Cell]) -> set[Cell]:
    """Walkable cells reachable from `start` without entering `blocked`."""
    seen, queue = {start}, [start]
    while queue:
        x, y = queue.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0] and (nx, ny) not in seen and (nx, ny) not in blocked
                    and K.passable(grid[ny, nx])):
                seen.add((nx, ny))
                queue.append((nx, ny))
    return seen


def _sight(grid: np.ndarray, actor: Actor) -> tuple[Cell, ...]:
    """The cells an actor notices the player on: up to `sight` in front of him, ending before the first blocked cell."""
    cells, (x, y) = [], actor.pos
    for _ in range(actor.sight):
        x, y = x + actor.facing[0], y + actor.facing[1]
        if not (0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]) or not K.passable(grid[y, x]):
            break
        cells.append((x, y))
    return tuple(cells)


def _walk_up_problems(floor: Floor, solved: np.ndarray) -> list[str]:
    """A trainer who notices the player walks along his line to the cell next to him and stays. For every cell he can notice
    the player on (with him standing on the cell where he stops and the others where they stand) the player must still reach
    the goal; and no trainer's sight may be walkable round, or the fight could be skipped."""
    problems = []
    entry = (floor.doors[0][0], floor.doors[0][1] - 1)
    for actor in floor.actors:
        others = frozenset(a.pos for a in floor.actors if a is not actor)
        seen = _sight(solved, actor)
        if actor.sight and not seen:
            problems.append(f"{actor.name} at {actor.pos} sees nothing")
        for walked, cell in enumerate(seen):
            stop = (actor.pos[0] + actor.facing[0] * walked, actor.pos[1] + actor.facing[1] * walked)
            if floor.goal not in _flood(solved, cell, others | {stop}):
                problems.append(f"{actor.name} noticing the player on {cell} stops on {stop} and shuts the way to "
                                f"{floor.goal}")
        if seen and floor.goal in _flood(solved, entry, others | frozenset(seen) | {actor.pos}):
            problems.append(f"{actor.name}'s sight {seen} can be walked round")
    return problems


def _adjacent(a: Cell, b: Cell) -> bool:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def check_floor(floor: Floor) -> list[str]:
    """Problems with one floor; an empty list means it works as designed (see the module docstring for what is proved)."""
    problems: list[str] = []
    initial, solved = build(floor), build(floor, _all_steps(floor))
    strips = _strips(floor)
    if _cells(floor.plan, "U") != floor.stairs_up:
        problems.append(f"the up stairs are {_cells(floor.plan, 'U')}, not {floor.stairs_up}")
    if _cells(floor.plan, "DM") != floor.doors:
        problems.append(f"the stairs or mats at the foot are {_cells(floor.plan, 'DM')}, not {floor.doors}")
    done = ""
    for ch in strips:      # each step changes its strip and nothing else, so no neighbour needs a new shade
        done += ch
        changed = {(x, y) for y, x in np.argwhere(build(floor, done) != initial)}
        if changed != {c for k in done for c in strips[k]}:
            problems.append(f"after steps {done} the cells that change are {sorted(changed)}, not just the strips")
    for wheel in floor.wheels:
        if floor.plan[wheel.wall[1]][wheel.wall[0]] != "#" or not _adjacent(wheel.wall, wheel.stand):
            problems.append(f"{wheel.name} wheel {wheel.wall} is not a wall cell next to its stand {wheel.stand}")
        if any(wheel.stand in cells for cells in strips.values()):
            problems.append(f"{wheel.name} wheel is read from {wheel.stand}, which floods")
    for view in floor.views:
        if not any(_adjacent(view, prop) for prop in floor.props):
            problems.append(f"the sign cell {view} is not next to a prop")
    for stage in STAGES[floor.folder]:
        reached = K.reachable(_spec(floor, build(floor, stage.steps)))
        wanted = stage.reach + tuple(w.stand for w in floor.wheels)
        problems += [f"steps {stage.steps!r}: {c} should be reachable" for c in wanted if c not in reached]
        problems += [f"steps {stage.steps!r}: {c} should be cut off" for c in stage.cut if c in reached]
    problems += [f"{c} should be water in every state" for c in floor.water_gaps if K.passable(solved[c[1], c[0]])]
    errors, warnings = K.lint(_spec(floor, solved, npc=_spots(floor)))
    problems += [f"solved grid: {m}" for m in errors + warnings]
    problems += _walk_up_problems(floor, solved)
    card = floor._replace(actors=tuple(a._replace(sight=a.card_sight) for a in floor.actors))
    if card != floor and not _walk_up_problems(card, solved):
        problems.append("the checker no longer sees the trap in the card's trainer sight")
    return problems


def check_puzzle() -> list[str]:
    """Problems with all three floors, including the stair blocks: the stairs down of a floor are as wide as the stairs up
    of the floor below."""
    problems = [f"{f.folder}: {m}" for f in FLOORS for m in check_floor(f)]
    for below, above in zip(FLOORS, FLOORS[1:]):
        if len(below.stairs_up) != len(above.doors):
            problems.append(f"{below.folder} has {len(below.stairs_up)} stair tiles up, but {above.folder} has "
                            f"{len(above.doors)} down")
    return problems


# ---------------------------------------------------------------- the specs
def _cell_text(cells) -> str:
    """'(3, 4), (5, 6)' for cells in reading order."""
    return ", ".join(str(c) for c in sorted(cells, key=lambda c: (c[1], c[0])))


COMMON_NOTES = (
    "General primary and Facility secondary (the module docstring says why, and what stands in for the card's art). "
    "Map settings: indoor, MUS_GYM, gym battle scene, and no wild_encounters entry (the mesh 743 is MB_CAVE, which flags "
    "encounters). Leave the water behaviour alone: 368 and 369 are MB_OCEAN_WATER, the sea of every outdoor map, and the "
    "collision bit already blocks them (the Surf and fishing checks need an elevation mismatch, which a blocked cell "
    "never gives)."
)


def _changes_text(floor: Floor) -> str:
    """What the scripts do to the grid: the setmetatile calls of each step, and how to flood a step back."""
    strips, initial = _strips(floor), build(floor)
    solved = build(floor, _all_steps(floor))
    steps = "; ".join(
        f"step {ch} ({wheel.name}): "
        + ", ".join(f"setmetatile {x}, {y}, {int(solved[y, x]) & ID_MASK}, FALSE" for x, y in cells)
        for (ch, cells), wheel in zip(strips.items(), floor.wheels))
    shaded = [c for cells in strips.values() for c in cells if int(initial[c[1], c[0]]) & ID_MASK == WATER_SHADE]
    flood = f"{WATER}, TRUE" + (f" (but {WATER_SHADE} on {_cell_text(shaded)})" if shaded else "")
    return (f"Initial state ships: every strip is solid water (collision 1, elevation 0). {steps}. setmetatile keeps the "
            f"elevation, so a drained strip is walkable (elevation 0 never mismatches) and no neighbouring cell needs a new "
            f"tile. To flood a step back set its cells to {flood}; on entering the map re-apply every step already done.")


def _objects_text(floor: Floor) -> str:
    """The signs and objects: wheels with their stands, actors with facing and sight (the card's sight where it differs)."""
    names = {UP_FACING: "up", DOWN_FACING: "down", LEFT_FACING: "left", RIGHT_FACING: "right"}
    wheels = "; ".join(f"{w.name} {w.wall} read from {w.stand} (piece {w.piece})" for w in floor.wheels)
    actors = []
    for a in floor.actors:
        text = f"{a.name} {a.pos} facing {names[a.facing]}"
        if a.sight:
            text += f", sight {a.sight}" + (f" (card: {a.card_sight})" if a.card_sight != a.sight else "")
        else:
            text += f", talked to from {_front(a)}"
        actors.append(text)
    return f"bg_events on wall tiles: {wheels}. Objects ({len(floor.actors)} of the 15 allowed): " + "; ".join(actors) + "."


def _warps_text(floor: Floor, below: Floor | None, above: Floor | None) -> str:
    """The warps: a warp on every tile of a stair block or mat, left to left and right to right."""
    here = _cell_text(floor.doors)
    down = (f"stairs down {here}: a warp on each to {below.folder} {_cell_text(below.stairs_up)}" if below
            else f"exit mats {here}: a warp on each to Beaconmouth warp 2 (the gym door (32, 30))")
    up = (f"; stairs up {_cell_text(floor.stairs_up)}: a warp on each to {above.folder} {_cell_text(above.doors)}"
          if above else "")
    return f"Warps: {down}{up}."


def _spec_of(floor: Floor, title: str, uses: str, notes: str) -> Spec:
    """The Spec of a floor: the initial grid, with `closed` listing the walkable cells that only the steps make reachable and
    `npc` the spots that can be reached from the door at the start (the rest are proved on the solved grid)."""
    index = FLOORS.index(floor)
    below = FLOORS[index - 1] if index else None
    above = FLOORS[index + 1] if index + 1 < len(FLOORS) else None
    initial, solved = build(floor), build(floor, _all_steps(floor))
    start, end = K.reachable(_spec(floor, initial)), K.reachable(_spec(floor, solved))
    closed = tuple(sorted(c for c in end - start if K.passable(initial[c[1], c[0]])))
    texts = (COMMON_NOTES, _changes_text(floor), _objects_text(floor), _warps_text(floor, below, above), notes)
    return _spec(floor, initial, npc=tuple(c for c in _spots(floor) if c in start), closed=closed, title=title, uses=uses,
                 notes=" ".join(texts))


def gym_1f() -> Spec:
    """Beaconmouth Gym 1F 15 x 21: the Pump Room."""
    return _spec_of(
        FLOOR_1F,
        "Beaconmouth Gym 1F: pump room, three wheels, two islands, stairs up",
        "Beaconmouth_Gym_1F (Gym 9, Water; MIZZLE, TIDE BADGE). Used by that one map only.",
        "The wheels are turned in the card's order Brass, Red, Blue; a wrong wheel floods back to step 0. Keeper's logbook: "
        "a bg_event on (3, 18) (desk 548) read from (3, 17). Gym statues: bg_events on (5, 19) and (8, 19) (buoy 517, which "
        "has MB_TRASH_CAN: the bg_event wins) read from (5, 18) and (8, 18). Corrin and Marlo stand on islands that only "
        "open at steps 1 and 2, so their spots are not in Spec.npc; check_floor proves them on the solved grid. With sight "
        "1 each sees the one cell where a strip meets his island, (7, 14) and (10, 10): the fights are forced and neither "
        "trainer ever stands on a strip (the card's sight 4 would shut the strips). Closed: the gallery, both islands, the "
        "stairs. Look compromises: the wheels are wall fittings, not wheels; the statues are buoys; the sandbars have no "
        "shoreline art.",
    )


def gym_2f() -> Spec:
    """Beaconmouth Gym 2F 15 x 21: the Gallery."""
    return _spec_of(
        FLOOR_2F,
        "Beaconmouth Gym 2F: gallery gantry round a pit with a pump, two wheels, two alcoves",
        "Beaconmouth_Gym_2F (Gym 9, Water). Used by that one map only.",
        "The card's order is reversed on purpose: Blue first (var 3 to 4), then Red (4 to 5); a wrong order floods GA and "
        "GB back. The west catwalk gap (1, 9) and (1, 10) is a visible dead end: water in every state. Ivo and Hobb stand "
        "in one-tile alcoves beside the one-tile walkway and see only the walkway cell next to them, (13, 10) and (10, 3): "
        "they never move, neither can shut the way and neither can be walked round (Hobb faces up; the card's FACE_DOWN "
        "is a slip). The pump is solid: the shipyard boiler, 4 wide (x 6 to 9) where the card has 3. Closed: the upper "
        "walkway, both alcoves, the stairs. Look compromises: as 1F; the gallery is a niche in a three-row wall; mesh "
        "stands in for the steel gantry.",
    )


def gym_3f() -> Spec:
    """Beaconmouth Gym 3F 15 x 19: the Lamp Room."""
    return _spec_of(
        FLOOR_3F,
        "Beaconmouth Gym 3F: lamp room, sand catwalk through a pool, leader's platform",
        "Beaconmouth_Gym_3F (Gym 9, Water; MIZZLE). Used by that one map only.",
        "The lever has no wrong order: it drains the sluice strip once, and the way ends at (8, 4) in front of MIZZLE. The "
        "brass lamp is the 2 x 2 block of portholes at (7, 1) to (8, 2); the four porthole lamps are single tiles. The "
        "entrance corridor is two wide (the card has one) so that both stair tiles have floor above them. Closed: the "
        "platform. Look compromises: the lever is a control panel; the platform is the card's 5 x 3 block, not a cross; "
        "the dark mass behind the pool is black.",
    )


_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Beaconmouth Gym check failed: " + "; ".join(_PROBLEMS))
SPECS = [gym_1f(), gym_2f(), gym_3f()]
