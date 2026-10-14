"""Shared work-room layouts of the 'offices' family: clerks' offices, a front hall, a library, a store room and a workshop.

Six layouts on the Gen 4 Interior set (`gTileset_Gen4Interior`, primary `gTileset_Building`), each reused by several
buildings of the cards in design/maps/detail/ (the `uses` of every spec names them):

    COUNTER    11 x 8   teal   a clerk's office: reception counter, the clerk's pocket behind it, a display table
    DESKS      12 x 8   teal   an open office: a desk at each end of the wall, a long table between them
    HALL       13 x 10  teal   a front hall: a U-shaped counter, a dark inner doorway, filing shelves, a rug
    READING    12 x 11  wood   a reading room: shelves, a poster, two pairs of desks and stools, a stairwell down
    ARCHIVE     9 x 8   wood   a store room: shelves, crates, a one-tile gap for a boulder, stairs up
    WORKSHOP   13 x 10  wood   a workshop: two hearths, a drying table, salt jars, barrels and crates

The Team Aqua 'Little Office' set that the cards ask for is not in the tree, so these are the Gen 4 fallbacks the cards allow.
Pieces come from the built Hollowbrook interiors (houses.py) and from the two sibling families: fam_houses.py (the teal lab
floor) and fam_homes.py (the green wood floor, the stairs). A furniture piece carries a slice of the floor behind it, so every
piece below was checked on the floor it stands on: tables three or more tiles wide exist only on teal, barrels and salt jars
only on wood. The blue counter, the filing chest and the cardboard box are floor-neutral. Collision follows the kit:
furniture solid; floor, rugs and cushions walkable.

Run `python3 layoutkit.py fam_offices OUT_DIR` from this folder to lint the specs and write the pictures.
"""
import houses as H
import layoutkit as K
import fam_homes as HM
import fam_houses as FH
from layoutkit import F_, W_

# --- the back wall, the same on every floor ------------------------------------------------------------------------
WALL_TRIM, WALL_PAPER = FH.WALL_TRIM, FH.WALL_PAPER  # 518 red trim, 526 striped wallpaper (row 2 is the floor's foot row)
WINDOW = H.WINDOW                                    # arched window, wall rows 0-1, 2 wide
CLOCK = HM.CLOCK                                     # round wall clock, wall rows 0-1, 1 wide
PICTURE = HM.PICTURE                                 # framed landscape, wall rows 0-1, 1 wide (a map, a notice, a poster)
DOORWAY = ((760, 761, 762), (768, 769, 770))         # dark open doorway, 3 x 2, wall rows 0-1; 769 carries MB_NON_ANIMATED_DOOR
FILING = ((811,), (819,))                            # tall chest with a lock, 1 x 2, floor-neutral: a filing cabinet
BOX = 920                                            # cardboard box, one tile, floor-neutral

# --- the blue counter: floor-neutral; only the plate, cup and 624 tiles carry MB_COUNTER, so plates and cups alternate -----
COUNTER_L, COUNTER_PLATE, COUNTER_CUP, COUNTER_R = 640, 641, 721, 643   # left end, plate, cup, right end of a straight run
ARM_L = (624, 723)                                   # left arm of a U: top (it meets the wall's foot row), then a cup tile
ARM_R = (635, 724)                                   # right arm of a U: top, then a cup tile
CORNER_L, CORNER_R = 640, 626                        # lower corners of a U: the left end piece, the right end with a highlight

# --- the teal floor (the Fennick lab's) and the pieces drawn for it ------------------------------------------------
TEAL, TEAL_FOOT = FH.TEAL, FH.TEAL_FOOT              # 737 floor, 738 the darker row under the wallpaper
TEAL_SHELF = FH.TEAL_SHELF                           # bookshelf, 2 x 2, teal behind its base
TEAL_PLANT = FH.TEAL_PLANT                           # potted tree, 1 x 2
TEAL_CUSHION = FH.TEAL_CUSHION                       # 743 walkable stool or bench seat
TEAL_DESK = FH.DESK                                  # writing desk with a monitor and papers, 2 x 2, against the wall
SIDE_TABLE = ((534, 535), (951, 952))                # 2 x 2 table with an orange top (the lab's aide desks)
TABLE_TOP = (832, 833, 834)                          # long lab table, top row: left end, middle, right end
TABLE_FRONT = (840, 841, 842)                        # its front row (it carries MB_COUNTER); the middle repeats for any width

