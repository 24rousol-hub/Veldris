"""Gloomsby Gym (Gym 3, Ghost), the one layout of the 'gym_gloomsby' family: a dark hall with a black pit in the middle.

The plan is the card of design/maps/detail/gloomsby.md section 5 (traced from the Ecruteak City Gym render): a leader's
hall at the top between two ghost statues, a landing with three doorways, a tall black pit crossed by a zig-zag of
stepping stones with a rail down both sides and a dead-end pocket behind each rail, a south hall with two Poke Ball
statues, and the door mat. It is built on `gTileset_Building` plus `gTileset_DewfordGym`, as the card says. The tile
rules are read off the vanilla Dewford Gym (LAYOUT_DEWFORD_TOWN_GYM), the one built gym on this tileset: solid ground is
brown wood with a grey lip, a wall is a cornice row over a teal face row, and the floor carries a shadow cast by the wall
face above it and by the solid cell to its left (light from the upper left). Every table entry occurs in that gym except
the three marked 'not in vanilla' (four cells).

Where this layout differs from the card (each difference is forced by the tileset's art):
  * 15 x 24, one row taller than the card's 15 x 23. A Dewford wall is two rows (cornice and face), so the bottom wall
    takes the card's last walkway row and one is added above it; every other row below the hall keeps its card y.
  * The wall between the hall and the landing is two rows (y5, y6) instead of one, so the hall has two rows (y3, y4).
    Its three doorways are two cells deep and sit at x 4, 7 and 10 (card 5, 7, 9): the tileset has no one-tile-wide wall
    piece, so the posts between doorways must be two tiles wide. The real doorway is the right one, x 10.
  * The landing is x 4 to 10 (card 5 to 9), because of the doorway move. The door mat is two tiles wide, (6, 23) and
    (7, 23): the tileset's mat is one picture in two tiles (the card's (7, 22) becomes (7, 23)).
  * The pockets are x 2 to 3, y 8 to 14, closed at the bottom by the wall. The card's text says y 8 to 15, but its
    drawing leaves them open to the south hall at y16, which would let the player skip the pit: the drawing is wrong.
  * The pit is the tileset's blank black metatile (the card asked for a black block) and the stones are plain floor.
    The rails are brown posts with a grey lip on both sides. The tileset has no ghost statue: the lone skull plaque is
    the ghost statue (and the gravestone), and a plaque under an orb is the Poke Ball statue (the vanilla pair).

Initial state is the only state: no block ever changes. The darkness is `setflashlevel` in the map script and the fake
doors are coord events on walkable doorway cells, so there is nothing to solve in the grid itself. `check_puzzle` proves
on the shipped grid that the stones are the only way to the landing, that the Psychic's stone cannot be passed, that the
pockets are dead ends, and that every spot the card names is reachable.

Run `python3 layoutkit.py fam_gym_gloomsby OUT_DIR` from this folder to lint and draw it.
"""
from __future__ import annotations

import numpy as np

import layoutkit as K
from layoutkit import F_, W_, Spec

PRIMARY, SECONDARY = "gTileset_Building", "gTileset_DewfordGym"

