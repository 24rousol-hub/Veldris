# Badges: survey of other hacks and a plan for Veldris

**Status: IMPLEMENTED (option C, a data-driven badge table), 2026-09-29, on the author's go-ahead** ("do 9 gyms + Elite Four and Champion, do your best for badges, outsource the badge art, look at my fork of the asset repo"). The survey and options below are kept as the reasoning. **Checked in an emulator on 2026-09-29:** the ROM boots, and the trainer card was opened at 0, 1 and 9 badges (screenshots in the session, not committed). At 0 badges the strip shows 9 grey sockets, at 1 the first is the Stone badge, at 9 all nine icons show with no overlap. Badges were set through the debug menu, so nothing has awarded one by a gym script yet.

## What was built

- **`include/veldris_badges.h` and `src/veldris_badges.c` (hack-owned).** One list, `VELDRIS_BADGE_LIST(X)`, with a row per badge: `X(flag, iconSlot)`. It generates both `gVeldrisBadges[]` and `gBadgeFlags[]`, and a compile-time check fails the build if the row count is not `NUM_BADGES`. Rows are in display order on the trainer card: reorder them to change that order, or change `iconSlot` to pick different art. Reordering does not move any HM, because HM gating names a badge by its flag, not by its row (see the HM gating bullet below). `GetBadgeCount()` counts earned badges.
- **9 badges.** Badges 1-8 keep the vanilla flags. Badge 9 is `FLAG_BADGE09_GET` = 0x88E (spare system flag, outside the story-beat range that [flags.md](flags.md) reserves). Badge 10 to 12 needs a flag, a row and art, plus the spots under 'Known limits' that assume 9 badges or fewer. The trainer card itself fits 12.
- **Trainer card.** The 8 numbered slots baked into `front.bin` are gone. Badges are drawn edge to edge (2 tiles each) and centred in the strip, so the front page shows all 9 (up to 12). Badges not yet earned show an empty grey socket (icon slot 15, `BADGE_ICON_SLOT_EMPTY`), so the player can see all 9 places. Keep slot 15 for that socket art; badges use slots 0-14. The sheet `graphics/trainer_card/badges.png` is 128x32: row 1 = slots 0-7, row 2 = slots 8-15. Row 2 loads at BG3 tile 352, clear of the mon icons (224-319) and the FRLG stickers (320-351).
- **Every "count the badges" loop** (main menu, save menu, TV, shop, catch malus, match call, debug menu, battle setup) now goes through `gBadgeFlags[]` or `GetBadgeCount()`, so a non-contiguous badge flag works. The white-out money table `sWhiteOutBadgeMoney` is sized `NUM_BADGES + 1` because it is indexed by badge count (0 to 9).
- **HM gating** (`src/field_move.c`) reads `gBadgeFlags[arg]`. Each move's `arg` is `FLAG_TO_BADGE(<badge flag>)`, which resolves that flag to its row in the table at compile time (`BADGE_INDEX_<flag>`, generated from `VELDRIS_BADGE_LIST` in `include/veldris_badges.h`). So any HM can be tied to any badge by changing the flag in that move's row, and never write a literal index. **Dive is bound to badge 9** (row 8; `FLAG_BADGE09_GET` is not contiguous with badges 1-8). The old `flag - FLAG_BADGE01_GET` arithmetic read past the table for badge 9; fixed 2026-10-09, see [engine-edits.md](engine-edits.md). The full HM list is in [field-moves.md](field-moves.md).
- **Level and EV caps** (`src/caps.c`) have a badge 9 row. Caps follow the gym aces: 60 at badge 9 and 75 for the Champion ([gyms.md](gyms.md)). They are off by default (`B_LEVEL_CAP_TYPE`).
- **Obedience** (`src/battle_util.c`): vanilla again. The 2026-09-29 edit (badge 9 ignoring obedience, badge 8 giving level 90) was reverted on 2026-10-09 because it changed no outcome, see [engine-edits.md](engine-edits.md). Do not re-add a badge 9 tier unless the level scale or in-game trades change.
- **Art.** Slots 0-7 are Kaixer's coloured badges from the author's asset repo fork (`User Interface/Kaixer/Trainer Card Badges`). Slot 8 is a plain gold placeholder disc I drew. **Badge art is to be outsourced**, so the sheet is the one file to swap. Credit rows are in `CREDITS.md`.
- Edits to upstream files are logged in [engine-edits.md](engine-edits.md).