# --- the wood floor (the houses') and the pieces drawn for it ------------------------------------------------------
WOOD_SHELF = H.SHELF                                 # bookshelf, 2 x 2, green behind its base
WOOD_PLANT = HM.PLANT                                # potted tree, 1 x 2
WOOD_TABLE = HM.DINING_TABLE                         # 2 x 2 table with an orange cloth, top and legs, drawn for wood
# The table's front half alone (2 x 1) has no top rim and looks cut off: the layouts here use WOOD_TABLE. It stays only
# because fam_halls.py puts it by a window.
DESK_LOW = ((542, 543),)
STOOL = HM.STOOL                                     # 605 walkable cushion stool
HEARTH = HM.STOVE_WOOD                               # stove with its base drawn for wood, 2 x 2, against the wall
SALT_JAR = 649                                       # red clay pot with a white heap, one tile
BARREL = HM.BARREL                                   # 926 barrel with a white lid, one tile


# ---------------------------------------------------------------- helpers for the builders
def teal_room(w: int, h: int):
    """Back wall (rows 0-2) and teal floor everywhere else."""
    return K.blank(w, h, TEAL, WALL_TRIM, WALL_PAPER, TEAL_FOOT)


def counter_run(g, x: int, y: int, width: int, cups: bool = True) -> None:
    """A straight blue counter `width` tiles long (4 or more) at row y: left end, then plates (and cups, unless `cups` is
    False) alternating, right end. Every tile between the ends carries MB_COUNTER, so a person two tiles behind it can be
    talked to across it."""
    middle = [COUNTER_CUP if cups and i % 2 else COUNTER_PLATE for i in range(width - 2)]
    for i, m in enumerate([COUNTER_L, *middle, COUNTER_R]):
        g[y, x + i] = W_ | m


def u_counter(g, left: int, right: int, top: int, bottom: int) -> None:
    """A U-shaped counter: arms at columns `left` and `right` from row `top` down to row bottom-1, joined by a run along row
    `bottom` (plates and cups alternate between the two corners). The arms start under the wall's foot row, so the pocket
    inside stays reachable along that row."""
    for y in range(top, bottom):
        arm = 0 if y == top else 1
        g[y, left] = W_ | ARM_L[arm]
        g[y, right] = W_ | ARM_R[arm]
    g[bottom, left], g[bottom, right] = W_ | CORNER_L, W_ | CORNER_R
    for i, x in enumerate(range(left + 1, right)):
        g[bottom, x] = W_ | (COUNTER_CUP if i % 2 else COUNTER_PLATE)


def long_table(g, x: int, y: int, width: int) -> None:
    """The lab's long table on teal, `width` tiles wide (3 or more), top row at y and counter front row at y+1."""
    top = (TABLE_TOP[0],) + (TABLE_TOP[1],) * (width - 2) + (TABLE_TOP[2],)
    front = (TABLE_FRONT[0],) + (TABLE_FRONT[1],) * (width - 2) + (TABLE_FRONT[2],)
    K.put(g, x, y, (top, front))


def seats(g, cells, tile: int) -> None:
    """Walkable seat tiles (cushion stools, bench cushions) at the given (x, y) cells."""
    for x, y in cells:
        g[y, x] = F_ | tile


