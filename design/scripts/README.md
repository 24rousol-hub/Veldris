# design/scripts: draft map scripts (UNBUILT)

**DRAFT, UNBUILT, not included in `data/event_scripts.s`.** Status: PROPOSED. Hand-written `scripts.inc` style (not Poryscript), ready to paste into the matching map's `scripts.inc` once the author builds the map in Porymap. The text labels come from `design/dialogue/*.inc` and get appended to the same `scripts.inc` (each label exactly once). Nothing here is claimed in `include/constants/flags.h` or `vars.h`.

Checked: all four files plus the dialogue drafts assemble with the real macros (preproc, cpp, `arm-none-eabi-as`) when the placeholder names are stubbed; only genuine externals stay undefined. No battle or cutscene has been run.

| File | Goes into | Covers |
|---|---|---|
| `hollowbrook_scripts.inc` | `Hollowbrook`, `Hollowbrook_PlayersHouse_1F`, `Hollowbrook_GoldsworthHouse` | signs, NPCs, Pokemon, mom, grandfather timeline, locked door, Troglodyte's first battle outside the lab with SIR BISCUIT |
| `hollowbrook_lab_scripts.inc` | `Hollowbrook_ProfFennickLab` | the lab scene (random starter, four balls, choice, exit blocker), aides, Fennick |
| `route1_scripts.inc` | `VeldrisRoute1` | signs, three trainers, guide POTION gift, sighting NPC |
| `wendlebury_scripts.inc` | `Wendlebury`, `Wendlebury_PokemonCenter_1F`, `Wendlebury_Mart` | town NPCs, nurse (vanilla heal script), mart clerk with item list |

## Proposed new flags and vars (all PROPOSED names, none claimed)

Claim by renaming a spare in place (see `design/flags.md`), keep the value, log it there and in `engine-edits.md`. Suggested homes are from the spare pool plan in `flags.md`.

**Vars (1 new)**

| Name | Values | Suggested slot |
|---|---|---|
| `VAR_HOLLOWBROOK_STATE` | 0 new game, 1 mom woke player, 2 lab scene running (Troglodyte has his ball, player not chosen), 3 player chose a starter (Trog waits outside), 4 Trog beaten outside the lab | a spare var, e.g. `VAR_UNUSED_0x40F8` |

Already claimed and used: `VAR_TROG_STARTER` (0x40F7). Vanilla used: `VAR_STARTER_MON`, `VAR_TEMP_TRANSFERRED_SPECIES`, `VAR_0x8008`.

**Flags (14 new, plus 2 fly flags)**

| Name | Meaning | Suggested block |
|---|---|---|
| `FLAG_HIDE_HOLLOWBROOK_GRANDPA` | bench grandfather hidden (set/cleared by timeline) | story 0x8E5+ |
| `FLAG_HIDE_HOLLOWBROOK_TROG` | Troglodyte outside the lab hidden (derived from state on each map load) | story 0x8E5+ |
| `FLAG_HIDE_HOLLOWBROOK_LAB_TROG` | Troglodyte inside the lab hidden, set when he leaves | story 0x8E5+ |
| `FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1` to `_4` (4 flags) | the four Poke Ball objects hidden | story 0x8E5+ |
| `FLAG_HOLLOWBROOK_GRANDPA_TALKED1` | first bench talk done | per-map 0x493-0x4EF |
| `FLAG_HOLLOWBROOK_GRANDPA_TALKED2` | second topic done | per-map |
| `FLAG_HOLLOWBROOK_GRANDPA_NAME_TOLD` | post-game name reveal done | per-map |
| `FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD` | mom's 'you have a POKeMON' speech done | per-map |
| `FLAG_ROUTE1_GUIDE_POTIONS` | guide's 3 POTIONs given | per-map |
| `FLAG_HIDDEN_ITEM_ROUTE1_POTION`, `FLAG_HIDDEN_ITEM_ROUTE1_REPEL` | hidden items | hidden-item range 0x264-0x2BB (not 0x264 itself) |
| `FLAG_VISITED_HOLLOWBROOK`, `FLAG_VISITED_WENDLEBURY` | fly flags, already planned (0x020-0x031) | fly block |

Count: 3 hide flags (grandpa, Trog, lab Trog) + 4 balls + 4 one-shots (talked1, talked2, name told, mom) + 1 guide + 2 hidden items = 14 new, plus the 2 fly flags = 16.

Trainer defeated flags come from trainer ids. `TRAINER_TROGLODYTE_HOLLOWBROOK` and the three Route 1 trainers are placeholder constants that still need `trainers.party` blocks and `opponents.h` defines.

Vanilla flags set or read: `FLAG_BADGE01_GET`, `FLAG_SYS_GAME_CLEAR`, `FLAG_SYS_POKEMON_GET`, `FLAG_ADVENTURE_STARTED`.

## Open questions and things I was unsure about

1. **Fourth starter and `VAR_STARTER_MON`.** **FIXED 2026-09-30** (author approved): `sStarterMon` in `src/starter_choose.c` now has a fourth entry (`VELDRIS_FOURTH_STARTER`, stand-in PIKACHU) and the bounds check is `>= STARTER_MON_TABLE_SIZE`. Ball 4 can now store 3 in `VAR_STARTER_MON`. Logged in [engine-edits.md](../engine-edits.md).
2. **Species are stand-ins** (Treecko, Torchic, Mudkip), and the fourth is `SPECIES_TBD4` in the scripts; use `VELDRIS_FOURTH_STARTER` (stand-in PIKACHU) until the author picks.
3. **All coordinates and movements are placeholders** (`TODO(coords)`): door tiles, Troglodyte's walk to the balls and out, the warp into the Goldsworth house. They depend on the built maps.
4. **Initial hide flags** are derived in `OnTransition` from `VAR_HOLLOWBROOK_STATE` instead of editing `EventScript_ResetAllMapFlags`, so no engine edit is needed. Cost: a few extra lines per map load.
5. **Goldsworth door** is a bg_event on a door tile with no warp, and it warps with `warpdoor` only after `FLAG_SYS_GAME_CLEAR`. Untested.
6. **Lab trigger** needs two coord_events (state 0 and 1) so skipping mom does not skip the scene.
7. **Troglodyte battle music** is not chosen (`teams.md`: Music TBD), so there is no `playbgm`.
8. **Wendlebury nurse wording** (`CenterNurse`, `CenterNurseDone`) is unused: vanilla's shared heal script prints its own texts.
9. **No Pokedex handout** in the lab draft, so `FLAG_SYS_POKEDEX_GET` is not set anywhere.
10. Two new lab texts (`LabExitBlocked`, `LabBallGone`) are at the bottom of `hollowbrook_lab_scripts.inc`; they fit the text box.
11. The optional Route 1 sighting NPC falls back to the guide's tip text before the first fight (stand-in).
