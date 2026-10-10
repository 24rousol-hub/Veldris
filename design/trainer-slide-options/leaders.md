# Gym leader slides: three tone options per leader (PROPOSED)

**ALL TEXT IN THIS FILE IS PROPOSED. Nothing is approved, nothing is wired, and no game file was changed.** It is draft material for the author's pick (CLAUDE.md rules 9 and 10). Scope is the author's of 2026-10-09: mid-battle lines for key battles only, and the nine gym leaders below are in scope. Companion file with every row as ready-to-paste, commented-out C: `veldris_trainer_slides_leaders_COMMENTED.h`. Mechanism, triggers and traps: `design/trainer-slides.md`.

Every line (97 distinct lines: 81 option rows, 7 ACE rows, 9 SCH rows) was run through the game's own line breaker with `design/tools/slide_check.py` and `dialogue_check.py`: all fit two 208 px lines, no scroll, for both a wide and a narrow player name. Output: `slide_check_log.txt`. Lines were also linted for the hack's rules: no real animals, no swearing, no double quotes, curly single quotes only, no `{PLAYER}`, and no TROGLODYTE, Goldsworth, faction or legendary names in any of the 81 option rows (only the nine SCH rows allude to the schemes, without naming the family).

## How to approve

Reply with the leader code and an option letter for each leader, for example **`GRE B, HAC A, SAN A, HAG A, WAK A, TOB B, ASE A, SUZ A, MIZ A`** (that is my recommended set; `all recommended` also works). You can mix by row id (`WAK A, but WAK-B3 instead of WAK-A2`), or say `none` for a leader who should stay silent. Three extra yes/no questions: **(1) `ace`**: add `Ace Pokemon` to the `AI:` line of the seven leaders with three or more Pokémon and allow the ACE rows (a gameplay change, see finding 3); **(2) `callbacks`**: which Goldsworth-scheme rows (`-SCH`) you want, if any (they only make sense once those schemes are canon); **(3)** anything you want reworded. Until you answer, the game is untouched. None of the recommended rows needs the ace flag or any other data change.

## Reading guide

**Row ids.** `GRE-B2` = leader code, option letter, row number. Extra rows end `-ACE` (names the last Pokémon, needs the ace flag) or `-SCH` (calls back to that gym's Goldsworth scheme, a story beat).

**Flags in the tables.** `SS` = the line is tied to the leader's Starting Status (weather or terrain), so re-read it if that status in `src/data/trainers.party` is ever changed. `EX` = a line that already exists as PROPOSED text, reused unchanged (the leader's last stand in `trainer-slides.md`, or `Briarwick_Text_HachimelAce`). `EXM` = an existing line with one word changed. **Option letters** (the tone names differ per leader): **A** is in voice, closest to the pitch and to the existing drafts. **B** is wry and dry, usually back-half lines only. **C** is theatrical, a bigger performance of the same character. Widths in square brackets are pixels per displayed line.

**The six triggers used.** The other 19 (crit, super-effective, STAB, unaffected and gimmick slides) are not used: the end-of-turn ones are easy to lose. One robust trigger that was not in the brief and is not drafted: `ATTACKER_LANDS_FIRST_DOWN`, a gloat when the player's first Pokémon faints. It fires in the faint script like first-down does, so it would suit a leader who wants a taunt.

| Trigger | Plays when | Reliable? | Best used for |
|---|---|---|---|
| `BEFORE_FIRST_TURN` | After both send-outs, after the Starting Status message and ability pop-ups, before the first menu | Yes, once | The entrance. Can joke about the weather or terrain. |
| `DEFENDER_TAKES_FIRST_DOWN` | The instant the leader's first Pokémon faints, before the replacement comes out | Yes, once the player scores one KO | A reaction. Safe to name the lead. |
| `SELF_LAST_SWITCHIN` | When the leader's last Pokémon is sent in after a faint | Yes, if the player gets that far | The ace's entrance. Never fires after a voluntary switch. |
| `OPPONENT_LAST_SWITCHIN` | When the player's last usable Pokémon is sent in after a faint | Only if the player owns two or more | A taunt or pity line. |
| `SELF_LAST_HALF_HP` | End of a turn: the leader's last Pokémon is above 25 percent and at most 50 percent HP | No, a bonus beat | A quiet aside. A big hit can skip it. |
| `SELF_LAST_LOW_HP` | End of a turn: the leader's last Pokémon is alive at 25 percent or less | No, a bonus beat | The closer. A one-hit KO from above skips it. |

No row uses the player's name. If you want one, `{B_PLAYER_NAME}` works (never `{PLAYER}`) and `slide_check.py` measures it at both a wide and a narrow name.

Existing traps still apply (`trainer-slides.md`): one end-of-turn slide per trainer per turn, half and low can never both play on one turn, and each slide plays at most once per battle.

### Findings from reading the source (new, not yet in trainer-slides.md)

1. **The opening line comes after the Starting Status message.** Order in `src/battle_main.c` (`include/battle_main.h:56-61`): weather, terrain, starting status, totem boosts, switch-in abilities, fainted-at-start, then the trainer slide. So a line like ‘Ha! Rain.’ or ‘Mind the sparks.’ lands right after the game prints ‘It started to rain!’ or ‘An electric current ran across the battlefield!’. Those rows are marked `SS`.
2. **A two-Pokémon leader plays first-down and last-send-in back to back.** First down fires inside the faint script (`data/battle_scripts_1.s:2727`), last send-in fires right after the replacement's entrance animation (`:2803`). For GRETA and HACHIMEL the player sees two slides within a few seconds. HAC option A is written as a deliberate pair (‘I'm so sorry’ twice), GRE option A as thank-then-tip, and B and C avoid it by using only one of the two.
3. **A leader's replacements do not come out in party order, so only the lead is safe to name.** After a faint the AI picks the next Pokémon with `GetMostSuitableMonToSwitchInto` (`src/battle_ai_switch.c:2607`, called from `src/battle_controller_opponent.c:539`). Without `AI_FLAG_SMART_MON_CHOICES` that is `GetBestMonVanilla`: Baton Pass, then a type-matchup pick, then best damage, with the last-listed Pokémon held back only when `AI_FLAG_ACE_POKEMON` is set. The leaders have `AI: Basic Trainer` (`Check Bad Move / Try To Faint / Check Viability`), which has no ace flag, and `Smart Trainer` does not add one either. So for any leader with three or more Pokémon the last one to come out is whichever the AI leaves, not necessarily the ace in the block. **Every recommended row therefore either names only the lead (first-down and opening lines, the lead is always sent first) or says nothing species-specific on the last send-in.** The ACE rows name the ace; they are only correct after `Ace Pokemon` is added to that leader's `AI:` line (data only, no engine change; `tools/trainerproc` turns the words into `AI_FLAG_ACE_POKEMON`). Found by reading the code, not by watching a fight. GRETA and HACHIMEL are exempt: with two Pokémon the second is always the last.
4. **Rare exception on the lead.** The AI could in theory switch its lead out before it faints (Perish Song and similar). Then ‘first down’ would be a different Pokémon and a line like ‘BRONZOR's down’ would be wrong once. Not worth designing around, noted for honesty.

