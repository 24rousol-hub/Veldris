"""Shared eatery and shop layouts of the 'shops' family: a cafe, a canteen, a counter shop and the League lounge floors.

Five layouts, each a different floor plan on the Gen 4 Interior set, reused by the buildings of the cards in
design/maps/detail/ that the `uses` of each spec name:

    CAFE        11 x 8   a counter on the back wall with the host in the aisle, small tables on stools, an armchair booth
    CANTEEN     13 x 10  a long serving counter, a tiled kitchen behind it, two big tables with six stools each
    SHOP        11 x 9   three shelves of jars, an L-shaped counter with the keeper's pocket behind it, two display tables
    LOUNGE_1F   31 x 12  the League lounge: a bar under jar shelves, a rug with low tables, a clerk's desk and a cloak counter
    LOUNGE_2F   31 x 12  the lounge terrace: nine tables in a three by three grid on a teal floor, stairs down

The Team Aqua 'Brick Cafe' set that the cafe, canteen and lounge cards ask for is not in the tree, so these are the Gen 4
fallbacks the cards allow. Marts, Pokemon Centers, the Pretty Petal flower shop and the Lavaridge herb shop keep their vanilla
layouts (the cards say so). The reading room with its archive, the salt works and the counter offices are built by the offices
family (fam_offices.py: READING, ARCHIVE, WORKSHOP, COUNTER), the same plans, so they are not repeated here.

Pieces come from the built Hollowbrook interiors (houses.py) and from the sibling families fam_homes.py (the wood room, the
stools, the rug, the door mat, the stairs, the armchairs, the barrel) and fam_houses.py (the dining table, the teal floor). A
piece carries a slice of the floor behind it, so every piece below was checked on the floor it stands on: the table legs and the
stools are drawn for wood, the stove, the fridge and the kitchen counter for tile, the barrel for the dark foot row of the back
wall, the low tables and their cushions for the blue rug, the teal table and cushion for the teal floor. Collision follows the
kit: furniture is solid; floor, rugs and stools are walkable (an NPC can sit on a stool or a cushion).

Counters: only the plate (641), cup (721) and return (624) tiles carry MB_COUNTER, so a keeper is talked to across those
tiles; every keeper spot below stands behind one of them. The plain ends (640, 643) and middle (642) have no behaviour.

Run `python3 layoutkit.py fam_shops OUT_DIR` from this folder to lint the specs and write the pictures.
"""
import houses as H
import layoutkit as K
import fam_homes as HM
import fam_houses as FH
from layoutkit import W_, Spec

# --- wall pieces (rows 1-2, two wide, a green base on the foot row) ----------------------------------------------------
JAR_SHELF = ((546, 547), (562, 563))       # open shelves of jars and tea tins; the top tiles carry MB_BOOKSHELF
CABINET = ((686, 687), (702, 703))         # blue-topped sideboard with an orange rail; the top tiles carry MB_BOOKSHELF

# --- counters: one tile high, floor-neutral ----------------------------------------------------------------------------
COUNTER_L, COUNTER_R = 640, 643            # the left and right ends of a run
COUNTER_PLATE, COUNTER_CUP = 641, 721      # middle tiles with a plate and with a cup; both carry MB_COUNTER
COUNTER_PLAIN = 642                        # plain middle tile
COUNTER_RETURN = 624                       # vertical piece that turns a run into an L (the kitchen L's left arm)
COUNTER_BACK = FH.COUNTER_WALL             # 617 wallpaper with the raised back edge of a wall counter (row 1)

# --- furniture ---------------------------------------------------------------------------------------------------------
SMALL_TABLE = HM.FOOTSTOOL                 # 808 one-tile framed table, solid; the only small table piece the set has
TEAL_TABLE = ((534, 535), (951, 952))      # the lab's aide desk: 2 x 2 with an orange top, teal floor behind its legs
TABLE = FH.DINING_TABLE                    # 534/535 over 564/565, 2 x 2 with an orange top, green floor behind its legs