## Badge art redrawn (2026-10-01, author: 'you can draw the badges and I will tweak from there')

`graphics/trainer_card/badges.png` is now all new art, drawn for this hack by `design/tools/draw_badges.py` (re-run it from the repo root to regenerate; or edit the PNG, keeping its palette). New shared 16-colour palette (index 0 background). Every badge is drawn on a supersampled canvas and sampled to exactly 14x14 (symmetric about the tile centre, so none looks off-centre), and the card now leaves one empty tile between neighbours (`BADGE_PITCH` in `src/trainer_card.c`, 3 tiles for 9 badges; with more than 9 it falls back to 2). Seen in mGBA with all nine earned: evenly spaced, no overlap. Slots 0-8 follow the gym order, slot 15 is the empty socket: 0 Standard (silver ring, blue centre; Normal), 1 Bug (green hexagon, yellow centre; Briarwick), 2 Ghost (purple wisp with eyes), 3 Steel (grey cog), 4 Ice (white snowflake on blue disc), 5 Flying (feather; the Feather Badge), 6 Poison (green drop, purple bubbles), 7 Fairy (pink heart, white star), 8 Water (blue wave disc). Checked as an enlarged render and the ROM builds; **seen on the trainer card in mGBA on 2026-10-01 with all nine earned (debug menu, Toggle All badges): all nine draw cleanly, no overlap**. Names for badges 2 to 9 are still undecided (PROPOSED: Briar, Gloom, Forge, Hoar, Feather, Hemlock, Primrose, Beacon). The Kaixer art and the gold placeholder described below are gone; their CREDITS rows are marked replaced.

## Known limits and things not done

- **One palette for all badges.** The card has no free BG palette bank (0-4 card and stars, 5-10 mon icons, 11-14 stickers, 15 text), so all badges share bank 3, one 15-colour palette. A per-badge palette is not possible without freeing a bank. Any new art has to use the sheet's palette (or replace it for all badges together).
- **Badge 1 is the STANDARD BADGE (author, 2026-09-29):** the standard you must meet to start the gym challenge. Names for badges 2 to 9 are not decided.
- **Badge 1 is now silver with a blue centre (author request, 2026-09-29).** Slot 0 was re-coloured using colours already in the shared palette (greys for the outside, blues for the inside), so no other badge changed. It is still the Stone Badge shape, a stand-in for art drawn to match Greta and the Normal-type gym. Checked as a rendered image, not yet on the card in an emulator.
- **The Kaixer badges are recolours of the Emerald shapes** (Stone, Knuckle...), so they will not match Veldris gym themes and derive from Game Freak art. Fine as a stand-in.
- **Names:** the table has no badge names yet, because the gym themes are not decided. Nothing in the game prints a badge name today.
- **Only 15 badge slots** are usable because slot 15 is the empty socket.
- **Checked in an emulator (2026-09-29):** the card layout, the `front.bin` edit and the row-2 tile load at BG tile 352 look right at 0, 1 and 9 badges. **Not checked:** 2 to 8 badges, badge 9 on its own, the back of the card, the girl's card, a long player name, save and load, and the FRLG-style link card.
- **FRLG card type** (only from a link partner) keeps the vanilla 8-slot layout and does not show badge 9. `veldris_badges` is Emerald only and would not compile with `IS_FRLG`.
- **Rematches and Route 23 style badge checks** still use `FLAG_BADGE05_GET` and the FRLG scripts; nothing in Veldris uses them yet.
- Only the Crestfall gym (badge 1) is built, so `FLAG_BADGE09_GET` is never set in play. Use the debug menu to test.
- **Sites that assume 9 badges or fewer** (nothing is wrong with 9; check these in the same commit as a 10th badge, `grep -n 'NUM_BADGES\|BADGE09' src/*.c`):
  - `src/menu.c` `BufferSaveMenuText` writes one character (`flagCount + CHAR_0`), so 10 shows a wrong glyph. It needs a two-digit buffer.
  - `src/main_menu.c` `MainMenu_FormatSavegameBadges` formats with `ConvertIntToDecimalStringN(..., 1)`, so 10 prints '?'. Change the digit count to 2.
  - `sWhiteOutBadgeMoney[NUM_BADGES + 1]` and `sBadgeLevel[]` in `src/battle_script_commands.c` need one more entry per added badge, or the new slot reads as 0 or runs past the array.
  - `src/caps.c` level and EV cap tables have explicit rows (`FLAG_BADGE09_GET`), so each new badge needs a row in both.
  - `BADGE_PITCH` in `src/trainer_card.c` already falls back to 2 tiles above 9 badges and needs no change.