# ---------------------------------------------------------------- the layouts
def counter_office() -> K.Spec:
    """COUNTER 11 x 8, teal floor, door mat (4..6,7) on the warp tile (5,7). Back wall: shelf (0-1), picture (2), window
    (3-4), clock (5), writing desk (6-7), shelf (8-9), filing cabinet (10). Reception counter x1-7 at y4 (plate and cup
    tiles x2-6): its left end touches the potted tree (0,3-4), so the clerk's row 3 is sealed on the left; the pocket is
    open only at the right end (8,3)-(8,4). A stack of three cardboard boxes (9-10,4) and (10,5) is the unclaimed luggage.
    Customers' side: display table (6-7,5-6), a bench of two cushions (8-9,5), a potted tree in the lower right corner
    (10,6-7) and one in the lower left (0,6-7)."""
    g = teal_room(11, 8)
    HM.on_wall(g, 0, TEAL_SHELF)
    HM.high(g, 2, PICTURE)
    HM.high(g, 3, WINDOW)
    HM.high(g, 5, CLOCK)
    HM.on_wall(g, 6, TEAL_DESK)
    HM.on_wall(g, 8, TEAL_SHELF)
    HM.on_wall(g, 10, FILING)
    counter_run(g, 1, 4, 7)
    K.put(g, 0, 3, TEAL_PLANT)
    for x, y in ((9, 4), (10, 4), (10, 5)):
        g[y, x] = W_ | BOX
    K.put(g, 6, 5, SIDE_TABLE)
    seats(g, ((8, 5), (9, 5)), TEAL_CUSHION)
    K.put(g, 0, 6, TEAL_PLANT)
    K.put(g, 10, 6, TEAL_PLANT)
    FH.put_mat(g, 5, FH.TEAL_MAT_ENDS)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_COUNTER", "VeldrisOffice_Counter", g, doors=((5, 7),),
        npc=((3, 3), (4, 3), (5, 3), (8, 3), (2, 5), (4, 5), (5, 5), (8, 5), (9, 5)),
        title="Counter office: a reception counter with the clerk behind it, 11 x 8",
        uses="Waymeet_LostProperty (waymeet 4.5), Gloomsby_Parlour (gloomsby 3.8) and Gildhaven_SalesOffice (gildhaven 4.8), "
             "all 11 x 8, exact fit; Waymeet_DockOffice (waymeet 4.4) and Cragdale_QuarryOffice (cragdale 4.5), 10 x 8 cards, "
             "so one column wider here",
        notes="Clerk spots (3..5,3): the player talks from (x,5) across the plate and cup tiles x2-6, which already carry "
              "MB_COUNTER (the end pieces (1,4) and (7,4) do not); the display table stands in front of x6-7, so (6,3) is "
              "not a clerk spot. The left end (1,4) touches the potted tree (0,3-4), so the only way behind the counter is "
              "the right-hand gap (8,3)-(8,4). Card tiles that fit as written: Dock harbourmaster and "
              "Lost Property clerk (5,3), Quarry clerk (4,3), Dock deckhand (2,5), Lost Property man and Sales model-maker "
              "(8,5). Not as the cards: the Sales clerk (card (5,4)) and the Parlour mortician (card (4,4)) stand at (5,3) "
              "and (4,3), because row 4 is the counter here. Props the cards name: the display table (6-7,5-6) is the Dock's "
              "chart table with the canal model (sign on (7,5)) and the Sales Office's model of Gildhaven (sign on (6,5)); "
              "the stack of boxes (9-10,4), (10,5) is Lost Property's 'UNCLAIMED' trunk (card (9,3), sign on (9,4)); the "
              "writing desk (6-7,1-2) is the Quarry ledger and the picture (2,0-1) its map (sign on (2,2), read from (2,3)); the Dock's "
              "tide table sign goes on (3,2), read from (3,3); the shelf bases (1,2), (8,2), (9,2) take Lost Property's hats "
              "and umbrellas. The desk monitor (933) is the Hollowbrook bedroom-PC tile: a prop here. The two cushions "
              "(8-9,5) are the Parlour's bench and walkable, so the Lost Property man can wander over them. The card's "
              "plants at (1,3) and (9,3) are not drawn ((1,3) is the clerk's end of the counter, (9,3) a shelf front). "
              "Sales Office has no glass pieces (Little Office is not in the tree).")