def counter(g, x: int, y: int, middle) -> None:
    """A one-tile-high counter on row y: left end at x, then the `middle` tiles, then the right end. Solid."""
    for i, m in enumerate((COUNTER_L,) + tuple(middle) + (COUNTER_R,)):
        g[y, x + i] = W_ | m


def small_table(g, x: int, y: int) -> None:
    """A small table at (x, y) with a walkable stool on each side, (x-1, y) and (x+1, y)."""
    g[y, x] = W_ | SMALL_TABLE
    HM.stools(g, ((x - 1, y), (x + 1, y)))


def cafe() -> Spec:
    """CAFE 11 x 8, door mat (4,7)+(5,7). Back wall: clock (0), wall counter (1-4, row 2: left end, plate, cup, right end,
    with the raised back edge at both ends in row 1), tea urn on the foot row (5,2), window (6-7), jar shelf (8-9), picture
    (10) over a potted tree (10,2-3). Aisle row 3 is free: the host stands there. Small tables with a stool each side at
    (2,4), (7,4) and (2,6); a quiet booth at the right, a small table (9,5) between two armchairs (8,5-6) and (10,5-6);
    a potted tree (0,6-7)."""
    g = HM.room(11, 8)
    HM.high(g, 0, HM.CLOCK)
    counter(g, 1, 2, (COUNTER_PLATE, COUNTER_CUP))
    g[1, 1] = g[1, 4] = W_ | COUNTER_BACK
    g[2, 5] = W_ | HM.BARREL
    HM.high(g, 6, H.WINDOW)
    HM.on_wall(g, 8, JAR_SHELF)
    HM.high(g, 10, HM.PICTURE)
    K.put(g, 10, 2, HM.PLANT)
    for x, y in ((2, 4), (7, 4), (2, 6)):
        small_table(g, x, y)
    K.put(g, 8, 5, HM.ARMCHAIR_E)
    g[5, 9] = W_ | SMALL_TABLE
    K.put(g, 10, 5, HM.ARMCHAIR_W)
    K.put(g, 0, 6, HM.PLANT)
    return Spec(
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
              "booth. Not as the cards: no lamps, arched kitchen windows or checker floor (Brick Cafe), and the small "
              "tables are the footstool piece. Set behaviours in Porymap: jar shelf tops (546, 547) are MB_BOOKSHELF, so give "
              "(8,2) and (9,2) a sign facing any; barrel MB_FOOD_SMELLS_TASTY.")