The rest of this file is the research and reasoning that led here.

Research date: 2026-09-29. Method: GitHub code search, then shallow read-only clones (added with the `add_repo` read path) of the repos below, reading the files cited. Nothing was built or run, so every statement about behaviour comes from reading source. **The PokéCommunity threads could not be read (HTTP 403, not worked around).** They are listed by URL only.

## Why this is needed

Veldris has 9 gyms, and the engine was built for 8 badges (before the table below was implemented). `FLAG_BADGE01_GET` to `FLAG_BADGE08_GET` are `SYSTEM_FLAGS + 0x7` to `+ 0xE`, and `SYSTEM_FLAGS + 0xF` is already `FLAG_VISITED_LITTLEROOT_TOWN`, so a 9th badge cannot simply be the next flag. See [engine-limits.md](engine-limits.md) row 1 and open decision 1 in [game-bible.md](game-bible.md). The author also asked to consider our own badge case with our own art so badges can be mixed and matched.

## Survey table

| # | Hack or tutorial | Link | Badges | Approach | Read? | Licence or credit terms |
|---|---|---|---|---|---|---|
| 1 | Pokémon Heart & Soul (HnS), commit `751823ab` | https://github.com/PokemonHnS-Development/pokemonhns | 16 | Keeps `NUM_BADGES` at 8. Adds `FLAG_BADGE09..16_GET` as a separate block at `SYSTEM_FLAGS + 0x85..0x8C`. Card shows 9-16 in a second row on the back page | Cloned, read | No LICENSE file. README lists credits and says it is open source and free to fork. That is informal, not a licence |
| 2 | Elite Redux, commit `334c5455` | https://github.com/Elite-Redux/eliteredux-source | 16 defined, 8 used | `NUM_BADGES = 1 + FLAG_BADGE16_GET - FLAG_BADGE01_GET`, plain-number flags 2889..2904 | Cloned, read | No LICENSE file. README points to their thread for credits |
| 3 | celias-stupid-repository (FRLG), commit `8b31f247` | https://github.com/celias-stupid-team/celias-stupid-repository | 10 | `NUM_BADGES` hard-coded to 10. Extra badges hang off unrelated flags. Second badge row on the card | Cloned, read | README is unchanged pret text, no LICENSE file |
| 4 | soulgold, HNS_modern, Gold-And-Silver-Gen-3-Decomp | https://github.com/Eemeliri/soulgold, https://github.com/resetes12/HNS_modern | 16 | Same trainer card block as HnS (code-search snippets) | Snippets only | Not checked |
| 5 | CrystalDust, commit `47408804` | https://github.com/Sierraffinity/CrystalDust | 8 in this tree | Not a >8 example. Two forks matched `FLAG_BADGE09_GET` in search | Cloned; forks not read | Not checked |
| 6 | Pokémon R.O.W.E. (`PokemonROWE`, `RoweSource`) | https://github.com/BelialClover/PokemonROWE | **8 in the source read** | The "16 badges" claim is **not confirmed**. Two other repos matched `FLAG_BADGE09_GET` and were not read | Cloned, read | No LICENSE file |
| 7 | Upstream pokeemerald-expansion and pret/pokeemerald | https://github.com/rh-hideout/pokeemerald-expansion | 8 | No issue, PR or config switch about badge count found (searches only). Related config: `B_FLAG_BADGE_BOOST_*`, `B_MISSING_BADGE_CATCH_MALUS`, `OW_REMATCH_BADGE_COUNT`, and the 8-badge level-cap table | Searches | n/a |
| 8 | PokéCommunity: "Increase the number of badges", "Having more than 8 badges", "Badges on Trainer Card" | https://www.pokecommunity.com/threads/pokeemerald-increase-the-number-of-badges.538944/, .../having-more-than-8-badges.348689/, .../badges-on-trainer-card.287807/ | ? | Search summaries say the work is in `src/trainer_card.c` (`SetDataFromTrainerCard`, `DrawStarsAndBadgesOnCard`) and a new flag after the last badge. That is a search summary, not something read | **Not read (403)** | Unknown |

