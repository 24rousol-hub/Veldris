# Decision briefs: text, relearning, night lights, comforts, defaults (UI and progression)

Status: **PROPOSED.** Nothing here is built in the repo. Everything marked 'ran' was run in a scratch copy of the tree (HEAD `8bb23927` plus the prototype patches in `prototypes/`) in mGBA. Pictures are in this folder.

**How to answer:** the question code and a letter, for example `U1 B`. Bold marks what I would pick.

## Quick answers

| # | Question | Options | Today / my pick |
|---|---|---|---|
| U1 | **Hold a button to skip text?** | A no, only set the default text speed to FAST / **B hold R** (pages turn by themselves, battle pauses shrink) / C hold B instead | Today: no skip, text MID. **Pick B** (cheap, ran fine) |
| U2 | **Story-unlockable move relearner?** | A leave it (level-up moves only, free, anywhere) / B **two more tabs (Egg, Tutor) switched on by story flags** / C Heart Scale tutor NPCs, pay per move / D everything on now. Then **F** (ordinary filler NPC gives the unlock, I can build it without asking) or **S** (a story person gives it, you decide who) | Today A. **Pick B F** |
| U3 | **Night lights?** | A none (night tint only, today) / B **glowing Pokémon Center and Mart signs and lamp orbs** / C B plus lit house windows | Today A. **Pick B**, windows later |
| U4 | **12 small comforts** (list below) | A my picks (items 1 to 6) / B none / C your own list of numbers | Today none. **Pick A** |
| U5 | **Defaults for a new game** | A TEXT SPEED FAST, SOUND STEREO, BATTLE STYLE SET / B same but SHIFT / C keep today's (MID, MONO, SHIFT) | Today C. **Pick A** |

One thing to know for U5 and U4: a new game keeps the options of an old save. The defaults only apply to a **fresh save file** (see U5).

---

## U1. Hold to skip text

**What the game does today**
- TEXT SPEED in OPTION has three steps. From the code (`src/text.c`), one letter appears every 8 frames (SLOW), 4 (MID, the default) or 1 (FAST). At 60 frames a second that is 7.5, 15 and 60 letters per second, so **a full two-line box (about 64 letters) takes 8.5 s on SLOW, 4.3 s on MID and 1.1 s on FAST.**
- Holding A or B speeds typing up, but only on SLOW and MID. On FAST it changes nothing (already one letter per frame).
- Every page still needs its own fresh press (the little red arrow). Holding does not turn pages.
- Battle text uses the same speed. Its pauses are already about 40% shorter than vanilla (`B_WAIT_TIME_MULTIPLIER` 10 instead of 16).
- Config offers only blunt tools: `TEXT_SPEED_INSTANT` (forces instant for everyone, removes the option) and `AUTO_SCROLL_TEXT` (every page turns itself after 0.8 s, for everyone, which would eat the jokes). I do not recommend either.

**So the default speed matters more than skipping.** On MID, a joke box takes 4.3 s to type before you can press anything. FAST makes typing effectively instant. Set it (U5) and most of the problem is gone.

**What a hold-to-skip adds on top of FAST:** pages turn by themselves and battle pauses shrink, so a long scene costs one held button instead of 20 presses. It matters most when you replay a scene (after a white-out, while testing on the phone).

**Prototype (ran in mGBA):** hold **R**.
- A 4-page notebook message passed in about 1 s with no presses, and the box closed itself ([hold_r_skip_filmstrip.png](img/hold_r_skip_filmstrip.png)).
- A trainer battle went from 'You are challenged by...' to the 'What will Buffie do?' menu in about 3 s with R held. The send-out animation still plays. No hang.
- A page stays up at least 8 frames (0.13 s) so it is still seen. YES/NO questions, naming screens and menus still wait for you. Walking cutscenes, fades, fanfares and move animations are **not** skipped (use BATTLE SCENE: OFF for moves).
- Cost: one new small file (`src/veldris_skip.c`, 30 lines) and about 10 changed lines in three engine files (`text.c`, `scrcmd.c`, `battle_script_commands.c`). No save change. No measurable ROM change.
- Why R: it is free in the overworld (only the unused DexNav uses it) and under the index finger on a handheld and in Delta. Hold B is already 'walk' (run-by-default) and 'cancel'.
- Risk: low. R is also 'throw last ball' in the battle menu (a fresh press only) and half of the debug chord R+START (dev ROM only; `make release` removes it). Not run on Delta (VBA-M) or Miyoo, only mGBA.

