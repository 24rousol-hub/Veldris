"""Shared home layouts of the 'homes' family: the Gen 4 Interior dwellings that the six shared houses (H1 to H6) do not cover.

Eight layouts, each a different floor plan and each reused by several buildings (cards in design/maps/detail/):

    FLAT        10 x 8   one room: bed, chest of drawers, a blue rug with a footstool         (the cards' 'G4-B' one-room cottage)
    STUDY       12 x 9   shelves at both ends, a blue rug with a low table and cushions       (the cards' 'G4-C' study and lounge)
    LODGE       12 x 8   a hut cut in two by a partition wall: sleeping nook and hearth room
    PARLOUR     13 x 10  desk, stove and trophy shelves round a tea table and two armchairs   (Cynthia's cottage)
    INN         14 x 9   reception counter, lounge, a partitioned rooms corner with two beds
    APIARY_1F   12 x 9   honey counter, shelf, glass hive dais, stairs up in the top-right corner
    APIARY_2F   12 x 8   the keeper's room above it, stairwell down in the same corner
    PENTHOUSE   15 x 10  an oversized home: window wall, cook's island, huge rug and a sofa

Pieces are the ones in the built Hollowbrook interiors (houses.py names them) plus a few more from the same secondary
tileset (`gTileset_Gen4Interior`, primary `gTileset_Building`). Ids are map-block ids: secondary index + 512. Most pieces
carry their own floor colour (a cushion drawn for the blue carpet shows a blue box on wood), so every piece below was
checked on the floor it is used on. Collision follows the kit: furniture solid; floor, rugs and cushions walkable.

Doors are two plain mat tiles (`MAT`), not the three-tile mat of H1: the plain tile has no tiled floor drawn round it,
so it sits on wood (the Fennick lab uses the same tile on its teal floor). Put a warp on each tile or on the left one.

Run `python3 layoutkit.py fam_homes OUT_DIR` from this folder to lint and draw them.
"""
import numpy as np

import houses as H
import layoutkit as K
from layoutkit import F_, W_, Spec

# ---------------------------------------------------------------- pieces beyond houses.py (map-block ids)
CLOCK = ((545,), (553,))            # round wall clock, wall rows 0-1 (its top tile carries the red cap band of the wall)
PICTURE = ((532,), (540,))          # framed hill landscape, wall rows 0-1, 1 wide (same cap band)
STOVE_WOOD = (H.STOVE[0], (610, 611))   # the stove with its lower half drawn for wood instead of kitchen tile
CHEST = ((811,), (819,))            # chest of drawers or wardrobe, 1 wide 2 tall, against the wall
DESK = ((933, 919), (542, 927))     # writing desk with a computer and papers, 2 wide (Hollowbrook 2F's desk, on wood)
DINING_TABLE = ((534, 535), (542, 543))  # 2 x 2 table with an orange cloth, drawn for wood
FOOTSTOOL = 808                     # one-tile low table or ottoman, framed, so it sits on any floor
BARREL = 926                        # barrel with a white lid, drawn for the dark foot row at the foot of the back wall (row 2)
ARMCHAIR_E = ((937,), (945,))       # armchair seen from the side, facing east, 1 wide 2 tall, on wood
ARMCHAIR_W = ((938,), (946,))       # the same facing west
LOVESEAT = ((670, 671), (678, 679))  # two-seat sofa seen from behind (it faces north), 2 x 2, on wood
PLANT = ((H.PLANT[0],), (H.PLANT[1],))  # the Hollowbrook potted tree, 1 wide 2 tall, on wood
COUNTER_RUN = (640, 641, 642, 643)  # free-standing counter, 1 tall: left end, middle, middle with a bowl, right end
STOOL = H.CUSHION                   # cushion stool on wood (walkable, as in Hollowbrook)
STOOL_TILE = 607                    # the same stool drawn for tiled floor (Hollowbrook 1F kitchen)
LOW_TABLE = (593, 594)              # 2 x 1 low table, drawn for the blue carpet
CUSHION_BLUE = (597, 598)           # a left and a right cushion drawn for the blue carpet (walkable)
MAT = 513                           # plain door mat tile, behaviour south-arrow warp
RUG = ((569, 570, 571), (577, 578, 579), (585, 586, 587))   # blue carpet 3 x 3: corners and edges round a plain middle
PART_MID = 705                      # partition wall, middle tile: plain stripes that join the back wall
PART_END = H.WALL                   # partition wall, last tile: the wall tile carries the skirting board at its foot
DOME = ((838, 839), (846, 847), (854, 855))   # the lab's observation dome, 2 x 3, drawn on teal glass floor
GLASS = 737                         # teal glass floor, the dome's own floor
# Both staircases are copied block for block (collision and elevation included) from the built Hollowbrook house: their
# bottom step is the one walkable arrow-warp tile. Source of each block: (layout id, x, y, width, height).
STAIRS_UP_SRC = ("LAYOUT_HOLLOWBROOK_PLAYERS_HOUSE_1F", 11, 0, 2, 4)    # cap row, three stair rows; step (0,2) = 672, east-arrow warp
STAIRS_DOWN_SRC = ("LAYOUT_HOLLOWBROOK_PLAYERS_HOUSE_2F", 9, 1, 2, 3)   # stairwell rows; step (1,1) = 695, west-arrow warp


