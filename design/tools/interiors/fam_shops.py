"""Shared eatery and shop layouts of the 'shops' family: a cafe, a canteen and a counter shop.

Three layouts, each a different floor plan on the Gen 4 Interior set, reused by the buildings of the cards in
design/maps/detail/ that the `uses` of each spec name:

    CAFE        11 x 8   a counter on the back wall with the host in the aisle, small tables on stools, an armchair booth
    CANTEEN     13 x 10  a long serving counter, a tiled kitchen behind it, two big tables with six stools each
    SHOP        11 x 9   three shelves of jars, an L-shaped counter with the keeper's pocket behind it, two display tables

The Team Aqua 'Brick Cafe' set that the cafe and canteen cards ask for is not in the tree, so these are the Gen 4 fallbacks
the cards allow. Marts, Pokemon Centers, the Pretty Petal flower shop and the Lavaridge herb shop keep their vanilla
layouts (the cards say so). The reading room with its archive, the salt works and the counter offices are built by the offices
family (fam_offices.py: READING, ARCHIVE, WORKSHOP, COUNTER), and the League lounge of Vesperhaven (two floors) by the halls
family (fam_halls.py: HALL_LOUNGE_1F, HALL_LOUNGE_2F): the same plans, so they are not repeated here.

Pieces come from the built Hollowbrook interiors (houses.py) and from the sibling families fam_homes.py (the wood room, the
stools, the door mat, the armchairs, the barrel) and fam_houses.py (the dining table, the wall counter's raised back edge). A
piece carries a slice of the floor behind it, so every piece below was checked on the floor it stands on: the table legs and
the stools are drawn for wood, the stove, the fridge and the kitchen counter for tile, the barrel for the dark foot row of the
back wall, the rug for wood. Collision follows the kit: furniture is solid; floor, rugs and stools are walkable (an NPC can
sit on a stool).

Which tiles answer when the player talks to them (checked in the tileset attributes). Counters: only the plate (641), cup
(721) and return (624) tiles carry MB_COUNTER, so a keeper is talked to across those tiles; every keeper spot below stands
behind one of them. The plain ends (640, 643) and middle (642) have none. Jar shelves and the sideboard: the behaviour
MB_BOOKSHELF is on their TOP tiles (546, 547, 686, 687, wall row 1), which the player never faces; the base tiles (562, 563,
702, 703, wall row 2) carry none. So these shelves are silent until the author puts a sign (bg_event, facing any) on each base
tile. The bookshelf (H.SHELF) is different: its base tiles (953, 954) carry MB_BOOKSHELF and speak by themselves.

Run `python3 layoutkit.py fam_shops OUT_DIR` from this folder to lint the specs and write the pictures.
"""
import houses as H
import layoutkit as K
import fam_homes as HM
import fam_houses as FH

# --- wall pieces (rows 1-2, two wide, a green base on the foot row) ----------------------------------------------------
JAR_SHELF = ((546, 547), (562, 563))       # open shelves of jars and tea tins; no behaviour on the base (see docstring)
CABINET = ((686, 687), (702, 703))         # blue-topped sideboard with an orange rail; no behaviour on the base

# --- counters: one tile high, floor-neutral ----------------------------------------------------------------------------
COUNTER_L, COUNTER_R = 640, 643            # the left and right ends of a run
COUNTER_PLATE, COUNTER_CUP = 641, 721      # middle tiles with a plate and with a cup; both carry MB_COUNTER
COUNTER_PLAIN = 642                        # plain middle tile
COUNTER_RETURN = 624                       # vertical piece that turns a run into an L (the kitchen L's left arm)
COUNTER_BACK = FH.COUNTER_WALL             # 617 wallpaper with the raised back edge of a wall counter (row 1)

# --- furniture ---------------------------------------------------------------------------------------------------------
SMALL_TABLE = HM.FOOTSTOOL                 # 808 one-tile framed table, solid; the only small table piece the set has
TABLE = FH.DINING_TABLE                    # 534/535 over 564/565, 2 x 2 with an orange top, green floor behind its legs

# --- plan constants ----------------------------------------------------------------------------------------------------
KITCHEN_W = 6                              # canteen: the tile kitchen floor covers x0-5 of rows 3-4, as wide as the counter


