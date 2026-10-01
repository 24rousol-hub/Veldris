# Elite Four, Champion, League finale and post-game

Status: **everything here is PROPOSED, not canon.** Only the items marked (author) come from the author. All names are placeholders. Dialogue: [dialogue/league.inc](dialogue/league.inc) (width-checked, not wired). No flag or var is claimed here; see [flags.md](flags.md) before wiring.

Fixed by the author: Elite Four of 4 members; the Champion is an aged Cynthia (2026-10-01); post-game exists; the grandfather's name (GATSBY GOLDSWORTH) stays hidden until the League is beaten and he then thanks the player; he was meeting the previous region's Champion, an old friend, the day Troglodyte came; no IVs or EVs on any trainer; Pokémon only (no real animals). Open decision 2 (Champion) in [game-bible.md](game-bible.md) should be marked decided (not edited here).

## Rules for every League team

- Level scale (author, 2026-10-01): the Elite Four starts at level 65 and the League ends at 75 with the Champion. Elite Four sizes 5, 5, 5, 6. Troglodyte's final fight is just before the Champion: 6 Pokémon, about levels 68 to 72. Champion 6 Pokémon, levels 73 to 75.
- No `IVs:` or `EVs:` lines (author). Species are all in this tree (checked against `include/constants/species.h`). Moves are not chosen here: pick from `gen_9.h` learnsets when the blocks go into `src/data/trainers.party`.
- Trainer ids: the four members, the Champion and the final Troglodyte fight are 6 ids. Only 9 brand-new ids fit and gyms use them, so these should **reuse vanilla Hoenn entries** (CLAUDE.md, 'A new trainer'). The vanilla Sidney, Phoebe, Glacia, Drake and Wallace entries are the natural ones.

## Elite Four, Option A (default, PROPOSED; types adjusted 2026-10-01)

The order is by difficulty, ending in Dragon. Gym type order is now set (author): B = Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water. The original Ghost and Ice members clashed with gyms 3 and 5, so they are now **Dark** (replaces Ghost) and **Psychic** (replaces Ice). Fighting and Dragon stay. Names are kept.

| # | Name | Type | Personality pitch | Size | Levels | Team |
|---|---|---|---|---|---|---|
| 1 | OSSIAN | Dark | Cheerful undertaker. Cheerful about death, polite about it. Keeps a crow on the hearse. | 5 | 65 to 66 | Mightyena 65, Houndoom 65, Honchkrow 65, Krookodile 66, Absol 66 |
| 2 | HYACINTH | Psychic | Icy manners, secretly keeps snow globes. Deadpan, always seems to know what you will do. | 5 | 66 to 68 | Espeon 66, Xatu 66, Slowbro 67, Reuniclus 67, Alakazam 68 |
| 3 | DUNMORE | Fighting | Huge, gentle, bad at puns, naps between rounds. | 5 | 68 to 70 | Breloom 68, Hariyama 68, Heracross 69, Machamp 69, Conkeldurr 70 |
| 4 | MAREN | Dragon | Oldest member, kind and quietly terrifying. Keeps dragons like pets. | 6 | 69 to 71 | Altaria 69, Flygon 69, Kingdra 70, Haxorus 70, Salamence 71, Dragonite 71 |

Lucario moved out of DUNMORE's team because it belongs to the Champion. Gardevoir stays Troglodyte's, so HYACINTH avoids it.

**Option B (not chosen as default, PROPOSED, shorter sketch):** Fire (a lazy chef), Electric (a stage magician), Psychic (a shy librarian), Steel (a retired smith). Steel would now clash with gym 4. Levels would need rescaling to 65 to 71.

## The Champion: an aged CYNTHIA (author, 2026-10-01)

Troglodyte is **not** the Champion. He is the last trainer the player fights before the Champion's chamber, in the League corridor.

### CYNTHIA, the previous region's Champion, Gatsby's old friend (author)

- She is the Sinnoh Champion from the Pokémon games, now old: the previous region's Champion and Gatsby's old friend. She holds the seat as the League's **guest, defending Champion** in Veldris: Veldris's own champion is vacant or retired, and the League asked a past Champion to defend the title. The player does not learn she is Gatsby's friend until after the League. The grandfather whereabouts payoff (he was meeting her) then lands as a reveal, not an exposition dump.
- Voice: dry, warm, sharp, long in the tooth, calm, a bit grandmotherly and still terrifying. Respects the grudge ('a grudge makes a good engine').
- Team (6, levels 73 to 75, signature flavour aged up, no IVs or EVs, Pokémon only): Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 (ace).
- Risk: it makes the League a second meeting with someone from outside Veldris, so the Goldsworth plot stays in the wings until the post-game. That suits the grandfather's hidden name.