# ---------------------------------------------------------------- helpers for the builders
def room(w: int, h: int) -> np.ndarray:
    """Back wall (rows 0-2: cap and wall solid, walkable foot row) and green wood floor everywhere else."""
    return K.blank(w, h, H.WOOD, H.WALLTOP, H.WALL, H.WALLFOOT)


def on_wall(g: np.ndarray, x: int, piece) -> None:
    """A two-row piece standing against the back wall (rows 1-2); the floor in front of it stays free."""
    K.put(g, x, 1, piece)


def high(g: np.ndarray, x: int, piece) -> None:
    """A piece hung on the wall in rows 0-1 (window, clock, picture): both rows are wall already, the foot row 2 stays."""
    K.put(g, x, 0, piece)


def rug(g: np.ndarray, x: int, y: int, w: int, h: int) -> None:
    """Blue carpet w x h (both at least 2): the 3 x 3 rug with its plain middle column and row repeated."""
    for r in range(h):
        src = RUG[0 if r == 0 else 2 if r == h - 1 else 1]
        for c in range(w):
            g[y + r, x + c] = F_ | src[0 if c == 0 else 2 if c == w - 1 else 1]


def door_mat(g: np.ndarray, x: int) -> tuple:
    """Two plain mat tiles at (x, bottom) and (x+1, bottom); returns both as the door tiles."""
    y = g.shape[0] - 1
    g[y, x] = g[y, x + 1] = F_ | MAT
    return ((x, y), (x + 1, y))


def partition(g: np.ndarray, x: int, last: int) -> None:
    """A one-tile-wide wall stub that hangs from the back wall (row 2) down to row `last`, inclusive."""
    g[2:last, x] = W_ | PART_MID
    g[last, x] = W_ | PART_END


def stairs_up(g: np.ndarray, x: int) -> None:
    """The Hollowbrook 1F staircase in columns x and x+1, rows 0-3. Its walkable bottom step (x, 2) is the east-arrow
    warp, entered walking east from (x-1, 2)."""
    K.stamp(g, x, 0, K.grab(*STAIRS_UP_SRC))


def stairs_down(g: np.ndarray, x: int) -> None:
    """The Hollowbrook 2F stairwell in columns x and x+1, rows 1-3. Its walkable step (x+1, 2) is the west-arrow warp,
    entered walking west from (x+2, 2)."""
    K.stamp(g, x, 1, K.grab(*STAIRS_DOWN_SRC))


def stools(g: np.ndarray, cells, tile: int = STOOL) -> None:
    """Walkable cushion stools (the Hollowbrook cushions are walkable) at the given (x, y) cells."""
    for x, y in cells:
        g[y, x] = F_ | tile