def canteen() -> Spec:
    """CANTEEN 13 x 10, door mat (6,9)+(7,9). Back wall: fridge (0-1), stove (2-3), window (4-5) over a prep counter (4,2)+(5,2),
    jar shelf (6-7), tea urn on the foot row (8,2) under the window (8-9), clock (10), bookshelf (11-12). A tile kitchen floor
    covers x0-7 of rows 3-4: row 3 is the cook's pocket, the serving counter is row 4 (x0-6: left end, plain, cup, plate, cup,
    plain, right end), open at its east end (7,3)-(7,4). Counter stools (1,5) (3,5) (5,5). Two big tables (2-3,6-7) and
    (9-10,6-7), each with six stools; a small table (10,4) with a stool each side (9,4) (11,4); potted trees in both lower
    corners (0,8-9) and (12,8-9)."""
    g = HM.room(13, 10)
    K.fill(g, 0, 3, 8, 2, H.TILE)
    HM.on_wall(g, 0, H.FRIDGE)
    HM.on_wall(g, 2, H.STOVE)
    HM.high(g, 4, H.WINDOW)
    counter(g, 4, 2, ())
    HM.on_wall(g, 6, JAR_SHELF)
    g[2, 8] = W_ | HM.BARREL
    HM.high(g, 8, H.WINDOW)
    HM.high(g, 10, HM.CLOCK)
    HM.on_wall(g, 11, H.SHELF)
    counter(g, 0, 4, (COUNTER_PLAIN, COUNTER_CUP, COUNTER_PLATE, COUNTER_CUP, COUNTER_PLAIN))
    HM.stools(g, ((1, 5), (3, 5), (5, 5)))
    small_table(g, 10, 4)
    for x in (2, 9):
        K.put(g, x, 6, TABLE)
        HM.stools(g, ((x - 1, 6), (x - 1, 7), (x + 2, 6), (x + 2, 7), (x, 8), (x + 1, 8)))
    K.put(g, 0, 8, HM.PLANT)
    K.put(g, 12, 8, HM.PLANT)
    return Spec(
        "LAYOUT_VELDRIS_CANTEEN", "VeldrisCanteen", g, doors=HM.door_mat(g, 6),
        npc=((3, 3), (2, 3), (4, 3), (3, 5), (2, 5), (4, 5), (9, 5), (11, 3), (5, 5), (11, 6)),
        title="Canteen: long counter, tiled kitchen, two big tables",
        uses="Smeltham_Canteen (smeltham 3.6, 13 x 10); Kingsquay_QuaysideTeaRooms (kingsquay 6.12, card 13 x 9, so one row "
             "taller here)",
        notes="Smeltham's plan one row lower, because the Gen 4 stove stands on rows 1-2: the cook is at (3,3) (card (3,2)) in "
              "front of the stove, talked to from (3,5) across the cup and plate tiles (2-4,4), which carry MB_COUNTER; the "
              "stool (3,5) is the player's seat. The pocket is open at (7,3)-(7,4), so the cook is reachable. Workers on "
              "lunch (4,5) and (9,5) (card (4,4) and (9,4); the small table (10,4) with stools (9,4) (11,4) is a second "
              "seat for them); Kingsquay's barista is the cook at (2,3), its customers (5,5) "
              "and (11,6) (card (10,6) is a table here) and the ferry hand (11,3). The tea urn is the barrel (8,2) on the "
              "foot row, talked to from (8,3) (card (8,3)). Not as the cards: no mug block, lamps or arched kitchen "
              "windows (Brick Cafe), the kitchen is the houses' stove and fridge on tile, and the card's plant (11,3) "
              "moves to the lower corners so the shelf (11-12,2) stays reachable. Set behaviours in Porymap: jar shelf tops (546, 547) are "
              "MB_BOOKSHELF, give (6,2) and (7,2) a sign facing any; fridge MB_FOOD, stove MB_KITCHEN; barrel "
              "MB_FOOD_SMELLS_TASTY.")


def shop() -> Spec:
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
    g[3, 7] = W_ | COUNTER_RETURN
    HM.rug(g, 3, 5, 3, 2)
    K.put(g, 1, 6, TABLE)
    K.put(g, 8, 6, TABLE)
    return Spec(
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
              "(9-10,2), talked to from (9,3) or (10,3). Not as the cards: no flower pots (the tables take their place), "
              "and the Rest Hut's counter is longer. Set behaviours in Porymap: jar shelf and sideboard tops (546, 547, "
              "686, 687) are MB_BOOKSHELF, so give the bases (1-6,2) and (9-10,2) signs facing any, or set a cabinet "
              "behaviour; the counter ends and plain middle (640, 642, 643) have no MB_COUNTER, set it if a keeper should "
              "be reachable across them.")


