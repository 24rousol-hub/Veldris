# Flags and vars

**Rules**

1. Every flag or var the hack uses is recorded in the table below, in the same commit that first uses it.
2. Take unused ones from the spare pool. **Never overwrite or repurpose one that is in use.**
3. Before claiming a spare, grep its name and its numeric value across `include/`, `src/`, `data/` and `test/`. Then check the table below.
4. Never hand-allocate a flag in the trainer block. Those come from the trainer ID.
5. Claiming a flag = renaming its `FLAG_UNUSED_0x...` line in place in `include/constants/flags.h`, keeping the value. Do the same for vars in `vars.h`. Log each rename in [engine-edits.md](engine-edits.md). (Porymap fills its flag and var dropdowns from those two headers. A separate header would not show up there.)

Measured on 2026-09-29 against this tree, Emerald build (`IS_FRLG` is 0); the spare-pool counts below were recounted on 2026-10-10. Values come from the preprocessor (`arm-none-eabi-gcc -E -dM`), not from reading numbers by hand.

## How the flag space is laid out

| Block | Range (hex) | Range (dec) | Safe for story state? |
|---|---|---|---|
| Temp flags | 0x000-0x01F | 0-31 | **No.** Cleared every time a map loads |
| Story, hide/show, item, event flags | 0x020-0x4FF | 32-1279 | Yes. Most spare flags live here |
| Trainer flags | 0x500-0x85F | 1280-2143 | **No.** One flag per trainer ID, set by the engine |
| System flags | 0x860-0x91F | 2144-2335 | Yes, where spare. Holds the badges (0x867-0x86E) and the `FLAG_VISITED_*` fly flags starting at 0x86F |
| Daily flags | 0x920-0x95F | 2336-2399 | **No.** Reset by the daily-flag clear |
| Special flags | 0x4000-0x407F | 16384-16511 | **No.** Computed at runtime, not saved |

Vars: persistent vars are 0x4000-0x40FF (256 in total). `VAR_TEMP_0` to `VAR_TEMP_F` (0x4000-0x400F) reset on map load. Special vars 0x8000-0x8015 are volatile script arguments and are never saved.

## In use by the hack