Also not read: `eeveeexpo.com/threads/8455` (verification wall), and Pokécharms and Serebii badge threads (search titles only). **No public tutorial for more than 8 badges on a decomp was found in what could be read.**

## What each hack changed and left broken

| Concern | HnS (16) | Elite Redux (16) | celias (10, FRLG) |
|---|---|---|---|
| Badge flags | 8 vanilla, plus `FLAG_BADGE09..16_GET` in a spare block (`flags.h:1510-1517`) | 16 contiguous plain numbers (`flags.h:1321-1337`) | 8 vanilla plus special flags (`flags.h:384`) |
| `NUM_BADGES` | Unchanged at 8; local `NUM_BADGES_TOTAL` in the card (`trainer_card.c:37-40`) | 16 | Hard-coded 10 (`flags.h:1435`) |
| Trainer card | Front page keeps 8. `DrawExtraBadgesOnBack()` draws the other 8 on the back (`trainer_card.c:1603-1622`), with a combined badge sheet (`:587`) | Draw loop steps `x += 3` for 16 badges (`:1507`), so badges 9-16 land past the 30-tile screen. **Probable layout bug, not run** | Second row: `if (i == 8) tileNum += 16` (`:1591-1620`) |
| Badge art | `badges.png` and `badges_kanto.png`, each 128x16 (8 badges), merged into one sheet | `badges.png` is 128x16 (8 badges) | Extra tiles allocated (`badgeTiles[0x80 * (NUM_BADGES + 4)]`) |
| Main menu, match call, obedience | **Still count only 8** (`menu.c:2143`, `main_menu.c:2360`, `match_call.c:1857`, `battle_util.c:3973`) | Count 16 through `NUM_BADGES`, but `battle_setup.c:329-338` `sBadgeFlags` lists only 8 (the rest are zero) | Quest log arrays had to be extended (`quest_log_events.c:415`) |
| Trainer card source of truth for badges 9+ | Reads `FLAG_DEFEATED_*_GYM` flags, not the new badge flags | n/a | Special-cased flags |
| Other | Save fix-up for old saves (`save.c:965-978`) | Extra badges defined but unused (`grep` found no `BADGE09`+ uses) | Very hack-specific |

Lessons: (1) widening `NUM_BADGES` alone is not enough, the art and layout must change too (Elite Redux); (2) hacks that leave `NUM_BADGES` at 8 silently ignore badge 9+ in the menu, match call and obedience code (HnS); (3) nobody found a config switch or an upstream feature, so this is always custom code.

## What is hard-wired to 8 in the Veldris tree

From reading this tree (`grep` for `NUM_BADGES`, `gBadgeFlags`, `FLAG_BADGE0`):

