"""Gildhaven Gym 'the Hangar' (Gym 6, Flying), the one layout of the 'gym_gildhaven' family: a wind-tunnel hall.

The plan is the tile map of design/maps/detail/gildhaven.md section 4.3 (15 x 18): TOBIN's platform at the top, three
wind belts (east, west, east) crossing the hall with a two-tile walking strip between them, the entry hall with two
Poke Ball statues at the bottom, the exit mat on the bottom row. Every card coordinate holds: TOBIN (7, 3), the step
down to him (7, 4), trainers (7, 12), (6, 9) and (10, 5), the guide (3, 16), the belts on y 13, 10 and 7 (twelve arrows
and a rest cell, which is x 13 for the two east belts and x 1 for the west belt), the door at (7, 17).

It is built on `gTileset_Building` plus `gTileset_MossdeepGym`, as the card says: grey tile floor, a black void and
orange-and-tan hall walls. The set has clean arrow plates in five colours (blue: east 600, south 601, west 602, north
603) that the vanilla Mossdeep Gym uses as hints beside its warp pads, so they carry no behaviour. The author gives the
two belt arrows their behaviour in Porymap's tileset editor (600 MB_WALK_EAST, 602 MB_WALK_WEST) and no art is drawn.
`gTileset_TrickHousePuzzle` (used by the Smeltham layout) is the alternative whose arrows already move the player, but
it is a green-and-gold wood set with no void and no grey floor.

Changes to the card, all of them small:
  * the card's wall columns (x 0 and x 14) and its blocked corners beside the platform are black void, not wall panels:
    the hall floats in the dark like the vanilla Mossdeep platforms, which gives the card's 'pit-like sky bridge'. They
    are solid, so nothing changes for the player. The back wall (rows 0-1) is the set's cornice over a tan wall face;
  * the bottom row is floor with the exit mat in it, as in the vanilla Mossdeep Gym (the set has no wall piece for a
    one-row front wall); the mat is the set's two-tile one, so both (7, 17) and (8, 17) warp out;
  * each Poke Ball statue is two cells (an orb on a plaque), so its head stands on (5, 14) and (9, 14). The card's hint
    board is a third plaque, a solid cell at (7, 15) read from (7, 16), not a sign on walkable floor at (7, 16) (a
    bg_event sign needs a blocked tile to face);
  * a round landing pad marks the rest cell at the end of each belt, so the player sees where the wind stops, and
    TOBIN stands on one too.
The puzzle has no gate and no switch, so the shipped grid is also the solved grid and no script changes a block.
`check_puzzle` proves the card's rules on it with a belt-aware walk (belts carry the player on until a rest cell).
Run `python3 layoutkit.py fam_gym_gildhaven OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

from collections import deque
from typing import NamedTuple

import numpy as np

from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_MossdeepGym"

# ---------------------------------------------------------------- metatile ids (secondary index + 512; the mat is primary)
VOID = 520                      # black, solid: the backdrop the hall floats in
# Floor shadow, light from the upper left: the set has one floor tile per case of (cell above is solid, cell to the left
# is solid, cell above-left is solid). The table is read off the vanilla Mossdeep Gym, whose floors float in the void.
FLOOR_SHADOW = {
    (False, False, False): 522,   # open on all three sides: plain floor
    (False, False, True): 515,    # only the above-left cell is solid: a corner shadow
    (False, True, False): 540,    # left cell solid, above-left open: a diagonal notch beside a plaque or the void
    (False, True, True): 521,     # shadow along the left edge
    (True, False, False): 548,    # above cell solid, above-left open: a diagonal notch under a wall or the void
    (True, False, True): 514,     # shadow along the top edge
    (True, True, False): 513,     # not in vanilla; the full corner shadow is the nearest
    (True, True, True): 513,      # shadow along the top and the left
}
BELT_EAST, BELT_WEST = 600, 602   # blue arrow plates on white tile; behaviour MB_WALK_EAST / MB_WALK_WEST set in Porymap
LANDING = 549                   # round blue-and-white pad on plain floor, no behaviour: the end of a belt, TOBIN's spot
CORNICE = (525, 526, 527)       # back wall row 0: orange cornice with a gold band: left end, middle, right end
FACE = (533, 534, 535)          # back wall row 1: tan wall face with red posts: left end, middle, right end
BANNER = 532                    # orange framed panel with a gold trim: a banner hung on the wall face
STATUE_HEAD = 516               # orb on a plinth, the top cell of a Poke Ball statue (walkable, drawn over the player)
PLAQUE = 524                    # grey tablet: the foot of a Poke Ball statue, and the free-standing hint board
MAT = (6, 7)                    # primary tiles: the two halves of the orange door mat

# ---------------------------------------------------------------- the plan (the card's tile map, 15 x 18)
# =  back wall (rows 0-1, built by `_back_wall`)       ~  void, solid
# .  floor, walkable                                   > <  wind belt, carries the player east / west (forced walk)
# e w  rest cell where a belt ends, a landing pad      L  TOBIN on his landing pad
# 1 2 3  gym trainers, G  gym guide: objects on floor cells
# h  Poke Ball statue head: walkable, drawn over the player like the vanilla one           M  exit mat, two cells
# p  statue plaque, b  hint board plaque: solid
PLAN = (
    "===============",   # y0  cornice
    "===============",   # y1  wall face, banners
    "~~~.........~~~",   # y2  leader platform, x 3-11
    "~~~....L....~~~",   # y3  TOBIN (7, 3) facing down
    "~~~~~~~.~~~~~~~",   # y4  the step down at (7, 4), the only floor in the gap
    "~.........3...~",   # y5  strip S3, trainer 3 (10, 5)
    "~.............~",   # y6  S3 lower row
    "~>>>>>>>>>>>>e~",   # y7  belt B3: east, rest cell (13, 7)
    "~.............~",   # y8  strip S2
    "~.....2.......~",   # y9  S2 lower row, trainer 2 (6, 9)
    "~w<<<<<<<<<<<<~",   # y10 belt B2: west, rest cell (1, 10)
    "~.............~",   # y11 strip S1
    "~......1......~",   # y12 S1 lower row, trainer 1 (7, 12)
    "~>>>>>>>>>>>>e~",   # y13 belt B1: east, rest cell (13, 13)
    "~....h...h....~",   # y14 entry hall S0, statue heads (5, 14) and (9, 14)
    "~....p.b.p....~",   # y15 statue plaques (5, 15) and (9, 15), the hint board (7, 15)
    "~..G..........~",   # y16 gym guide (3, 16)
    "~......MM.....~",   # y17 exit mat (7, 17) and (8, 17)
)
BACK_WALL_ROWS = 2                 # rows 0-1
PLATFORM_ROWS = range(2, 4)        # TOBIN's platform: he stands on the only way in, (7, 3), so the player never steps on it
BANNER_X = (3, 11)                 # the two banners on the wall face, over the platform's end columns
FLOOR_CHARS = frozenset(".123G")   # plan characters drawn as shadowed floor (the objects stand on them)
PAD_CHARS = frozenset("ewL")       # plan characters drawn as a landing pad
SOLID = frozenset("=~pb")          # plan characters the player cannot enter (the statue head cell is walkable)
BELTS = {">": (1, 0), "<": (-1, 0)}   # plan character -> the step a belt forces

# Object and sign spots from the card (the author places the objects, warps and signs in Porymap).
LEADER = (7, 3)                    # TOBIN, facing down
LEADER_TALK = (7, 4)               # the player talks to him, and he hands over the badge, TM and HM, here
GUIDE = (3, 16)
DOORS = ((7, 17), (8, 17))         # the exit mat; both cells warp to Gildhaven (card: lands on (25, 13))
STATUE_VIEW = ((5, 16), (9, 16))   # the cell in front of each statue plaque, where its sign is read from
BOARD_VIEW = (7, 16)               # the cell the hint board is read from
BELT_RESTS = ((13, 13), (1, 10), (13, 7))   # the rest cell at the end of belt B1, B2 and B3, in the order walked


class Trainer(NamedTuple):
    """A gym trainer: where he stands, which way he faces, how far he sees, and the cells the card says he sees."""
    name: str
    pos: tuple[int, int]
    facing: tuple[int, int]
    sight: int
    sees: tuple[tuple[int, int], ...]


TRAINERS = (
    Trainer("Cooltrainer (Pelipper, Altaria)", (7, 12), (0, -1), 2, ((7, 11), (7, 10))),
    Trainer("Pokemon Ranger (Dodrio, Fearow)", (6, 9), (0, -1), 2, ((6, 8), (6, 7))),
    Trainer("Cooltrainer (Noctowl, Staraptor)", (10, 5), (0, 1), 2, ((10, 6), (10, 7))),
)
OBJECTS = (LEADER, GUIDE) + tuple(t.pos for t in TRAINERS)    # cells an object stands on, so the player cannot enter them
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))                    # the four key presses


# ---------------------------------------------------------------- builder
def _cell(plan: tuple[str, ...], x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan counts as void."""
    return plan[y][x] if 0 <= x < len(plan[0]) and 0 <= y < len(plan) else "~"