def counter(g, x: int, y: int, middle, back_edges: bool = False) -> None:
    """A one-tile-high counter on row y: left end at x, then the `middle` tiles, then the right end. Solid. With
    `back_edges` the wall tiles above its two ends (row y-1) get the raised back edge, so a wall counter looks fitted."""
    run = (COUNTER_L,) + tuple(middle) + (COUNTER_R,)
    for i, m in enumerate(run):
        g[y, x + i] = K.W_ | m
    if back_edges:
        g[y - 1, x] = g[y - 1, x + len(run) - 1] = K.W_ | COUNTER_BACK


def small_table(g, x: int, y: int) -> None:
    """A small table at (x, y) with a walkable stool on each side, (x-1, y) and (x+1, y)."""
    g[y, x] = K.W_ | SMALL_TABLE
    HM.stools(g, ((x - 1, y), (x + 1, y)))


def cafe() -> K.Spec:
    """CAFE 11 x 8, door mat (4,7)+(5,7). Back wall: clock (0), wall counter (1-4, row 2: left end, plate, cup, right end,
    with the raised back edge at both ends in row 1), tea urn on the foot row (5,2), window (6-7), jar shelf (8-9), picture
    (10) over a potted tree (10,2-3). Aisle row 3 is free: the host stands there. Small tables with a stool each side at
    (2,4), (7,4) and (2,6); a quiet booth at the right, a small table (9,5) between two armchairs (8,5-6) and (10,5-6);
    a potted tree (0,6-7)."""
    g = HM.room(11, 8)
    HM.high(g, 0, HM.CLOCK)
    counter(g, 1, 2, (COUNTER_PLATE, COUNTER_CUP), back_edges=True)
    g[2, 5] = K.W_ | HM.BARREL
    HM.high(g, 6, H.WINDOW)
    HM.on_wall(g, 8, JAR_SHELF)
    HM.high(g, 10, HM.PICTURE)
    K.put(g, 10, 2, HM.PLANT)
    for x, y in ((2, 4), (7, 4), (2, 6)):
        small_table(g, x, y)
    K.put(g, 8, 5, HM.ARMCHAIR_E)
    g[5, 9] = K.W_ | SMALL_TABLE
    K.put(g, 10, 5, HM.ARMCHAIR_W)
    K.put(g, 0, 6, HM.PLANT)
    return K.Spec(
        "LAYOUT_VELDRIS_CAFE", "VeldrisCafe", g, doors=HM.door_mat(g, 4),
        npc=((3, 3), (2, 3), (4, 3), (6, 5), (7, 5), (9, 4), (9, 6), (7, 6)),
        title="Cafe: wall counter, small tables on stools, an armchair booth",
        uses="Gildhaven_Cafe (gildhaven 4.8); Waymeet_Cafe 'The Junction' (waymeet 4.3); Lingmoor_TeaRooms (lingmoor 4.3); "
             "all three cards say 11 x 8",
        notes="The cards' counter 'at cols 1-4, top left': the host or owner stands in the aisle in front of it, at (3,3) "
              "(Waymeet, Lingmoor) or (2,3) (Gildhaven), facing right and talked to from (4,3). Customers on the cards' "
              "free tiles: (6,5), (7,5) fisherman or customer, (9,4) hiker, (9,6) scone-eater; Gildhaven's (8,6) moves to "
              "(7,6) (an armchair stands on (8,6)). The stools (1,4) (3,4) (6,4) (8,4) (1,6) (3,6) are walkable, so a "
              "customer can sit. The tea urn (Waymeet) or kettle (Lingmoor) is the barrel (5,2), talked to from (5,3); "
              "the jar shelf (8-9,2) is the jars of dried heather. Three small tables plus the booth table are the "
              "four tables of the Gildhaven and Waymeet cards; Lingmoor's three small tables are the three away from the "
              "booth. Warps: the exit mat is (4,7)+(5,7), so the cards' warp tables change (Gildhaven says (5,8), outside "
              "this 11 x 8 room; Lingmoor says (2,7), plain floor here). Not as the cards: no lamps, arched kitchen "
              "windows or checker floor (Brick Cafe), and the small tables are the footstool piece. Porymap: the jar shelf "
              "has no behaviour on its base, so put a sign facing any on (8,2) and (9,2) to say jars and heather; barrel "
              "MB_FOOD_SMELLS_TASTY.")