| Site | What it does | Sized for 8 by |
|---|---|---|
| `include/constants/flags.h:1359-1367` | Badge flags and `NUM_BADGES` | Contiguous flags, `+0xF` taken |
| `src/event_data.c:39-48` `gBadgeFlags[NUM_BADGES]` | Flag list used by `debug.c`, `match_call.c`, `battle_setup.c`, `battle_script_commands.c` | Array size |
| `src/trainer_card.c:62,86,855,1525` | Card data, badge tiles (`0x80 * NUM_BADGES`), draw loop with `x += 3` | Array sizes, 8 in a row |
| `graphics/trainer_card/badges.png` | Badge art, 8 badges | Sheet width |
| `src/main_menu.c:2213`, `src/menu.c:1859`, `src/tv.c:1689` | Badge counts | Loop over `NUM_BADGES` |
| `src/shop_criteria.c:53` | Shop stock by badge count (expansion only) | Loop |
| `src/battle_script_commands.c:8085-8094` | Catch-rate malus, uses `sBadgeLevel[]` (expansion only) | Table size |
| `src/caps.c:12-19` and `:89-96` | Level cap and EV cap tables keyed by `FLAG_BADGE01..08` and `FLAG_IS_CHAMPION` (expansion only) | Explicit flags |
| `src/battle_util.c:5645-5662` | Obedience by badge | Explicit flags 01-08 |
| `src/field_move.c:24-119` | HM gating: `FLAG_TO_BADGE(FLAG_BADGE0n_GET)` as an index from `FLAG_BADGE01_GET` | Index relative to badge 01 (as found; since fixed for badge 9 on 2026-10-09 and now a table lookup, see 'What was built') |
| `src/battle_util.c:6829-6840`, `src/battle_main.c:4409` | Badge stat boosts via `B_FLAG_BADGE_BOOST_*` (`include/config/battle.h`) | Config flags |
| `src/pokenav_match_call_list.c:517`, `include/config/overworld.h:148` | Rematch unlock at a badge count | `FLAG_BADGE05_GET`, `OW_REMATCH_BADGE_COUNT` |

Spare flags for a separate badge block: `SYSTEM_FLAGS + 0x86..0x9F` (`FLAG_UNUSED_0x8E6..0x8FF`) are unused in `flags.h`, but [flags.md](flags.md) currently **reserves 0x8E5-0x91E for story beats**. A badge block needs the author's OK to carve out (for example 0x8E6-0x8ED for badges 9 to 16), and any claim goes in `flags.md` in the same commit.

## Options

| | A. 8 badges plus a non-badge reward for gym 9 | B. HnS-style: `NUM_BADGES` stays 8, extra flags, patch each site | C. **Custom badge table (recommended)** |
|---|---|---|---|
| What the player gets | 8 real badges, gym 9 gives a different item and flag | 9+ real badges | 9+ real badges, mix and match art |
| Engine files touched | 0 | About 12 to 14 | About 14 to 16, one new file |
| Art | None | Extend badge sheet | Own icon sheet, per-badge palette |
| Risk | Design feels lopsided; the Elite Four gate still works | Sites left at 8 ignore badge 9 (as HnS does) | More code, but the failure mode is a compile error, not a silent skip |
| Reversible | Trivially | Yes, but spread across many files | Yes, mostly one table |

### Recommendation: C, done in stages, with A as the fallback

**Design (as built, see "What was built" above; the trainer card differs from this first sketch: one row of up to 12 edge-to-edge badges instead of two rows of 6):**