**Answer:** `U1 A` (no skip) / `U1 B` (hold R, **my pick**) / `U1 C` (hold B).
Patch: `prototypes/u1_hold_r_skip.patch` (applies to HEAD).

---

## U2. Story-unlockable move relearner

**What the game does today.** Three different things share the name.

1. **Summary screen (Moves page, the 'relearn' prompt).** Level-up moves only. Since 2026-10-08 it offers every level-up move of the Pokémon and its earlier forms, at any level, free, anywhere (`P_ENABLE_ALL_LEVEL_UP_MOVES`, `P_PRE_EVO_MOVES`), and refills the move's PP. The Egg, Tutor and TM lists exist in the code but are **switched off**:
   - Egg: needs `P_FLAG_EGG_MOVES` (now `0`, and flag 0 can never be set) or `P_ENABLE_MOVE_RELEARNERS`.
   - Tutor: needs `P_FLAG_TUTOR_MOVES` (now `0`) or `P_ENABLE_MOVE_RELEARNERS`.
   - TM: only `P_TM_MOVES_RELEARNER` (no flag, so it cannot be story-gated; with reusable TMs it would only list TMs you already own, so it is pointless).
   - So **the two flags are the only story switches that exist**: one for Egg, one for Tutor.
2. **The talking NPC script `Common_EventScript_MoveRelearner`** (`data/scripts/move_relearner.inc`): a menu Level Up / Egg / TM / Tutor / See ya, free. No map uses it; only the debug menu does (Party > Move Relearner). **It ignores the flags**: from the code, the script path skips the 'is this list switched on' check (`src/move_relearner.c:789`), so any NPC that calls it hands out Egg, TM and Tutor moves for free. I saw its menu with all four entries in the emulator but did not open the lists. Do not use it for a gated NPC.
3. **The Fallarbor-style Heart Scale tutor** (`FallarborTown_MoveRelearnersHouse`, a Hoenn map): level-up moves only, one Heart Scale per move. It is the template for a paid NPC.

What the lists contain: Egg moves come from the base form of the family. The Tutor list is the 30 Emerald tutor moves (Body Slam, Counter, Double-Edge, Dream Eater, Explosion, Fire/Ice/Thunder Punch, Mimic, Rock Slide, Seismic Toss, Sleep Talk, Substitute, Swagger, Swords Dance, Thunder Wave and others).

**Notes from your own cards.** Kingsquay (town 16 of 18) has a 'Move Reminder's House' that relearns moves for Heart Scales, with 'build it last' and your open question 4. Since level-up relearning is now free, that card as written does nothing; it only makes sense as the Tutor or Egg giver. Lingmoor (place 10) has a Day Care (open question: wanted?). Heart Scales are already planned as hidden items.

**Options**
- **A. Leave it.** Level-up only. Egg and Tutor moves never reach the player. Cost 0.
- **B. Two tabs unlocked by the story.** Egg tab and Tutor tab each switch on when a flag is set. After that they sit in the same relearner, free. Cost: 2 config lines, 2 flags, one short script per giver. About 45 minutes in total.
- **C. Heart Scale tutor NPCs** (per move, like Fallarbor). No config, no flags; the NPC's town is the gate. Cost: one 60-line script per NPC and a Heart Scale supply to plan. Does not use the flags at all.
- **D. Everything on now** (`P_ENABLE_MOVE_RELEARNERS` TRUE, one line). No progression: Egg moves on any Pokémon from minute one.

