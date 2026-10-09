# Time-of-day wild encounters

Status: switch BUILT 2026-10-08 (author: 'time of day'). **No table is split yet**, so the game plays exactly as before. Which Pokémon appear at which hour is the author's call (or a proposal for the author to approve).

## What changed

| Switch (`include/config/overworld.h`) | Value | Why |
|---|---|---|
| `OW_TIME_OF_DAY_ENCOUNTERS` | TRUE | Wild tables may be split by time |
| `OW_TIME_OF_DAY_FALLBACK` | **TIME_DAY** (was TIME_MORNING) | A plain (un-suffixed) table is the **Day** table; `_Morning`, `_Evening` and `_Night` tables override it. Any time with no table uses the plain table |
| `OW_TIME_OF_DAY_DISABLE_FALLBACK` | FALSE | Empty times fall back, they do not turn encounters off |

The generator (`tools/wild_encounters/wild_encounters_to_header.py`) puts every table with no time suffix into the fallback slot, so with TIME_DAY the existing 389 tables are all 'Day' tables and nothing changes. The fallback is **one fixed time, not the nearest**: with TIME_MORNING an Evening without its own table would have shown the Morning table, which is why TIME_DAY was chosen. Changing it later, after tables exist, means renaming labels.

Fallback is decided separately for land, water, rock smash and fishing.

## Hours (OW_TIMES_OF_DAY = GEN_LATEST, i.e. Gen 9)

| Time | Hours |
|---|---|
| Morning | 06:00 to 10:00 |
| Day | 10:00 to 19:00 |
| Evening | 19:00 to 20:00 |
| Night | 20:00 to 06:00 |

The table is chosen at the moment of each encounter roll, so there is no lag. The clock is the cartridge or emulator RTC (`OW_USE_FAKE_RTC` is FALSE) minus a saved offset, which is 0 because Hollowbrook has no wall clock to set. A dead cartridge battery gives a frozen or wrong clock.

## How to add a Night table (PROPOSED workflow)

In `src/data/wild_encounters.json` one entry per time. The new entry has the **same `map`**, a `base_label` of `<usual label>_<Morning|Day|Evening|Night>` (capital first letter, suffix only), and any subset of `land_mons`, `water_mons`, `rock_smash_mons` and `fishing_mons`. Slot counts are fixed per field (12 land, 5 water, 5 rock smash, 10 fishing) and slot percentages are global, but each table has its own `encounter_rate`. In Porymap the extra tables are extra **groups** of the map (Wild Pokémon tab, '+' next to Group, a unique name, 'Copy from current group'); names and menus may differ slightly by Porymap version, which was not run.

Rules, and what goes wrong:

- **Time words only as the final `_Suffix`.** The generator tests the words as substrings of the whole label and the later one wins: `gVeldrisDaybreakRoad_Morning` lands in the Day slot. Avoid Morning, Day, Evening, Night in any route or town name.
- **Keep the plain table.** A route with only a `_Night` table has an empty fallback and **no encounters by day**, with no build error.
- **Never suffix the Altering Cave tables** (`gAlteringCave1` to `9` share one map).
- No table for a map that does not exist yet (the build fails on an undeclared `MAP_*`).
- **Do not run `migration_scripts/add_time_based_encounters.py`**: it renames every symbol, rewrites all 389 entries, grows the JSON to about 4 MB with `--copy`, and leaves an untracked 1 MB `wild_encounters.json.bak` in a public repo.
- Porymap rewrites the whole `wild_encounters.json` on save: close it before a hand or script edit and read the changed-files list before committing.
- **Run `python3 design/tools/wild_lint.py`** before committing any change to the JSON. It checks the suffix rule, slot counts, duplicate times and an orphan time table.

Cost: a land-only table is about 56 bytes of ROM and 1.4 to 1.9 KB of JSON; 6.27 MiB of ROM is free. Add `_Night` only where it matters; skip `_Evening` (one hour) and caves.

## Engine edit made for it

`src/pokedex_area_screen.c`: with the switch on, the Pokédex Area page reads one time slot with no fallback, so every wild species showed 'AREA UNKNOWN' outside the fallback time. A 20-line helper (`GetDexEncounterTypes`) now applies the same per-field fallback as the game. Logged in [engine-edits.md](engine-edits.md).

## Other facts

- Time also drives expansion features that do not depend on this switch (evolutions that need day or night; the screen tint, which was visible at night in the emulator).
- Debug menu (R+START): Utilities > Time Functions has 'Get time', 'Get time of day' and 'Set wall clock' (works with the real RTC). 'Set time of day' and 'Set weekday' only work with `OW_USE_FAKE_RTC` TRUE.
- Nothing starts the daily clock in this hack (no wall clock scene): berries and daily events never begin. That is a separate item from this feature.
- Changing `OW_TIMES_OF_DAY` away from GEN_LATEST changes the hours and the tint; GEN_2 and GEN_4 remove Evening, which makes an `_Evening` table unreachable.
- **PROPOSED, not built:** a Night table for Route 1 with a nocturnal bird in place of Sentret and Lillipup (Gen 2 species are enabled). Route 1's species list is the author's decision, so it waits for approval.

## Open questions for the author

1. Real clock (night in the game is night where you are) or fake clock (a game day lasts about 72 minutes, changes the save layout)? Recommendation: real clock.
2. Should the player be able to set the in-game clock (a wall clock in the house)? It also starts the berry and daily-event clocks.
3. Which routes get a Night table, and the species for each?
4. Standard hours (above) or the Gen 4 style (Morning 4 to 10, Day 10 to 20, Night 20 to 4, no Evening)?

## Tests (mGBA, 2026-10-08, emulator clock read night)

| Check | Result |
|---|---|
| Build passes with the switch on and the TIME_DAY fallback; generated `src/data/wild_encounters.h` has Route 1 in `[TIME_DAY]` and the other slots NULL | Pass |
| Route 1 tall grass at night gave Zigzagoon Lv 3 and Lv 4 (the plain table is the fallback for Night) | Pass |
| Pokédex Area page for Zigzagoon at night ('NIGHT' shown) lists areas instead of 'AREA UNKNOWN' | Pass (with the `pokedex_area_screen.c` fix) |
| A split table at a real Night/Day boundary | Not built, not tested |