def canteen() -> K.Spec:
    """CANTEEN 13 x 10, door mat (6,9)+(7,9). Back wall: fridge (0-1), stove (2-3), window (4-5) over a prep counter (4,2)+(5,2),
    jar shelf (6-7), tea urn on the foot row (8,2) under the window (8-9), clock (10), bookshelf (11-12). A tile kitchen floor
    covers x0-5 of rows 3-4: row 3 is the cook's pocket, the serving counter is row 4 (x0-5: left end, plain, cup, plate, cup,
    right end), and the pocket is open at its east end (6,3)-(7,4), on wood. Counter stools (1,5) (3,5) (5,5). Two big
    tables (2-3,6-7) and (9-10,6-7), each with six stools; a small table (10,4) with a stool each side (9,4) (11,4); potted
    trees in both lower corners (0,8-9) and (12,8-9)."""
    g = HM.room(13, 10)
    K.fill(g, 0, 3, KITCHEN_W, 2, H.TILE)
    HM.on_wall(g, 0, H.FRIDGE)
    HM.on_wall(g, 2, H.STOVE)
    HM.high(g, 4, H.WINDOW)
    counter(g, 4, 2, ())
    HM.on_wall(g, 6, JAR_SHELF)
    g[2, 8] = K.W_ | HM.BARREL
    HM.high(g, 8, H.WINDOW)
    HM.high(g, 10, HM.CLOCK)
    HM.on_wall(g, 11, H.SHELF)
    counter(g, 0, 4, (COUNTER_PLAIN, COUNTER_CUP, COUNTER_PLATE, COUNTER_CUP))
    HM.stools(g, ((1, 5), (3, 5), (5, 5)))
    small_table(g, 10, 4)
    for x in (2, 9):
        K.put(g, x, 6, TABLE)
        HM.stools(g, ((x - 1, 6), (x - 1, 7), (x + 2, 6), (x + 2, 7), (x, 8), (x + 1, 8)))
    K.put(g, 0, 8, HM.PLANT)
    K.put(g, 12, 8, HM.PLANT)
    return K.Spec(
        "LAYOUT_VELDRIS_CANTEEN", "VeldrisCanteen", g, doors=HM.door_mat(g, 6),
        npc=((3, 3), (2, 3), (4, 3), (3, 5), (2, 5), (4, 5), (9, 5), (11, 3), (5, 5), (11, 6)),
        title="Canteen: long counter, tiled kitchen, two big tables",
        uses="Smeltham_Canteen (smeltham 3.6, 13 x 10); Kingsquay_TeaRooms (the Quayside Tea Rooms, kingsquay 6.12, card "
             "13 x 9, so one row taller here)",
        notes="Smeltham's plan one row lower, because the Gen 4 stove stands on rows 1-2: the cook is at (3,3) (card (3,2)) in "
              "front of the stove, talked to from (3,5) across the cup and plate tiles (2-4,4), which carry MB_COUNTER; the "
              "stool (3,5) is the player's seat. The pocket is open at (6,3)-(7,4), so the cook is reachable. Workers on "
              "lunch (4,5) and (9,5) (card (4,4) and (9,4); the small table (10,4) with stools (9,4) (11,4) is a second "
              "seat for them); Kingsquay's barista is the cook at (2,3), its customers (5,5) "
              "and (11,6) (card (10,6) is a table here) and the ferry hand (11,3). The tea urn is the barrel (8,2) on the "
              "foot row, talked to from (8,3) (card (8,3)). Warps: the exit mat is (6,9)+(7,9) (Smeltham's card agrees); "
              "Kingsquay's card has a 13 x 9 room with mats (6,8),(7,8), so its warp table moves down a row, and its "
              "counter at the left becomes this long counter. Not as the cards: no mug block, lamps or arched kitchen "
              "windows (Brick Cafe), the kitchen is the houses' stove and fridge on tile, and the card's plant (11,3) "
              "moves to the lower corners so the shelf (11-12,2) stays reachable. The prep counter (4-5,2) sits straight "
              "under the window, which is why it has no raised back edge like the cafe's counter. The jar shelf base "
              "(6-7,2) is drawn on wood, so the tile kitchen ends at x5 to keep that seam out of the picture. Porymap: the "
              "jar shelf has no behaviour on its base, so put a sign facing any on (6,2) and (7,2); suggested behaviours: "
              "fridge MB_FOOD, stove MB_KITCHEN, barrel MB_FOOD_SMELLS_TASTY; the bookshelf (11-12,2) speaks on its own.")


