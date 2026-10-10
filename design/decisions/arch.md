# Hoenn purge: decision brief

**Where the files are:** the tested SKIP recipe and the measuring scripts are in `prototypes/hoenn-skip/` next to this file (scripts, the 7-line `mapjson_null_slots.patch`, `results/keep_scripts.txt` and `results/ladder.md`). The build logs, error reports and per-step size files from the experiment (about 3 MB) stayed in the scratch area and are not in the repo; every number below can be re-measured with the scripts. Paths in the tables below that start with `results/` or name a script mean that folder.

Stream `arch`, 2026-10-10. Hoenn costs and the option ladder were measured at `e250a8e6` (now `d9389673`), and the recommended form was re-measured at the current HEAD `04385f05`: the Hoenn numbers did not move, only the ROM total did, because the author imported 70 overworld sprites and 94 battle pictures in between (+238,108 bytes). All work was in a throw-away clone (deleted afterwards). Nothing in `/home/user/Veldris` was changed. **Everything below is PROPOSED until the author answers** (CLAUDE.md rules 8 and 9).

## 1. The answer in plain words

The ROM still builds all of Hoenn: 518 Hoenn maps, their scripts, layouts, tilesets, and about 1 MB of Hoenn-only game systems (Battle Frontier, contests, TV shows, secret bases and so on). Veldris can never reach any of it.

**The purge is not needed for scale.** Every number the purge is supposed to help is nowhere near a limit, and the ones that are tight (map sections, spare vars) are not helped by it:

| What | Today | What Veldris plans to need | Does a purge matter? |
|---|---|---|---|
| ROM free of 32 MiB | **6.19 MiB** (6,493,940 bytes; 25.81 MiB used; it was 6.42 MiB before the sprite import) | about 1.3 MiB for the rest of the game (estimate, section 3.3) | No. The best safe purge adds 1.2 MiB, the most aggressive tested adds 1.5 MiB |
| Spare flags | **299** safe (+2 reserved) | about 100 to 120 | No, and 568 more Hoenn-only story and item flags can be reused with no purge |
| Spare vars | **19** (`flags.md`) | 14 planned | This is the tight one, but **104 more vars** (37 never used, 67 Hoenn-only) can be reused with no purge |
| Trainer ids | 9 brand-new (not needed: the author reuses vanilla ids) | about 183, 21 built | No. 409 Hoenn-only ids are free to reuse today |
| Map sections (MAPSEC) | **8 left** of 252 | every planned section already exists | Not by SKIP. Only a DELETE that also rewrites the C tables (`region_map.c`) could free any |
| Map slots per group | group 0: 67 free, Dungeons (24): 19 free, SpecialArea (26): 38 free | one Veldris cave group at most | Only true deletion frees slots, and nothing needs them |

**Recommendation: LEAVE it as it is.** The author's own plan copies Hoenn maps, layouts (`LAYOUT_POKEMON_CENTER_1F/2F`, `LAYOUT_MART`, `LAYOUT_HOUSE1/2`, `LAYOUT_HARBOR`) and tilesets (`gTileset_Cave`, `EliteFour`, `Facility` ...) as the starting point for Veldris maps (`design/map-plan.md`). A purge before that is finished removes the author's template library and makes copied maps silently vanish from the build. If a purge is wanted later (free ROM under about 2 MiB, or a shorter map list), a tested, reversible recipe is ready (option SKIP).

**One word to answer: `LEAVE`, `SKIP` or `DELETE`.** (Optional second word `FRLG` to also delete the 421 unbuilt FRLG map folders, which costs zero code edits and changes no ROM bytes. Say `LEAVE FRLG` for that alone.)

## 2. The three options

