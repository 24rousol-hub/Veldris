# AI ladder (opponent cleverness)

Status: **the direction was given by the author on 2026-10-12; the rung contents below are my applied reading of it and stay changeable.** Three rungs, deliberately short. The `AI:` lines are data in `src/data/trainers.party`, which exists upstream, so [engine-edits.md](engine-edits.md) has one data-only row for it (no C, header or config change). No new id, no flag or var, no save change.

## The author's words

'Like the starters, short AI ladder weak to better but not crazy good, no level caps,' (2026-10-12, answering items S1, 1 and 3 of [decisions-pending.md](decisions-pending.md)).

- 'Short AI ladder weak to better but not crazy good' is this page.
- 'No level caps' is the last section.
- 'Like the starters' was item S1. It was ambiguous, so the author was asked, and confirmed set A (Johto + Togepi). The starters are not part of this page.

**Not the author's words (my applied reading, changeable):** the three rungs and the flags each holds, `Ace Pokemon` on gym leaders 3 to 9, the League and Cynthia, the per-block mapping, the exclusion of Smart Trainer, Prediction, Omniscient and Smart Switching, and the middle of the Troglodyte plan. The author asked for a short ladder, weak to better, not crazy good, and no level caps. **One Troglodyte answer is the author's (2026-10-13): he should be genuinely sharp**, so he ends on the Sharp rung (see 'Troglodyte' below).

## The three rungs

| Rung | `AI:` line | Feel |
|---|---|---|
| 1 Dim | `AI: Check Bad Move` | Random but sane. It never picks a move that would fail, but it may pick Growl over a strong hit |
| 2 Basic | `AI: Basic Trainer` | `Basic Trainer` is Check Bad Move + Try To Faint + Check Viability. It takes a knockout when it sees one, otherwise the strongest move |
| 3 Sharp | `AI: Basic Trainer / Hp Aware / Try To 2hko` | Basic, and it also heals and sets up at sensible times and goes for two-hit knockouts |

`/ Ace Pokemon` goes on the end for gym leaders 3 to 9, the four Elite Four and Cynthia. So the five full lines in use are:

- `AI: Check Bad Move`
- `AI: Basic Trainer`
- `AI: Basic Trainer / Ace Pokemon`
- `AI: Basic Trainer / Hp Aware / Try To 2hko`
- `AI: Basic Trainer / Hp Aware / Try To 2hko / Ace Pokemon`

Write a line like this, with the flags in this order. `tools/trainerproc` turns the words into `AI_FLAG_*` bits and a typo is a build error, not a silent no-op (it surfaces at the C compile step as an undeclared `AI_FLAG_...`, not in trainerproc itself). The lint compares the written flag names, so order and case do not matter to it, but it does not expand a bundle: write `Basic Trainer`, not its three members `Check Bad Move / Try To Faint / Check Viability` (the unit test compares the real bits, so both spellings pass the test and only the first passes the lint).

## Who sits where (built blocks)

Find each block in `src/data/trainers.party` by its `=== TRAINER_X ===` header.

| Block | Fight | Rung |
|---|---|---|
| `TRAINER_TROGLODYTE_HOLLOWBROOK` | Troglodyte 1, lab door | Dim |
| `TRAINER_TROGLODYTE_CRESTFALL` | Troglodyte 2, gym 1 | Dim |
| `TRAINER_CRESTFALL_GRETA` | Gym 1 | Basic, unchanged, no Ace |
| `TRAINER_HACHIMEL` | Gym 2 | Basic, unchanged, no Ace |
| `TRAINER_SANZUFORD` | Gym 3 | Basic + Ace Pokemon |
| `TRAINER_HAGANE`, `TRAINER_WAKASAGI`, `TRAINER_TOBIN` | Gyms 4, 5, 6 | Sharp + Ace Pokemon |
| `TRAINER_ASEBY`, `TRAINER_SUZURAN`, `TRAINER_MIZZLE` | Gyms 7, 8, 9 | Sharp + Ace Pokemon |
| `TRAINER_OSSIAN`, `TRAINER_HYACINTH`, `TRAINER_DRAYDEN`, `TRAINER_DUNMORE` | Elite Four | Sharp + Ace Pokemon |
| `TRAINER_CYNTHIA` | Champion | Sharp + Ace Pokemon |