### Not chosen

Greta as Champion (old Option B) and Troglodyte as Champion (old Option C) were dropped by the author. Their dialogue is gone from `league.inc`.

## The final Troglodyte battle (Arc A, author-chosen)

Place: a corridor outside the Champion's chamber, after MAREN.

Team (Pool Prune: Rival Starter as in [teams.md](teams.md)): fixed Pokémon Stoutland 68 (SIR BISCUIT, now grown), Gardevoir 69, Vaporeon 70, Tyranitar 70, Arcanine 70, plus one starter final form, tagged per starter, at level 72 (stand-in Sceptile, Blaziken or Swampert). Party Size 6, the five fixed plus one survivor of the prune. Milotic moved to the Champion. No IVs or EVs. Well-bred, poorly trained: no held items, AI Basic Trainer (or the lowest that makes him lose).

| Beat | Arc A: contemptuous then humbled |
|---|---|
| Arrival | He claims he bought a League pass, calls the player 'the help' (`League_Text_TrogArcA1`) |
| Battle intro | Money and breeding (`TrogArcA2`) |
| Defeat | Denial, then a real admission: he never worked at it (`TrogArcADefeat`, `TrogArcAHumbled`) |
| Afterwards | He leaves, angry but quiet. Promises to come back 'properly' (`TrogArcAHumbled2`) |

Shared: `League_Text_TrogBattleIntro` and `TrogBiscuit`. Arc B (oblivious) was not chosen; its labels stay in `league.inc` marked UNUSED.

## Hall of Fame

The standard flow: the Champion falls, the player walks in, the Hall of Fame records the team, the credits roll, and the save sets `FLAG_SYS_GAME_CLEAR` (used by the grandfather's after-League lines). Lines: `League_Text_HofAttendant`, and a call from Fennick (`League_Text_HofFennickCall`) once the player is back in Hollowbrook. Art and the Hall of Fame stage are vanilla, so this costs no engine edit. The credits currently read `VAR_STARTER_MON` (story-outline.md), so check the fourth starter there.

## Post-game

### Grandfather Gatsby reveal scene (author's beats, wording PROPOSED)

1. After the Hall of Fame, the town `OnTransition` clears the hide flag (`FLAG_SYS_GAME_CLEAR` set) and the door note 'GG' is gone. The house is open for the first time.
2. The player walks into the house. Gatsby thanks them for setting Troglodyte straight; his lines already exist (`Hollowbrook_Text_GrandpaLeague1`, `GrandpaLeague2`, `GrandpaLeagueName`) and are **not repeated here**.
3. **New scene, the reunion (PROPOSED):** CYNTHIA arrives at the big door (`PostGame_Text_CynthiaArrives`). The two old friends greet each other (`GatsbyReunion1` to `3`). Gatsby explains he was with her the day Troglodyte came and nobody knew, and thanks the player again (`GatsbyThanks`).
4. No fight in the reunion. Her rematch comes later, as a reward.

### What unlocks (PROPOSED)

- Gatsby's house and its interior.
- Elite Four and Champion rematches at higher levels (same species plus one, levels 70 to 85).
- The previous Champion's rematch (Cynthia) at her house or a League lounge.
- Any locked routes or gates that only open post-game (TBD when maps exist).
- The Goldsworth tower's top floor (if it is built), as the epilogue location.

### Post-game activities (short list, PROPOSED)

1. **Rematches:** every gym leader and the Elite Four, at a scaled level, via `cleartrainerflag` per fight.
2. **Previous Champion visit:** Cynthia in Hollowbrook, a rematch and a short story told over tea.
3. **Goldsworth family epilogue:** the parents in the tower are baffled by the board; the wider family are humiliated but unchanged; Troglodyte has a job (`PostGame_Text_TrogEpilogue`, `GoldsworthEpilogue`). He is sullen but trying (Arc A).
4. **The grandfather's kettle:** a recurring tea scene with small rewards (a berry, a TM), optional.
5. **A rival rematch:** Troglodyte at higher level, one per region area, to keep the joke going.

## Open questions for the author

1. Which Elite Four set stays (A as adjusted is the default)? Do the new Dark and Psychic types need a second look once all gym leaders are written?
2. Which story points trigger Troglodyte's later change, if any?
3. Do these use vanilla trainer entries (recommended) or new ids?
4. Does the post-game reunion need a League lounge map, or just Gatsby's house?
