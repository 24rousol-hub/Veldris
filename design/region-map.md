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
