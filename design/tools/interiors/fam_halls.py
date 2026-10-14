"""Shared layouts of the 'halls' family: public halls and special-purpose rooms that are not houses, shops or offices.

Seven layouts, each a different floor plan, each for the building named in its `uses` (cards in design/maps/detail/):

    PLAYHOUSE   13 x 10  Gen 4 wood   a small theatre: a raised stage on a blue carpet, two rows of stools
    TOWER       11 x 10  Gen 4 stone  an old tower's ground floor: flagstones, altar shelf, urns, hearth, sealed stairs
    LOUNGE_1F   31 x 12  Gen 4 wood   the League lounge: bar, armchair corners, a carpet of low tables, clerk and cloak desks
    LOUNGE_2F   31 x 12  Gen 4 teal   its terrace: nine tables in three columns under a row of windows, a balustrade
    CHAMPIONS   11 x 16  Hall of Fame the vanilla Emerald Hall of Fame (CableClub set), cut down to 11 wide
    SHRINE      10 x 9   Gen 4 wood   a shrine hall: stairwell, three pools, a clock face and a clear path for the mirror beam
    CASINO      20 x 16  Game Corner  the vanilla Mauville Game Corner pieces, laid out as the Gildhaven casino

The Gen 4 layouts use `gTileset_Gen4Interior` with primary `gTileset_Building`; ids are map-block ids (secondary index + 512).
Their pieces come from the built Hollowbrook interiors (houses.py) and from the sibling families: fam_homes.py (the green wood
room, the blue carpet, stairs, cushions, armchairs), fam_houses.py (the teal lab floor) and fam_offices.py (the blue counter, the
tall chest). A furniture piece carries a slice of the floor behind it, so every piece below was checked on the floor it stands on.
The Brick Cafe, Zelda House and Dojo sets that the cards ask for are not in the tree: the Gen 4 versions here are the fallbacks
the cards allow. CHAMPIONS and CASINO copy pieces block for block from the vanilla Hall of Fame and Game Corner layouts, so
their collision and elevation are the originals (the two slopes of the Hall of Fame's exit notch are normalised to solid).
Collision follows the kit: furniture solid; floor, rugs and cushions walkable; a seat is a walkable tile so that a person can
sit on it. Nothing here blocks the floor in front of a bookshelf, and no walkable pocket is cut off unless `closed` says so.
LOUNGE_1F and LOUNGE_2F are the only layouts for the two lounge floors of Vesperhaven: fam_shops.py no longer defines a
lounge pair (its docstring points here), so there is nothing to choose between when the layouts are installed.

Run `python3 layoutkit.py fam_halls OUT_DIR` from this folder to lint the specs and write the pictures.
"""
import numpy as np

import houses as H
import layoutkit as K
import fam_homes as HM
import fam_houses as FH
import fam_offices as OF
from layoutkit import F_, W_, Spec

# --- the front edge of a raised stage: the blue counter's end pieces (blue top, orange front) on the blue carpet -------------
LIP_LEFT, LIP_RIGHT = OF.COUNTER_L, OF.COUNTER_R     # a lip segment is a left end then a right end

# --- the stone floor of the tower: the Hollowbrook kitchen tile, with a darker flagstone row under the wallpaper -------------
FLAGSTONE_FOOT = 521                                 # the foot row of a stone room (the wood and teal floors have their own)
URN = FH.POT                                         # red pot drawn on tile floor, one tile, solid
SHELF_JARS = ((546, 547), (562, 563))                # shelf of jars and bottles, 2 x 2, against the wall (bookshelf behaviour)

# --- the terrace balustrade: the flat staircase railing of the Gen 4 set; an end, a repeating pair, an end ------------------
RAIL_LEFT, RAIL_MID, RAIL_RIGHT = 880, (881, 882), 883

