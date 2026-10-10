# Built trainer roster: leaders, Elite Four and Champion

Status: **BUILT 2026-10-01** (compiled, and fought in mGBA, see the battle checks below). Names approved by the author on 2026-10-01 ([leader-names.md](leader-names.md)). Teams and levels from [gyms.md](gyms.md) and [postgame.md](postgame.md). Movesets were hand-curated by agents from this tree's real learnsets, then checked by script: every move is level-up-legal at that level, or (from level 40 up) teachable. Source: `src/data/trainers.party`.

**How they were added.** They **reuse vanilla Hoenn trainer ids**, so they cost no new id and `TRAINERS_COUNT_EMERALD` is unchanged. Each vanilla block was rewritten and its header renamed. In `include/constants/opponents.h` the id now has the Veldris name, and the old Hoenn name is kept as an alias, so the untouched Hoenn map scripts still compile. Use the new names in scripts (`trainerbattle_single TRAINER_HACHIMEL, ...`). **Every Pokémon has `IVs: 0 ...`** (no IVs, per the author) and no EVs. Items: Potion up to Full Restore. AI: Basic Trainer. Elite Four and Champion keep the vanilla Mugshot colours.

| Constant | Name | Replaces | Type | Pic | Team (level) |
|---|---|---|---|---|---|
| `TRAINER_HACHIMEL` | HACHIMEL | Roxanne | Bug, gym 2 | Veldris Leader Bug | Kricketune 17, Vivillon 19 |
| `TRAINER_SANZUFORD` | SANZUFORD | Brawly | Ghost, gym 3 | Veldris Leader Ghost | Shuppet 23, Litwick 24, Mimikyu 25 |
| `TRAINER_HAGANE` | HAGANE | Wattson | Steel, gym 4 | Veldris Leader Steel | Bronzor 29, Pawniard 30, Tinkatuff 31 |
| `TRAINER_WAKASAGI` | WAKASAGI | Flannery | Ice, gym 5 | Veldris Leader Ice | Sneasel 35, Vanillish 36, Lapras 37, Avalugg 37 |
| `TRAINER_TOBIN` | TOBIN | Norman | Flying, gym 6 | Veldris Leader Flying | Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42 |
| `TRAINER_ASEBY` | ASEBY | Winona | Poison, gym 7 | Veldris Leader Poison | Weezing 46, Crobat 47, Drapion 47, Garbodor 47, Toxapex 48 |
| `TRAINER_SUZURAN` | SUZURAN | Tate and Liza (now a single battle) | Fairy, gym 8 | Veldris Leader Fairy | Azumarill 52, Dachsbun 52, Ribombee 53, Hatterene 54, Gardevoir 55 |
| `TRAINER_MIZZLE` | MIZZLE | Juan | Water, gym 9 | Veldris Leader Water | Gyarados 58, Seismitoad 58, Araquanid 59, Barraskewda 59, Lanturn 59, Milotic 60 |
| `TRAINER_OSSIAN` | OSSIAN | Sidney | Elite Four, Dark | Veldris Elite Four Ossian (Galaxeeh Giovanni sprite) | Houndoom 65, Honchkrow 65, Pangoro 65, Krookodile 66, Absol 66 |
| `TRAINER_HYACINTH` | HYACINTH | Phoebe | Elite Four, Psychic | Veldris Elite Four Hyacinth (Black Fragrant Karen sprite) | Espeon 66, Meowstic 66, Reuniclus 67, Farigiraf 67, Alakazam 68 |
| `TRAINER_DUNMORE` | DUNMORE | Drake | Elite Four, Fighting | Veldris Elite Four Dunmore (Black Fragrant Chuck sprite) | Breloom 68, Hawlucha 68, Heracross 69, Annihilape 69, Conkeldurr 70 |
| `TRAINER_DRAYDEN` | DRAYDEN | Glacia | Elite Four, Dragon | Veldris Elite Four Drayden | Goodra 69, Kommo-o 69, Dragapult 70, Baxcalibur 70, Salamence 71, Dragonite 71 |
| `TRAINER_CYNTHIA` | CYNTHIA | Wallace | Champion | Veldris Champion Cynthia | Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 |

