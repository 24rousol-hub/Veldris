# Mid-battle line options: Elite Four, Champion and the villain bosses

**Status: PROPOSED. Nothing in this file is approved, canon or wired.** Every line is draft material for the author to pick from (CLAUDE.md rules 9 and 10: the Commons, the Drowned Crown, Cynthia and the League are key story beats). Written 2026-10-09 by the slides-league stream. Scope is the author's of 2026-10-09: mid-battle lines for **key battles only**; none for ordinary trainers or Troglodyte (his words go in the scenes around his fights).

Companion file: `veldris_trainer_slides_league_COMMENTED.h` holds the **recommended** option of every battle as commented-out rows, ready to paste into `src/data/veldris_trainer_slides.h`.

## How to approve

Reply with one letter per battle, for example: **OSSIAN A, HYACINTH A, DUNMORE C, DRAYDEN B, CYNTHIA B, TEDDY later, CROWN later.** You may also mix rows ("CYNTHIA: the first-down row of A and the last-switch-in row of B"), because every row is independent as long as one slide name appears once per trainer, or quote a rewritten line and it will be re-measured. Until you answer nothing changes. After approval the lead copies the chosen block out of `veldris_trainer_slides_league_COMMENTED.h` (swapping rows if you picked a non-recommended option), removes the leading `//`, runs `python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h`, builds, fights each trainer once in mGBA (debug menu, Trainers, Try Battle) and moves the approved lines into the Approved table of `design/trainer-slides.md`. The last three blocks (TEDDY, the Crown leader, the Mothwood officer) can only be wired once their trainer blocks exist, so approving their wording now just parks it.

## At a glance

Eight battles, three tone options each (A, B, C), one to three rows per option, only the six robust triggers. **My recommended pick is in bold**; it is the one in the `.h` file. The picks follow the voice already written in `design/dialogue/league.inc`, so they are the least likely to clash with the field text, not necessarily the funniest.

| # | Battle | Trainer block in the tree? | Recommended | Tone options |
|---|---|---|---|---|
| 1 | OSSIAN, Elite Four 1 (Dark) | yes, `TRAINER_OSSIAN` | A | **A Sunny undertaker** / B Soft menace / C Funeral-home customer service |
| 2 | HYACINTH, Elite Four 2 (Psychic) | yes, `TRAINER_HYACINTH` | A | **A I saw it coming** / B Icy perfectionist / C The snow globes leak |
| 3 | DUNMORE, Elite Four 3 (Fighting) | yes, `TRAINER_DUNMORE` | A | **A Terrible puns** / B Coach / C Drowsy |
| 4 | DRAYDEN, Elite Four 4 (Dragon) | yes, `TRAINER_DRAYDEN` | B | A Kindly grandfather / **B Quiet terror** / C Fussy dragon keeper |
| 5 | CYNTHIA, Champion (aged, author-chosen) | yes, `TRAINER_CYNTHIA` | A | **A Warm and sincere** / B Dignified / C Dry and wicked |
| 6 | TEDDY, leader of the Commons (double battle with Troglodyte) | NO (see the missing-blocks table) | A | **A Tired and fair** / B Rally speaker / C Road works |
| 7 | The Drowned Crown's leader (the R19 climax; name not decided) | NO (see the missing-blocks table) | A | **A Imperious** / B Cold tide / C Damp pedigree |
| 8 | OPTIONAL: a Crown officer at Mothwood (my suggestion, not in factions.md) | NO (see the missing-blocks table) | A | **A Brisk borrower** / B Restful menace / C Mild clerk |

## Which trigger fits which beat

Only the six triggers that `design/trainer-slides.md` calls robust are used. Read from `src/trainer_slide.c`, `src/battle_script_commands.c` and `src/battle_end_turn.c` in this tree.

| Beat | Trigger (`TRAINER_SLIDE_` prefix) | Fires when | Reliability |
|---|---|---|---|
| Stance, mood setter | `BEFORE_FIRST_TURN` | once, after both send-outs and before the first menu | Certain. Tested in mGBA on 2026-10-08, and again on 2026-10-09 (single battle and a double with a partner). It lands right after the scripted intro speech, so keep it to one short line and never repeat the intro |
| First blood | `DEFENDER_TAKES_FIRST_DOWN` | the trainer's first Pokémon faints | Certain (not an end-of-turn slide). Run in mGBA on 2026-10-09: played once, in a single battle and in a double with a partner |
| Pressure on the player | `OPPONENT_LAST_SWITCHIN` | the player sends in their last usable Pokémon after a faint | Certain after a forced replacement, never after a voluntary switch. **Not yet run in game** |
| Signature entrance, the ace | `SELF_LAST_SWITCHIN` | the trainer's last Pokémon comes out after a faint | Same rule. Needs a team of 2 or more Pokémon. Run in mGBA on 2026-10-09 (single battle and double with a partner) |
| Midpoint | `SELF_LAST_HALF_HP` | the last Pokémon is between 25 and 50 percent HP at the end of a turn | Bonus: a big hit can jump straight past the window. Run in mGBA on 2026-10-09 (single battle) |
| Last stand | `SELF_LAST_LOW_HP` | the last Pokémon is at 25 percent or less at the end of a turn | Bonus: a one-hit KO from above 25 percent skips it (seen in the double test, where the last Pokémon was one-shot). Pair it with a `SELF_LAST_SWITCHIN` row if the line must always appear. Run in mGBA on 2026-10-09 (single battle) |

Rule of thumb used below: **put the beat that matters on a certain trigger** (stance, first blood, last switch-in) and **use the HP triggers only for a bonus last-stand line**.

## Traps that matter for these fights

