"""Hoarfell Gym (Gym 5, Ice), the one layout of the 'gym_hoarfell' family: an ice hall with a slide puzzle.

The plan is the tile map of design/maps/detail/hoarfell.md section 5 (15 x 23, from the Mahogany Town Gym render): a leader's
dais at the top, an 11-wide field of slick ice with ice boulders and snow patches, a start patch, and an entry carpet with
two statues. The card's coordinates hold: door (7, 22), WAKASAGI (7, 4), goal patch (7, 5), start patch (7, 17), statues
(5, 20) and (9, 20), Fisherman (6, 16), Hiker (5, 15), Lass (3, 16), and the card's 8-move route is still the only
shortest one.

Tilesets: `gTileset_Building` plus `gTileset_Cave`, the pair the card names with the Building primary in place of the
General one. The slide needs the metatile behaviour MB_ICE, and the only MB_ICE metatile with ice art in the compiled
tilesets is Cave 909, the floor of the Shoal Cave ice room (the Mirage Tower set holds an identical copy and nothing else
icy; the Seafoam pair is FRLG and not compiled, and the Sootopolis gym set has only a south-only slide and cracking ice).
Every metatile used here draws with the Cave set's own palette 11 and nothing from the primary's palettes
(`check_palettes` proves it), so the Building primary looks the same as the General one and brings what a gym needs: the
orange exit mat (primary 6 and 7, MB_SOUTH_ARROW_WARP) and the indoor map type.

Where this layout differs from the card (`check_puzzle` proves each change, and shows the card's version failing):
  * Soft-lock. Played as a slide puzzle the card's grid traps the player: the band of ice at the top (y5 to y7) and the
    pocket (11, 9) to (12, 9) have no slide that leads out, and a stop on (3, 7), (4, 5), (8, 7) or (11, 8) lets the player
    slide into them. Nothing gets him out again (no Dig or Escape Rope in a gym). The cell (4, 5) is a snow patch here, not
    ice, which gives the band an exit down column 4.
  * The first fight was meant to be unavoidable, but row 17 let the player step from the carpet onto six other ice cells
    and slide past the Fisherman. Those six cells (x 3, 4, 6, 8, 10 and 11 on y17) are ice boulders here, so the start
    patch (7, 17) is the only way onto the field.
  * The Hiker's sight is 2, not the card's 3. A trainer who notices the player walks up to him and then stays where he
    ended; a Hiker who saw (8, 15) would walk to (7, 15), the only channel between the field and the start patch, and shut
    the player in for good. With sight 2 no trainer can end his walk on a cell that cuts the player off.
  * The exit mat is the tileset's two-tile mat, (7, 22) and (8, 22), as in the Crestfall gym.
  * The card's third wall row and its snow bank (y2 to y4) are the dais: a terrace (y2, y3) and its front face (y4), with
    the notch (7, 4) cut into the face for WAKASAGI. The emblem on the wall at (7, 1) and the Poke Ball statues have no
    art: the wall has no emblem and the statues are piles of ice crystals.

How the pictures are made, so the builder stays free of magic numbers:
  * the frame is the Shoal Cave ice room's: two rows of wall along the top, two columns along each side (dark on the
    left, light and hatched on the right), with a corner piece where they meet;
  * the dais is a snow terrace whose front face is the same wall piece as the top wall;
  * the bottom wall is a snow bank (the piece the Shoal Cave room uses for the edge of a raised floor) with the mat in it;
  * 909 is the only slippery tile. Patches use 655, the single stopper tile of the vanilla ice room.
Run `python3 layoutkit.py fam_gym_hoarfell OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

import itertools
from collections import deque
from collections.abc import Iterable
from typing import NamedTuple

import numpy as np

from layoutkit import F_, W_, Spec
from mrender import TS

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_Cave"

# ---------------------------------------------------------------- metatile ids (secondary index + 512; the mat is primary)
ICE = 909               # slick ice, hatched: MB_ICE, the only tile that slides the player
PATCH = 655             # smooth pale patch, MB_NORMAL: a snow patch where a slide stops
SNOW = 897              # plain frosted snow, MB_CAVE: the carpet, the leader's notch, the terrace
BOULDER = 893           # ice boulder, three chunks: blocks the player and a slide
STATUE = 894            # pile of ice crystals, five chunks: stands in for the card's Poke Ball statues
WALL = 905              # ice wall, scalloped on both edges: the two top rows and the dais front face
CORNER_LEFT = 891       # top left corner of the frame, and where the left column turns into the top rows
CORNER_RIGHT = 892      # the same, mirrored
SIDE_LEFT = 898         # left wall column: dark band, scallops on its right
SIDE_RIGHT = 896        # right wall column: light hatched band, scallops on its left
BANK = 889              # snow bank edge: a light lip on top, plain snow below: the bottom wall
MAT = (6, 7)            # primary tiles: the two halves of the orange exit mat
BLACK = 1               # primary metatile 1, the blank black one: the border around the hall
ID_MASK = 0x03FF        # bits 0-9 of a map block are the metatile id (the top six bits are collision and elevation)
SECONDARY_BASE = 512    # the first secondary metatile id; also the number of primary tiles
TILES_PER_METATILE = 8  # two layers of four tiles
TILE_MASK = 0x03FF      # bits 0-9 of a metatile's tile entry are the tile; bits 12-15 are the palette slot
PALETTE_SHIFT = 12
PRIMARY_PALETTES = 6    # palette slots 0-5 belong to the primary tileset, 6-12 to the secondary

# ---------------------------------------------------------------- the plan (the card's tile map, 15 x 23, with two changes)
# #  frame: top wall (rows 0-1) and side wall columns (x 0-1 and 13-14), placed by `_frame`. Blocked
# t  terrace of the dais (snow), blocked                f  front face of the dais, blocked
# L  WAKASAGI's notch in the face: snow floor, he stands on it
# .  slick ice (slides the player)                      B  ice boulder, blocked
# S  start patch    G  goal patch    s  snow patch: a slide stops on it, a step off it is normal
# c  carpet, snow floor     a  statue, blocked     k  snow bank (bottom wall), blocked     M  exit mat, two tiles
PLAN = (
    "###############",   # y0
    "###############",   # y1
    "##ttttttttttt##",   # y2  the dais terrace
    "##ttttttttttt##",   # y3
    "##fffffLfffff##",   # y4  front face with WAKASAGI's notch (7, 4)
    "##..s.BGB....##",   # y5  G (7, 5) between two boulders; (4, 5) is the escape patch (the card has ice)
    "##.B.B..BB.B.##",   # y6
    "##...........##",   # y7
    "##B..B......B##",   # y8
    "##.....B..B..##",   # y9
    "##.......B.BB##",   # y10
    "##B..BB......##",   # y11
    "##B.........B##",   # y12
    "##B.....B...B##",   # y13
    "##B.s.B.....B##",   # y14
    "##B..s......B##",   # y15 Hiker (5, 15) on the patch
    "##Bs.B.sBs...##",   # y16 Lass (3, 16) on a patch, Fisherman (6, 16) on ice
    "##BBBBBSBBBBB##",   # y17 the start patch (7, 17) is the only gap (the card has ice cells here)
    "##..ccccccc..##",   # y18
    "##..ccccccc..##",   # y19
    "##..cacccac..##",   # y20 statues (5, 20) and (9, 20)
    "##..ccccccc..##",   # y21
    "##kkkkkMMkkkk##",   # y22 snow bank with the exit mat (7, 22) and (8, 22)
)
TOP_WALL_ROWS = 2                  # rows 0-1 are wall
SIDE_WALL_COLUMNS = 2              # wall columns on each side
ICE_CHAR = "."
PATCH_CHARS = "SGs"                # patch cells: a slide stops on them and a step off them is normal
BLOCKED_CHARS = frozenset("#tfBakL")   # the player cannot enter these; the leader's cell is blocked because he stands on it
GATE = ((3, 17), (4, 17), (6, 17), (8, 17), (10, 17), (11, 17))   # boulders the card does not have: they close row 17
ESCAPE_PATCH = (4, 5)              # snow patch the card does not have: it lets the player leave the band at the top

# Object spots from the card (the author places the objects, warps and triggers in Porymap).
LEADER = (7, 4)                    # WAKASAGI, facing down
LEADER_TALK = (7, 5)               # the goal patch: the player talks to him from here
START = (7, 17)                    # the start patch; the carpet cell below it is (7, 18)
DOORS = ((7, 22), (8, 22))         # the exit mat, both cells warp to Hoarfell (card: door (7, 22))
ENTRY = (7, 21)                    # the carpet cell above the mat; the player walks on from here
STATUES = ((5, 20), (9, 20))       # the card's Poke Ball statues, which are piles of ice crystals here
STATUE_VIEW = tuple((x, y + 1) for x, y in STATUES)   # the cell in front of each statue, where its sign is read from
ROUTE = ((7, 16), (7, 10), (2, 10), (2, 9), (6, 9), (6, 6), (7, 6), (7, 5))   # the card's 8 moves, as the stop after each
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
CARD_HIKER_SIGHT = 3               # the Hiker's sight on the card


class Trainer(NamedTuple):
    """A gym trainer: where he stands, which way he faces, how far he sees, and the plan character under him."""
    name: str
    pos: tuple[int, int]
    facing: tuple[int, int]
    sight: int
    standing_on: str


TRAINERS = (
    Trainer("Fisherman", (6, 16), (1, 0), 2, "."),     # a boulder ends his line after (7, 16): the first fight
    Trainer("Hiker", (5, 15), (1, 0), 2, "s"),         # sees (6, 15) and (7, 15); the card's sight 3 adds (8, 15), a trap
    Trainer("Lass", (3, 16), (0, -1), 5, "s"),         # sees the lane (3, 11) to (3, 15)
)


# ---------------------------------------------------------------- builder
def _frame(g: np.ndarray) -> None:
    """The cave wall: two rows along the top and two columns down each side. A corner piece sits at each corner of the
    map and one cell in, where the columns meet the rows; the cell below each outer corner is plain side wall."""
    w = g.shape[1]
    g[:TOP_WALL_ROWS, :] = W_ | WALL
    g[1:, :SIDE_WALL_COLUMNS] = W_ | SIDE_LEFT
    g[1:, w - SIDE_WALL_COLUMNS:] = W_ | SIDE_RIGHT
    g[0, 0] = g[1, 1] = W_ | CORNER_LEFT
    g[0, w - 1] = g[1, w - 2] = W_ | CORNER_RIGHT


def build(plan: tuple[str, ...] = PLAN) -> np.ndarray:
    """The map blocks of `plan`. Nothing in it changes while the game runs: the shipped grid is the only state."""
    g = np.zeros((len(plan), len(plan[0])), np.uint16)
    _frame(g)
    for y, row in enumerate(plan):
        for x, ch in enumerate(row):
            if ch == ICE_CHAR:
                g[y, x] = F_ | ICE
            elif ch in PATCH_CHARS:
                g[y, x] = F_ | PATCH
            elif ch in "cL":
                g[y, x] = F_ | SNOW
            elif ch == "t":
                g[y, x] = W_ | SNOW
            elif ch == "f":
                g[y, x] = W_ | WALL
            elif ch == "B":
                g[y, x] = W_ | BOULDER
            elif ch == "a":
                g[y, x] = W_ | STATUE
            elif ch == "k":
                g[y, x] = W_ | BANK
            elif ch == "M":
                g[y, x] = F_ | MAT[x - plan[y].index("M")]
    return g


def check_palettes() -> list[str]:
    """Problems with the palettes: every secondary metatile of the grid must show pixels in secondary palette slots only,
    so that the Building primary in place of the card's General primary changes nothing on screen."""
    ts = TS(PRIMARY, SECONDARY)
    problems = []
    for mid in sorted({int(v) & ID_MASK for v in build().flatten()} - set(MAT)):
        base = (mid - SECONDARY_BASE) * TILES_PER_METATILE
        for entry in ts.sm[base:base + TILES_PER_METATILE]:
            tile, slot = int(entry) & TILE_MASK, int(entry) >> PALETTE_SHIFT
            pixels = ts.pt[tile] if tile < SECONDARY_BASE else ts.st[tile - SECONDARY_BASE]
            if slot < PRIMARY_PALETTES and pixels.any():
                problems.append(f"metatile {mid} draws with primary palette {slot}")
    return problems