**Concrete design for B (PROPOSED)**
- Flags (spare, system range, both unused today): `FLAG_RELEARN_EGG` (0x883) and `FLAG_RELEARN_TUTOR` (0x884). Config in `include/config/summary_screen.h`: `P_FLAG_EGG_MOVES FLAG_RELEARN_EGG`, `P_FLAG_TUTOR_MOVES FLAG_RELEARN_TUTOR`. I compiled this; the two flags and the debug reset line must be added to `flags.md` and `Veldris_Debug_ResetStory` in the same commit.
- Scene for Egg: the **Lingmoor Day Care keeper** (an ordinary filler NPC) says the Pokémon 'remembers its family' and sets the flag on first talk. Mid-game (place 10 of 18).
- Scene for Tutor: a **market-stall man in Wendlebury** (town 3, an ordinary filler NPC), early and cheap. Or Kingsquay's Move Reminder, late. One-time fee optional (for example 5 Heart Scales) if you want a cost.
- How the player sees it: Moves page, the relearn prompt, SELECT switches lists once more than one is on.
- Draft giver lines (checked for width, not wired): `relearn_giver_lines_DRAFT.inc`.
- A **story giver** (Prof. Fennick's notebook, Greta, Gatsby) is the same scripts with different speakers, but it touches your key story beats, so I would only draft and ask first.

**Effort and risk for B:** about 45 min; low (upstream config switches, no save change). The summary-screen lists were **not opened in the emulator** with the flags on; the config compiles and the code path is read, not run. Test: set the flag from the debug menu, open a Pokémon with egg moves, Moves page.

**Answer:** `U2 B F` (**my pick**), or `U2 A`, `U2 C`, `U2 D`; add `S` for a story giver. If B, also tell me the two towns (or say 'your choice').

---

## U3. Night lights

**What the game does today.** `OW_ENABLE_DNS` is on. At night (20:00 to 06:00 of the fake clock, **about 30 of every 72 real minutes**, so you will often see it) every **outdoor** map (town, city, route, sea route) is darkened to about 46% and tinted blue. **Interiors are never tinted**: a room looks the same at noon and midnight. Nothing glows.

The engine has three lighting tools, none used anywhere yet:
1. **Light Sprites**: a glow drawn on top of the map at night only, placed as an object event (in Porymap: graphics `OBJ_EVENT_GFX_LIGHT_SPRITE`, 'Sight radius / berry tree id' 0, 1 or 2). Type 0 is a round warm orb (a lamp or candle), type 1 a Pokémon Center sign glow, type 2 a Mart sign glow. They ignore the darkening, so they look lit.
2. **Lit window colours** (`.pla` file next to a tileset palette): some palette colours blend to warm yellow at night instead of darkening.
3. **Night palettes** (`swapPalettes`): a whole alternate palette per tileset slot. Heavier, same discipline as 2.

**What I ran (Crestfall at night, [night_lights_crestfall.png](img/night_lights_crestfall.png)).**
- Light Sprites work in this build. A type 0 orb and a type 1 sign glow appear at night and are invisible by day.
- **The roof emblem does not glow**: a sprite placed there is drawn behind the roof. The glow belongs on the **front sign**. The type 1 glow sits about half a tile left of the tile you give it, so the Center's 'P.C' sign (tiles 10 to 11, row 14) should want it at **(11,14)**. I tried (10,14) and the glow landed between the door and the sign; (11,14) is my inference from that offset and **was not re-run**. The Mart sign should be (33,14) by the same logic; **not seen**. Each building needs one look in Porymap (plus or minus one tile).
- The orb floats over bare grass today because the tileset has no lamp post. For lamps you need a lamp tile first.
- Each glow uses one of the map's 64 object slots.

**Windows ([night_windows_mock_*.png](img/); a mock-up, not the engine).** Hollowbrook's house windows use one palette colour that no other tile in either town uses, so one line in a `.pla` file would light every house window there. Crestfall's red-roof houses, Center and Mart use other palettes and each needs checking. Honest look: the engine blends the pane **halfway** to a warm yellow, so a blue pane goes pale grey-yellow, not a strong yellow. For a real glow you would repaint the pane in a paler colour or change the palette's colour 0. And the rule is silent: if you later repaint window tiles so the glass shares a colour with something else, it looks right by day and wrong at night.

**What you would do in Porymap/tileset:** for B nothing (I add the object events; close or reload Porymap first so it does not overwrite them; you check the position in the preview). For C you keep window glass on its own palette colour and I add the `.pla` file after you say yes (palette files are tileset files, your area).

**Options and my pick**
- A. None.
- **B. Signs and lamps.** About 10 minutes per town for the Center and Mart (more where a lamp tile exists). Safe, no engine edit, no tileset edit. **Pick.**
- C. B plus windows. Wait until the exterior art is final: it ties the glow to palette colours, which change every time you repaint.

**Answer:** `U3 A` / `U3 B` (**my pick**) / `U3 C`.
Prototype (not for merging as is): `prototypes/u3_crestfall_light_sprites.patch` (my 5 test positions; the keepers would be a Center glow at (11,14), inferred, and a Mart glow near (33,14), unseen).

---

## U4. Twelve small comforts

'Today' is the value in this tree. 'Ran' means seen in mGBA in the prototype ROM. **Items 1 to 6 are my picks.**

| # | Comfort | Today | Proposed | What the player feels | Cost and risk | Checked |
|---|---|---|---|---|---|---|
| 1 | **National Pokédex from minute one** | Pokédex lists the 202 Hoenn species; National switches on only through a Hoenn story script (and the debug menu), and no Veldris map calls it | Call `EnableNationalPokedex()` at new game (`VeldrisNewGameDefaults`, hack-owned file) | Species from every generation get an entry and a number, not only Hoenn's. Without it, Dialga, Giratina, Shaymin and any non-Hoenn Pokémon would not appear in the list at all | 1 line, no save change | code read; note: no map hands out the Pokédex yet |
| 2 | **Door popups only once** | `OW_HIDE_REPEAT_MAP_POPUP` FALSE: the area name pops up every time you step out of a house | TRUE | The name appears when you enter a new town or route, not at every door | 1 config line | code read (`src/overworld.c:915`); houses share the town's area id, so it works |
| 3 | **Pop-up shows the time** | `OW_POPUP_GENERATION` GEN_3, no time | GEN_5 and `OW_POPUP_BW_TIME_MODE` 12_HR | A black banner top and bottom: area name top left, clock bottom right ('08:40 PM'). The only place the player can read the fake clock away from home | 2 config lines; changes the look of every entry | **ran** ([popup_gen5_time_night.png](img/popup_gen5_time_night.png)) |
| 4 | **B jumps to RUN in wild battles** | `B_QUICK_MOVE_CURSOR_TO_RUN` FALSE | TRUE | Fleeing a wild Pokémon is B then A | 1 config line | compiled |
| 5 | **No nickname question after a catch** | Asked after every catch | Delete 4 lines of `data/battle_scripts_2.s` (no config switch). Renaming stays on the summary screen (`P_SUMMARY_SCREEN_RENAME` TRUE) | Catching ends two screens sooner | 4 lines, upstream asm file | compiled, **catch not run** |
| 6 | **Shinies somewhat commoner** | `SHINY_ODDS` 8 = 1 in 8192 | 16 = 1 in 4096 (one number in `include/constants/pokemon.h`, an engine file) | Over 500 encounters the chance of seeing a shiny goes from 6% to 12% (2048: 22%, 1024: 39%) | 1 line; taste | arithmetic |
| 7 | **Follower Pokémon** | `OW_FOLLOWERS_ENABLED` FALSE | TRUE | Your first healthy Pokémon walks behind you ([followers_crestfall.png](img/followers_crestfall.png), Swampert) | 1 line plus a flag to hide it in scenes and a test of every built scene (lab, Crestfall Scheme 1, walk-ups, doors, Surf). Cost in ROM: none measured. Save layout unchanged. Slow cores unknown | **ran** (open-air walking only). My pick: later, once the scenes are final |
| 8 | **HGSS-style Pokédex** | `POKEDEX_PLUS_HGSS` FALSE | TRUE | Stats bars, evolution tab, moves, area map, search, cry and size tabs (`hgss_pokedex_*.png`) | 1 line, +49 KB (25.57 to 25.62 MiB); my time-of-day area fix still shows 'DAY' on the Area tab | **ran** (booted, list, Info, Area). Pick: yes if you like the look |
| 9 | **Skip the 'already a save file' question** | `SKIP_SAVE_CONFIRMATION` FALSE | stay FALSE | Would save one press per save, but it also removes the warning when a new game overwrites an old save | do not | code read. **Do not change** |
| 10 | **DexNav** | `DEXNAV_ENABLED` FALSE | stay FALSE for now | Search for a species, chains, hidden abilities | needs 2 vars and 3 flags of the 19 spare vars, many new screens | no |
| 11 | **Low-HP beep** | `B_NUM_LOW_HEALTH_BEEPS` 4 beeps then silence | `NUM_BEEPS_OFF` | No beep at all | 1 config line; taste | no |
| 12 | **IV and EV letters in the summary** | `P_SUMMARY_SCREEN_IV_EV_INFO` FALSE | TRUE | A stats-judge style grade (F to S) per stat | 1 config line; taste | no |

Already on, nothing to decide: running indoors (`OW_RUNNING_INDOORS`), run by default, Exp. Share on, faster battle pauses and intro, reusable TMs, repel menu when a Repel runs out (`I_REPEL_LURE_MENU`), type-effectiveness hint (`B_SHOW_EFFECTIVENESS` SEEN), catch swap into the party, move descriptions, last-used ball (R).
Not switches in this tree: auto-save (none exists), bike music (hard-coded; the bike is not in your plan), encounter rate (set per route in `wild_encounters.json`, there is no global setting), catching tutorial (nothing to switch).

**Answer:** `U4 A` (**my picks**: 1 to 6) / `U4 B` / `U4 C 1,2,8` (your list). Say `7` when you want the follower pass.

---

## U5. Defaults for a new game

**Today** (`SetDefaultOptions`, `src/new_game.c:102`): TEXT SPEED MID, BATTLE SCENE ON, BATTLE STYLE SHIFT, SOUND MONO, BUTTON MODE NORMAL (never set, left at 0), FRAME TYPE 1.

**Proposed set A** ([defaults_option_screen.png](img/defaults_option_screen.png), ran): TEXT SPEED **FAST**, BATTLE SCENE ON, BATTLE STYLE **SET**, SOUND **STEREO**, BUTTON MODE NORMAL, FRAME TYPE 1.

| Option | Today | Proposed | Why |
|---|---|---|---|
| Text speed | MID (4.3 s per full box) | **FAST** (1.1 s) | The game is dialogue-heavy; MID makes you wait for every joke to type. Players who want slower can pick it |
| Battle style | SHIFT | **SET** (or keep SHIFT: set B) | SHIFT asks 'Will you switch?' after every knock-out; SET does not (you can still switch on your own turn). SET is faster and slightly harder, which fits the faster battles. Revisit with the difficulty decision |
| Sound | MONO | **STEREO** | MONO is the GBA's one speaker. Phone and Miyoo with headphones are stereo; no downside |
| Battle scene | ON | ON | Move animations stay; the option is there. Delta can fast-forward anyway |
| Button mode | NORMAL | NORMAL | L is the run toggle and only works in NORMAL and LR; `L=A` turns it off |
| Frame | TYPE 1 | TYPE 1 | Cosmetic |

**Important:** options are set only when the save file is empty (`intro.c:1148`, `reload_save.c:30`). Choosing NEW GAME over an existing save **keeps the old save's options**, and the Birch/Fennick speech types at whatever was saved. So the new defaults reach a fresh phone install but not your current test saves. If you want NEW GAME to always reset the options, say so (3 more lines, before the speech starts).

**Effort and risk:** 3 changed lines in `src/new_game.c` (log in `engine-edits.md`). No save layout change. Low.

**Answer:** `U5 A` (**my pick**) / `U5 B` (same but SHIFT) / `U5 C` (keep today's). Add `RESET` if NEW GAME should always reset the options.

---

## When you answer: what I do next

| Answer | Work | Where |
|---|---|---|
| U1 B | Apply the patch, log 3 rows in `engine-edits.md`, `make`, 2 minutes of mGBA, one commit | `src/veldris_skip.c`, `text.c`, `scrcmd.c`, `battle_script_commands.c` |
| U2 B F | Claim 0x883 and 0x884 (rename, `flags.md`, debug reset, `engine-limits.md`), 2 config lines, two giver scripts when the two towns are built | `include/config/summary_screen.h` |
| U3 B | Add Light Sprite objects to each town's Center and Mart (and lamps where a lamp tile exists); you check the glow position in Porymap | each `map.json` |
| U4 A | National Pokédex line, 3 config lines, nickname lines, shiny constant, logs | `veldris_new_game.c`, `overworld.h`, `battle.h`, `battle_scripts_2.s`, `constants/pokemon.h` |
| U5 A | 3 lines in `SetDefaultOptions`, log | `src/new_game.c` |

---

# Appendix for the lead (not for the author)

## Files in this folder

| File | What | Integrate |
|---|---|---|
| `briefs.md` | this document | Fold the quick-answers table and U1 to U5 into the author's breakdown doc (same `A/B` answer style as `lead_decisions.md`; my ids are U1 to U5) |
| `prototypes/u1_hold_r_skip.patch` | hold-R skip, applies to `8bb23927` | Only if U1 B: `git apply`, add 3 rows to `design/engine-edits.md`, make, retest |
| `prototypes/u2_u4_u5_config_and_defaults.patch` | experiment bundle: followers ON, GEN_5 popup with time, hide repeat popup, B to RUN, `P_FLAG_EGG/TUTOR_MOVES` pointed at the **unclaimed** `FLAG_UNUSED_0x883/0x884`, FAST/STEREO/SET defaults, nickname lines removed | **Do not apply whole.** Cherry-pick per the author's answers. Followers and the popup change are test settings |
| `prototypes/u3_crestfall_light_sprites.patch` | 5 Light Sprite objects in Crestfall, test positions: (9,12) type 1 on the roof emblem (**does not show**), (10,14) type 1 on the P.C sign (**shows**, half a tile left of the sign), (6,15) type 0 orb (**shows**), (31,12) and (31,14) type 2 at the Mart (**not looked at**) | Do not apply. If U3 B: add the Center glow at (11,14) and the Mart glow near (33,14), nothing else, close Porymap first |
| `relearn_giver_lines_DRAFT.inc` | 2 DRAFT giver texts, pass `dialogue_check.py` | Only if U2 B F; PROPOSED wording, not wired |
| `img/*.png` | evidence screenshots (mGBA) and the window mock-ups | Already copied to `img/` in this folder |
| `tools/nightmock.py`, `tools/emu143.sh` | the window mock-up script (reads the tileset and the Hollowbrook and Crestfall layouts) and the headless-mGBA helper I used (own display :143, kills only its own pids) | Optional; ignore if not wanted |

## Evidence index (file:line in this tree)

- Text: `src/text.c:293` frame delays 8/4/1/1; `:492` the stored delay is one less (`--textSpeed`), so FAST is zero delay; `:1338-1341` A/B held only after a first press and only while delaying; `:1253` button wait (`SetResultWithButtonPress`); `:324` `GetPlayerTextSpeed`; `include/config/text.h`; `src/field_message_box.c` and `src/menu.c:193-197` give field messages the A/B speed-up.
- Defaults: `src/new_game.c:102`; callers gated on an empty save at `src/intro.c:1148`, `src/reload_save.c:30`. `buttonMode` is never set (zero save).
- Relearner: `include/config/summary_screen.h:33-52`; `src/move_relearner.c:789` (script mode bypasses `isActive`), `:1024-1031`, `:1127-1141` (flag checks); `src/chooseboxmon.c:71-78` (script picker ignores `isActive`); `data/scripts/move_relearner.inc` (menu pushes all four entries unconditionally); `src/debug.c:641` is the only caller; `src/data/tutor_moves.h` (30 moves).
- Night: `src/overworld.c:1686-1693` tint table, `:1778` `MapHasNaturalLight`; `src/event_object_movement.c:2741-2843` light sprites (visible only at `TIME_NIGHT`); `src/data/field_effects/field_effect_objects.h:43-75`; `include/constants/event_objects.h:485`; `src/palette.c:897-1040` `TimeMixPalettes` (marked colours blend 50% toward (248,224,120) once `coeff` is 16); `docs/tutorials/dns.md` (`.pla` and `swapPalettes`); no tileset in the tree uses `.pla` or `swapPalettes`; no map uses `OBJ_EVENT_GFX_LIGHT_SPRITE`. `src/debug.c` 'Set time of day: Night' goes to exactly 20:00, so the tint needs about 3 real minutes to deepen, but the light sprites switch on within a few seconds.
- Popups: `src/overworld.c:670` (`sLastMapSectionId` set on every map load), `:915-925`; houses and the Center use the town's section and `show_map_name` false.
- Dex: `src/event_data.c:72` `EnableNationalPokedex()` also sets the dex mode to National; `src/pokedex.c:1357` new game resets to Hoenn mode; `data/maps/Hollowbrook_ProfFennickLab/scripts.inc:360` 'No Pokedex handout yet'.

## Measured

| What | Result |
|---|---|
| Prototype ROM size with followers, popup, skip, defaults | 25.573 MiB used (today 25.58 in `devices.md`, no change) |
| Same plus `POKEDEX_PLUS_HGSS` | 25.620 MiB (+0.047) |
| Hold R: 4-page field message | all pages and the closing wait done in about 1 s (frames sampled at about 0.15 s) |
| Hold R: battle intro to command menu | about 3 s, no hang; a trainer turn also ran through |

## Not verified

- Hold-R on Delta (VBA-M) or Miyoo; only mGBA.
- Egg and Tutor tabs in the summary screen with the flags set (compiled only); the NPC script's Egg list (menu seen, list not opened).
- Nickname-skip catch flow (compiled only).
- Followers through doors, Surf, scenes and warps (open-air walking only).
- The window `.pla` glow in the real engine (my image is a simulation of the blend formula), and the Mart sign position.
- The 'door popups only once' behaviour (read from code, not walked).

## Traps for whoever applies these

- Closing the Porymap window before touching any `map.json`.
- The light sprite offsets differ per type (type 0 is centred on the tile, type 1 is half a tile left).
- New flags: rename in `include/constants/flags.h`, add to `design/flags.md`, add to `Veldris_Debug_ResetStory` and run `python3 design/tools/check_debug_reset.py`.
- Disk: the scratch disk was at 98% (about 1 GB free) during this work and one ROM copy failed with 'No space left'. Delete finished clones (`scratchpad/clones/*`, about 400 to 700 MB each).
