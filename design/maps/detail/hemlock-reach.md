# HEMLOCK REACH, detailed design (city, place 12, gym 7 Poison)

Status: **PROPOSED**, written 2026-10-01. Nothing here is built and no name below is canon unless the existing card or [../../region-names.md](../../region-names.md) says so. New minor names are marked PROPOSED. This file adds detail to the card [../towns/hemlock-reach.md](../towns/hemlock-reach.md) and follows the brief in [../interiors/README.md](../interiors/README.md). Rules: [../README.md](../README.md), house style from [../../interiors.md](../../interiors.md), everything reusable in [../interiors/catalogue.md](../interiors/catalogue.md). Roads: [routes-east-detail.md](routes-east-detail.md). Neighbours: [primrose-vale.md](primrose-vale.md), [brinecombe.md](brinecombe.md).

**How to read the coordinates.** `(x,y)` is a tile counted from the map's top-left corner `(0,0)`, as Porymap shows it. In every interior the top two rows are back wall, the exit door mat is on the bottom row, and an NPC stands on a floor tile in front of the furniture. Exterior footprints are estimates (a Hoenn Pokémon Center building is about 5 x 4 tiles, a Mart about 4 x 3, a house about 4 x 3); the door tile is the number that matters. Trace by eye and move things a tile if the art wants it. Everything is Pokémon only: no real animals, even in jokes. House layouts follow the templates **G4-A, G4-B, G4-C** of [ebbsworth.md](ebbsworth.md) 6.0 and the shared Goldsworth layout of [kingsquay.md](kingsquay.md) 6.10, so the whole region uses one set of plans.

## 1. Description

**First glance.**
- **From R13 (west, the way most players arrive).** A gap in a long cliff line opens onto a low stone quay. Straight ahead the whole city climbs the rock in three stacked terraces, each edged with a brass handrail. Copper pipes run down the cliff face between the buildings and join into vats in the open air. Steam rises from them in thin white columns. The first thing the player sees is a signboard: HEMLOCK REACH, CHEMISTS WELCOME. Every window has a label in it.
- **From the sea (R14, the east shore).** The quay and its boathouse sit at the foot of the cliff. Above them the apothecary row looks out over the water with its drying racks like rows of flags. It is the one place on the coast that smells of mint rather than salt.
- **From the north inlet (R16).** A narrow sea inlet cuts into the cliff. The gym stands over it on the top terrace, with a small waterfall coming off the rock to the east.

**Mood and colour.** Late afternoon, copper and bronze on warm grey rock, with the pale green of herbs in boxes along every ledge. Everything is tidy and labelled. People speak quietly and read the label before they trust anything. Weather: sunny.

**Sound.** Music suggestion (existing Hoenn tracks): town `MUS_RUSTBORO` (orderly and brisk), Pokémon Center `MUS_POKE_CENTER`, gym `MUS_GYM`. Ambient: the hiss of the vats; no extra sound needed.

**The memorable view.** From the top of the central ramp the player sees all three terraces under them, the quay and the sea, and, small and far off in the north-east, the Goldsworth house sitting behind its hedge like a gift nobody asked for.

## 2. Source, size, tilesets

| Item | Decision |
|---|---|
| Base map | Vanilla `LavaridgeTown` (`LAYOUT_LAVARIDGE_TOWN`, 20 x 20, `gTileset_General` + `gTileset_Lavaridge`), duplicated and enlarged with Change Dimensions (the new area comes in empty at elevation 0, so repaint elevation 3 for ground, CLAUDE.md and [../../map-plan.md](../../map-plan.md)). |
| Final size | **44 wide x 40 tall.** (44 + 15) x (40 + 14) = 3186, under 10240. |
| Palladium | None for this city ([../../region-names.md](../../region-names.md)). Optional: `Cianwood City.png` for the shape of its ledge lines only, which would need a Palladium credit row; **recommended: skip it**, Brinecombe already uses that render. |
| Tilesets | `gTileset_General` is now the LeoB ORAS recolour (CREDITS.md), so the terraces come out in the same palette as Hollowbrook. `gTileset_Lavaridge` gives rock walls, ledges, the stepped roofs and the herb-shop look. **No new import is needed for the exterior.** |
| Waterfall tiles | Used for the small falls on the north inlet. **Checked in the tree: `gTileset_General` (primary) has 5 metatiles with the waterfall behaviour**, so the falls need no extra tileset. |
| Section | New `MAPSEC_HEMLOCK_REACH` (PROPOSED). Interiors share it. |
| Music | `MUS_RUSTBORO` town, see above. |
| Fly and heal | One row in `src/data/veldris_fly_towns.h` and the checklist in [../../region-map.md](../../region-map.md). Heal location `HEAL_LOCATION_HEMLOCK_REACH` on `(6,29)` (the tile in front of the Center door); write `respawn_map` before `respawn_npc` and give both (CLAUDE.md). `FLAG_VISITED_HEMLOCK_REACH` is set in the map's `MAP_SCRIPT_ON_TRANSITION`. |

## 3. Street layout, a numbered walk

The map is four horizontal bands. The sea is north (inlet) and east (shore). Ledges are one-way jumps down; stairs and ramps go both ways. Rows are `y` values.

| Band | Rows | What is there |
|---|---|---|
| North inlet and shore | 0 to 8 | Water inlet, small waterfall, a sand and rock shore at rows 7 to 8. |
| **Upper Ledge** | 9 to 19 | The gym, the vat-yard in front of it, the Goldsworth house, the North Ledge (rocks). |
| **Middle Terrace** | 21 to 30 | The market street: Center, Mart, three apothecaries, a house. A promenade runs along rows 29 to 30. |
| **Lower Quay** | 32 to 39 | The R13 gap in the south-west, a boardwalk, two small buildings, the pier into the R14 sea. |

Cliff steps sit at rows 19 to 20 (Upper to Middle) and rows 30 to 31 (Middle to Lower).

