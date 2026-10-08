# Time-of-day wild encounters

Status: switch BUILT 2026-10-08 (author: 'time of day'). **No table is split yet**, so the game plays exactly as before. The per-time Pokémon are the author's to choose, or mine to propose.

## What changed

`OW_TIME_OF_DAY_ENCOUNTERS` is TRUE (`include/config/overworld.h`). The wild-encounter loader now looks for a table by time of day.

| Rule | Detail |
|---|---|
| Table names | The map's `base_label` plus a suffix: `_Morning`, `_Day`, `_Evening`, `_Night` (the `TimeOfDay` enum in `include/rtc.h`) |
| A table with no suffix | Counts as the **Morning** table |
| Empty time | Falls back to the Morning table (`OW_TIME_OF_DAY_FALLBACK`, with `OW_TIME_OF_DAY_DISABLE_FALLBACK` FALSE) |
| Result today | Route 1 (`gVeldrisRoute1`, no suffix) is the Morning table and the fallback for the other three, so it behaves as before |

## How to add a Night table

Either in Porymap's wild-encounter editor or by hand in `src/data/wild_encounters.json`: copy the map's block, set `base_label` to `gVeldrisRoute1_Night` (keep `map` the same), and change the Pokémon. Times left out use the Morning table. `migration_scripts/add_time_based_encounters.py --copy` can make all four copies at once (it backs up the file first; about 9 KB of ROM more).

Porymap rewrites `wild_encounters.json` on save, so close and reload it before editing by hand, and read the changed-files list before committing.

## Things to know

- The clock is the cartridge or emulator RTC. `OW_USE_FAKE_RTC` is FALSE. Emulators keep real time; a cartridge with a dead battery will not.
- Which hours are Morning, Day, Evening and Night depends on `OW_TIMES_OF_DAY` (GEN_LATEST).
- Time also drives some other expansion features (evolutions that need day or night, Pokédex time lists). Those do not depend on this switch.
- **PROPOSED idea, not built:** a night-only table for Route 1 (Sentret, Hoothoot-style night birds) once the author picks species. Not started, because Route 1's species list is the author's decision.

## Test

The build passes with the switch on. In mGBA (the emulator clock read night) Route 1 tall grass still gave a Lv 4 Zigzagoon from the unsuffixed table, which confirms the fallback. A split table was not built, so a real Night-only encounter is untested. The debug menu has a time submenu (Utilities) for changing the hour.