| Name | Value | Kind | Purpose | Set by | Cleared by | Added in |
|---|---|---|---|---|---|---|
| `FLAG_BADGE09_GET` | 0x88E | Story | 9th gym badge (was `FLAG_UNUSED_0x88E`). Listed in `include/veldris_badges.h` | The 9th gym leader's script (`setflag FLAG_BADGE09_GET`) | Debug menu only | 2026-09-29 |
| `FLAG_HIDE_HOLLOWBROOK_LAB_TROG` | 0x8E5 | Hide | Troglodyte inside Fennick's lab hidden | Lab scene, when he leaves | Never | 2026-10-01 |
| `FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1` to `_3` | 0x8E6-0x8E8 | Hide | Starter balls 1-3 on the lab table hidden (taken by Troglodyte or the player) | Lab scene / ball scripts | Never | 2026-10-01 |
| `FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4` | 0x8E9 | Hide | The fourth (revealed) starter ball hidden | Lab `OnTransition` while `VAR_HOLLOWBROOK_STATE` < 2; ball 4 script when taken | Lab scene (reveal) | 2026-10-01 |
| `FLAG_HIDE_HOLLOWBROOK_GRANDPA` | 0x8EA | Hide | Grandfather on the Hollowbrook bench hidden. Starts set (the bench is empty until the lab scene) | Town `OnTransition` (`UpdateGrandpa`) while `VAR_HOLLOWBROOK_STATE` < 3, and once `FLAG_BADGE01_GET` or `FLAG_SYS_GAME_CLEAR` is set (he is inside his house then); debug `ResetStory` | Lab scene, after the fourth-ball reveal; town `OnTransition` at state >= 3 with no badge; debug presets | 2026-10-01 |
| `FLAG_HIDE_HOLLOWBROOK_TROG` | 0x8EB | Hide | Troglodyte waiting outside the lab hidden | Town `OnTransition` unless `VAR_HOLLOWBROOK_STATE` is 3 | Town `OnTransition` when it is 3 | 2026-10-01 |
| `FLAG_HOLLOWBROOK_GRANDPA_TALKED1`, `_TALKED2` | 0x493, 0x494 | One-shot | First and second bench talks with the grandfather done | Grandfather's script | Never | 2026-10-01 |
| `FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD` | 0x495 | One-shot | Mom's 'you have a POKéMON now' speech done | Mom's script in the player's house 1F | Never | 2026-10-01 |
| `FLAG_VISITED_HOLLOWBROOK` | 0x020 | Fly | Hollowbrook is a fly destination | Town `OnTransition` | Never | 2026-10-01 |
| `FLAG_RECEIVED_TM_CRUNCH` (alias of vanilla `FLAG_RECEIVED_TM_ROCK_TOMB`) | 0x0A5 | Item | Greta gave TM CRUNCH | `Crestfall_Gym` | Never | 2026-10-08 |
| `FLAG_RECEIVED_HM_CUT` (vanilla, reused) | 0x089 | Item | Greta gave HM CUT | `Crestfall_Gym` | Never | 2026-10-08 |
| `FLAG_VISITED_CRESTFALL` | 0x021 | Fly | Crestfall is a fly destination | Town `OnTransition` | Never | 2026-10-08 |
| `FLAG_SYS_RUN_BY_DEFAULT` | 0x881 | System | Set = the player runs unless B is held (clear = vanilla, B runs). **Set at new game** (author, 2026-10-09). L toggles it once the Running Shoes (`FLAG_SYS_B_DASH`) are owned. See [running-shoes.md](running-shoes.md) | New game (`src/veldris_new_game.c`), Mom's shoes scene, L press in the overworld (`src/veldris_run.c`) | L press again, debug menu | 2026-10-08 |
| `FLAG_SYS_EXP_SHARE_ON` | 0x882 | System | Set = the Exp. Share key item is switched on (whole party gains Exp). Read by `IsGen6ExpShareEnabled` via `I_EXP_SHARE_FLAG`. **Set at new game** (author, 2026-10-09). See [exp-share.md](exp-share.md) | New game (`src/veldris_new_game.c`), using the Exp. Share item (`src/item_use.c`) | Using it again, debug menu | 2026-10-08 |
| `FLAG_SYS_CLOCK_SET` | vanilla (`SYSTEM_FLAGS`) | System | Vanilla flag, no claim needed: set = the fake clock has been started, which lets berries and daily events run (`DoTimeBasedEvents`). See [time-of-day.md](time-of-day.md) | New game (`src/veldris_new_game.c`), the wall-clock set screen, debug Cheat start | Debug menu | 2026-10-09 |
| `FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS` | 0x496 | One-shot | Route 1 guide's 3 POTIONs given | Guide's script | Never | 2026-10-01 |
| `FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_POTION`, `_REPEL` | 0x265, 0x266 | Hidden item | Route 1 hidden POTION (27,13) and REPEL (44,17) picked up | The hidden item event | Never | 2026-10-01 |
| `VAR_VELDRIS_LOOK` | 0x40FA | Var | Player customization, packed: bits 0-1 outfit (0 Emerald, 1 Ruby/Sapphire, 2 Diamond/Pearl), 2-4 skin, 5-7 hair (Brendan: clothes), 8-10 top, 11-13 accent. 0 = Emerald with the original colours | The Costume Box picker (`src/veldris_look.c`) | Debug presets (`Veldris_Debug_ResetStory`) | 2026-10-10 |
| `FLAG_VELDRIS_OUTFIT_RS`, `FLAG_VELDRIS_OUTFIT_DP` | 0x883, 0x885 | Story | Ruby/Sapphire and Diamond/Pearl outfits unlocked early. The outfits also unlock by badge count (3 and 6, PROPOSED), so nothing sets these yet; they are for a later scene or the debug menu | (none yet) | Debug presets | 2026-10-10 |
| `VAR_CRESTFALL_STATE` | 0x40F9 | Var | Scheme 1: 0 gym booked (scene waits at the gym door), 1 scene done (photographer by the noticeboard, normal gym sign) | Crestfall Scheme 1 scene | Never | 2026-10-08 |
| `FLAG_TEMP_11` (temp, Crestfall only) | 0x11 | Temp | Hides Hollis, Troglodyte and the outdoor Greta in Crestfall; set on every load, the scene spawns them with `addobject` | Crestfall `OnTransition` | Cleared on every map load | 2026-10-08 |
| `VAR_HOLLOWBROOK_STATE` | 0x40F8 | Var | 0 new game, 1 mom woke player, 2 Troglodyte has his ball (player choosing, lab exit blocked), 3 player chose, 4 Troglodyte beaten outside. **While it is 1 or 2 the player has no starter, so Hollowbrook's east exit is gated** (triggers at (30, 9..11), `Hollowbrook_EventScript_NoStarterGate`), and the lab's whole 4-tile doorway runs the Troglodyte scene (states 0 and 1) or the exit blocker (state 2). See [interiors.md](interiors.md) | Lab scene (2, 3); mom and the town scripts later (1, 4) | Never (debug menu resets it to 0) | 2026-10-01 |
| `VAR_TROG_STARTER` | 0x40F7 | Var | Troglodyte's random starter: 0, 1 or 2 for the 1st, 2nd or 3rd starter on show. Read by `VeldrisRivalStarterPrune` (`src/veldris_trainer_pools.c`, called from `src/trainer_pools.c`) to drop the two starter versions that do not match; the starter versions are also tagged `Lead` (2026-10-09), so his starter comes out first and SIR BISCUIT second | Lab scene (`random 3`) | Never (debug menu resets it to 0) | 2026-09-30 |
| `VAR_TEMP_1` (temp, `Crestfall_Gym` only) | 0x4001 | Temp var | 1 only on the visit Greta was beaten, to pick her idle line. Same slot as vanilla `VAR_TEMP_TRANSFERRED_SPECIES`, which the Hollowbrook lab uses: no clash, because both are per-map and reset on every map load | `Crestfall_Gym_EventScript_GretaDefeated` | Cleared on every map load | 2026-10-08 |
| `FLAG_SYS_POKEMON_GET`, `FLAG_ADVENTURE_STARTED` (vanilla) | vanilla (`SYSTEM_FLAGS`) | System | Vanilla flags, no claim needed: the player has a first Pokémon / the adventure has begun | Lab `ChoiceDone` | Debug `ResetStory` | 2026-10-01 |
| `VAR_STARTER_MON` (vanilla) | vanilla | Var | Which ball the player took: 0, 1 or 2 = the three on show, 3 = the fourth starter (`VELDRIS_FOURTH_STARTER`, [engine-edits.md](engine-edits.md)). Read by Mom, the neighbour and the Troglodyte text | Lab ball scripts | Debug `ResetStory` | 2026-10-01 |
| `FLAG_SYS_B_DASH` (vanilla) | vanilla (`SYSTEM_FLAGS`) | System | Running Shoes owned. See [running-shoes.md](running-shoes.md) | Mom's shoes scene in the player's house 1F | Debug menu | 2026-10-08 |

