# Engine limits and config switches

Hard limits of this tree (pokeemerald-expansion 1.17.1, an untagged commit after 1.17.0; Emerald build). Numbers were measured with the preprocessor or read from source by two independent audits. Nothing here was tested in an emulator.

Read this before designing anything that scales: 18 towns, 33 routes, 9 gyms and a lot of trainers push against several of these.

## Limits

| # | Limit | Number | What it means for Veldris |
|---|---|---|---|
| 1 | **Badges** | 9 (was 8, hard-wired) | A 9th badge has no flag slot: 0x86F is already `FLAG_VISITED_LITTLEROOT_TOWN`. Also sized for 8: `gBadgeFlags` (`src/event_data.c`), the trainer card and its art (`badges.png` holds 8), white-out money and badge-level tables, obedience checks, the level-cap table (`src/caps.c`), the main menu, shop criteria, TV and match call. **Done 2026-09-29:** 9 badges through a data-driven table; see [badges.md](badges.md). Original problem and direction: study public hacks with more than 8 badges and plan a custom badge case with our own art ([badges.md](badges.md), plan written 2026-09-29, recommends a data-driven badge table). Options: 8 badges and the 9th gym grants a non-badge reward tracked by its own flag, or a real 9th badge touching all of the above plus new art |
| 2 | **Trainer IDs** | 9 spare (ids 855 to 863, flags 0x857-0x85F) | Every trainer's defeated flag is `0x500 + id`. Raising `MAX_TRAINERS_COUNT` shifts every system and daily flag and grows `FLAGS_COUNT` (fine on a fresh start, and it needs a header edit). **Save headroom:** `SaveBlock1` is 15,696 bytes of 15,872, so about 176 bytes, roughly 1,400 flags, so a few hundred more trainers fit. `include/config/save.h` switches can free about 3,000 more bytes. Untested |
| 3 | **Map sections** | 43 more fit | Section ids are one byte (`mapsec_u8_t`) and `0xFD-0xFF` are special. 209 exist. New ids go at the end of the JSON list. Veldris wants 51. See [region-map.md](region-map.md) |
| 4 | **Town map picture** | 256 distinct 8x8 tiles, 28 x 15 cells | `map.bin` has one byte per position. Hoenn's uses 233. The grid size is a constant in `src/region_map.c` |
| 5 | **Spare flags and vars** | 317 flags, 22 vars | See [flags.md](flags.md) |
| 6 | **Map size** | `(width + 15) * (height + 14)` must be at most 10240 | 80 x 60 is fine (7,030). 100 x 100 is too big (13,110) |
| 7 | **Tilesets per map** | 512 primary + 512 secondary metatiles, 13 palettes (6 primary + 7 secondary) | Dual-layer metatiles only (`NUM_TILES_PER_METATILE` is 8). Triple-layer tilesets need an engine patch |
| 8 | **Objects and events** | 16 live object events; 64 object templates per map; `MAX_SPRITES` 64; event counts are one byte | With shadows enabled an object can cost 2 sprites, so crowded town or gym maps hit the sprite limit first |
| 9 | **Map groups** | 75 groups, group and map numbers must stay at most 127 | Warp data stores them as signed bytes. Adding 51 outdoor maps to group 0 gives 108, which is fine |
| 10 | **ROM space** | 32 MiB maximum; 25.73 MiB used, **about 6.27 MiB free** | `P_CRIES_ENABLED`, `P_FOOTPRINTS` and the `species_enabled.h` switches free space (cries alone are over 25% of the ROM by upstream's comment) |
| 11 | **What gets built** | Only maps with region `REGION_HOENN` and layouts with `layout_version` `emerald` | The FRLG maps and layouts are skipped by the Emerald build. New maps must stay at the defaults or they are silently left out |
| 12 | **Fly** | Needs the Feather Badge; only 16 vanilla `FLAG_VISITED_*` flags | Each new fly town needs 3 small C edits, or with the proposed A-prime hooks one table row (draft in [region-map.md](region-map.md), not applied) |
| 13 | **Section names** | 16 characters, charmap characters only | Longer overflows a buffer |

## Config switches worth knowing

All in `include/config/`. Prefer these to editing code.

| File | Switch | Why it matters here |
|---|---|---|
| `name_box.h` | `OW_NAME_BOX_NPC_TRAINER` (off), `OW_FLAG_SUPPRESS_NAME_BOX` | A speaker name box above dialogue, useful for Prof. Fennick, Greta and Troglodyte |
| `quickstart.h` | `ENABLE_QUICKSTART` (on) | Press SELECT on the title screen to skip the intro while testing. Remember it when testing intro dialogue edits |
| `debug.h` | `DEBUG_OVERWORLD_MENU` (on in a normal `make`) | Warp, set flags and vars. Use it to test flying between the first three towns |
| `overworld.h` | `OW_FLAG_POKE_RIDER` (off), `OW_POPUP_GENERATION` (Gen 3), `OW_REMATCH_BADGE_COUNT` (5) | Poké Rider lets the Pokénav map fly without the HM if pointed at a spare flag |
| `wild_encounter.h` | `WE_FLAG_NO_ENCOUNTER` (0) | Point at a flag to switch encounters off, handy for cutscene maps |
| `caps.h` | `B_LEVEL_CAP_TYPE` (none) | Level caps by badge count. Its table is sized for 8 badges plus the champion flag |
| `save.h` | `FREE_MYSTERY_EVENT_BUFFERS`, `FREE_RECORD_MIXING_HALL_RECORDS`, `FREE_MYSTERY_GIFT` (all off) | Free about 3,000 save bytes if the save block gets tight |
| `pokemon.h` | `P_GBA_STYLE_SPECIES_GFX` and `_ICONS` (off), `P_CRIES_ENABLED`, `P_FOOTPRINTS` | The first two switch to the Gen 3 look already in the tree, so the `sprites` repo's Emerald art is not needed |
| `map_preview_screen.h` | `MPS_ENABLE_MAP_PREVIEWS` (`IS_FRLG`, so off here) | FRLG-style splash when entering an area |
| `text.h` | `TEXT_SPEED_INSTANT`, `AUTO_SCROLL_TEXT` | Speeds up testing dialogue |

## Update this file when

A limit is measured again, a switch is used, or an engine edit removes or moves a limit (log the edit in [engine-edits.md](engine-edits.md) too).
