"""Shared one-floor house layouts H2 (kitchen house), H4 (studio) and H6 (big house) on the Gen 4 Interior set.

The plans are in design/maps/interiors/house-layouts.md. H1 and H5 (houses.py) and H3 (the built Hollowbrook neighbour)
are the other three plans, so with these there are six distinct single-floor houses.

Every id below is a secondary metatile id (512 + index): the Building primary set has only 8 metatiles and indoor walls and
floors come from the secondary set. A furniture piece carries a slice of the floor behind it, so it only looks right on the
floor it was drawn for. H2 uses the Hollowbrook look (pale kitchen TILE beside green WOOD); H4 and H6 use the TEAL floor of
the Hollowbrook lab with the blue carpet. Pieces that already stand in a built Hollowbrook layout keep their ids and their
collision and elevation bits (houses.py names them).

Block words are never masked: floor = F_ | id (walkable, elevation 3), solid = W_ | id (collision 1, elevation 0).
Run `python3 layoutkit.py fam_houses OUT_DIR` to lint the specs and write the pictures.
"""
import houses as H
import layoutkit as K
from layoutkit import F_

# --- the back wall (rows 0-2: red trim, striped wallpaper, wall foot), the same on every floor --------------------
WALL_TRIM, WALL_PAPER = H.WALLTOP, H.WALL            # 518, 526
WINDOW = H.WINDOW                                    # 548/549 over 556/557: rows 0-1, two wide, the wall foot stays below
CLOCK = ((545,), (553,))                             # round wall clock, rows 0-1, one wide
SHELF_TOP = (538, 539)                               # bookshelf top; the base row depends on the floor
DOOR_MAT = 513                                       # the mat tile that carries the south-arrow warp

# --- H2: the pale TILE kitchen floor (x0-5) and the green WOOD side (x6-9) -----------------------------------------
TILE, FRIDGE = H.TILE, H.FRIDGE                      # 520; 936/940 over 944/948 (tile behind the base)
STOVE_WINDOW = (WINDOW[0], (712, 713), (608, 609))   # stove under an arched window, rows 0-2; tile behind the base
COUNTER_WALL = 617                                   # wallpaper with the back edge of a counter, row 1 of a wall counter
COUNTER_L, COUNTER_MID, COUNTER_R = 640, 641, 643    # blue counter, one tile high: left end, middle with a plate (a counter
                                                     # tile), right end. Not 625/626: their corners hold green floor pixels
STOOL = 607                                          # round stool on tile floor (solid, as in the Hollowbrook kitchen)
POT = 648                                            # red pot on tile floor
TILE_MAT_ENDS = (H.MAT[0], H.MAT[2])                 # door mat ends with tile behind them (536, 537)
DINING_TABLE = ((534, 535), (564, 565))              # plain 2 x 2 table, green floor behind its legs
GREEN_PLANT = ((H.PLANT[0],), (H.PLANT[1],))         # potted tree, 582 over 590

# --- H4 and H6: the TEAL floor -------------------------------------------------------------------------------------
TEAL, TEAL_FOOT = 737, 738                           # floor, and the darker row under the wallpaper
TEAL_SHELF = (SHELF_TOP, (949, 950))                 # bookshelf with teal behind its base
TEAL_TV = ((912, 913),)                              # wall-hung flat TV, one row high (the only TV drawn for teal)
TEAL_SOFA = ((884, 885), (892, 893))                 # two-seat brown sofa, 2 x 2; teal behind its top row, so never on the wall
TEAL_PLANT = ((739,), (747,))                        # potted tree
TEAL_URN = 746                                       # big orange urn, one tile
TEAL_CUSHION = 743                                   # seat, walkable
TEAL_MAT_ENDS = (741, 742)                           # door mat ends with teal behind them
DESK = ((933, 919), (934, 935))                      # writing desk with a monitor and a notebook, rows 1-2 of the wall

# --- blue carpet: 3 x 3 pieces that stretch to any rug of two or more rows and columns, and what stands on it -----
CARPET = ((569, 570, 571),
          (577, 578, 579),
          (585, 586, 587))
VASE = (595, 596)                                    # flowers in a vase; its top pixel rows are the rug's top border
LOW_TABLE = (593, 594)                               # low table, 2 x 1, carpet behind its legs


def put_mat(g, x: int, ends: tuple, tiles: int = 1) -> None:
    """Door mat on the bottom row: an end piece, `tiles` warp tiles (the first at x), an end piece."""
    row = (ends[0],) + (DOOR_MAT,) * tiles + (ends[1],)
    for i, m in enumerate(row):
        g[g.shape[0] - 1, x - 1 + i] = F_ | m