## At a glance: my recommended set

| Code | Leader | Gym and town | Team | Rec | Rows in the recommended option | Needs ace flag or data edit |
|---|---|---|---|---|---|---|
| GRE | GRETA | Gym 1, Crestfall (town), Normal, STANDARD BADGE | SKITTY 10 (lead), MILTANK 12 (ace, Oran Berry) (2) | **B** | Last send-in (B1), Player's last (B2), Last stand (B3) | no |
| HAC | HACHIMEL | Gym 2, Briarwick (city), Bug, HUSK BADGE | KRICKETUNE 17 (lead), VIVILLON 19 (ace) (2) | **A** | Opening (A1), First down (A2), Last send-in (A3) | no |
| SAN | SANZUFORD | Gym 3, Gloomsby (town), Ghost, WISP BADGE | SHUPPET 23 (lead), LITWICK 24, MIMIKYU 25 (ace) (3) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |
| HAG | HAGANE | Gym 4, Smeltham (town, foundry), Steel, RIVET BADGE | BRONZOR 29 (lead), PAWNIARD 30, TINKATUFF 31 (ace) (3) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |
| WAK | WAKASAGI | Gym 5, Hoarfell (city, frozen lake), Ice, FROST BADGE | SNEASEL 35 (lead), VANILLISH 36, LAPRAS 37, AVALUGG 37 (ace) (4) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |
| TOB | TOBIN | Gym 6, Gildhaven (skyscraper city), Flying, FEATHER BADGE (and HM Fly) | SWELLOW 40 (lead), UNFEZANT 41, TALONFLAME 41, CORVIKNIGHT 42 (ace) (4) | **B** | Opening (B1), Player's last (B2), Last stand (B3) | no |
| ASE | ASEBY | Gym 7, Hemlock Reach (town), Poison, VIAL BADGE | WEEZING 46 (lead), CROBAT 47, DRAPION 47, GARBODOR 47, TOXAPEX 48 (ace) (5) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |
| SUZ | SUZURAN | Gym 8, Primrose Vale (city), Fairy, CHARM BADGE | AZUMARILL 52 (lead), DACHSBUN 52, RIBOMBEE 53, HATTERENE 54, GARDEVOIR 55 (ace) (5) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |
| MIZ | MIZZLE | Gym 9, Beaconmouth (town, flooded lighthouse), Water, TIDE BADGE | GYARADOS 58 (lead), SEISMITOAD 58, ARAQUANID 59, BARRASKEWDA 59, LANTURN 59, MILOTIC 60 (ace) (6) | **A** | Opening (A1), First down (A2), Last stand (A3) | no |

**If you only read ten lines**, these are my favourites (row id, leader, line):

- **MIZ-A2** (MIZZLE, option A, `DEFENDER_TAKES_FIRST_DOWN`): GYARADOS is down. Fine. I once lost a pier. This is manageable.
- **SAN-A1** (SANZUFORD, option A, `BEFORE_FIRST_TURN`): Don't worry, the twisting wears off. Unlike my usual clients.
- **HAG-A1** (HAGANE, option A, `BEFORE_FIRST_TURN`): Mind the sparks. The safety inspector's at lunch. So is everyone.
- **TOB-B3** (TOBIN, option B, `SELF_LAST_LOW_HP`): Mayday, mayday. Sorry, I've always wanted to say that.
- **SUZ-B2** (SUZURAN, option B, `OPPONENT_LAST_SWITCHIN`): Your last one? How brave. I do press the brave ones in books.
- **GRE-B1** (GRETA, option B, `SELF_LAST_SWITCHIN`): Meet MILTANK. Everyone remembers her. Nobody enjoys it.
- **WAK-B3** (WAKASAGI, option B, `SELF_LAST_HALF_HP`): Half already? Here, hold my thermos. Careful, it's hot.
- **ASE-C3** (ASEBY, option C, `SELF_LAST_LOW_HP`): Fascinating. I appear to be losing. I must write this down.
- **HAC-B3** (HACHIMEL, option B, `SELF_LAST_LOW_HP`): Sorry, VIVILLON. Sorry, grass. Sorry, hives. Sorry, floor.
- **SUZ-A2** (SUZURAN, option A, `DEFENDER_TAKES_FIRST_DOWN`): You're being so gentle with us. How kind. You can stop now.

Pick an option for a leader because of its tone. Every option plays at least one beat that is certain to appear (opening, first faint or last send-in); the others are bonus or conditional beats.

---

## 1. GRETA (GRE): Gym 1, Crestfall (town), Normal, STANDARD BADGE

- **Constant:** `TRAINER_CRESTFALL_GRETA`
- **Team:** SKITTY 10 (lead), MILTANK 12 (ace, Oran Berry). Two Pokémon.
- **Starting Status:** none (the first gym stays plain)
- **Voice:** Young, confident, a tad sassy, kind underneath (characters.md). She sees through the Goldsworths at once and loves being underestimated: ‘I look too young. I get that a lot. Usually right before I win.’ Her field lines already say ‘Try to keep up. No pressure.’ and ‘Normal is reliable. Flashy gets you a cool entrance. Reliable gets you badges.’ The gym is a farmyard with a hay maze and MILTANK ‘like a big, pink stove’. No farm link (author, 2026-10-08): she was posted here, so no ‘my farm’ or ‘my barn’. Clean, no swearing.
- **Existing PROPOSED baseline:** Oh, you're actually good. Don't let it go to your head, sweetheart!  (existing PROPOSED last stand, trainer-slides.md. Reworded in GRE-B3: ‘sweetheart’ reads as patronising from someone this young.)

