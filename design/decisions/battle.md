# Battle decisions: five briefs for the author

Written 2026-10-09 by the `decisions-battle` stream. **Everything here is PROPOSED.** Nothing in the repo was edited. Facts come from reading the tree at commit `8bb23927` ("read") and from a throw-away lab build in a scratch clone, run in mGBA ("ran"; the lab patch is `prototypes/battle_lab.patch`, never merged; its screenshots stayed in the scratch area and are not in the repo). Each brief ends with a one-word answer.

## Answer sheet

| # | Question | Answer with one of | My pick |
|---|---|---|---|
| 1 | How clever should opponents get as the game goes on? | `ladder` / `flat` / `custom` | `ladder` |
| 2 | What do trainer Pokémon get when a block forgets the `IVs:` line? | `zero` / `explicit` / `leave` | `zero` |
| 3 | Level caps (stop the team out-levelling the next gym) | `off` / `soft` / `hard` / `hardobey` | `soft` |
| 4 | Stat boosts at the start of boss fights | `none` / `legends` / `bosses` | `legends` |
| 5 | Tag battles and two-opponent battles | `none` / `tag` / `both` | `both` |

Example reply: `1 ladder, 2 zero, 3 soft, 4 legends, 5 both`.

---

## 1. AI ladder: weak early, smart late

**Plain words.** Every opponent built so far (all 18 blocks: gym leaders, Elite Four, Cynthia, Greta and her two trainers, both Troglodyte fights) thinks the same way: `Basic Trainer` (never picks a move that will fail, takes a knockout when it sees one, otherwise the strongest move, and swaps only in a few special cases). The engine has a dial from 'random but sane' up to 'knows your moves and predicts your swaps'. A ladder lets Troglodyte fumble early and the League fight like a player.

**What exists (read).** `include/constants/battle_ai.h` has 37 numbered flags (bit 0 to 36), four engine-only flags (`Dynamic Func`, `Roaming`, `Safari`, `First Battle`) and four bundles:

| Group | Flags |
|---|---|
| Move choice | Check Bad Move, Try To Faint, Check Viability, Try To 2hko, Prefer Highest Damage Move, Hp Aware, Force Setup First Turn, Risky, Conservative, Powerful Status, Prefer Status Moves, Prefer Baton Pass, Stall, Will Suicide |
| Switching | Smart Switching (adds Smart Mon Choices), Smart Mon Choices, Sequence Switching (party order, never swaps), Randomize Switchin, **Ace Pokemon** (last mon held back), Double Ace Pokemon, Randomize Party Indices |
| What it knows about you | **Omniscient** (moves, items, abilities), Ability / Item / Move Omniscience, Assume Stab, Assume Status Moves, Weigh Ability Prediction, Know Opponent Party |
| Prediction | Predict Switch, Predict Incoming Mon, Predict Move, Pp Stall Prevention |
| Handicap and doubles | Negate Unaware, Attacks Partner, Smart Tera, Double Battle (the engine sets it in doubles) |
| **Bundles** | `Basic Trainer` = Check Bad Move + Try To Faint + Check Viability. `Smart Trainer` = Basic + Omniscient + Smart Switching + Smart Mon Choices + Pp Stall Prevention + Smart Tera + Randomize Switchin. `Prediction` = the three Predict flags. `Assumptions` = Assume Stab + Assume Status Moves + Weigh Ability Prediction |

**How the party file sets it (read, and ran).** One line per block, `AI: Flag / Flag / Flag`. The name is the constant without `AI_FLAG_`, any capitals, spaces or underscores, bundles allowed, up to 64 (`tools/trainerproc/main.c` lines 1198 and 1891). I ran `AI: Smart Trainer / Prediction / Hp Aware / Try To 2hko / Ace Pokemon` through the tool and compiled the result against the header: fine. A typo (`AI: Foo Bar`) is not silent: it becomes `AI_FLAG_FOO_BAR undeclared`, a build error. No `AI:` line means no flags at all (every move scores the same, so moves are random). Today in `trainers.party` (855 blocks, 839 with an `AI:` line): 640 `Check Bad Move`, 175 `Basic Trainer`, 24 older mixes; all 18 Veldris blocks `Basic Trainer`.