# --- the vanilla Hall of Fame (primary Building, secondary CableClub) ---------------------------------------------------
HOF = "LAYOUT_EVER_GRANDE_CITY_HALL_OF_FAME"         # 15 x 17; the rows and columns below are its own
CABLE_CLUB = "gTileset_CableClub"
HOF_TOP_ROWS = 4                                     # rows 0-3: the top wall with its screens and the recess
HOF_TOP_COLUMNS = (0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14)   # the vanilla column that feeds each of the 11 columns of the top wall
HOF_FLOOR_ROW, HOF_LAST_FLOOR_ROW = 6, 15            # vanilla rows used as templates: a plain floor row, the rounded bottom row
HOF_FLOOR, HOF_EDGE_LEFT, HOF_EDGE_RIGHT = 5, 0, 13  # vanilla columns used as templates: plain floor, left wall pair, right wall pair
HOF_CONSOLE_SRC = (HOF, 6, 4, 3, 2)                  # the recording console: a solid upper row and a walkable base row
HOF_NOTCH_SRC = (HOF, 5, 16, 5, 1)                   # the exit notch: slope, three mat tiles, slope
HOF_OUTSIDE_SRC = (HOF, 0, 16, 1, 1)                 # the black solid tile outside the notch
HOF_NOTCH_SLOPES = (3, 7)                            # the notch's two slope columns in the 11-wide room

# --- the Mauville Game Corner set (primary Building, secondary MauvilleGameCorner): pieces copied block for block from the
#     vanilla layout, as (layout id, x, y, width, height) --------------------------------------------------------------
GAME_CORNER = "LAYOUT_MAUVILLE_CITY_GAME_CORNER"     # 22 x 11
GAME_CORNER_SET = "gTileset_MauvilleGameCorner"
CASINO_FLOOR, CASINO_EDGE, CASINO_FOOT = 514, 515, 516   # red dotted carpet, its darker left-edge strip, the foot row under the wall
CASINO_WALL_TOP, CASINO_WALL = 530, 538              # the wall's two rows (solid)
BOOTH_SRC = (GAME_CORNER, 9, 0, 7, 5)                # a prize booth 7 wide, 5 tall: counter, the clerk's recess, a walkable front row
BOOTH_COLUMNS = (0, 1, 3, 5, 6)                      # its columns kept to make the booth 5 wide (the middle pairs repeat)
BANK_SRC = (GAME_CORNER, 1, 5, 4, 6)                 # a double bank of slot machines: stool, two machines, stool; 6 rows with shadow
WHEEL_SRC = (GAME_CORNER, 14, 6, 3, 4)               # a roulette table: 2 wide, 3 tall, with its shadow strip at the right and below
TERMINAL_SRC = (GAME_CORNER, 0, 1, 2, 2)             # two coin-exchange terminals side by side, 2 x 2, on the wall
PLANT_SRC = (GAME_CORNER, 5, 1, 1, 2)                # a potted plant against the wall, 1 x 2
MAT_SRC = (GAME_CORNER, 11, 10, 2, 1)                # the entry mat, two tiles (the south-arrow warp)
ROUND_STOOL = 558                                    # round stool with a pot-like base, one tile, solid


# ---------------------------------------------------------------- helpers for the builders
def armchair(g: np.ndarray, x: int, y: int, facing_east: bool) -> None:
    """An armchair in column x: the back at row y (solid) and the seat at row y+1 (walkable: a person sits there)."""
    back, seat = HM.ARMCHAIR_E if facing_east else HM.ARMCHAIR_W
    g[y, x] = W_ | back[0]
    g[y + 1, x] = F_ | seat[0]


def solidify(g: np.ndarray, x: int, y: int) -> None:
    """Make one cell a normal solid cell: the same metatile with collision 1 and elevation 0 (the kit's solid class)."""
    g[y, x] = W_ | (int(g[y, x]) & 0x3FF)


def sealed(block: np.ndarray) -> np.ndarray:
    """A copy of a grabbed block with every walkable cell made solid (a staircase that cannot be used)."""
    out = block.copy()
    for (y, x), v in np.ndenumerate(block):
        if K.passable(v):
            solidify(out, x, y)
    return out


def stage_lip(g: np.ndarray, y: int, left: int, right: int) -> None:
    """Front edge of a stage along row y: a left end at x=left and a right end at x=right (a segment closes on both sides)."""
    g[y, left] = W_ | LIP_LEFT
    g[y, right] = W_ | LIP_RIGHT


def balustrade(g: np.ndarray, y: int) -> None:
    """A solid railing along the whole of row y, joined without a seam: left end, middle pairs, right end."""
    w = g.shape[1]
    for x in range(w):
        g[y, x] = W_ | (RAIL_LEFT if x == 0 else RAIL_RIGHT if x == w - 1 else RAIL_MID[(x - 1) % 2])