| | A. LEAVE | B. SKIP (tag Hoenn maps as another region, like FRLG) | C. DELETE (true deletion) |
|---|---|---|---|
| What it is | nothing | `"region": "REGION_HOENN_SKIPPED"` on 518 maps, `"layout_version": "skipped"` on the layouts only they use, one 7-line fix in `tools/mapjson/mapjson.cpp`; optionally stop assembling Hoenn map scripts and drop Hoenn wild rows. `MAP_*` constants stay, so C still compiles | remove the 518 map folders, their layouts and every C reference |
| ROM freed (of 6.19 MiB free now) | 0 | **+0.75 MiB** (level 1), **+1.19 MiB** (level 2), **+1.20 MiB** (level 3 with the Battle Tower kept, the recommended form); +1.51 MiB if the tilesets are also pruned (not recommended) | about +1.2 MiB, the same as SKIP, plus at most about 1 MB more, and only if Frontier, contests, TV and the rest are cut out of the C code |
| Benefit | none needed | smaller ROM; nothing else of value (ids can be reused without it, build time gains under 1 s per script edit, Porymap still lists every map) | Porymap list shorter; frees map slots (not needed) |
| Risk | none | low and mostly silent: copied Hoenn maps inherit the skip tag and vanish from the build, template layouts and tilesets disappear, a few screens read a null map header (section 5). Existing saves are safe (map numbers do not move) | **high**: saves in Hollowbrook, Route 1 and Crestfall break (map numbers 57 to 59 become 0 to 2), 63 compile and assembler errors in 9 files plus 37 failing lines in 8 shared script files on the first try, then 586 undefined script symbols, then more |
| Work for the lead (estimates) | 0 | about 1 to 2 hours (script ready and tested: `apply_skip.sh`), plus docs and a Porymap check | 4 to 8 sessions: 43 C files, 17 shared script files, 40 map scripts relocated, 262 pinned maps decided one by one |
| Upstream merge impact | none | low: 518 one-line `map.json` edits, `layouts.json`, 7 lines in a tool; re-run the script after each merge. Level 2 adds about 850 lines to `data/event_scripts.s` (conflict-prone when upstream adds includes) | high: deleted folders conflict with any upstream map fix, and 43 frequently edited C files change (`field_specials.c`, `region_map.c`, `battle_setup.c`, `overworld.c`) |
| Needs a ROM or save restart | no | no | yes (map numbers move) |
| My recommendation | **yes, now** | later, only if needed, after the maps are traced | no |

## 3. What Hoenn costs today

### 3.1 Files

- `data/maps`: **951 folders = 12 Veldris + 518 Hoenn-only + 421 FRLG** (FRLG is never built). Disk: Hoenn maps 5.4 MiB, FRLG maps 3.3 MiB, Veldris 0.15 MiB; 796 layouts, 452 of them Emerald-version (12 used by Veldris) and 344 FRLG. The repo tracks 30,610 files, 1,852 of them under `data/maps`.
- `data/maps/map_groups.json`: 76 groups. Group 75 (`gMapGroup_IndoorVeldris`) is Veldris only. Group 0 (`gMapGroup_TownsAndRoutes`) is mixed: 57 Hoenn maps, then Hollowbrook, Route 1, Crestfall at indexes 57 to 59. Groups 1 to 33 are pure Hoenn. Groups 34 to 74 are pure FRLG.
- Why group 0 matters: the Pokedex Area page only lists maps in `MAP_GROUP_TOWNS_AND_ROUTES`, `_DUNGEONS` and `_SPECIAL_AREA` (`src/pokedex_area_screen.c`), so Veldris routes and caves have to live in groups 0, 24 and 26 beside the Hoenn maps. Whole-group removal is therefore not possible for those three; the NULL-slot patch (option B) is what makes it work.

### 3.2 ROM bytes (from the linker map and `nm`; scripts in `rom_by_map.py`, `rom_by_object.py`, `systems.py`)

What fills the ROM (27.18 MB resident at `04385f05`):