# ---------------------------------------------------------------- the layouts
def flat() -> Spec:
    """Flat 10 x 8. Wall: bed (0-1), chest of drawers (2), window (3-4), clock (5), bookshelf (6-7), stove (8-9).
    Floor: blue rug x2-6 y4-6 with the footstool (4,5) in its centre, potted trees (9,5-6) and (0,6-7). Mat (3,7)+(4,7).
    The rest is free floor for people."""
    g = room(10, 8)
    on_wall(g, 0, H.BED)
    on_wall(g, 2, CHEST)
    high(g, 3, H.WINDOW)
    high(g, 5, CLOCK)
    on_wall(g, 6, H.SHELF)
    on_wall(g, 8, STOVE_WOOD)
    rug(g, 2, 4, 5, 3)
    g[5, 4] = W_ | FOOTSTOOL
    K.put(g, 9, 5, PLANT)
    K.put(g, 0, 6, PLANT)
    doors = door_mat(g, 3)
    return Spec(
        "LAYOUT_VELDRIS_FLAT", "VeldrisFlat", g, doors=doors,
        npc=((2, 3), (3, 4), (4, 4), (6, 4), (7, 3), (2, 5), (3, 5), (5, 5), (7, 5)),
        title="Flat: one room with a bed, a chest and a blue rug",
        uses="Gildhaven_CleanersFlat and Gildhaven_MoveDeletersHouse (gildhaven 4.8); Ebbsworth_NetMendersCottage and "
             "Ebbsworth_LockHouse (6.3, 6.7); Beaconmouth_DiversShed and Beaconmouth_ArtistsHouse (6.6, 6.8); "
             "Aldermere_StiltHouseB (6.4); Vesperhaven_Boathouse (6.6); Brinecombe_HouseB (5.6); "
             "Driftsands_LifeguardsHut and Driftsands_BeachcombersCottage (6.3, 6.4); Kingsquay_MoveRemindersHouse (6.8)",
        notes="The cards' G4-B one-room cottage, same 10 x 8. The people tiles listed are the free floor the cards use: "
              "(4,4) artist, lifeguard, mover, deleter; (3,5) and (5,5) menders, Gatsby, diver, beachcomber, stilt-house "
              "couple; (7,3) item ball or clerk; (6,4), (2,5), (2,3), (3,4), (7,5) the Cleaners', Brinecombe and stilt "
              "houses' spots. The footstool (4,5) is the card's low table (bg event for the logbook, boat model, tide "
              "table). Not as the cards: the stove stands on wood (no tiled kitchen floor, no counter), the clock (5,1) "
              "stands in for a tide table or barometer, the bookshelf (6-7,1-2) for the rod rack, paintings or first-aid "
              "shelf (put those bg events on its lower tiles (6,2) and (7,2), the tiles the player faces). The cards "
              "disagree on the mat tile ((2,7) Cleaners, (3,7) Move Deleter and G4-B): it is (3,7)+(4,7) here.")