# ---------------------------------------------------------------- metatile ids (secondary index + 512; the mat is primary)
VOID = 512                  # blank metatile: shows the black backdrop. The pit
FLOOR = 528                 # plain olive floor, no shadow
FLOOR_CORNER = 515          # shadow in the top-left corner only (the cell above-left is solid)
FLOOR_LEFT = 521            # shadow along the left edge
FLOOR_LEFT_FADE = 522       # shadow along the left edge, thinning out upwards
FLOOR_TOP = 514             # shadow along the top
FLOOR_TOP_FADE = 523        # shadow along the top, thinning out to the left
FLOOR_TOP_LEFT = 513        # shadow along the top and the left
# Floor with a grey lip bar along its bottom over a brown strip: a floor cell above solid ground. A cap is the short
# vertical piece where the lip turns down, at the end of a bar that has floor to the south on that side.
LIP = 538                   # no shadow, the bar runs on to both sides
LIP_CAP_LEFT = 534
LIP_CAP_RIGHT = 533
LIP_CORNER = 530            # corner shadow, the bar runs on
LIP_CORNER_CAP_LEFT = 536
LIP_TOP_FADE = 518          # top shadow thinning out to the left, the bar runs on
LIP_TOP_FADE_CAP_LEFT = 517
LIP_TOP = 546               # top shadow, the bar runs on
LIP_TOP_CAP_LEFT = 529
LIP_TOP_CAP_RIGHT = 531
# Solid ground: brown wood mass. The lip is drawn on each side that faces floor, the pit or a wall face.
MASS = 520                  # wood, no lip
MASS_LIP_LEFT = 527         # lip on the left, floor carries on to the south-west
MASS_LIP_LEFT_UNDER = 535   # lip on the left, solid ground to the south-west (the floor cell there has its own lip)
MASS_LIP_RIGHT = 524
MASS_LIP_RIGHT_UNDER = 532
MASS_LIP_LEFT_CORNICE = 519     # lip on the left where a cornice joins from the left
MASS_LIP_RIGHT_CORNICE = 516    # lip on the right where a cornice joins from the right
POST = 553                  # one tile wide: lip on both sides
EDGE_TOP = (568, 569, 570)  # top edge of the map: left corner, middle, right corner
# Walls: a cornice (wood top, lip, stripes) over a teal face; end tiles close a run that has floor beside it.
CORNICE = (542, 540, 541)   # left end, middle, right end
FACE = (550, 548, 549)
CORNICE_NOTCH = (571, 572)  # cornice pair over the emblem
EMBLEM = (579, 580)         # blue orb emblem on the face, 2 wide
STATUE_PLAQUE = 551         # grey tablet with a skull: the ghost statue, and the plinth of the Poke Ball statue
STATUE_HEAD = 543           # orb on a plinth: the head of the Poke Ball statue, on the floor cell above the plaque
MAT = (6, 7)                # primary tiles: the two halves of the orange door mat

# ---------------------------------------------------------------- the plan (15 x 24)
# #  solid ground (frame, blocks, rails)      ~  the pit (black, solid)
# .  floor                                    o  stepping stone: plain floor in the pit, and the two rail gaps
# c  cornice (wall top, solid)                t  teal wall face (solid)
# S  skull plaque (solid): a ghost statue, a gravestone or the plinth of a Poke Ball statue
# h  orb head of a Poke Ball statue (solid)   m  door mat (walkable), two tiles
PLAN = (
    "###############",   # y0  top edge
    "##ccccccccccc##",   # y1  cornice; the two emblems sit over x 5-6 and x 8-9
    "##ttttttttttt##",   # y2  teal face
    "##...S...S...##",   # y3  leader's row: ghost statues at (5, 3) and (9, 3), SANZUFORD at (7, 3)
    "##...........##",   # y4  walkway: the leader is talked to from (7, 4)
    "####.cc.cc.####",   # y5  doorways at x 4, 7, 10; posts at x 5-6 and 8-9; solid ground over the side blocks
    "##cc.tt.tt.cc##",   # y6
    "##tt.......tt##",   # y7  the landing, x 4 to 10
    "##..#o~~~~#..##",   # y8  pit rows y8-y14, rails at x 4 and 10, pockets at x 2-3 and 11-12
    "##S.#o~~~~#.S##",   # y9  gravestones at (2, 9) and (12, 9)
    "##..#ooooo#..##",   # y10 the Psychic stands on (7, 10)
    "##..#~~~~oo..##",   # y11 right rail gap (10, 11)
    "##..ooo~oo#..##",   # y12 left rail gap (4, 12)
    "##..#~o~o~#..##",   # y13
    "##..#~ooo~#..##",   # y14
    "##ccccc.ccccc##",   # y15 front wall of the pit and the pockets, one gap at x 7
    "##ttttt.ttttt##",   # y16
    "##...........##",   # y17 south hall; the stones start at (7, 16) above (7, 17)
    "##...........##",   # y18 the Hex Maniac stands on (3, 18)
    "##...h...h...##",   # y19 Poke Ball statue heads
    "##...S...S...##",   # y20 plaques at (5, 20) and (9, 20)
    "##...........##",   # y21
    "cccccc..ccccccc",   # y22 bottom wall, gap over the mat
    "ttttttmmttttttt",   # y23 the mat at (6, 23) and (7, 23)
)
WIDTH, HEIGHT = len(PLAN[0]), len(PLAN)
OUTSIDE = "O"               # what a lookup outside the plan reads as: the map edge acts like open air beside a lip or a wall end
OPEN = ".ohm"               # cells that act as floor for shadows, lip caps and wall ends (statue heads and the mat included)
LIP_OVER = "#~c"            # a floor cell above one of these carries a lip bar
LIP_FACING = ".ohmS~tO"     # solid ground draws a lip on a side that faces any of these (a plaque stands on floor)
EDGE_ROW = 0
EMBLEM_X = (5, 8)           # left cell of each emblem, either side of the leader's column
NOTCH_ROW, FACE_ROW = 1, 2