def hall_of_fame_row(g: np.ndarray, y: int, template_row: int) -> None:
    """One floor row of the Hall of Fame room, copied from a vanilla row: the wall pair at the left, floor, the wall pair at
    the right."""
    w = g.shape[1]
    K.stamp(g, 0, y, K.grab(HOF, HOF_EDGE_LEFT, template_row, 2, 1))
    K.stamp(g, 2, y, np.repeat(K.grab(HOF, HOF_FLOOR, template_row, 1, 1), w - 4, axis=1))
    K.stamp(g, w - 2, y, K.grab(HOF, HOF_EDGE_RIGHT, template_row, 2, 1))


# ---------------------------------------------------------------- the layouts
def playhouse() -> Spec:
    """PLAYHOUSE 13 x 10, wood floor, door mat (6,9). Back wall: bookshelf wings (1-2) and (10-11), windows (3-4) and (8-9),
    a painted backdrop (6). Stage: blue carpet x3-8 y2-4 (6 wide, 3 deep) with a lip along y5 that opens in a two-tile step
    at (5,5)-(6,5). Plants (0,4-5) and (12,4-5), a footstool for a prop (11,4). Two rows of stools at y6 and y8, x3 5 7 9.
    The floor in front of both bookshelves stays free so they can be read."""
    g = HM.room(13, 10)
    HM.on_wall(g, 1, H.SHELF)
    HM.on_wall(g, 10, H.SHELF)
    HM.high(g, 3, H.WINDOW)
    HM.high(g, 6, HM.PICTURE)
    HM.high(g, 8, H.WINDOW)
    HM.rug(g, 3, 2, 6, 3)
    stage_lip(g, 5, 3, 4)
    stage_lip(g, 5, 7, 8)
    K.put(g, 0, 4, HM.PLANT)
    K.put(g, 12, 4, HM.PLANT)
    g[4, 11] = W_ | HM.FOOTSTOOL
    for y in (6, 8):
        HM.stools(g, [(x, y) for x in (3, 5, 7, 9)])
    g[9, 6] = F_ | HM.MAT
    return Spec(
        "LAYOUT_VELDRIS_HALL_PLAYHOUSE", "VeldrisHall_Playhouse", g, doors=((6, 9),),
        npc=((4, 3), (6, 3), (5, 5), (6, 5), (9, 7)),
        title="Playhouse: a stage on a blue carpet and two rows of seats, 13 x 10",
        uses="Gloomsby_Playhouse (gloomsby 3.4, 13 x 10, exact fit); also any small hall that wants a stage and rows of seats",
        notes="Card tiles that hold as written: the lead actor (4,3) facing east and the second actor (6,3) facing south on "
              "the stage, the director (6,5) facing north, the audience member (9,7) between the two stool rows. The "
              "director stands in the two-tile step of the stage lip (5,5)-(6,5) and is talked to from (6,6), free between "
              "the stools (5,6) and (7,6); the actors are reached by walking up the step. The stage is the card's 6 x 3 blue "
              "carpet (the card's two rug blocks side by side). Not as the card: the stage has a front lip (the blue "
              "counter's end pieces: blue top, orange front) that the card does not draw. The plants moved out to the wall "
              "edge, (0,4-5) and (12,4-5), so that the two sides match and a plant never stands in front of a shelf (the "
              "card's (1,4) and (11,4) would, if they name the base of a 2-tall plant: it would cover (1,3) and (11,3)). The "
              "card's flower table (11,3) is dropped for the footstool (11,4): (11,3) is the front of the right shelf's "
              "right-hand tile and must stay free. The wings are the bookshelves (signs on their lower tiles (1,2) (2,2) "
              "(10,2) (11,2), read from row 3). The backdrop is the two windows and the picture (6,0-1): the set has no "
              "curtains or footlights.")