| Object | Bytes | Share |
|---|---:|---:|
| `data/sound_data.o` (songs, voicegroups, cries) | 10,470,164 | 38.5% |
| `src/pokemon.o` (species data) | 6,186,335 | 22.8% |
| `src/graphics.o` | 1,019,288 | 3.8% |
| `data/event_scripts.o` (all map scripts and text) | 1,011,765 | 3.7% |
| `src/event_object_movement.o` (overworld sprites) | 812,946 | 3.0% |
| `src/tilesets.o` | 711,412 | 2.6% |
| `data/maps.o` (headers and layouts) | 698,036 | 2.6% |

What Hoenn map data costs inside that (ceiling for any purge of maps):

| Part | Bytes |
|---|---:|
| Hoenn map scripts and text | 623,290 |
| Hoenn map headers, events, connections | 118,756 |
| Hoenn layouts (+41,896 of dead FRLG layouts in the ROM) | 623,144 (+41,896) |
| Hoenn-only tilesets (+15,788 referenced by nothing) | 631,680 (+15,788) |
| **Hoenn map data total** | **2,054,554 (7.6% of the ROM)** |
| Hoenn game systems in C and shared scripts (ceiling, `systems.py`; some is shared with kept features) | about 1,017,000 |

So everything Hoenn is at most about 3.1 MB, 11% of the ROM. The two big blocks (music and species data) are not Hoenn.

### 3.3 Is ROM a problem for Veldris? Forecast

Measured: the 12 Veldris maps cost 33.3 KB in total (scripts and text 20.6 KB, headers and events 2.7 KB, layouts 10.0 KB), 2.8 KB a map. Hoenn averages, as a ceiling: 8.4 KB an outdoor map (big layouts), 1.4 KB an indoor map. For 51 outdoor and about 200 indoor Veldris maps that is at most 0.7 MB. Add about 0.3 MB for new town tilesets and 0.3 MB for trainer pictures and sprites: **about 1.3 MB, about 21% of the 6.19 MiB free.** Doubling the estimate still leaves about 3.6 MiB. Real data point: the DP sprite import (70 overworld sprites, 94 battle pictures) cost 0.23 MiB, which is in line with the 0.3 MB I allowed for sprites. ROM only becomes a problem if the author imports many more asset packs of that size (rule 8 already asks first). Engine edits so far cost about 0.08 MiB.

### 3.4 Flags, vars, trainer ids that only Hoenn uses (`reclaimable_ids.py`, lists in `analysis/reclaimable_*.txt`)

| | Reclaimable by value | Of which |
|---|---:|---|
| Flags | **587 Hoenn-only** (568 story and item, 6 system, 13 temp) plus 19 named but referenced nowhere | 162 `FLAG_ITEM_*`, 105 `FLAG_HIDDEN_ITEM_*`, 81 `FLAG_RECEIVED_*`, 108 `FLAG_HIDE_*`, 25 `FLAG_MET_*`, 19 `FLAG_DEFEATED_*`, 69 other |
| Vars | **67 Hoenn-only + 37 named but referenced nowhere** | e.g. `VAR_OLDALE_TOWN_STATE`, `VAR_OBJ_GFX_ID_*` |
| Trainer ids | **409 Hoenn-only** | 445 are in use (21 by Veldris through reuse) |

Two points that change the picture:

1. **None of this needs a purge.** A flag or var is "free" once nothing that still gets built names it. Rename it in `flags.h` or `vars.h` and keep the old name as an alias line (`#define FLAG_OLD FLAG_NEW`) so the unreachable Hoenn scripts still assemble. That is exactly how the 21 trainer ids were reused. (Reasoned from how the preprocessor works; not built, because a flag change recompiles the whole tree.)
2. The 162 + 105 + 81 item and gift flags are the ones `design/setup-budget.md` already plans to reuse by name for Veldris items. They are a pool the plan counts on already, not a new gain.

### 3.5 What Veldris still uses from Hoenn (these MUST stay)