# Object spots (the author places the objects in Porymap).
LEADER = (7, 3)                         # SANZUFORD, facing south
LEADER_TALK = (7, 4)
DOORWAYS = (4, 7, 10)                   # x of the three doorways, each two cells deep; the real one is the last
FAKE_DOORS, REAL_DOOR = DOORWAYS[:-1], DOORWAYS[-1]
DOORWAY_ROWS = (5, 6)                   # a doorway's two cells; the landing is the row below
LANDING_ROW = 7
FAKE_DOOR_TRIGGERS = tuple((x, DOORWAY_ROWS[1]) for x in FAKE_DOORS)   # the cell the player enters from the landing
LOOP_BACK = (7, 21)                     # a fake door puts the player here, at the start of the south hall (as the card)
LIGHT = (11, 4)                         # pool of light by the real doorway's exit (the card: (10, 5))
HEX_MANIAC = (3, 18)                    # faces east, sight 5: sees (4..8, 18)
PSYCHIC = (7, 10)                       # faces east, sight 3: sees (8, 10) and (9, 10); the rail at (10, 10) ends the sight
HEX_SIGHT, PSYCHIC_SIGHT = 5, 3
STATUE_FRONTS = ((5, 4), (9, 4), (5, 21), (9, 21))   # cells in front of the four statue plaques
GRAVESTONE_FRONTS = ((2, 10), (12, 10))              # the pocket signs are read from here (gravestones at (2, 9), (12, 9))
PIT_ENTRY = (7, 17)                     # the south hall cell under the first stone (7, 16)
STONE_GAPS = ((4, 12), (10, 11))        # rail gaps that open the pockets
POCKET_FLOORS = ((2, 8), (12, 8))       # the far corners of the two pockets
DOORS = ((6, 23), (7, 23))


# ---------------------------------------------------------------- shadow and lip rules
# A shadow case is (top, left, corner): the cell above is a wall face, the cell to the left is not floor, the cell
# above-left is not floor.
PLAIN_FLOOR = {
    (0, 0, 0): FLOOR, (0, 0, 1): FLOOR_CORNER, (0, 1, 0): FLOOR_LEFT_FADE, (0, 1, 1): FLOOR_LEFT,
    (1, 0, 0): FLOOR_TOP_FADE, (1, 0, 1): FLOOR_TOP, (1, 1, 1): FLOOR_TOP_LEFT,
    (1, 1, 0): FLOOR_TOP_LEFT,                      # not in vanilla: the nearest shadow
}
# Lip floor: shadow case, then (floor to the south-west, floor to the south-east) -> tile.
LIP_FLOOR = {
    (0, 0, 0): {(0, 0): LIP, (1, 0): LIP_CAP_LEFT, (0, 1): LIP_CAP_RIGHT},
    (0, 0, 1): {(0, 0): LIP_CORNER, (1, 0): LIP_CORNER_CAP_LEFT,
                (0, 1): LIP_CAP_RIGHT},             # not in vanilla: the cap is kept, the corner shadow is lost
    (0, 1, 1): {(0, 0): LIP_CORNER,
                (1, 1): LIP_CORNER},                # not in vanilla: floor on both sides of a one-tile post
    (1, 0, 0): {(0, 0): LIP_TOP_FADE, (1, 0): LIP_TOP_FADE_CAP_LEFT},
    (1, 0, 1): {(0, 0): LIP_TOP, (1, 0): LIP_TOP_CAP_LEFT, (0, 1): LIP_TOP_CAP_RIGHT},
    (1, 1, 1): {(0, 0): LIP_TOP},
}