def lounge_1f() -> Spec:
    """LOUNGE_1F 31 x 12, door mat (14,11)+(15,11). Back wall: clock (0), five jar shelves (2-11) over the bar, picture (12),
    four windows (14-15) (17-18) (20-21) (23-24), picture (26), stairs up (29-30, rows 0-3) whose walkable step (29,2) is the
    east-arrow warp (enter walking east from (28,2)). Bar: counter row 4 from x3 to x11 (cups, one plate at (7,4)), the
    bartender's pocket row 3 (open at both ends), four stools (4,5) (6,5) (8,5) (10,5). A blue rug x11-20, y5-8 with three
    low tables (14-15,6) (12-13,7) (16-17,7) and cushions (13,6) (16,6) (14,7) (15,7) (18,7), an armchair on each side (9,6-7)
    and (21,6-7). Window table (24-25,4-5) with a stool each side (23,4) (26,4). Two nooks: a small table (3,7) with a cushion
    (2,7), a small table (26,7) with a cushion (27,7). The League desk (8-10,9) and the cloak counter (19-22,9), staff row 10.
    Potted trees (1,9-10) and (29,9-10)."""
    g = HM.room(31, 12)
    HM.high(g, 0, HM.CLOCK)
    for x in range(2, 12, 2):
        HM.on_wall(g, x, JAR_SHELF)
    HM.high(g, 12, HM.PICTURE)
    for x in (14, 17, 20, 23):
        HM.high(g, x, H.WINDOW)
    HM.high(g, 26, HM.PICTURE)
    HM.stairs_up(g, 29)
    counter(g, 3, 4, (COUNTER_CUP, COUNTER_PLAIN, COUNTER_CUP, COUNTER_PLATE, COUNTER_CUP, COUNTER_PLAIN, COUNTER_CUP))
    HM.stools(g, ((4, 5), (6, 5), (8, 5), (10, 5)))
    HM.rug(g, 11, 5, 10, 4)
    K.put(g, 9, 6, HM.ARMCHAIR_E)
    K.put(g, 21, 6, HM.ARMCHAIR_W)
    for x, y in ((14, 6), (12, 7), (16, 7)):
        K.put(g, x, y, (HM.LOW_TABLE,))
    HM.stools(g, ((13, 6), (15, 7)), HM.CUSHION_BLUE[0])
    HM.stools(g, ((16, 6), (14, 7), (18, 7)), HM.CUSHION_BLUE[1])
    K.put(g, 24, 4, TABLE)
    HM.stools(g, ((23, 4), (26, 4)))
    g[7, 3] = g[7, 26] = W_ | SMALL_TABLE
    HM.stools(g, ((2, 7), (27, 7)))
    counter(g, 8, 9, (COUNTER_PLATE,))
    counter(g, 19, 9, (COUNTER_PLATE, COUNTER_CUP))
    K.put(g, 1, 9, HM.PLANT)
    K.put(g, 29, 9, HM.PLANT)
    return Spec(
        "LAYOUT_VELDRIS_LOUNGE_1F", "VeldrisLounge1F", g, doors=HM.door_mat(g, 14),
        npc=((7, 3), (7, 5), (23, 4), (13, 6), (2, 7), (27, 7), (9, 10), (9, 8), (20, 10), (20, 8)),
        title="League lounge, ground floor: a bar under jar shelves, a rug with low tables, a clerk's desk, a cloak counter",
        uses="Vesperhaven_LoungeFloor1 (vesperhaven 6.3, card 31 x 12)",
        notes="The card's plan on Gen 4 pieces, one row lower in the bar: the jar shelves fill rows 1-2, so the bartender is "
              "at (7,3) (card (7,2)) behind the plate tile of the counter (7,4) (card row 3), and the stools are on row 5 "
              "(card row 4). Everything below keeps the card's tiles: OSSIAN (2,7) on a cushion with the small table (3,7) "
              "(the card's black armchair; the two armchairs flank the rug instead); HYACINTH (23,4) on a stool at the "
              "window table; DRAYDEN (13,6) on a cushion left of the low table (14-15,6); DUNMORE (27,7) on a cushion by a "
              "small table (26,7); the clerk (9,10) behind the desk (8-10,9), the player at (9,8); TROGLODYTE (20,10) behind "
              "the cloak counter (19-22,9), the player at (20,8). The bartender can stand behind any cup or plate tile "
              "(4,3) (6,3) (7,3) (8,3) (10,3), the cloak clerk at (21,10) too. The pockets are open at their ends, so every "
              "staff tile is reachable. Stairs to 2F: the step (29,2) (tile 672, east-arrow warp; card (29,1)) goes to the "
              "2F step (29,2); the player arrives on it and walks west. Not as the card: no arched lit windows, brick wall "
              "or checker floor (Brick Cafe), no coat racks (the card's 'R' tiles by the cloak counter: put them as signs "
              "on the counter tiles, the staff row must stay open). Set behaviours in Porymap: jar shelf tops (546, 547) "
              "are MB_BOOKSHELF, so give the bases (2-11,2) signs facing any, or set a cabinet behaviour; barrels none.")