def tower() -> Spec:
    """TOWER 11 x 10, stone floor, door mat (4..6,9) on the warp tile (5,9). Back wall: window (0-1), tablet picture (2),
    altar shelf (4-5) between two urns (3) and (6), hearth (7-8), sealed stairs (9-10, rows 0-3). Urns down the left
    wall (1,4-7). A timber floor patch x4-10 y4-7 with the plank table (5-6,5-6) on it."""
    g = K.blank(11, 10, H.TILE, H.WALLTOP, H.WALL, FLAGSTONE_FOOT)
    HM.high(g, 0, H.WINDOW)
    HM.high(g, 2, HM.PICTURE)
    g[2, 3] = g[2, 6] = W_ | URN
    HM.on_wall(g, 4, H.SHELF)
    HM.on_wall(g, 7, H.STOVE)
    K.stamp(g, 9, 0, sealed(K.grab(*HM.STAIRS_UP_SRC)))
    for y in range(4, 8):
        g[y, 1] = W_ | URN
    K.fill(g, 4, 4, 7, 4, H.WOOD)
    K.put(g, 5, 5, HM.DINING_TABLE)
    FH.put_mat(g, 5, FH.TILE_MAT_ENDS)
    return Spec(
        "LAYOUT_VELDRIS_HALL_TOWER", "VeldrisHall_Tower", g, doors=((5, 9),),
        npc=((5, 4), (8, 6)),
        title="Old tower, ground floor: flagstones, altar shelf, urns and a sealed stair, 11 x 10",
        uses="Gloomsby_OldTower_1F (gloomsby 3.4b, 11 x 10, exact fit)",
        notes="The Gen 4 fallback the card allows (its Zelda House set is not in the tree). Stone is the kitchen tile with "
              "the darker flagstone row as the foot row; the timber patch (x4-10, y4-7) carries the plank table (card "
              "(5,5)-(6,6)) and hides the green fringe the staircase and the table legs bring with them. Card tiles as "
              "written: keeper (5,4), lore NPC (8,6), urns (1,4)-(1,7), exit warp (5,9) on the middle of the three-tile mat, "
              "tablet sign on (2,2) read from (2,3) (the picture (2,0-1) is the tablet). Not as the card: the altar is the "
              "bookshelf (4-5,1-2) flanked by two urns (3,2) and (6,2) as candles (the card's x4-6 is one tile off); the "
              "hearth is the kitchen stove (7-8,1-2), the nearest piece; the bricked-up stairway is the Hollowbrook "
              "staircase with its walkable step turned solid, in the corner (9-10, rows 0-3) instead of (8-9,3): put the "
              "'upper floors are closed' sign on (9,3), read from (9,4). Shelf bases carry the bookshelf behaviour; the "
              "stove carries none (set one in Porymap if the hearth should speak).")