# ---------------------------------------------------------------- builder
def _at(x: int, y: int) -> str:
    """The plan character at (x, y); anything outside the plan reads as `OUTSIDE`."""
    return PLAN[y][x] if 0 <= x < WIDTH and 0 <= y < HEIGHT else OUTSIDE


def _floor_tile(x: int, y: int) -> int:
    """Floor cell: the shadow from the wall face above and the solid cells to the left, and a lip bar when solid
    ground (or the pit, or a cornice) lies below, capped at either end that has floor to the south."""
    shadow = (int(_at(x, y - 1) == "t"), int(_at(x - 1, y) not in OPEN), int(_at(x - 1, y - 1) not in OPEN))
    if _at(x, y + 1) in LIP_OVER:
        caps = (int(_at(x - 1, y + 1) in OPEN), int(_at(x + 1, y + 1) in OPEN))
        return LIP_FLOOR[shadow][caps]
    return PLAIN_FLOOR[shadow]


def _mass_tile(x: int, y: int) -> int:
    """Solid ground: a lip on each side that faces floor, the pit or a wall face; both sides make a post. The lip turns
    under when solid ground lies to the south on that side. A cornice on one side has its own lip tile."""
    left, right = _at(x - 1, y), _at(x + 1, y)
    if left in LIP_FACING and right in LIP_FACING:
        return POST
    if left in LIP_FACING:
        return MASS_LIP_LEFT if _at(x - 1, y + 1) in LIP_FACING else MASS_LIP_LEFT_UNDER
    if right in LIP_FACING:
        return MASS_LIP_RIGHT if _at(x + 1, y + 1) in LIP_FACING else MASS_LIP_RIGHT_UNDER
    if left == "c":
        return MASS_LIP_LEFT_CORNICE
    if right == "c":
        return MASS_LIP_RIGHT_CORNICE
    return MASS


def _wall_tile(x: int, y: int, ends: tuple[int, int, int]) -> int:
    """Cornice or face cell: an end tile on a side that has floor (or the map edge) beside it, else the middle tile."""
    open_left = _at(x - 1, y) in OPEN or _at(x - 1, y) == OUTSIDE
    open_right = _at(x + 1, y) in OPEN or _at(x + 1, y) == OUTSIDE
    return ends[0] if open_left else ends[2] if open_right else ends[1]


def build() -> np.ndarray:
    """The map blocks of `PLAN`: the pit, walls and solid ground solid; floor, stones and the mat walkable. The top row
    takes the edge tiles and the two emblems replace the wall cells at `EMBLEM_X`."""
    g = np.zeros((HEIGHT, WIDTH), np.uint16)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            ch = PLAN[y][x]
            if ch == "#":
                g[y, x] = W_ | _mass_tile(x, y)
            elif ch == "~":
                g[y, x] = W_ | VOID
            elif ch == ".":
                g[y, x] = F_ | _floor_tile(x, y)
            elif ch == "o":
                g[y, x] = F_ | FLOOR
            elif ch == "c":
                g[y, x] = W_ | _wall_tile(x, y, CORNICE)
            elif ch == "t":
                g[y, x] = W_ | _wall_tile(x, y, FACE)
            elif ch == "S":
                g[y, x] = W_ | STATUE_PLAQUE
            elif ch == "h":
                g[y, x] = W_ | STATUE_HEAD
            elif ch == "m":
                g[y, x] = F_ | MAT[x - PLAN[y].index("m")]
    g[EDGE_ROW, :] = W_ | EDGE_TOP[1]
    g[EDGE_ROW, 0] = W_ | EDGE_TOP[0]
    g[EDGE_ROW, WIDTH - 1] = W_ | EDGE_TOP[2]
    for left in EMBLEM_X:
        for dx in (0, 1):
            g[NOTCH_ROW, left + dx] = W_ | CORNICE_NOTCH[dx]
            g[FACE_ROW, left + dx] = W_ | EMBLEM[dx]
    return g