**Two behaviours worth knowing (read).**
- `Check Bad Move` alone gives *random but sane*: it only removes moves that would fail, then picks among equals (`ChooseMoveOrAction_Singles`, `src/battle_ai_main.c`). `Try To Faint` and `Check Viability` are what make the AI hunt knockouts and damage.
- Without `Smart Switching` an AI swaps only in a short list of special cases (every move useless, Wonder Guard, Truant, Perish Song, a Natural Cure or Regenerator Pokémon). The type-matchup swap, the absorb-ability swap, the trapper swap and most status swaps sit behind `Smart Switching` (`src/battle_ai_switch.c`, about ten gates). The engine's own wild-Pokémon ladder is the same idea in miniature: `Check Bad Move` always, `Check Viability` from average level 20, `Try To 2hko` from 60, `Hp Aware` from 80 (`GetWildAiFlags`, `src/battle_ai_main.c` line 231).

**Proposed ladder.** Rungs add things; names are labels only.

| Rung | Line | Feel |
|---|---|---|
| Dim | `AI: Check Bad Move` | Random sane moves, so it will sometimes pick Growl over a strong hit. Never swaps cleverly |
| Basic (today) | `AI: Basic Trainer` | Takes KOs, best damage |
| Sharp | `AI: Basic Trainer / Hp Aware / Try To 2hko` | Also heals and sets up at sensible times, goes for two-hit KOs |
| Smart | `AI: Smart Trainer / Hp Aware` | Swaps on bad matchups, sends the right mon after a KO, reads your moves |
| Smart plus | `AI: Smart Trainer / Hp Aware / Try To 2hko` | Smart, and finishes you faster |
| Smartest | `AI: Smart Trainer / Prediction / Hp Aware / Try To 2hko` | Also guesses your swaps and your next move |

`/ Ace Pokemon` is added to every leader, Elite Four and Cynthia line (their last Pokémon is the ace; the flag keeps it in the back until it is the last one). It is not added for Troglodyte: his party order is random (see below).

| Fight | Block and line in `src/data/trainers.party` | Today | Proposed |
|---|---|---|---|
| Troglodyte 1 (lab door) | `TRAINER_TROGLODYTE_HOLLOWBROOK`, line 9527 | Basic | **Dim** |
| Troglodyte 2 (Crestfall) | `TRAINER_TROGLODYTE_CRESTFALL`, line 9573 | Basic | **Dim** |
| Troglodyte 3, 4 (gym 3, gym 5) | not built | | Basic |
| Troglodyte 5 to 8 (gym 6, gym 7, Victory Road, finale) | not built | | Sharp (never Smart: he stays one rung under the leaders of his time; `postgame.md` already asks for 'the lowest that makes him lose') |
| Gym 1 GRETA | `TRAINER_CRESTFALL_GRETA`, 16853 | Basic | Basic (unchanged) |
| Gym 2 HACHIMEL | 4809 | Basic | Basic (unchanged) |
| Gym 3 SANZUFORD | 4836 | Basic | Basic `/ Ace Pokemon` |
| Gym 4 HAGANE, gym 5 WAKASAGI, gym 6 TOBIN | 4871, 4906, 4949 | Basic | Sharp `/ Ace Pokemon` |
| Gym 7 ASEBY, gym 8 SUZURAN, gym 9 MIZZLE | 4992, 5043, 5094 | Basic | Smart `/ Ace Pokemon` |
| Elite Four OSSIAN, HYACINTH, DRAYDEN, DUNMORE | 4597, 4648, 4699, 4758 | Basic | Smart plus `/ Ace Pokemon` |
| Champion CYNTHIA | 6265 | Basic | Smartest `/ Ace Pokemon` |

That is **14 lines** edited today (2 Troglodyte, SANZUFORD, 3 + 3 leaders, 4 League, Cynthia); six Troglodyte blocks follow when built. Troglodyte's later fights are written with the same lines when they are made.

**Cost.** Data only: `AI:` lines in a file we own. No engine edit, no new id or flag, no save change, no ROM growth (`aiFlags` is already 64 bits in every trainer). **The lab ROM built and ran with all of these flag sets** (Dim, Basic, Smart, Smartest, with `Ace Pokemon`).

**Thinking time (ran).** Debug switch `DEBUG_AI_DELAY_TIMER` prints the AI's frames and CPU cycles in place of 'What will X do?'. Six-versus-six singles, my level-50 team against Cynthia's team on each rung, first fights (60 frames = 1 second):