## Spare pool: permanent flags

355 flags are named `FLAG_UNUSED_*` (354 numbered plus `FLAG_UNUSED_RS_LEGENDARY_BATTLE_DONE`; 373 originally, the rest were claimed since). **299 are safe to claim** (recounted 2026-10-10). **Recount:** `grep -cE '^#define FLAG_UNUSED_' include/constants/flags.h`, minus the 56 excluded below. Excluded, with reasons:

- 52 sit in the daily range (0x920-0x95F). They reset every day. One of them, `FLAG_UNUSED_0x95F`, is also used by name: it defines `DAILY_FLAGS_END` in `flags.h`.
- `FLAG_UNUSED_0x91F`, just below the daily range, is used by name: it defines `DAILY_FLAGS_START`.
- `FLAG_UNUSED_RS_LEGENDARY_BATTLE_DONE` (0x71) is used by `data/maps/CaveOfOrigin_UnusedRubySapphireMap1/scripts.inc`.
- That is 54 excluded. The 2 reserved below bring the total to 56, and 355 - 56 = 299.
- `FLAG_UNUSED_0x1AA` and `FLAG_UNUSED_0x1AB` are **reserved as rematch headroom.** Trainer-registered flags run from 0x15C for `REMATCH_TABLE_ENTRIES` (78) entries, so 0x15C-0x1A9 are taken and the next two are the first to go if rematches are added. Beyond those two, the next flag (0x1AC) is `FLAG_DEFEATED_DEOXYS`.

The flags in `include/constants/flags_frlg.h` with the same names are the FRLG variant. They are not compiled into the Emerald build, so they do not count as uses.

Claimable ranges (each flag is named `FLAG_UNUSED_0x` plus its 3-digit hex value):