GRID = build()
OBJECT_SPOTS = (LEADER, LEADER_TALK, HEX_MANIAC, PSYCHIC, LIGHT) + STATUE_FRONTS + GRAVESTONE_FRONTS


def _spec(grid: np.ndarray, **fields) -> Spec:
    return Spec("LAYOUT_GLOOMSBY_GYM", "Gloomsby_Gym", grid, PRIMARY, SECONDARY, doors=DOORS, **fields)


# ---------------------------------------------------------------- the puzzle, proved on the shipped grid
def _reach(blocked: tuple = ()) -> set[tuple[int, int]]:
    """Cells reachable from the door when the listed cells are made solid (a trainer standing in the way, say)."""
    grid = GRID.copy()
    for x, y in blocked:
        grid[y, x] |= W_
    return K.reachable(_spec(grid))


def _sight(start: tuple[int, int], length: int) -> list[tuple[int, int]]:
    """The cells a trainer at `start` looking east sees: up to `length` of them, ending before the first solid cell."""
    seen = []
    for dx in range(1, length + 1):
        if not K.passable(GRID[start[1], start[0] + dx]):
            break
        seen.append((start[0] + dx, start[1]))
    return seen


def check_puzzle() -> list[str]:
    """Problems with the gym as the card describes it; an empty list means the layout works as designed.
    No block changes in this gym, so the shipped grid is also the solved grid and must lint clean with every object spot
    reserved. The Psychic's stone is the only way to the landing; the rail gaps are the only way into the pockets; each
    doorway joins the landing to the hall; the loop-back cell is reachable; each trainer sees the player's way in."""
    problems: list[str] = []
    reached = _reach()
    wanted = OBJECT_SPOTS + POCKET_FLOORS + (LOOP_BACK, PIT_ENTRY) + FAKE_DOOR_TRIGGERS + ((REAL_DOOR, DOORWAY_ROWS[0]),)
    problems += [f"{c} should be reachable" for c in wanted if c not in reached]
    behind_psychic = _reach((PSYCHIC,))
    cut_off = (LEADER_TALK, (DOORWAYS[0], LANDING_ROW), (REAL_DOOR, LANDING_ROW))
    problems += [f"{c} should be cut off by the Psychic on {PSYCHIC}" for c in cut_off if c in behind_psychic]
    sealed = _reach(STONE_GAPS)
    problems += [f"pocket cell {c} should only open through the rail gaps" for c in POCKET_FLOORS if c in sealed]
    for x in DOORWAYS:
        column = [(x, y) for y in (DOORWAY_ROWS[0] - 1,) + DOORWAY_ROWS + (LANDING_ROW,)]   # walkway, doorway, landing
        problems += [f"doorway column x {x}: {c} is not walkable" for c in column if not K.passable(GRID[c[1], c[0]])]
    hex_sees = {x for x, _ in _sight(HEX_MANIAC, HEX_SIGHT)}
    problems += [f"the Hex Maniac cannot see the mat's column x {x}" for x, _ in DOORS if x not in hex_sees]
    psychic_sees = _sight(PSYCHIC, PSYCHIC_SIGHT)
    if psychic_sees != [(PSYCHIC[0] + 1, PSYCHIC[1]), (PSYCHIC[0] + 2, PSYCHIC[1])]:
        problems.append(f"the Psychic should see the two stones east of him and stop at the rail, sees {psychic_sees}")
    errors, warnings = K.lint(_spec(GRID, npc=OBJECT_SPOTS))
    problems += [f"grid: {m}" for m in errors + warnings]
    return problems


