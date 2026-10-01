# CRAGDALE, detailed design (town, place 9, ridge town, no gym)

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Card this expands: [../towns/cragdale.md](../towns/cragdale.md). Rules: [../interiors/README.md](../interiors/README.md), catalogue [../interiors/catalogue.md](../interiors/catalogue.md), house style [../../interiors.md](../../interiors.md). Roads: [routes-centre-detail.md](routes-centre-detail.md). New minor names are PROPOSED. Coordinates are `x, y` tiles from the top-left tile (0,0); anything placed from a picture or by eye is good to about one tile.

## 0. Facts and changes against the card

- **No Palladium render.** The card is right: Cragdale has none. Vanilla base `FallarborTown` (20 x 20) is too small, so this document lays out a **34 x 28** map by hand. `(34+15)*(28+14) = 2058`, under 10240.
- **All doors face south.** The card puts the Hostel door 'facing east' and the Lodge door 'facing west'; a Gen 3 door can only be on a south face, so every door below is south-facing and opens onto a street or terrace row.
- **Tilesets: LeoB ORAS `fallarbor` secondary** (dual-layer, 367 metatiles, same ids as vanilla Fallarbor, so it drops in) with the ORAS General already in the tree. Folder: `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/fallarbor/`. It supplies the rock, ledges and short grass the card asks for. The set also has **ash grass** (vanilla Fallarbor's feature): simply do not paint the ash tiles (no ash weather either). **Needs a CREDITS row**: extend the existing leob0505 row to name `fallarbor`.
- **Section** `MAPSEC_CRAGDALE` (new, PROPOSED, one of the free ids). Fly destination, `HEAL_LOCATION_CRAGDALE` PROPOSED, landing at (13,14) outside the Pokémon Center door.

## 1. Description

**From R10 (the west).** The pass opens onto a **lane of cobbles under a rock face**: stacked quarry stone beside the road, two squat grey houses with slate roofs, a wind that never lets up. Above the lane the town rises in **two more terraces**, each a lighter grey than the last, with a red Pokémon Center roof halfway up and a **weather vane spinning on the top terrace**. Colour: grey stone, lichen green, brown thatch, the red of the Center roof. Sound: wind only (a faint hum of the vane). Music: `MUS_FALLARBOR` for the town (a dry, windblown tune), `MUS_POKE_CENTER` / `MUS_POKE_MART` as vanilla, `MUS_RUSTBORO` in the Weather Station (the tune the vanilla institute uses).

**From R11 (the east).** The player comes through a **notch in the ridge wall** onto the lane's east end. A one-way **ledge** drops away on the right (south-east) into the road they just walked; ahead, the lane runs west under the houses. A bench with a view faces back through the notch.

**The memorable view.** At the **north-east rail** of the top terrace (30,3) a **coin telescope** points south. It shows **Gildhaven's tower far away, 'glinting like a sales pitch'**, the only thing in the region that is out of scale. With the Feather Badge held, a second look picks out the top-floor light (the optional secret).

## 2. Street layout, in words

North at the top. Three terraces stacked on a ridge, joined by two short stair flights and a one-way ledge. `#` cliff, `:` terrace ground, `.` lane or street, `=` stairs, `r` viewpoint rail, `T` telescope, `b` Strength boulder, `c` Cut tree, `k` Rock Smash rock, `v` one-way ledge, `n` cave nook floor. Buildings: `W` Weather Station, `L` Climbers' Lodge, `H` Hostel, `P` Pokémon Center, `M` Mart, `A` House A, `B` House B, `Q` Quarry office, `C` House C; the digit in a building is its door.

```
      x: 0000000000111111111122222222223333
         0123456789012345678901234567890123
 y 0  |##################################|
 y 1  |##################################|
 y 2  |###::::::::::::::::::::::::rrrrr##|
 y 3  |###::WWWWWWW::::::::::LLLLLrrrTr##|
 y 4  |###::WWWWWWW::::::::::LLLLL::::###|
 y 5  |###::WWWWWWW::::::::::LLLLL::::###|
 y 6  |###::WWWWWWW::::::::::LLLLL::::###|
 y 7  |###::WWW1WWW::::::::::LL2LL::::###|
 y 8  |###::::::::::::::::::::::::b:::###|
 y 9  |################==################|
 y10  |##:HHHHHH::PPPPP:::MMMM:::::::::##|
 y11  |##:HHHHHH::PPPPP:::MMMM:::::::::##|
 y12  |##:HHHHHH::PPPPP:::MMMM:::::::::##|
 y13  |##:HHH3HH::PP4PP:::M5MM:::::::::##|
 y14  |##c.............................##|
 y15  |##..............................##|
 y16  |########################==########|
 y17  |:::AAAAA:BBBBB::QQQQQQ::::::CCCCC:|
 y18  |:::AAAAA:BBBBB::QQQQQQ::::::CCCCC:|
 y19  |:::AAAAA:BBBBB::QQQQQQ::::::CCCCC:|
 y20  |:::AA6AA:BB7BB::QQ8QQQ::::::CC9CC:|
 y21  |..................................|
 y22  |..................................|
 y23  |..................................|
 y24  |::::k:::::::::::::::::::::::::vvvv|
 y25  |::nnnnn:::::::::::::::::::::::::::|
 y26  |::nnnnn:::::::::::::::::::::::::::|
 y27  |::nnnnn:::::::::::::::::::::::::::|
```

Numbered walk:

1. **West edge (R10).** The lane enters at **(0,21)-(0,23)** (3 wide) and runs the full width of the **lower terrace** to the east edge. Quarry stone is stacked as decor along the south side (rows 24-26, cols 10-24, tile art: the rock-pile metatiles in the Fallarbor set).
2. **House A and House B** on the lane's north side, **doors (5,20) and (11,20)**. A low fence between them.
3. **Quarry office** at **cols 16-21, rows 17-20, door (18,20)**, with a pallet of cut blocks beside it.
4. **The way up.** North of the lane between the Quarry office and House C, a path at **cols 23-26, rows 17-20** leads to the **lower stairs (24,16)-(25,16)**.
5. **House C, door (30,20)**, and beside it the **one-way ledge** along **(30,24)-(33,24)** (jump south). The strip **(31,25)-(33,26)** below the ledge is part of R11's first stretch (see connections). The ledge is one way only: from R11 the player cannot climb it.
6. **East edge (R11).** The lane leaves at **(33,21)-(33,23)** through the notch.
7. **Middle terrace, the main street.** The street is **rows 14-15, cols 2-31**. From the west: the **Hostel** (cols 3-8, rows 10-13, door **(6,13)**), the **Pokémon Center** (cols 11-15, rows 10-13, door **(13,13)**), the **Mart** (cols 19-22, rows 10-13, door **(20,13)**). A **Cut tree at (2,14)** closes the west end of the street; behind it, a strip at (1,10)-(2,13) holds a Revive.
8. **Upper stairs** at **(16,9)-(17,9)**, above the gap between Center and Mart.
9. **Upper terrace (rows 2-8).** The **Weather Station** (cols 5-11, rows 3-7, door **(8,7)**), a wide grey building with an **instrument tower** (a vane object or a tall metatile) on its roof. The **Climbers' Lodge** (cols 22-26, rows 3-7, door **(24,7)**). East of the Lodge a **back yard** (cols 27-31, rows 4-8) behind a **Strength boulder at (27,8)**; north-east the **viewpoint rail** (cols 27-31, rows 2-3) and the **telescope (30,3)**.
10. **South-west nook.** Below the lane, the cave nook (cols 2-6, rows 25-27) behind a **Rock Smash rock at (4,24)**: Max Ether at (3,26).

**Palette and tile notes.** Fallarbor secondary: rock cliff (the terrace edges), ledge metatiles, short grass, stone fences, stacked-stone decor. Pale stone cobbles for the lane (the ORAS General path tile). Roofs: slate grey for houses, red for the Center (vanilla door animations `poke_center`, `poke_mart` already imported with the ORAS General). Draw the **instrument tower** from two existing tall metatiles (a lamp post and a tree base are common stand-ins) or a vane object; nothing needs new art.

## 3. Doors and warps (outdoor map `Cragdale`, 34 x 28)

| # | Tile | Destination (arrival) | Notes |
|---|---|---|---|
| 0 | (6,13) | `Cragdale_Hostel` (mat 5,8 and 6,8) | |
| 1 | (13,13) | `Cragdale_PokemonCenter_1F` (mat 6,8) | Fly lands at (13,14) |
| 2 | (20,13) | `Cragdale_Mart` (mat 3,7) | |
| 3 | (8,7) | `Cragdale_WeatherStation_1F` (mat 9,12) | |
| 4 | (24,7) | `Cragdale_ClimbersLodge` (mat 2,7) | |
| 5 | (5,20) | `Cragdale_HouseA` (mat 2,7) | |
| 6 | (11,20) | `Cragdale_HouseB` (mat 2,7) | |
| 7 | (18,20) | `Cragdale_QuarryOffice` (mat 2,7) | |
| 8 | (30,20) | `Cragdale_HouseC` (mat 2,7) | |

**Connections.**

| Edge | Neighbour | Offset | Lines up |
|---|---|---|---|
| West | `VeldrisRoute10` (64 x 23) east edge | +9 | R10's carved east exit (rows 12-14) meets the lane (rows 21-23) |
| East | `VeldrisRoute11` (67 x 25) west edge | +8 | R11's west road (rows 13-15) meets the lane; R11 rows 17-18 meet the ledge strip (rows 25-26) |
| North, South | none | | cliff |

Check both offsets in Porymap once the roads exist.

## 4. Interiors

Maps: `Cragdale_PokemonCenter_1F/_2F`, `_Mart`, `_WeatherStation_1F/_2F`, `_Hostel`, `_ClimbersLodge`, `_HouseA`, `_HouseB`, `_HouseC`, `_QuarryOffice`: **12 maps**. Interior section `MAPSEC_CRAGDALE`.

### 4.1 Pokémon Center and Mart (vanilla, unchanged)

`LAYOUT_POKEMON_CENTER_1F` (14 x 9) and `_2F` (14 x 10), `LAYOUT_MART` (11 x 8). Vanilla facts: Center nurse (7,2), mats (6,8) and (7,8), stairs up (1,6); 2F attendants (1,2), (2,2), (6,2), (10,2), exits (1,6) (5,1) (9,1). Mart clerk (1,3), mats (3,7) and (4,7). **Never move them.** Center flavour NPCs (3, on the vanilla tiles): a **hiker** (4,4) facing down, a **climber with a thermos** (10,6) facing right, a **child** (3,7) facing right. Mart: clerk (1,3), a **shopper** (5,5), the **shopkeeper's line about the boy in loafers** is the clerk's second topic. Stock per the card: Great Ball, Super Potion, Antidote, Repel, Super Repel, Escape Rope.

### 4.2 Weather Station: 1F (20 x 13) and 2F (20 x 11)

**Base:** vanilla `Route119_WeatherInstitute_1F/_2F`, `gTileset_Lab` (the tileset is already in the tree, no import). **Remove** the Aqua grunts, the cutscene triggers and the vanilla `LOCALID_WEATHER_INSTITUTE_*` scripts; keep the layout. Not a Team Aqua/Magma set, just the building.

**1F:** exit mats **(9,12) and (10,12)** (the vanilla warps), stairs up **(17,1)**. The vanilla **bed** (bg events at (0,2),(1,2),(0,3),(1,3)) stays as the **forecaster's cot** (a sign: 'A cot. Somebody sleeps through the gales.'). NPCs (4): **forecaster** (5,4) facing down (talks wind; the ridge never has anything else); **station hand** (15,3) facing left (recalibrating a dial); **weather kid** (14,11) wandering (wants to see the tower through the telescope but is too short); **instrument checker** (2,11) looking around. Signs: a wall barometer at (9,2) ('FAIR. FAIR. FAIR. WIND.'), a rain gauge at (11,2).

**2F:** stairs down **(17,1)**. NPCs (3): **station intern** (18,6) looking around (the logs: 'the tower's lights have never once gone off'), **log clerks** at (0,6) and (1,7) facing right (the vanilla non-scripted men). **Log shelf** (sign) at (9,2): 'TOWER LIGHTS: ON. ON. ON. ON. ON.'. Objects 3 of 15. The card has no gift here (the card's role line says 'the gift' but the Items table gives none): the **telescope secret** (outside) is its reward.

### 4.3 Ridge Hostel (12 x 9)

**Layout:** vanilla `LilycoveCity_CoveLilyMotel_1F` (12 x 9, `gTileset_GenericBuilding`) **keeps its geometry** so the vanilla free-rest script (owner heals the player) works: owner object at **(10,3)** facing up, mats **(5,8) and (6,8)**. Repaint in `gTileset_Gen4Interior` to match the Hollowbrook house style (bunk beds, kitchen block, window). Remove the stairs (2,1): Cragdale needs only one floor. NPCs (3): **keeper** (10,3) (tea, bunks, the thermos joke); a **walker asleep in a bunk** (3,3) facing down (a sleeping NPC); a **guest with a map** (7,5) wandering. The Cut-tree nook behind the Hostel is **outdoors** (see section 2).

### 4.4 Climbers' Lodge (11 x 8)

**Template N** = `Hollowbrook_NeighboursHouse` (11 x 8, built, mat (2,7), bookshelf signs (7,2),(8,2), free floor x 1-9, y 3-6). Repaint as a club hall: rope coils and ice picks as decor on the wall, a long table, framed photos of summits. NPCs (3): **Lodge elder** (8,3) facing down (gives **TM Rock Tomb** after the errand: carry a message to the Hostel keeper and break the rock in front of the nook, Rock Smash badge 2); a **member** (3,5) facing right (complains the boulder is where the view was); a **young climber** (6,6) facing up (the thermos joke's source).

### 4.5 Houses

| Map | Template and size | Interior in words | NPCs (tile, facing) |
|---|---|---|---|
| `Cragdale_HouseA` (quarryman) | N, 11 x 8 | slate dust on the shelf, a stone-cutter's tools on a rack | **quarryman** (8,3) facing up (quarry stone goes to Smeltham's foundry); his **wife** (5,6) facing up |
| `Cragdale_HouseB` (grandmother) | N, 11 x 8, mat at (2,7) | a rocking chair by the window, knitting, a photo of the footpath | **grandmother** (4,4) facing right (remembers when the road to Hoarfell was a footpath); a **Skitty** (8,5) looking around |
| `Cragdale_HouseC` (young family) | N, 11 x 8 | toys on the rug, a high chair | **mother** (5,6) facing up; **toddler** (8,4) wandering; **father** (9,3) facing left |
| `Cragdale_QuarryOffice` | 10 x 8 (shorter N), Gen 4 | a desk with a ledger, a map of the quarry on the wall | **clerk** (4,3) facing down (sells nothing, 'cannot sell you a rock') |

NPC topics are in the card ([../towns/cragdale.md](../towns/cragdale.md)).

## 5. NPCs outdoors (7 of 15 live objects)

| Role | Tile | Movement | Topic |
|---|---|---|---|
| Hiker | (10,3) | wander, upper terrace | recommends R10's ponds for a rest |
| Child | (28,3) | face down | wants the telescope but is too short |
| Lodge member | (30,6) | face left, back yard | complains about the boulder |
| Quarry worker | (14,22) | look around, lane | cut blocks go to Smeltham |
| Weather watcher | (8,8) | face up, under the Station | points at the instruments |
| Walker | (17,15) | wander, street | asks the way to Hoarfell |
| Window-shopper | (18,14) | face up | looks at the Mart: 'A boy in loafers asked here for a nicer ridge' (shopkeeper's line spoken by her) |

Signs: town sign at (1,20) by the west entry ('CRAGDALE, ridge town. Mind the wind.'), a street sign at (15,15), the Station sign (7,8), the Lodge sign (23,8).

## 6. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| **TM Rock Tomb** | Lodge elder | Rock Smash plus the Hostel errand |
| Max Ether | cave nook (3,26) behind the rock (4,24) | Rock Smash |
| Revive | strip behind the Hostel (2,12) | Cut tree at (2,14) |
| Hyper Potion | back yard (30,6) | Strength boulder at (27,8) |
| Great Ball (visible) | lower terrace (22,25) | none |
| Escape Rope (hidden) | upper rail (29,3) | none |
| Super Repel (hidden) | behind the Mart (21,9) | none |
| **Secret** | telescope (30,3) with the Feather Badge: the top-floor light; optional one-line payoff in Gildhaven | the Feather Badge |

## 7. Build checklist (in order)

1. Import ORAS `fallarbor` (CREDITS row) in the first commit that uses it. Build `Cragdale` 34 x 28 per section 2 (terraces, cliffs, ledge), doors per section 3. Save, then check `event_scripts.s` for the single `.include`, `heal_locations.json` ids ([../../../CLAUDE.md](../../../CLAUDE.md)).
2. Add `MAPSEC_CRAGDALE` and the fly row (`src/data/veldris_fly_towns.h`; the checklist in [../../region-map.md](../../region-map.md)).
3. Shared Center and Mart, then the Weather Station (two maps), Hostel, Lodge.
4. Four houses by duplicating Hollowbrook's neighbour's house.
5. Connections to R10 and R11 once those maps exist; the Cut tree, Rock Smash rock, Strength boulder and the ledge.
6. Scripts (gift, errand, telescope), dialogue (`python3 design/tools/dialogue_check.py`), `design/` updates, CREDITS, `make -j4`, check no ROM staged.

## 8. Open questions

1. Is the **one-way ledge into R11** worth the offset fiddle (it needs R11's rows 17-18 to line up with Cragdale's rows 25-26)? Cheap to drop.
2. **Weather Station vs plain rest stop.** It costs two maps for jokes and a telescope secret. The Station could be a single-room house if the author wants a smaller Cragdale.
3. **Palladium Route 42 is used twice**: for R10 (this group) and R13 (the east group, [../routes-east.md](../routes-east.md)). Mirror one of them (see [routes-centre-detail.md](routes-centre-detail.md)).
4. **Hostel layout:** keep vanilla's motel geometry (for the free-rest script) or write a new rest script for a smaller room?
5. **TM Rock Tomb** as the gift and a Rock Smash errand: confirm, or swap for a gift that does not need a second badge.