def open_office() -> K.Spec:
    """DESKS 12 x 8, teal floor, door mat (4..7,7) on the warp tiles (5,7) and (6,7). Back wall: writing desk (0-1), window
    (2-3), picture (4), window (5-6), picture (7), shelf (8-9), writing desk (10-11). A stool in front of each monitor
    (0,3) and (10,3). The lab's long table x4-7 at y3-4 (front row y4) with the foot row open behind it. Potted trees
    (0,5-6) and (11,5-6)."""
    g = teal_room(12, 8)
    HM.on_wall(g, 0, TEAL_DESK)
    HM.high(g, 2, WINDOW)
    HM.high(g, 4, PICTURE)
    HM.high(g, 5, WINDOW)
    HM.high(g, 7, PICTURE)
    HM.on_wall(g, 8, TEAL_SHELF)
    HM.on_wall(g, 10, TEAL_DESK)
    seats(g, ((0, 3), (10, 3)), TEAL_CUSHION)
    long_table(g, 4, 3, 4)
    K.put(g, 0, 5, TEAL_PLANT)
    K.put(g, 11, 5, TEAL_PLANT)
    FH.put_mat(g, 5, FH.TEAL_MAT_ENDS, tiles=2)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_DESKS", "VeldrisOffice_Desks", g, doors=((5, 7), (6, 7)),
        npc=((4, 5), (7, 5), (9, 4), (1, 5), (2, 5), (10, 5), (10, 6), (9, 6), (3, 3), (6, 2), (8, 3)),
        title="Open office: a desk at each end of the wall and a long table, 12 x 8",
        uses="Gloomsby_ProductionOffice (gloomsby 3.9, 13 x 8 card, so one column narrower here) and Smeltham_MineOffice "
             "(smeltham 3.4, 11 x 8 card, so one column wider here)",
        notes="Production Office: PC desks (0-1,1-2) and (10-11,1-2) with a stool in front of each monitor (card x1-2 and "
              "x10-11); the folding table is the long table x4-7, y3-4 (card x5-7, y3-4); the script board is the picture "
              "(7,0-1), sign on (7,1), read from (7,2) along the foot row behind the table (card (6,1)); producer (4,5) and "
              "runner (9,4) are the card's own tiles; the boxes are objects the flag hides after Scheme 3, free floor for "
              "them at (1,5), (2,5), (10,5), (10,6), (9,6) (the card's (11,5), (11,6), (12,5) are the plant column or off "
              "the map). Mine Office: the table is the desk (card x6-8, y3-4), the clerk at (7,5) facing north as the card "
              "says; hard-hat shelf = the shelf (8-9,1-2), exactly the card's x8-9; the mine map = the picture (7,0-1) "
              "(card (8,1)); window pair (5-6) as the card; plants (0,5-6) and (11,5-6) for the plant column. Not as the "
              "Mine card: no kitchen block or kettle (put the kettle in the shelf's sign line). The mat is at (5,7)+(6,7) "
              "for both buildings, not the Mine card's (2,7).")