def shop() -> K.Spec:
    """SHOP 11 x 9, door mat (5,8)+(6,8). Back wall: clock (0), three jar shelves (1-2) (3-4) (5-6), window (7-8, over the
    foot tiles (7,2) (8,2), which stay walkable), sideboard (9-10). L-shaped counter: row 4 from x2 to x7 (left end, plate,
    cup, plate, plain, right end) with a vertical return at (7,3); the keeper's pocket is row 3, x2-6, open to the left at
    (0-1,3-4). Customers' side: a blue rug (3-5,5-6) in front of the counter and a display table at (1-2,6-7) and (8-9,6-7)."""
    g = HM.room(11, 9)
    HM.high(g, 0, HM.CLOCK)
    for x in (1, 3, 5):
        HM.on_wall(g, x, JAR_SHELF)
    HM.high(g, 7, H.WINDOW)
    HM.on_wall(g, 9, CABINET)
    counter(g, 2, 4, (COUNTER_PLATE, COUNTER_CUP, COUNTER_PLATE, COUNTER_PLAIN))
    g[3, 7] = K.W_ | COUNTER_RETURN
    HM.rug(g, 3, 5, 3, 2)
    K.put(g, 1, 6, TABLE)
    K.put(g, 8, 6, TABLE)
    return K.Spec(
        "LAYOUT_VELDRIS_SHOP", "VeldrisShop", g, doors=HM.door_mat(g, 5),
        npc=((4, 3), (3, 3), (5, 3), (4, 5), (3, 5), (5, 5), (8, 5), (9, 3), (9, 4)),
        title="Shop: jar shelves, an L-shaped counter, display tables",
        uses="HemlockReach_StopperedAndSons (hemlock-reach 5.4, 11 x 9); Route15_RestHut (routes-east-detail 3.3, card 10 x 8: "
             "one tile wider and taller); HemlockReach_OldDispensary (5.3) if the author prefers the Gen 4 style to the "
             "vanilla herb shop (card 11 x 8: one row taller)",
        notes="Stoppered and Sons as its card draws it: jar shelves along the back wall, L-shaped counter x2-6 with a return "
              "at x7, keeper at (4,3) behind the cup tile (4,4), the player at (4,5); the son (8,5) and a customer by the "
              "right table. The keeper can stand at (3,3), (4,3) or (5,3), the tiles behind the plate, cup and plate; the "
              "return (7,3) is a counter too. The pocket is open on the left, so the keeper is reachable. The Rest Hut's "
              "keeper stands at (3,3) (card (3,2)); its FULL HEAL shelf (card (8,2)) is the sideboard (9,2); the display "
              "tables take the stools' place, put its two stools on (8,5) and (9,5). The Old Dispensary's clerk is "
              "(3,3), its customer (7,5) and its expert (9,3). The 'Antidote Cabinet' of the Stoppered card is the sideboard "
              "(9-10,2), talked to from (9,3) or (10,3). Warps: the exit mat is (5,8)+(6,8) (the Stoppered card has (5,8)); "
              "the Rest Hut's card has mat (4,7) in a 10 x 8 room, so its warp table changes. Not as the cards: no flower "
              "pots (the tables take their place), and the Rest Hut's counter is longer. Porymap: the jar shelves and "
              "the sideboard have no behaviour on their bases, so put a sign facing any on each base tile ((1-6,2) for the "
              "jars, (9,2) and (10,2) for the Antidote Cabinet); the counter ends and plain middle (640, 642, 643) have no "
              "MB_COUNTER, set it in the tileset editor if a keeper should be reachable across them.")


SPECS = [cafe(), canteen(), shop()]