def study() -> Spec:
    """Study 12 x 9. Wall: bookshelf (0-1), picture (2), window (3-4), double chest (5-6), TV (7-8), picture (9),
    bookshelf (10-11). Floor: blue rug x3-8 y4-6 with the low table (5-6,5) and cushions (4,5) and (7,5), potted trees
    (1,5-6) and (10,5-6). Mat (5,8)+(6,8)."""
    g = room(12, 9)
    on_wall(g, 0, H.SHELF)
    high(g, 2, PICTURE)
    high(g, 3, H.WINDOW)
    on_wall(g, 5, CHEST)
    on_wall(g, 6, CHEST)
    on_wall(g, 7, H.TV)
    high(g, 9, PICTURE)
    on_wall(g, 10, H.SHELF)
    rug(g, 3, 4, 6, 3)
    K.put(g, 5, 5, (LOW_TABLE,))
    g[5, 4] = F_ | CUSHION_BLUE[0]
    g[5, 7] = F_ | CUSHION_BLUE[1]
    K.put(g, 1, 5, PLANT)
    K.put(g, 10, 5, PLANT)
    doors = door_mat(g, 5)
    return Spec(
        "LAYOUT_VELDRIS_STUDY", "VeldrisStudy", g, doors=doors,
        npc=((2, 4), (8, 3), (7, 4), (3, 5), (4, 5), (8, 5), (9, 6), (9, 7), (10, 7)),
        title="Study and lounge: shelves at both ends, a rug with a low table",
        uses="Beaconmouth_KeepersCottage (beaconmouth 6.4); Aldermere_FossilScholarsCottage (6.3); "
             "Beaconmouth_LamplightersLodge (6.7); Ebbsworth_OldCaptainsHouse (6.4); Vesperhaven_House2 (6.8); "
             "HemlockReach_House2 (5.7); PrimroseVale_HouseB (5.5); Driftsands_House2 (6.5); Kingsquay_PilotsHouse (6.11)",
        notes="The cards' G4-C study and lounge, same 12 x 9, mat (5,8)+(6,8). Free floor for the card tiles: (8,5) "
              "captain, chief, widow, pilot, wife; (7,4) scholar; (3,5) widow and Slowbro; (4,5) husband; (2,4) mum; "
              "(8,3), (9,6), (9,7), (10,7) pets, child and item balls. The low table (5-6,5) takes the model ship, "
              "ferry model or tea bg events. Not as the cards: the TV and the double chest stay (there is no ship's wheel "
              "or fossil case: read the shelves, chest or TV as display cases, charts or lamps in their signs); an item "
              "ball the cards put on a shelf tile ((10,2)) goes on the floor in front, (10,3) or (9,3).")


def lodge() -> Spec:
    """Lodge 12 x 8, a hut cut in two. Left room (x0-3): beds (0-1) and (2-3), chest of drawers (0,4-5). A partition
    hangs from the back wall at x4 down to row 5 (cap at (4,5)). Hearth room (x5-11): window (5-6), clock (7), stove
    (8-9), bookshelf (10-11), dining table (7-8,4-5) with four stools (6,4) (6,5) (9,4) (9,5), potted tree (11,5-6).
    Rows 6-7 are open across both rooms. Mat (2,7)+(3,7)."""
    g = room(12, 8)
    on_wall(g, 0, H.BED)
    on_wall(g, 2, H.BED)
    partition(g, 4, 5)
    high(g, 5, H.WINDOW)
    high(g, 7, CLOCK)
    on_wall(g, 8, STOVE_WOOD)
    on_wall(g, 10, H.SHELF)
    K.put(g, 0, 4, CHEST)
    K.put(g, 7, 4, DINING_TABLE)
    stools(g, ((6, 4), (6, 5), (9, 4), (9, 5)))
    K.put(g, 11, 5, PLANT)
    doors = door_mat(g, 2)
    return Spec(
        "LAYOUT_VELDRIS_LODGE", "VeldrisLodge", g, doors=doors,
        npc=((5, 3), (5, 4), (8, 3), (3, 5), (6, 6)),
        title="Lodge: a hut with a sleeping nook behind a partition",
        uses="Hoarfell_HouseA (hoarfell 3.4); Mothwood_WardensLodge (landmarks-west); Route4_MarshkeepersLodge "
             "(routes-west-b); HemlockReach_Boathouse (5.8, same 12 x 8); Cragdale_ClimbersLodge (4.4); also usable for "
             "VeldrisRoute8_RestHouse and Lingmoor_PeatShed",
        notes="No card draws this plan: it is the Warden's lodge idea (two beds, hearth, plank table) as a two-room hut, "
              "one tile wider than the 11 x 8 cards, the same size as the Hemlock boathouse. Free floor for the cards' "
              "spots: (5,3) warden and marshkeeper, (5,4) the hut boy and dock hand, (8,3) lodge elder, (3,5) member, "
              "(6,6) young climber. The stove is the hearth (bg event for the kettle or thermos), the dining table is "
              "the plank table, the beds read as bunks in the boathouse. The partition is a plain wall stub (no door "
              "frame): the nook is open along rows 6-7.")


