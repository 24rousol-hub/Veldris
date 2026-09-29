# Region map and fly destinations

How a map gets onto the town map and becomes a fly destination in this tree. Everything below was traced in the source of this repository (file names and function names given), except where marked **unverified**. The Porymap manual was read on 2026-09-29 (see below).

## What the Porymap manual says (read 2026-09-29)

Source: <https://huderlem.github.io/porymap/manual/region-map-editor.html>, plus the "Project Files" page of the same manual. **The PokéCommunity guide could not be read**: `www.pokecommunity.com` answered HTTP 403 to the fetch tool. It was not worked around. Nothing here comes from that thread.

What the Region Map Editor (Tools > Region Map Editor, Ctrl+M) does:

- **Three tabs:** *Background Image* (paint the tilemap), *Map Layout* (which section each cell belongs to) and *Map Entries* (each section's x, y, width, height). This matches pieces 2, 3 and 4 below, so one tool covers all three.
- **Background Image** writes the tilemap binary (the `map.bin` of piece 4). The manual does not say whether it regenerates it or edits it in place, and it says nothing about a tile limit. The 256-tile limit below is from the engine, not the manual. Tilemap "format" can be Plain, 4bpp or 8bpp; only non-Plain formats give per-tile palette and flips. Width can be 16, 32, 64 or 128 tiles.
- **Map Layout** writes the layout file (C array or binary). The vanilla one is `sRegionMap_MapSectionLayout` in `src/data/region_map/region_map_layout.h`. The Map Section dropdown is filled from `include/constants/region_map_sections.h`, so **a new section must exist in `region_map_sections.json` before the editor can place it.** (The manual says the dropdown comes from the generated header, but Porymap's source reads the JSON directly, so no build is needed.) Handy tools: Clear Map Layout, Swap Layout Sections, Replace Layout Section.
- **Map Entries** edits `src/data/region_map/region_map_sections.json`. x and y are the top-left cell; width and height set the size. The manual says the entry decides "where the player's head appears".
- **Config:** the editor's own settings live in `src/data/region_map/porymap_config.json` (Project Files page lists it as read and written; key `json_region_porymap_cfg`). It holds the per-region alias, tilemap and layout paths and sizes. **This file does not exist in this repo yet**, so Porymap will use its pokeemerald defaults. It is fine to commit the file Porymap creates. The Project Files page also lists `define_map_section_prefix` (`MAPSEC_`) and `define_map_section_empty` (`NONE`) as project settings, which our constants already follow.
- **Not in the manual:** any section-count limit, any tile limit, any mention of `name_clone`, and whether the picture step keeps or rewrites other files. Those stay engine facts.

**`name_clone`:** not on either manual page. In this tree it appears on 4 of the 209 vanilla records in `region_map_sections.json` (the `ROUTE_4_POKECENTER`-style records) and **no build template or C file reads it** (checked with grep). So it does nothing to the build. Most likely a marker that the record only repeats another section's name. Treat it as optional and do not set it on Veldris sections.

**Correction to earlier notes:** the editor does cover all three of the picture, the grid and the JSON, so step 3 of the checklist is confirmed by the manual. What is still unverified is only how it treats `map.bin` internally and the untested-in-game claims below.

## The town map and fly, in plain language

The **town map** (Pokénav's region map) and the **Fly** picker are the same screen and the same data. Six pieces connect a map to them:

1. **Each map names its section.** Every `data/maps/<Map>/map.json` has `"region_map_section": "MAPSEC_..."`. A section is a named place: a town, a route, a cave. A town and all its houses can share one section. The name popup when you enter a map comes from this too.
2. **Each section has a record.** `src/data/region_map/region_map_sections.json` holds, per section: `id`, `name` (what the player sees), and `x`, `y`, `width`, `height` (where it sits on the map, in cells). The build turns this file into the `MAPSEC_*` list (`include/constants/region_map_sections.h`) and the `gRegionMapEntries` table. Do not edit those two generated files.
3. **A grid says which cell belongs to which section.** `sRegionMap_MapSectionLayout[15][28]` in `src/data/region_map/region_map_layout.h`. The cursor moves cell by cell and shows the name of the section in the cell it is on. The `x/y/width/height` in step 2 must agree with this grid.
4. **The picture is separate.** What you see is drawn from 8x8 tiles: `graphics/pokenav/region_map/map.png` (the tile sheet, 128x120, 8-bit indexed), `map.bin` (the tilemap: 4096 bytes, one byte per tile position) and `map.pal`. **A byte holds only 256 different tile numbers, so the picture can use at most 256 distinct 8x8 tiles.** Hoenn's uses 233. So the picture, the grid and the JSON are three things kept in step, not one.
5. **Whether a town can be flown to is decided in C, not data.** Three places in `src/region_map.c`:
   - `GetMapsecType()` is a `switch` that says "this section is a city, and it is flyable once *this flag* is set". Any section not listed there is treated as a plain route.
   - `sFlyLocations[]` is the list of fly icons: region, flag, section.
   - `sMapHealLocations[]` (plus `FilterFlyDestination()`) says where you land. Normally it is a **heal location** from `src/data/heal_locations.json`, the spot outside the Pokémon Center. Failing that, it uses the map's warp.
6. **The visited flag is set by the town's own script.** For example `LittlerootTown_OnTransition` runs `setflag FLAG_VISITED_LITTLEROOT_TOWN` (`data/maps/LittlerootTown/scripts.inc`). Until that runs, the town shows on the map but cannot be flown to.

Which region map you get (Hoenn, Kanto, Sevii) comes from the section's number: sections in the Kanto block (`KANTO_MAPSEC_START` up to, but not including, `MAPSEC_SPECIAL_AREA`; `include/regions.h`) use the Kanto map, and **anything else uses the Hoenn map** (`GetRegionMapType`). Veldris will therefore use the Hoenn map, and new sections must go at the **end** of the JSON list, never inside the Kanto block.

## What this means for Veldris

**Data only (no C):** section names, positions, the grid, the picture, heal locations, and each map's `region_map_section`.

**C edits: none per town any more.** The A-prime hooks (applied, see below) mean each fly town is one row in `src/data/veldris_fly_towns.h`. Alongside that, the data side needs a claimed visited flag ([flags.md](flags.md)), a heal location in `src/data/heal_locations.json`, and the town's `OnTransition` setting the flag. Routes need no C: an unlisted section is a route.

**Limits found:**

- **Map sections are 8-bit and share their value space with `0xFD-0xFF`** (special met-location codes). 209 sections existed in vanilla, so **at most 43 more fit.** The first six Veldris sections were added on 2026-09-29, so 215 exist and **37 more fit**. Veldris wants 51 (18 towns and 33 routes) before any caves or landmarks. So 45 are still to add against 37 left, and at least 8 sections have to reuse the IDs of vanilla sections we no longer need (rename their record only), or vanilla content has to be stripped later. Not blocking the first 3 towns and 3 routes.
- **Popup themes.** `sMapSectionToThemeId` in `src/map_name_popup.c` sets each section's popup style. New sections default to theme 0 until a line is added.
- **Name clashes.** FRLG already owns `MAPSEC_ROUTE_1` to `MAPSEC_ROUTE_25`. See [towns-and-routes.md](towns-and-routes.md). The FRLG maps themselves are not built into this Emerald ROM (`mapjson` skips every map not tagged `REGION_HOENN`), but their `MAP_*` and `MAPSEC_*` constants still exist as placeholders.
- **Tile budget.** At most 256 distinct 8x8 tiles in the picture (see piece 4). The finished art has to reuse tiles heavily: repeating sea, grass and mountain tiles and a small set of coast and road pieces.
- **Names** are at most 16 characters, charmap characters only (no double quote).
- **Heal locations.** Each flyable section needs a row in `sMapHealLocations`, which is indexed by section number (a gap row is all zeros). The build also rewrites `heal_locations.json` when a heal location's `respawn_map` does not exist yet, so add a heal location only after its Pokémon Center map exists.
- **Fly is gated.** In this build Fly needs the Feather Badge (`src/field_move.c`), and a town only becomes flyable after the player has walked into it once (its `OnTransition` sets the flag). To test flying between the first three towns early, use the debug menu, or point `OW_FLAG_POKE_RIDER` (`include/config/overworld.h`) at a spare flag, which lets you open the fly map from the Pokénav without the HM. The config route is untested in game.
- **No city zoom picture is needed, but the Pokénav panel is untidy without one.** `NUM_CITY_MAPS` is 22 and all are Hoenn towns. For a flyable town with no picture, `DrawCityMap` (`src/pokenav_region_map.c` about line 664) returns early without clearing the picture area, so the previous town's picture can stay on screen (read from source, not run). It does not affect the Fly map. A fix is a small engine edit that needs the author's approval.
- **The 16 vanilla Hoenn fly towns stay.** The hooks only add rows. `CreateFlyDestIcons` still draws the 16 vanilla locked-town icons at the vanilla sections' x/y. When the Veldris picture replaces Hoenn's, either move or reuse those 16 section records, or add a hack-owned way to drop vanilla rows (an engine edit, needs approval).
- **Rows need ids after `MAPSEC_TRAINER_HILL`.** `VELDRIS_FLY_ROW` hard-codes `REGION_MAP_HOENN`, and the engine picks the region map from the section id. A row in the Kanto block would sit on the wrong region map: it has no cell on the Hoenn grid so it cannot be selected, and its icon appears or not depending on which region the player is standing in. New ids appended after `MAPSEC_TRAINER_HILL` are fine.

## Checklist: add one fly town

Checked by a dry run on 2026-09-29: a throwaway Hollowbrook section, flag, heal location and table row were added in a scratch copy of the repo (no map files) and it built. Upstream files touched are marked **U**: log each in [engine-edits.md](engine-edits.md).

Order matters. Steps 1 and 2 build on their own. Step 7 needs steps 3 and 6. Step 9 needs 1, 2, 3 and 7.

1. **U** `src/data/region_map/region_map_sections.json`: append one record at the very END of the list. It must stay after `MAPSEC_TRAINER_HILL`, so the Kanto block is not disturbed (today the last record is `MAPSEC_VELDRIS_ROUTE_3`). Uppercase name, 16 characters at most. Porymap reads this JSON directly, so its Location dropdown offers the new `MAPSEC_*` without a build.
2. **U** `include/constants/flags.h`: rename the spare `FLAG_UNUSED_0x0NN` to `FLAG_VISITED_<TOWN>` (keep the value; 0x020-0x031 are reserved for this). Add the row in [flags.md](flags.md).
3. Author, Porymap: the town map. `region_map_section` is the new section, `show_map_name` true, `map_type` `MAP_TYPE_TOWN`, group 0 (`gMapGroup_TownsAndRoutes`), `region` and `layout_version` at the defaults. Every interior of the town uses the same `region_map_section` as the town.
4. **U** `data/event_scripts.s`: Porymap appends the `.include "data/maps/<Name>/scripts.inc"` line itself on the first save of a new map. Check it is there exactly once. Add it by hand only for a map made without Porymap.
5. The town's `scripts.inc`: the `OnTransition` script does `setflag FLAG_VISITED_<TOWN>`. Nothing else sets it, and it only runs when the town map itself loads.
6. The town's Pokémon Center 1F map must exist before step 7, and its nurse object needs a `local_id` (for example `LOCALID_HOLLOWBROOK_NURSE`).
7. **U** `src/data/heal_locations.json`: append an entry at the END. `x`/`y` is where a flying player lands, so it must be a walkable town tile outside the Center door (Fly does not check that the tile is walkable). Rules found by test:
   - The map, the `respawn_map` and the `LOCALID_*` must already exist, or the generated header fails to compile.
   - Write `respawn_map` BEFORE `respawn_npc`. `mapjson` rewrites the file line by line, and if `respawn_map` is not a valid map it zeroes the next `LOCALID_*` line, which can be another entry's.
   - Always give both respawn fields. Without `respawn_npc`, the whiteout tables come out one entry short and a later whiteout reads past the array (`src/heal_location.c` about line 80; read from source, not run). `"respawn_npc": "LOCALID_NONE"` is fine when there is no nurse cutscene.
   - Never edit the generated `include/constants/heal_locations.h` or `src/data/heal_locations.h`; they are gitignored.
8. The Center's `OnTransition`: `setrespawn HEAL_LOCATION_<TOWN>`, only after step 7 (the constant comes from the JSON).
9. `src/data/veldris_fly_towns.h`: add the row. Every row ends with a backslash except the last one.
10. **U** `src/data/region_map/region_map_layout.h`: put the section in its grid cell, so the cursor lands on it and shows the name (author, Region Map Editor). Nothing checks that the grid agrees with the section's x/y/width/height.
11. **U** `graphics/pokenav/region_map/map.png` and `map.bin`: the picture. Art only. Name, cursor, icon and Fly all work without it.
12. Optional, **U**: a popup theme in `src/map_name_popup.c` (the default is the wood frame), and the debug flag list in `src/debug.c`.
13. `make -j4`, then test: walk into the town, then debug menu (R+START) > Fly to map, and check the name, the red icon, the landing tile and the popup. Warnings are errors in this build.

A town with two heal spots, or a subtitle name (like Ever Grande), needs `FilterFlyDestination` and `sMultiNameFlyDestinations` edits in `src/region_map.c`. Not covered by the hooks.

## Decision on fly towns: approach A-prime (author: "whatever is best for the future")

| | A. New sections, edit the C tables per town | B. Reuse an unused Hoenn town's slot | **A-prime (chosen)** |
|---|---|---|---|
| C edits | 3 small ones per town, in an upstream file | None | **One small change once**, then none per town |
| Names | Clean | Hoenn-named | Clean |
| Section budget | Uses the 43 spare IDs | Saves them | Uses them, reuse vanilla IDs for routes later |
| Fits 18 towns? | Yes, until IDs run out | Only about 14 slots | Yes |
| Upstream merges | 54 edit sites for 18 towns | Few | **A handful of hook sites** |

**A-prime:** new sections with clean names, but instead of adding three entries per town inside `src/region_map.c`, make one small one-time change there. It adds one include and three table-tail lines (the heal-location table, the `GetMapsecType` switch and the fly-icon table) that also read a **hack-owned table** in a new file (for example `src/data/veldris_fly_towns.h`, one row per town: section, visited flag, heal location). After that, adding a fly town is one table row plus data, and the upstream file is touched in only those few places, which keeps upstream pulls cheap.

**Applied 2026-09-29** (see below). Routes need no C at all, so once the 43 spare section IDs are used, routes can take over unused vanilla section IDs by renaming their records.

## A-prime: APPLIED 2026-09-29 (author: "Yes apply"), table still empty

Applied by the other session with `src/data/veldris_fly_towns.h` and four added lines in `src/region_map.c`, logged in [engine-edits.md](engine-edits.md). The table is empty, so nothing changes in game yet.

**Checked 2026-09-29:**
- Two independent reviews found no defects in the hooks. With the table empty, each hooked path compiles and behaves as vanilla did (compiled with the Makefile's flags including `-Werror`, with and without LTO). One row compiled clean, and a dry-run town built and linked.
- The ROM boots in an emulator, the intro plays and the trainer card works. That does not exercise Fly, because no town is in the table yet.
- Not tested in game: icons, cursor snapping, popup text, landing position.

**The four hook sites in `src/region_map.c`** (line numbers as of this check, they will drift):

| Line | Site | What the hook does |
|---|---|---|
| 31 | includes | `#include "data/veldris_fly_towns.h"` |
| 539 | end of `sMapHealLocations[][3]` | `VELDRIS_HEAL_LOCATION_ROWS`: designated-index rows, so the array grows to the highest section id. This is what `SetFlyDestination` and `FilterFlyDestination` read, so landing spots need no other change |
| 1507 | `GetMapsecType()`, just before `default:` | `VELDRIS_MAPSEC_TYPE_CASES`: `case MAPSEC_X: return FlagGet(FLAG_VISITED_X) ? MAPSECTYPE_CITY_CANFLY : MAPSECTYPE_CITY_CANTFLY;` |
| 2325 | end of `sFlyLocations[]` | `VELDRIS_FLY_LOCATION_ROWS`: the fly icon row. The icon loop is untouched |

No new functions and no change to control flow. `field_region_map.c` and `pokenav_region_map.c` need no edit for fly (`party_menu.c` only opens the fly map, which reaches `SetFlyDestination`).

**Why an out-of-range read cannot happen:** every row adds both the heal row and the `GetMapsecType` case, and every caller of `SetFlyDestination` requires `CANFLY` (the Fly map also accepts `MAPSECTYPE_BATTLE_FRONTIER`, which only the vanilla Battle Frontier section returns). So do not add a `CANFLY` case outside the table.

**Guard:** `veldris_fly_towns.h` has a `STATIC_ASSERT` that fails the build when the section ids run past the met-location codes (`MAPSEC_NONE < METLOC_SPECIAL_EGG`, 43 new sections in total).

**Merge cost:** four added lines in one upstream file, all at the ends of existing blocks.

---

# Veldris layout proposal (shape APPROVED 2026-09-29; details PROPOSED)

**Version 3.** The same organic shape as version 2 (a crescent of land around an inland bay, placeholder name Marrow Bay), redrawn in the style of the game's own town map and of the example you sent: striped sea, textured green land, wide bands for routes, round markers for towns. It replaces the lattice of version 1 and the thin smooth roads of version 2.

**The picture as it would sit in the game** (native 256x160, no text baked in):

![Veldris at 256x160](veldris-layout-256x160.png)

**Labelled, with the game's own font** ([open it full size](veldris-layout-annotated.png)). The first three towns have gold plates. Other towns are T4 to T18, and routes are R1 to R33:

![Veldris, labelled](veldris-layout-annotated.png)

**The 28 x 15 cell grid the game stores**, with coordinates, for the Region Map Editor step ([full size](veldris-layout-cells.png)):

![Veldris cells](veldris-layout-cells.png)

## Style and names

- **Style.** Striped sea, textured land, **orange bands** for land routes, **blue bands** for sea routes, **red round markers** for towns, **green markers** at the end of each side path (a cove, a cave mouth). The colours are taken from vanilla's own town-map palette (16 colours, where Hoenn's picture uses 27). **The author chose the vanilla GBA look (2026-09-29).** The colour meanings are still proposals. The example the author sent uses pink rectangles for cities and green squares for landmarks, and recolouring to that would be a palette change.
- **Town names use the GBA font automatically.** They are not part of the picture. The engine prints the name of the section under the cursor at run time, in `FONT_NORMAL` (the game's font), into its own name windows (`WIN_MAPSEC_NAME` and `WIN_MAPSEC_NAME_TALL` in `src/region_map.c`). So there is nothing to draw and nothing to match. The labelled image above is drawn with the game's own font sheets (`graphics/fonts/latin_normal.png` and `latin_small.png`, glyph widths from `src/fonts.c`) so you can see how the names read. The plates are for the mockup only.
- **Names** are at most 16 characters, in capitals like vanilla (`LITTLEROOT TOWN`), and charmap characters only. The names on the plates for towns 4 to 18 are placeholders.

## Why it is not a grid

- **The picture and the cells are separate things.** The picture is painted from 8x8 tiles, so the coastline, islands and lakes can be any shape. The 28 x 15 cells only tell the game which section the cursor is on. The grid is never drawn in the game.
- Towns sit where the land wants them, not on a lattice. Routes wind around lakes, forest and mountains as bands of touching cells, the way vanilla's routes do.
- **"Zoomed out":** each cell stands for a big stretch of land, so a town is one cell and a route is a few bent cells. The 28 x 15 size itself is fixed by the engine (`MAP_WIDTH` and `MAP_HEIGHT` in `src/region_map.c`). If you meant a bigger map area than that, it needs an engine edit, so say so and I will look at what it costs.

## Numbers

- 18 towns and 33 routes: **23 links between towns** (17 on land, 6 by sea) and **10 side paths** that dead-end (a lane into the hills, a cove). 155 of the 420 cells are used.
- Checked by script: every route sits on the right terrain (land or sea), routes never overlap, every route touches its towns, every town is reachable from town 1, and no town has more than 4 routes (a town is one cell, so only its 4 neighbours can hold a route).
- Numbers are placeholders. Only routes 1 to 3 are meaningful: town 1 to 2, town 2 to 3 (Crestfall), and town 3 onwards to town 4, which stays blocked at first.
- **Section budget:** 51 sections against 43 spare IDs (209 vanilla, 215 now, 37 left). See "Limits found" above. The first 6 are in.
- **Tile budget (measured):** the picture uses **148 distinct 8x8 tiles** in the map area against the limit of 256 (vanilla Hoenn uses 215), and 16 colours. It is built from a handful of repeating patterns (land, forest, mountain, farm, route, sea) plus the coast tiles, so it fits. Version 2's smooth coast and roads needed 324 and would not have. It is still a mockup: the real picture is painted with tiles in the Region Map Editor.
- A winding route's rectangle is the bounding box of its cells, exactly as Hoenn does it (52 of Hoenn's 54 section rectangles equal the bounding box of their cells; Route 114 is a 4-cell bend inside a 2x3 box). The player marker is placed inside that box, so on a bent route it may not sit exactly on the road. Untested in game.
- The labelled image leaves off the numbers of R22, R24, R27, R29 and R33, which are too short to fit a label. The tables below list every route.

## Section list

`x`, `y`, `w`, `h` are in cells and are what `region_map_sections.json` needs. Names are placeholders. The full cell lists are in [`veldris-layout.json`](veldris-layout.json), reference data for entering the cells by hand (nothing reads it at build time).

| # | Section id | Name shown | x | y | w | h | Cells | Status |
|---|---|---|---|---|---|---|---|---|
| T1 | `MAPSEC_HOLLOWBROOK` | HOLLOWBROOK | 3 | 12 | 1 | 1 | 1 | **build first** |
| T2 | `MAPSEC_WENDLEBURY` | WENDLEBURY | 8 | 11 | 1 | 1 | 1 | **build first** |
| T3 | `MAPSEC_CRESTFALL` | CRESTFALL | 5 | 7 | 1 | 1 | 1 | **build first** |
| T4 | `MAPSEC_VELDRIS_TOWN_04` | TOWN 04 | 2 | 4 | 1 | 1 | 1 | planned |
| T5 | `MAPSEC_VELDRIS_TOWN_05` | TOWN 05 | 8 | 2 | 1 | 1 | 1 | planned |
| T6 | `MAPSEC_VELDRIS_TOWN_06` | TOWN 06 | 12 | 4 | 1 | 1 | 1 | planned |
| T7 | `MAPSEC_VELDRIS_TOWN_07` | TOWN 07 | 11 | 8 | 1 | 1 | 1 | planned |
| T8 | `MAPSEC_VELDRIS_TOWN_08` | TOWN 08 | 14 | 12 | 1 | 1 | 1 | planned |
| T9 | `MAPSEC_VELDRIS_TOWN_09` | TOWN 09 | 19 | 11 | 1 | 1 | 1 | planned |
| T10 | `MAPSEC_VELDRIS_TOWN_10` | TOWN 10 | 16 | 2 | 1 | 1 | 1 | planned |
| T11 | `MAPSEC_VELDRIS_TOWN_11` | TOWN 11 | 21 | 3 | 1 | 1 | 1 | planned |
| T12 | `MAPSEC_VELDRIS_TOWN_12` | TOWN 12 | 25 | 4 | 1 | 1 | 1 | planned |
| T13 | `MAPSEC_VELDRIS_TOWN_13` | TOWN 13 | 18 | 5 | 1 | 1 | 1 | planned |
| T14 | `MAPSEC_VELDRIS_TOWN_14` | TOWN 14 | 26 | 10 | 1 | 1 | 1 | planned |
| T15 | `MAPSEC_VELDRIS_TOWN_15` | TOWN 15 | 23 | 12 | 1 | 1 | 1 | planned |
| T16 | `MAPSEC_VELDRIS_TOWN_16` | TOWN 16 | 18 | 8 | 1 | 1 | 1 | planned |
| T17 | `MAPSEC_VELDRIS_TOWN_17` | TOWN 17 | 22 | 7 | 1 | 1 | 1 | planned |
| T18 | `MAPSEC_VELDRIS_TOWN_18` | TOWN 18 | 25 | 8 | 1 | 1 | 1 | planned |
| R1 | `MAPSEC_VELDRIS_ROUTE_1` | ROUTE 1 | 4 | 11 | 4 | 2 | 5 | **build first** |
| R2 | `MAPSEC_VELDRIS_ROUTE_2` | ROUTE 2 | 5 | 8 | 4 | 3 | 6 | **build first** |
| R3 | `MAPSEC_VELDRIS_ROUTE_3` | ROUTE 3 | 2 | 5 | 3 | 3 | 5 | **build first** |
| R4 | `MAPSEC_VELDRIS_ROUTE_4` | ROUTE 4 | 3 | 3 | 6 | 2 | 7 | planned |
| R5 | `MAPSEC_VELDRIS_ROUTE_5` | ROUTE 5 | 9 | 2 | 3 | 3 | 5 | planned |
| R6 | `MAPSEC_VELDRIS_ROUTE_6` | ROUTE 6 | 11 | 5 | 2 | 3 | 4 | planned |
| R7 | `MAPSEC_VELDRIS_ROUTE_7` | ROUTE 7 | 12 | 8 | 3 | 4 | 6 | planned |
| R8 | `MAPSEC_VELDRIS_ROUTE_8` | ROUTE 8 | 15 | 11 | 4 | 2 | 5 | planned |
| R9 | `MAPSEC_VELDRIS_ROUTE_9` | ROUTE 9 | 19 | 12 | 4 | 1 | 4 | planned |
| R10 | `MAPSEC_VELDRIS_ROUTE_10` | ROUTE 10 | 23 | 10 | 3 | 2 | 4 | planned |
| R11 | `MAPSEC_VELDRIS_ROUTE_11` | ROUTE 11 | 12 | 2 | 4 | 2 | 5 | planned |
| R12 | `MAPSEC_VELDRIS_ROUTE_12` | ROUTE 12 | 16 | 3 | 3 | 2 | 4 | planned |
| R13 | `MAPSEC_VELDRIS_ROUTE_13` | ROUTE 13 | 19 | 4 | 3 | 2 | 4 | planned |
| R14 | `MAPSEC_VELDRIS_ROUTE_14` | ROUTE 14 | 22 | 3 | 3 | 2 | 4 | planned |
| R15 | `MAPSEC_VELDRIS_ROUTE_15` | ROUTE 15 | 6 | 7 | 5 | 2 | 6 | planned |
| R16 | `MAPSEC_VELDRIS_ROUTE_16` | ROUTE 16 | 8 | 12 | 6 | 1 | 6 | planned |
| R17 | `MAPSEC_VELDRIS_ROUTE_17` | ROUTE 17 | 8 | 1 | 9 | 1 | 9 | planned |
| R18 | `MAPSEC_VELDRIS_ROUTE_18` | ROUTE 18 | 18 | 6 | 1 | 2 | 2 | planned (sea route) |
| R19 | `MAPSEC_VELDRIS_ROUTE_19` | ROUTE 19 | 19 | 7 | 3 | 2 | 4 | planned (sea route) |
| R20 | `MAPSEC_VELDRIS_ROUTE_20` | ROUTE 20 | 22 | 8 | 3 | 1 | 3 | planned (sea route) |
| R21 | `MAPSEC_VELDRIS_ROUTE_21` | ROUTE 21 | 25 | 5 | 1 | 3 | 3 | planned (sea route) |
| R22 | `MAPSEC_VELDRIS_ROUTE_22` | ROUTE 22 | 26 | 8 | 1 | 2 | 2 | planned (sea route) |
| R23 | `MAPSEC_VELDRIS_ROUTE_23` | ROUTE 23 | 18 | 9 | 2 | 2 | 3 | planned (sea route) |
| R24 | `MAPSEC_VELDRIS_ROUTE_24` | ROUTE 24 | 1 | 12 | 2 | 1 | 2 | planned (side path) |
| R25 | `MAPSEC_VELDRIS_ROUTE_25` | ROUTE 25 | 3 | 6 | 3 | 1 | 3 | planned (side path) |
| R26 | `MAPSEC_VELDRIS_ROUTE_26` | ROUTE 26 | 2 | 1 | 2 | 3 | 4 | planned (side path) |
| R27 | `MAPSEC_VELDRIS_ROUTE_27` | ROUTE 27 | 5 | 2 | 3 | 1 | 3 | planned (side path) |
| R28 | `MAPSEC_VELDRIS_ROUTE_28` | ROUTE 28 | 13 | 3 | 2 | 2 | 3 | planned (side path) |
| R29 | `MAPSEC_VELDRIS_ROUTE_29` | ROUTE 29 | 13 | 13 | 2 | 1 | 2 | planned (side path) |
| R30 | `MAPSEC_VELDRIS_ROUTE_30` | ROUTE 30 | 17 | 1 | 2 | 2 | 3 | planned (side path) |
| R31 | `MAPSEC_VELDRIS_ROUTE_31` | ROUTE 31 | 21 | 2 | 4 | 2 | 5 | planned (side path) |
| R32 | `MAPSEC_VELDRIS_ROUTE_32` | ROUTE 32 | 25 | 11 | 2 | 3 | 4 | planned (side path) |
| R33 | `MAPSEC_VELDRIS_ROUTE_33` | ROUTE 33 | 22 | 13 | 2 | 1 | 2 | planned (side path) |

## Route connections

| Route | From | To | Kind | Cells |
|---|---|---|---|---|
| R1 | T1 Hollowbrook | T2 Wendlebury | land | 5 |
| R2 | T2 Wendlebury | T3 Crestfall | land | 6 |
| R3 | T3 Crestfall | T4 | land | 5 |
| R4 | T4 | T5 | land | 7 |
| R5 | T5 | T6 | land | 5 |
| R6 | T6 | T7 | land | 4 |
| R7 | T7 | T8 | land | 6 |
| R8 | T8 | T9 | land | 5 |
| R9 | T9 | T15 | land | 4 |
| R10 | T15 | T14 | land | 4 |
| R11 | T6 | T10 | land | 5 |
| R12 | T10 | T13 | land | 4 |
| R13 | T13 | T11 | land | 4 |
| R14 | T11 | T12 | land | 4 |
| R15 | T3 Crestfall | T7 | land | 6 |
| R16 | T2 Wendlebury | T8 | land | 6 |
| R17 | T5 | T10 | land | 9 |
| R18 | T13 | T16 | sea (Surf) | 2 |
| R19 | T16 | T17 | sea (Surf) | 4 |
| R20 | T17 | T18 | sea (Surf) | 3 |
| R21 | T12 | T18 | sea (Surf) | 3 |
| R22 | T14 | T18 | sea (Surf) | 2 |
| R23 | T9 | T16 | sea (Surf) | 3 |
| R24 | T1 Hollowbrook | dead end | side path (dead end) | 2 |
| R25 | T3 Crestfall | dead end | side path (dead end) | 3 |
| R26 | T4 | dead end | side path (dead end) | 4 |
| R27 | T5 | dead end | side path (dead end) | 3 |
| R28 | T6 | dead end | side path (dead end) | 3 |
| R29 | T8 | dead end | side path (dead end) | 2 |
| R30 | T10 | dead end | side path (dead end) | 3 |
| R31 | T11 | dead end | side path (dead end) | 5 |
| R32 | T14 | dead end | side path (dead end) | 4 |
| R33 | T15 | dead end | side path (dead end) | 2 |

## The first six section records (ADDED 2026-09-29)

These six records were appended to `src/data/region_map/region_map_sections.json` (at the **end** of the list) so Porymap's Location dropdown offers them. Their grid cells in `region_map_layout.h` and the picture are not done yet. The JSON they were added from:

```json
[
  {
    "id": "MAPSEC_HOLLOWBROOK",
    "name": "HOLLOWBROOK",
    "x": 3,
    "y": 12,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_WENDLEBURY",
    "name": "WENDLEBURY",
    "x": 8,
    "y": 11,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_CRESTFALL",
    "name": "CRESTFALL",
    "x": 5,
    "y": 7,
    "width": 1,
    "height": 1
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_1",
    "name": "ROUTE 1",
    "x": 4,
    "y": 11,
    "width": 4,
    "height": 2
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_2",
    "name": "ROUTE 2",
    "x": 5,
    "y": 8,
    "width": 4,
    "height": 3
  },
  {
    "id": "MAPSEC_VELDRIS_ROUTE_3",
    "name": "ROUTE 3",
    "x": 2,
    "y": 5,
    "width": 3,
    "height": 3
  }
]
```

## Denser tile art: what "zoom out" means here (author, 2026-09-29)

The author meant making the individual tiles more pixel dense so more fits into the same amount of space. Findings, checked in this tree:

- **The picture and the cell grid are independent.** The picture is 8x8-pixel tiles and can carry any pixel detail: thinner roads, a finer coastline, small markers, shading. That costs no engine edit.
- **The picture's real limit is 256 distinct tiles**, not pixels. Layout v3 uses 148, so about **108 are spare** for extra detail.
- **Cells are not scarce.** The 28 x 15 grid uses 155 of 420 cells (37%). **Section IDs are the scarce resource** (43 spare over the vanilla 209, 37 left after the first six, 51 wanted), and denser art does not change that.
- **A finer cell grid** (cells smaller than one 8x8 tile, to fit more distinct places) would be an **engine edit**. Counted by grep as a rough measure: `src/region_map.c` has 26 references to the grid constants and 21 places with 8-pixel arithmetic (cursor, player icon, fly icons); `src/pokedex_area_screen.c` has 9 more; `src/field_region_map.c` and `src/pokenav_region_map.c` one each. The layout array and every section rectangle are also in cell units. Not recommended now. Revisit only if the cells run out.
- **Recommendation:** keep 28 x 15 and spend the spare tiles on detail. Whether the Region Map Editor supports any cell size other than one tile is still to be checked against its manual.

## What is still open

1. ~~Does the overall shape work?~~ **Resolved (author, 2026-09-29):** the shape is APPROVED.
2. ~~What did the author mean by "zoom it out"?~~ **Resolved:** denser tile art, see above.
3. Marrow Bay is a placeholder name.
4. Approach A-prime: applied (see above).