**Notes and caveats.**
- Elite Four pictures chosen by the author (2026-10-01, candidate #1 each) and battle-checked: all render with clean transparency.
- The ids are in vanilla order (Sidney, Phoebe, Glacia, Drake), so the id order is OSSIAN, HYACINTH, DRAYDEN, DUNMORE. The League script sets the actual fight order (DRAYDEN last), so nothing depends on the id order.
- The Hoenn rematch blocks still hold the old Hoenn teams, except that Roxanne 2 to 4 (ids 770 to 772) are now Crestfall's GRETA, DALE and WREN; Roxanne 5 and the other leaders' rematch blocks are untouched. `gRematchTable` in `src/battle_setup.c` still keys these ids (`REMATCH_ROXANNE` now groups HACHIMEL, GRETA, DALE and WREN). It is inert while no Veldris script uses `ShouldTryRematchBattle` or `trainerbattle_rematch*`, `FLAG_HAS_MATCH_CALL` stays unset (only Hoenn scripts and the debug menu set it) and the VS Seeker is off (`I_VS_SEEKER_CHARGING` 0). Rewrite the table before enabling any of them. Never set `FREE_MATCH_CALL` to TRUE: every table trainer would then count as ready for a rematch.
- Gender and Music are placeholders chosen to fit each sprite (SANZUFORD uses the 'Girl' music).
- **Battle check (2026-10-01, mGBA, debug menu Trainers > Try Battle).** All 13 trainers were fought: intro text, class and name, picture and first send-out species and level were correct for each. CYNTHIA was played for several turns and used her curated moves (Payback seen). One bug found and fixed: MIZZLE's picture drew a light-blue box because the background was palette index 4, not 0. The indices were swapped in `veldris_leader_water.png` and the fix re-checked. Not checked: later team members, full fights, and the vanilla alias scripts.
- The movesets are in the file itself. Tune any set by editing its block.

## Crestfall and Troglodyte blocks (BUILT 2026-10-01)

When a new TROGLODYTE block is added, also add its row to `VELDRIS_TROGLODYTE_FIGHTS` in `include/veldris_journal.h` ([journal.md](journal.md)).

| Constant | Id | Name | Pic and class | Team |
|---|---|---|---|---|
| `TRAINER_CRESTFALL_GYM_1` | 771 (was Roxanne 3) | DALE | **placeholder** Youngster pic, Youngster | Zigzagoon 9 |
| `TRAINER_CRESTFALL_GYM_2` | 772 (was Roxanne 4) | WREN | **placeholder** Gentleman pic, Gentleman | Slakoth 10 |
| `TRAINER_CRESTFALL_GRETA` | 770 (was Roxanne 2) | GRETA | `Veldris Leader Normal` (kwenio ORAS lass, indexed), Leader | Skitty 10, Miltank 12 (Oran Berry) |
| `TRAINER_TROGLODYTE_HOLLOWBROOK` | 520 (was Brendan Route 103 Mudkip) | TROGLODYTE | Veldris Troglodyte pic (DP Rich Boy, 2026-10-01), Rival | SIR BISCUIT (Lillipup) 1, plus his starter 5 |
| `TRAINER_TROGLODYTE_CRESTFALL` | 521 (was Brendan Route 110 Mudkip) | TROGLODYTE | same | SIR BISCUIT 7, plus his starter 8 (starters also know Quick Attack for Treecko and Torchic) |

Teams are from [teams.md](teams.md). All have `IVs: 0` on every Pokémon. Troglodyte uses `Pool Prune: Rival Starter` with `Party Size: 2`.

**Battle check (mGBA, same method as above):** all five show the right intro, name and first Pokémon. TROGLODYTE's second Pokémon was seen to be exactly one starter (Treecko, `VAR_TROG_STARTER` = 0) after SIR BISCUIT fainted, so the pool prune works. Not yet seen: the Torchic and Mudkip variants (set the var to 1 or 2), full fights, and the old Hoenn Route 103 and 110 scripts that now point at the renamed ids.

**Caveats.** The Rival class shows 'PKMN TRAINER' in the intro, so a Veldris class name would need a small text edit. **Author rule (2026-10-01): always reuse vanilla ids.** Greta, DALE and WREN were first built on new ids 855 to 857 and moved to reused ids 770 to 772 the same day, so all 9 brand-new ids (855 to 863) are free again and `TRAINERS_COUNT_EMERALD` is back at 855. The other six Troglodyte fights should reuse vanilla ids too.

**Poshness update (BUILT 2026-10-08, author liked it).** Both built Troglodyte blocks now have `Ball: Luxury` under every Pokémon (his Pokémon come out of black-and-gold Luxury Balls with a green sparkle burst, seen in mGBA) and `Music: Rich` instead of `Music: Male` (the rich-kid spotted-you jingle, `mus_encounter_rich`, a real song in the ROM; the `// MUS_TEST` comment in `songs.h` is upstream noise). The shared `Rival` class entry is untouched (39 blocks use it, most never reached in Veldris). **The Goldsworth cousins and Troglodyte's other fights should copy the same two lines when their blocks are built.** Not run in game: the jingle itself (it plays when he spots you in the overworld; the debug battle skips that), so the author may want to hear it once (a clip was sent to the author in chat on 2026-10-08).

**Banner and sting (BUILT 2026-10-09, author: 'i like the Rich jingle, vs fanfare for trog').** Troglodyte's blocks also carry `Mugshot: Gold` (his own gold vs-screen banner: new colour `MUGSHOT_COLOR_GOLD`, palette `graphics/battle_transitions/gold_bg.pal`, a recolour of the yellow banner, hack-made so no credits row) and beating a Class `Rival` trainer plays the gym-leader victory tune (`MUS_VICTORY_GYM_LEADER`) instead of the ordinary trainer one. **Copy `Music: Rich`, `Mugshot: Gold` and `Ball: Luxury` onto every Troglodyte and Goldsworth-cousin block.** In the Hollowbrook scene (`Hollowbrook_EventScript_TrogOutsideTrigger`) a `playbgm MUS_ENCOUNTER_RICH, FALSE` plays the Rich jingle as he shouts. `trainerbattle_no_intro` does not skip the trainer's `Music:` jingle: its macro passes `playMusicA` TRUE, so `BattleSetup_ConfigureTrainerBattle` (`src/battle_setup.c`) plays it when the macro runs, after the scripted dialogue and just before the battle. The explicit `playbgm` only moves the first play to the shout, and the jingle (a looping song) restarts once when the battle starts, because the BGM player always restarts a song. This is deliberate (the author wants the jingle at the shout). A `trainerbattle_no_intro` fight with no `playbgm` (Crestfall) gets one play, at battle start. Debug menu Trainers > Try Battle uses the wild transition and never shows the banner; to see it set `VAR_HOLLOWBROOK_STATE` to 3 (flag/var debug) and walk into the lab doorway scene in Hollowbrook. Engine edits are logged in [engine-edits.md](engine-edits.md). **Tested 2026-10-09 (headless mGBA, debug preset 3):** the gold banner shows (Troglodyte's Rich Boy picture on an orange-gold band over the blue player band), and the battle runs as before. The Rich jingle and the new victory tune are **not heard** in the headless run (no audio captured); the build contains both. Alternative victory sting if wanted: `MUS_VICTORY_LEAGUE` (the Elite Four tune, 35 seconds, a little long). The tune is one word in `src/battle_main.c`.

## Route 1 trainers (BUILT 2026-10-01)

Three vanilla Route 102 entries reused (no new ids). Names are PROPOSED.

| Alias | Reused id | Name | Pic and class | Team |
|---|---|---|---|---|
| `TRAINER_VELDRIS_ROUTE1_YOUNGSTER` | `TRAINER_ALLEN` (333) | TOBY | Youngster | Lillipup 4 |
| `TRAINER_VELDRIS_ROUTE1_LASS` | `TRAINER_TIANA` (603) | MAISIE | Lass | Zigzagoon 4, Skitty 4 |
| `TRAINER_VELDRIS_ROUTE1_FARMER` | `TRAINER_RICK` (615) | AMOS | **placeholder** Hiker pic and class (no farmer class yet; the DP rancher sprites in the asset repo are an option) | Zigzagoon 5, Skitty 5 |

All IVs 0. **Checked in mGBA:** TOBY spots the player, walks over, says his intro, battles with Lillipup 3 (before the 2026-10-01 level raise), pays out and says his after line. **MAISIE and AMOS fought 2026-10-09 (mGBA, debug warps):** both spot the player, walk up, say the intro, send out Zigzagoon then Skitty (levels 4 and 5), and give the defeat and after lines. Their Skitty uses Sing, so a test Mudkip spends turns asleep.

## Gym battlefield conditions (BUILT 2026-10-08, PROPOSED defaults)

The author liked the idea of weather and terrain at the start of a gym fight (2026-10-08). Each leader block in `src/data/trainers.party` has one `Starting Status:` line, which sets a condition on the first turn with an on-screen message. Chosen to be fun but fair: temporary versions (about 5 turns) so the effect opens the fight without running it, and nothing that harms only the player except one light hazard. **The exact picks are PROPOSED**, easy to change.

| Gym | Leader | Line in the block | What the player sees | Why this one |
|---|---|---|---|---|
| 1 Normal | GRETA | none | n/a | First gym stays plain |
| 2 Bug | HACHIMEL | `Starting Status: Grassy Terrain Temporary` | meadow terrain, grounded Pokémon heal a little each turn | Apiary and meadow theme; helps both sides |
| 3 Ghost | SANZUFORD | `Starting Status: Trick Room Temporary` | the dimensions twist, slower Pokémon move first | Spooky and symmetrical; the alternative is `Weather Fog Temporary` but fog cuts every move's accuracy to 60 percent, which feels bad |
| 4 Steel | HAGANE | `Starting Status: Electric Terrain Temporary` | sparks on the floor, no sleep for grounded Pokémon | Forge theme without chip damage (sandstorm would hurt only the player, since his whole team is Steel) |
| 5 Ice | WAKASAGI | `Starting Status: Weather Snow Temporary` | it starts to snow; Ice types get a Defense boost | Tested in mGBA, message and snow animation seen |
| 6 Flying | TOBIN | `Starting Status: Tailwind Opponent Temporary` | his side's speed doubles for the first turns | Wind theme; the alternative is no status, since this one is a head start for him |
| 7 Poison | ASEBY | `Starting Status: Toxic Spikes Player L1` | toxic spikes on the player's side | Tested in mGBA, message seen; only bites when the player switches in a grounded Pokémon |
| 8 Fairy | SUZURAN | `Starting Status: Misty Terrain Temporary` | mist, no new status conditions on grounded Pokémon | Fits the Fairy gym; helps both sides |
| 9 Water | MIZZLE | `Starting Status: Weather Rain Temporary` | it starts to rain, Water moves hit harder and Fire moves weaker | Water gym; temporary because his whole team is Water and permanent rain would be harsh |

**To change or remove one:** edit or delete its `Starting Status:` line in `src/data/trainers.party`. Values are the camelCase names in `include/constants/battle.h` (`STARTING_STATUS_DEFINITIONS`) written as words, for example `Weather Rain` or `Weather Rain Temporary`, and several can be joined with `/`. Drop `Temporary` for a status that lasts the whole fight. Not checked in mGBA: Grassy, Trick Room, Electric, Tailwind, Misty and Rain.