| Rung | Frames at the action prompt | CPU cycles | Seconds on a real GBA |
|---|---|---|---|
| Dim (`Check Bad Move`) | 3 to 4 | 1.00 to 1.07 million | 0.06 |
| Basic | 4 | 1.16 million | 0.07 |
| Smart (`Smart Trainer / Hp Aware / Ace Pokemon`) | 8 | 2.37 million | 0.14 |
| Smartest (adds `Try To 2hko / Prediction`) | 13 | 3.87 to 3.94 million | 0.23 |

One battle per rung, turns 1 to 3, so read it as plus or minus one frame. A small fight (one Pokémon each side) costs 0 to 1 frames on Basic, and the tag battle in brief 5 (Basic foe plus a dim partner) cost 8 frames on its first turn. The Smartest rung is about 3 times Basic and a quarter of a second: noticeable, not a freeze.

For scale, the upstream test suite caps singles at 2 frames (no flags) and 7 (Smart Trainer), doubles at 14 and 28, a Steven-style tag battle at 24 (`test/battle/ai/ai_thinking_time.c`).

**Risks.**
1. **Omniscient feels like cheating.** `Smart Trainer` knows your whole moveset, items and abilities. Softer middle rung: replace it by `Basic Trainer / Smart Switching / Assumptions` (knows your same-type moves and sometimes your status moves, not the rest). Say `custom` if you want that for gyms 7 to 9.
2. **Smart switching lengthens fights.** On bad matchups it swaps about half the time (`SHOULD_SWITCH_HASBADODDS_PERCENTAGE` 50, `include/config/ai.h`); six-mon leaders take more turns.
3. **The AI is only as good as the four moves in the block.** A smart AI with weak moves is still weak; the 13 built blocks have curated, level-legal sets.
4. **Doubles and tag battles.** `Smart Mon Choices` and `Smart Tera` are singles only; in doubles the engine adds `Double Battle` by itself and the rungs do less. Doubles cost about 4 times the thinking time.
5. **Troglodyte's party order is random** (pool prune). `Ace Pokemon` would hold back a random mon, so he gets none. Pin an ace with `Tags: Ace` first if you ever want one.
6. **The debug 'Try Battle' ignores the block's AI line** (it uses the AI flags set in its own menu, `gDebugAIFlags`, `src/battle_ai_main.c` line 315, and `GetDebugAiTrainer` in `include/data.h`). Test through a real script fight.
7. AI is random, so a rung change cannot be proved by one fight; it needs a few.