def lounge_2f() -> Spec:
    """LOUNGE_2F 31 x 12, teal floor, no door: the way in is the stairwell (28-29, rows 1-3) whose walkable step (29,2) is
    the west-arrow warp (enter walking west from (30,2)). Back wall: windows (4-5) (10-11) (16-17) (22-23) onto the pool,
    pictures (8) (14) (20), clock (26). Nine tables 2 x 2 at x5-6, x15-16, x25-26 and y3-4, y6-7, y9-10, each with the leader's
    cushion on its left at (x-1, y). Potted trees (1,9-10) and (29,9-10)."""
    g = K.blank(31, 12, FH.TEAL, H.WALLTOP, H.WALL, FH.TEAL_FOOT)
    for x in (4, 10, 16, 22):
        HM.high(g, x, H.WINDOW)
    for x in (8, 14, 20):
        HM.high(g, x, HM.PICTURE)
    HM.high(g, 26, HM.CLOCK)
    HM.stairs_down(g, 28)
    for x in (5, 15, 25):
        for y in (3, 6, 9):
            K.put(g, x, y, TEAL_TABLE)
            HM.stools(g, ((x - 1, y),), FH.TEAL_CUSHION)
    K.put(g, 1, 9, FH.TEAL_PLANT)
    K.put(g, 29, 9, FH.TEAL_PLANT)
    return Spec(
        "LAYOUT_VELDRIS_LOUNGE_2F", "VeldrisLounge2F", g, doors=((30, 3),),
        npc=((4, 3), (14, 3), (24, 3), (4, 6), (14, 6), (24, 6), (4, 9), (14, 9), (24, 9),
             (5, 2), (5, 5), (15, 5), (25, 5), (5, 8), (15, 8), (25, 8)),
        title="League lounge, terrace: nine tables in a three by three grid",
        uses="Vesperhaven_LoungeFloor2 (vesperhaven 6.4, card 31 x 12)",
        notes="The card's plan: nine tables, one gym leader each in gym order left to right and top to bottom, the leader on "
              "the cushion to the left of the table facing right ((4,3) GRETA, (14,3) HACHIMEL, (24,3) SANZUFORD, (4,6) "
              "HAGANE, (14,6) WAKASAGI, (24,6) TOBIN, (4,9) ASEBY, (14,9) SUZURAN, (24,9) MIZZLE: exactly the card's "
              "tiles), the player above or below a table ((5,2), (5,5), (5,8) and the same in x15 and x25). The tables are "
              "2 x 2 (the card draws 2 x 1), so each leader's table takes two rows. The floor is teal for the pool; the "
              "card's Brick Cafe vocabulary is not in the tree. The only way in is the stairs: the step (29,2) (tile 695, "
              "west-arrow warp; card (29,1)) goes to the 1F step (29,2); the player enters walking west from (30,2); the "
              "lint warning 'door (30,3) is not on the bottom row' is expected (no exit mat, as the Apiary's upper floor). "
              "Nine leader objects and nothing else, well under 15.")


SPECS = [cafe(), canteen(), shop(), lounge_1f(), lounge_2f()]