def _floor_tile(plan: tuple[str, ...], x: int, y: int) -> int:
    """Floor cell: the shadow variant for the solid cells around it (above, left, above-left)."""
    solid = lambda dx, dy: _cell(plan, x + dx, y + dy) in SOLID
    return FLOOR_SHADOW[(solid(0, -1), solid(-1, 0), solid(-1, -1))]


def _back_wall(g: np.ndarray) -> None:
    """Rows 0-1: the orange cornice over the tan wall face, a banner over each end column of the platform."""
    for row, (left, middle, right) in enumerate((CORNICE, FACE)):
        g[row, :] = W_ | middle
        g[row, 0] = W_ | left
        g[row, -1] = W_ | right
    for x in BANNER_X:
        g[1, x] = W_ | BANNER


def build(plan: tuple[str, ...] = PLAN) -> np.ndarray:
    """The map blocks of `plan`. Floor cells take their shadow from the solid cells around them; the void, plaques and the
    back wall are solid; belts, landing pads, the statue heads and the mat are walkable pieces of their own."""
    g = np.zeros((len(plan), len(plan[0])), np.uint16)
    _back_wall(g)
    for y in range(BACK_WALL_ROWS, len(plan)):
        for x, ch in enumerate(plan[y]):
            if ch in FLOOR_CHARS:
                g[y, x] = F_ | _floor_tile(plan, x, y)
            elif ch == "~":
                g[y, x] = W_ | VOID
            elif ch in "pb":
                g[y, x] = W_ | PLAQUE
            elif ch == "h":
                g[y, x] = F_ | STATUE_HEAD
            elif ch in PAD_CHARS:
                g[y, x] = F_ | LANDING
            elif ch == ">":
                g[y, x] = F_ | BELT_EAST
            elif ch == "<":
                g[y, x] = F_ | BELT_WEST
            elif ch == "M":
                g[y, x] = F_ | MAT[x - plan[y].index("M")]
    return g