**Test plan.** (1) `make -j4` after the 14 edits. (2) A throw-away debug slot that starts a chosen trainer with `trainerbattle_no_intro` (the lab's scripts `Veldris_Lab_*` in `prototypes/battle_lab.patch` are exactly that) and `DEBUG_AI_DELAY_TIMER` TRUE in a private build to read the thinking time. (3) Troglodyte 1: expect Growl and Tail Whip turns; Cynthia: expect swaps and no wasted moves; check six turns each. (4) Never ship the timer switch.

**Answer:** `ladder` (as tabled), `flat` (keep Basic everywhere, nothing changes), `custom` (you edit the table above).

---

## 2. Default IVs of 0

**Plain words.** Trainer Pokémon must have no IVs (your rule). Today that depends on every block remembering an `IVs: 0 ...` line. If a line is forgotten the Pokémon silently gets perfect IVs.

**Facts (read and ran).**
- `tools/trainerproc` has a **file-level default**, set by a header line, no tool edit needed: `#pragma trainerproc ivs 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe`. Also `#pragma trainerproc ivs explicit` (a missing line becomes a build error) and the same pair for `level` (`level 5`, `level explicit`). Parsed in `parse_pragma`, `tools/trainerproc/main.c` line 1051; the pragma must come before the first `===` block, once per file.
- **Today's default is 31.** I generated a block with no `IVs:` line: `TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31)`. The same for a missing `Level:` (it becomes **100**).
- **All 855 vanilla and Veldris blocks already carry an `IVs:` and a `Level:` line on every Pokémon** (1,819 of 1,819). 699 of them are zero IVs; the rest keep vanilla Hoenn values (31, 12, 3, 4, 2, 18, ...). So no vanilla block is changed by any choice below.
- **The 18 built Veldris blocks plus the three Route 1 trainers (76 Pokémon) are all explicitly `0 / 0 / 0 / 0 / 0 / 0`.** Nothing changes for them.
- **Proof it is safe:** I inserted the pragma lines and ran the real `trainers.party` through the tool: the generated `trainers.h` is identical to today's, line for line (diffed, ignoring the `#line` markers and the source-path comment). Both the `0` form and the `explicit` form.
- The pragma is per file. `src/data/battle_partners.party` (Steven's block has explicit 31s) is separate; a tag-battle partner block (brief 5) needs its own two lines or explicit IVs.
- A partial line like `IVs: 31 Spe` would start from the pragma's value (0) instead of from 31. Nothing uses partial lines.

**Options.**
| Word | What changes | Result |
|---|---|---|
| `zero` | Add `#pragma trainerproc ivs 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe` and `#pragma trainerproc level explicit` under the header comment | A forgotten `IVs:` means 0. A forgotten `Level:` stops the build instead of making a level-100 trainer |
| `explicit` | `ivs explicit` and `level explicit` | A forgotten line stops the build with a message. Keeps the rule 'every Pokémon lists its IVs' but enforced |
| `leave` | Nothing | Today: a forgotten line means 31 and nothing warns |

**Cost.** One or two lines in `src/data/trainers.party`, near line 72; data only, no engine edit, nothing for `engine-edits.md` (it is a data-file line, not an upstream C change). Then reword the CLAUDE.md rule ('a missing `IVs:` line means 31' becomes 'means 0, set by the pragma at the top of `trainers.party`') and the note in `design/teams.md` line 5; `design/postgame.md` line 10 repeats it too. Optional: still write `IVs: 0 ...` lines for clarity; they are harmless.

**Risk.** A merge conflict if upstream rewrites the header comment of `trainers.party` (low: the file is already ours block by block). Because the pragma also sets `Level`, nothing else is affected.

**Test plan.** `make` and diff `src/data/trainers.h` against the previous build (done once here: identical). After adding a new block without IVs, check the generated header shows `TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0)`.

**Answer:** `zero` (my pick), `explicit`, `leave`.

---

## 3. Level caps

**Plain words.** The engine can stop a Pokémon from gaining levels past 'the strongest thing you must beat next' (the next gym leader's ace). The cap table is already written in `src/caps.c` but switched off. With the Exp. Share on from the first frame, the whole team of six levels up together, so a cap matters more here than in a normal game.

**The table is already right (read).** `src/caps.c` `sLevelCapFlagMap`: the cap is the first row whose badge you do not yet hold.

| You hold | Cap | Next opponent's highest level (from `trainers.party`) |
|---|---|---|
| 0 badges | 12 | GRETA 12 |
| badge 1 | 19 | HACHIMEL 19 |
| 2 | 25 | SANZUFORD 25 |
| 3 | 31 | HAGANE 31 |
| 4 | 37 | WAKASAGI 37 |
| 5 | 42 | TOBIN 42 |
| 6 | 48 | ASEBY 48 |
| 7 | 55 | SUZURAN 55 |
| 8 | 60 | MIZZLE 60 |
| 9 badges, not yet Champion | **75** | Elite Four 66, 68, 70, 71 then CYNTHIA 75 |
| Champion (`FLAG_IS_CHAMPION`, set in `data/scripts/hall_of_fame.inc`) | none | post-game |

Two findings. **(a) One gap:** between badge 9 and the Champion the cap jumps to 75, but the four Elite Four members top out at 66 to 71. A player could grind to 75 before the League. The fix is one more row, keyed on a League flag (`FLAG_DEFEATED_ELITE_4_SIDNEY` and friends exist, 0x4FB to 0x4FE); which flag depends on the League script, which is not built, so I did not guess. **(b) Doc drift:** `design/gyms.md` ('badge 9 row currently the placeholder 50') and `design/engine-limits.md` (`caps.h` row, 'badge 9 at level 50') are stale; the table says 60. Troglodyte's planned levels (arc doc: fight 3 at 20 to 22 with cap 25, fight 5 at 37 to 40 with cap 42, fight 7 at 55 to 57 once the cap is 75) all sit under the cap of their time.

**Everything that reads the cap (read).**
| What | Where | Behaviour |
|---|---|---|
| Battle Exp | `src/battle_script_commands.c` 2294 to 2330, `GetSoftLevelCapExpValue` | Soft: Exp divided by 4 at the cap, 8 at cap+1, 16, 32, then 64 from cap+4. Hard: 0 at or above the cap, and Exp that would cross the cap is trimmed to land exactly on it |
| Rare Candy | `src/party_menu.c` 5840 | Refused at or above the cap if `B_RARE_CANDY_CAP` is TRUE (works with soft or hard) |
| Exp Candies | `src/pokemon.c` 3522 | Trimmed to the cap only with `B_RARE_CANDY_CAP` TRUE **and** hard |
| Day Care | `src/daycare.c` 324, 337, 389, and `TryIncrementMonLevel` (`pokemon.c` 5003) | Levels stop at the cap whenever the level-cap type is on (even with Exp cap off) |
| Catch-exp, Exp. Share | the same Exp routine | Capped the same way |
| Obedience | `src/battle_util.c` 5625 | **Not tied to the cap.** Thresholds 10, 20, ... 90 per badge, ignored after badge 9 (a Veldris edit). With `B_OBEDIENCE_MECHANICS` at `GEN_LATEST` the check uses the level a Pokémon was *met* at, so a Pokémon you caught yourself never disobeys; only traded or NPC-gifted Pokémon do. Ran: a level-40 Pokémon handed over by a script at 0 badges printed 'Tropius ignored orders!' |
| Catch-rate penalty | `src/battle_script_commands.c` 8038 `sBadgeLevel` {25, 30, 35 ... 65} | A third level table, unaligned with the gym curve; it only lowers catch rates |

**How the always-on Exp. Share interacts (read; and ran, below).** With `B_SPLIT_EXP` at `GEN_LATEST` each Pokémon that fought gets the full Exp, and every other living party member gets **half** (`calculatedExp / 2`, lines 2224 to 2243). So the lead levels at its normal speed and the bench at half speed: the team does not out-level the lead by much, it climbs together. The cap is applied per Pokémon, so a hard cap stops the whole team at once.

**Options.**
| Word | Switches in `include/config/caps.h` | What the player sees |
|---|---|---|
| `off` (today) | nothing | Free grinding. A patient player reaches a gym 10 levels over its ace; the leader scaling is for nothing |
| `soft` | `B_EXP_CAP_TYPE EXP_CAP_SOFT`, `B_LEVEL_CAP_TYPE LEVEL_CAP_FLAG_LIST`, `B_RARE_CANDY_CAP TRUE` | Nothing is ever blocked. At the cap a Pokémon earns a quarter, then an eighth ... so grinding past it is pointless but not forbidden (ran: the same Mudkip at the cap earned 20 Exp. Points where the hard cap gave 0). Rare Candy refuses at the cap |
| `hard` | same, with `EXP_CAP_HARD` | At the cap a Pokémon earns **nothing** (ran: the game still prints 'Mudkip gained 0 Exp. Points!' for it, then 'The rest of your team gained Exp. Points thanks to the Exp. Share!'). Exp Candies and the Day Care stop at the cap. Beating the next leader lifts it |
| `hardobey` | `hard` plus one edit in `GetAttackerObedienceForAction` (`src/battle_util.c`): replace the nine badge lines by `obedienceLevel = GetCurrentLevelCap();` | Own Pokémon cannot pass the cap by Exp, and traded or gifted ones that are above it start ignoring orders. (Also optional: set `sBadgeLevel` to `{12, 19, 25, 31, 37, 42, 48, 55, 60, 100}`.) Touches an upstream function that already carries two Veldris edits, so log it in `engine-edits.md` |

Optional with any cap: `B_LEVEL_CAP_EXP_UP TRUE` gives Pokémon below the cap extra Exp (up to double when four or more levels under), a catch-up for new catches.

**Cost.** `off`: none. `soft` and `hard`: three config lines (the table needs no change); log them in `engine-edits.md`; the lab ROM built and ran with both the hard and the soft set. Plus one new row for the Elite Four gap when the League exists. `hardobey`: one function edit.

**Risks.** (1) Hard cap plus Exp. Share stalls the whole team the moment the weakest-leveled slot catches up; players feel it as 'no more Exp until the badge', and route trainers still pay money. (2) Hard cap prints 'gained 0 Exp. Points!' for a Pokémon at the cap (ran), which reads like a bug; hiding it needs a small edit to the Exp routine in `src/battle_script_commands.c`. (3) A caught or gifted Pokémon above the cap (a level 20 wild Pokémon at 0 badges) is simply frozen there; fine. (4) The cap table must be edited whenever a gym ace changes (it is in four places: `trainers.party`, `caps.c`, debug preset 7, the docs). (5) `soft` can feel stingy at exactly the cap (÷4 at once).

**Test plan.** The lab already ran one fight under each (messages in the table). In the real build: debug preset 7 'Next badge + team' gives a team at the ace level of each gym; fight a trainer with a team member exactly at the cap and one well under; check (a) Exp amounts and messages, (b) Rare Candy refusal, (c) the cap lifting when a badge flag is set (debug menu Flags), (d) Day Care. For the League gap, check the cap with 9 badges and each Elite Four flag set.

**Answer:** `off`, `soft` (my pick: keeps the leader curve honest without a wall), `hard`, `hardobey`.

---

## 4. Stat boosts for bosses at battle start

**What exists in this tree (read).**
| Tool | What it does | Engine edit? |
|---|---|---|
| `Starting Status:` line in a block | Field conditions only (weather, terrains, rooms, Tailwind, hazards, pledge effects). **No stat stages.** Already used on the eight gym leaders (`design/trainer-roster.md`) | none |
| **`settotemboost` script command** | Queues stat stages for one battler in the next battle, applied before turn 1 with an animation and the line '*X's aura flared to life!*' (`asm/macros/event.inc` 2217, `src/battle_main.c` 5799 and 3479, string `STRINGID_AURAFLAREDTOLIFE`). Seven stats, any size. Example: `settotemboost B_POSITION_OPPONENT_LEFT, 1, 0, 0, 1` (+1 Attack, +1 Sp. Atk) | none |
| Held items | Terrain seeds raise Defence or Sp. Def on entry when a gym terrain is up (`TryTerrainSeeds`, `src/battle_hold_effects.c` 90), White Herb, Weakness Policy, Focus Sash, Booster Energy | none (data) |
| Abilities per Pokémon | `Ability:` line: Intimidate, Moxie, Speed Boost, Download, Defiant ... | none (data) |
| `AI: ... / Force Setup First Turn` | The AI opens with its own setup move (Swords Dance, Calm Mind ...) at the cost of its first turn | none (data) |
| A new Starting Status entry with stat stages | Would need `include/constants/battle.h` (the X-macro list), `src/battle_util.c`, a battle script | 3 upstream files; not recommended |

**Limits of `settotemboost` (read).** (1) It boosts only the Pokémon on the field first, i.e. the lead (`B_POSITION_OPPONENT_LEFT`); for Troglodyte the lead is random unless pinned with `Tags: Lead`. (2) The boost vanishes if that Pokémon faints or is swapped out (Smart Switching may do that). (3) It must come right before the battle in a script that the player *talks to or that a cutscene runs*; a trainer that spots the player and walks over reads its `trainerbattle` line before any other script command, so sighted trainers cannot be boosted without restructuring. Gym leaders, Elite Four and Cynthia (talk to start) and scripted Troglodyte fights can. (4) **Trap: the queue is not cleared until the next battle of any kind.** If the script queues a boost and the fight then does not start (trainer already beaten, script skipped), the next wild battle gets the aura. Guard it: set the boost only inside the branch where the fight is certain, after the `goto_if_defeated`. Confirmed in the lab (below). (5) The message wording is shared with real totem Pokémon (one string, `src/battle_message.c` 688).

**Which fights deserve it (my proposal; the story ones are your call under rule 10).** Not ordinary trainers or the eight gym leaders: each already has a field condition, and a boost on top is a second gimmick. The natural fits are single-Pokémon bosses, the legendaries (Kyogre, Dialga, Giratina: wild fights started with `setwildbattle`, where one aura line sells the moment), and, if you want them, the Commons leader, the Crown leader and Cynthia's lead. Nothing is built or placed until those fights exist.

**Cost.** One script line plus a guard per fight; no engine edit, no flag. **Ran:** (a) a script queued `settotemboost B_POSITION_OPPONENT_LEFT, 1, 0, 0, 1` and then `trainerbattle_no_intro` against DALE: after the send-out the game printed 'The opposing Zigzagoon's aura flared to life!'. (b) A boost queued and then a **wild** fight started instead (what a skipped trainer fight leaves behind): 'The wild Zigzagoon's aura flared to life!' on the wild Pokémon. The trap is real. (c) The data-only route: HACHIMEL's block (`Starting Status: Grassy Terrain Temporary`) with her Kricketune holding a `Grassy Seed` printed 'The battlefield is covered with grass!' then 'The Grassy Seed boosted the opposing Kricketune's Defense!' before turn 1, so a terrain gym can give its leader a free +1 with no script.

**Risks.** The trap above; boosting a random-order lead (Troglodyte); the boost being lost to a swap on a Smart rung (use it on bosses that do not swap, or on a single-Pokémon fight).

**Test plan.** (1) The labs above are the first pass (Lab 5, 6 and the seed fight are in `prototypes/battle_lab.patch`). (2) When the first real boss script is written: fight it, win, talk again, then walk into grass: no aura on the wild Pokémon. (3) Check the lead is the intended Pokémon (pin it with `Tags: Lead` on a pooled block). (4) For a seed or ability route, read the first-turn messages once.

**Answer:** `none`, `legends` (only the legendaries when they are built, my pick), `bosses` (legendaries plus the story bosses you approve).

---

## 5. Tag battles and two-opponent battles

**What the tree supports (read).**
| Kind | What it is | How it is started | State |
|---|---|---|---|
| Trainer double battle | One trainer with `Double Battle: Yes`, two Pokémon out each side | `trainerbattle_double` (a 'not enough Pokémon' text is required) | Vanilla, used by Gabby and Ty |
| **Two opponents** | Two trainers against you, you send two Pokémon | `trainerbattle_two_trainers A, textA, B, textB` from an NPC's script (macro exists, **unused in vanilla scripts**), the raw `trainerbattle` line from a cutscene, or two sighted double-battle trainers who both see you | Lab-tested here (below), with one trap |
| **Tag (multi) battle** | You plus an AI partner against one or two trainers | `multi_2_vs_1 TRAINER, text, PARTNER_X` or `multi_2_vs_2 ...`, exactly what Mossdeep's Space Center does with Steven (`data/maps/MossdeepCity_SpaceCenter_2F/scripts.inc` line 248) | Vanilla; lab-tested here with a Troglodyte stand-in |
| Follower NPC partner | An NPC walks behind you and joins every battle | `setfollowernpc` | **Off** (`FNPC_ENABLE_NPC_FOLLOWERS` is FALSE); turning it on grows `SaveBlock3`, which breaks Delta save states, so it needs your say-so first |

**What a Troglodyte tag partner costs (read, then ran).**
1. **Partner block:** a `=== PARTNER_TROGLODYTE ===` block in `src/data/battle_partners.party` (name, class, a front pic id, `AI:` line, Pokémon), a `#define PARTNER_TROGLODYTE 2` and `PARTNER_COUNT 3` in `include/constants/battle_partner.h` (an upstream file; log it). Partner ids sit above the trainer ids (`TRAINER_PARTNER(n) = MAX_TRAINERS_COUNT + n`), so **no trainer id, no flag, no save change**.
2. **A back-view picture is required.** A partner is drawn from behind. Only ten real pictures in the ROM have a back view (Brendan, May, Red, Leaf, the two Ruby/Sapphire kids, Wally, Steven, the Pokédex kid and the Old Man; `src/data/graphics/trainers.h`). The 15 Veldris pictures are front-only. So Troglodyte needs a **new back pic**: 64x256 four-frame sheet or 64x320 five-frame (the asset repo has `Trainer Back Sprites/Lhea/pt_lucas.png`, a 64x320 Platinum Lucas that could be recoloured; credit row required), plus one picture entry in `include/constants/trainers.h` and `src/data/graphics/trainers.h`. Until then a stand-in (Wally's back view) works and shows the right name and team; the lab used it.
3. **No random starter for partners.** The partner builder reads the block's first N Pokémon in file order and ignores the pool and prune (`FillPartnerParty`, `src/battle_partner.c` 26). So 'one of his three starters' needs **three partner blocks** (one per starter) and the script picks by `VAR_TROG_STARTER`. Costs two more partner entries, nothing else.
4. **Party size.** Without `Multi Party: Half` on the opponents both sides use full parties (up to 6 each; you bring your whole party). With `Multi Party: Half` (as Mossdeep's Maxie and Tabitha have) each side is cut to 3 and you pick 3 (`special ChooseHalfPartyForBattle` before the macro, copied from Mossdeep).
5. **Script:** about 15 lines per fight modelled on Mossdeep: save party, optionally choose three, `multi_2_vs_1`, `switch VAR_RESULT` (win continues; loss `special SetCB2WhiteOut`), and set the opponent's trainer flag by hand (`settrainerflag`; a tag battle does not set it). Both sides must lose all Pokémon for the battle to end (`B_MULTI_BATTLE_WHITEOUT`), so a dim partner can carry or drag.
6. **AI:** the partner thinks with the `AI:` line in its own block (a dim Troglodyte, `Check Bad Move`, plays the 'useless ally' joke for free; `Basic Trainer` makes him competent). The engine ships a scoring helper for tag battles (`AI_TagBattlePreferFoe`, `setdynamicaifunc`) that stops the foes piling onto the same target; optional.
7. **Mid-battle lines** work for a partner too (`[TRAINER_PARTNER(PARTNER_TROGLODYTE)]` key in `veldris_trainer_slides.h`, slot already in `FIRST_TURN_EVENTS_TRAINER_SLIDE_PARTNER`).
8. **Levels do not scale.** The partner's levels are fixed in the block, so write them for that moment in the story.

**Two opponents (for example Troglodyte plus a Goldsworth parent) cost (read, then ran).** Two ordinary blocks with `Multi Party: Half` (else 12 Pokémon against your 6), one script line (`trainerbattle_two_trainers` from an NPC's script, the raw `trainerbattle` form from a cutscene, see risk 4), and a guard that the player has two usable Pokémon first (the macro does **not** check; a one-Pokémon player gets a double battle with one Pokémon). Both trainers' defeated flags are set afterwards, so the Journal tally for Troglodyte still counts. His random starter works (he is an ordinary opponent, pool prune runs). No new art. Mugshot banner follows the first named trainer.

**Fits the story as it stands.** The author already set (2026-10-04) that **the player and Troglodyte fight the Commons leader together** (`design/factions.md`, `design/troglodyte-arc.md` decision 5), which is the tag battle above. The Goldsworth-parents scene at gym 6 (Troglodyte fight 5) is the natural two-opponents candidate. **Placing either in the story is your call (rule 10); this brief only says it is cheap in code.** One art cost (the back picture) and nothing else.

**Risks.** (1) The back picture is the only real work. (2) Thinking time in a tag fight is about double a single fight (8 frames with a Basic foe and a dim partner, ran; upstream allows 24 for two smart foes). (3) Partner blocks need their own `IVs`/`Level` lines (brief 2: the pragma is per file). (4) **`trainerbattle_two_trainers` called from a plain script raised the engine's error screen** ('trainer script that needs to be used from an object event was called from player', `src/battle_setup.c` 1394; in the dev ROM it is a resumable crash screen, in a release build it silently skips a step). It turns the trainer to face the player, so it needs an NPC to talk to. From a cutscene use the raw `trainerbattle` line with `facePlayer` FALSE, `continueScript` TRUE, `skipFlagCheck` TRUE (the last form in lab 8, which worked). (5) Following-NPC partner is a save change, so avoid it.

**Ran (lab, `prototypes/battle_lab.patch`).** Lab 7, tag battle: the player's Swampert, Tropius, Blaziken (level 40) plus `PARTNER_TROGLODYTE` (Lillipup, Eevee, Treecko at 30, `Check Bad Move`, Wally's back view as a stand-in) against DALE. A two-team preview came first; the partner's name showed as 'PKMN TRAINER TROGLODYTE' (his class is Rival, the known class-name caveat); his Lillipup acted by itself (Take Down), the foe fainted, Exp and money came out right, the script carried on. Thinking time on turn 1 was 8 frames (a Basic foe plus the dim partner). Lab 8, two opponents (raw `trainerbattle`): 'You are challenged by YOUNGSTER DALE and GENTLEMAN WREN!', both send out, you send your first two, 8 frames on turn 1.

**Test plan.** (1) Labs above are the first pass. (2) With the real picture: check the partner's back view in the battle intro and in the party preview. (3) Lose on purpose: the white-out path, and the case where only the partner is left. (4) A one-Pokémon player on the two-opponents fight (the guard). (5) Each of the three partner blocks (one per starter) once. (6) Win, then check the opponent's defeated flag and the Journal tally by hand.

**Answer:** `none`, `tag` (Troglodyte as partner only), `both` (tag plus the two-opponents option kept open, my pick: nothing is built now, it only decides that the back picture gets planned).

---

## Files

`briefs.md` (this file). Supporting, not for the repo: `prototypes/battle_lab.patch` (the experiment patch against `8bb23927`, final state = soft cap, seed fight, raw two-opponent line; the hard-cap and macro runs used the two lines it replaced), `lab/*.png` (screenshot sheets quoted above: `ai1` to `ai4`, `cap_hard_and_boost`, `cap_soft`, `stale_boost_wild`, `seed_hachimel`, `tag_battle`, `two_opponents_*`), `lab/emu.sh`, `lab/lab_slow.sh`, `lab/lab_two.sh` (the xdotool driver), `evidence/` (pragma and AI-line test inputs with a README), `build1.log` and `build2.log` (both lab builds passed: 7 min 20 s clean under load, 12 s incremental). Nothing in the repo was changed.
