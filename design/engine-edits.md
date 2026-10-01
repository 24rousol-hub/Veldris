# Engine edits log

The rule: keep edits to upstream (pokeemerald-expansion) files minimal, and prefer config switches in `include/config/*.h`, so upstream updates can still be pulled with few conflicts.

**Every edit to a file that exists upstream is logged here, in the same commit.** Hack-only files (everything under `design/`, new maps, new scripts) do not need a row.

Before pulling upstream, read this list. Each row is a place a merge could conflict.

| Date | File | Change | Why | Config switch instead? |
|---|---|---|---|---|
| 2026-09-29 | `.gitignore` | Appended a Veldris block at the end (ROMs, saves, build output). No upstream lines changed. | Public repo: never commit a ROM or save | n/a |
| 2026-09-29 | `data/text/birch_speech.inc` | Rewrote the intro text as Prof. Fennick. Text only: every label is unchanged and no C was touched | The author asked for the intro to be Fennick's, in this file | n/a (text file) |
| 2026-09-29 | `CREDITS.md` | Added a hack credits section above the upstream one. Upstream content is untouched. | Credit every third-party asset | n/a |
| 2026-09-29 | `include/constants/flags.h` | Renamed `FLAG_UNUSED_0x88E` to `FLAG_BADGE09_GET`; `NUM_BADGES` is now the literal `9` | 9th badge for 9 gyms | No |
| 2026-09-29 | `src/event_data.c` | Removed the `gBadgeFlags[]` definition (it moved to the hack-owned `src/veldris_badges.c`, generated from one table) | Single badge table | No |
| 2026-09-29 | `src/trainer_card.c` | Badge tile buffer is 2 sheet rows; badges load at BG3 tiles 192 and 352; front-page badges drawn edge to edge and centred from the table; badge flags read via `gBadgeFlags`; FRLG card layout untouched | Show 9 (up to 12) badges | No |
| 2026-09-29 | `graphics/trainer_card/badges.png` (slot 0 re-coloured silver and blue, same palette), `front.bin` | Sheet is now 128x32 (Kaixer badges 1-8 + placeholder 9); the 8 baked numbered slots in `front.bin` rows 15-16 were replaced by the plain band tile; slot 15 of the sheet is an empty-socket icon for unearned badges | Room for 9+ badges | No |
| 2026-09-29 | `src/main_menu.c`, `src/menu.c`, `src/tv.c`, `src/shop_criteria.c`, `src/battle_script_commands.c` | Badge-count loops replaced by `GetBadgeCount()`; `sBadgeLevel[]` gained a 65 entry | The old loops added `NUM_BADGES` to `FLAG_BADGE01_GET`, which breaks with a non-contiguous 9th flag | No |
| 2026-09-29 | `src/field_move.c` | `HasBadgeForFieldMove` reads `gBadgeFlags[arg]` instead of `FLAG_BADGE01_GET + arg` | HM gating works for any badge flag | No |
| 2026-09-29 | `src/battle_util.c` | Obedience: badge 9 ignores obedience, badge 8 gives level 90 (vanilla: badge 8 ignored it) | 9 badges | No |
| 2026-09-29 | `src/caps.c` | Added `FLAG_BADGE09_GET` rows to the level-cap (50, PROPOSED placeholder) and EV-cap tables; EV fractions now /19 | 9 badges. Caps are off by default (`B_LEVEL_CAP_TYPE`) | Caps are config-gated |
| 2026-09-29 | `src/region_map.c` | A-prime fly hooks: `#include "data/veldris_fly_towns.h"` plus one line each at the end of `sMapHealLocations`, `sFlyLocations` and before `default:` in `GetMapsecType` | One table row per fly town instead of 3 edits in this file | No |
| 2026-09-29 | `src/data/region_map/region_map_sections.json` | Appended six records at the end: `MAPSEC_HOLLOWBROOK`, `MAPSEC_WENDLEBURY`, `MAPSEC_CRESTFALL`, `MAPSEC_VELDRIS_ROUTE_1` to `_3`. `MAPSEC_NONE` moves from 209 to 215 | So Porymap's Location dropdown offers them and the name popup works. The town map grid and picture are not touched yet | No |
| 2026-09-30 | `include/trainer_pools.h`, `src/trainer_pools.c` | Added `POOL_PRUNE_RIVAL_STARTER` and `RivalStarterPrune` (about 25 lines incl. two includes): drops the two non-matching starter versions from Troglodyte's pool, reading `VAR_TROG_STARTER` | One trainer entry per Troglodyte fight instead of three (author approved 2026-09-30) | No (the pool feature itself is upstream) |
| 2026-09-30 | `src/starter_choose.c` | `sStarterMon` gets a fourth entry (`VELDRIS_FOURTH_STARTER`, stand-in PIKACHU) and `GetStarterPokemon` bounds-checks against it (also fixes an upstream off-by-one, `>` to `>=`). The choose screen still shows three | So `VAR_STARTER_MON` can hold 3 for the revealed fourth starter | No |
| 2026-10-01 | `include/constants/trainers.h`, `src/data/graphics/trainers.h` | Added 10 `TRAINER_PIC_VELDRIS_*` entries before `TRAINER_PIC_COUNT`, their `INCGFX` lines and `gTrainerPicInfo` rows (gym leaders 2 to 9, Elite Four Drayden, Champion Cynthia). Front pics only | Imported trainer art ([gym-leader-art.md](gym-leader-art.md)). Built; `trainerproc` accepts `Pic: Veldris Leader Bug` etc. | No (appended at the end of each table, so upstream merges stay clean) |
| 2026-10-01 | `include/constants/opponents.h`, `src/data/trainers.party` | 13 vanilla Hoenn trainer ids reused for the Veldris gym leaders 2 to 9, Elite Four and Champion: each block rewritten and renamed, the id `#define` renamed to the Veldris name and the old Hoenn name kept as an alias. No new ids, `TRAINERS_COUNT_EMERALD` unchanged | [trainer-roster.md](trainer-roster.md). Built | No. The Hoenn rematch blocks are untouched (never reached) |
| 2026-10-01 | `src/field_move.c` | Three Emerald-branch `.arg` badge numbers changed: Flash badge 2 to 3, Rock Smash badge 3 to 2, Dive badge 7 to 9 (author approved). FRLG branch untouched | HM plan in [gyms.md](gyms.md) | No |
| 2026-10-01 | `src/caps.c` | `sLevelCapFlagMap` values set to the gym aces (12, 19, 25, 31, 37, 42, 48, 55, 60) and the Champion 75. Cap itself is still off in `include/config/caps.h` | Level scale (author, 2026-10-01) | No |
| 2026-09-30 | `include/constants/vars.h` | Renamed `VAR_UNUSED_0x40F7` to `VAR_TROG_STARTER` | Holds Troglodyte's random starter | No |