# ---------------------------------------------------------------- the puzzle, proved on the plan
def _blocked(plan: tuple[str, ...], objects: tuple[tuple[int, int], ...], x: int, y: int) -> bool:
    """True where the player cannot step: walls, the void, plaques and the cells objects stand on."""
    return _cell(plan, x, y) in SOLID or (x, y) in objects


def _press(plan: tuple[str, ...], objects: tuple[tuple[int, int], ...], cell: tuple[int, int],
           step: tuple[int, int]) -> tuple[tuple[int, int], tuple[tuple[int, int], ...]] | None:
    """One key press on `cell`: (the cell the player stands still on, every cell he entered on the way), or None if the
    first cell is blocked. Stepping onto a belt carries him on along it until a cell that is not a belt, or until the
    next cell is blocked (the engine then stops the forced walk and gives the player his keys back)."""
    x, y = cell[0] + step[0], cell[1] + step[1]
    if _blocked(plan, objects, x, y):
        return None
    entered = [(x, y)]
    while _cell(plan, x, y) in BELTS:
        bx, by = BELTS[plan[y][x]]
        if _blocked(plan, objects, x + bx, y + by):
            break
        x, y = x + bx, y + by
        entered.append((x, y))
    return (x, y), tuple(entered)


def _stops(plan: tuple[str, ...], objects: tuple[tuple[int, int], ...] = OBJECTS,
           avoid: frozenset[tuple[int, int]] = frozenset()) -> dict[tuple[int, int], set[tuple[int, int]]]:
    """Every cell the player can stand still on when he walks in through the door, with the cells one key press leads to.
    A press that enters a cell of `avoid` (a cell a trainer sees: the fight would start there) is not followed."""
    edges: dict[tuple[int, int], set[tuple[int, int]]] = {}
    queue = deque([DOORS[0]])
    while queue:
        cell = queue.popleft()
        if cell in edges:
            continue
        edges[cell] = set()
        for step in STEPS:
            move = _press(plan, objects, cell, step)
            if move is not None and not avoid.intersection(move[1]):
                edges[cell].add(move[0])
                queue.append(move[0])
    return edges


def _stuck(edges: dict[tuple[int, int], set[tuple[int, int]]]) -> set[tuple[int, int]]:
    """Cells the player can stand on but cannot leave for the door again (a soft-lock)."""
    back: dict[tuple[int, int], set[tuple[int, int]]] = {cell: set() for cell in edges}
    for cell, targets in edges.items():
        for target in targets:
            back[target].add(cell)
    free, queue = {DOORS[0]}, deque([DOORS[0]])
    while queue:
        for prev in back[queue.popleft()] - free:
            free.add(prev)
            queue.append(prev)
    return set(edges) - free