def parlour() -> Spec:
    """Parlour 13 x 10. Wall: desk (0-1), picture (2), window (3-4), clock (5), stove (6-7), bookshelves (8-9) and
    (10-11); (12,2) stays plain floor. Tea table (5-6,5-6) between armchairs (4,5-6) and (7,5-6), stools (5,7) (6,7),
    potted trees (1,5-6) and (11,5-6). Mat (5,9)+(6,9)."""
    g = room(13, 10)
    on_wall(g, 0, DESK)
    high(g, 2, PICTURE)
    high(g, 3, H.WINDOW)
    high(g, 5, CLOCK)
    on_wall(g, 6, STOVE_WOOD)
    on_wall(g, 8, H.SHELF)
    on_wall(g, 10, H.SHELF)
    K.put(g, 5, 5, DINING_TABLE)
    K.put(g, 4, 5, ARMCHAIR_E)
    K.put(g, 7, 5, ARMCHAIR_W)
    stools(g, ((5, 7), (6, 7)))
    K.put(g, 1, 5, PLANT)
    K.put(g, 11, 5, PLANT)
    doors = door_mat(g, 5)
    return Spec(
        "LAYOUT_VELDRIS_PARLOUR", "VeldrisParlour", g, doors=doors,
        npc=((9, 5), (8, 5), (12, 2), (0, 3), (6, 3)),
        title="Parlour: desk, stove and trophy shelves round a tea table",
        uses="Vesperhaven_CynthiasCottage (vesperhaven 6.5). Layout only; the 13 x 10 footprint is also the Smeltham "
             "canteen's and Brinecombe harbour office's, which belong to other families",
        notes="Cynthia's cottage as the card draws it, minus the carpet (the armchairs are drawn for wood): stationery "
              "desk (0-1,1-2, bg event (0,1)), window, stove with the kettle (6-7), trophy shelves (8-11), tea table "
              "with an armchair each side. Cynthia stands at (9,5), the player talks from (8,5); the Sea Incense appears "
              "on the plain foot tile (12,2). Front tiles of the desk, stove and shelves are free floor.")


def inn() -> Spec:
    """Inn 14 x 9. Reception: window (1-2), clock (4), counter x1-4 at y3 with the keeper's pocket behind it (row 2, x0-5),
    potted tree (0,3-4) sealing the left end, stools (2,4) and (4,4). Lounge: TV (6-7), flower table (6-7,4-6),
    cushions (5,5) and (8,5). Rooms corner behind a partition at x8 (rows 2-4): bed (9-10), chest (11), bed (12-13),
    dining table (10-11,5-6) with stools (9,5) (9,6) (12,5) (12,6), potted tree (13,7-8). Mat (6,8)+(7,8)."""
    g = room(14, 9)
    high(g, 1, H.WINDOW)
    high(g, 4, CLOCK)
    for i, m in enumerate(COUNTER_RUN):
        g[3, 1 + i] = W_ | m
    K.put(g, 0, 3, PLANT)
    stools(g, ((2, 4), (4, 4)))
    on_wall(g, 6, H.TV)
    K.put(g, 6, 4, H.TABLE)
    stools(g, ((5, 5), (8, 5)))
    partition(g, 8, 4)
    on_wall(g, 9, H.BED)
    on_wall(g, 11, CHEST)
    on_wall(g, 12, H.BED)
    K.put(g, 10, 5, DINING_TABLE)
    stools(g, ((9, 5), (9, 6), (12, 5), (12, 6)))
    K.put(g, 13, 7, PLANT)
    doors = door_mat(g, 6)
    return Spec(
        "LAYOUT_VELDRIS_INN", "VeldrisInn", g, doors=doors,
        npc=((3, 2), (3, 4), (2, 4), (4, 4), (5, 5), (8, 5), (11, 3)),
        title="Inn: reception, lounge and a rooms corner with two beds",
        uses="Wendlebury_Inn (wendlebury 3.5). Can stand in for Cragdale_Hostel (cragdale 4.3) and Gildhaven_Hotel_1F "
             "(gildhaven 4.5): their cards say 12 x 9 with the vanilla motel geometry, so that is the author's call",
        notes="Wendlebury's card plan at its own 14 x 9, mat (6,8). The keeper (3,2) stands behind the counter; the "
              "player talks from (3,4) between the two stools. The pocket is open at its right end ((5,2)-(5,3)) so it "
              "is reachable and never sealed. The beds flank a chest of drawers, as a bedside table. Beds are scenery "
              "(the Inn does not heal). The kitchen of the card is dropped (stove and fridge would hide the keeper's "
              "pocket); the counter is the kitchen counter, there is no bell or key board.")