def lounge_1f() -> Spec:
    """LOUNGE_1F 31 x 12, wood floor, door mat (14..15,11). Back wall: jar shelves (0-1) and (12-13) close the ends of the bar's
    back row, windows (3-4) and (10-11), pictures (5) and (9), clock (7); windows (14-15) (17-18) (20-21) (23-24); trophy
    shelf (26-27); stairs up (29-30, rows 0-3) whose walkable step (29,2) is the east-arrow warp (enter walking east from
    (28,2)). Bar: counter x3-11 at y3, stools (4,4) (6,4) (8,4) (10,4); the bartender's row is the wall's foot row y2, open
    at the left end through (2,3). Blue carpet x10-20 y5-8 with three low tables and cushions. Armchair corners: (2,6-7)
    facing east with a footstool (3,7) and (27,6-7) facing west with a footstool (26,7). Window table (24-25,4) with a stool
    (23,4). Clerk's desk x8-10 and cloak counter x19-22, both at y9 with the staff behind them at y10; a hat and coat shelf
    (23-24,10-11) at the pocket's right end, which leaves the pocket open to the west; potted trees (1,10-11) and (29,10-11)."""
    g = HM.room(31, 12)
    HM.on_wall(g, 0, SHELF_JARS)
    HM.on_wall(g, 12, SHELF_JARS)
    HM.high(g, 3, H.WINDOW)
    HM.high(g, 5, HM.PICTURE)
    HM.high(g, 7, HM.CLOCK)
    HM.high(g, 9, HM.PICTURE)
    HM.high(g, 10, H.WINDOW)
    for x in (14, 17, 20, 23):
        HM.high(g, x, H.WINDOW)
    HM.on_wall(g, 26, H.SHELF)
    HM.stairs_up(g, 29)
    OF.counter_run(g, 3, 3, 9)
    HM.stools(g, [(x, 4) for x in (4, 6, 8, 10)])
    armchair(g, 2, 6, facing_east=True)
    g[7, 3] = W_ | HM.FOOTSTOOL
    armchair(g, 27, 6, facing_east=False)
    g[7, 26] = W_ | HM.FOOTSTOOL
    HM.rug(g, 10, 5, 11, 4)
    for x, y in ((14, 6), (12, 7), (16, 7)):
        K.put(g, x, y, (HM.LOW_TABLE,))
    for x, y, cushion in ((13, 6, 0), (16, 6, 1), (11, 7, 0), (18, 7, 1)):
        g[y, x] = F_ | HM.CUSHION_BLUE[cushion]
    HM.stools(g, [(23, 4)])
    K.put(g, 24, 4, OF.DESK_LOW)
    OF.counter_run(g, 8, 9, 3)
    OF.counter_run(g, 19, 9, 4)
    K.put(g, 23, 10, H.SHELF)
    K.put(g, 1, 10, HM.PLANT)
    K.put(g, 29, 10, HM.PLANT)
    doors = HM.door_mat(g, 14)
    return Spec(
        "LAYOUT_VELDRIS_HALL_LOUNGE_1F", "VeldrisHall_Lounge1F", g, doors=doors,
        npc=((7, 2), (2, 7), (23, 4), (27, 7), (13, 6), (9, 10), (20, 10), (7, 4), (9, 8), (20, 8)),
        title="League lounge, ground floor: bar, carpet of low tables, clerk and cloak desks, 31 x 12",
        uses="Vesperhaven_LoungeFloor1 (vesperhaven 6.3, 31 x 12, exact fit)",
        notes="Every card tile holds: bartender (7,2) behind the bar (3..11,3), talked to from (7,4) across the cup tile (7,3); "
              "stools (4,4) (6,4) (8,4) (10,4); Ossian (2,7) on the armchair seat with the small table (3,7); Hyacinth "
              "(23,4) on a stool at the window table (24-25,4); Dunmore (27,7) asleep on the west-facing armchair; "
              "Drayden (13,6) on a cushion with the table (14-15,6); the league clerk (9,10) behind the desk (8..10,9), "
              "talked to from (9,8) across the plate tile (9,9); Troglodyte (20,10) behind the cloak counter (19..22,9), "
              "talked to from (20,8) across the plate (20,9); mats (14,11)+(15,11). The card's rug (x10-20, y6-8) is one row "
              "taller here (y5-8) so the three low tables (14-15,6) (12-13,7) (16-17,7) stand on its inner rows. The "
              "plate and cup tiles of the counters already carry MB_COUNTER, so the talk-across spots work with no edit. "
              "Stairs: the card says (29,1); the walkable step is (29,2) (tile 672, east-arrow warp, enter walking east from "
              "(28,2)); pair it with Lounge 2F's landing (30,2) and arrive back from 2F on (28,2), not on the step. Not as the "
              "card: the set has no brick wall, hanging bottles or coat racks: the jar shelves (0-1) and (12-13) close the "
              "bar's ends, a hat shelf (23-24,10-11) stands in for the racks, and the card's armchairs are brown, not "
              "black. The hat shelf is decoration: its front is the map edge and a bookshelf speaks only when faced from the "
              "south, so to make it readable put a facing-any sign on its top tile (23,10) or (24,10), read from (23,9) or "
              "(24,9) facing south. The bartender's row is the wall's foot row, reachable only through (2,3) at the bar's left "
              "end. The columns x0 and x30 are floor (the card draws walls there).")