def gloomsby_gym() -> Spec:
    """Gloomsby Gym 15 x 24; see the module docstring, the tables above and the notes below."""
    triggers = " and ".join(f"({x}, {y})" for x, y in FAKE_DOOR_TRIGGERS)
    return _spec(
        GRID,
        npc=OBJECT_SPOTS,
        closed=(),
        title="Gloomsby Gym: dark hall, three doorways, a black pit with stepping stones, pockets",
        uses="Gloomsby Gym (Gym 3, Ghost; SANZUFORD). Used by that one building only.",
        notes=(
            "Dewford Gym secondary (the card's pair). No block ever changes: the initial grid is the solved grid, so "
            "Spec.closed is empty. Walls, rails and pit are solid in the grid; the pit is the blank black metatile 512. "
            "Darkness is script, not tiles: OnTransition runs the setflashlevel ladder of data/maps/DewfordTown_Gym "
            "(6 at the start, 4 after the Hex Maniac, 2 after the Psychic, 0 after SANZUFORD). "
            f"OBJECTS (suggested spots, 4 of 15): SANZUFORD {LEADER} facing south, talked to from {LEADER_TALK}; Hex Maniac "
            f"{HEX_MANIAC} facing east, sight {HEX_SIGHT}; Psychic {PSYCHIC} facing east, sight {PSYCHIC_SIGHT} (the only "
            f"way to the landing: his stone has no way round, so the script must take him off it after the fight, "
            f"by hiding him with a flag, or the player is trapped); light sprite {LIGHT} for the real doorway "
            "(card: (10, 5)). "
            f"DOORWAYS: x {', '.join(map(str, DOORWAYS))}, each two cells deep (y {DOORWAY_ROWS[0]}, {DOORWAY_ROWS[1]}), "
            f"landing y {LANDING_ROW}. Fake doors x {', '.join(map(str, FAKE_DOORS))}: a coord_event with no var on "
            f"{triggers}, the cell entered from the landing, plays the text and runs warpteleport MAP_GLOOMSBY_GYM, "
            f"{LOOP_BACK[0]}, {LOOP_BACK[1]}. The real doorway x {REAL_DOOR} is plain floor. "
            "BG EVENTS: ghost statues = the plaques at (5, 3) and (9, 3), read from (5, 4) and (9, 4); the card's guide "
            "statues = the plaques at (5, 20) and (9, 20), read from (5, 21) and (9, 21) (the orb heads at (5, 19) and "
            "(9, 19) are solid; the sign goes on the plaque); gravestone signs at (2, 9) and (12, 9), read from (2, 10) or "
            "(3, 9) and from (12, 10) or (11, 9). Rail gaps: (4, 12) into the left pocket, (10, 11) into the right pocket. "
            f"WARPS: one on each mat tile, {DOORS[0]} and {DOORS[1]}, both to Gloomsby. "
            "STONES (the card's route, unchanged): (7, 16), (7, 15), (7, 14); west fork (6, 14), (6, 13), (6, 12), (5, 12), "
            "(4, 12) into the left pocket; east route (8, 14), (8, 13), (8, 12), (9, 12), (9, 11) [gap (10, 11) to the right "
            "pocket], (9, 10), then west along y10 through (7, 10) to (5, 10), north (5, 9), (5, 8), (5, 7). "
            "Look compromises: the stones and the two gaps are plain floor tiles; the rails use the post tile (vanilla "
            "only has it on the map edge); the ghost statue is the skull plaque; the orb emblem is Dewford's blue orb, "
            "two of them either side of the leader because it is two tiles wide (the card has one at (7, 1)); the floor is "
            "olive stone, not wood; the three doorways are plain gaps with no door art; four tiles use the nearest "
            "tile because vanilla never draws that shape: (6, 4) and (10, 7) lose their corner shadow, (4, 7) has floor "
            "on both sides of a one-tile post, (11, 8) has a top and left shadow with an open corner. "
            "Used metatile ids: secondary 512 to 580 (the set has 69), primary 6 and 7."
        ),
    )


SPECS = [gloomsby_gym()]
_PROBLEMS = check_puzzle()
if _PROBLEMS:
    raise ValueError("Gloomsby Gym puzzle check failed: " + "; ".join(_PROBLEMS))