def apiary_1f() -> Spec:
    """Apiary ground floor 12 x 9. Wall: bookshelf (0-1), window (2-3), clock (5), barrels (7,2) (8,2) on the foot row,
    staircase (10-11, rows 0-3) whose walkable bottom step (10,2) is the east-arrow warp (enter walking east from
    (9,2)). Honey counter x2-5 at y3, Wilf's pocket behind it (row 2, x2-6), open at (6,2)-(6,3). Glass dais x6-9 y3-7
    carrying the hive dome (7-8,4-6). Rug x2-5 y5-6, potted tree (11,5-6). Mat (5,8)+(6,8)."""
    g = room(12, 9)
    on_wall(g, 0, H.SHELF)
    high(g, 2, H.WINDOW)
    high(g, 5, CLOCK)
    stairs_up(g, 10)
    for i, m in enumerate(COUNTER_RUN):
        g[3, 2 + i] = W_ | m
    g[3:8, 6:10] = F_ | GLASS
    K.put(g, 7, 4, DOME)
    rug(g, 2, 5, 4, 2)
    g[2, 7] = g[2, 8] = W_ | BARREL
    K.put(g, 11, 5, PLANT)
    doors = door_mat(g, 5)
    return Spec(
        "LAYOUT_VELDRIS_APIARY_1F", "VeldrisApiary1F", g, doors=doors,
        npc=((3, 2), (3, 4), (9, 5), (9, 6), (9, 2)),
        title="Apiary, ground floor: honey counter, glass hive dais, stairs up",
        uses="Briarwick_Apiary_1F (briarwick 3.4)",
        notes="The card's plan with the hive dome (the lab's dome machine, there is no honey-gold recolour) moved off the "
              "wall to the middle of a glass dais: the dome's art has teal corners, so it must stand on teal floor and "
              "cannot touch the wall. Wilf (3,2) is behind the honey counter, talked to from (3,4); the card's two "
              "Combee (8,5) and (9,6) become (9,5) and (9,6) on the dais edge. Stairs up: the walkable step (10,2) "
              "(tile 672, east-arrow warp) goes to Briarwick_Apiary_2F (10,2); arrive back on (9,2). Honey barrels "
              "stand on the foot row at (7,2), (8,2).")


def apiary_2f() -> Spec:
    """Apiary upper floor 12 x 8. Wall: trophy shelf (1-2), windows (3-4) and (5-6), bookshelf (7-8), stairwell (9-10, rows
    1-3) whose walkable step (10,2) is the west-arrow warp (enter walking west from (11,2)). Floor: table (4-5,4-5) with
    cushion stools (3,5) and (6,5), potted trees (1,5-6) and (10,5-6). There is no door on this floor."""
    g = room(12, 8)
    on_wall(g, 1, H.SHELF)
    high(g, 3, H.WINDOW)
    high(g, 5, H.WINDOW)
    on_wall(g, 7, H.SHELF)
    stairs_down(g, 9)
    K.put(g, 4, 4, DINING_TABLE)
    stools(g, ((3, 5), (6, 5)))
    K.put(g, 10, 5, PLANT)
    K.put(g, 1, 5, PLANT)
    return Spec(
        "LAYOUT_VELDRIS_APIARY_2F", "VeldrisApiary2F", g, doors=((11, 3),),
        npc=((5, 3), (8, 5), (11, 2)),
        title="Apiary, upper floor: the old keeper's room",
        uses="Briarwick_Apiary_2F (briarwick 3.4)",
        notes="Reached only by the stairs: the walkable step (10,2) (tile 695, west-arrow warp) leads back to "
              "Briarwick_Apiary_1F (10,2); the player arrives on (11,2). The kit has no stairs-only floor, so the one "
              "door entry is the landing (11,3) and the lint warns 'not on the bottom row': expected, there is no "
              "exit mat. The old keeper stands at (5,3), Combee at (8,5). The trophy cabinet is the left shelf, the "
              "card's bookshelf the right one (bg events on their lower tiles).")