def lounge_2f() -> Spec:
    """LOUNGE_2F 31 x 12, teal floor, no door: the way in is the stairwell (28-29, rows 1-3) whose walkable step (29,2) is the
    west-arrow warp (enter walking west from (30,2)). Back wall: shelf (0-1), windows (4-5) (10-11) (16-17) (22-23).
    Nine tables in three columns and three rows: a leader's cushion at x4 14 24, a 2 x 2 table at x+1..x+2, a
    visitor's cushion at x+3; the rows are y3-4, y6-7 and y9-10. Potted trees (11,6-7) (21,6-7) (0,8-9) (30,8-9); a
    balustrade closes the bottom row."""
    g = OF.teal_room(31, 12)
    HM.on_wall(g, 0, OF.TEAL_SHELF)
    for x in (4, 10, 16, 22):
        HM.high(g, x, H.WINDOW)
    HM.stairs_down(g, 28)
    balustrade(g, 11)
    for x in (11, 21):
        K.put(g, x, 6, OF.TEAL_PLANT)
    K.put(g, 0, 8, OF.TEAL_PLANT)
    K.put(g, 30, 8, OF.TEAL_PLANT)
    for column in (4, 14, 24):
        for row in (3, 6, 9):
            OF.seats(g, [(column, row), (column + 3, row)], OF.TEAL_CUSHION)
            K.put(g, column + 1, row, OF.SIDE_TABLE)
    return Spec(
        "LAYOUT_VELDRIS_HALL_LOUNGE_2F", "VeldrisHall_Lounge2F", g, doors=((30, 3),),
        npc=((4, 3), (4, 6), (4, 9), (14, 3), (14, 6), (14, 9), (24, 3), (24, 6), (24, 9)),
        title="League lounge, terrace: nine tables under a row of windows, 31 x 12",
        uses="Vesperhaven_LoungeFloor2 (vesperhaven 6.4, 31 x 12, exact fit)",
        notes="The nine leader tiles are the card's: (4,3) (14,3) (24,3) (4,6) (14,6) (24,6) (4,9) (14,9) (24,9), each on a "
              "cushion seat facing right at a table in x+1..x+2 (the card's table is 2 x 1, the set's is 2 x 2, so the "
              "player stands above or below it as the card says). The visitor's cushion at x+3 is an extra. Windows at the "
              "card's x4-5, 10-11, 16-17, 22-23. The lint warns 'door not on the bottom row': expected, there is no exit "
              "mat, the only way in is the stairs (the Apiary 2F does the same). The stairwell's step is (29,2) (tile 695, "
              "west-arrow warp, enter walking west from (30,2)); pair it with Lounge 1F's landing (28,2) and arrive from 1F "
              "on (30,2). The stairwell piece is drawn for a wood floor and shows a thin green edge on the teal. The bottom "
              "row is a balustrade (the card's plain wall) so the terrace has an edge; repaint it in Porymap for a plain wall.")


def champions() -> Spec:
    """CHAMPIONS 11 x 16, the vanilla Hall of Fame set. Top wall copied from the vanilla Hall of Fame: caps (0-1) and (9-10),
    a display screen each at (2) and (8), the recess with its wide screen (3-7, rows 0-3). The recording console stands
    under the recess (4-6, rows 4-5: the upper row solid, the base row walkable). Floor x1-9, y4-14 with the vanilla edge
    strips at x1 and x9 and walls at x0 and x10; the exit is the notch in the bottom row, mats (4..6,15)."""
    w, h = 11, 16
    g = np.zeros((h, w), np.uint16)
    for x, column in enumerate(HOF_TOP_COLUMNS):
        K.stamp(g, x, 0, K.grab(HOF, column, 0, 1, HOF_TOP_ROWS))
    for y in range(HOF_TOP_ROWS, h - 2):
        hall_of_fame_row(g, y, HOF_FLOOR_ROW)
    hall_of_fame_row(g, h - 2, HOF_LAST_FLOOR_ROW)
    K.stamp(g, 4, HOF_TOP_ROWS, K.grab(*HOF_CONSOLE_SRC))
    for x in range(w):
        K.stamp(g, x, h - 1, K.grab(*HOF_OUTSIDE_SRC))
    K.stamp(g, 3, h - 1, K.grab(*HOF_NOTCH_SRC))
    for x in HOF_NOTCH_SLOPES:
        solidify(g, x, h - 1)
    return Spec(
        "LAYOUT_VELDRIS_HALL_CHAMPIONS", "VeldrisHall_Champions", g, doors=((4, h - 1), (5, h - 1), (6, h - 1)),
        npc=((5, 6), (2, 14), (8, 14)),
        primary="gTileset_Building", secondary=CABLE_CLUB,
        title="Hall of Past Champions: the Hall of Fame look, 11 x 16",
        uses="Vesperhaven_HallOfPastChampions (vesperhaven 6.7, 10 x 16 card, one column wider here); the same plan and image "
             "are ThePinnacle_HallOfFame (pinnacle 8), which belongs to the League rooms and needs the real record machine",
        notes="The vanilla Emerald Hall of Fame (the card names it as the option), narrowed from 15 to 11 columns: the "
              "caps, one screen each side and the recess with its wide screen are the vanilla pieces, the recording "
              "console is the vanilla one (decoration here: do not run the real Hall of Fame script). The card's red-and-gold "
              "wall and diamond floor are not reproduced, this is the vanilla purple. Card tiles: the portraits are signs on "
              "the wall tiles (0,y) and (10,y) for y = 4 6 8 10 12 (the card's x0 and x9), read from (1,y) and (9,y); "
              "Cynthia's is (0,12), the unfinished frame (10,12); the walls carry no frame art, the only visible "
              "frames are the three green screens in the top wall. The attendant stands at (5,6) (card (5,5), which is the "
              "console's walkable base row, where a person would stand in front of the picture of the machine); the two "
              "Rare Candy balls at (2,14) and (8,14) (card (2,14) and (7,14), the second mirrored for the extra column). "
              "Exit: the notch's three mat tiles (4..6,15), warp on the middle one (card mats (4,15),(5,15)). Why 11 and "
              "not the card's 10: the vanilla recess is a symmetrical 5 columns wide over a 3-wide console, so an even "
              "room would leave both off-centre by half a tile; one tile over a card is what the shared-layout rule "
              "allows. The card (vesperhaven.md 6.7 and the warp table in 7) then needs: width 11, portraits x0 and x10, "
              "mats (4..6,15), attendant (5,6), candies (2,14) and (8,14).")


