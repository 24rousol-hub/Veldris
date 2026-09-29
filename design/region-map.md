# Region map and fly destinations

How a map gets onto the town map and becomes a fly destination in this tree. Everything below was traced in the source of this repository (file names and function names given), except where marked **unverified**.

## What I could not read

Two sources were requested and the environment's network policy blocked both hosts:

- `huderlem.github.io` (Porymap's Region Map Editor manual)
- `www.pokecommunity.com` (the "Guide to Editing the Region Map" thread)

So **nothing here is taken from those pages.** Anything about what Porymap's Region Map Editor does with these files is marked **unverified**. To let me read them, add those two hosts under Network access in the environment settings.

## The town map and fly, in plain language

The **town map** (Pokénav's region map) and the **Fly** picker are the same screen and the same data. Six pieces connect a map to them:

1. **Each map names its section.** Every `data/maps/<Map>/map.json` has `"region_map_section": "MAPSEC_..."`. A section is a named place: a town, a route, a cave. A town and all its houses can share one section. The name popup when you enter a map comes from this too.
2. **Each section has a record.** `src/data/region_map/region_map_sections.json` holds, per section: `id`, `name` (what the player sees), and `x`, `y`, `width`, `height` (where it sits on the map, in cells). The build turns this file into the `MAPSEC_*` list (`include/constants/region_map_sections.h`) and the `gRegionMapEntries` table. Do not edit those two generated files.
3. **A grid says which cell belongs to which section.** `sRegionMap_MapSectionLayout[15][28]` in `src/data/region_map/region_map_layout.h`. The cursor moves cell by cell and shows the name of the section in the cell it is on. The `x/y/width/height` in step 2 must agree with this grid.
4. **The picture is separate.** What you see is drawn from 8x8 tiles: `graphics/pokenav/region_map/map.png` (the tile sheet, 128x120 indexed), `map.bin` (the tilemap, 2048 entries) and `map.pal`. So the picture, the grid and the JSON are three things kept in step, not one.
5. **Whether a town can be flown to is decided in C, not data.** Three places in `src/region_map.c`:
   - `GetMapsecType()` is a `switch` that says "this section is a city, and it is flyable once *this flag* is set". Any section not listed there is treated as a plain route.
   - `sFlyLocations[]` is the list of fly icons: region, flag, section.
   - `sMapHealLocations[]` (plus `FilterFlyDestination()`) says where you land. Normally it is a **heal location** from `src/data/heal_locations.json`, the spot outside the Pokémon Center. Failing that, it uses the map's warp.
6. **The visited flag is set by the town's own script.** For example `LittlerootTown_OnTransition` runs `setflag FLAG_VISITED_LITTLEROOT_TOWN` (`data/maps/LittlerootTown/scripts.inc`). Until that runs, the town shows on the map but cannot be flown to.

Which region map you get (Hoenn, Kanto, Sevii) comes from the section's number: sections in the Kanto block (`KANTO_MAPSEC_START` to `KANTO_MAPSEC_END`) use the Kanto map, and **anything else uses the Hoenn map** (`GetRegionMapType`). Veldris will therefore use the Hoenn map, and new sections must go at the **end** of the JSON list, never inside the Kanto block.

## What this means for Veldris

**Data only (no C):** section names, positions, the grid, the picture, heal locations, and each map's `region_map_section`.

**C edits, three small ones per fly town, all in `src/region_map.c`:** a `GetMapsecType` case, an `sFlyLocations` entry and an `sMapHealLocations` entry. Alongside those, the data side needs a claimed visited flag ([flags.md](flags.md)), a heal location in `src/data/heal_locations.json`, and the town's `OnTransition` setting the flag. Routes need no C: an unlisted section is a route.

**Limits found:**

- **Map sections are 8-bit and share their value space with `0xFD-0xFF`** (special met-location codes). 209 sections already exist, so **at most 43 more fit.** Veldris wants 51 (18 towns and 33 routes) before any caves or landmarks. So at least 8 sections have to reuse the IDs of vanilla sections we no longer need (rename their record only), or vanilla content has to be stripped later. Not blocking the first 3 towns and 3 routes.
- **Popup themes.** `sMapSectionToThemeId` in `src/map_name_popup.c` sets each section's popup style. New sections default to theme 0 until a line is added.
- **Name clashes.** FRLG already owns `MAPSEC_ROUTE_1` to `MAPSEC_ROUTE_25`. See [towns-and-routes.md](towns-and-routes.md).

## Checklist: add one fly town

1. Author (Porymap): make the map. Set `region_map_section` to the town's section.
2. Add the section record to the **end** of `region_map_sections.json` (id, name, x, y, width, height).
3. Update the grid and the picture so the new cell shows the town (author, Region Map Editor; **unverified** that the editor covers all three files).
4. Add a heal location in `src/data/heal_locations.json`.
5. Claim a visited flag ([flags.md](flags.md), log it in [engine-edits.md](engine-edits.md)).
6. `src/region_map.c`: add the `GetMapsecType` case, the `sFlyLocations` entry and the `sMapHealLocations` entry.
7. Town's `OnTransition` script: `setflag <the flag>`.
8. `make -j4`, then fly there in an emulator.

## Decision needed before the first fly town (PROPOSED default: A)

| | A. Add new sections and edit the C tables | B. Reuse an unused Hoenn town's slot |
|---|---|---|
| C edits | 3 small ones per town | None |
| Names | Clean (`MAPSEC_HOLLOWBROOK`, own flag) | Hoenn-named (`Hollowbrook` would sit in `MAPSEC_OLDALE_TOWN` and set `FLAG_VISITED_OLDALE_TOWN`) |
| Section budget | Uses up the 43 spare IDs | Saves them |
| Fits 18 towns? | Yes, until IDs run out | Only about 14 slots, since Littleroot and Ever Grande have special cases |

Recommendation: **A**, and reuse vanilla IDs for the remainder once the spare IDs are gone.

---

# Veldris layout proposal (PROPOSED, not approved)

A first layout for the whole region: **18 towns, 33 routes** (30 on land, 3 by sea). Only towns 1 to 3 and routes 1 to 3 are meant to be built first, so all three towns can be flown between.

**Native size, 256x160** (the whole Pokénav screen). One cell is 8x8 px. The cursor grid is 28 x 15 cells and starts at tile (1, 2), i.e. pixel (8, 16) (`MAPCURSOR_X_MIN` and `MAPCURSOR_Y_MIN` in `src/region_map.c`). The first three towns and routes have a gold outline.

![Veldris layout at 256x160](veldris-layout-256x160.png)

**Labelled, 4x** ([open it full size](veldris-layout-annotated.png)):

![Veldris layout, labelled](veldris-layout-annotated.png)

## How to read it

- Farm country in the south-west (the start). Sea along the east and south. Mountains in the north-west and north-east. A lake in the middle, ringed by routes. These are only painted hints for you to reshape.
- Every route is a straight one-cell corridor, so each route is one rectangle (`x, y, width, height`) in the section list. That keeps the grid simple. Bend them if you prefer, but then the section rectangle and the grid must be kept in agreement.
- The town order T4 to T18 follows a suggested main path. It is **not** the gym order. Only T3 (Crestfall, gym 1) is fixed.
- Route 3 leaves Crestfall and stays blocked (gate or barricade) until town 4 exists. Routes 27 to 33 are dead ends and sea routes for later.
- This is a plan, not the final art. The game draws the map from 8x8 tiles and a tilemap (`graphics/pokenav/region_map/`), so the picture is painted with tiles later, in the Region Map Editor.

## Numbers

- 18 towns and 33 routes. 128 of the 420 cells are used. Every town is reachable from town 1 (checked).
- **Section budget:** 18 + 33 = 51 sections, against about 43 spare IDs. See "Limits found" above. The first 6 fit easily.

## Section list

`x`, `y`, `w`, `h` are in cells and match what `region_map_sections.json` needs. Names are placeholders.

| # | Section id | Name shown | x | y | w | h | Status |
|---|---|---|---|---|---|---|---|
| T1 | `MAPSEC_HOLLOWBROOK` | HOLLOWBROOK | 2 | 12 | 1 | 1 | **build first** |
| T2 | `MAPSEC_WENDLEBURY` | WENDLEBURY | 7 | 12 | 1 | 1 | **build first** |
| T3 | `MAPSEC_CRESTFALL` | CRESTFALL | 7 | 8 | 1 | 1 | **build first** |
| T4 | `MAPSEC_VELDRIS_TOWN_04` | TOWN 04 | 12 | 8 | 1 | 1 | planned |
| T5 | `MAPSEC_VELDRIS_TOWN_05` | TOWN 05 | 12 | 12 | 1 | 1 | planned |
| T6 | `MAPSEC_VELDRIS_TOWN_06` | TOWN 06 | 17 | 12 | 1 | 1 | planned |
| T7 | `MAPSEC_VELDRIS_TOWN_07` | TOWN 07 | 22 | 12 | 1 | 1 | planned |
| T8 | `MAPSEC_VELDRIS_TOWN_08` | TOWN 08 | 22 | 8 | 1 | 1 | planned |
| T9 | `MAPSEC_VELDRIS_TOWN_09` | TOWN 09 | 17 | 8 | 1 | 1 | planned |
| T10 | `MAPSEC_VELDRIS_TOWN_10` | TOWN 10 | 17 | 4 | 1 | 1 | planned |
| T11 | `MAPSEC_VELDRIS_TOWN_11` | TOWN 11 | 22 | 4 | 1 | 1 | planned |
| T12 | `MAPSEC_VELDRIS_TOWN_12` | TOWN 12 | 22 | 1 | 1 | 1 | planned |
| T13 | `MAPSEC_VELDRIS_TOWN_13` | TOWN 13 | 12 | 4 | 1 | 1 | planned |
| T14 | `MAPSEC_VELDRIS_TOWN_14` | TOWN 14 | 7 | 4 | 1 | 1 | planned |
| T15 | `MAPSEC_VELDRIS_TOWN_15` | TOWN 15 | 2 | 4 | 1 | 1 | planned |
| T16 | `MAPSEC_VELDRIS_TOWN_16` | TOWN 16 | 2 | 8 | 1 | 1 | planned |
| T17 | `MAPSEC_VELDRIS_TOWN_17` | TOWN 17 | 12 | 1 | 1 | 1 | planned |
| T18 | `MAPSEC_VELDRIS_TOWN_18` | TOWN 18 | 17 | 1 | 1 | 1 | planned |
| R1 | `MAPSEC_VELDRIS_ROUTE_1` | ROUTE 1 | 3 | 12 | 4 | 1 | **build first** |
| R2 | `MAPSEC_VELDRIS_ROUTE_2` | ROUTE 2 | 7 | 9 | 1 | 3 | **build first** |
| R3 | `MAPSEC_VELDRIS_ROUTE_3` | ROUTE 3 | 8 | 8 | 4 | 1 | **build first** |
| R4 | `MAPSEC_VELDRIS_ROUTE_4` | ROUTE 4 | 12 | 9 | 1 | 3 | planned |
| R5 | `MAPSEC_VELDRIS_ROUTE_5` | ROUTE 5 | 13 | 12 | 4 | 1 | planned |
| R6 | `MAPSEC_VELDRIS_ROUTE_6` | ROUTE 6 | 18 | 12 | 4 | 1 | planned |
| R7 | `MAPSEC_VELDRIS_ROUTE_7` | ROUTE 7 | 22 | 9 | 1 | 3 | planned |
| R8 | `MAPSEC_VELDRIS_ROUTE_8` | ROUTE 8 | 18 | 8 | 4 | 1 | planned |
| R9 | `MAPSEC_VELDRIS_ROUTE_9` | ROUTE 9 | 17 | 5 | 1 | 3 | planned |
| R10 | `MAPSEC_VELDRIS_ROUTE_10` | ROUTE 10 | 18 | 4 | 4 | 1 | planned |
| R11 | `MAPSEC_VELDRIS_ROUTE_11` | ROUTE 11 | 13 | 4 | 4 | 1 | planned |
| R12 | `MAPSEC_VELDRIS_ROUTE_12` | ROUTE 12 | 8 | 4 | 4 | 1 | planned |
| R13 | `MAPSEC_VELDRIS_ROUTE_13` | ROUTE 13 | 3 | 4 | 4 | 1 | planned |
| R14 | `MAPSEC_VELDRIS_ROUTE_14` | ROUTE 14 | 2 | 5 | 1 | 3 | planned |
| R15 | `MAPSEC_VELDRIS_ROUTE_15` | ROUTE 15 | 2 | 9 | 1 | 3 | planned |
| R16 | `MAPSEC_VELDRIS_ROUTE_16` | ROUTE 16 | 8 | 12 | 4 | 1 | planned |
| R17 | `MAPSEC_VELDRIS_ROUTE_17` | ROUTE 17 | 7 | 5 | 1 | 3 | planned |
| R18 | `MAPSEC_VELDRIS_ROUTE_18` | ROUTE 18 | 13 | 8 | 4 | 1 | planned |
| R19 | `MAPSEC_VELDRIS_ROUTE_19` | ROUTE 19 | 17 | 9 | 1 | 3 | planned |
| R20 | `MAPSEC_VELDRIS_ROUTE_20` | ROUTE 20 | 12 | 5 | 1 | 3 | planned |
| R21 | `MAPSEC_VELDRIS_ROUTE_21` | ROUTE 21 | 22 | 5 | 1 | 3 | planned |
| R22 | `MAPSEC_VELDRIS_ROUTE_22` | ROUTE 22 | 12 | 2 | 1 | 2 | planned |
| R23 | `MAPSEC_VELDRIS_ROUTE_23` | ROUTE 23 | 17 | 2 | 1 | 2 | planned |
| R24 | `MAPSEC_VELDRIS_ROUTE_24` | ROUTE 24 | 13 | 1 | 4 | 1 | planned |
| R25 | `MAPSEC_VELDRIS_ROUTE_25` | ROUTE 25 | 22 | 2 | 1 | 2 | planned |
| R26 | `MAPSEC_VELDRIS_ROUTE_26` | ROUTE 26 | 18 | 1 | 4 | 1 | planned |
| R27 | `MAPSEC_VELDRIS_ROUTE_27` | ROUTE 27 | 2 | 13 | 1 | 2 | planned |
| R28 | `MAPSEC_VELDRIS_ROUTE_28` | ROUTE 28 | 23 | 12 | 4 | 1 | planned (sea route) |
| R29 | `MAPSEC_VELDRIS_ROUTE_29` | ROUTE 29 | 22 | 13 | 1 | 2 | planned (sea route) |
| R30 | `MAPSEC_VELDRIS_ROUTE_30` | ROUTE 30 | 2 | 1 | 1 | 3 | planned |
| R31 | `MAPSEC_VELDRIS_ROUTE_31` | ROUTE 31 | 7 | 1 | 1 | 3 | planned |
| R32 | `MAPSEC_VELDRIS_ROUTE_32` | ROUTE 32 | 23 | 1 | 4 | 1 | planned |
| R33 | `MAPSEC_VELDRIS_ROUTE_33` | ROUTE 33 | 23 | 8 | 4 | 1 | planned (sea route) |

## Route connections

| Route | From | To | Kind |
|---|---|---|---|
| R1 | T1 Hollowbrook | T2 Wendlebury | land |
| R2 | T2 Wendlebury | T3 Crestfall | land |
| R3 | T3 Crestfall | T4 | land |
| R4 | T4 | T5 | land |
| R5 | T5 | T6 | land |
| R6 | T6 | T7 | land |
| R7 | T7 | T8 | land |
| R8 | T8 | T9 | land |
| R9 | T9 | T10 | land |
| R10 | T10 | T11 | land |
| R11 | T10 | T13 | land |
| R12 | T13 | T14 | land |
| R13 | T14 | T15 | land |
| R14 | T15 | T16 | land |
| R15 | T16 | T1 Hollowbrook | land |
| R16 | T2 Wendlebury | T5 | land |
| R17 | T3 Crestfall | T14 | land |
| R18 | T4 | T9 | land |
| R19 | T6 | T9 | land |
| R20 | T13 | T4 | land |
| R21 | T11 | T8 | land |
| R22 | T13 | T17 | land |
| R23 | T10 | T18 | land |
| R24 | T17 | T18 | land |
| R25 | T11 | T12 | land |
| R26 | T12 | T18 | land |
| R27 | T1 Hollowbrook | dead end / sea | dead end |
| R28 | T7 | dead end / sea | sea (Surf) |
| R29 | T7 | dead end / sea | sea (Surf) |
| R30 | T15 | dead end / sea | dead end |
| R31 | T14 | dead end / sea | dead end |
| R32 | T12 | dead end / sea | dead end |
| R33 | T8 | dead end / sea | sea (Surf) |

## Ready to paste for the first six (do not add yet)

These are the six records for `src/data/region_map/region_map_sections.json`. They go at the **end** of the list, and only after the maps exist and decision A or B above is made.

```json
[
  {
    "id": "MAPSEC_HOLLOWBROOK",
    "name": "HOLLOWBROOK",
    "x": 2,
    "y": 12,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_WENDLEBURY",
    "name": "WENDLEBURY",
    "x": 7,
    "y": 12,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_CRESTFALL",
    "name": "CRESTFALL",
    "x": 7,
    "y": 8,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_1",
    "name": "ROUTE 1",
    "x": 3,
    "y": 12,
    "width": 4,
    "height": 1
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_2",
    "name": "ROUTE 2",
    "x": 7,
    "y": 9,
    "width": 1,
    "height": 3
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_3",
    "name": "ROUTE 3",
    "x": 8,
    "y": 8,
    "width": 4,
    "height": 1
  }
]
```

## What I need from you

1. Do you like the shape, or should it be reshaped (a different start corner, a bigger sea, a ring road)?
2. Are Hollowbrook and Wendlebury fine as names for towns 1 and 2? (Crestfall comes from your `TRAINER_CRESTFALL_GRETA`.)
3. Decision A or B above for fly towns.