1. **Enter at the R13 gap**, tiles `x 0 to 2, y 34 to 38` (a 5-tile opening in the west cliff, ground level). A sign at `(4,36)`: HEMLOCK REACH. The nearest NPC, a **cliff kid** at `(7,33)`, dares the player to jump the ledge row at `x 6 to 9, y 31` (the hop down from the Middle Terrace back to the quay).
2. **Walk the boardwalk east along row 35.** House 2 stands at `x 12 to 16, y 33 to 37` (door `(14,37)`). Further on the **Boathouse** at `x 30 to 34, y 32 to 36` (door `(32,36)`). The boardwalk ends in a **pier** at `x 36 to 41, y 35`, with the **fisherman** at `(40,35)` and the water of R14 beyond. East shore water: `x 38 to 43, y 30 to 39` (the R14 connection runs along `y 30 to 37` on the east edge).
3. **Cut tree nook.** At the west end of the quay, `x 4 to 6, y 32`: a one-tile nook closed by a Cut tree at `(5,33)`, an ETHER on `(5,32)` (Cut, badge 1).
4. **Climb the west stairs.** Stair tiles `x 2 to 3, y 30 to 31` go from the quay up to the Middle Terrace.
5. **Middle Terrace, the market street.** West to east along row 28 (the building bottoms): Pokémon Center door `(6,28)`, Mart `(11,28)`, the Old Dispensary `(18,28)`, Stoppered and Sons `(23,28)`, the Reading Room `(29,28)`, House 1 `(36,28)`. The promenade at rows 29 to 30 is paved and has a signpost at `(15,29)`: LABEL EVERYTHING. Above the apothecaries, at `x 15 to 17, y 21 to 22`, are the **herb racks** (decorative rows of hanging bundles); `(17,23)` hides a PECHA BERRY. A **giant copper kettle** (decorative, steaming) stands at `x 12 to 14, y 21 to 23`.
6. **The ramp.** The central ramp is `x 21 to 22, y 19 to 21`. It leads up to the Upper Ledge. A second, smaller stair at `x 40 to 41, y 15 to 21` on the east side leads up to the Goldsworth house. Both can be climbed from the Middle Terrace.
7. **Upper Ledge, the vat-yard.** The gym stands at `x 18 to 24, y 10 to 14`, door `(21,14)`. In front of it is the **vat-yard**: eight big copper vats (decorative, `x 12 to 30, y 15 to 18`), leaving a clear approach lane `x 20 to 22, y 15 to 18`. A **vat-yard worker** at `(15,16)` stirs. This is where Scheme 7 plays out (section 7). One vat at `(27,13)` has a hidden POISON BARB at `(27,12)` behind it.
8. **North Ledge.** The north-west of the Upper Ledge, `x 2 to 12, y 9 to 14`: two **Rock Smash rocks** at `(6,11)` and `(8,11)` (they hide a NUGGET and a PP UP, Rock Smash badge 2). The one-way ledge row at `x 4 to 9, y 19` drops from here to the Middle Terrace.
9. **North shore and inlet.** A stair at `x 21 to 22, y 7 to 8` runs from the Upper Ledge up to the sand shore. The inlet water is `x 17 to 28, y 0 to 6`, with an east arm `x 29 to 33, y 4 to 8`. The **R16 connection** is the 8-tile channel `x 19 to 26` on row 0. On the north-east cliff a small **waterfall** at `x 31, y 2 to 3` drops into the arm; above it a ledge pocket at `x 30 to 32, y 1` holds the MAX ELIXIR at `(31,1)` (Waterfall badge 8, a return-trip reward, PROPOSED).
10. **Goldsworth house, far north-east.** `x 35 to 39, y 10 to 14`, door `(37,14)`. A hedge row `x 34 to 40, y 15` and an iron fence stand in front of it, leaving one gate gap at `(37,15)` that the east stair reaches. A gold knocker on the door and a view of nothing. The card said the door faces west; Gen 3 building art only has south-facing doors, so it faces south (open question 5).

### Connections (to be written by Claude after the maps exist)

| Edge | Map | Offset | Matching tiles |
|---|---|---|---|
| West | `Route13` (R13, 64 x 23) | Hemlock `left` offset `+26` (R13 row 0 sits at Hemlock row 26) | R13 rows 8 to 12 meet Hemlock rows 34 to 38 |
| East | `Route14` (R14, 56 x 24) | Hemlock `right` offset `+24` | R14 rows 6 to 13 meet Hemlock rows 30 to 37 (sea) |
| North | `Route16` (R16, 40 x 60) | Hemlock `up` offset `+2` (R16 `x 0` sits at Hemlock `x 2`) | R16 `x 17 to 24` meets Hemlock `x 19 to 26` (sea) |

Offsets are my arithmetic from the planned openings; recompute them when the maps are drawn, and check Porymap's connection preview.

## 4. Palette and tile notes

- **Terraces:** Lavaridge's rock wall and the ledge tiles. The apothecaries and their racks are mostly details: use the stepped roofs from the Lavaridge tileset, small plant boxes on every ledge edge, brass-coloured handrails where the tileset has railings.
- **Pipes and vats:** the town has no pipe tile. Painted as decoration: use Lavaridge's chimney and rock details for the pipe runs and the biggest round object the tileset has for the vats. If nothing reads as a vat, leave the vat-yard as rows of crates and barrels (the General tileset has them) and let the interior gym carry the vat art (see section 6, Facility tiles). This is a known unknown; flag it when tracing.
- **Gas, steam:** no gas tile exists. Do not try to show gas in the town; the Scheme 7 beat uses inspectors and a Smog animation instead (section 7).
- **Needs redrawing:** nothing is required for a first playable version.

## 5. Every building

### 5.1 Pokémon Center (`HemlockReach_PokemonCenter_1F` and `_2F`)

