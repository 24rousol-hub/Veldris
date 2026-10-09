# Time-of-day wild encounters

Status: switch BUILT 2026-10-08 (author: 'time of day'). **2026-10-09 (author): the clock is a fake clock the player sets at the wall clock in their room; only open-air routes that are not special locations get night tables; the lead picks the species as each route is built. Route 1 has its Night table.** Other routes still play one table all day.

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

The table is chosen at the moment of each encounter roll, so there is no lag. The clock is the fake clock described below (`OW_USE_FAKE_RTC` is TRUE), so night in the game no longer matches night in the room.

## Fake clock (BUILT 2026-10-09, author: 'a fake clock that the player can set in their home')

`OW_USE_FAKE_RTC` is TRUE, so the in-game clock is a counter saved in the save file (SaveBlock3), not the cartridge or emulator clock. SaveBlock3 grows from 4 to 16 bytes (limit 1624).

| Fact | Value |
|---|---|
| New game | Saturday 10:00 (`CB2_NewGame` calls `RtcCalcLocalTimeOffset(0, 10, 0, 0)`; `VeldrisNewGameDefaults` repeats it) |
| Speed | `OW_ALTERED_TIME_RATIO` stays GEN_LATEST: 20 game seconds per real second. **A game day is 72 real minutes** (Morning 12, Day 27, Evening 3, Night 30). For real time set it to `TIME_DEBUG` (1:1); `GEN_8_PLA` is 60x. Author's call, not asked yet |
| When it runs | While the game runs, including menus and battles. Stops at the title screen and when the console is off |
| Where to set it | The wall clock on the back wall of the player's room (2F), event at (3,1). **The author paints the clock metatiles** (`0x221` over `0x229`, Gen 4 Interior, the clock pair already in the tileset) at (3,0) and (3,1), between the bed and the PC desk, and keeps both blocked. Alternative spot x=6 (between the desk and the TV). Until painted, pressing A facing that bit of wall still works but nothing is drawn. Press A facing it: running clock = 'Reset it?' (YES: set screen; NO: clock face); stopped clock = 'Set the time and start it?' |
| Setting it | The vanilla Hoenn clock screens. Resets the date to Saturday and the day counter to 0 and restarts the berry timer. It never fires a daily event by itself |
| Berries and daily events | Need `FLAG_SYS_CLOCK_SET` (vanilla system flag, no new flag). **A new game sets it** (`InitTimeBasedEvents()` in `src/veldris_new_game.c`), so they run from the first hour; the clock can still be re-set at home. A daily event is about every 72 real minutes |
| Needed for night tables? | No. Time of day, the tint and time evolutions work without the flag |
| Battery message | Never shows |
| Old saves | A save made before this change loads, but its clock reads 00:00 (Night) and its berry and daily timers are dead until the clock is set once at home. **The save layout changed: start a new game after this build** |
| Debug menu | Utilities > Time Functions: 'Set time of day' and 'Set weekday' now work |

The script is `Hollowbrook_PlayersHouse_2F_EventScript_WallClock` (`data/maps/Hollowbrook_PlayersHouse_2F/scripts.inc`), a bg_event sign at (3,1) in the map's `map.json`; it reuses the vanilla `PlayersHouse_2F_EventScript_SetWallClock`. **Close or reload Porymap before it saves**, or the new event is overwritten.

## Night tables: open-air routes only (author, 2026-10-09)

Only **open-air routes** get a `_Night` table, and never a special location. 'Open-air' means a road map of type `MAP_TYPE_ROUTE` under the sky. (The night tint also covers towns, cities and sea routes, `MapHasNaturalLight` in `src/overworld.c`, but only `MAP_TYPE_ROUTE` maps get a Night table.) The lead picks the species per route as each route is built. `_Morning` and `_Evening` stay unused (they use Day). `python3 design/tools/wild_lint.py` warns when a time table sits on a map that is not `MAP_TYPE_ROUTE`.

Never a time table: towns and cities, interiors, caves and mines, forests and mazes (Mothwood), the Pinnacle and the Victory Road cave floors, shrines and ruins (Mirror Isle, Aldermere), underwater maps, Altering Cave, Battle Frontier groups. Sea routes have no grass and stay out unless the author asks (the engine supports a Night water table).

| Road | Kind | Night table? |
|---|---|---|
| R1 Hollowbrook-Crestfall | farm road | **YES, built** |
| R2 Crestfall-Wendlebury | farm road | yes, when built |
| R3 Crestfall-Briarwick | wooded lane | yes, when built |
| R4 Briarwick-Gloomsby | meadow road, fog in the east third | yes (author to confirm) |
| R5 Gloomsby-Smeltham, R6 Smeltham-Hoarfell | foothills, mountain pass | yes |
| R7 Slagwell spur | dead end to the mine door | no (part of the mine), author to confirm |
| R8 Briarwick-Wendlebury | lakeside road (Mothwood branches off) | yes (Mothwood itself: never) |
| R10, R11, R12, R13 | pass, moor, farm road, heath | yes |
| R15 Primrose Vale-Brinecombe, R18 Hoarfell-Gildhaven | valley road, avenue | yes |
| R20 Gildhaven-Pinnacle | surface climb yes; the three cave floors never | surface map only |
| R21 Pinnacle-Vesperhaven (post-league), R24, R25 | cliff-top descent, wood road, cliff road | yes |
| R23 Ebbsworth-Kingsquay | sea route with a land path | land table only, if wanted |
| R30 Vesperhaven-Echo Hollow (post-game) | road to a cave door | no, author to confirm |
| R31 Hollowbrook-Argent Peak (post-game) | mountain trail | yes (Argent Peak itself: never) |
| R14, R16, R17, R19, R22, R26-R29 | sea | no |