def shrine() -> Spec:
    """SHRINE 10 x 9, wood floor, door mat (4..5,8). Back wall: window (0-1), scroll picture (2), stairwell down (3-4, rows
    1-3) whose walkable step (4,2) is the west-arrow warp (enter walking west from (5,2)), window (5-6), clock (7), the carved
    door (8, rows 0-1: a tall locked chest in the wall). Three pools of teal glass, solid, two by two: (1-2,5-6), (1-2,7-8)
    (these two touch, as the card's do) and (7-8,7-8); a pale light patch (8,6); the blue carpet clock face x3-5 y4-6; potted
    trees (9,4-5) and (0,7-8). The hermit's corner (x0-2, rows 2-3) is walled in by the stairwell on the east, so row 4
    stays free across x0-2 and joins it to the carpet. The mirror puzzle's beam runs through free floor: (8,6) (7,6) (6,6),
    (6,5) (6,4), (7,4) (8,4), (8,3) (8,2)."""
    g = HM.room(10, 9)
    HM.high(g, 0, H.WINDOW)
    HM.high(g, 2, HM.PICTURE)
    HM.stairs_down(g, 3)
    HM.high(g, 5, H.WINDOW)
    HM.high(g, 7, HM.CLOCK)
    K.put(g, 8, 0, OF.FILING)
    for x, y in ((1, 5), (1, 7), (7, 7)):
        K.put(g, x, y, ((HM.GLASS, HM.GLASS),) * 2)
    g[6, 8] = F_ | H.TILE
    for y in range(4, 7):
        for x in range(3, 6):
            g[y, x] = F_ | FH.CARPET[y - 4][x - 3]
    K.put(g, 9, 4, HM.PLANT)
    K.put(g, 0, 7, HM.PLANT)
    doors = HM.door_mat(g, 4)
    return Spec(
        "LAYOUT_VELDRIS_HALL_SHRINE", "VeldrisHall_Shrine", g, doors=doors,
        npc=((2, 2), (6, 6), (6, 4), (8, 4), (7, 2), (8, 6)),
        title="Shrine hall: stairwell, three pools and a clock face, 10 x 9",
        uses="MirrorIsle_Shrine (mirror-isle-detail 4, 10 x 9, exact fit)",
        notes="The Gen 4 fallback for the card's Dojo set (not in the tree; the card's other fallback, the Sootopolis gym, "
              "would need a second tileset). Green planks stand in for the tatami, teal glass squares for the pools (solid, "
              "the player reads them by facing them), the blue carpet for the clock face, the tall locked chest in the wall "
              "for the carved door. Card tiles as written: hermit (2,2) facing down, stairs down (4,2) (tile 695, "
              "west-arrow warp, entered walking west from (5,2): arrive back from the Hollow on (5,2)), TM Light Screen "
              "ball (7,2), mirrors M1 (6,6), M2 (6,4), M3 (8,4), exit mat (5,8) (here (4,8)+(5,8), warp on both), the "
              "skylight patch (8,6) (a pale tile), the carved door (8,1) (swap its two tiles with setmetatile when the beam "
              "lands: the closed look is the chest 811/819, put the open look in Porymap). Every tile of the beam path is "
              "free floor. The hermit's corner (x0-2, rows 2-3) is shut in by the two-wide stairwell (3-4, rows 1-3), where "
              "the card leaves (3,2) and (3,3) free: it is joined to the room by row 4, free across x0-2 and open to the "
              "carpet at (3,4), so the player walks in three tiles wide; the strip (0,5)-(0,6) beside the pool is a short "
              "dead end, still reachable. Not as the card: the pools are three 2 x 2 squares at (1-2,5-6), (1-2,7-8) and "
              "(7-8,7-8) (the card's P1 y4-5 and P2 y6-7 touch, as these two do, one row lower so that row 4 is free; its "
              "P3 is 2 x 1); the clock face is a plain blue 3 x 3 carpet (the set has no clock pattern); x0 and x9 are "
              "floor, the card's walls.")