- **Layout:** `LAYOUT_POKEMON_CENTER_1F` and `LAYOUT_POKEMON_CENTER_2F`, unchanged (decision 2). 14 x 9 and 14 x 10. Palladium `newcenter.png` is a reference only. Vanilla look; the optional re-skin (Alternative Pokecenter Secondary) is the author's later call.
- **Facts from the vanilla map (checked in the tree):** nurse at `(7,2)`, facing down, behind a counter that fills `x 4 to 9, y 2 to 3`; the player talks from `(7,4)`. Door mats `(6,8)` and `(7,8)`. Staircase warp `(1,6)`. A sofa corner at the right.
- **Objects (3):** nurse `(7,2)` (needs `LOCALID_HEMLOCK_NURSE` for the whiteout script, like `DewfordTown_PokemonCenter_1F`), a customer buying cough syrup `(10,6)` facing left, a courier `(5,5)` wandering left and right. 2F has the vanilla three attendants and the Mystery Gift man.
- **Warps:** 1F `(6,8)` and `(7,8)` to `HemlockReach` warp 0 (exterior tile `(6,28)`); 1F `(1,6)` to 2F warp 0; 2F `(1,6)` to 1F warp 2; the other 2F warps stay as vanilla (Union Room, Trade Center).
- **Player does:** heals, saves the fly point, reads the poster board in 2F. Scheme 7 gag: one of the customers asks if the review applies to the soup.

### 5.2 Mart (`HemlockReach_Mart`)

- **Layout:** `LAYOUT_MART` (11 x 8), unchanged (decision 2). Clerk `(1,3)` behind a counter at `x 2, y 2 to 4`; the player talks from `(3,3)`. Door mats `(3,7)` and `(4,7)`.
- **Objects (3):** clerk, a shopper `(5,5)` facing right, an old woman `(9,5)`.
- **Stock leans** to Antidote, Full Heal, Super Potion, Max Repel. A clerk line says Antidotes sell out when a Weezing is nearby.
- **Warps:** `(3,7)` and `(4,7)` to `HemlockReach` warp 1 (tile `(11,28)`).

### 5.3 Apothecary 1, 'The Old Dispensary' (PROPOSED, `HemlockReach_OldDispensary`)

- **Layout:** `LAYOUT_LAVARIDGE_TOWN_HERB_SHOP` (11 x 8, Shop secondary), the vanilla herb shop reused as a **shared layout** (Add New Map with Layout). Its counter is the row `x 0 to 5, y 3`; the clerk stands at `(3,2)`; the player talks from `(3,4)`. Door mats `(3,7)` and `(4,7)`.
- **Objects (3):** the old apothecary `(3,2)` (clerk script; sells Energy Powder, Heal Powder, Energy Root, Revival Herb as vanilla), a customer `(7,5)` looking around (buys cough syrup for a Pokémon and reads the dose aloud), an expert `(9,3)` wandering left and right (a delivery man).
- **Warps:** `(3,7)` and `(4,7)` to `HemlockReach` warp 2 (tile `(18,28)`).
- **Why this layout:** vanilla, already shaped for a herb seller, no new art.

### 5.4 Apothecary 2, 'Stoppered and Sons' (PROPOSED, `HemlockReach_StopperedAndSons`)

- **Layout:** new, 11 x 9, **Gen 4 Interior Secondary** with `gTileset_Building` (house style, decision 1). The card said `LAYOUT_HOUSE2` as a stand-in; the house style wins.
- **Plan, `(x,y)`:**
  - Back wall: three long shelves of jars (the bookshelf metatiles in green and brown), `x 1 to 3`, `x 5 to 7`, `(9..10)` at rows 1 to 2. Bookshelf behaviour tiles at `(2,2)`, `(6,2)`, `(9,2)` read as jar labels. The **Antidote Cabinet** is a bg event on `(9,2)`: the one-time free ANTIDOTE.
  - Counter: the kitchen counter, L-shaped, `x 2 to 6, y 4` with a return at `(7,4)`. The shopkeeper stands behind it at `(4,3)`. The player talks from `(4,5)`.
  - A stool at `(8,6)` and a flower pot at `(1,7)` and `(9,7)`. A rug `x 4 to 6, y 6 to 7`.
  - Door mat `(5,8)`.
- **Objects (2):** the shopkeeper `(4,3)` facing down (gives the cabinet item once, bickers with his son about the sign), his son `(8,5)` facing left.
- **Warps:** `(5,8)` to `HemlockReach` warp 3 (tile `(23,28)`).
- **Palladium image:** none; `Elm's House.png` (13 x 10) gives the furniture mood.
- **Optional upgrade:** the Team Aqua `Brick Cafe Interior Secondary` has a tall shelf of canisters and a counter exactly like a dispensary, but it needs a Porytiles conversion and a CREDITS row for one small room. Not recommended for the first pass.

### 5.5 Apothecary 3, 'The Reading Room' (PROPOSED, `HemlockReach_ReadingRoom`) and its Archive