- **Map folders, `MAP_*` constants, script labels: none.** Checked for all 12 Veldris maps.
- **One vanilla layout:** `LAYOUT_MART` (Crestfall Mart; shared with 14 Hoenn marts, 212 bytes). The other 11 layouts are Veldris's own.
- **Seven tilesets:** `gTileset_General`, `Petalburg` (all outdoors), `Building` (9 interiors), `Gen4Interior` (6), `PokemonCenter`, `Shop`, `PetalburgGym`.
- Engine-level reuse that is not a map: 21 reused Hoenn trainer ids (aliases), a few vanilla flags (`FLAG_RECEIVED_HM_CUT` ...), Hoenn route `MAPSEC` entries for Routes 4 to 21, the songs `MUS_LITTLEROOT` and so on, all shared scripts in `data/scripts`.
- **Planned reuse that does not exist yet (the design docs name them):** layouts `LAYOUT_POKEMON_CENTER_1F/2F`, `LAYOUT_MART`, `LAYOUT_HOUSE1/2`, `LAYOUT_HARBOR` (about 2 KB together); 17 tilesets named in the docs that a tileset prune would delete (`EliteFour`, `Facility`, `Lab`, `Underwater`, `MossdeepGym`, `DewfordGym`, `Lavaridge`, `SeafoamIslands` ... 139 KB of the 333 KB a prune frees; `Cave` survives it); and **a possible Battle Tower in Aldermere** that "would reuse the expansion's Battle Frontier tower" (`design/factions.md`). The Battle Tower is 7 maps (`BattleFrontier_BattleTower*`, 41 KB without layouts) plus the Frontier C code.

### 3.6 Hoenn systems that hang off Hoenn maps and are referenced from C

ROM figures are ceilings from `systems.py`. "Maps" counts Hoenn-only maps by name family; "pinned" is how many of those are named by C, headers or shared scripts that stay (`deletable_maps.py` with the 40 kept scripts counted).

| System | C and data objects | Script and text | Maps (pinned) | Main C files that name its maps |
|---|---:|---:|---|---|
| Battle Frontier, Tent, Pass | 250,668 (+93,600 of Frontier trainer slides in `trainer_slide.o`) | 9,606 | 72 (39) | `battle_tower.c`, `battle_pyramid.c`, `frontier_pass.c`, `field_specials.c`, `save_location.c` |
| Contests, Pokeblocks | 132,837 | 17,263 | 8 (2) | `contest_util.c`, `contest_hall.inc` |
| Secret bases, decorations | 37,806 | 9,866 | 24 (24) | `secret_base.c` |
| TV, news, Gabby and Ty, Old Man, Lilycove Lady, trends | 57,835 | 79,501 | in Routes 111/118/120, Slateport, Lilycove | `tv.c` (11 maps), `field_specials.c` |
| Pokenav conditions, ribbons, Match Call | 51,596 | 53,617 | rematch table in `battle_setup.c` (44 maps) | `battle_setup.c`, `match_call.c` |
| Apprentice, Trainer Hill, Safari Zone, Mirage Tower | 64,137 | 56,806 | 7 + 8 (5 + 7) | `trainer_hill.c`, `item_use.c`, `pokedex_area_screen.c` |
| Mini-games (Dodrio, Berry Crush, Jump, Roulette, Slots) | 128,426 | 97 | Mauville 11 (8) | `roulette.c`, `field_specials.c` |
| Hoenn trainer dialogue | 0 | 67,349 | | `data/text/trainers.inc` |
| **Sum of the rows above** | | **1,017,410** | | |
| Lilycove (department store elevator, museum, contest hall, harbor) | counted in the rows above | | 24 (13) | `field_specials.c`, `tv.c`, `region_map.c`, `save_location.c` |
| Link rooms (Pokemon Center 2F, Trade Center, Union Room, Colosseums) | not in the sum: `union_room.o` 34,099, `link.o` 9,991, `link_rfu_2.o` 14,136, `cable_club.o` 5,996 | | 21 (21) | `save_location.c`, `union_room.c`, `cable_club.inc` |
| Record mixing, trade | not in the sum: `record_mixing.o` 7,148, `trade.o` 74,050 | | none | `record_mixing.c`, `trade.c` (link features; in-game NPC trades use `trade.c` too) |
| Roamers, follower rules, rematch table | table rows only | | | `roamer.c` (20 maps), `follower_helper.c` (10), `battle_setup.c` |