def _sight(plan: tuple[str, ...], trainer: Trainer) -> tuple[tuple[int, int], ...]:
    """The cells `trainer` sees: in a straight line from him, up to his sight range, stopping at the first blocked cell."""
    seen = []
    for dist in range(1, trainer.sight + 1):
        x, y = trainer.pos[0] + trainer.facing[0] * dist, trainer.pos[1] + trainer.facing[1] * dist
        if _blocked(plan, (), x, y):
            break
        seen.append((x, y))
    return tuple(seen)


def _with_cell(plan: tuple[str, ...], cell: tuple[int, int], ch: str) -> tuple[str, ...]:
    """The plan with one cell replaced."""
    x, y = cell
    return plan[:y] + (plan[y][:x] + ch + plan[y][x + 1:],) + plan[y + 1:]


def _cells(plan: tuple[str, ...], chars: str) -> list[tuple[int, int]]:
    """Every cell of the plan holding one of `chars`, top to bottom and left to right."""
    return [(x, y) for y, row in enumerate(plan) for x, c in enumerate(row) if c in chars]


def check_puzzle() -> list[str]:
    """Problems with the card's puzzle; an empty list means it works as designed.
    The plan agrees with the card's object spots; the walk from the door reaches TOBIN and every rest cell and every
    walkable cell that is not a belt (TOBIN's platform apart, which he blocks); every belt ride ends on a rest cell; no
    cell is a soft-lock (the return trip works); each trainer sees exactly the cells the card says, and walling those off cuts TOBIN off (each fight is unavoidable,
    the belt cells included: src/trainer_see.c tests the player's destination cell every frame, on forced steps too);
    the strips stay passable wherever a trainer ends up after walking up to the player; the checker itself sees a belt that
    runs into a wall."""
    problems: list[str] = []
    marks = {"L": [LEADER], "G": [GUIDE], "1": [TRAINERS[0].pos], "2": [TRAINERS[1].pos], "3": [TRAINERS[2].pos],
             "M": sorted(DOORS, key=lambda p: (p[1], p[0])), "e": [BELT_RESTS[0], BELT_RESTS[2]], "w": [BELT_RESTS[1]]}
    for ch, spots in marks.items():
        if _cells(PLAN, ch) != sorted(spots, key=lambda p: (p[1], p[0])):
            problems.append(f"plan '{ch}' cells {_cells(PLAN, ch)} differ from the card's {spots}")
    problems += [f"{spot} should be plain floor"
                 for spot in STATUE_VIEW + (BOARD_VIEW, LEADER_TALK) if _cell(PLAN, *spot) != "."]
    edges = _stops(PLAN)
    for spot in (LEADER_TALK,) + BELT_RESTS + STATUE_VIEW + (BOARD_VIEW,):
        if spot not in edges:
            problems.append(f"{spot} cannot be reached from the door")
    if not any(near in edges for near in ((GUIDE[0] + dx, GUIDE[1] + dy) for dx, dy in STEPS)):
        problems.append(f"nobody can stand next to the guide {GUIDE}")
    belts = [cell for cell in edges if _cell(PLAN, *cell) in BELTS]
    if belts:
        problems.append(f"a belt ride ends on a belt cell (the wind runs into a wall): {sorted(belts)}")
    idle = [c for c in _cells(PLAN, ".123Gh") + _cells(PLAN, "ewL") + list(DOORS)
            if c not in edges and c not in OBJECTS and c[1] not in PLATFORM_ROWS]
    if idle:
        problems.append(f"walkable cells the player can never stand on: {idle}")
    if _stuck(edges):
        problems.append(f"soft-lock cells (the player cannot leave them): {sorted(_stuck(edges))}")
    for t in TRAINERS:
        if _sight(PLAN, t) != t.sees:
            problems.append(f"the {t.name} sees {_sight(PLAN, t)}, the card says {t.sees}")
        if LEADER_TALK in _stops(PLAN, avoid=frozenset(t.sees)):
            problems.append(f"TOBIN can be reached without fighting the {t.name}")
        for dist in range(t.sight):          # he may end up on any cell between his post and the player
            rest = (t.pos[0] + t.facing[0] * dist, t.pos[1] + t.facing[1] * dist)
            moved = tuple(rest if pos == t.pos else pos for pos in OBJECTS)
            if _cell(PLAN, *rest) in BELTS or LEADER_TALK not in _stops(PLAN, moved) or _stuck(_stops(PLAN, moved)):
                problems.append(f"the {t.name} on {rest} after his walk blocks the hall or a belt")
    broken = _with_cell(PLAN, BELT_RESTS[1], "<")          # the west belt's rest cell made a belt: it now runs into the void
    if not [cell for cell in _stops(broken) if _cell(broken, *cell) in BELTS]:
        problems.append("the checker no longer sees a belt that runs into a wall")
    return problems


