# Setup budget for everything past Hollowbrook and Route 1 (2026-10-01)

Background work done so the later maps can be built without surprises. Everything here is checked against this tree. The card text it counts is in [maps/](maps/index.md).

## Map sections (DONE, data only)

All settlements, roads and landmarks from the cards now have a section in `src/data/region_map/region_map_sections.json`. Build passes. **244 sections, 29 new ids added today** (35 Veldris ids in all, with the first six of 2026-09-29), so **8 of the 43 spare ids are left** (recounted 2026-10-10: 252 minus the number of records in the JSON; the guard in `src/data/veldris_fly_towns.h` fails the build if they run out). Routes 32 and 33 have no record yet and would take 2 of the 8.

- **Settlements (17 new):** `MAPSEC_BRIARWICK`, `GLOOMSBY`, `SMELTHAM`, `HOARFELL`, `GILDHAVEN`, `CRAGDALE`, `LINGMOOR`, `WAYMEET`, `HEMLOCK_REACH`, `PRIMROSE_VALE`, `BRINECOMBE`, `EBBSWORTH`, `KINGSQUAY`, `DRIFTSANDS`, `BEACONMOUTH`, `ALDERMERE`, `VESPERHAVEN`.
- **Roads:** R1 to R3 and R22 to R31 are `MAPSEC_VELDRIS_ROUTE_<n>` (10 new today). R4 to R21 reuse Hoenn route entries (table in [region-sketch.md](region-sketch.md)).
- **Landmarks:** five borrow Hoenn cave and peak entries (no new id): Slagwell Mine on `MAPSEC_GRANITE_CAVE`, Mothwood on `MAPSEC_PETALBURG_WOODS`, Echo Hollow on `MAPSEC_SHOAL_CAVE`, Argent Peak on `MAPSEC_MT_PYRE`, Mirror Isle on `MAPSEC_ISLAND_CAVE`. Two are new: `MAPSEC_SILVERSTRAND` and `MAPSEC_PINNACLE`. Checked that each borrowed entry is used only for its popup style (and one follower check), not for story logic.
- **Positions** come from the author's sketch scaled onto the 28 x 15 town-map grid. They are rough. The author redraws the town-map picture and grid later in Porymap's Region Map Editor, then these x, y, width, height values get tuned.
- **Not done:** fly rows in `veldris_fly_towns.h`. Each needs the map, its heal location and a claimed visited flag first (checklist in [region-map.md](region-map.md)).

## Wild tables (CHECKED)

`python3 design/tools/cardcheck.py` checks every wild table in the cards: rates add to 100, every species exists in `species.h`, level ranges are sane, and inline species lists (Surf, rods, trainer teams, 875 names) are known species. **Result: 38 tables, 0 errors, 0 warnings.** Not checked: that a species is enabled by a config switch, and evolution-level sanity (use `teamcheck.py` for built trainer teams).

## Flags (BUDGET)

The cards propose **about 176 named flags, 14 vars and 49 families of numbered flags** (items, one-shots). Against the spare pool in [flags.md](flags.md) (about 300 permanent flags, 299 on 2026-10-10; flags.md holds the exact count and how to recount):

- **Item flags cost nothing from the pool.** Hoenn already has 167 `FLAG_ITEM_*` (0x3E8-0x492) and 112 `FLAG_HIDDEN_ITEM_*` (0x1F4-0x264) flags that nothing in Veldris uses. The cards list about 58 visible and 37 hidden items. Use the existing Hoenn flag constants for them (same reuse idea as trainers). Hidden-item flags already satisfy the 0x1F4 floor. **Careful:** `include/constants/flags.h` also defines 190 FRLG-only `FLAG_HIDDEN_ITEM_*` names, 297 `FLAG_HIDE_*`, 14 `FLAG_DEFEATED_*` and 2 `FLAG_VISITED_*` names as `0`. In this Emerald build those do nothing (`FlagSet(0)` is a no-op, `FlagGet(0)` is FALSE), so check a name's value before reusing it.
- **Hoenn `FLAG_RECEIVED_*` flags** (100) cover HMs and TMs given by gym leaders and NPCs, so those need no claim either.
- That leaves roughly **100 to 120 story and one-shot flags** to claim from the pool. Fits, with margin. Do not claim any until a map using it is built (rule 1 of flags.md).
- 14 vars are fine (the var pool is separate, 256 persistent).

## Trainers (BUDGET)

The cards list about **183 trainers** (gym leaders, gym trainers, route trainers, E4). Vanilla has about 850 ids and the Veldris trainers built so far reuse 21 of them (13 leaders, Elite Four and Champion, 3 Crestfall, 2 Troglodyte, 3 on Route 1; see [trainer-roster.md](trainer-roster.md)), so reuse is easy. Rules that stay: reuse vanilla ids only (author rule), explicit `IVs: 0`, defeated flag follows the id. Two things to watch:

- A reused id carries the vanilla defeated flag. If two Veldris trainers ever need to reset together, pick them on purpose.
- Rematch support (`REMATCH_TABLE_ENTRIES` is 78) is a separate system. Post-game rematches for the gym leaders and Elite 4 will need table entries. Not planned yet.

## Still to do (needs the author's maps first)

Heal locations and fly rows per town, claimed visited flags, Palladium credits in `CREDITS.md` (done in the commit that first traces each map), the trainer id mapping per road, and the scripts. All sit behind the author building the maps in Porymap.