def front_hall() -> K.Spec:
    """HALL 13 x 10, teal floor, door mat (5..7,9) on the warp tile (6,9). Symmetrical about column 6. Back wall: shelf (0-1),
    picture (2), window (3-4), dark doorway (5-7), window (8-9), picture (10), shelf (11-12). A U-shaped counter: arms at x3
    and x9 (rows 3-4), run along y5 from x3 to x9 (plate and cup tiles x4-8); the pocket inside is x4-8, rows 3-4, and
    opens along the foot row. Blue rug (4-8,7-8) in front of the door, a bench of three cushions (1-3,7), the lab's aide
    table (10-11,6-7), potted trees (0,8-9) and (12,8-9)."""
    g = teal_room(13, 10)
    HM.on_wall(g, 0, TEAL_SHELF)
    HM.on_wall(g, 11, TEAL_SHELF)
    HM.high(g, 2, PICTURE)
    HM.high(g, 10, PICTURE)
    HM.high(g, 3, WINDOW)
    HM.high(g, 8, WINDOW)
    K.put(g, 5, 0, DOORWAY)
    u_counter(g, 3, 9, 3, 5)
    HM.rug(g, 4, 7, 5, 2)
    seats(g, ((1, 7), (2, 7), (3, 7)), TEAL_CUSHION)
    K.put(g, 10, 6, SIDE_TABLE)
    K.put(g, 0, 8, TEAL_PLANT)
    K.put(g, 12, 8, TEAL_PLANT)
    FH.put_mat(g, 6, FH.TEAL_MAT_ENDS)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_HALL", "VeldrisOffice_Hall", g, doors=((6, 9),),
        npc=((6, 2), (5, 4), (6, 4), (7, 4), (6, 6), (2, 5), (12, 7), (9, 7)),
        title="Front hall: a U-shaped counter, a dark inner doorway and a rug, 13 x 10",
        uses="Brinecombe_HarbourOffice (brinecombe 5.4, 13 x 10, exact fit) and Kingsquay_TallowAndCrane (kingsquay 6.9, "
             "14 x 10 card, so one column narrower here)",
        notes="Harbour Office: the master stands inside the U at (6,4) (card (6,3): the counter tiles x4-8 carry MB_COUNTER, "
              "so the player talks across (6,5) from (6,6) as the card says); tide table = the left shelf base (1,2) (card "
              "(1,2)); the dark back door is the doorway (5-7,0-1), centred instead of the card's (9,1), no warp; chart "
              "table = the aide table (10-11,6-7) (card (11,4),(11,5)); plants (0,8-9) and (12,8-9) (card (1,8),(11,8)); "
              "the card's round rug is the 5 x 2 blue rug (4-8,7-8); sailor at (9,7) facing east to the chart table "
              "(card (10,7), which is the table here). Tallow & Crane: second "
              "clerk at (7,4) (card (7,3)), Mr Tallow at (6,2) before the locked doorway as the card says (the foot row "
              "is open round the arms); invoice table (10-11,6-7) and Pip (12,7) are the card's own tiles; the filing "
              "shelves 'Q' are the shelves (0-1,1-2) and (11-12,1-2) (signs on (1,2) and (11,2)); windows at (3-4) and "
              "(8-9) (card (3,1) and (9,1)); the mat is one warp tile (6,9) (card (6,9)+(7,9)). Doorway tile (6,1) (769) "
              "carries MB_NON_ANIMATED_DOOR and is solid: put a sign on it for 'closed for conclusions', or nothing for "
              "the Harbour's decorative door. Counter behaviour: the plate and cup tiles x4-8 of the run and the left arm's "
              "top tile (3,3) (624) carry MB_COUNTER, the right arm's top (9,3) does not, so a player at (2,3) can talk across "
              "(3,3) to (4,3): leave (4,3) empty. Little Office is not in the tree, so Tallow & Crane has no glass "
              "partition.")