(R9 was dropped on 2026-10-08. Route list from the route numbering in `design/towns-and-routes.md` and `design/region-names.md`; the kinds are my reading, author to confirm.)

## Route 1 Night table (BUILT, species PROPOSED)

Label `gVeldrisRoute1_Night`, land only, rate 20, same levels as the Day table slot for slot. The Day table is untouched; Morning and Evening use Day.

| Slot | Rate | Day | Night | Levels |
|---|---|---|---|---|
| 1 | 20% | Zigzagoon | Zigzagoon | 3-4 |
| 2 | 20% | Lillipup | Hoothoot | 3-4 |
| 3 | 10% | Bidoof | Rattata | 3-4 |
| 4 | 10% | Sentret | Hoothoot | 3-4 |
| 5 | 10% | Zigzagoon | Zigzagoon | 4 |
| 6 | 10% | Lillipup | Hoothoot | 4 |
| 7 | 5% | Bidoof | Rattata | 4-5 |
| 8 | 5% | Sentret | Spinarak | 4-5 |
| 9 | 4% | Skitty | Skitty | 4-5 |
| 10 | 4% | Skitty | Skitty | 5 |
| 11 | 1% | Slakoth | Slakoth | 5 |
| 12 | 1% | Miltank | Murkrow | 5 |

The Pokédex Area page shows the table for the time it is set to (D-pad Up/Down cycles Morning, Day, Evening, Night), so a Night-only Pokémon reads AREA UNKNOWN by day. To change the species, edit `src/data/wild_encounters.json` (Porymap closed) and run `wild_lint.py`.

## How to add a Night table (workflow)

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
- Debug menu (R+START): Utilities > Time Functions has 'Get time', 'Get time of day', 'Set wall clock', and (now that the fake clock is on) 'Set time of day' and 'Set weekday'. To test Night: Utilities, Time Functions, Set time of day, Night.
- Changing `OW_TIMES_OF_DAY` away from GEN_LATEST changes the hours and the tint; GEN_2 and GEN_4 remove Evening, which makes an `_Evening` table unreachable.

## Open questions for the author

Resolved 2026-10-09: fake clock (not the real one), the player can set it at home, open-air routes only, the lead picks species. Still open:

1. Game-day length: 72 real minutes (20x, now) or real time (1:1)?
2. Standard hours (above) or the Gen 4 style (Morning 4 to 10, Day 10 to 20, Night 20 to 4, no Evening)?
3. Paint the wall-clock tiles in Porymap (see 'Fake clock'), and confirm the spot (x=3 or x=6) and the 'author to confirm' rows in the route table.

## Tests (mGBA, 2026-10-08, emulator clock read night)

| Check | Result |
|---|---|
| Build passes with the switch on and the TIME_DAY fallback; generated `src/data/wild_encounters.h` has Route 1 in `[TIME_DAY]` and the other slots NULL | Pass |
| Route 1 tall grass at night gave Zigzagoon Lv 3 and Lv 4 (the plain table is the fallback for Night) | Pass |
| Pokédex Area page for Zigzagoon at night ('NIGHT' shown) lists areas instead of 'AREA UNKNOWN' | Pass (with the `pokedex_area_screen.c` fix) |
| A split table at a real Night/Day boundary | Built 2026-10-09 (Route 1), see below |

## Tests (mGBA, 2026-10-09, fake clock)

| Check | Result |
|---|---|
| Build passes with `OW_USE_FAKE_RTC` TRUE, the furniture lookup and the Route 1 Night table | Pass |
| New game via the title-screen quickstart: A on the wall-clock spot (3,1) in the 2F room says 'The wall clock keeps its own time. Reset it?' (so `FLAG_SYS_CLOCK_SET` is already set), NO shows the clock face, and it reads about 10:00 AM | Pass |
| Debug Utilities > Time Functions > Set time of day > Night: the field gets the night tint | Pass |
| Review fix: the clock face follows the player's gender (a May player first saw the blue boy's face, now pink) | Pass |
| Wall clock YES branch: the vanilla set-clock screen, 'Is this the correct time?', YES, then 'The wall clock is ticking.' | Pass |
| Generated `src/data/wild_encounters.h`: Route 1's `[TIME_NIGHT]` slot points at `gVeldrisRoute1_Night_LandMonsInfo` (12 slots, rate 20, the species above) | Pass (read from the build, 2026-10-09) |
| Route 1 tall grass at Night actually gives the new table in the emulator | Not seen (walking to the grass pen in the emulator was slow); the 2026-10-08 test already showed a Night roll uses the Night slot when it exists |
| The stopped-clock text (flag clear) | Not run (a new game sets the flag) |
