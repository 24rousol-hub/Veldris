# Elite Four, Champion, League finale and post-game

Status: **everything here is PROPOSED, not canon.** Only the items marked (author) come from the author. All names are placeholders. Dialogue: [dialogue/league.inc](dialogue/league.inc) (width-checked, not wired). No flag or var is claimed here; see [flags.md](flags.md) before wiring.

Fixed by the author: Elite Four of 4 members; Champion not specified; post-game exists; the grandfather's name (GATSBY GOLDSWORTH) stays hidden until the League is beaten and he then thanks the player; he was meeting the previous region's Champion, an old friend, the day Troglodyte came; no IVs or EVs on any trainer; Pokémon only (no real animals). Open decision 2 (Champion) in [game-bible.md](game-bible.md) still stands.

## Rules for every League team

- 4 to 5 Pokémon per Elite Four member, levels 50 to 58. Champion 6 Pokémon, levels 58 to 62. Troglodyte 6 Pokémon, levels 58 to 62.
- No `IVs:` or `EVs:` lines (author). Species are all in this tree (checked against `include/constants/species.h`). Moves are not chosen here: pick from `gen_9.h` learnsets when the blocks go into `src/data/trainers.party`.
- Trainer ids: the four members, the Champion and the final Troglodyte fight are 6 ids. Only 9 brand-new ids fit and gyms use them, so these should **reuse vanilla Hoenn entries** (CLAUDE.md, 'A new trainer'). The vanilla Sidney, Phoebe, Glacia, Drake and Wallace entries are the natural ones.

## Elite Four, Option A (PROPOSED)

The order is by difficulty, ending in Dragon. One per type, all different from the gym leaders' types so far (Normal is taken by Greta; the other gym types are still TBD, so check this set when they are fixed).

| # | Name | Type | Personality pitch | Size | Levels | Team |
|---|---|---|---|---|---|---|
| 1 | OSSIAN | Ghost | Cheerful undertaker. Cheerful about death, polite about it. | 4 | 50 to 53 | Sableye 50, Banette 51, Froslass 52, Dusknoir 53 |
| 2 | HYACINTH | Ice | Icy manners, secretly keeps snow globes. Deadpan. | 4 | 52 to 55 | Glalie 52, Weavile 53, Walrein 54, Mamoswine 55 |
| 3 | DUNMORE | Fighting | Huge, gentle, bad at puns, naps between rounds. | 5 | 54 to 57 | Breloom 54, Hariyama 55, Heracross 55, Lucario 56, Conkeldurr 57 |
| 4 | MAREN | Dragon | Oldest member, kind and quietly terrifying. Keeps dragons like pets. | 5 | 55 to 58 | Altaria 55, Flygon 56, Kingdra 57, Haxorus 57, Salamence 58 |

**Option B (alternative, PROPOSED, shorter sketch):** Fire (a lazy chef), Electric (a stage magician), Psychic (a shy librarian), Steel (a retired smith, the last member). Sizes 4, 4, 5, 5, levels 50 to 58. Species pools: Fire Magmortar, Arcanine, Houndoom, Ninetales; Electric Electivire, Jolteon, Rotom, Magnezone if added later; Psychic Alakazam, Gardevoir, Gengar as a hybrid; Steel Steelix, Scizor, Skarmory, Metagross, Mawile. Gardevoir here clashes with Troglodyte's team (below), so swap one if this set is used.

## The Champion, three alternatives (PROPOSED)

Troglodyte is **the player's champion-tier rival** in all three: he is the last trainer the player fights before the Champion's chamber, in the League corridor. In Option C he is also the Champion.

### Option A: OTTOLINE, the previous region's Champion, Gatsby's old friend (recommended by me, not decided)

- She holds the seat as the League's **guest Champion**: Veldris's own champion is vacant or retired, and the League asked a past Champion from the previous region to defend the title. The player does not learn she is Gatsby's friend until after the League. The grandfather whereabouts payoff (he was meeting her) then lands as a reveal, not an exposition dump.
- Voice: dry, warm, long in the tooth, respects the grudge ('a grudge makes a good engine').
- Team: Togekiss 59, Starmie 59, Roserade 58, Houndoom 60, Ferrothorn 60, Garchomp 62 (ace). No IVs or EVs.
- Risk: it makes the League a second meeting with someone from outside Veldris, so the Goldsworth plot stays in the wings until the post-game. That suits the grandfather's hidden name.

### Option B: Greta, risen to Champion

- Gym 1 leader, young and moving up fast (author), is the Champion when the player arrives. Payoff for her 'rising quickly' and her sass. Keeps it all in Veldris.
- Team: Skitty 58, Miltank 60, Kangaskhan 60, Chansey 59, Ursaring 61, Snorlax 62 (check each in tree before building). All Normal, as her gym was.
- Risk: she has to leave Crestfall's gym, so the gym needs a new leader or an empty gym in the post-game (and the gym 1 scene must not say she is stuck there).

### Option C: Troglodyte himself, Champion by the family's money