**Which trigger fits which beat, for this leader**

- **Two Pokémon means two beats land together.** `DEFENDER_TAKES_FIRST_DOWN` fires the moment SKITTY faints and `SELF_LAST_SWITCHIN` fires when MILTANK is sent in a few seconds later, so the player sees two Greta slides back to back. Option A is written as a deliberate pair (thank SKITTY, then the tip). Options B and C use only the send-in.
- `SELF_LAST_SWITCHIN` is guaranteed for a two-Pokémon leader (MILTANK is the only one left), so it carries the line that must always show. It names MILTANK safely.
- `OPPONENT_LAST_SWITCHIN` needs a player with two or more Pokémon who sends in the last one after a faint. Most gym 1 players qualify, but it can miss.
- `SELF_LAST_LOW_HP` is the bonus beat: MILTANK at a quarter or less at the end of a turn. A one-hit KO from higher up skips it.
- No `BEFORE_FIRST_TURN` in A and B on purpose: her field intro (‘Try to keep up. No pressure.’) already opens the fight. Option C uses one because the showgirl act needs an opening.

**Option A: Warm coach.** Kind underneath, and it teaches the player the Rollout trap. Closest to the field drafts.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| GRE-A1 | `DEFENDER_TAKES_FIRST_DOWN` | SKITTY, you were lovely. Go and nap in the hay. | [139/97] |
| GRE-A2 | `SELF_LAST_SWITCHIN` | Free tip, since it's gym one: MILTANK rolls harder every turn. | [188/123] |
| GRE-A3 | `SELF_LAST_LOW_HP` | Between us, I'm proud of you. Don't tell MILTANK. She'd want a raise. | [179/167] |

**Option B: Sassy.** The ‘tad sassy but nice’ version. Short, quotable, nothing taught.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| GRE-B1 | `SELF_LAST_SWITCHIN` | Meet MILTANK. Everyone remembers her. Nobody enjoys it. | [177/113] |
| GRE-B2 | `OPPONENT_LAST_SWITCHIN` | Your last one? No pressure. ...Okay, a little pressure. | [181/91] |
| GRE-B3 | `SELF_LAST_LOW_HP` | Oh, you're actually good. Don't let it go to your head, hotshot! `EXM` | [176/145] |

**Option C: Showgirl.** She preaches ‘reliable’ and then stages a big entrance anyway. The joke is the contradiction.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| GRE-C1 | `BEFORE_FIRST_TURN` | Ladies, gentlemen and hay bales: welcome to the main event! | [168/138] |
| GRE-C2 | `SELF_LAST_SWITCHIN` | Lights! Music! Roll out the big, pink stove: MILTANK! | [160/107] |
| GRE-C3 | `SELF_LAST_LOW_HP` | This is where I stage my comeback. Watch closely. I'm very good. | [178/148] |

**Recommended: option B.** B is the sassy-but-nice Greta in three short lines. GRE-B1 is the best single line of the three options and GRE-B2 calls back to her own ‘No pressure.’ GRE-B3 keeps the existing last stand with one word swapped. Pick A instead if you want the first gym to teach: it is the only option that explains Rollout. B is back-half only (nothing before MILTANK appears), which suits a first gym that should not talk over the tutorial.

**Optional extras (not in the recommended set)**

- **STORY row (`GRE-SCH`), needs the author:** calls back to Scheme 1 (consultants, hay maze, MILTANK eat the paperwork). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `SELF_LAST_SWITCHIN`. It would replace GRE-B1.

  > Meet MILTANK. She ate a consultant's whole report this week.  [193/120]

---

## 2. HACHIMEL (HAC): Gym 2, Briarwick (city), Bug, HUSK BADGE

- **Constant:** `TRAINER_HACHIMEL`
- **Team:** KRICKETUNE 17 (lead), VIVILLON 19 (ace). Two Pokémon.
- **Starting Status:** Grassy Terrain, Temporary (the game prints ‘Grass grew to cover the battlefield!’ before the first-turn slide)
- **Voice:** Young beekeeper in a veil, gentle, oddly formal, and she apologises to every Bug she sends out. The apology is the joke engine: she is sorry for everything, including winning. Field draft: ‘KRICKETUNE, I'm sorry. Do go on. Play something brave.’ A gym trainer says the apologies make the Pokémon ‘try harder. Out of guilt, I think.’ Never says the real animal word for her trade: she says hives, APIARY, honey, Bug types.
- **Existing PROPOSED baseline:** Oh dear. I'm so sorry, little one. Just a little longer, please.  (existing PROPOSED last stand). Also existing in dialogue/briarwick.inc as `Briarwick_Text_HachimelAce`: ‘VIVILLON, I'm so sorry. It's your turn. Do be elegant.’ That draft is reused as HAC-A3 so it can double as the slide (drop the field copy if A is picked).

**Which trigger fits which beat, for this leader**

