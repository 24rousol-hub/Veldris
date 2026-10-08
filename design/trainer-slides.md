# Trainer slides: mid-battle trainer lines

**Status: the mechanism is BUILT (2026-10-08, author approved the idea). No lines are wired yet.** Troglodyte's fights and the gym leaders' story lines are key beats (CLAUDE.md rules 9 and 10), so every line below stays PROPOSED until the author picks. Open questions are at the bottom.

A trainer slide is a short line a trainer says during a fight: their picture slides in from the right, the line shows in the battle text box, the picture slides out. It costs no flags, vars, art or ROM space (the empty tables were already in the ROM; only the string bytes are new).

## Where rows live

- `src/data/veldris_trainer_slides.h` (hack-owned) holds one block per trainer, keyed by trainer id.
- `src/trainer_slide.c` includes it once, inside the `DIFFICULTY_NORMAL` block of `sTrainerSlides` (the only upstream edit, logged in [engine-edits.md](engine-edits.md)). Difficulty is not used here, so only that block is read.
- A row is `VELDRIS_SLIDE(NAME, "text")`. The macro adds `{PAUSE_UNTIL_PRESS}` so the line waits for A or B.
- Keys can be alias names (`TRAINER_HACHIMEL`, `TRAINER_TROGLODYTE_HOLLOWBROOK`), but **list each id once**: `TRAINER_ROXANNE_1` is the same id as `TRAINER_HACHIMEL`, and two blocks for one id is a build error. The same slide twice in one block is also a build error.

## Triggers

Robust ones, good for story beats: `BEFORE_FIRST_TURN`, `DEFENDER_TAKES_FIRST_DOWN` (this trainer's first Pokémon faints), `SELF_LAST_SWITCHIN` (their last Pokémon is sent in), `OPPONENT_LAST_SWITCHIN` (the player's last), `SELF_LAST_HALF_HP`, `SELF_LAST_LOW_HP` (their last Pokémon at a quarter HP or less).

All 25 names are in `include/constants/trainer_slide.h` (prefix `TRAINER_SLIDE_`): crit, super effective, STAB, unaffected, gimmick (Mega, Z, Dynamax, Tera) and first-down variants for both sides.

## Traps

- Only **one end-of-turn slide plays per trainer per turn**; the rest are dropped. Crit, super effective, STAB and unaffected slides are end-of-turn ones, so do not hang a story beat on them.
- `SELF_LAST_LOW_HP` needs the last Pokémon alive at end of turn: a one-hit KO from above a quarter HP skips it. Pair it with `SELF_LAST_SWITCHIN` if the line must always appear.
- `*_LAST_SWITCHIN` fires only after a forced replacement (a faint), never after a voluntary switch.
- End-of-turn slides still run after the finishing blow, so a `DEFENDER_*` crit or super-effective line can appear after the fight is decided.
- **Troglodyte's party order is random per battle** (the pool is shuffled; no Pokémon has `Lead` or `Ace`), so 'first Pokémon down' is SIR BISCUIT or his starter 50/50. A line that names SIR BISCUIT is wrong half the time unless the order is pinned with `Tags: Lead / Tag6` on each starter and `Tags: Ace` on SIR BISCUIT (open question below).
- The Veldris rows are not covered by the upstream battle tests, which use their own table. The Python check and mGBA are the only coverage.

## Text rules

- The battle box is 208 px wide, 2 lines per page. The game wraps battle text itself, so write one plain run of text with no `\n`. A line holds about 200 px of words (8 px is kept for the scroll arrow). A third line scrolls with an arrow rather than being lost.
- Single curly quotes only; write TROGLODYTE literally. The player's name is `{B_PLAYER_NAME}`, **never** `{PLAYER}` (that prints a battle buffer).
- Check with `python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h`. It runs the game's own line-breaker and prints the wrapped widths per row.

## Add a row (3 steps)

1. Add the line to the trainer's block in `src/data/veldris_trainer_slides.h`.
2. Run the check above, then `make -j4`.
3. Fight that trainer once in mGBA (debug menu, Trainers, Try Battle) and add the result to the test log here. Update the Approved table.