That is 14 blocks edited. Greta and Hachimel are not edited but are pinned at Basic by the lint and the unit test (16 rows in all). Not touched and not pinned: Greta's two gym trainers DALE and WREN (`Basic Trainer`) and the three Route 1 trainers (`Check Bad Move`); for them only the allowed-flag check applies.

## Troglodyte, fights not built yet (end state decided, middle PROPOSED)

**Author's answer (2026-10-13): he should be genuinely sharp.** So he is not a pushover at the end: fights 7 and 8 are on the Sharp rung, the top rung of this ladder (the same as the Elite Four and Cynthia). Nothing is built for this yet, because only fights 1 and 2 exist. The rows for fights 3 to 6 are still my plan, not an author answer. When a fight is built, copy its line from this table. **Never Ace Pokemon for Troglodyte** (his party order is random, see 'Why Ace Pokemon'). He always sits at or under the rung of the leader of his time, so he is never smarter than the gym leader he is racing; how hard he is to beat comes from his teams and levels ([troglodyte-arc.md](troglodyte-arc.md)).

**Open, not blocking:** the leaders of gyms 5 to 7 are already Sharp, so fights 4 to 6 could be Sharp too if you want him sharp earlier. Until you say so they stay Basic, as in the table.

| Fight | Where | Leader of his time | Rung |
|---|---|---|---|
| 1 (built) | Outside the lab | none | Dim |
| 2 (built) | Gym 1, Crestfall | Greta, Basic | Dim |
| 3 | Gym 3, Ghost | Sanzuford, Basic | Basic |
| 4 | Gym 5, Ice | Wakasagi, Sharp | Basic |
| 5 | Gym 6, Flying | Tobin, Sharp | Basic |
| 6 | Gym 7, Poison | Aseby, Sharp | Basic |
| 7 | Victory Road | Mizzle, Sharp | Sharp |
| 8 | Finale before Cynthia | Elite Four, Sharp | Sharp |

The fight list and levels are in [troglodyte-arc.md](troglodyte-arc.md). Add each new fight to the table in this page, to the lint table and to the test (see 'Where it is enforced'). The lint already refuses Ace Pokemon on any `TRAINER_TROGLODYTE*` block.

**Not decided:** the rung for Troglodyte as the player's tag-battle partner (a story beat for the author, see [decisions/battle.md](decisions/battle.md) brief 5 and item 5 of [troglodyte-arc.md](troglodyte-arc.md)). Its block would live in `src/data/battle_partners.party`, which the lint table and the test do not cover.

## Why Ace Pokemon

- The flag keeps a trainer's last-listed Pokémon in the back until it is the last one left. Every leader, Elite Four and Cynthia block lists the ace last, so the ace comes out last.
- Without the flag, replacements are chosen by type matchup and damage, not in block order. The last Pokémon out is then whichever the AI leaves, not necessarily the ace (read in the code, `trainer-slide-options/leaders.md` finding 3; not watched in a fight).
- It is data only. It also makes mid-battle lines that name the last Pokémon safe ([trainer-slide-options/](trainer-slide-options/); the wording there is still PROPOSED).
- **Not for Troglodyte.** His party order is random (the pool prune), so the flag would hold back a random Pokémon. If the author ever wants him to have an ace, pin one first with `Tags: Ace`.
- **Not for Greta or Hachimel.** They have two Pokémon each, so the second is always the last. They stay exactly as they are today.

## What 'not crazy good' leaves out

None of these appears in any line above, at any rung:

- **Smart Trainer.** It adds Omniscient (it reads your moves, items and abilities), Smart Switching, Smart Mon Choices, Pp Stall Prevention, Smart Tera and Randomize Switchin.
- **Prediction.** Predict Switch, Predict Incoming Mon and Predict Move.
- **Omniscient** on its own.
- **Smart Switching** on its own. It makes the AI swap on bad matchups (about half the time, `SHOULD_SWITCH_HASBADODDS_PERCENTAGE` 50 in `include/config/ai.h`) and so lengthens fights.

So no opponent reads your moves, guesses your swaps or swaps on a bad matchup. Sharp is the ceiling, even for Cynthia. Her strength is her team.

**Offer for later, not built:** a 4th rung for the League, Sharp plus Smart Switching (`AI: Basic Trainer / Hp Aware / Try To 2hko / Smart Switching`, with Ace Pokemon). Smart Switching pulls in Smart Mon Choices, so any mid-battle line that names the last Pokémon would need a re-check. Only if the author asks.