**Files Porymap writes.** When the author saves a new map, Porymap appends to or rewrites these upstream files. They are not engine edits, so they get one standing row here rather than a row per map: `data/maps/map_groups.json`, `data/layouts/layouts.json`, `data/event_scripts.s` (an appended `.include` line per new map), and on every save `src/data/region_map/region_map_sections.json`, `src/data/heal_locations.json`, `src/data/wild_encounters.json`. Read the changed-files list before committing.

**Files each new fly town touches (PROPOSED standing rows).** Per [region-map.md](region-map.md): `region_map_sections.json`, `include/constants/flags.h` (one rename), `src/data/heal_locations.json`, `src/data/region_map/region_map_layout.h`, and the map picture. Logging each of these per town would be 18 towns x 5 files of noise, so the proposal is one standing 'appends only' row per file, added when the file is first touched. That changes the logging rule above, so it waits for the author's OK. Hack-owned files (`src/data/veldris_fly_towns.h`, `src/veldris_badges.c`, `include/veldris_badges.h`) need no row.

## Planned edits (not yet made)

| File | Change | Waiting on |
|---|---|---|
| `include/constants/flags.h`, `vars.h` | One-line renames of `FLAG_UNUSED_*` / `VAR_UNUSED_*` as flags and vars are claimed. See [flags.md](flags.md) | First non-badge flag or var claim |
| `include/constants/opponents.h` | Trainer slot changes (only 9 free) | Open decision 6 in [game-bible.md](game-bible.md) |
| `include/constants/opponents.h` (2026-10-01) | `TRAINER_CRESTFALL_GRETA/GYM_1/GYM_2` reuse ids 770 to 772 (Roxanne 2 to 4, kept as aliases); `TRAINERS_COUNT_EMERALD` unchanged at 855 (all 9 spare ids free). Ids 520 and 521 renamed `TRAINER_TROGLODYTE_HOLLOWBROOK/CRESTFALL`, with the Brendan names kept as aliases. `include/constants/trainers.h` and `src/data/graphics/trainers.h`: `TRAINER_PIC_VELDRIS_LEADER_NORMAL` | Built, tested |
| `include/constants/trainers.h`, `src/data/graphics/trainers.h` (2026-10-01) | Three more pics: `TRAINER_PIC_VELDRIS_ELITE_FOUR_OSSIAN/HYACINTH/DUNMORE` | Built, seen in battle |
| `src/data/region_map/region_map_sections.json` (2026-10-01, second edit) | Data only: 29 new section records at the end (17 settlements, `MAPSEC_VELDRIS_ROUTE_22` to `_31`, `SILVERSTRAND`, `PINNACLE`), five Hoenn cave and peak entries renamed for landmarks, and the positions of every Veldris section recomputed from the author's sketch. See [setup-budget.md](setup-budget.md) | Built |
| `src/data/region_map/region_map_sections.json` (2026-10-01) | Data only: 18 Hoenn route entries (`MAPSEC_ROUTE_101, 102, 103, 105, 107, 108, 113, 117, 118, 120, 123, 124, 126, 127, 128, 129, 130, 131`) renamed `ROUTE 4` to `ROUTE 21` with Veldris positions. No C change. See [region-sketch.md](region-sketch.md) | Built |