None of these is planned for Veldris except possibly the Battle Tower. All are unreachable for the player, but they stay compiled in every option except a very deep DELETE.

## 4. The experiment (all in a clone, ROM sizes are the length of `pokeemerald.gba` without its `FF` padding)

Method: copy of the repo at HEAD, one option applied, `make -j4`, then the headless emulator robot (`design/tools/emu`, 17 quick tests plus the slow Route 1 night walk), a Veldris smoke test I wrote (`tests/test_purge_smoke.py`: all 12 Veldris maps load, the Crestfall nurse heals) and unit tests. The baseline at `e250a8e6` was 26,822,384 bytes (matches `devices.md`, 6.42 MiB free); at `04385f05` it is 27,060,492 bytes, equal to the length of the lead's own `pokeemerald.gba` (6.19 MiB free).

### 4.1 SKIP, step by step (`results/ladder.md`)

| Step | What | Edits | ROM saved | Free of 32 MiB |
|---|---|---|---:|---:|
| A | HEAD `e250a8e6` | | 0 | 6.420 MiB |
| B0 | tag the 461 maps in pure-Hoenn groups (stock tool) | 461 one-line `map.json` edits | 88,056 | 6.504 |
| B0+ | + skip the 383 layouts only those maps use | + `layouts.json` | 431,484 | 6.832 |
| **B1** | **all 518 maps (group 0 too), 440 layouts, 7-line mapjson patch** | + `tools/mapjson/mapjson.cpp` | **785,640** | **7.169** |
| B2 | + do not assemble 428 Hoenn map scripts (40 stay: C needs them) | + about 850 lines in `data/event_scripts.s` | 1,248,880 | 7.611 |
| B3 | + drop the C data of 87 dead tilesets | 3 big upstream data files change about 3,500 lines | 1,585,608 | 7.932 |
| B4 | + drop the 124 Hoenn rows of `gWildMonHeaders` | `wild_encounters.json` | 1,605,636 | 7.951 |
| L1 | `apply_skip.sh 1`: B1 with the six template layouts left live | as B1 | 783,852 | 7.168 |
| L2 | `apply_skip.sh 2`: L1 + B2 | as B2 | 1,247,092 | 7.609 |
| **R** | **`apply_skip.sh 3` with the 7 Battle Tower maps kept: L2 + B4, no tileset pruning (the recommended form)** | | **1,262,824** | **7.625** |

The ladder was measured at `e250a8e6`; **R was run again at `04385f05` with the same saving, 1,262,824 bytes** (27,060,492 to 25,797,668 bytes, free 6.19 to 7.40 MiB), a clean build, 17 of 17 quick emulator tests and 2 of 2 smoke tests, so the recipe survives the sprite import. The ladder numbers reproduce the 2026-10-09 numbers to within 4 bytes (B1 to B3: 785,640 / 1,248,880 / 1,585,608), with the same 40-map keep list, although four commits landed in between.

How B1 works: `mapjson` already skips maps whose `region` is not `REGION_HOENN` (that is how the 421 FRLG maps are left out) but keeps their `MAP_*` constants, `LOCALID_*` constants and numbers. The one problem is that it drops skipped maps from the group tables, which would shift Hollowbrook (57) out of its slot. The patch writes a `NULL` slot instead. Result: every `MAP_*` number is unchanged, no C file changes, no saves break. Checked: the generated `include/constants/map_groups.h` and `map_event_ids.h` of the SKIP build are byte-identical to HEAD's (`MAP_HOLLOWBROOK` is still 57 in group 0).