1. **A data-driven badge table** in a new hack-owned file (for example `src/veldris_badges.c` with `include/veldris_badges.h`), one row per badge slot: `id`, `flag`, `name`, `iconTile` (index into our own icon sheet), `palette`. Order in the table is the display order, so badges can be reordered or swapped without touching code. Badges 1 to 8 keep the vanilla flags `FLAG_BADGE01..08_GET`; badges 9 and up use flags from a claimed spare block. Vanilla flags stay in place so other code (and the debug menu) keep working.
2. **One set of helpers** replaces the scattered loops: `GetBadgeCount()`, `HasBadge(id)`, `GetBadgeFlag(id)`. Every `NUM_BADGES` loop (`main_menu.c`, `menu.c`, `tv.c`, `match_call.c`, `shop_criteria.c`, `battle_script_commands.c`, `debug.c`, `battle_setup.c`) calls them. `gBadgeFlags` becomes derived from the table.
3. **Trainer card that holds 9 or more.** Front page becomes two rows of up to 6 badges (12 slots) instead of one row of 8, so a badge case with 9 to 12 badges stays on the front. This needs new art: a badge icon sheet of 16x16 icons (the existing `badges.png` is 128x16, 8 icons) with a per-badge palette, and new positions in `DrawStarsAndBadgesOnCard` (`src/trainer_card.c`, loop at about line 1525). The `badgeTiles` buffer is sized from the slot count. The exact tile budget and whether a per-badge palette fits the card's palette slots are **not checked yet**.
4. **Decouple HM gating and level caps from the badge index.**
   - `src/field_move.c`: the `arg` of each move is `FLAG_TO_BADGE(FLAG_BADGE0n_GET)`, an index from badge 01. Replace with a table entry naming the badge id required, so any gym can grant any HM.
   - `src/caps.c`: the level and EV cap tables list `FLAG_BADGE01..08_GET` directly. Replace with rows keyed by table badge id (and the champion flag), so a 9th cap is one row.
   - `src/battle_util.c` obedience: the same, keyed by badge id.
   - Vanilla-Emerald-only assumptions (for example Rustboro's gym giving Cut) are not needed in Veldris, so the mapping is entirely ours.
5. **Save compatibility:** a new game is planned, so none is needed. If a save from an earlier build ever matters, HnS did a fix-up in `save.c` and the same would be needed.

**Estimate:** about 14 to 16 files (the 12 to 13 sites in the table above plus the new file, header and art). Roughly: the new table file, `flags.h` (claim the spare flags), `event_data.c/.h`, `trainer_card.c`, `main_menu.c`, `menu.c`, `tv.c`, `match_call.c`, `shop_criteria.c`, `battle_script_commands.c`, `caps.c`, `battle_util.c`, `field_move.c`, `debug.c`, `battle_setup.c`, plus the icon sheet. Not measured by building it.

**Risks:**
- Trainer card layout and art are the real work; Elite Redux shows what happens if the layout is not redone.
- Upstream merge conflicts in about 14 upstream files. Mitigation: keep each edit tiny and put all logic in the hack-owned file, log every edit in [engine-edits.md](engine-edits.md).
- Expansion-only sites (`caps.c`, `shop_criteria.c`, catch malus) exist in Veldris but not in the hacks surveyed, so there is no prior art to copy for them.
- Needs the author's decision on spare flags: 0x8E6-0x8ED sits inside the range [flags.md](flags.md) reserves for story beats.
- All of this is pre-implementation source-reading. The table was built later and the card checked in mGBA (see the top of this file).

**Reuse and credit:** none of the hacks surveyed has a LICENSE file, so **do not copy their code**. Their approach is described here as an idea only. If any code or art is later borrowed, credit it in `CREDITS.md` and ask the author of that hack first. HnS asks to be told about missed credits.

**Fallback (option A)** costs no engine work: 8 real badges and the 9th gym awards a non-badge reward tracked by its own flag. It can be switched to C later.

## Decisions for the author (answered 2026-09-29: 9 real badges, option C, badge art to be outsourced, use the asset repo fork; badge flag 0x88E chosen instead of the 0x8E6 proposal so the story-beat range stays intact)

1. Real 9th badge (option C, or B) or a non-badge 9th reward (option A)?
2. If C: OK to carve a badge flag block out of the spare pool (proposal: 0x8E6-0x8ED, which overlaps the story-beat reservation in `flags.md`)?
3. Is the badge case art yours to draw, or should badge icons be sourced (with credit) from your asset repos? Nothing has been checked in those repos for badge art.
4. Go-ahead to write an implementation plan file by file (still no engine edits) before any code change.