- **Layout:** new, 12 x 11, Gen 4 Interior + `gTileset_Building`, traced from Palladium **`Trainer School.png`** (12 x 14 in the render: a shelf at top-left, a green board in the middle of the back wall, two rows of desks with stools, plants in the bottom corners, door mat bottom-centre). Cut three rows from the middle to reach 11.
- **Plan:**
  - Back wall: bookshelf at `x 1 to 2`; the **poster** (the green board, a bg event) at `(5,2)` and `(6,2)`; windows at `x 8 to 10`.
  - Four reading desks with stools in two pairs: desks at `(3,5)`, `(4,5)`, `(7,5)`, `(8,5)`, stools in front at `y 6`. The rest is open floor.
  - Plants in the bottom corners `(1,9)` and `(10,9)`.
  - **Staircase down** at `(10,2)` (the Gen 4 staircase, bottom step at `(10,3)`, enter walking up/east as in Hollowbrook's staircase) to the Archive.
  - Door mat `(6,10)`.
- **Objects (3):** the **archivist** at `(6,4)` facing down (explains the poster as a fire drill), two **readers** at `(3,7)` and `(8,7)` (flavour, one of them is a hazmat-suited junior inspector on his lunch break, only before Scheme 7 is beaten).
- **The poster** (bg event at `(5,2)`): shows the four valve colours in order, blue, green, red, yellow, with the words 'Fire drill' over it. It spoils the gym puzzle a second time on purpose (open question 3). The gym itself gives words, not colours, so the two hints fit together: the poster says the colours, the gym plaque says what each does.
- **Archive (`HemlockReach_ReadingRoom_Archive`):** 9 x 8, Gen 4 Interior. Entered by the staircase, arrive at `(7,2)`. A narrow store room: shelves along the back wall, crates at `(1,5)`, `(2,5)`, a **Strength boulder** (object, `OBJ_EVENT_GFX_PUSHABLE_BOULDER`) at `(5,4)` blocking a one-tile passage between two crate stacks at `(4,3)` and `(4,5)`. Push it east once to open the route to the **TM Rock Tomb** ball at `(7,5)`. Staircase back up at `(7,2)`. This is the 'boulder room behind the Reading Room' of the card; I made it an interior because a boulder outdoors would collide with the North Ledge rocks (open question 4).
- **Warps:** `(6,10)` to `HemlockReach` warp 4 (tile `(29,28)`); `(10,3)` to Archive warp 0; Archive `(7,3)` back to `(10,3)`.

### 5.6 House 1, the retired chemist (`HemlockReach_House1`)

- **Layout:** **shares `LAYOUT_HOLLOWBROOK_NEIGHBOURS_HOUSE`** (11 x 8, built, Gen 4 Interior; Add New Map with Layout) so one painted family house serves several towns. Exit mat `(2,7)`. Free floor at `(8,3)`, `(5,6)` and `(9,5)`; bookshelf bg events at `(7,2)` and `(8,2)`; the flower table sits at `x 6 to 7, y 4 to 6`.
- **Objects (3):** the **retired chemist** `(8,3)` facing up by the bookshelf (talks about ASEBY as a student; hints that the North Ledge rocks hide something), his **grandchild** `(9,5)` wandering (repeats a label), a Skitty `(2,4)` wandering, as in the Hollowbrook house.
- **Warps:** `(2,7)` to `HemlockReach` warp 5 (tile `(36,28)`).
- **Why sharing:** the card calls for an ordinary resident only; a shared layout costs no new painting.

### 5.7 House 2, the ferry widow (`HemlockReach_House2`)

- **Layout:** the **G4-C 'Study and lounge' template, 12 x 9** (a new layout, own painting, defined in [ebbsworth.md](ebbsworth.md) 6.0 so every house in the region uses the same three plans). Gen 4 Interior + `gTileset_Building`. Palladium reference: the lower half of **`Gold's House.PNG`** (the render is two 13 x 10 floors stacked; the lower floor has a kitchen strip, a bookshelf, a green rug with four cushions around a table, a plant in each bottom corner), which G4-C already follows. If the other writers have not yet built G4-C, it is the plan to paint first (open question 8).
- **Plan (G4-C, `x 0 to 11`, `y 0 to 8`):** tall bookshelf runs at `x 0 to 2` and `x 10 to 11`, rows 1 to 2 (bg events on the lower tile of each); window `(4,1)`; TV and cabinet `x 7 to 8, y 1 to 2`; rug `x 3 to 8, y 4 to 6` with a low table `(5,5)` and `(6,5)`; plants `(1,5)` and `(10,5)`; door mats `(5,8)` and `(6,8)`.
- **Objects (3):** the **ferry widow** `(3,5)` facing right, a **model ferry** (bg event on the low table `(5,5)`; she mentions Mirror Isle by name once), a Slakoth on the floor `(9,7)`.
- **Warps:** `(5,8)` and `(6,8)` to `HemlockReach` warp 8 (tile `(14,37)`).

### 5.8 Boathouse (`HemlockReach_Boathouse`)

- **Layout:** new, 12 x 8, **Team Aqua `Legend of Zelda House Secondary`** + `gTileset_Building`. Timber walls, stone-brown floor, clay pots, a shelf of bowls, a hearth, two jugs and a woven green mat (see its `example.png`): a fishing hut without any fuss. This is the **only Team Aqua tileset recommended for Hemlock**. It needs the same Porytiles conversion Hollowbrook's Gen 4 set got (it is a triple-layer set, 512 metatiles, interiors.md 'Tileset notes'), plus a `CREDITS.md` row (credits file in the folder: Buildings Hek-el-grande, Assembler Yumekua, Main Creator Ekat99, reformat Rahtak), and it should be imported **in the commit that first needs it**. Fallback if the author does not want a second tileset: Gen 4 Interior with the Cottage layout.
- **Plan:** back wall `x 1 to 10, y 1 to 2` with the bowl shelf at `x 2 to 4`; hearth at `(9,2)`; two jugs at `(7,3)` and `(8,3)`; clay pots down the left wall at `(1,4)` to `(1,7)` (they are the hut's furniture, not objects); a long bench at `x 4 to 6, y 5`; a stool at `(9,5)`; door mat on the green mat `(4,7)`.
- **Objects (2):** the **dock hand** `(5,4)` facing down (says R14 and R16 are Surf only, the tide is gentler in the morning), a **rowing-boat model** (bg event on the bench `(5,5)`).
- **Warps:** `(4,7)` to `HemlockReach` warp 9 (tile `(32,36)`).
- **Player does:** gets the Surf-roads orientation: two routes out, east to Brinecombe, north to the mere.

### 5.9 Goldsworth House, shared layout (`HemlockReach_GoldsworthHouse`)

All city Goldsworth houses share **one** layout (map-plan.md). It is **defined once, in [kingsquay.md](kingsquay.md) 6.10** (13 x 11, Gen 4 Interior + `gTileset_Building`, bookshelf runs on the left, TV and cabinet on the right, a large gold-and-cream rug with a low table `(6,5)` and `(7,5)`, plants, door mats `(5,10)` and `(6,10)`). I use it unchanged: **Butler** at `(6,3)` facing down, **Cousin A** at `(3,6)` facing right, **Cousin B** at `(10,6)` facing left. Palladium `Gold's House.PNG` (lower floor) and `President's Office Tiled.PNG` are its look-and-feel references.

- **Hemlock objects (4):** the Butler `(6,3)`, **Prescott** (Cousin A, wine snob) `(3,6)` beside the left bookshelf run, which reads as his wine rack ('Vintage, 1984'), **Kip** (Cousin B) `(10,6)` with **Duchess**, a PERSIAN, `(11,6)` (`OBJ_EVENT_GFX_SPECIES(PERSIAN)`, expansion's per-species overworld sprite; check it exists in the tree). Before Scheme 7 is cleared Prescott scorns the town's cough syrup and offers a vintage tonic he cannot name; Kip warns the player off Duchess. After: Prescott must pay for his own dinner and Duchess looks embarrassed. The Butler says nothing useful. They may swear lightly (Goldsworth places only, [../../dialogue-style.md](../../dialogue-style.md)); no battle, no flags beyond the scheme stage.
- **Warps:** `(5,10)` and `(6,10)` to `HemlockReach` warp 7 (tile `(37,14)`).
- **Allocation conflict (open question 8):** the card gives Hemlock Reach Prescott and Kip, but [../towns/beaconmouth.md](../towns/beaconmouth.md) and [beaconmouth.md](beaconmouth.md) give the same pair to Beaconmouth, so one of the two cities has to change.

### 5.10 Gym 7, `HemlockReach_Gym` (the full design is section 6)

15 x 22. Door `(21,14)` on the exterior; interior exit mats `(7,21)` and `(8,21)`.

### 5.11 Extra, non-enterable

Giant kettle (decor), herb racks, vats, drying racks, hedge and iron fence at the Goldsworth house. None has a warp.

## 6. Gym 7, the Poison gym, in full

**Leader:** ASEBY, ace level 48 (team in the card: Weezing 46, Crobat 47, Drapion 47, Garbodor 47, Toxapex 48). Trainer id `TRAINER_ASEBY`. VIAL BADGE and TM Sludge Bomb. The pitch: a chemist who treats a battle as quality control; the dialogue should not give an age (the sprite is young, card open question 4).

### 6.1 Source and tiles

- **Footprint:** Palladium `KantoGyms3YearsLatercorrected.png`, the **pink-floored panel** (bottom right of the sheet). I measured it at about **272 x 359 px** including its black border, which is about **15 tiles wide and 22 tall** at 16 px per tile (the card's estimate of 15 x 21 holds; the extra row is the door row). My reading of that panel is the Fuchsia gym: a bare floor with four scattered trainers and a back wall with four barred windows and a heart emblem. In the original the walls are invisible; here the **gas curtains replace the invisible walls**, which is a neat fit.
- **Size:** `15 x 22`, (15 + 15) x (22 + 14) = 1080.
- **Tilesets:** `gTileset_Building` primary + **vanilla `gTileset_Facility` secondary** (the Aqua Hideout set, already in the tree at `data/tilesets/secondary/facility/`). It has round tanks, pipe runs, a hook and gantry, computers, cabinets and several palette banks (orange, grey-blue and green are visible in its tile sheet), so a red, a green and a blue tank are palette variants of one tank. Yellow needs one palette bank edited in Porymap's palette editor (open question 6). Use the palest floor tile the set has; the Fuchsia pink floor is not available without recolouring.
- **No Team Aqua import and no credit row** for this gym beyond the Palladium credit that the first traced map already carries.

### 6.2 Plan and puzzle in tiles

```
 x:  0 1 2 3 4 5 6 7 8 9 A B C D E        (A=10 B=11 C=12 D=13 E=14)
 y0  W W W W W W W W W W W W W W W        back wall: barred windows, heart emblem at x 7
 y1  W W W W W W W W W W W W W W W
 y2  W W W W W W W W W W W W W W W
 y3  . . . . . . . L . . . . . . .        L = ASEBY (7,3), facing down
 y4  . . . . . . . . . . . . . . .
 y5  P P P P P P P 1 P P P P P P P        curtain 3 at (7,5)
 y6  . . . . . . . . . . . . . . .
 y7  . . . . M . . . . . . . . . .        M = Pokémaniac (4,7), facing right, sight 3
 y8  . . . . . . . . . . . . . . .
 y9  P P P P P P P 2 P P P P P P P        curtain 2 at (7,9)
 y10 . . . E . . . . . . . C . . .        E = Expert (3,10) down, sight 2;  C = Collector (11,10) down, sight 2
 y11 . R R . . . . . . . . . Y Y .        red vat (1,11)-(2,12);  yellow vat (12,11)-(13,12)
 y12 . R R . . . . . . . . . Y Y .
 y13 . . . . . . . . . . . . . . .
 y14 P P P P P q P 3 P P P P P P P        curtain 1 at (7,14);  q = plaque at (5,14)
 y15 . . . . . . . . . . . . . . .
 y16 . . . . . . . A . . . . . . .        A = Aroma Lady (7,16), facing down, sight 2
 y17 . B B . . . . . . . . . G G .        blue vat (1,17)-(2,18);  green vat (12,17)-(13,18)
 y18 . B B . . . . . . . . . G G .
 y19 . . . . . . . . . . . . . . .
 y20 . . . . S . . . . S g . . . .        statues (4,20) and (9,20); g = Gym guide (10,20)
 y21 . . . . . . . D D . . . . . .        door mats (7,21) and (8,21)
```

(`P` is a pipe wall, collision on; `1 2 3` are the three gas curtains; letters on the floor are objects or vats.) Statue and guide positions follow the Palladium panel: the statues flank the door, the guide stands at the right statue. Check the offsets against the trace.

- **Ground:** all floor elevation 3. Pipe rows `y 5, 9, 14` are walls across the whole width except the three curtain tiles at `x 7`. The vats are 2 x 2 tank metatiles with collision.
- **The three curtains** are **metatiles**, not objects: a closed 'gas shimmer' tile (impassable) swapped for plain floor with `setmetatile` when the valves run, and set again on `MAP_SCRIPT_ON_LOAD` from the saved stage. There is no gas sprite in the tree and no object art for it (gyms.md open question 2). If a closed curtain tile does not exist, use the Facility set's closed grate or hatch tile in the pipe row. Because they are not objects, the gym needs only 6 of its 15 object slots (leader, four trainers, guide). The card counted the curtains as objects; both work.
- **Valves** are bg events (signs) on the vat tile, read from the tile named 'stand':

| Vat | Colour | Tiles | Valve bg event | Player stands | Label on the valve | Stage effect |
|---|---|---|---|---|---|---|
| Blue | blue | `(1,17)` to `(2,18)` | `(2,18)` | `(3,18)` facing west | COOL | stage 0 to 1 |
| Green | green | `(12,17)` to `(13,18)` | `(12,18)` | `(11,18)` facing east | VENT | stage 1 to 2, **curtain 1 drops** |
| Red | red | `(1,11)` to `(2,12)` | `(2,12)` | `(3,12)` facing west | SEAL | stage 2 to 3, **curtain 2 drops** |
| Yellow | yellow | `(12,11)` to `(13,12)` | `(12,12)` | `(11,12)` facing east | DRAIN | stage 3 to 4, **curtain 3 drops** |

- **The order: blue, green, red, yellow** (cools, vents, seals, drains, the card's PROPOSED order). The **plaque** at `(5,14)` (a bg event on the first pipe wall, read from `(5,15)` facing north) says: PROCEDURE 4: COOL, VENT, SEAL, DRAIN. The vats carry the words, not their colours in the plaque, so the player must match words to colours. The Reading Room poster gives the colours. Together they are the puzzle's two halves.
- **Rules (stage var `VAR_HEMLOCK_GYM_VALVES`, 0 to 4, kept in the save so leaving does not reset):**
  - Valve k only works if the stage is `k - 1`. The correct valve prints its label and a short hiss, and the stage rises.
  - A **wrong valve** vents a harmless puff of gas (message and screen shake) and sets the stage back to the **start of that room**: `0` if the player is in the lower hall (y 15 to 20), `2` if in the middle hall (y 10 to 13). Curtains already dropped stay dropped. This cannot trap the player, because the lower-hall valves are never needed again after curtain 1 drops. The yellow valve (the fourth) is in the middle hall, so the final step of the puzzle has the player go back down from the upper hall to the middle hall: after curtain 2 drops, the way on to the top is sealed again at curtain 3 until yellow.
  - After **two wrong turns** (a temp counter) the Gym guide offers a hint: 'Read the labels, not the colours.'
- **Trainers.** Positions are chosen so the valves are guarded by a fight:

| # | Class | Team | Position | Facing, sight | Notes |
|---|---|---|---|---|---|
| 1 | Aroma Lady | Victreebel 42, Amoonguss 42, Roserade 43 | `(7,16)` | down, 2 | First corridor, sees the player walking up the lane at `(7,18)` |
| 2 | Expert | Muk 43, Toxicroak 43 | `(3,10)` | down, 2 | Covers `(3,11)` and `(3,12)`: the stand tile of the **red** valve |
| 3 | Collector | Arbok 42, Skuntank 42, Venomoth 42 | `(11,10)` | down, 2 | Covers `(11,11)` and `(11,12)`: the stand tile of the **yellow** valve. Labels her Pokémon |
| 4 | Pokémaniac | Nidoking 43, Salazzle 43 | `(4,7)` | right, 3 | Last before ASEBY; sees `(5,7)` to `(7,7)`, where the player emerges from curtain 2 |

All reuse vanilla ids; no IVs. Levels are the card's (42 to 43).

- **Objects (6 of 15):** ASEBY `(7,3)`, trainers 1 to 4, the guide. Statues are bg events: `(4,20)` left, `(9,20)` right, with the standard gym statue text, as in `LavaridgeTown_Gym_1F`.
- **Warps:** `(7,21)` and `(8,21)` to `HemlockReach` warp 6 (exterior tile `(21,14)`). **No warp on the exterior tile** while Scheme 7 is unresolved: the inspectors block the approach lane (see 7).
- **Guide** at `(10,20)`: before the gym, 'ASEBY has a clipboard for every move'; after two resets, the hint.
- **Flags:** see section 10.

## 7. Scheme 7 on the Upper Ledge, step by step

Source: [../../troglodyte-arc.md](../../troglodyte-arc.md) (fight 6, Scheme 7) and the card. All triggers are `coord_event` triggers (CLAUDE.md), not `MAP_SCRIPT_ON_TRANSITION`: tile walkable, elevation 3.

| Step | Where | What |
|---|---|---|
| Setup | Upper Ledge, always visible while `VAR_HEMLOCK_SCHEME7 == 0` | Lead inspector `(21,16)`, junior inspector `(22,15)`, both in hazmat suits, one holding a clipboard and a stamp, **blocking the approach lane to the gym door** (`(21,14)`). A vat-yard worker `(15,16)` grumbles that they are standing too close. |
| Reveal | `coord_event` triggers at `(20,18)`, `(21,18)`, `(22,18)` (the top of the ramp), `VAR_HEMLOCK_SCHEME7 == 0` | The lead inspector 'pins' a **regulatory review** to the gym door: **47 violations**, number 1 is 'Existing'. The date at the top is **before** they arrived; a local points out the stamp is not dry. Var to 1. Foreshadowed on R13 (the milestone argument). |
| Collapse | `coord_event` triggers at `(20,16)` and `(22,16)` (beside the lead inspector, who stands at `(21,16)`), `VAR_HEMLOCK_SCHEME7 == 1` | ASEBY's **WEEZING** (object `OBJ_EVENT_GFX_SPECIES(WEEZING)`, appears at the door `(21,14)` for the scene and hides after) lets out one polite Smog; the suits are not rated for it; the inspectors run down the ramp, leaving the clipboards. Both inspector objects hidden by their flags. Var to 2. |
| Troglodyte | The ramp top `(21,19)` to `(21,17)` | He walks up from the Middle Terrace, quieter than before ('No jokes this time', as in the card and the arc table). Fight 6 starts when he reaches `(21,16)` (a scripted `trainerbattle`, the Pool Prune entry in the arc doc). Level 43 to 46, six Pokémon, Stoutland, Vaporeon, Gardevoir, Pyroar, Pupitar and his starter's third stage. Win or lose he walks off down the ramp. Var to 3. |
| Aftermath | ASEBY's Weezing hides; ASEBY steps to `(21,15)` and invites the player in | The gym door works. NPCs switch to their 'After' lines. A returned inspector appears in Brinecombe afterwards. |

The Weezing and Troglodyte are temporary objects. Outdoor object budget: see section 8.

## 8. NPCs

Cities list 12 to 20 roles; this one has 16. Max 15 live objects per map: the outdoor map shows at most 14 at once and 12 after the scheme clears.

**Outdoor objects (`HemlockReach`, 14 maximum):**

| # | Role | Position | Behaviour | Topic |
|---|---|---|---|---|
| 1 | Lead inspector | `(21,16)` | faces down; hidden after stage 2 | Reads 'Violation 1 of 47' aloud. |
| 2 | Junior inspector | `(22,15)` | faces left; hidden after stage 2 | Cannot find the clipboard's 47th page; holds the gym's name on a form. |
| 3 | Troglodyte | arrives at `(21,17)` | scene only; hidden otherwise | Fight 6. |
| 4 | Weezing (ASEBY's) | `(21,14)` | scene only | One polite Smog. |
| 5 | Vat-yard worker | `(15,16)` | wanders up and down | Complains the inspectors stand too close. |
| 6 | Herb carrier | `(26,29)` | wanders left and right | Carries a basket; points out the ramp. |
| 7 | Cliff kid | `(7,33)` | faces up | Dares the player to jump the ledge. |
| 8 | Fisherman | `(40,35)` | faces right | Says Tentacruel gather in the R14 sea. |
| 9 | Cut tree | `(5,33)` | tree | ETHER nook. |
| 10 and 11 | Rock Smash rocks | `(6,11)`, `(8,11)` | rocks | NUGGET and PP UP. |
| 12 | ETHER ball | `(5,32)` | item | |
| 13 | MAX ELIXIR ball | `(31,1)` | item | Waterfall pocket. |

13 of 15, 12 once the inspectors, Troglodyte and Weezing are gone.

**Interior NPCs:** Center nurse, customer and courier; Mart clerk and two shoppers; the Old Dispensary's three; the Stoppered pair; the Reading Room's archivist and two readers; the chemist, grandchild and Skitty in House 1; the widow and Slakoth in House 2; the dock hand; the Goldsworth cousins Prescott and Kip with Duchess; the gym's five. Card topics are kept; the extra NPCs are flavour only.

## 9. Items and secrets (positions added to the card)

| Item | Where (tile) | Gate |
|---|---|---|
| ANTIDOTE ('Cabinet', once) | Stoppered bg event `(9,2)` | none |
| ETHER | `(5,32)` behind the Cut tree `(5,33)` | Cut (badge 1) |
| TM Rock Tomb | Reading Room Archive, ball `(7,5)` behind the boulder | Strength (badge 4) |
| Hidden POISON BARB | `(27,12)` behind the vat `(27,13)` | none (0x264 hidden-item range, [../../flags.md](../../flags.md)) |
| Hidden PECHA BERRY | `(17,23)` by the herb racks | none |
| NUGGET and PP UP | under the two North Ledge rocks `(6,11)`, `(8,11)` | Rock Smash (badge 2) |
| MAX ELIXIR | `(31,1)` in the waterfall pocket | **Waterfall (badge 8)**, PROPOSED return trip |
| TM Sludge Bomb, VIAL BADGE | ASEBY | after the gym |
| Fly point | the town | Fly (badge 6) |

## 10. Flags and vars (not claimed, names only)

Claim them in [../../flags.md](../../flags.md) when built.

- `FLAG_VISITED_HEMLOCK_REACH` (fly flag, set on transition).
- `VAR_HEMLOCK_SCHEME7` (0 not started, 1 reveal seen, 2 collapse done, 3 Troglodyte fought).
- Hide flags: `FLAG_HIDE_HEMLOCK_INSPECTORS` (set at stage 2), `FLAG_HIDE_HEMLOCK_TROG`, `FLAG_HIDE_HEMLOCK_WEEZING`.
- `VAR_HEMLOCK_GYM_VALVES` (0 to 4) and a temp var for the wrong-turn counter (`VAR_TEMP_*`).
- `FLAG_HEMLOCK_ANTIDOTE_TAKEN`, `FLAG_HEMLOCK_TM_ROCK_TOMB`, `FLAG_HEMLOCK_ITEM_ETHER`, `FLAG_HEMLOCK_ITEM_NUGGET`, `FLAG_HEMLOCK_ITEM_PPUP`, `FLAG_HEMLOCK_ITEM_MAXELIXIR`, two hidden-item flags from 0x264.
- `FLAG_BADGE07_GET` (exists).
- That is about 9 flags and 2 vars, from the spare pool (about 300 flags, 19 vars; exact count in [flags.md](../../flags.md)). Use `VAR_TEMP_*` for the wrong-turn counter.

## 11. Door and warp table, whole town

| Map | Tile | To | Dest warp |
|---|---|---|---|
| `HemlockReach` 0 | `(6,28)` | `HemlockReach_PokemonCenter_1F` | 0 |
| `HemlockReach` 1 | `(11,28)` | `HemlockReach_Mart` | 0 |
| `HemlockReach` 2 | `(18,28)` | `HemlockReach_OldDispensary` | 0 |
| `HemlockReach` 3 | `(23,28)` | `HemlockReach_StopperedAndSons` | 0 |
| `HemlockReach` 4 | `(29,28)` | `HemlockReach_ReadingRoom` | 0 |
| `HemlockReach` 5 | `(36,28)` | `HemlockReach_House1` | 0 |
| `HemlockReach` 6 | `(21,14)` | `HemlockReach_Gym` | 0 |
| `HemlockReach` 7 | `(37,14)` | `HemlockReach_GoldsworthHouse` | 0 |
| `HemlockReach` 8 | `(14,37)` | `HemlockReach_House2` | 0 |
| `HemlockReach` 9 | `(32,36)` | `HemlockReach_Boathouse` | 0 |
| PC 1F | `(6,8)`, `(7,8)` | `HemlockReach` | 0 |
| PC 1F | `(1,6)` | PC 2F | 0 |
| Mart | `(3,7)`, `(4,7)` | `HemlockReach` | 1 |
| Old Dispensary | `(3,7)`, `(4,7)` | `HemlockReach` | 2 |
| Stoppered | `(5,8)` | `HemlockReach` | 3 |
| Reading Room | `(6,10)` | `HemlockReach` | 4 |
| Reading Room | `(10,3)` | Archive | 0 |
| House 1 | `(2,7)` | `HemlockReach` | 5 |
| Gym | `(7,21)`, `(8,21)` | `HemlockReach` | 6 |
| Goldsworth house | `(5,10)`, `(6,10)` | `HemlockReach` | 7 |
| House 2 | `(5,8)`, `(6,8)` | `HemlockReach` | 8 |
| Boathouse | `(4,7)` | `HemlockReach` | 9 |

Signs (bg events): town sign `(4,36)`, signpost `(15,29)`, gym sign `(19,15)`, Center sign `(7,29)`, Mart sign `(12,29)`, three apothecary signs `(19,29)`, `(24,29)`, `(30,29)`, Goldsworth door sign `(38,15)`, boathouse sign `(33,36)`.

## 12. Build checklist, in order

1. Duplicate `LavaridgeTown` in Porymap (close Porymap before Claude edits event lists, CLAUDE.md). Delete the two copied heal locations before the first save and check `heal_locations.json` for duplicate ids afterwards. Change the header to `MAPSEC_HEMLOCK_REACH`. Change Dimensions to 44 x 40, repaint ground at elevation 3.
2. Paint the four bands: quay and boardwalk, the Middle Terrace row, the Upper Ledge, the inlet. Place ledges and stairs per section 3.
3. Place the building footprints and door tiles (section 11). Place decorations: vats, racks, kettle, hedge.
4. Paint the Gen 4 interiors (5.4 to 5.9): the two new layouts are **G4-C** (House 2) and the shared **Goldsworth House layout** (defined in [kingsquay.md](kingsquay.md) 6.10; paint it once, whichever town is built first). Share the Hollowbrook neighbour layout (G4-A) for House 1.
5. Add Center, Mart and Old Dispensary on their shared layouts (no painting).
6. Import and convert `Legend of Zelda House Secondary` for the Boathouse (or fall back), add the CREDITS row, **only in the commit that first needs it**.
7. Paint the gym on `Facility`: pipe rows, vats, plaque, statues, three curtain tiles (open and closed variants).
8. Claude wires: connections, warps, objects, coord events (section 7), the valve scripts and `MAP_SCRIPT_ON_LOAD`, trainers (reuse vanilla ids), the Fly row and heal location, `flags.md`, `engine-edits.md` if needed, `CREDITS.md` (Palladium rows for the Reading Room, Gold's House and the gym panel, the Zelda tileset row).
9. Dialogue check: `python3 design/tools/dialogue_check.py` on any text; build (`make -j4`); test the Scheme 7 scene and the valve order.

## 13. Open questions

1. **Curtain and vat art.** No gas tile and no vat tile exist. Is the Facility tank enough, with a closed-grate tile for the curtain? If the author wants real shimmering gas, it is a small art job (one 2-frame tile) that [../../gyms.md](../../gyms.md) already flags.
2. **Strength boulder as an interior.** I moved TM Rock Tomb to a cellar behind the Reading Room instead of the North Ledge. Keep, or put a boulder on the ledge as the card said?
3. **The poster spoils the order.** Keep both hints (poster and plaque), or hide one?
4. **North Ledge.** I kept two Rock Smash rocks there and no boulder. The retired chemist's hint now points at the rocks.
5. **Goldsworth door direction.** The card says the door faces west. Gen 3 buildings face south only. I used south.
6. **Yellow vat.** Facility has orange, grey-blue and green banks; a fourth (yellow) bank needs a palette edit. Acceptable?
7. **Waterfall tile.** Resolved by checking the tree: the waterfall tiles are in `gTileset_General`. Remaining question: does the Lavaridge secondary's rock wall look right beside them? Check when painting.
8. **Shared layouts and cousins.** The G4-A, G4-B, G4-C house templates ([ebbsworth.md](ebbsworth.md) 6.0) and the Goldsworth layout ([kingsquay.md](kingsquay.md) 6.10) are another writer's proposals; I adopted them. The **cousin allocation collides across cards**: Prescott and Kip are Hemlock's on its card and also Beaconmouth's; Winston is Primrose's on its card, and also appears at Hoarfell, Kingsquay and Aldermere. The author or the index writer has to pick which city gets whom.
9. **ASEBY's ace and valve order** stay the card's PROPOSED values.
10. **Troglodyte fight 6** stays outside the gym; confirm the card's placement against a quieter 'Work phase' alternative.