- **Two Pokémon: first-down and last-switch-in play back to back.** In option A the pair reads as a running gag (‘I'm so sorry’ twice in a row). This is the best fit of all nine leaders for the pairing.
- `BEFORE_FIRST_TURN` plays after the Grassy Terrain message, so a line about the grass lands right on cue. If the Starting Status line in trainers.party is ever changed, rows marked SS need a re-read.
- `OPPONENT_LAST_SWITCHIN` is the polite-menace slot: she apologises to the player for what is about to happen.
- `SELF_LAST_LOW_HP` watches VIVILLON, the only Pokémon left, at a quarter HP or less. It is a bonus beat: a big hit from higher up skips it.

**Option A: Gentle apology (in voice).** Straight from the pitch. The repeated apology is the gag.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAC-A1 | `BEFORE_FIRST_TURN` | Please forgive the grass. It gets terribly keen around guests. `SS` | [174/149] |
| HAC-A2 | `DEFENDER_TAKES_FIRST_DOWN` | Oh, KRICKETUNE, I'm so sorry. You played beautifully. | [148/121] |
| HAC-A3 | `SELF_LAST_SWITCHIN` | VIVILLON, I'm so sorry. It's your turn. Do be elegant. `EX` | [168/102] |

**Option B: Polite menace.** She apologises in advance, then keeps winning. Same character, a shade colder. No opening line.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAC-B1 | `DEFENDER_TAKES_FIRST_DOWN` | KRICKETUNE did its best. I'm sorry in advance: VIVILLON is better. | [190/150] |
| HAC-B2 | `OPPONENT_LAST_SWITCHIN` | Is that your last one? I'm terribly sorry. I'll be quick. | [180/100] |
| HAC-B3 | `SELF_LAST_LOW_HP` | Sorry, VIVILLON. Sorry, grass. Sorry, hives. Sorry, floor. | [154/132] |

**Option C: Ceremonial.** Grand formal speeches delivered with total sincerity by someone who cannot raise her voice.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAC-C1 | `BEFORE_FIRST_TURN` | By the honour of the APIARY, I regret everything that follows. | [195/128] |
| HAC-C2 | `SELF_LAST_SWITCHIN` | Hush, hives. VIVILLON takes the floor, and I take full responsibility. | [199/158] |
| HAC-C3 | `SELF_LAST_LOW_HP` | It is said the gentle inherit the meadow. Not today, apparently. | [169/159] |

**Recommended: option A.** A plays an opening line, a first-faint line and the last send-in, so she is present from turn one to the end. The grass line (HAC-A1) uses the Starting Status the author already liked, and HAC-A3 is a line she already has. If you want a last-stand row too, HAC-B3 (‘Sorry, floor.’) is the best joke in her set: swap it for A1.

**Optional extras (not in the recommended set)**

- **STORY row (`HAC-SCH`), needs the author:** calls back to Scheme 2 (the fumigation tent). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace HAC-A1.

  > I did apologise to the tent, afterwards. It looked so crumpled.  [144/179]

---

## 3. SANZUFORD (SAN): Gym 3, Gloomsby (town), Ghost, WISP BADGE

- **Constant:** `TRAINER_SANZUFORD`
- **Team:** SHUPPET 23 (lead), LITWICK 24, MIMIKYU 25 (ace). Three Pokémon.
- **Starting Status:** Trick Room, Temporary (the game prints a dimensions-twisted message before the first-turn slide)
- **Voice:** Teenage mortician's apprentice, dry and unbothered, ‘thinks the dead are the better audience’. The town sign says ‘We do the dead right.’ Her mother jokes she will finally tidy her room. The humour is service-industry deadpan: clients, appointments, euphemisms, bookings. Never spooky for its own sake.
- **Existing PROPOSED baseline:** Huh. The living put up more of a fight than I was told.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `DEFENDER_TAKES_FIRST_DOWN` names SHUPPET, the lead. That is safe: the lead is always the first Pokémon listed in the block.
- With three Pokémon there is a gap between first-down and last-switch-in, so both can be used without a back-to-back.
- `SELF_LAST_SWITCHIN` is written generically (‘my last one’). Naming MIMIKYU there is only safe once the block gets `Ace Pokemon` (see finding 3 at the top and the ACE row below).
- `BEFORE_FIRST_TURN` follows the Trick Room message (‘The dimensions were twisted!’), so a line about the twisting wearing off lands on cue.

**Option A: Dry apprentice (in voice).** The mortician's-apprentice voice, with her existing last stand.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SAN-A1 | `BEFORE_FIRST_TURN` | Don't worry, the twisting wears off. Unlike my usual clients. `SS` | [185/122] |
| SAN-A2 | `DEFENDER_TAKES_FIRST_DOWN` | SHUPPET is resting. We never say ‘fainted’. Bad for business. | [168/142] |
| SAN-A3 | `SELF_LAST_LOW_HP` | Huh. The living put up more of a fight than I was told. `EX` | [152/122] |

**Option B: Service-industry deadpan.** She runs the fight like an appointment book.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SAN-B1 | `OPPONENT_LAST_SWITCHIN` | That's your last one? Don't worry. I'll keep it tasteful. | [175/109] |
| SAN-B2 | `SELF_LAST_SWITCHIN` | My last one. Try to be a good audience. The dead usually are. | [199/109] |
| SAN-B3 | `SELF_LAST_LOW_HP` | Ugh, this is running late. I've got a funeral at four. | [153/113] |

**Option C: Gothic ham.** Funeral-service language played big, as if she wished she had a bigger room.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SAN-C1 | `BEFORE_FIRST_TURN` | Dearly beloved, we are gathered to watch you lose. Refreshments after. | [179/188] |
| SAN-C2 | `DEFENDER_TAKES_FIRST_DOWN` | A moment of silence for SHUPPET. ...That's enough. Moving on. | [169/139] |
| SAN-C3 | `SELF_LAST_LOW_HP` | Wait! I haven't finished the eulogy! Give me a minute here! | [186/113] |

**Recommended: option A.** SAN-A1 is the best first-turn line in the whole set (it uses the Trick Room), SAN-A2 is the euphemism that makes the character, and SAN-A3 is the line the author has already seen. SAN-A3 is the only A row that may not show; if you prefer a guaranteed closer, swap in SAN-B2 (‘a good audience’), the best last-send-in line in her set.

**Optional extras (not in the recommended set)**

- **ACE row (`SAN-ACE`)** names MIMIKYU on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > MIMIKYU's shy. Be kind to the costume. It's all it has.  [151/123]
- **STORY row (`SAN-SCH`), needs the author:** calls back to Scheme 3 (frat guys in sheets, a real HAUNTER joins in). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace SAN-A1.

  > A real ghost took the boys' sheets. I call that peer review.  [183/121]

---

## 4. HAGANE (HAG): Gym 4, Smeltham (town, foundry), Steel, RIVET BADGE

- **Constant:** `TRAINER_HAGANE`
- **Team:** BRONZOR 29 (lead), PAWNIARD 30, TINKATUFF 31 (ace). Three Pokémon.
- **Starting Status:** Electric Terrain, Temporary (the game prints ‘An electric current ran across the battlefield!’ before the first-turn slide)
- **Voice:** Middle-aged (the pitch; the dialogue should not give an age) foundry foreman, exhausted and very patient. His workers are always at lunch: the gym sign reads ‘Workers are at lunch. Back at one. Probably.’ The humour is gentle labour comedy: shifts, forms, overtime, the lads who are never there. He never snaps.
- **Existing PROPOSED baseline:** Lads, a hand? ...Lunch. Of course. Right, I'll manage.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the Electric Terrain message: the ‘mind the sparks’ line lands right after the game says there is a current across the floor.
- `DEFENDER_TAKES_FIRST_DOWN` names BRONZOR, the lead (safe).
- `SELF_LAST_SWITCHIN` is generic (‘my last one … on shift since six’). Naming TINKATUFF needs `Ace Pokemon` first (the ACE row below).
- `SELF_LAST_HALF_HP` (option B) is a good slot for the paperwork joke because it fires once, quietly, while the fight goes on.

**Option A: Tired foreman (in voice).** The pitch as written, with his existing last stand.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAG-A1 | `BEFORE_FIRST_TURN` | Mind the sparks. The safety inspector's at lunch. So is everyone. `SS` | [144/190] |
| HAG-A2 | `DEFENDER_TAKES_FIRST_DOWN` | BRONZOR's down. It's built like a manhole cover. It'll be fine. | [166/144] |
| HAG-A3 | `SELF_LAST_LOW_HP` | Lads, a hand? ...Lunch. Of course. Right, I'll manage. `EX` | [170/93] |

**Option B: Paperwork deadpan.** Labour comedy: shifts, cover, incident forms. A near tie with A.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAG-B1 | `OPPONENT_LAST_SWITCHIN` | Last one, is it? Take five. I would, if anyone covered my shift. | [178/142] |
| HAG-B2 | `SELF_LAST_SWITCHIN` | That's my last one. It's been on shift since six. Please be gentle. | [194/142] |
| HAG-B3 | `SELF_LAST_HALF_HP` | That's half. I'll need an incident report. I'll fill it in myself. | [170/144] |

**Option C: Foundry boom.** He tries a rousing speech. The room does not help.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| HAG-C1 | `BEFORE_FIRST_TURN` | Behold! Forty years of iron, sweat and unpaid overtime! | [177/107] |
| HAG-C2 | `DEFENDER_TAKES_FIRST_DOWN` | Strike while the iron's hot, I always say. Nobody ever listens. | [186/130] |
| HAG-C3 | `SELF_LAST_LOW_HP` | Everything I've got! Hammer and tongs! Don't tell the union. | [165/142] |

**Recommended: option A.** HAG-A1 (‘So is everyone.’) is the strongest line he has, HAG-A2 makes BRONZOR specific, and HAG-A3 is the existing gag. Option B is a near tie and funnier in the back half (HAG-B2 and HAG-B3), but has nothing before the last send-in; if you like B better, say so, it is a fine pick.

**Optional extras (not in the recommended set)**

- **ACE row (`HAG-ACE`)** names TINKATUFF on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > TINKATUFF, you're on. Bring your own hammer. The lads took ours to lunch.  [187/186]
- **STORY row (`HAG-SCH`), needs the author:** calls back to Scheme 4 (hard hats, the crane, the neat cube with a receipt). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace HAG-A1.

  > Did you see the cube out front? It came with a receipt. I'm keeping it.  [180/180]

---

## 5. WAKASAGI (WAK): Gym 5, Hoarfell (city, frozen lake), Ice, FROST BADGE

- **Constant:** `TRAINER_WAKASAGI`
- **Team:** SNEASEL 35 (lead), VANILLISH 36, LAPRAS 37, AVALUGG 37 (ace). Four Pokémon.
- **Starting Status:** Snow, Temporary (the game prints ‘It started to snow!’ before the first-turn slide)
- **Voice:** Old fisherman, very relaxed, who left the ice-fishing hole for the battle and brought a thermos. The gym sign says ‘Mind the ice. It minds you.’ Time is not a thing he owns. Only fishing words (bite, line, hole, patience): no animal is ever named. The thermos is his running prop.
- **Existing PROPOSED baseline:** Now that's a bite. Hold on while I pour a cup first.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the snow message, so ‘Ah, snow’ lands right after the game says it started to snow.
- `DEFENDER_TAKES_FIRST_DOWN` names SNEASEL, the lead (safe).
- `SELF_LAST_SWITCHIN` is generic. The better joke (AVALUGG, the iceberg, ‘slow to get going’) needs `Ace Pokemon` (the ACE row below).
- He is the slowest talker in the set, so keep his rows few and let the thermos do the work.

**Option A: Unhurried (in voice).** Everything is slow and fine. Closest to his pitch and his existing last stand.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| WAK-A1 | `BEFORE_FIRST_TURN` | Ah, snow. Lovely. Take your time. Nobody hurries on a lake. `SS` | [166/129] |
| WAK-A2 | `DEFENDER_TAKES_FIRST_DOWN` | SNEASEL's down. Fair enough. I'd sit, but the whole floor is ice. | [187/135] |
| WAK-A3 | `SELF_LAST_LOW_HP` | Now that's a bite. Hold on while I pour a cup first. `EX` | [160/95] |

**Option B: Wry angler.** Patience as a weapon, and the thermos as a prop.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| WAK-B1 | `OPPONENT_LAST_SWITCHIN` | Last one, eh? Good. I've waited all winter for a proper bite. | [177/127] |
| WAK-B2 | `SELF_LAST_SWITCHIN` | This is my last, and it's in no hurry. Neither am I. | [149/100] |
| WAK-B3 | `SELF_LAST_HALF_HP` | Half already? Here, hold my thermos. Careful, it's hot. | [186/88] |

**Option C: Storyteller.** He keeps almost telling a story. Every row starts one he does not finish.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| WAK-C1 | `BEFORE_FIRST_TURN` | Did I ever tell you about the winter the lake froze twice? No? Later. | [185/168] |
| WAK-C2 | `DEFENDER_TAKES_FIRST_DOWN` | That reminds me of a story. It's long. We'll do it afterwards. | [164/143] |
| WAK-C3 | `SELF_LAST_LOW_HP` | This reminds me of the Great Frost. I lost that one too. | [182/103] |

**Recommended: option A.** A gives him an opening line, a first-faint line and the existing last stand, all in his slow voice. WAK-B3 (hand the thermos to the player) is the funniest thing he could do: swap it for A2, the weakest A row. WAK-B2 (‘Neither am I.’) is the best guaranteed closer.

**Optional extras (not in the recommended set)**

- **ACE row (`WAK-ACE`)** names AVALUGG on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > AVALUGG's slow to get going. Lucky I've got all day.  [146/116]
- **STORY row (`WAK-SCH`), needs the author:** calls back to Scheme 5 (flags in the lake, ‘angling rights’, the crew sold soup). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace WAK-A1.

  > A fellow bought the ‘angling rights’ to this lake. Then I sold him soup.  [199/160]

---

## 6. TOBIN (TOB): Gym 6, Gildhaven (skyscraper city), Flying, FEATHER BADGE (and HM Fly)

- **Constant:** `TRAINER_TOBIN`
- **Team:** SWELLOW 40 (lead), UNFEZANT 41, TALONFLAME 41, CORVIKNIGHT 42 (ace). Four Pokémon.
- **Starting Status:** Tailwind on his side, Temporary (the game prints the tailwind message before the first-turn slide)
- **Voice:** Young pilot in a leather jacket, dry, a little vain, never raises his voice. He calls the battle a flight plan. The humour is aviation: tailwind, boarding, runway, seat belts, mayday, cleared for landing. The word for a flying animal is never used (only Pokémon names). Vanity is understated: hair, paint, the jacket.
- **Existing PROPOSED baseline:** A little turbulence. Do keep your seat belts fastened.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the tailwind message, so ‘Good tailwind today’ lands on cue.
- `DEFENDER_TAKES_FIRST_DOWN` names SWELLOW, the lead (safe).
- `SELF_LAST_SWITCHIN` is generic (‘last flight of the day’). Naming CORVIKNIGHT needs `Ace Pokemon` (the ACE row below).
- Gym 6 is also where the town doc stages the Goldsworth parents' gift-basket scene before the fight. None of the recommended rows touches it; only the SCH row below does.

**Option A: Calm captain (in voice).** Reassuring announcements. His existing last stand is the closer.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| TOB-A1 | `BEFORE_FIRST_TURN` | Good tailwind today. Expected flight time: short. `SS` | [156/95] |
| TOB-A2 | `DEFENDER_TAKES_FIRST_DOWN` | SWELLOW is grounded. A minor delay. Please remain seated. | [181/112] |
| TOB-A3 | `SELF_LAST_LOW_HP` | A little turbulence. Do keep your seat belts fastened. `EX` | [170/109] |

**Option B: Wry safety demo.** Airline-safety deadpan, applied to losing.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| TOB-B1 | `BEFORE_FIRST_TURN` | In the unlikely event of defeat, remain seated. Weeping is allowed. | [168/175] |
| TOB-B2 | `OPPONENT_LAST_SWITCHIN` | Final approach, then. I'll hold the runway. Do land stylishly. | [175/132] |
| TOB-B3 | `SELF_LAST_LOW_HP` | Mayday, mayday. Sorry, I've always wanted to say that. | [176/102] |

**Option C: Vain showman.** The vanity version: hair, paint, and a dry loss.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| TOB-C1 | `BEFORE_FIRST_TURN` | Pardon the breeze. My hair took forty minutes and I'm not redoing it. `SS` | [195/158] |
| TOB-C2 | `SELF_LAST_SWITCHIN` | Last flight of the day. Mind the paint, it's freshly waxed. | [165/131] |
| TOB-C3 | `SELF_LAST_LOW_HP` | Fine. You win this approach. I'd like it noted my hair held up. | [184/125] |

**Recommended: option B.** TOB-B1 and TOB-B3 are the two best jokes in his set and fit ‘never raises his voice’ exactly: a calm safety announcement about his own defeat. TOB-B2 is the weakest row and is easy to swap for TOB-C2. Pick A for the safe, in-voice version (it uses the tailwind and the existing line), or C for the funniest opener (TOB-C1).

**Optional extras (not in the recommended set)**

- **ACE row (`TOB-ACE`)** names CORVIKNIGHT on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > CORVIKNIGHT, you're cleared for takeoff. And for landing. On them.  [166/175]
- **STORY row (`TOB-SCH`), needs the author:** calls back to Scheme 6 (the parents' gift basket, the sincere tip). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace TOB-B1.

  > I've been tipped to lose today. I declined. Kindly. Twice.  [161/128]

---

## 7. ASEBY (ASE): Gym 7, Hemlock Reach (town), Poison, VIAL BADGE

- **Constant:** `TRAINER_ASEBY`
- **Team:** WEEZING 46 (lead), CROBAT 47, DRAPION 47, GARBODOR 47, TOXAPEX 48 (ace). Five Pokémon.
- **Starting Status:** Toxic Spikes on the player's side, one layer (the game prints the poison-spikes message before the first-turn slide)
- **Voice:** Chemist who reads the ingredients on everything and treats a battle as quality control: ‘a clipboard for every move’. The art is a young man, so no age is given. The humour is lab-and-factory deadpan: batch, sample, tolerance, control, data point, ‘please hold’. Precise, polite, mildly alarming.
- **Existing PROPOSED baseline:** This batch is outside tolerance. Please hold while I rework it.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the toxic spikes message, so a line about having ‘pre-treated’ the player's side lands on cue. Nothing here blames the player: the spikes are his own standard procedure.
- `DEFENDER_TAKES_FIRST_DOWN` names WEEZING, the lead (safe).
- With five Pokémon first-down and last-switch-in are far apart, so both are used in different options without feeling repeated.
- `SELF_LAST_SWITCHIN` is generic (‘final sample’). Naming TOXAPEX needs `Ace Pokemon` (the ACE row below).

**Option A: Clipboard (in voice).** The pitch as written, with his existing last stand.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| ASE-A1 | `BEFORE_FIRST_TURN` | Pre-treated your side of the floor. Standard procedure. You're welcome. `SS` | [184/186] |
| ASE-A2 | `DEFENDER_TAKES_FIRST_DOWN` | WEEZING: failed. Logging it. Next sample, please. | [142/104] |
| ASE-A3 | `SELF_LAST_LOW_HP` | This batch is outside tolerance. Please hold while I rework it. `EX` | [168/150] |

**Option B: Data-point dry.** Every beat is a note in a lab book.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| ASE-B1 | `OPPONENT_LAST_SWITCHIN` | That's your last one. Good. I only need one more data point. | [172/132] |
| ASE-B2 | `SELF_LAST_SWITCHIN` | Final sample, and strictly speaking, the one that works. | [185/101] |
| ASE-B3 | `SELF_LAST_HALF_HP` | Half. That's within tolerance. Barely. I'll note it. | [153/99] |

**Option C: Mad chemist.** The clipboard man lets the lab-coat showman out. Louder, a little unhinged.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| ASE-C1 | `BEFORE_FIRST_TURN` | Behold: science! Please don't touch the floor, the walls, or me. | [184/136] |
| ASE-C2 | `DEFENDER_TAKES_FIRST_DOWN` | A failed trial! Wonderful! Failure is just data wearing a hat. | [171/138] |
| ASE-C3 | `SELF_LAST_LOW_HP` | Fascinating. I appear to be losing. I must write this down. | [180/118] |

**Recommended: option A.** A plays three consistent quality-control jokes from turn one: the spikes line follows the game's own message, ASE-A2 is a one-line version of the pitch, and ASE-A3 is the line the author has seen. Best swaps: ASE-C3 (‘I must write this down.’) is his best last stand, and ASE-B1 (‘one more data point’) is his best taunt.

**Optional extras (not in the recommended set)**

- **ACE row (`ASE-ACE`)** names TOXAPEX on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > TOXAPEX is the control sample. The rest were to make it look good.  [179/159]
- **STORY row (`ASE-SCH`), needs the author:** calls back to Scheme 7 (hazmat inspectors, 47 violations written in advance). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace ASE-A1.

  > Forty-seven violations, written in advance. I respect the efficiency.  [180/181]

---

## 8. SUZURAN (SUZ): Gym 8, Primrose Vale (city), Fairy, CHARM BADGE

- **Constant:** `TRAINER_SUZURAN`
- **Team:** AZUMARILL 52 (lead), DACHSBUN 52, RIBOMBEE 53, HATTERENE 54, GARDEVOIR 55 (ace). Five Pokémon.
- **Starting Status:** Misty Terrain, Temporary (the game prints ‘Mist swirled around the battlefield!’ before the first-turn slide)
- **Voice:** Young florist, much tougher than she looks, who ‘pretends not to notice that everyone underestimates her’. Her gym trainers are enormous and she is smaller than all of them (a fake-out the guide warns about). Her name is lily of the valley: pretty and poisonous. Polite menace in gardening words: prune, bloom, press, perennial, thorn, wilt, lawn. Never raises her voice.
- **Existing PROPOSED baseline:** I do wear flowers. I also have thorns. Sorry!  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the mist message, so ‘Mist is lovely, isn't it?’ lands on cue.
- `DEFENDER_TAKES_FIRST_DOWN` is the best slot for the ‘pretends not to notice’ gag, because it is the first time the player has visibly won something: SUZURAN thanks them for being ‘gentle’.
- `SELF_LAST_SWITCHIN` is generic. Naming GARDEVOIR needs `Ace Pokemon` (the ACE row below).
- `OPPONENT_LAST_SWITCHIN` suits her quiet menace (‘I press the brave ones in books’).

**Option A: Sweet and sincere (in voice).** The pitch as written: sweet, untroubled, quietly sharp. Her existing last stand closes it.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SUZ-A1 | `BEFORE_FIRST_TURN` | Mist is lovely, isn't it? It hides the thorns. `SS` | [135/90] |
| SUZ-A2 | `DEFENDER_TAKES_FIRST_DOWN` | You're being so gentle with us. How kind. You can stop now. | [179/118] |
| SUZ-A3 | `SELF_LAST_LOW_HP` | I do wear flowers. I also have thorns. Sorry! `EX` | [126/100] |

**Option B: Gardener's dry.** Everything is a gardening metaphor said with a smile.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SUZ-B1 | `DEFENDER_TAKES_FIRST_DOWN` | Pruned already! Don't worry, things grow back stronger. | [182/102] |
| SUZ-B2 | `OPPONENT_LAST_SWITCHIN` | Your last one? How brave. I do press the brave ones in books. | [187/126] |
| SUZ-B3 | `SELF_LAST_LOW_HP` | Cut me down and I come back every spring. That's perennials, dear. | [176/162] |

**Option C: Sweetness drops.** The act cracks. She is cross, and she tells you how long a rose takes.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| SUZ-C1 | `BEFORE_FIRST_TURN` | Behold the wrath of the garden! Please stay off the lawn. | [165/131] |
| SUZ-C2 | `SELF_LAST_SWITCHIN` | Now you've made me cross. Do you know how long a rose takes? | [167/144] |
| SUZ-C3 | `SELF_LAST_LOW_HP` | Wilt me? I bloom out of spite. Ask any daisy. | [151/73] |

**Recommended: option A.** SUZ-A2 is the pitch in one line (she ‘pretends not to notice’ and thanks the player for being gentle), SUZ-A1 uses the Starting Status, and SUZ-A3 is the line the author has seen. SUZ-B2 (‘press the brave ones in books’) is the funniest single line in her set: swap it in for SUZ-A3 if you would like a taunt more than a last stand.

**Optional extras (not in the recommended set)**

- **ACE row (`SUZ-ACE`)** names GARDEVOIR on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > They call me the small one. GARDEVOIR, dear, shall we discuss it?  [196/132]
- **STORY row (`SUZ-SCH`), needs the author:** calls back to Scheme 8 (surveyors, ‘Glade Heights’ condominiums). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace SUZ-A1.

  > They wanted condominiums here. I pressed their brochure in a book.  [172/172]

---

## 9. MIZZLE (MIZ): Gym 9, Beaconmouth (town, flooded lighthouse), Water, TIDE BADGE

- **Constant:** `TRAINER_MIZZLE`
- **Team:** GYARADOS 58 (lead), SEISMITOAD 58, ARAQUANID 59, BARRASKEWDA 59, LANTURN 59, MILOTIC 60 (ace). Six Pokémon.
- **Starting Status:** Rain, Temporary (the game prints ‘It started to rain!’ before the first-turn slide)
- **Voice:** Big, jolly, deadpan lighthouse keeper, the last gym before the coast. ‘Mizzle. Like the weather, but more of it.’ Cheerful man who says terrible things calmly: ‘the sea gives, then takes, mostly takes.’ Props: the lamp, the brass logbook, the tide. No sea creature is named, only Pokémon. Warm, never cruel.
- **Existing PROPOSED baseline:** Ha ha! That's the sea for you. Giving, then taking. Mostly taking.  (existing PROPOSED last stand)

**Which trigger fits which beat, for this leader**

- `BEFORE_FIRST_TURN` follows the rain message, so the rain joke (‘It does that when I'm excited’) lands on cue. The rain is Temporary, so it is still falling when he speaks.
- `DEFENDER_TAKES_FIRST_DOWN` names GYARADOS, the lead (safe).
- Six Pokémon means a long fight: the first-down line and the last-send-in line are many turns apart, which is good for a leader whose gag is understatement.
- `SELF_LAST_SWITCHIN` is generic (‘my last one … the lamp coming on’). Naming MILOTIC needs `Ace Pokemon` (the ACE row below).

**Option A: Cheerful deadpan (in voice).** The pitch as written: calm, jolly, terrible things said gently.  **(recommended)**

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| MIZ-A1 | `BEFORE_FIRST_TURN` | Ha! Rain. Sorry. It does that when I'm excited. `SS` | [147/88] |
| MIZ-A2 | `DEFENDER_TAKES_FIRST_DOWN` | GYARADOS is down. Fine. I once lost a pier. This is manageable. | [180/135] |
| MIZ-A3 | `SELF_LAST_LOW_HP` | Ha ha! That's the sea for you. Giving, then taking. Mostly taking. `EX` | [191/141] |

**Option B: Keeper's logbook.** Thirty years on the lamp and a logbook. Calm and slightly sad.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| MIZ-B1 | `BEFORE_FIRST_TURN` | Thirty years on this lamp. Never lost a ship. Hats, yes. Hundreds. | [190/141] |
| MIZ-B2 | `OPPONENT_LAST_SWITCHIN` | Down to your last? Don't fret. The tide goes out, then it comes back. | [176/176] |
| MIZ-B3 | `SELF_LAST_SWITCHIN` | My last one. Think of it as the lamp coming on. Do try not to stare. | [181/158] |

**Option C: Big and jolly.** The booming version. He is delighted by everything, including losing.

| Row | Trigger | Line (PROPOSED) | Px |
|---|---|---|---|
| MIZ-C1 | `BEFORE_FIRST_TURN` | Welcome to the end of the road! Past me is only sea! No pressure! | [190/143] |
| MIZ-C2 | `DEFENDER_TAKES_FIRST_DOWN` | Overboard goes the first one! Don't worry. Most of them float. | [185/134] |
| MIZ-C3 | `SELF_LAST_LOW_HP` | Now that's a wave! Somebody log it! ...Right. I'm somebody. | [164/129] |

**Recommended: option A.** MIZ-A1 turns the Starting Status into a character joke, MIZ-A2 (‘I once lost a pier’) is the whole pitch in one line, and MIZ-A3 is the line the author has seen. MIZ-B1 (‘Hats, yes. Hundreds.’) is a very close second and is the pick if you would rather not echo the rain.

**Optional extras (not in the recommended set)**

- **ACE row (`MIZ-ACE`)** names MILOTIC on `SELF_LAST_SWITCHIN`. Correct only after `Ace Pokemon` is added to this leader's `AI:` line. The recommended option has no last-send-in row, so it would be an added row.

  > MILOTIC, the lamp's all yours. Do try not to dazzle them.  [167/120]
- **STORY row (`MIZ-SCH`), needs the author:** calls back to Scheme 9 (the box of 400 permits and invoices, carried out to sea). It touches a Goldsworth scheme, which is a key story beat and PROPOSED itself. Trigger `BEFORE_FIRST_TURN`. It would replace MIZ-A1.

  > Four hundred invoices, and the sea took them all. Poor sea.  [180/121]

---

## If you approve: what wiring involves

1. Paste the approved blocks into `src/data/veldris_trainer_slides.h` at `// rows go here` (the commented file has them ready; remove the leading `// `). One block per trainer id, never two (the check tool and the compiler both reject it).
2. `python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h`, then `make -j4`. No engine file is touched, no flag or var is used, no SaveBlock change (nothing for the Delta save-state rule). The tracked pre-commit hook runs the same check on the added lines.
3. If `ace` is approved: add `/ Ace Pokemon` to the `AI:` line of the seven leader blocks in `src/data/trainers.party`, then rebuild. This changes the fight (the last-listed Pokémon stays in reserve), so mention it in `design/trainer-roster.md`.
4. Test in mGBA with the debug menu, Trainers > Try Battle, one leader at a time. The 2026-10-08 test only proved `BEFORE_FIRST_TURN`; **first down, last send-in, player's last, half and low HP have never been seen in a real fight**, so give a strong debug party and watch for: the first-faint slide, the replacement slide, and (for GRETA and HACHIMEL) the back-to-back pair. Add the result to the test log in `trainer-slides.md`.
5. Update `design/trainer-slides.md`: move the approved rows to the APPROVED table, and retire the nine leader one-liners in its PROPOSED 'last stand' list (GRETA to MIZZLE), which this file supersedes. The Elite Four and Champion one-liners there are a different stream.

## What was and was not checked

- **Checked:** every row's wrapping and width with the game's own line breaker (`slide_check_log.txt`); the animal, swearing and story-name lint; that each option has at most one row per trigger (two rows on one trigger in one block is a build error); that every reused line matches the existing text; and the trigger behaviour by reading `src/trainer_slide.c`, `src/battle_script_commands.c`, `src/battle_main.c`, `src/battle_end_turn.c` and `data/battle_scripts_1.s`.
- **Compile-checked in a scratch clone** (never in the repo): the recommended set, all of option A, all of B, all of C, the ACE rows and the SCH rows each compiled `src/trainer_slide.o` cleanly with the project's `-Werror`; a deliberately duplicated row failed with `initialized field overwritten [-Werror=override-init]`, so the test can fail. Adding `/ Ace Pokemon` to a leader's `AI:` line made `tools/trainerproc` emit `.aiFlags = AI_FLAG_BASIC_TRAINER | AI_FLAG_ACE_POKEMON`.
- **Not checked:** any row in a running game. Only `BEFORE_FIRST_TURN` has ever been seen in an emulator (2026-10-08, on Troglodyte); first down, last send-in, the player's last, half and low HP are code-read only. Finding 3 (replacement order) is also code-read only. Humour is a judgement call: the lines were written against `design/dialogue-style.md` (deadpan, short, clean) and each leader's pitch, and tested on nobody.