1. **Only one end-of-turn slide plays per trainer per turn.** `TryEndTurnTrainerSlide` tries them in a fixed order, and `SELF_LAST_LOW_HP` comes first, then the opponent-side HP slides, then `SELF_LAST_HALF_HP`. A block with both HP rows is safe, because the two HP windows never overlap, but a hit from 100 percent to 20 percent plays only the LOW_HP row. No option below uses both HP rows.
2. **Full Restore.** All five existing blocks carry `Items: Full Restore` (two each, four for Cynthia). A Pokémon healed back above 25 percent misses the LOW_HP window. Every slide plays once per battle, so an HP row can never be a required story beat.
3. **`*_LAST_SWITCHIN` fires only after a forced replacement** (a faint), never after a voluntary switch (the engine hooks it into the faint-replacement scripts). A trainer with one Pokémon can never trigger it. An officer with one Pokémon uses `SELF_LAST_LOW_HP` instead, because that Pokémon is also "the last".
4. **Field text already says hello and goodbye.** `League_Text_*Intro/Defeat/After` and `ChampSendOut` play around the fight, so a slide must not repeat their jokes. Per-trainer overlaps are flagged in the notes under each option (OSSIAN's old last-stand line echoed his defeat line; HYACINTH Option C would spoil her snow-globe after-line; DRAYDEN's old last-stand line echoes his defeat line).
5. **Rematches reuse the same trainer ids** (post-game `cleartrainerflag` rematches, `PostGame_Text_E4Rematch`), so the same rows play again. Every line below reads fine the second time; none says "first time". Rematch-only lines would need a code change and are not proposed.
6. **Naming a Pokémon in a row is only safe on `SELF_LAST_SWITCHIN`, and only while the League blocks keep `AI: Basic Trainer`.** The five blocks are plain parties (no pool, no shuffle) with the ace last (ABSOL, ALAKAZAM, CONKELDURR, DRAGONITE, GARCHOMP), and the basic AI sends the next Pokémon in block order after a faint. A smarter AI (`AI_FLAG_SMART_TRAINER` adds `SMART_MON_CHOICES` and `SMART_SWITCHING`) chooses its own Pokémon and may bring the ace out early, which would make a named row wrong. `Tags: Ace` pins order only for pooled parties like Troglodyte's, not for these blocks. So every recommended row is name-free; the two named add-ons (DRAYDEN, CYNTHIA) are optional and marked.
7. **Double battle (TEDDY).** The planned fight uses `multi_2_vs_1` with Troglodyte as the in-game partner. Slides are keyed on the boss id only, and the engine marks both of the boss's battlers as one trainer so each slide plays once (`ShouldDoTrainerSlide`, the "single-trainer doubles" guard). Troglodyte's partner key (`TRAINER_PARTNER(PARTNER_TROGLODYTE)`) stays empty because of the author's scope. `SELF_LAST_SWITCHIN` needs the boss to have **three or more** Pokémon, otherwise nothing is ever sent in last. A double with a partner was run on 2026-10-09 (see the end of this file): `BEFORE_FIRST_TURN`, `DEFENDER_TAKES_FIRST_DOWN` and `SELF_LAST_SWITCHIN` each played exactly once.
8. **Wild Kyogre has no slides.** Slides are trainer-only (`BATTLE_TYPE_TRAINER`). The legendary fight gets its music automatically (see below).
9. **Tone limits** (`design/dialogue-style.md`): no swearing outside the Goldsworths, no real animals (so no "crows" for OSSIAN, no pets that are not Pokémon), the Commons and the Crown are not Goldsworths.

## Where the jingles and fanfares should differ

How music is chosen in this tree (checked in the source):