- The Goldsworths bought the seat (their final scheme). The League finale is then the last scheme and the biggest humiliation, and the grandfather's reveal is the aftermath. This reuses open decision 2's first half.
- It forces the contemptuous arc (he gets a title he did not earn) or the oblivious arc (he genuinely thinks he earned it). The 'previous Champion, old friend' line still works as a post-game visitor rather than a fight.
- Risk: no separate surprise Champion; the final fight and the Champion fight are the same battle, so the dramatic beat is one slot short.

## The final Troglodyte battle (PROPOSED)

Place: a corridor outside the Champion's chamber, after MAREN. In Option C it is the chamber itself.

Team (Pool Prune: Rival Starter as in [teams.md](teams.md)): fixed Pokémon Stoutland 58 (SIR BISCUIT, now grown), Gardevoir 59, Milotic 60, Tyranitar 60, Arcanine 60, plus one starter final form, tagged per starter, at level 62 (stand-in Sceptile, Blaziken or Swampert). Party Size 6, the five fixed plus one survivor of the prune. No IVs or EVs. Well-bred, poorly trained: no held items, AI Basic Trainer (or the lowest that makes him lose).

| Beat | Arc A: contemptuous then humbled | Arc B: oblivious and confused |
|---|---|---|
| Arrival | He claims he bought a League pass, calls the player 'the help' (`League_Text_TrogArcA1`) | He didn't think anyone would come (`League_Text_TrogArcB1`) |
| Battle intro | Money and breeding (`TrogArcA2`) | The best are just a matter of having them (`TrogArcB2`) |
| Defeat | Denial, then a real admission: he never worked at it (`TrogArcAHumbled`, `TrogArcAHumbled2`) | Confused why he loses, asks if it is allowed (`TrogArcBConfused`, `TrogArcBConfused2`) |
| Afterwards | He leaves, angry but quiet. Promises to come back 'properly' | He shakes the player's hand, baffled. Promises to try again |

Shared: `League_Text_TrogBattleIntro` and `TrogBiscuit` work for both. Which arc is decided by story points the author has not fixed (characters.md). A single var chooses the arc, read at the finale.

## Hall of Fame

The standard flow: the Champion falls, the player walks in, the Hall of Fame records the team, the credits roll, and the save sets `FLAG_SYS_GAME_CLEAR` (used by the grandfather's after-League lines). Lines: `League_Text_HofAttendant`, and a call from Fennick (`League_Text_HofFennickCall`) once the player is back in Hollowbrook. Art and the Hall of Fame stage are vanilla, so this costs no engine edit. The credits currently read `VAR_STARTER_MON` (story-outline.md), so check the fourth starter there.

## Post-game

### Grandfather Gatsby reveal scene (author's beats, wording PROPOSED)

1. After the Hall of Fame, the town `OnTransition` clears the hide flag (`FLAG_SYS_GAME_CLEAR` set) and the door note 'GG' is gone. The house is open for the first time.
2. The player walks into the house. Gatsby thanks them for setting Troglodyte straight; his lines already exist (`Hollowbrook_Text_GrandpaLeague1`, `GrandpaLeague2`, `GrandpaLeagueName`) and are **not repeated here**.
3. **New scene, the reunion (PROPOSED):** OTTOLINE arrives at the big door (`PostGame_Text_OttolineArrives`). The two old friends greet each other (`GatsbyReunion1` to `3`). Gatsby explains he was with her the day Troglodyte came and nobody knew, and thanks the player again (`GatsbyThanks`). In Options B and C she is simply a visiting old friend from the previous region, with no effect on the League.
4. No fight in the reunion. Her fight, if she is not the Champion, is a rematch reward.

### What unlocks (PROPOSED)

- Gatsby's house and its interior.
- Elite Four and Champion rematches at higher levels (same species plus one, levels 60 to 70).
- The previous Champion's rematch (Ottoline) at her house or a League lounge.
- Any locked routes or gates that only open post-game (TBD when maps exist).
- The Goldsworth tower's top floor (if it is built), as the epilogue location.

### Post-game activities (short list, PROPOSED)

1. **Rematches:** every gym leader and the Elite Four, at a scaled level, via `cleartrainerflag` per fight.
2. **Previous Champion visit:** Ottoline in Hollowbrook, a rematch and a short story told over tea.
3. **Goldsworth family epilogue:** the parents in the tower are baffled by the board; the wider family are humiliated but unchanged; Troglodyte has a job (`PostGame_Text_TrogEpilogue`, `GoldsworthEpilogue`). In Arc A he is sullen but trying; in Arc B he is puzzled and earnest.
4. **The grandfather's kettle:** a recurring tea scene with small rewards (a berry, a TM), optional.
5. **A rival rematch:** Troglodyte at higher level, one per region area, to keep the joke going.

## Open questions for the author

1. Which Champion option (A, B or C)? This also decides whether the previous Champion fights or just visits.
2. Which Elite Four set (A or B), and do their types clash with the gym types once fixed?
3. Which arc for Troglodyte, and which story points trigger the change?
4. Do these use vanilla trainer entries (recommended) or new ids?
5. Does the post-game reunion need a League lounge map, or just Gatsby's house?