def reading_room() -> K.Spec:
    """READING 12 x 11, wood floor, door mat (5,10)+(6,10). Back wall: bookshelves (0-1) and (2-3), clock (4), two pictures
    (5) (6) as the poster, window (7-8), stairwell down (9-10, rows 1-3) whose walkable step (10,2) is the west-arrow warp
    (enter walking west from (11,2)). Two reading tables (3-4,4-5) and (7-8,4-5), each with two cushion stools in front
    at y6. Standing bookshelves (1-2,7-8) and (9-10,7-8), blue rug (4-7,8-9), potted trees (0,8-9) and (11,8-9)."""
    g = HM.room(12, 11)
    HM.on_wall(g, 0, WOOD_SHELF)
    HM.on_wall(g, 2, WOOD_SHELF)
    HM.high(g, 4, CLOCK)
    HM.high(g, 5, PICTURE)
    HM.high(g, 6, PICTURE)
    HM.high(g, 7, WINDOW)
    HM.stairs_down(g, 9)
    K.put(g, 3, 4, WOOD_TABLE)
    K.put(g, 7, 4, WOOD_TABLE)
    seats(g, ((3, 6), (4, 6), (7, 6), (8, 6)), STOOL)
    K.put(g, 1, 7, WOOD_SHELF)
    K.put(g, 9, 7, WOOD_SHELF)
    HM.rug(g, 4, 8, 4, 2)
    K.put(g, 0, 8, WOOD_PLANT)
    K.put(g, 11, 8, WOOD_PLANT)
    doors = HM.door_mat(g, 5)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_READING", "VeldrisOffice_Reading", g, doors=doors,
        npc=((5, 4), (6, 4), (3, 7), (8, 7), (11, 2), (2, 4)),
        title="Reading room: shelves, a poster, two reading tables and a stairwell down, 12 x 11",
        uses="HemlockReach_ReadingRoom (hemlock-reach 5.5, 12 x 11, exact fit). Gildhaven_PilotsClub (gildhaven 4.6, 12 x 14) "
             "is the same Trainer School plan three rows taller: duplicate this layout, add three rows and paint the "
             "stairwell over",
        notes="Stairwell (9-10,1-3): the walkable step (10,2) (tile 695, west-arrow warp) leads to the Archive's step (7,2); "
              "the player enters walking west from (11,2). Its top row (686, 687) still carries MB_BOOKSHELF in the "
              "tileset, a book line if the player faces it from the step: clear it or leave it. Archivist (6,4), readers "
              "(3,7) and (8,7): the card's tiles. The poster is the two pictures (5,0-1) and (6,0-1) (card: the green "
              "board at (5,2),(6,2): signs on (5,2) and (6,2), read from (5,3) and (6,3)). Bookshelves (0-3) (card x1-2), "
              "window (7-8) (card x8-10, the stairwell takes x9-10). The card's four desks at (3,5), (4,5), (7,5), (8,5) "
              "with stools at y6 are two 2 x 2 tables (3-4,4-5) and (7-8,4-5), whose front row is the card's y5, with "
              "two stools each; (5,4) and (6,4) stay free between them for the archivist. Plants (0,8-9) and (11,8-9) "
              "(card (1,9), (10,9)). Extras beyond the card (it says 'the rest is open floor'): the standing bookshelves and the rug; "
              "paint them out in Porymap if the room feels full. Mat (5,10)+(6,10) (card (6,10)).")


def archive() -> K.Spec:
    """ARCHIVE 9 x 8, wood floor, no door: the way in is the staircase (7-8, rows 0-3) whose walkable bottom step (7,2) is
    the east-arrow warp (enter walking east from (6,2)). Back wall: three bookshelves (0-1) (2-3) (4-5). A line of crates
    at x4 (rows 3 and 5-7) leaves a one-tile passage at (4,4); the boulder spot (5,4) is just east of it. West of the
    line, crates (1,5) and (2,5). Cabinets (0,3-4) and (8,4-5), a sorting table (5-6,6-7) that leaves (7,5)-(8,7)
    open round it."""
    g = HM.room(9, 8)
    HM.on_wall(g, 0, WOOD_SHELF)
    HM.on_wall(g, 2, WOOD_SHELF)
    HM.on_wall(g, 4, WOOD_SHELF)
    HM.stairs_up(g, 7)
    for y in (3, 5, 6, 7):
        g[y, 4] = W_ | BOX
    for x in (1, 2):
        g[5, x] = W_ | BOX
    K.put(g, 0, 3, FILING)
    K.put(g, 8, 4, FILING)
    K.put(g, 5, 6, WOOD_TABLE)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_ARCHIVE", "VeldrisOffice_Archive", g, doors=((6, 3),),
        npc=((6, 2), (5, 4), (4, 4), (3, 4), (1, 4), (6, 5)),
        title="Archive store room: shelves, a crate line with a one-tile passage and stairs up, 9 x 8",
        uses="HemlockReach_ReadingRoom_Archive (hemlock-reach 5.5, 9 x 8, exact fit)",
        notes="No exit mat: the only way in is the staircase, whose walkable bottom step (7,2) (tile 672, east-arrow warp) "
              "joins the Reading Room's step (10,2); the player enters walking east from (6,2). The lint warning 'door not "
              "on the bottom row' is expected (the kit's door here is the landing (6,3)). The crates at x4 (rows 3 and "
              "5-7) leave a one-tile passage at (4,4) (card: stacks at (4,3) and (4,5)) and the boulder starts at (5,4) as "
              "the card says. The card's route does not work as written (the ball at (7,5) is on the boulder's own side), "
              "so the plan here: push the boulder west from (6,4) through (4,4) into (3,4), then (2,4), which opens the "
              "west half; put the TM Rock Tomb ball there, e.g. (1,4) (card (7,5)). Crates (1,5), (2,5) are the card's. "
              "Extras: cabinets (0,3-4) and (8,4-5), a sorting table (5-6,6-7) (talk to it from (5,5) or (6,5)). The "
              "boulder can also be pushed north or south, from (5,5) or (5,3): that opens (4,4) without the west push. It "
              "is harmless (Strength is still needed, nothing locks: pushed north the boulder sticks at (5,3) and only "
              "hides that shelf's line), so no crate was added at (5,3). Shelf bases carry the bookshelf behaviour.")