def put_rug(g, x: int, y: int, w: int, h: int) -> None:
    """Blue carpet, w x h tiles (both at least 2), walkable."""
    for j in range(h):
        for i in range(w):
            row = 0 if j == 0 else (2 if j == h - 1 else 1)
            col = 0 if i == 0 else (2 if i == w - 1 else 1)
            g[y + j, x + i] = F_ | CARPET[row][col]


def put_flower_table(g, x: int, rug_top: int) -> None:
    """Low table with a vase of flowers at the top edge of a rug whose first row is `rug_top`: the vase takes the rug's
    border row (its own top pixels are that border), the table the row under it. Solid, two wide."""
    K.put(g, x, rug_top, (VASE, LOW_TABLE))


def put_seat(g, x: int, y: int, cushion: int) -> None:
    """A walkable cushion, as in the Hollowbrook houses."""
    K.put(g, x, y, ((cushion,),), solid=False)


def kitchen_house() -> K.Spec:
    """H2 Kitchen house 10 x 8, door mat (1,7). Back wall: fridge (0-1), counter (2-3), stove under a window (4-5),
    bookshelf (6-7), TV (8-9). Tile kitchen floor x0-5, green wood x6-9. Breakfast counter (2-4,5) with a stool at each end
    (2,6) and (4,6) and a pot at (5,6). Green side: a dining table (7-8,4-5) with a cushion on each of its four sides
    and a potted tree in the lower right corner (9,6-7)."""
    g = K.blank(10, 8, H.WOOD, WALL_TRIM, WALL_PAPER, H.WALLFOOT)
    K.fill(g, 0, 3, 6, 5, TILE)                                  # kitchen floor under the fridge, counter and stove
    K.put(g, 0, 1, FRIDGE)
    K.put(g, 2, 1, ((COUNTER_WALL, COUNTER_WALL), (COUNTER_L, COUNTER_R)))
    K.put(g, 4, 0, STOVE_WINDOW)
    K.put(g, 6, 1, H.SHELF)
    K.put(g, 8, 1, H.TV)
    K.put(g, 2, 5, ((COUNTER_L, COUNTER_MID, COUNTER_R),))       # breakfast counter; the plate tile is a counter tile
    K.put(g, 2, 6, ((STOOL,),))
    K.put(g, 4, 6, ((STOOL,),))                                  # (3,6) between the stools faces the counter
    K.put(g, 5, 6, ((POT,),))
    K.put(g, 7, 4, DINING_TABLE)
    for x, y in ((6, 5), (9, 5), (7, 6), (8, 6)):
        put_seat(g, x, y, H.CUSHION)
    K.put(g, 9, 6, GREEN_PLANT)
    put_mat(g, 1, TILE_MAT_ENDS)
    return K.Spec(
        "LAYOUT_VELDRIS_HOUSE_KITCHEN", "VeldrisHouse_Kitchen", g, doors=((1, 7),),
        npc=((4, 3), (3, 4), (6, 5), (8, 7)),
        title="H2 Kitchen house, 10 x 8",
        uses="Briarwick_HouseA and Wendlebury_House1 (their cards are 10 x 8, exact fit); family kitchen-and-lounge houses "
             "of the 11 x 8 cards: Smeltham_HouseA, Gloomsby_HouseA, Gildhaven_NavigatorsHouse, Brinecombe_HouseA",
        notes="Cook at the stove (4,3) facing up; a second person behind the breakfast counter (3,4): the plate tile "
              "(3,5) already has the counter behaviour, so the player talks across it from (3,6) between the stools. "
              "Someone on a dining cushion (6,5), a pet or child at (8,7). Bookshelf signs (6,2) and (7,2), TV signs "
              "(8,2) and (9,2). Set behaviours in Porymap: fridge MB_FOOD, stove and counters MB_KITCHEN. "
              "Card asked for two bookshelves: the 10-wide wall holds fridge, counter, stove, shelf and TV, so one.")