def casino() -> Spec:
    """CASINO 20 x 16, the Mauville Game Corner set. Back wall: prize booths 5 wide at x1-5 and x14-18 (rows 0-4; the clerk's
    recess is the walkable pocket (2-4,2) and (15-17,2), sealed on purpose; the front row y4 is walkable and the player faces
    north from it), coin terminals (9-10,1-2) between them, potted plants (7,1-2) and (12,1-2). Two double banks of slot
    machines at x6-9 and x11-14, rows 6-11 (stools at x6 and x9, x11 and x14, the machines between). Two roulette tables at
    x17-18, rows 6-9 and 10-13, with a shadow strip at x19. Round stools down the left (1,6) (1,8) (1,10) (1,12). Entry mat
    (3..4,15)."""
    g = np.full((16, 20), F_ | CASINO_FLOOR, np.uint16)
    g[:, 0] = F_ | CASINO_EDGE
    g[0, :] = W_ | CASINO_WALL_TOP
    g[1, :] = W_ | CASINO_WALL
    g[2, :] = F_ | CASINO_FOOT
    booth = K.grab(*BOOTH_SRC)[:, list(BOOTH_COLUMNS)]
    K.stamp(g, 1, 0, booth)
    K.stamp(g, 14, 0, booth)
    K.stamp(g, 9, 1, K.grab(*TERMINAL_SRC))
    for x in (7, 12):
        K.stamp(g, x, 1, K.grab(*PLANT_SRC))
    for x in (6, 11):
        K.stamp(g, x, 6, K.grab(*BANK_SRC))
    for y in (6, 10):
        K.stamp(g, 17, y, K.grab(*WHEEL_SRC))
    for y in (6, 8, 10, 12):
        g[y, 1] = W_ | ROUND_STOOL
    K.stamp(g, 3, 15, K.grab(*MAT_SRC))
    return Spec(
        "LAYOUT_VELDRIS_HALL_CASINO", "VeldrisHall_Casino", g, doors=((3, 15), (4, 15)),
        npc=((3, 4), (16, 4), (9, 3), (5, 8), (10, 8), (16, 8)),
        closed=tuple((x, 2) for x in (2, 3, 4, 15, 16, 17)),
        primary="gTileset_Building", secondary=GAME_CORNER_SET,
        title="Casino: two prize booths, two banks of slot machines and two roulette tables, 20 x 16",
        uses="Gildhaven_Casino (gildhaven 4.7, 20 x 16, exact fit; optional building, card open question 6)",
        notes="Every piece is copied block for block from the vanilla Mauville Game Corner (same ids, collision and "
              "elevation), so the vanilla scripts' furniture works as it does there: the slot machines and roulette "
              "tables are the vanilla pieces, and the author puts the same signs on them. The card's plan holds: two "
              "prize and exchange counters on the top wall (left x1-5, right x14-18, the vanilla booth cut to five "
              "tiles), the coin terminals at the middle, two double banks (x6-9 and x11-14, rows 6-11), two roulette "
              "tables on the right, the mat at (3,15). The two clerks stand inside the booth recesses at (3,2) and "
              "(16,2) (walkable but sealed, listed as closed), talked to from the walkable front row (3,4) and (16,4) "
              "across the counter top (row 3, MB_COUNTER); the card's coin clerk (2,2) is a recess tile too, so (2,2) works "
              "as well as (3,2). Manager (9,3) between the booths. The card's gamblers (7,9) and (12,9) fall on slot "
              "machines in this arrangement (the banks cover x6-9 and x11-14, rows 6-11), so they stand in the free aisles "
              "at (5,8) and (10,8). The croupier is at (16,8) beside the first table (card (17,8), now a table tile). Not as "
              "the card: the tables are at x17-18 (the card's x17 only), the left column holds round stools instead of "
              "plants and stools (a plant piece exists only against the wall), and there is no central poster at (12,1) "
              "(the coin terminals (9-10,1-2) take its place).")


SPECS = [playhouse(), tower(), lounge_1f(), lounge_2f(), champions(), shrine(), casino()]