- **Encounter sting** (the tune when a trainer spots you): the `Music:` line of a trainer block picks one of 14 stings (`src/battle_setup.c` `PlayTrainerEncounterMusic`): Male, Female, Girl, Suspicious, Intense, Cool, Aqua, Magma, Swimmer, Twins, Elite Four, Hiker, Interviewer, Rich. It only plays when a trainer walks up in the overworld. **A scripted boss fight skips it**, so a scene plays its own with `playbgm MUS_X, FALSE` before the speech (Hoenn's Elite Four and Champion rooms do exactly this with `MUS_ENCOUNTER_ELITE_FOUR` and `MUS_ENCOUNTER_CHAMPION`). A scene may use any song constant, and **no code is needed**. Note that no `Music:` value maps to `MUS_ENCOUNTER_CHAMPION`.
- **Battle theme**: chosen by trainer **class** in `GetBattleBGM` (`src/pokemon.c`): Leader, Champion, Elite Four, Rival, Aqua/Magma grunts and admins, Aqua/Magma leaders each have one; everything else gets `MUS_VS_TRAINER`. A script cannot choose it. A per-trainer difference needs a small C edit (log it in `design/engine-edits.md`).
- **Victory fanfare**: also by class, in `HandleEndTurn_BattleWon` (`src/battle_main.c`): Elite Four and Champion share `MUS_VICTORY_LEAGUE`, the Aqua/Magma family shares `MUS_VICTORY_AQUA_MAGMA`, Leader and (Veldris edit) Rival get `MUS_VICTORY_GYM_LEADER`, the rest `MUS_VICTORY_TRAINER`.

Lengths are one pass through the `.mid` in `sound/songs/midi/` (looped tunes play longer in the game), measured by a throwaway script, so treat them as approximate. All the constants named exist in `include/constants/songs.h`, `sound/song_table.inc` and `sound/songs/midi/`.

| Class or scene | Encounter sting | Battle theme | Victory fanfare | Cost and notes |
|---|---|---|---|---|
| Gym leaders (built, for reference) | block `Music:` (placeholders) | `MUS_VS_GYM_LEADER` (76 s) | `MUS_VICTORY_GYM_LEADER` (48 s) | Nothing to do |
| Troglodyte (built, for reference) | `MUS_ENCOUNTER_RICH` (18 s) via `Music: Rich` | `MUS_VS_RIVAL` (65 s) | `MUS_VICTORY_GYM_LEADER` (48 s) (Rival-class edit, 2026-10-09) | Built |
| **Elite Four** (OSSIAN, HYACINTH, DUNMORE, DRAYDEN) | `MUS_ENCOUNTER_ELITE_FOUR` (22 s), `playbgm` at the top of each member's script | `MUS_VS_ELITE_FOUR` (62 s), automatic for class Elite Four | `MUS_VICTORY_LEAGUE` (35 s), automatic | 0 code. Distinct from leaders on all three tunes. Four 35 s fanfares in a row is vanilla behaviour; if that drags, the first three members could use `MUS_VICTORY_TRAINER` (16 s) with a one-line per-trainer check in `HandleEndTurn_BattleWon` (author call, not recommended) |
| **Champion** (CYNTHIA) | `MUS_ENCOUNTER_CHAMPION` (30 s), `playbgm` (no `Music:` value reaches it) | `MUS_VS_CHAMPION` (66 s), automatic for class Champion | `MUS_VICTORY_LEAGUE` (35 s) (shared with the Elite Four), then `MUS_HALL_OF_FAME` (36 s) by script | 0 code. She already differs from the Elite Four on sting and theme. Optional, about 3 lines in `GetBattleBGM`: Cynthia only gets `MUS_RG_VS_CHAMPION` (74 s), the Kanto Champion theme that is in this ROM, to set her apart as the visiting legend |
| **Commons** (grunts, TEDDY) | `MUS_ENCOUNTER_MAGMA` (21 s) via `Music: Magma`, or `playbgm` in a scene. Comic alternative for the work crews: `MUS_ENCOUNTER_HIKER` (17 s) | grunts `MUS_VS_AQUA_MAGMA` (101 s); TEDDY `MUS_VS_AQUA_MAGMA_LEADER` (79 s) | `MUS_VICTORY_AQUA_MAGMA` (12 s) | 0 code **if** the Magma classes are reused (land twin of the sea team). The battle intro would read TEAM MAGMA / MAGMA LEADER until the class strings in `gTrainerClasses` (`src/battle_main.c`) are renamed, which is an upstream edit. 12 s is the shortest fanfare, which suits a defeat that leads into a talky change of heart |
| **Drowned Crown** (grunts, officer, leader) | `MUS_ENCOUNTER_AQUA` (31 s) via `Music: Aqua` | grunts `MUS_VS_AQUA_MAGMA` (101 s); leader `MUS_VS_AQUA_MAGMA_LEADER` (79 s) | `MUS_VICTORY_AQUA_MAGMA` (12 s) | 0 code with the Aqua classes. The two villain families share the other two tunes (as Aqua and Magma do in Hoenn), so the sting is where they must differ: **Commons = Magma, Crown = Aqua** keeps them from ever sounding alike. A bigger split (own battle theme for the Crown leader, for example `MUS_VS_FRONTIER_BRAIN` (94 s)) is a 3-line per-trainer edit |
| Crown climax on R19 (scene) | `playbgm` `MUS_AWAKEN_LEGEND` (11 s) when Kyogre wakes, then `MUS_ABNORMAL_WEATHER` (36 s) as the sky turns | wild Kyogre: `MUS_VS_KYOGRE_GROUDON` (49 s), automatic for the legendary | catch: `MUS_CAUGHT`, the usual one | 0 code. `MUS_ABNORMAL_WEATHER` replaces the Kyogre weather theme of Ruby and Sapphire (`songs.h` comment) |

**Summary of where I would differ (all zero code):** (1) the encounter sting per family: Elite Four, Champion, Commons = Magma, Crown = Aqua; (2) the class-driven battle theme and fanfare stay as they are for the League (they already differ from the leaders); (3) the Crown climax uses scene music for the wake and the sky. The two small C edits above are optional polish and I would hold them until the author has heard the zero-code version.

Real song constants available (from `include/constants/songs.h`; lengths in seconds):

- Encounter stings (Hoenn): `MUS_ENCOUNTER_GIRL` 15, `MUS_ENCOUNTER_MALE` 16, `MUS_ENCOUNTER_SWIMMER` 13, `MUS_ENCOUNTER_RICH` 18, `MUS_ENCOUNTER_FEMALE` 16, `MUS_ENCOUNTER_MAY` 34, `MUS_ENCOUNTER_INTENSE` 14, `MUS_ENCOUNTER_COOL` 31, `MUS_ENCOUNTER_AQUA` 31, `MUS_ENCOUNTER_BRENDAN` 34, `MUS_ENCOUNTER_SUSPICIOUS` 21, `MUS_ENCOUNTER_MAGMA` 21, `MUS_ENCOUNTER_TWINS` 11, `MUS_ENCOUNTER_ELITE_FOUR` 22, `MUS_ENCOUNTER_HIKER` 17, `MUS_ENCOUNTER_INTERVIEWER` 12, `MUS_ENCOUNTER_CHAMPION` 30
- Encounter stings (Kanto, `MUS_RG_`): `MUS_RG_ENCOUNTER_ROCKET` 9, `MUS_RG_ENCOUNTER_GIRL` 7, `MUS_RG_ENCOUNTER_BOY` 9, `MUS_RG_ENCOUNTER_RIVAL` 20, `MUS_RG_ENCOUNTER_GYM_LEADER` 9, `MUS_RG_ENCOUNTER_DEOXYS` 15
- Battle themes (Hoenn): `MUS_VS_RAYQUAZA` 49, `MUS_VS_FRONTIER_BRAIN` 94, `MUS_VS_MEW` 45, `MUS_VS_WILD` 53, `MUS_VS_AQUA_MAGMA` 101, `MUS_VS_TRAINER` 90, `MUS_VS_GYM_LEADER` 76, `MUS_VS_CHAMPION` 66, `MUS_VS_REGI` 60, `MUS_VS_KYOGRE_GROUDON` 49, `MUS_VS_RIVAL` 65, `MUS_VS_ELITE_FOUR` 62, `MUS_VS_AQUA_MAGMA_LEADER` 79
- Battle themes (Kanto): `MUS_RG_VS_GYM_LEADER` 57, `MUS_RG_VS_TRAINER` 102, `MUS_RG_VS_WILD` 45, `MUS_RG_VS_CHAMPION` 74, `MUS_RG_VS_DEOXYS` 81, `MUS_RG_VS_MEWTWO` 45, `MUS_RG_VS_LEGEND` 45
- Victory fanfares (Hoenn and Kanto): `MUS_VICTORY_WILD` 16, `MUS_VICTORY_GYM_LEADER` 48, `MUS_VICTORY_LEAGUE` 35, `MUS_VICTORY_TRAINER` 16, `MUS_VICTORY_AQUA_MAGMA` 12, `MUS_VICTORY_ROAD` 54, `MUS_RG_VICTORY_ROAD` 32, `MUS_RG_VICTORY_TRAINER` 16, `MUS_RG_VICTORY_WILD` 16, `MUS_RG_VICTORY_GYM_LEADER` 48
- Scene tunes useful for the League and the climax: `MUS_AWAKEN_LEGEND` 11, `MUS_ABNORMAL_WEATHER` 36, `MUS_HALL_OF_FAME` 36, `MUS_HALL_OF_FAME_ROOM` 34, `MUS_VICTORY_ROAD` 54, `MUS_RG_VICTORY_ROAD` 32, `MUS_SEALED_CHAMBER` 36, `MUS_RAYQUAZA_APPEARS` 26, `MUS_SAILING` 32, `MUS_CAUGHT` 14, `MUS_OBTAIN_BADGE` 5

## The battles

Row tables show the slide name, the line, and the pixel width of each displayed line (measured with the game's own line-breaker, 7 wide letters for `{B_PLAYER_NAME}`; the box is 208 px, so every line fits on one page of two lines, with no scroll). Each row was also checked with a narrow name.

### 1. OSSIAN, Elite Four 1 (Dark)

- **Block:** id 261 (was Sidney). Pic `Veldris Elite Four Ossian`, 5 Pokémon: Houndoom 65, Honchkrow 65, Pangoro 65, Krookodile 66, Absol 66. 2 Full Restore.
- **Voice:** Cheerful undertaker, cheerful about death, polite about it. Field intro: 'Mind the dark... I bury things for a living.' Field defeat: 'Oh, that was lovely. A proper send-off.'
- **Field text:** `League_Text_OssianIntro / Defeat / After` already play around the fight. Slides must not repeat 'mind the dark', 'bury things' or 'send-off'. Aside for the author: that intro says 'It's only the crows. Mostly.', and crows are real animals under the Pokémon-only rule; 'the Honchkrow' would be the safe wording.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (one short mood line; the field intro has just finished); `DEFENDER_TAKES_FIRST_DOWN` (his reaction to losing the first Pokémon); `SELF_LAST_SWITCHIN` (his fifth Pokémon comes out, Absol under the current Basic AI: the signature line); `OPPONENT_LAST_SWITCHIN` (pressure when the player is down to the last Pokémon); `SELF_LAST_LOW_HP` (last stand, a bonus that a one-hit KO can skip).

**Option A: Sunny undertaker (recommended).** The house voice from league.inc: a genial host who treats the fight as an event he is hosting. Warmest of the three.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `DEFENDER_TAKES_FIRST_DOWN` | Well struck! That's one for the guest book. Do carry on. | 160 / 124 |
| `SELF_LAST_SWITCHIN` | My last one. Now the service proper begins. Do mind the flowers. | 182 / 143 |
| `SELF_LAST_LOW_HP` | Lovely! That's my funeral, I think. Wonderful turnout. | 177 / 98 |

*Note:* The earlier PROPOSED last-stand line in trainer-slides.md was 'Lovely! A proper send-off. Mine, I think. Wonderful turnout.' It repeats the field defeat line ('A proper send-off'), so the LOW_HP row here is reworded. Swap the old one back if you prefer the echo.

**Option B: Soft menace.** Same politeness, but the Dark type shows. He is calm, slightly too pleased, and never raises his voice.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Take your time. Nobody has ever left this room early. | 164 / 106 |
| `OPPONENT_LAST_SWITCHIN` | Your last one, {B_PLAYER_NAME}. I do like a guest who stays to the end. | 176 / 144 |
| `SELF_LAST_LOW_HP` | Hm. Now I'm the one lying down. How novel. Do go on. | 155 / 100 |

**Option C: Funeral-home customer service.** Pure deadpan comedy: the battle as a small business with terms and conditions.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | A reminder: all losses are final, and the flowers are extra. | 162 / 136 |
| `SELF_LAST_SWITCHIN` | Last one out. Please keep your hands inside the hearse. | 159 / 127 |
| `SELF_LAST_LOW_HP` | Ah. I am being buried by a client. Highly irregular. | 168 / 85 |

### 2. HYACINTH, Elite Four 2 (Psychic)

- **Block:** id 262 (was Phoebe). Pic `Veldris Elite Four Hyacinth`, 5 Pokémon: Espeon 66, Meowstic 66, Reuniclus 67, Farigiraf 67, Alakazam 68. 2 Full Restore.
- **Voice:** Icy manners, deadpan, always seems to know what you will do, secretly keeps snow globes. Field intro: 'I saw it coming. I always do... Try to surprise me.' Field defeat: 'I did not see that one. Don't tell anyone.'
- **Field text:** `League_Text_HyacinthIntro / Defeat / After`. The 'I saw it coming' gag and 'Try to surprise me' are already in the intro, so Option A plays on the idea without repeating either line, and B avoids it. C is the one that spoils the after-line (see its note).
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (she announces what she already knows); `DEFENDER_TAKES_FIRST_DOWN` (the first time the player surprises her); `SELF_LAST_SWITCHIN` (her last Pokémon comes out, Alakazam under the current Basic AI); `OPPONENT_LAST_SWITCHIN` (she 'foresaw' the player running low); `SELF_LAST_LOW_HP` (last stand).

**Option A: I saw it coming (recommended).** Her omniscience as the running joke: she has notes, a diary and no surprises, until the field defeat line, where the first surprise lands. No row repeats the field intro's 'try to surprise me'.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `DEFENDER_TAKES_FIRST_DOWN` | Mm. That was in my notes. Page nine, I believe. | 127 / 105 |
| `OPPONENT_LAST_SWITCHIN` | Your last one. Naturally. I put it in my diary this morning. | 170 / 125 |
| `SELF_LAST_LOW_HP` | I saw this coming. I did rather hope I was wrong. | 157 / 89 |

*Note:* The LOW_HP row is the earlier PROPOSED last-stand line, unchanged. A deliberately has no `BEFORE_FIRST_TURN` row, because her intro already ends on a challenge.

**Option B: Icy perfectionist.** No jokes at all: aristocratic, bored and cold. The Psychic gym-leader-who-has-seen-everything.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | I have already watched this fight twice. It ends badly for you. | 176 / 148 |
| `SELF_LAST_SWITCHIN` | My last. You'll forgive me for not looking nervous. I never do. | 170 / 144 |
| `SELF_LAST_LOW_HP` | A cold front I did not foresee. How irritating. Continue. | 159 / 128 |

**Option C: The snow globes leak.** The secret soft spot (snow globes in her desk) slips out through the composure. Gentlest of the three.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Do keep your voice down. The snow globes startle easily. | 174 / 114 |
| `DEFENDER_TAKES_FIRST_DOWN` | Hm. Excuse me. I must go and shake something. Calmly. Later. | 177 / 128 |
| `SELF_LAST_SWITCHIN` | My last. If I win tonight, I am allowed to shake one globe. One. | 194 / 124 |

*Note:* Spoils the reveal in `League_Text_HyacinthAfter` ('I keep snow globes in my desk. Not a word.'). Choose C only if that after-line is moved or dropped.

### 3. DUNMORE, Elite Four 3 (Fighting)

- **Block:** id 264 (was Drake). Pic `Veldris Elite Four Dunmore`, 5 Pokémon: Breloom 68, Hawlucha 68, Heracross 69, Annihilape 69, Conkeldurr 70. 2 Full Restore.
- **Voice:** Huge, gentle, terrible at puns, naps between rounds. Field intro: 'I lift, I punch, I nap.' Field defeat: 'Oh, that's the good kind of ow.'
- **Field text:** `League_Text_DunmoreIntro / Defeat / After`. The nap gag is in the intro, so Option C leans on it on purpose; A and B do not.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (warm-up line); `DEFENDER_TAKES_FIRST_DOWN` (pun delivery slot: the first KO is the natural setup); `SELF_LAST_SWITCHIN` (big finish); `OPPONENT_LAST_SWITCHIN` (coach-style encouragement); `SELF_LAST_HALF_HP` (a mid-point beat; plays before LOW_HP on a later turn); `SELF_LAST_LOW_HP` (last stand).

**Option A: Terrible puns (recommended).** Every row is a pun that dies on delivery. Funniest on paper, and the easiest to extend later.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `DEFENDER_TAKES_FIRST_DOWN` | Well, that was a punch line! ...No? I'll keep working on it. | 170 / 117 |
| `SELF_LAST_SWITCHIN` | Last round! My best, hands down! ...Hands. Fists. Never mind. | 169 / 136 |
| `SELF_LAST_LOW_HP` | Whew! Running low. Don't let me sit down. I'll nap! | 142 / 106 |

*Note:* The LOW_HP row is the earlier PROPOSED last-stand line, unchanged.

**Option B: Coach.** No jokes: a big friendly sports coach who is delighted to be hit. Sincere, and a bit scary because he means it.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Right! Stretch, breathe and don't hold back. I won't. | 174 / 94 |
| `OPPONENT_LAST_SWITCHIN` | Your last one? Chin up, {B_PLAYER_NAME}. This is where it counts. | 166 / 122 |
| `SELF_LAST_LOW_HP` | Ha! That's the stuff! Hit me again, that was lovely! | 144 / 118 |

**Option C: Drowsy.** Leans on the nap gag: he is barely awake until he is hit. Quietest of the three.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Mm? Is it round one? I was resting my eyes. Carry on. | 177 / 91 |
| `DEFENDER_TAKES_FIRST_DOWN` | Oh! That woke me up. Thank you. I'll have another. | 136 / 115 |
| `SELF_LAST_HALF_HP` | Halfway there! The fight, I mean. The nap comes after. | 170 / 107 |

### 4. DRAYDEN, Elite Four 4 (Dragon)

- **Block:** id 263 (was Glacia). Pic `Veldris Elite Four Drayden`, 6 Pokémon: Goodra 69, Kommo-o 69, Dragapult 70, Baxcalibur 70, Salamence 71, Dragonite 71. 2 Full Restore.
- **Voice:** Oldest member, a kind old man, quietly terrifying, keeps dragons like pets. Field intro: 'Sit, child. No? Then we'll do it the loud way.' Field defeat: 'They do so hate losing.'
- **Field text:** `League_Text_DraydenIntro / Defeat / After`. The earlier last-stand line ('They do so hate to lose') overlaps the field defeat ('They do so hate losing'); keep it if you like a callback, drop it if not.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (the gentle warning); `DEFENDER_TAKES_FIRST_DOWN` (soothing a Pokémon that fainted); `SELF_LAST_SWITCHIN` (his sixth Pokémon comes out, Dragonite under the current Basic AI); `OPPONENT_LAST_SWITCHIN` (he notices the player's last Pokémon); `SELF_LAST_LOW_HP` (last stand).

**Option A: Kindly grandfather.** Gentle and sweet with a faint threat underneath. The closest to the existing PROPOSED last-stand line.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | There will be tea afterwards, child. Probably for one of us. | 182 / 119 |
| `DEFENDER_TAKES_FIRST_DOWN` | There, there. That one is only sulking. They all do it. | 153 / 116 |
| `SELF_LAST_LOW_HP` | Gently now, child. They do so hate to lose, you see. | 147 / 112 |

*Note:* The LOW_HP row is the earlier PROPOSED last-stand line, unchanged.

**Option B: Quiet terror (recommended).** The same kind voice with the mask slipping: calm, specific, unhurried. Most menacing, still no raised voice.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Be at ease, child. The first few minutes are the gentle ones. | 161 / 148 |
| `OPPONENT_LAST_SWITCHIN` | Your last, I see. Do keep breathing. They notice when you stop. | 183 / 139 |
| `SELF_LAST_SWITCHIN` | Ah. This is the one I keep by the fire. Mind your manners. | 167 / 122 |

**Option C: Fussy dragon keeper.** Comic: the world's most dangerous man fusses over his pets like an anxious old uncle.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Mind the tails, child. They're sensitive. And it's nearly supper. | 148 / 173 |
| `DEFENDER_TAKES_FIRST_DOWN` | Oh dear, oh dear. Who's my fierce one? You are. You are. | 166 / 112 |
| `SELF_LAST_LOW_HP` | Now, now, nobody is to bite the guest. ...Not yet. | 137 / 108 |

*Optional named version of the `SELF_LAST_SWITCHIN` row (names the ace, so see trap 6; use it in place of that row, or as an extra row in an option that has none):* DRAGONITE, my dear. Do be gentle with the child. Or don't. (168 / 122 px)

### 5. CYNTHIA, Champion (aged, author-chosen)

- **Block:** id 335 (was Wallace). Pic `Veldris Champion Cynthia`, 6 Pokémon: Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 (ace, last in the block). 4 Full Restore.
- **Voice:** Dry, warm, sharp, long in the tooth, calm, a bit grandmotherly and still terrifying; respects the grudge. Field intro: 'I've been a Champion longer than you've been walking... That's a fine engine.' Send-out: 'Don't mind my knees, dear.'
- **Field text:** `League_Text_ChampIntro / SendOut / Defeat / After / Praise`. Her friendship with Gatsby is a post-League reveal: none of the options mention Gatsby, Hollowbrook or where she is from.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (keep it to one line: the intro and the knees line have just played); `DEFENDER_TAKES_FIRST_DOWN` (her delight at the first real hit); `SELF_LAST_SWITCHIN` (the ace comes out: Garchomp under the current Basic AI); `OPPONENT_LAST_SWITCHIN` (she respects the player's last stand); `SELF_LAST_LOW_HP` (her last stand: the line the earlier draft already had).

**Option A: Warm and sincere (recommended).** A delighted grandmother-champion. Praise, encouragement and 'dear', and genuinely moved. The safest fit for the existing intro.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `DEFENDER_TAKES_FIRST_DOWN` | Oh, well done, dear! Lovely timing. I was getting drowsy. | 173 / 111 |
| `SELF_LAST_SWITCHIN` | Come along, old friend. Show the youngster what we can do. | 164 / 134 |
| `SELF_LAST_LOW_HP` | Splendid. It has been years since my heart raced like this. | 173 / 127 |

*Note:* The LOW_HP row is the earlier PROPOSED last-stand line, unchanged. A deliberately has no `BEFORE_FIRST_TURN` row: she has already spoken twice (the intro, then the knees line). The last-switch-in row is name-free, so it is right for any last Pokémon.

**Option B: Dignified.** Formal, hushed, mythic: short sentences and a sense of the weight of the seat. Delighted, but you have to listen for it.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Begin when you are ready. I have waited a long time to be asked. | 167 / 159 |
| `OPPONENT_LAST_SWITCHIN` | Your last. Stand tall, {B_PLAYER_NAME}. This is the part they remember. | 183 / 136 |
| `SELF_LAST_SWITCHIN` | Enough. You have earned my best. Let us finish this properly. | 170 / 143 |

**Option C: Dry and wicked.** Her wit as a weapon: jokes about her age and her enemies, and a naughty twinkle at being challenged. Funniest, least solemn.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | I've outlasted four rivals and most of a knee. Do your worst, dear. | 184 / 156 |
| `DEFENDER_TAKES_FIRST_DOWN` | Ha! You do have teeth. How lovely. I'd begun to worry. | 174 / 97 |
| `SELF_LAST_LOW_HP` | Oh, stop it. No, don't stop. Don't you dare stop. Marvellous. | 166 / 135 |

*Optional named version of the `SELF_LAST_SWITCHIN` row (names the ace, so see trap 6; use it in place of that row, or as an extra row in an option that has none):* GARCHOMP, dear. Do be kind to the youngster. Or don't. (150 / 124 px)

### 6. TEDDY, leader of the Commons (double battle with Troglodyte)

- **Block:** NO BLOCK YET. Sprite planned: DP Pokéfan M with a forest-green shirt (not imported). Team, class and levels not decided. Planned as a 2 vs 1 double battle with TROGLODYTE as the in-game partner (badges 5 to 7; order of team-up and fight not fixed). Suggested vanilla id to reuse: `TRAINER_MAXIE_MAGMA_HIDEOUT` (601, class Magma Leader, Music Magma).
- **Voice:** A tired, decent local who is fed up with the Goldsworths; friendly guest at the inn in Wendlebury; political ('have a word with the lads'); British-flavoured ('mate', 'love', 'lads'). After losing he changes approach: the Goldsworths are not evil, and some of the blame belongs to the Commons' own ignorance.
- **Field text:** No field text exists. Rows marked (P) name the Goldsworth partner and need Troglodyte beside the player.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (his stance to the pair of them; fires once, the engine handles 2 vs 1); `DEFENDER_TAKES_FIRST_DOWN` (the first of his two active Pokémon to faint); `SELF_LAST_SWITCHIN` (needs a team of 3 or more; with 2 Pokémon nothing is ever 'switched in last'); `SELF_LAST_LOW_HP` (last stand: a good place for a humane line that sets up the change of heart).

**Option A: Tired and fair (recommended).** A decent man doing a wrong thing and knowing it. Sets up his change of heart, since nothing he says here would embarrass him later.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | No hard feelings, mate. Plenty for the Goldsworth, mind. (P) | 155 / 129 |
| `DEFENDER_TAKES_FIRST_DOWN` | Fair play, that's one. I'll not hold it against you. Him, though. (P) | 175 / 141 |
| `SELF_LAST_LOW_HP` | Go easy, mate. There's a whole crew's lunch riding on this. | 188 / 105 |

(P) = depends on a partner being there (it names the Goldsworth or counts two against one). Without Troglodyte beside the player, reword.

**Option B: Rally speaker.** The Commons as a movement: a man who speechifies in the middle of a fight and cannot stop. Political and funny, a little hypocritical.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Two against one! Typical of how they treat the working man! (P) | 190 / 117 |
| `DEFENDER_TAKES_FIRST_DOWN` | They've taken one of ours! Remember this day! ...It's a Tuesday. | 188 / 137 |
| `SELF_LAST_SWITCHIN` | My last, friends, and there is nothing common about it! ...Sorry. Habit. | 194 / 163 |

(P) = depends on a partner being there (it names the Goldsworth or counts two against one). Without Troglodyte beside the player, reword.

**Option C: Road works.** Pure deadpan: the fake road works from Route 3 as a manner of speaking. Barriers, diversions, delays expected.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Sorry, this battle is closed for maintenance. Use another one. | 163 / 156 |
| `DEFENDER_TAKES_FIRST_DOWN` | One of ours is down. Delays expected. We apologise for any inconvenience. | 193 / 186 |
| `SELF_LAST_LOW_HP` | Estimated completion: never. Do mind the barriers on your way out. | 189 / 150 |

### 7. The Drowned Crown's leader (the R19 climax; name not decided)

- **Block:** NO BLOCK YET. Name, look, class and team not decided. Believed to be the last descendant of the kings and queens who ruled the waters from Aldermere. Fought after badge 9 on the way into Gildhaven, with the Elite Four and Cynthia away; Kyogre (a wild legendary, so no slide) is woken on R19. Suggested vanilla id to reuse: `TRAINER_ARCHIE` (34, class Aqua Leader, Music Aqua).
- **Voice:** Menacing in the hack's deadpan register. The Crown is the volatile group that does not care about casualties. 'Believed' leaves the lineage unproven, so no row confirms it; Option C deliberately leans toward the claim being shaky (a story call, see open questions).
- **Field text:** No field text exists. No row uses a gendered pronoun or the leader's name.
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (the entrance threat); `DEFENDER_TAKES_FIRST_DOWN` (the first crack in the composure); `SELF_LAST_SWITCHIN` (the last of the line); `OPPONENT_LAST_SWITCHIN` (cold pressure when the player is down to the last Pokémon); `SELF_LAST_LOW_HP` (last stand, right before Kyogre's wake).

**Option A: Imperious (recommended).** Royal 'we', decrees and disdain. Menacing and funny because it is so grand. Does not depend on whether the claim is true.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | We shall be brief. Kneel, or sink. Most do both. | 137 / 97 |
| `DEFENDER_TAKES_FIRST_DOWN` | Our first loss. Someone shall be dismissed. Possibly everyone. | 164 / 153 |
| `SELF_LAST_SWITCHIN` | Behold the last of the line. Do try not to blink. We never do. | 177 / 130 |

**Option B: Cold tide.** Soft, patient and frightening. The only option that plays the 'does not care about casualties' trait straight, at PG-13.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | The sea is patient. I am not. Do hurry up and lose. | 146 / 107 |
| `OPPONENT_LAST_SWITCHIN` | Your last one. How brave. How brief. Accept my condolences in advance. | 182 / 179 |
| `SELF_LAST_LOW_HP` | Go on, then. A few of us will drown. Some of you, too. Nothing personal. | 176 / 181 |

**Option C: Damp pedigree.** The grandest family tree in the region, under water. Funniest; it undercuts the leader, so it leans toward the 'claim may be false' twist.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | I have the family tree. It is under water, but I have it. | 178 / 105 |
| `DEFENDER_TAKES_FIRST_DOWN` | My ancestors ruled these waves. They would be furious. And damp. | 194 / 139 |
| `SELF_LAST_LOW_HP` | Don't! I'm the last of a very old line! ...Probably. The papers are wet. | 191 / 160 |

### 8. OPTIONAL: a Crown officer at Mothwood (my suggestion, not in factions.md)

- **Block:** NO BLOCK YET, and factions.md does not promise a battle here: it says the Crown steal a Time Gear-like piece of Dialga's seal from the shrine and time stops in the forest (required event after badge 2). Included only in case the author wants a boss-style fight at the shrine; skip otherwise. Suggested vanilla id: `TRAINER_MATT` (30, class Aqua Admin, Music Aqua).
- **Voice:** Brisk, junior, out of their depth: the player's first real look at the Crown, inland where they should not be.
- **Field text:** No field text exists. A one- or two-Pokémon fight is assumed, so rows are limited to BEFORE_FIRST_TURN and SELF_LAST_LOW_HP (with one Pokémon that is also the 'last' one).
- **Triggers that fit this fight:** `BEFORE_FIRST_TURN` (threat or excuse at the shrine); `SELF_LAST_LOW_HP` (works even for a one-Pokémon officer, since that Pokémon is the last).

**Option A: Brisk borrower (recommended).** Polite thief: they are only borrowing it.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Please don't touch the shrine. We're only borrowing it. For ever. | 186 / 140 |
| `SELF_LAST_LOW_HP` | Careful, it's delicate! ...Oh dear. I suppose it's already stopped. | 177 / 154 |

**Option B: Restful menace.** The stopped forest as a threat: nothing here will ever hurry again.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | Time has stopped here. Isn't it restful? Do stay. | 147 / 103 |
| `SELF_LAST_LOW_HP` | Take your time. Everyone here has. For rather a long while. | 178 / 120 |

**Option C: Mild clerk.** A junior official more worried about the paperwork than the heist.

| Slide | Line (PROPOSED) | px per line |
|---|---|---|
| `BEFORE_FIRST_TURN` | I need a signature for the shrine. Sadly, the pen has stopped too. | 176 / 163 |
| `SELF_LAST_LOW_HP` | Ugh. Please don't tell the Crown I lost. They're so damp about it. | 173 / 157 |

## Blocks that do not exist yet

The five League blocks exist and carry the right ids (`TRAINER_OSSIAN` 261, `TRAINER_HYACINTH` 262, `TRAINER_DRAYDEN` 263, `TRAINER_DUNMORE` 264, `TRAINER_CYNTHIA` 335), so their rows can be wired and tried through the debug menu as soon as the author approves them. (Their `Music:` lines are Male/Female placeholders; this only matters if one of them ever spots the player in the overworld.) The three boss battles cannot be wired yet:

| Battle | What is missing | Suggested way to build it (not a decision) |
|---|---|---|
| TEDDY, Commons leader | The `trainers.party` block (name, class, pic, team, `IVs: 0` on every Pokémon); a `TRAINER_TEDDY` constant; the pic (DP Pokéfan M with the forest-green shirt is planned, not imported); a class name; a team; a `PARTNER_TROGLODYTE` entry in `include/constants/battle_partner.h` and `src/data/battle_partners.h` (`PARTNER_COUNT` goes from 2 to 3); the scene script with `multi_2_vs_1`; the fight's place in the story (the order of team-up and fight is open in `factions.md`) | Reuse a vanilla id, as the author's rule says: `TRAINER_MAXIE_MAGMA_HIDEOUT` (601, Magma Leader) with `#define TRAINER_TEDDY TRAINER_MAXIE_MAGMA_HIDEOUT`. A team of 3 or more so that `SELF_LAST_SWITCHIN` can fire. |
| The Crown's leader | Everything: name, look, class, pic, team, the constant, the scene on R19, Kyogre's wake. The leader's name and look are undecided in `factions.md` | `TRAINER_ARCHIE` (34, Aqua Leader) behind a `TRAINER_CROWN_LEADER` alias; rename the class string if the Aqua class is reused |
| Optional Mothwood officer | Not promised in `factions.md` (it describes a theft and a stopped forest, not a battle). Only needed if the author wants a fight at the shrine | `TRAINER_MATT` (30, Aqua Admin) behind `TRAINER_CROWN_OFFICER_MOTHWOOD`. One or two Pokémon is enough |

Every vanilla id above was read from `include/constants/opponents.h` and `src/data/trainers.party` in this tree; none is used by a Veldris block. Check again before reusing, since other work may take them.

## Open questions for the author

1. **Pick a tone per battle** (A, B or C, or mix rows). My picks are in the glance table. Where I am least sure: **Cynthia** (A is warm and matches her intro; B is more solemn; C is the funniest) and **Drayden** (B is the most "quietly terrifying", A is closest to the existing one-liner).
2. **Does every Elite Four member need a `BEFORE_FIRST_TURN` line?** It plays right after the scripted intro, so it is a second speech. In the recommended set only DRAYDEN, TEDDY, the Crown leader and the Mothwood officer use one; the others rely on first-blood, last-switch-in and last-stand rows. Recommendation: keep it to one short line where used.
3. **Name-the-ace rows** for DRAYDEN and CYNTHIA: wanted? They are only right while the League keeps the basic AI (trap 6). Recommendation: no for now; if wanted, CYNTHIA only, once the AI decision for the League is made.
4. **Crown leader tone is a story call.** Option B plays the "does not care about casualties" trait straight (the darkest line in this file: "A few of us will drown. Some of you, too."). Option C undercuts the lineage ("the paperwork is wet"), which leans toward the "claim may be false" twist in `factions.md`. A (imperious) commits to neither. Recommendation: A, until the twist is decided.
5. **TEDDY:** fine to assume Troglodyte as partner in the rows marked (P), and a boss team of 3 or more? Recommendation: yes to both.
6. **Mothwood officer:** do you want a battle at the shrine at all? Recommendation: no, keep it a cutscene; the option rows are there only in case.
7. **Fanfares:** keep the League fanfare shared by the Elite Four and Champion (as in every Gen 3 game)? Commons sting `MUS_ENCOUNTER_MAGMA` (serious) or `MUS_ENCOUNTER_HIKER` (comic workmen)? Recommendation: keep the League as is, Magma for the Commons and Aqua for the Crown.

## How this was checked

- Every row (all 24 options, the 2 optional add-ons, and the 23 recommended rows in the `.h` file) was run through the real `design/tools/slide_check.py` / `dialogue_check.py` logic: charmap, line-breaker and glyph widths. All fit two lines of 208 px or less with no scroll, for a wide and a narrow player name. No double quotes, no `{PLAYER}`, no `{RIVAL}`, no real-animal words.
- The commented `.h` file was un-commented mechanically (the exact `sed` in its header), the three non-existent names were replaced with their suggested vanilla ids, and the result was run through `slide_check.py`: 23 strings, 0 errors, no duplicate ids, no duplicate slide in a block.
- **Compile.** A scratch clone of the repo at HEAD `8bb23927` (deleted afterwards) got the 23 rows pasted into `src/data/veldris_trainer_slides.h`; `make -j2` compiled and linked with no errors. (The first run stopped at the very last step, writing the 32 MiB ROM, with "No space left on device": the shared disk was full. A second `make` finished it. It was a disk problem, not a compile one.)
- **In the emulator (mGBA 2026-10-09, headless, own display; throwaway build, never committed).** In the clone, TRAINER_OSSIAN was given a two-Pokémon team (Magikarp 3, Chansey 5, no items) and the stand-in id for TEDDY (`TRAINER_MAXIE_MAGMA_HIDEOUT`) a three-Pokémon team (Magikarp 3 twice, Chansey 5), and each was given a union of the proposed rows so every trigger could be seen in one fight. Debug preset 4 (Mudkip), then R+START, Trainers, Try Battle:
  - **Single battle, OSSIAN (id 261):** `BEFORE_FIRST_TURN`, `DEFENDER_TAKES_FIRST_DOWN`, `SELF_LAST_SWITCHIN`, `SELF_LAST_HALF_HP` and `SELF_LAST_LOW_HP` all played, in that order, once each. The trainer picture slid in, the text was exactly the proposed row on two lines with no scroll, and each waited for a button press. The half-HP line came on one turn and the low-HP line on a later one, as predicted.
  - **Double battle with a partner (Trainer 1 = id 601, Partner = STEVEN, Double Battle TRUE):** the boss sent out two Pokémon; `BEFORE_FIRST_TURN`, `DEFENDER_TAKES_FIRST_DOWN` and `SELF_LAST_SWITCHIN` each played exactly once (the single-trainer-doubles guard works). `SELF_LAST_LOW_HP` did not appear because Steven's Metang one-shot the last Pokémon, which is the documented trap.
  - Screenshots (contact sheets) of these are in `evidence/` next to this file. They show the proposed text, not a decision.
- **Not run:** `OPPONENT_LAST_SWITCHIN` (needs the player to be reduced to the last Pokémon after a faint, which the debug party could not do cheaply; it shares the call path of `SELF_LAST_SWITCHIN`, `BS_TryTrainerSlideMsgLastOn`, but with a different condition), `SELF_LAST_LOW_HP` in a double, any real boss block (none exists), and any run on a phone emulator (Delta). The rows seen in game were OSSIAN's option A rows plus two borrowed rows (OSSIAN B's stance row, DUNMORE C's half-HP row) and TEDDY's option A rows plus option B's last-switch-in row. Every other recommended row was compiled and measured, but not fought.
- **Note for `design/trainer-slides.md` test log (if the lead wants it):** 2026-10-09, mGBA, throwaway rows and weak teams in a scratch clone: BEFORE_FIRST_TURN, DEFENDER_TAKES_FIRST_DOWN, SELF_LAST_SWITCHIN, SELF_LAST_HALF_HP, SELF_LAST_LOW_HP work in a single battle; BEFORE_FIRST_TURN, DEFENDER_TAKES_FIRST_DOWN and SELF_LAST_SWITCHIN work once each in a double with an in-game partner; OPPONENT_LAST_SWITCHIN not run.