## How to test

- **The AI is random.** One fight cannot prove a rung. Fight a few times. Dim should now and then pick a weak move such as Growl or Leer. Basic and Sharp should take a knockout when one is on offer. None of the three should swap on a bad matchup.
- **The debug menu 'Try Battle' ignores the block's `AI:` line.** It uses the flags set in its own menu (`gDebugAIFlags`, `src/battle_ai_main.c`, and `GetDebugAiTrainer` in `include/data.h`). Test through a real script fight: talk to the trainer, or play the scenario with the robot player ([tools/emu/README.md](tools/emu/README.md)).
- **Thinking time.** `DEBUG_AI_DELAY_TIMER` (`include/config/debug.h`, FALSE) prints the AI's frames in place of 'What will X do?'. It is a **private-build switch. Never ship it.**
- **Measured in the lab** ([decisions/battle.md](decisions/battle.md), brief 1; mGBA, six against six, first fights, plus or minus one frame; 60 frames = 1 second):

| Rung | Frames at the action prompt | Seconds on a real GBA |
|---|---|---|
| Dim | 3 to 4 | 0.06 |
| Basic | 4 | 0.07 |
| Smart (not used) | 8 | 0.14 |
| Smartest (not used) | 13 | 0.23 |

Sharp was **not measured**. It adds two flags to Basic, so expect it a little above Basic and far below Smart. Read the timer once on a real Sharp fight if it matters.

## Where it is enforced

- `design/tools/trainer_lint.py` has a `LADDER` dict with 16 rows (the 14 edited blocks plus Greta and Hachimel at Basic). The pre-commit hook runs the lint when `src/data/trainers.party`, `battle_ai.h` or `trainer_lint.py` itself is staged. The lint also holds every Veldris-owned block to an allowed-flag list (Check Bad Move, Basic Trainer, Check Viability, Try To Faint, Hp Aware, Try To 2hko, Ace Pokemon, and nothing smarter), requires every Veldris-owned block to have an `AI:` line, and refuses Ace Pokemon on any `TRAINER_TROGLODYTE*` block. DALE, WREN and the Route 1 trio are not in the `LADDER` dict; for them only the allowed-flag and missing-line checks apply.
- `test/veldris.c` has a hack unit test named 'Veldris: AI ladder gives the 16 ladder trainers exactly their rung and no smart flags'. For the same 16 blocks it checks the exact flag bits and that nothing outside the three rungs and Ace Pokemon is set (so no Smart Trainer extras, Prediction, Omniscient, Assume or Know flags). Run it with `make check TESTS='Veldris: AI ladder'` (the filter is a prefix match on the whole test name, so `TESTS='AI ladder'` finds nothing and still exits 0 with 'No tests found'). Built and passed 2026-10-12, and checked to fail when Sanzuford's Ace Pokemon is removed. Two traps: the unit-test build swaps `gTrainers` for a small stub (`test/test_runner_battle.c`), so the test compiles its own copy of the generated `src/data/trainers.h` and reads `aiFlags` from that (`GetTrainerAIFlagsFromId` would only see the stub); and `make` does not re-patch the filter into an existing `pokeemerald-test.elf`, so delete that file (gitignored) before running with a different `TESTS` value.

**If the ladder changes, update this page, the `LADDER` dict and the test together.** A new built block that joins the ladder gets a row in all three, and a data-only row in [engine-edits.md](engine-edits.md) is already there for `trainers.party`.

## Level caps

The author chose **no level caps** (2026-10-12). Nothing is built and no config or C file changes: `include/config/caps.h` is already off (`B_EXP_CAP_TYPE` is `EXP_CAP_NONE`, `B_LEVEL_CAP_TYPE` is `LEVEL_CAP_NONE`, `B_RARE_CANDY_CAP` and `B_LEVEL_CAP_EXP_UP` are FALSE). The table in `src/caps.c` (12, 19, 25, 31, 37, 42, 48, 55, 60, then 75 for the Champion) stays as an inert reference. The aces in [trainer-roster.md](trainer-roster.md) and the Troglodyte level ranges in [troglodyte-arc.md](troglodyte-arc.md) are design targets, not a cap.