# ---------------------------------------------------------------- the puzzle, proved on the plan
Cell = tuple[int, int]
Path = tuple[Cell, ...]      # the cells one key press passes through; the last is where the player stands still
Graph = dict[Cell, list[Path]]
SEEN = (False, True)         # whether a trainer sees a player who only slides through his line


class Facts(NamedTuple):
    """What the slide puzzle of a plan does."""
    stuck: set[Cell]                          # standing cells with no way back to the carpet
    route: tuple[int, int, list[Cell]]        # start patch to goal: moves, how many shortest routes, one of them
    skippable: dict[str, tuple[bool, bool]]   # trainer -> can the goal be reached without his line, for each of SEEN


def _cells(plan: tuple[str, ...], ch: str) -> list[Cell]:
    """Every cell of the plan holding `ch`, top to bottom and left to right."""
    return [(x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c == ch]


def _blocked(plan: tuple[str, ...], cell: Cell, objects: frozenset[Cell]) -> bool:
    """True where the player cannot step: outside the plan, in a solid cell, or on an object."""
    x, y = cell
    return not (0 <= x < len(plan[0]) and 0 <= y < len(plan)) or plan[y][x] in BLOCKED_CHARS or cell in objects


def _press(plan: tuple[str, ...], cell: Cell, direction: Cell, objects: frozenset[Cell]) -> Path | None:
    """One key press from a standing cell, or None if the first step is blocked. Stepping onto slick ice carries the player
    on in the same direction until the next cell is blocked (the game's MB_ICE slide; an object stops it too); any other
    cell stops him where he steps."""
    path: list[Cell] = []
    x, y = cell
    while not _blocked(plan, (x + direction[0], y + direction[1]), objects):
        x, y = x + direction[0], y + direction[1]
        path.append((x, y))
        if plan[y][x] != ICE_CHAR:
            break
    return tuple(path) or None


def _graph(plan: tuple[str, ...], start: Cell, objects: frozenset[Cell]) -> Graph:
    """Every cell the player can stand still on from `start`, with the paths of the key presses that leave it."""
    graph: Graph = {}
    queue = deque([start])
    while queue:
        cell = queue.popleft()
        if cell in graph:
            continue
        graph[cell] = [p for p in (_press(plan, cell, d, objects) for d in DIRECTIONS) if p]
        queue.extend(p[-1] for p in graph[cell])
    return graph


def _reach(graph: Graph, start: Cell, avoid: frozenset[Cell], passing: bool) -> set[Cell]:
    """Standing cells reachable from `start` without touching `avoid`: with `passing`, a slide that only passes through an
    avoided cell is refused too, otherwise just a stop on one is."""
    seen, queue = {start}, deque([start])
    while queue:
        for path in graph[queue.popleft()]:
            if path[-1] not in seen and not avoid.intersection(path if passing else path[-1:]):
                seen.add(path[-1])
                queue.append(path[-1])
    return seen


def _shortest(graph: Graph, start: Cell, goal: Cell) -> tuple[int, int, list[Cell]]:
    """(moves, how many shortest routes there are, one of them as the stop after each move); (0, 0, []) if unreachable."""
    if start not in graph:
        return 0, 0, []
    moves, count, before = {start: 0}, {start: 1}, {}
    queue = deque([start])
    while queue:
        cell = queue.popleft()
        for target in (p[-1] for p in graph[cell]):
            if target not in moves:
                moves[target], count[target], before[target] = moves[cell] + 1, count[cell], cell
                queue.append(target)
            elif moves[target] == moves[cell] + 1:
                count[target] += count[cell]
    if goal not in moves:
        return 0, 0, []
    route = [goal]
    while route[-1] != start:
        route.append(before[route[-1]])
    return moves[goal], count[goal], route[-2::-1]


def _stuck(graph: Graph, home: Cell) -> set[Cell]:
    """Standing cells from which no sequence of key presses leads back to `home`: a soft-lock, since a gym allows no Dig
    and no Escape Rope."""
    back: dict[Cell, set[Cell]] = {cell: set() for cell in graph}
    for cell, paths in graph.items():
        for path in paths:
            back[path[-1]].add(cell)
    free, queue = {home}, deque([home])
    while queue:
        for cell in back[queue.popleft()] - free:
            free.add(cell)
            queue.append(cell)
    return set(graph) - free


def _sight(plan: tuple[str, ...], trainer: Trainer) -> frozenset[Cell]:
    """The cells a trainer sees: up to `sight` cells along his facing, ending before the first wall or boulder."""
    cells = []
    for step in range(1, trainer.sight + 1):
        cell = (trainer.pos[0] + trainer.facing[0] * step, trainer.pos[1] + trainer.facing[1] * step)
        if _blocked(plan, cell, frozenset()):
            break
        cells.append(cell)
    return frozenset(cells)


def _facts(plan: tuple[str, ...]) -> Facts:
    """Run the slide puzzle of `plan` from the carpet, with the three trainers standing where they stand."""
    graph = _graph(plan, ENTRY, frozenset(t.pos for t in TRAINERS))
    skippable = {t.name: tuple(LEADER_TALK in _reach(graph, ENTRY, _sight(plan, t), passing) for passing in SEEN)
                 for t in TRAINERS}
    return Facts(_stuck(graph, ENTRY), _shortest(graph, START, LEADER_TALK), skippable)


def _approach_traps(plan: tuple[str, ...], trainers: tuple[Trainer, ...]) -> list[str]:
    """Ways a trainer's walk can shut the player in. A trainer who notices the player walks along his line until he stands
    next to him and stays there, so he can end on his own cell or on any cell of his line but the last one he sees. For every
    mix of those end cells, every stop the player can reach must still lead back to the carpet. Returns the first few
    stops that do not, with the end cells that cut them off."""
    start_objects = frozenset(t.pos for t in trainers)
    stops = _graph(plan, ENTRY, start_objects)
    ends = [[(t.pos[0] + t.facing[0] * k, t.pos[1] + t.facing[1] * k) for k in range(len(_sight(plan, t)))] or [t.pos]
            for t in trainers]
    traps = []
    for combo in itertools.product(*ends):
        cut_off = [stop for stop in stops if stop not in combo and ENTRY not in _graph(plan, stop, frozenset(combo))]
        if cut_off:
            traps.append(f"trainers ending on {sorted(combo)} cut off the stops {sorted(cut_off)[:4]}")
    return traps


def _defects(facts: Facts) -> set[str]:
    """The card's two defects a puzzle shows: a soft-lock ('stuck'), and a first fight that can be skipped ('Fisherman')."""
    return ({"stuck"} if facts.stuck else set()) | ({"Fisherman"} if any(facts.skippable["Fisherman"]) else set())


def _card_plan(gate: bool = True, escape: bool = True) -> tuple[str, ...]:
    """The plan as the card draws it: ice where this layout has the gate boulders (`gate`) and the escape patch (`escape`).
    Passing False keeps that change."""
    rows = [list(row) for row in PLAN]
    for x, y in (GATE if gate else ()) + ((ESCAPE_PATCH,) if escape else ()):
        rows[y][x] = ICE_CHAR
    return tuple("".join(row) for row in rows)


def check_puzzle() -> list[str]:
    """Problems with the puzzle of the card; an empty list means it works as designed.
    The plan agrees with the card's object spots and the leader can only be reached from the goal patch; the card's route
    is still the one shortest route from the start patch; no stop is a soft-lock; the Fisherman cannot be avoided, the Lass
    can be skipped, and the Hiker cannot be avoided once a sliding player counts as seen; and the checker still finds the
    card's two defects, with each of the two changes undone alone and together. No trainer's walk to the player can shut him
    in, and the checker still sees the trap in the card's Hiker sight."""
    problems: list[str] = []
    for label, spot, ch in (("WAKASAGI", LEADER, "L"), ("the goal patch", LEADER_TALK, "G"), ("the start patch", START, "S")):
        if _cells(PLAN, ch) != [spot]:
            problems.append(f"{label} should be the one '{ch}' cell, at {spot}")
    problems += [f"the {t.name} {t.pos} should stand on '{t.standing_on}'" for t in TRAINERS
                 if PLAN[t.pos[1]][t.pos[0]] != t.standing_on]
    problems += [f"statue view {c} should be carpet" for c in STATUE_VIEW if PLAN[c[1]][c[0]] != "c"]
    if _cells(PLAN, "M") != sorted(DOORS, key=lambda c: (c[1], c[0])):
        problems.append("the mat cells differ from DOORS")
    if _cells(PLAN, "a") != list(STATUES):
        problems.append(f"the statues are not where the card has them, {STATUES}")
    neighbours = [(LEADER[0] + dx, LEADER[1] + dy) for dx, dy in DIRECTIONS]
    approaches = [c for c in neighbours if not _blocked(PLAN, c, frozenset())]
    if approaches != [LEADER_TALK]:
        problems.append(f"WAKASAGI can be walked up to from {approaches}, not only from the goal patch")
    if any(PLAN[y][x] != "B" for x, y in GATE) or PLAN[ESCAPE_PATCH[1]][ESCAPE_PATCH[0]] != "s":
        problems.append("the gate boulders or the escape patch are not in the plan")
    facts = _facts(PLAN)
    if facts.route != (len(ROUTE), 1, list(ROUTE)):
        problems.append(f"the route from the start patch is {facts.route}; the card has {len(ROUTE)} moves via {list(ROUTE)}")
    if facts.stuck:
        problems.append(f"soft-lock stops (no way back to the carpet): {sorted(facts.stuck)}")
    for name, wanted in (("Fisherman", (False, False)), ("Hiker", (True, False)), ("Lass", (True, True))):
        if facts.skippable[name] != wanted:
            problems.append(f"{name}: goal reachable without his line is {facts.skippable[name]}, expected {wanted}")
    problems += _approach_traps(PLAN, TRAINERS)
    card_trainers = tuple(t._replace(sight=CARD_HIKER_SIGHT) if t.name == "Hiker" else t for t in TRAINERS)
    if not _approach_traps(PLAN, card_trainers):
        problems.append("the checker no longer sees the trap in the card's Hiker sight")
    for label, plan, expected in (("both changes", _card_plan(), {"stuck", "Fisherman"}),
                                  ("the gate", _card_plan(escape=False), {"Fisherman"}),
                                  ("the escape patch", _card_plan(gate=False), {"stuck"})):
        card = _facts(plan)
        if _defects(card) != expected or card.route[:2] != (len(ROUTE), 1):
            problems.append(f"card plan without {label}: found {_defects(card)} and route {card.route[:2]}, "
                            f"expected {expected}")
    return problems


# ---------------------------------------------------------------- the spec
def _spec(grid: np.ndarray, **fields) -> Spec:
    """The Spec of the gym around `grid`, with the layout id, folder, tilesets, door and border fixed."""
    return Spec("LAYOUT_HOARFELL_GYM", "Hoarfell_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, border=(BLACK,) * 4, **fields)


def _cell_list(cells: Iterable[Cell]) -> str:
    """'(3, 4), (5, 6)' for a collection of cells, in reading order."""
    return ", ".join(str(c) for c in sorted(cells, key=lambda c: (c[1], c[0])))


def _moves_named(stops: tuple[Cell, ...]) -> str:
    """'north, west' for the key presses that lead from one stop to the next."""
    names = {(0, -1): "north", (0, 1): "south", (-1, 0): "west", (1, 0): "east"}
    return ", ".join(names[((b[0] > a[0]) - (b[0] < a[0]), (b[1] > a[1]) - (b[1] < a[1]))] for a, b in zip(stops, stops[1:]))


def _notes() -> str:
    """The Spec notes: what the tilesets give, the puzzle, the changes to the card, the objects, and what is left to do."""
    sights = "; ".join(f"{t.name} {t.pos} facing {'east' if t.facing[0] > 0 else 'north'}, sight {t.sight}, sees "
                       f"{_cell_list(_sight(PLAN, t))}" for t in TRAINERS)
    return " ".join((
        "Cave secondary on the Building primary (reason in the module docstring: Cave 909 is the only MB_ICE tile with ice "
        "art, and every tile used draws with Cave palette 11 only, which check_palettes proves). Nothing to set in Porymap "
        "for the slide: 909 already has MB_ICE (it is the vanilla Shoal Cave ice room's floor), the patches (655) are "
        "MB_NORMAL, the mat (primary 6 and 7) is MB_SOUTH_ARROW_WARP, and the colliding pieces are solid in the block word. "
        "Map settings: indoor, MUS_GYM, gym battle scene. The border is primary metatile 1 (black).",
        "Initial state is the only state: no gate, no switch, no setmetatile, and Spec.closed is empty. A player can walk to "
        "every walkable cell, so the puzzle is the slide. check_puzzle models it (a step onto 909 carries on until the next "
        "cell is a wall, a boulder or an object; any other cell stops) and proves on the shipped grid, with the three "
        f"trainers standing where they stand, that the goal patch {LEADER_TALK} is reached from the start patch {START} in "
        f"{len(ROUTE)} moves by one route only, the card's: {_moves_named((START,) + ROUTE)}, stopping on "
        f"{', '.join(str(c) for c in ROUTE)}. From the carpet the player first walks to the start patch. No stop on the "
        "field is a soft-lock: from every stop some sequence of slides leads back to the carpet. "
        f"WAKASAGI {LEADER} faces down, in the notch of the dais face; his only walkable neighbour is {LEADER_TALK}, so the "
        "dais cannot be walked round.",
        f"Changes to the card: the escape patch {ESCAPE_PATCH} (the card has ice there), because the card's grid soft-locks "
        "(see the docstring: the ice band y5 to y7 and the pocket (11, 9) to (12, 9) cannot be left once entered); and six "
        f"gate boulders on y17 at {_cell_list(GATE)} (the card has ice), because the card let the player step off the carpet "
        "onto other ice cells and skip the Fisherman. Both changes leave the card's route the one shortest route; "
        "check_puzzle also runs the card's own grid and finds both defects. The Hiker's sight is "
        f"{TRAINERS[1].sight}, not the card's {CARD_HIKER_SIGHT}: a trainer who notices the player walks up to him and "
        "stays there, and a Hiker who saw (8, 15) would end on (7, 15), the only channel between the field and the carpet, "
        "shutting the player in (check_puzzle tries every mix of end cells and finds none that cuts him off at sight 2; "
        "keep (7, 15) and (7, 16) free of objects and signs). Also: the "
        f"exit mat is two tiles, {DOORS[0]} and {DOORS[1]} (put a warp on each, both to Hoarfell warp 2, arrival (22, 16)); "
        "the dais is a terrace (y2, y3) plus a front face (y4) instead of the card's wall row and snow bank.",
        f"Objects ({len(TRAINERS) + 1} of the 15 allowed): WAKASAGI, then {sights}. The Fisherman's line ends at the boulder "
        "(8, 16). Fights: the engine tests the player's destination tile every frame (trainer_see.c "
        "GetTrainerApproachDistance), so a trainer should also notice a player who slides through his line. If so, the route "
        "forces the Fisherman (the stop (7, 16)) and the Hiker (the slide up column 7 passes (7, 15)), and only the Lass can "
        "be skipped; the checker asserts this reading, and that the Hiker is skippable only if a sliding player is not seen. "
        "Test it in the game; if a slide is not noticed, put a coord_event on (7, 15) to start the Hiker (the Fisherman sees "
        f"the stop, so he is safe). Statues: stand-ins (a pile of ice crystals) at {_cell_list(STATUES)}; put a sign "
        f"bg_event on each, read from {_cell_list(STATUE_VIEW)}. Optional coord_event on the carpet row y18 for the card's "
        "'ICE! WALK ON IT AND YOU GLIDE' hint; the start patch is also the natural place for a thermos line.",
        "Look compromises: a frozen cave, not a building (scalloped ice walls, no emblem on the back wall, a plain snow "
        "carpet instead of the purple one, an orange door mat); the patches are pale (the vanilla ice room uses the same "
        "tile); the statues are the same family as the boulders but stand on the carpet, which no boulder does. The older "
        "'heater tile' idea (gyms.md, the town card) is not in the detail card and is not built: the Cave set has no heater "
        "art (its red lava tiles 863 to 883 are the nearest, and are not used).",
    ))


def hoarfell_gym() -> Spec:
    """Hoarfell Gym 15 x 23; see the module docstring and the notes."""
    return _spec(
        build(),
        npc=(LEADER, LEADER_TALK, START) + tuple(t.pos for t in TRAINERS) + STATUE_VIEW,
        title="Hoarfell Gym: ice hall, slide puzzle, leader's dais",
        uses="Hoarfell Gym (Gym 5, Ice; WAKASAGI, FROST BADGE). Used by that one building only.",
        notes=_notes(),
    )


SPECS = [hoarfell_gym()]
_PROBLEMS = check_palettes() + check_puzzle()
if _PROBLEMS:
    raise ValueError("Hoarfell Gym check failed: " + "; ".join(_PROBLEMS))