## Test log

**2026-10-08, mGBA, throwaway rows (never committed), debug menu Trainers > Try Battle on Troglodyte's fight 1 (id 520):** `BEFORE_FIRST_TURN` works. After the send-outs, Troglodyte's picture (the DP Rich Boy art) slid in from the right with correct colours, the line showed in the battle box with `{B_PLAYER_NAME}` expanded to the real player name (BRENDAN or MAY), it waited for A with no arrow, and the action menu followed. It did not repeat on turn 2. **Not run:** the other triggers (first down, last switch-in, last low HP, the scroll for a third line) and the leaders' blocks; the debug party's Wobbuffet fell asleep on its first move, so no knock-out was seen. Test them when real rows are approved.

## APPROVED lines

None yet.

## PROPOSED options (NOT approved, for the author to pick from)

ALL TEXT BELOW IS PROPOSED (not canon). It is draft material for the author's pick, to live in design/trainer-slides.md until approved, not in the build. Each line gets {PAUSE_UNTIL_PRESS} from the VELDRIS_SLIDE macro. Every line was measured with the ported game line-breaker (208 px box, 2 lines); all fit one page (widest line 195 px). Shape in brackets = pixels per displayed line.

=== TROGLODYTE FIGHT 1, Hollowbrook (TRAINER_TROGLODYTE_HOLLOWBROOK, id 520) ===
Written to work whichever mon leads. BEFORE_FIRST_TURN is left empty on purpose: the field text already introduces him (Hollowbrook_Text_TrogOutside1, TrogPetIntro). Triggers: DEFENDER_TAKES_FIRST_DOWN (his first mon faints), SELF_LAST_SWITCHIN (his last mon comes out), SELF_LAST_LOW_HP (last stand).

Option A, pompous (matches the arc sample 'Fine. You can be my warm-up'):
  FIRST_DOWN: Get up! Get up! You have a pedigree!  [186]
  LAST_SWITCHIN: Fine. Enough games. This one cost more than your house.  [173/112]
  LAST_LOW_HP: Hold still! This is not how it goes in the books!  [133/108]
Option B, petty:
  FIRST_DOWN: That one was not ready! Have you no manners?  [150/83]
  LAST_SWITCHIN: Last one. If it loses, I'm telling Mother.  [128/77]
  LAST_LOW_HP: Wait, wait! I wasn't ready! Nobody said it was timed!  [174/91]
Option C, deadpan posh (closest to dialogue-style 'deadpan and dry'):
  FIRST_DOWN: It has fainted. It does that when it is bored.  [148/85]
  LAST_SWITCHIN: Right. The expensive one. Do try to look impressed.  [146/114]
  LAST_LOW_HP: This is a clerical error. I shall be writing to someone.  [159/115]
If the author pins SIR BISCUIT last (Tags: Ace), add or swap: SELF_LAST_SWITCHIN: SIR BISCUIT, you're up. Please don't embarrass me.  [156/100]

=== TROGLODYTE FIGHT 2, Crestfall (TRAINER_TROGLODYTE_CRESTFALL, id 521) ===
Context: Greta has just beaten him on camera; he fights the player to 'prove it was a fluke' (Scheme 1 draft, also unapproved). Triggers add BEFORE_FIRST_TURN.
Option A, pompous:
  BEFORE_FIRST_TURN: Get my good side, photographer. Both of them are good.  [164/116]
  FIRST_DOWN: Not in front of the photographer! Get up!  [176/37]
  LAST_SWITCHIN: My family pays for these. Do try not to waste them.  [145/116]
  LAST_LOW_HP: Not the noticeboard again! Not twice in one day, damn it!  [161/130]
Option B, petty:
  BEFORE_FIRST_TURN: That leader cheated. You will too. I can tell.  [129/98]
  FIRST_DOWN: Ow. No. That was a practice one. It doesn't count.  [138/114]
  LAST_SWITCHIN: Right, I'm warm now. Look how warm I am. So warm.  [147/94]
  LAST_LOW_HP: It's the hay. It gets in everything. Everyone's eyes!  [184/87]