def workshop() -> K.Spec:
    """WORKSHOP 13 x 10, wood floor, door mat (6,9)+(7,9). Back wall: shelf (0-1), window (2-3), shelf (4-5), window (6-7),
    clock (8), hearths (9-10) and (11-12). Drying table: a counter x4-8 at y4 (plates at x5-7). Salt jars in a column
    (0,3-6), barrels (12,5-6) beside a cabinet (11,5-6), crates (11,7) (12,7) (12,8), a tea table (6-7,6-7) with a
    stool each side of its top (5,6) and (8,6)."""
    g = HM.room(13, 10)
    HM.on_wall(g, 0, WOOD_SHELF)
    HM.high(g, 2, WINDOW)
    HM.on_wall(g, 4, WOOD_SHELF)
    HM.high(g, 6, WINDOW)
    HM.high(g, 8, CLOCK)
    HM.on_wall(g, 9, HEARTH)
    HM.on_wall(g, 11, HEARTH)
    counter_run(g, 4, 4, 5, cups=False)
    for y in range(3, 7):
        g[y, 0] = W_ | SALT_JAR
    for y in (5, 6):
        g[y, 12] = W_ | BARREL
    K.put(g, 11, 5, FILING)
    for x, y in ((11, 7), (12, 7), (12, 8)):
        g[y, x] = W_ | BOX
    K.put(g, 6, 6, WOOD_TABLE)
    seats(g, ((5, 6), (8, 6)), STOOL)
    doors = HM.door_mat(g, 6)
    return K.Spec(
        "LAYOUT_VELDRIS_OFFICE_WORKSHOP", "VeldrisOffice_Workshop", g, doors=doors,
        npc=((6, 3), (3, 6), (10, 3), (6, 5), (10, 5)),
        title="Workshop: two hearths, a drying table, salt jars, barrels and crates, 13 x 10",
        uses="Brinecombe_SaltWorks (brinecombe 5.3, 13 x 10, exact fit)",
        notes="The card's plan on Gen 4 pieces (its Zelda House set is not in the tree): the drying table is the counter "
              "x4-8 at y4 with three plate tiles for the heaps of salt (card x4-8, y4), the foreman at (6,3) behind it, "
              "talked to from (6,5) across (6,4); hearths (9-10,1-2) and (11-12,1-2) (card hearth (11,2)), the boiler "
              "stands in front of them at (10,3) (card (10,5)); salt jars (0,3-6) (card (1,3)-(1,6): at the edge so no "
              "dead corridor), barrels (12,5-6) are the card's jugs (card (10,3),(10,4), moved off the hearth fronts), "
              "the cabinet (11,5-6) is the sieve rack (card (11,6), bg event), stools (5,6) and (8,6) with a tea table "
              "between them (6-7,6-7) (the table is an extra: (6,5) and (7,5) stay free for the foreman's talk spot, and "
              "row 8 stays free to the door) and the raker at (3,6) are the card's tiles, crates (11-12,7-8) are sacks of "
              "salt. The card's two windows at x3 and x9 are (2-3) and (6-7), its shelf of bowls x2-4 is (0-1) and (4-5). "
              "Not as the card: no green mat, no timber and stone look.")


SPECS = [counter_office(), open_office(), front_hall(), reading_room(), archive(), workshop()]