# ---------------------------------------------------------------- the spec
def gildhaven_gym() -> Spec:
    """Gildhaven Gym 15 x 18; see the module docstring and the notes below."""
    return Spec(
        "LAYOUT_GILDHAVEN_GYM", "Gildhaven_Gym", build(), PRIMARY, SECONDARY,
        doors=DOORS,
        npc=(LEADER, LEADER_TALK, GUIDE) + tuple(t.pos for t in TRAINERS) + STATUE_VIEW + (BOARD_VIEW,),
        title="Gildhaven Gym 'the Hangar': three wind belts across a hall, leader's platform",
        uses="Gildhaven Gym (Gym 6, Flying; TOBIN, FEATHER BADGE). Used by that one building only.",
        notes=(
            "Mossdeep Gym secondary on the Building primary, as the card says. THE ONE PORYMAP STEP: in the tileset editor of "
            "gTileset_MossdeepGym give metatile 600 (0x258, blue east arrow) the behaviour MB_WALK_EAST and 602 (0x25A, blue west "
            "arrow) MB_WALK_WEST (MB_SLIDE_EAST / MB_SLIDE_WEST are the faster wind); without it the belts are plain floor. The "
            "engine lets forced movement override the keys (src/field_player_avatar.c, TryDoMetatileBehaviorForcedMovement), so "
            "the player cannot steer on a belt. Log the edit in design/engine-edits.md; the vanilla Mossdeep Gym uses the same "
            "two arrows as hints but is not reachable in Veldris. Belts: B3 y 7 x 1-12 east, B2 y 10 x 2-13 west, B1 y 13 x 1-12 "
            "east; rest cells (13, 7), (1, 10), (13, 13) are landing pads (549, no behaviour; never use 528-531, those are the "
            "Mossdeep warp pads, behaviour 14). No gate and no switch: the shipped grid is the solved grid, no script calls "
            "setmetatile and Spec.closed is empty. TOBIN's platform (x 3-11, y 2-3) is floor but he stands on its only way in "
            "(7, 3), so the player never steps on it (if a script walks TOBIN aside it is plain floor). Objects, 5 of 15: TOBIN "
            "(7, 3) facing down, talk from (7, 4), pad under him; trainer 1 Cooltrainer (7, 12) facing north, sight 2, sees (7, 11) "
            "and the belt cell (7, 10); trainer 2 Pokemon Ranger (6, 9) facing north, sight 2, sees (6, 8) and the belt cell (6, 7); "
            "trainer 3 Cooltrainer (10, 5) facing south, sight 2, sees (10, 6) and the belt cell (10, 7); the guide (3, 16). "
            "check_puzzle proves each fight is unavoidable (walling off a trainer's sight cuts TOBIN off), that every belt ride ends "
            "on a rest cell, that the return trip works from every cell (south onto a belt, then south off its rest cell), and that "
            "the 2-tall strips stay passable wherever a trainer ends after walking up to the player. src/trainer_see.c tests the "
            "player's destination cell every frame, forced steps included, so trainers 1 and 2 do see the belt cells; confirm it in "
            "the emulator, and if a fight is missed put a coord_event on that belt cell. Signs (bg_events): the statue plaques (5, 15) "
            "and (9, 15), read from (5, 16) and (9, 16) facing north (the card's Poke Ball statues, the head is the walkable cell "
            "above); the hint board is the lone plaque (7, 15), read from (7, 16), 'Stand still. The wind will do the talking.' "
            "(the card put it on walkable (7, 16)). Warp: the mat is two cells, (7, 17) and (8, 17), both to Gildhaven; allow_escaping "
            "true on the map (card). Look compromises: the hall is orange and tan, not the card's blue-grey (a palette edit in "
            "Porymap does it, nothing else changes); the set has no window piece, so two framed panels (532) hang as banners at "
            "(3, 1) and (11, 1); the wind is drawn as arrow plates, not streaks; the void is flat black with no cliff edge; the "
            "set's blue dais does not centre on an odd-width map, so TOBIN stands on a landing pad instead of a stage."
        ),
    )


SPECS = [gildhaven_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Gildhaven Gym puzzle check failed: " + "; ".join(_PROBLEMS))