Option C, deadpan:
  BEFORE_FIRST_TURN: Smile, everyone. Someone is about to go on the noticeboard.  [173/132]
  FIRST_DOWN: That makes two embarrassments today. I am keeping count.  [163/136]
  LAST_SWITCHIN: My last chance. You have as many as you like, I suppose.  [169/116]
  LAST_LOW_HP: Write this down: I was distracted by the smell. Hay, mostly.  [172/129]
If SIR BISCUIT is pinned last: SELF_LAST_SWITCHIN: SIR BISCUIT. Be brave. Mother is watching, somehow.  [154/110]

=== LAST STAND, one per built leader / Elite Four / Champion (all SELF_LAST_LOW_HP) ===
Voices follow design/gyms.md, leader-names.md and dialogue/league.inc. LOW_HP only fires if the last mon is alive at or below a quarter HP at end of turn, so it is a bonus beat, not guaranteed.
  GRETA (TRAINER_CRESTFALL_GRETA, young, sassy, kind): Oh, you're actually good. Don't let it go to your head, sweetheart!  [189/149]
  HACHIMEL (Bug, apologises to every Pokémon): Oh dear. I'm so sorry, little one. Just a little longer, please.  [192/118]
  SANZUFORD (Ghost, dry apprentice): Huh. The living put up more of a fight than I was told.  [152/122]
  HAGANE (Steel, tired foreman, workers at lunch): Lads, a hand? ...Lunch. Of course. Right, I'll manage.  [170/93]
  WAKASAGI (Ice, relaxed fisherman, thermos): Now that's a bite. Hold on while I pour a cup first.  [160/95]
  TOBIN (Flying, vain pilot, 'flight plan'): A little turbulence. Do keep your seat belts fastened.  [170/109]
  ASEBY (Poison, chemist, quality control): This batch is outside tolerance. Please hold while I rework it.  [168/150]
  SUZURAN (Fairy, tougher than she looks): I do wear flowers. I also have thorns. Sorry!  [126/100]
  MIZZLE (Water, big jolly deadpan keeper): Ha ha! That's the sea for you. Giving, then taking. Mostly taking.  [191/141]
  OSSIAN (Dark E4, cheerful undertaker): Lovely! A proper send-off. Mine, I think. Wonderful turnout.  [166/141]
  HYACINTH (Psychic E4, 'I saw it coming'): I saw this coming. I did rather hope I was wrong.  [157/89]
  DUNMORE (Fighting E4, gentle, naps): Whew! Running low. Don't let me sit down. I'll nap!  [142/106]
  DRAYDEN (Dragon E4, kind old man): Gently now, child. They do so hate to lose, you see.  [147/112]
  CYNTHIA (Champion, aged): Splendid. It has been years since my heart raced like this.  [173/127]

Row format once approved (macro form):
    [TRAINER_TROGLODYTE_HOLLOWBROOK] =
    {
        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "It has fainted. It does that when it is bored."),
        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Right. The expensive one. Do try to look impressed."),
        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "This is a clerical error. I shall be writing to someone."),
    },


## Open questions for the author

1. Tone for Troglodyte's fights 1 and 2: pompous (A), petty (B) or deadpan posh (C), or a mix? Which triggers should he use?
2. Troglodyte's party order: always the starter first and SIR BISCUIT last (matches the built field line 'stay back, SIR BISCUIT', allows pet-specific lines), SIR BISCUIT first, or random (then slides cannot name him)?
3. Are the 14 last-stand lines for the leaders, Elite Four and Champion good, or should some also get a first-turn battle cry?
4. Fight 2 options mention the photographer and noticeboard from the unapproved Scheme 1 draft: keep or make generic? One option says 'damn it': keep fights clean or let a Goldsworth swear a little?
5. Slides shorter and more fleeting than the field text (proposal), or allowed to repeat it?