def studio() -> K.Spec:
    """H4 Studio 10 x 9, a two-tile door mat at (4,8) and (5,8) so it sits exactly in the middle. Symmetrical back wall:
    bookshelves (0-1) and (8-9), windows (2-3) and (6-7), writing desk (4-5). A 6 x 3 blue rug (2-7,4-6) carries the hobby
    table with its vase (4-5,4-5); a cushion each side of the rug (1,4) and (8,4); a potted tree in each lower corner
    (0,6-7) and (9,6-7)."""
    g = K.blank(10, 9, TEAL, WALL_TRIM, WALL_PAPER, TEAL_FOOT)
    K.put(g, 0, 1, TEAL_SHELF)
    K.put(g, 8, 1, TEAL_SHELF)
    K.put(g, 2, 0, WINDOW)
    K.put(g, 6, 0, WINDOW)
    K.put(g, 4, 1, DESK)
    put_rug(g, 2, 4, 6, 3)
    put_flower_table(g, 4, 4)
    put_seat(g, 1, 4, TEAL_CUSHION)
    put_seat(g, 8, 4, TEAL_CUSHION)
    K.put(g, 0, 6, TEAL_PLANT)
    K.put(g, 9, 6, TEAL_PLANT)
    put_mat(g, 4, TEAL_MAT_ENDS, tiles=2)
    return K.Spec(
        "LAYOUT_VELDRIS_HOUSE_STUDIO", "VeldrisHouse_Studio", g, doors=((4, 8), (5, 8)),
        npc=((3, 5), (6, 5), (4, 6), (5, 6), (3, 3), (6, 3)),
        title="H4 Studio, 10 x 9",
        uses="Workshop and collector houses: Smeltham_HouseC (scrap collector), Gloomsby_HouseB (story collector), "
             "Briarwick_HouseB (Tansy's trophy shelf), Lingmoor_HouseA (weaver), Cragdale_HouseA (quarryman); the H4 slots "
             "of the rotation rule in Gildhaven, Ebbsworth and Beaconmouth (the 12 x 9 study houses belong to the homes family)",
        notes="Both mat tiles (4,8) and (5,8) are warps to the same door: the mat is four pieces wide so it is centred. "
              "The rug is clear around the table: a collector or crafter at (3,5) or (6,5), a visitor at (4,6) or (5,6). "
              "The desk monitor (933) is the Hollowbrook bedroom-PC tile: here it is a prop unless a sign runs the PC "
              "script. Shelf bases 949/950 already carry the bookshelf behaviour.")


def big_house() -> K.Spec:
    """H6 Big house 13 x 9, door mat (6,8), symmetrical about column 6. Back wall: bookshelf (0-1), window (2-3), TV (4-5),
    clock (6), writing desk (7-8), window (9-10), bookshelf (11-12). A 7 x 3 blue rug (3-9,4-6) with a flower table each
    side of the centre aisle (4-5,4-5) and (7-8,4-5); a sofa at each end (0-1,4-5) and (11-12,4-5); a potted tree under
    each sofa (0,6-7) and (12,6-7); an urn each side of the door mat (4,8) and (8,8)."""
    g = K.blank(13, 9, TEAL, WALL_TRIM, WALL_PAPER, TEAL_FOOT)
    K.put(g, 0, 1, TEAL_SHELF)
    K.put(g, 11, 1, TEAL_SHELF)
    K.put(g, 2, 0, WINDOW)
    K.put(g, 9, 0, WINDOW)
    K.put(g, 4, 1, TEAL_TV)
    K.put(g, 6, 0, CLOCK)
    K.put(g, 7, 1, DESK)
    put_rug(g, 3, 4, 7, 3)
    put_flower_table(g, 4, 4)
    put_flower_table(g, 7, 4)
    K.put(g, 0, 4, TEAL_SOFA)
    K.put(g, 11, 4, TEAL_SOFA)
    K.put(g, 0, 6, TEAL_PLANT)
    K.put(g, 12, 6, TEAL_PLANT)
    K.put(g, 4, 8, ((TEAL_URN,),))
    K.put(g, 8, 8, ((TEAL_URN,),))
    put_mat(g, 6, TEAL_MAT_ENDS)
    return K.Spec(
        "LAYOUT_VELDRIS_HOUSE_BIG", "VeldrisHouse_Big", g, doors=((6, 8),),
        npc=((6, 6), (3, 6), (9, 6), (10, 6), (10, 3), (11, 3), (6, 3), (6, 5)),
        title="H6 Big house (the Goldsworth plan), 13 x 9",
        uses="Every Goldsworth house: Briarwick, Hoarfell, HemlockReach, PrimroseVale, Kingsquay, Beaconmouth "
             "(_GoldsworthHouse)",
        notes="Card positions still work: butler (6,6) (or (6,3) in the Kingsquay and Beaconmouth cards), cousins (3,6) "
              "and (9,6) or (10,6), a cousin at (10,3) and the dog at (11,3) or (9,6). The Kingsquay vase is either flower "
              "table: put the bg_event on (7,5) or (8,5). Set behaviours in Porymap: TV tiles (4-5,1) MB_TELEVISION, "
              "shelves as trophy cabinets (bookshelf behaviour is already on the bases). The desk monitor (933) is the "
              "Hollowbrook bedroom-PC tile: a prop here.")


SPECS = [kitchen_house(), studio(), big_house()]