def penthouse() -> Spec:
    """Penthouse 15 x 10, a home that is slightly too big. Wall: stove (0-1), fridge (2-3), windows (4-5) and (6-7),
    picture (8), window (9-10), bookshelf (11-12), chest (13). Tiled kitchen x0-4 y3-6 with a counter island x1-4 at y5
    and stools (1,6) and (3,6). Lounge: rug x6-11 y3-5 with the low table (8-9,4) and cushions (7,4) and (10,4); a
    sofa of two loveseats (6-9,6-7) facing the windows; armchairs (11,7-8) and (13,7-8) round a footstool (12,8);
    potted trees (14,4-5) and (0,7-8). Mat (2,9)+(3,9); the floor tile (1,8) is the private stair door."""
    g = room(15, 10)
    g[3:7, 0:5] = F_ | H.TILE
    on_wall(g, 0, H.STOVE)
    on_wall(g, 2, H.FRIDGE)
    high(g, 4, H.WINDOW)
    high(g, 6, H.WINDOW)
    high(g, 8, PICTURE)
    high(g, 9, H.WINDOW)
    on_wall(g, 11, H.SHELF)
    on_wall(g, 13, CHEST)
    for i, m in enumerate(COUNTER_RUN):
        g[5, 1 + i] = W_ | m
    stools(g, ((1, 6), (3, 6)), STOOL_TILE)
    rug(g, 6, 3, 6, 3)
    K.put(g, 8, 4, (LOW_TABLE,))
    g[4, 7] = F_ | CUSHION_BLUE[0]
    g[4, 10] = F_ | CUSHION_BLUE[1]
    K.put(g, 6, 6, LOVESEAT)
    K.put(g, 8, 6, LOVESEAT)
    K.put(g, 11, 7, ARMCHAIR_E)
    K.put(g, 13, 7, ARMCHAIR_W)
    g[8, 12] = W_ | FOOTSTOOL
    K.put(g, 14, 4, PLANT)
    K.put(g, 0, 7, PLANT)
    doors = door_mat(g, 2)
    return Spec(
        "LAYOUT_VELDRIS_PENTHOUSE", "VeldrisPenthouse", g, doors=doors,
        npc=((3, 3), (10, 6), (5, 7), (5, 6), (1, 8)),
        title="Penthouse: an oversized home with a window wall",
        uses="Gildhaven_GoldsworthTower_6F (gildhaven 4.4.6). Layout only, no story content",
        notes="The card's plan: window wall, cook's counter nobody uses (the island), photo shelf (11-12) and locked "
              "cabinet (13), a rug and sofa too big for the room. People tiles: housemaid (3,3), Mr. (10,6), Mrs. (5,7). "
              "The card's Troglodyte tile (7,7) is under the sofa: use (5,6). The framed list is the picture (8,0-1) "
              "(sign on (8,2)); the photo shelf's sign goes on (12,2), the cabinet's on (13,2). The private stair door "
              "(1,8) is a plain floor tile (no door or stair art fits a south room): put its warp there next to the "
              "exit mat.")


SPECS = [flat(), study(), lodge(), parlour(), inn(), apiary_1f(), apiary_2f(), penthouse()]