| Range | Count | Proposed block (PROPOSED) |
|---|---|---|
| 0x022-0x04F | 46 | **Fly visited flags** for Veldris towns (18 needed: 0x020-0x031; 0x020 and 0x021 are taken by Hollowbrook and Crestfall). The rest general purpose, first-fit |
| 0x054-0x055 | 2 | General purpose |
| 0x068 | 1 | General purpose |
| 0x0E9 | 1 | General purpose |
| 0x1DA | 1 | General purpose |
| 0x1DE-0x1E3 | 6 | General purpose |
| **0x264, 0x267-0x2BB** | 86 | **Hidden items (reserved; 0x265-0x266 are Route 1's).** Hidden-item flags must be 0x1F4 or higher (the assembler macro in `asm/macros/map.inc` rejects lower ones) and 0x264 is where the existing hidden-item range grows. Config comments in `include/config/battle.h` and `pokemon.h` use 0x264 as their example toggle flag, so skip 0x264 or use it for a config switch |
| 0x2D9 | 1 | General purpose |
| 0x468, 0x470, 0x472, 0x479 | 1 each | General purpose |
| **0x497-0x4EF** | 89 | **Per-map one-shots** (talked-to flags, single pickups) for towns and routes. Goldsworth houses are NPC-only and need none unless an NPC in one has a once-only line (at most one per house, and there are only about 7 houses) |
| 0x4F9-0x4FA, 0x4FF | 2 + 1 | General purpose |
| 0x863 | 1 | General purpose |
| 0x883-0x887 | 5 | General purpose (0x881 is now `FLAG_SYS_RUN_BY_DEFAULT`, 0x882 `FLAG_SYS_EXP_SHARE_ON`) |
| 0x88F | 1 | General purpose (0x88E is now `FLAG_BADGE09_GET`) |
| 0x8E3 | 1 | General purpose |
| **0x8EC-0x91E** | 51 | **Story beats and cutscenes:** gyms, Elite Four, post-game. Spill into the general flags if needed |

Reminder: the spare flags for ordinary game state are numerous but they are not unlimited. 299 flags for 18 towns, 33 routes, 9 gyms, the League and the post-game is enough only if boolean state is packed sensibly. Use `VAR_TEMP_*` for anything local to one map visit.

## Spare pool: permanent vars

20 vars are named `VAR_UNUSED_*` (after the claims below). **19 are safe to claim.** Excluded: `VAR_UNUSED_0x8014`, which is a volatile special var (0x8000 block, never saved). Also note `VAR_UNUSED_0x404E`: the config comment in `include/config/battle.h` names it as an example toggle. Claim it for a config switch, or skip it.

Claimable vars (19): 0x404E, 0x4083, 0x408B, 0x4091, 0x409B, 0x409D, 0x40A1, 0x40A8, 0x40B8, 0x40BB, 0x40DB, 0x40DC, 0x40E5, and 0x40FA to 0x40FF (6 in a row). Two of them, **0x4083 and 0x408B, are also used as FRLG map-script variables** (through `vars_frlg.h` aliases). FRLG maps are not built into this Emerald ROM, so they are safe here, but skip them if FRLG maps are ever enabled. That leaves 17 with no alias at all.

**Claimed 2026-10-08:** `VAR_CRESTFALL_STATE` (0x40F9, was `VAR_UNUSED_0x40F9`), see the table above.

**Claimed 2026-09-30:** `VAR_TROG_STARTER` (0x40F7, was `VAR_UNUSED_0x40F7`): Troglodyte's random starter, 0, 1 or 2 for the 1st, 2nd or 3rd starter on show. Set once by the lab scene (`random 3`) and read by the pool prune in `src/trainer_pools.c`.

**Planned, not claimed yet (villain teams, [factions.md](factions.md)):** a Route 3 block flag or story var (Commons grunts gone after the Wendlebury beat), a hide flag for the Commons leader in Wendlebury, a story var for the factions' progress, and one saved var for Kyogre's daily hour in Aldermere. **Also planned:** a flag for Troglodyte's attitude, contemptuous or oblivious, once the story points that change it are decided (from the story-beat block above). Route 1's guide flag (0x496) and two hidden-item flags (0x265, 0x266) were claimed 2026-10-01 (rows above). **Already claimed:** `VAR_TROG_STARTER` (0, 1 or 2), set by the lab scene and read by every Troglodyte battle (see its row above). **Claimed 2026-10-01 for the lab scene:** `VAR_HOLLOWBROOK_STATE` (0x40F8) and five hide flags 0x8E5-0x8E9 (table above). **Claimed 2026-10-01 for the town:** the grandfather and Troglodyte hide flags (0x8EA, 0x8EB; the grandfather's is driven by the lab scene, `FLAG_BADGE01_GET` and `FLAG_SYS_GAME_CLEAR`), three per-map one-shots (0x493-0x495) and `FLAG_VISITED_HOLLOWBROOK` (0x020). Claim the rest and add rows here when the scripts are written.

**The Journal ([journal.md](journal.md)) claims no flag or var.** It reads the badge flags, the TROGLODYTE trainer flags (0x708, 0x709), `FLAG_SYS_GAME_CLEAR` and `VAR_HOLLOWBROOK_STATE`, and uses the volatile `VAR_0x8004`/`VAR_0x8005` as hand-off.

**Only 19 spare persistent vars.** Use a var only for a state that has more than two values (a story chapter counter, a puzzle stage). Use a flag for anything yes/no. If we run short, the remaining Hoenn vars can be freed by removing the Hoenn maps that use them, but that is a decision for the author.

## Range and comment traps

- **Hidden items** are reached as `FLAG_HIDDEN_ITEMS_START` (0x1F4) plus an id, and the assembler macro rejects any hidden-item flag below 0x1F4. So the spare flags below 0x1F4 can never be hidden-item flags, and hidden items in Veldris need flags from 0x1F4 up.
- **Rematches.** Trainer-registered flags run 0x15C-0x1A9 (78 entries). Adding rematch entries walks into 0x1AA-0x1AB and then `FLAG_DEFEATED_DEOXYS` (0x1AC), so only 2 more fit.
- **Zero-valued names.** `include/constants/flags.h` also defines FRLG-only names as `0`: 190 `FLAG_HIDDEN_ITEM_*`, 297 `FLAG_HIDE_*`, 14 `FLAG_DEFEATED_*` and 2 `FLAG_VISITED_*` (counted 2026-10-10 with the preprocessor). In this Emerald build they do nothing (`FlagSet(0)` is a no-op, `FlagGet(0)` is FALSE), and only the hidden-item macro rejects 0 at build time, so check a name's value before reusing it.
- **Do not trust an `Unused Flag` comment.** `FLAG_TEMP_5` and `FLAG_TEMP_6` say so but are referenced (dozens of times). Only the name `FLAG_UNUSED_*` plus a zero-reference grep counts.
- **Not counted:** about 10 more flags are documented as leftovers but are not named `FLAG_UNUSED_*` (for example `FLAG_RECEIVED_CONTEST_PASS`). They can be reclaimed later if the pool runs short.
- **Flag ids of 0x960 and above** are outside the save block. The save block has no bounds check for them, and the flags array is followed directly by the vars.

## Related limits worth knowing

- **Trainer slots.** `TRAINERS_COUNT` is 855 and `MAX_TRAINERS_COUNT` is 864, so only **9 new trainer IDs** fit before trainer flag space overflows (upstream's own note in `include/constants/opponents.h`). New trainers must reuse IDs of vanilla trainers you no longer need (rename them), or `MAX_TRAINERS_COUNT` is raised. That costs save block space, but there are 304 bytes of headroom (about 2,400 flags, measured 2026-10-09 and 2026-10-10), so a few hundred more trainers fit. It shifts every system and daily flag, which is fine on a fresh start. See [engine-limits.md](engine-limits.md). None of the 21 built Veldris trainers uses a new id (Greta is 770, a reused one). See open decision 6 in [game-bible.md](game-bible.md).
- **Badges.** Flags 0x867-0x86E are badges 1-8, and 0x86F is already a `FLAG_VISITED_*`, so badge 9 is `FLAG_BADGE09_GET` at 0x88E. See [badges.md](badges.md).
- **Fly flags.** `FLAG_VISITED_*` are Hoenn-named and sit in the system block. The A-prime hooks are applied and `src/data/veldris_fly_towns.h` has two rows (Hollowbrook, Crestfall). Claim `FLAG_UNUSED_0x022` to `0x031` as `FLAG_VISITED_<TOWN>` one town at a time (renaming the one line in `include/constants/flags.h`), with the checklist in [region-map.md](region-map.md). `0x020` is `FLAG_VISITED_HOLLOWBROOK` (2026-10-01) and `0x021` is `FLAG_VISITED_CRESTFALL` (2026-10-08).