What passed: on **B3** the build had 0 errors, **17 of 17 quick emulator tests** (130 s), the 90 s Route 1 night walk (wild battles, a real fight) and the smoke test (2 of 2). On **B4** (everything except the recommended form): `make check TESTS=Veldris` 3 of 3, the 7 mass-outbreak tests (the only tests that name a Hoenn map) 7 of 7, and a partial run of the full suite (first 1,222 tests: 1,210 pass, 7 expected-fail, 5 known-failing, 0 fail; I stopped it, the whole suite takes more than 45 minutes here). On **R** and on **H** (4.3) the build had 0 errors and the 17 quick tests passed (H also the smoke test).

What R changes in the repo (`results/R_diffstat_*.txt`): 511 one-line `map.json` edits, `data/layouts/layouts.json` (429 tags), `data/event_scripts.s` (425 `.if` wrappers), `src/data/wild_encounters.json` (124 Hoenn rows removed), `tools/mapjson/mapjson.cpp` (+7/-1, saved as `mapjson_null_slots.patch`). 515 files, no C, no headers, no `src/` file at all.

Build time barely moves: re-assembling `event_scripts.o` takes 3.4 s instead of 4.0 s, and a full `make` after editing one script 3.85 s instead of 4.7 s. A clean build is the same (C is untouched).

### 4.2 DELETE: what breaks (`results/c1_true_delete_errors.txt`)

I removed the 518 folders, their `map_groups.json` entries, their layouts and their `.include` lines, then ran `make -k`.

First wave, compiler and assembler only:

- **63 errors in 9 files:** `src/tv.c` 24, `src/field_special_scene.c` 12, `src/field_specials.c` 12, `src/contest_util.c` 7, `asm/macros/map.inc` 4, `src/faraway_island.c` 1, `src/field_player_avatar.c` 1, `src/mirage_tower.c` 1, `asm/macros/event.inc` 1. They come from 42 missing names (41 `LOCALID_*` such as the 12 mart clerks, Gabby and Ty, contestants, truck boxes, plus `LAYOUT_SS_TIDAL_CORRIDOR`).
- **37 failing lines in 8 shared script files:** `abnormal_weather.inc` 8, `contest_hall.inc` 8, `battle_pike.inc` 7, `cable_club.inc` 5, `players_house.inc` 4, `safari_zone.inc` 2, `trainer_hill.inc` 2, `berry_blender.inc` 1 (`warp MAP_X` to a deleted map).
- No `MAP_*` constant went missing: `tools/mapjson/required_map_defines.json` already defines the ones C needs (upstream's FRLG build lacks the Hoenn maps the same way). What went missing are the `LOCALID_*` and layout names, which no such list covers.

Later waves (not rebuilt for deletion, but known from the SKIP experiment): without the 40 Frontier, Littleroot, Mauville, Sootopolis ... map scripts the linker reports **612 undefined references to 586 symbols** (`battle_tower.o` 330, `battle_pyramid.o` 126, `field_specials.o` 104, assembler 27, `pokemon.o` 25). The linker only reports after the compiler passes, so more would follow.

Static view of the full edit list (`deletable_maps.py`): **262 of the 518 Hoenn maps are named by something that stays**, 256 are not. The pinning files are 43 C and header files (`field_specials.c` pins 73 maps, `region_map.c` 53, `battle_setup.c` 44, `save_location.c` 39, `frontier_pass.c` 28, `secret_base.c` 24, `item_use.c` 21, `roamer.c` 20, `overworld.c` 18 ...), 17 shared script and text files, the scripts of the 40 kept maps (they name other maps too), and one test. The 256 free maps hold only 191 KB of map data plus 189 KB of layouts.

### 4.3 Two cheap deletions that need no code edits

- **FRLG folders (421, 3.3 MiB of maps):** deleting them builds with **0 errors**, ROM unchanged (-152 bytes). Keep `layouts.json` as it is: `src/map_name_popup.c` names seven `LAYOUT_CELADON_*` ids (removing the FRLG layouts gave 7 errors in that one file). Benefit: Porymap's map list drops from 951 to 530.
- **Hybrid H:** B2 + delete the 253 Hoenn maps nothing outside names (group 0 left alone so Veldris numbers never move) + the 421 FRLG folders, tag the other 265 as skipped. Builds with 0 errors, ROM 25,553,292 (-1,269,092), emulator 17 of 17 and smoke 2 of 2. Porymap's list drops from 951 to 277 folders. Cost: 1,591 files changed in the commit, and the modify/delete merge conflicts that come with it.

## 5. Traps found (so the author is not surprised)

1. **A copied Hoenn map vanishes silently.** Porymap's Duplicate Map copies the whole `map.json`, region tag included. A Veldris map made from a skipped Hoenn map is left out of the build with no error (CLAUDE.md already warns for FRLG). Proposed guard: `skip_lint.py` (tested on a synthetic case) fails when a tagged map is not on an allow-list (E3), a live map warps to a skipped one (E2), a live map uses a skipped layout (E1), or a wild row names a skipped map (E4). It also caught the Battle Tower lobby's warp into the skipped Frontier outdoors.
2. **Template layouts and tilesets.** Tagging layouts "only skipped maps use" would skip `LAYOUT_POKEMON_CENTER_1F` and the house layouts the plan reuses. `apply_skip.sh` keeps six template layouts live (2 KB) by default. Pruning tilesets (B3) deletes 17 tilesets the docs name. B3 is not part of the recommended form.
3. **Pokedex Area page** reads every wild row's map header (`pokedex_area_screen.c:358`). With Hoenn maps skipped those 124 rows give a null header and a junk section id, so a phantom area can appear. Level 3 (drop the rows) removes it. Read from the code, not run (the Pokedex needs a long button path).
4. **Evolutions on Hoenn maps:** Eevee to Leafeon (`MAP_PETALBURG_WOODS`), Glaceon and Crabominable (`MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM`), and `MAPSEC_NEW_MAUVILLE` for Magnezone, Probopass, Vikavolt. They cannot be met in Veldris with any option, and the Pokedex evolution page shows a wrong place name when the map is skipped. This is a design question (point them at Veldris maps), independent of the purge.
5. **Debug menu** warp or fly to a skipped map crashes (dev ROM only).
6. **Link rooms** (Pokemon Center 2F, Union Room, Trade Center) would crash if entered. The Veldris Center has no 2F, so nothing leads there.
7. **Porymap and the new values:** `REGION_HOENN_SKIPPED` and `"layout_version": "skipped"` are my own strings. Whether Porymap keeps unknown values when it rewrites `map.json` and `layouts.json` is unknown (no Porymap here). The fallback with known values is `REGION_KANTO` and `frlg`. Ask the author to open one tagged map and save once.
8. **Saves:** SKIP keeps every map number (reasoned and exercised by the emulator tests, no save file was loaded). DELETE moves them.
9. **Roamers:** `roamer.c` walks a fixed Hoenn route table; a roamer would enter a null header. No roamer is planned.

## 6. Recommendation and sequence

1. **Answer LEAVE now.** No limit is near, and the author is still tracing Hoenn bases.
2. Optional, free: `FRLG` deletion for a shorter Porymap list.
3. Revisit SKIP when the maps are traced and free ROM is under about 2 MiB, or if the author wants the shorter list. Then `apply_skip.sh 3` with the Battle Tower list if Aldermere will use it (one hour), run `skip_lint.py`, the emulator tests, and document it (`engine-edits.md`, CLAUDE.md rule on duplicated maps).
4. Reuse Hoenn-only flags, vars and trainer ids by alias whenever the spare pool runs short. No purge needed.
5. Never pick DELETE unless the author wants the C systems gone too; at that point it is a project of its own.

## 7. Not verified

- Porymap with the new tag strings (section 5, item 7). No Porymap here.
- Loading an old save file on the SKIP ROM (reasoned only).
- The Pokedex Area and evolution pages (code read only).
- The full unit-test suite (partial run only).
- The `make release` ROM under SKIP (data-only change; not built).
- DELETE beyond the first wave; the labour estimate is from the static edit list.
- Flag and var reuse by alias (reasoned, not built).
- Everything on mGBA, not on Delta (VBA-M).

## 8. Files (all in `/tmp/claude-0/-home-user/9fd7bd62-02de-54b5-9261-788aa0f695b6/scratchpad/out4/arch/`)

| File | Use |
|---|---|
| `brief.md` | this document |
| `apply_skip.sh` | the SKIP recipe, levels 1 to 3, keep lists; non-destructive; refuses the real repo unless `PURGE_ALLOW_REAL_REPO=1` |
| `purge_experiment.py` | the steps it calls (`patch-mapjson`, `tag-maps`, `tag-layouts`, `skip-scripts`, `prune-wild`, `delete-frlg`, `delete-listed`, `delete-maps`, `restore`); `restore` never runs on the real repo |
| `prune_tilesets.py` | B3, with `--keep=gTileset_X,...`; not recommended |
| `resolve_undefined.py` | finds which Hoenn map scripts C needs (the loop that produced the 40) |
| `skip_lint.py` | the proposed guard for SKIP |
| `deletable_maps.py`, `systems_maps.py` | which maps are pinned by C or shared scripts; per-system map counts |
| `reclaimable_ids.py`, `static_refs.py`, `rom_symbols.py`, `rom_by_map.py`, `rom_by_object.py`, `systems.py` | the measuring tools from the earlier pass, rerun on HEAD |
| `build_stage.sh`, `time_incremental.sh`, `ladder.py`, `err_report.py`, `undef_report.py`, `romsize.py` | build, timing and report helpers |
| `tests/test_purge_smoke.py` | the Veldris smoke test for the emulator robot |
| `results/` | `ladder.md`, build logs, emulator logs, `keep_scripts.txt`, `dead_tilesets.txt`, error reports |
| `analysis/` | per-symbol table, ROM by map, `reclaimable_*.txt`, `static_refs.txt`, deletable sets (measured at `e250a8e6`); `analysis_04385f05/` is the same rerun on the current HEAD, with identical Hoenn numbers |
| `mapjson_null_slots.patch` | the 7-line tool patch behind SKIP |

## 9. What the lead still has to do

1. Give the author the section 1 table and the one-word question. Do not apply anything before the answer.
2. If `LEAVE`: nothing. Optionally add one line to `design/engine-limits.md` (ROM row) that the purge was measured and not needed, with the 1.2 MiB figure, and keep `apply_skip.sh`, `purge_experiment.py`, `skip_lint.py`, `results/keep_scripts.txt` somewhere durable if you want the recipe later (they are only in the scratchpad now; they are small, `design/tools/purge/` would be the place).
3. If `SKIP`: tell the author to close Porymap; in a fresh clone run `apply_skip.sh <clone> 3 <Battle Tower maps if wanted>`, build, run the emulator tests and `skip_lint.py`, then repeat in `/home/user/Veldris` with `PURGE_ALLOW_REAL_REPO=1`; update `design/engine-edits.md` (mapjson patch, `event_scripts.s` wrappers, `layouts.json`, `wild_encounters.json`), `design/engine-limits.md` row 11, `design/flags.md` (nothing changes), `CLAUDE.md` (a Duplicate Map of a skipped Hoenn map copies the skip tag), add `skip_lint.py` to the pre-commit hook. `results/keep_scripts.txt` (the 40 maps C needs) is valid for HEAD `e250a8e6` and `04385f05` (the recipe built clean on both); if C changes, regenerate it with `resolve_undefined.py` in a clone. Ask the author to open one tagged map in Porymap and save once (section 5, item 7).
4. If `DELETE`: ask again with the cost in section 4.2 in front of the author. Do not start.
5. `FRLG` add-on: `purge_experiment.py <clone> delete-frlg`, then mirror in the real repo (delete the 421 folders, drop them from `map_groups.json`, remove their `.include` lines from `data/event_scripts.s`; keep `layouts.json` whole). Update the CLAUDE.md sentence that says FRLG `MAP_*` constants still exist.
