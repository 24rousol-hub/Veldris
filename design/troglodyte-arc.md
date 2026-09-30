# Troglodyte's arc (beat sheet)

Status: **PROPOSED, all of it.** Nothing here is canon until the author approves it. Facts that do come from the author: he starts contemptuous and may become oblivious and confused after story points that are undecided; his parents are oblivious assholes, the wider family contemptuous; grandfather Gatsby is kind; every scheme fails; no IVs or EVs; his first fight is outside the lab with one Pokémon ([characters.md](characters.md), [game-bible.md](game-bible.md) decision 13).

Sample lines: [dialogue/troglodyte_arc_samples.inc](dialogue/troglodyte_arc_samples.inc) (width-checked, 0 errors, not wired).

## Two alternative arcs (OPTION A and OPTION B, choose one or mix)

Both share the same fights 1 to 3 (contemptuous). They split from fight 4.

**OPTION A: contemptuous, then humbled.**
| Phase | Fights | Mode |
|---|---|---|
| Sneer | 1 to 4 | Looks down on locals, blames the grass, the referee, the player |
| Crack | 5 | Parents watch him lose at home ground. First real shame |
| Work | 6 to 7 | Trains for real (off-screen), drops the pet jokes, still stiff |
| Humbled | 8 | Concedes plainly, writes to his grandfather. Fits the grandfather's post-game thanks |

**OPTION B: oblivious and confused.**
| Phase | Fights | Mode |
|---|---|---|
| Sneer | 1 to 3 | As above |
| Turn | 4 | First story point (see triggers) breaks his script: nothing works the way he was told |
| Drift | 5 to 7 | Polite, bewildered, asks the player what the rules are, repeats his parents' phrases |
| Lost | 8 | Sincerely confused he is there at all. Goes to ask his grandfather |

**Turn triggers (all undecided, pick one or none):** (1) the tower city, when his parents fail to understand a gym either; (2) Scheme 4 collapses and the townsfolk are kind to him anyway; (3) he finds his grandfather's 'GG' note and cannot read it as a message. Each needs a var in [flags.md](flags.md) when chosen; nothing claimed here.

## Schemes 2 to 9

Gym towns and types are **TBD** (the table in [story-outline.md](story-outline.md) is still empty). The types below are **placeholders** only so each joke has a home. All Pokémon, no real animals. Scheme 1 (Crestfall: consultants, hay maze, MILTANK eat the paperwork) is already drafted.

| # | Placeholder type | Setup | Reveal | Collapse |
|---|---|---|---|---|
| 2 | Bug | A polite crew in white suits seals the gym in a tent. | The tent is 'fumigation.' The gym is full of Bug types, which are the point of the gym. | A SPINARAK seals the tent from the inside. The crew is delivered to the Pokémon Center, gift-wrapped in String Shot. |
| 3 | Water | A man installs meters on every tap in town. | He has 'bought the water rights' and will bill the gym per splash. | The Leader's POLITOED calls rain. The meters overflow, the invoice reads minus four hundred. |
| 4 | Electric | 'Premium electricity' vans park outside the gym. | The family cut the town's grid to sell it back at triple cost. | The gym's MAGNETON runs the whole town for free. The vans' lights flicker on and stay on. |
| 5 | Rock | Surveyors stake out the quarry with tiny flags. | It is to become a golf course, with a clubhouse over the gym. | GRAVELER mistake the golf balls for eggs and roll the course flat. The clubhouse sinks politely. |
| 6 | Psychic | Troglodyte's parents arrive with a gift basket (this is the tower city, PROPOSED slot). | They have come to buy the badge for their boy. They cannot see why it is not for sale. | The Leader explains it kindly, twice. The parents tip her, sincerely, and leave confused. |
| 7 | Ghost | A film crew sets up a 'haunting' in the gym at night. | Frat guys in sheets try to scare the Leader out of the building. | A real HAUNTER joins in, better. The sheets leave first. The HAUNTER takes the sheets. |
| 8 | Ice | A new snow machine appears on the mountain lift. | It is meant to bury the gym's road and close it. | The machine freezes solid, then the lift. The hired crew hangs there until the Leader's GLALIE thaws them, at cost. |
| 9 | Dragon | A lawyer hands the Leader a box of 400 permits. | It is every gym's invoice, billed to the last gym: the total of Schemes 1 to 8. | Troglodyte reads the total aloud. Nobody has a response. The Leader signs for it with a DRATINI stamp. |

## Troglodyte's battle schedule

Levels follow the curve in [teams.md](teams.md): 5 at Hollowbrook, 10 to 12 at gym 1, about 60 at the League. He always trails the current leader's ace by a few levels. **No IVs, no EVs.** Each fight is **one trainer entry** using `Pool Prune: Rival Starter`: `Party Size` is the fixed Pokémon plus one, and the three starter versions are tagged `Tag6` (1st on show), `Tag7` (2nd), `Tag8` (3rd) so exactly one survives. Each entry writes the right evolution stage for its level ([story-outline.md](story-outline.md), 'Starters and the lab scene').

Starter lines use Emerald stand-ins until the real species are chosen (Treecko, Torchic, Mudkip evolve at 16 and 36). Fixed species here are **PROPOSED stand-ins** for 'well-bred, poorly trained'.

| # | Where | Story beat | Party | Level range | Starter stage | Fixed team (PROPOSED) |
|---|---|---|---|---|---|---|
| 1 | Outside lab, Hollowbrook | First meeting (PROPOSED, see [teams.md](teams.md)) | 1 (+ optional Sir Biscuit, level 1) | 5 | Basic | none (starter only) |
| 2 | Crestfall | Scheme 1 | 2 | 7 to 8 | Basic | Lillipup 'Sir Biscuit' (7) |
| 3 | Gym town 3 | Scheme 3 | 3 | 18 to 21 | Stage 2 (16) | Sir Biscuit as Herdier, Meowth |
| 4 | Gym town 5 | Scheme 5 | 4 | 28 to 31 | Stage 2 | Herdier, Persian, Kirlia |
| 5 | Tower city | Scheme 6, parents watch | 5 | 37 to 41 | Stage 3 (36) | Stoutland 'Sir Biscuit' (32 min), Persian, Gardevoir, Ponyta |
| 6 | Gym town 7 | Scheme 7 | 6 | 42 to 46 | Stage 3 | Stoutland, Persian, Gardevoir, Rapidash, Gabite |
| 7 | Victory Road | The turn (A) or the drift (B) | 6 | 52 to 56 | Stage 3 | same six, Gabite becomes Garchomp at 48+ (PROPOSED: he cannot control it) |
| 8 | League finale | See note | 6 | 58 to 60 | Stage 3 | same six at the top of the curve |

**Fight 8 depends on open decision 2 (who is Champion).** If Troglodyte is Champion, fight 8 is the Champion fight at 60. If not, cut fight 8 and end the arc at fight 7 or keep him as a fixed E4-lobby scene. Seven encounters is the floor.

**Trainer ids:** eight fights cost 8 ids if new. Reuse vanilla entries (for example the `TRAINER_BRENDAN_*` set) via `#define` per [CLAUDE.md](../CLAUDE.md); nothing here claims ids.

## What he says at each beat

Mode C is contemptuous, A and B per the arcs above. Full lines, each under 208 px, in the `.inc` file. One or two lines here per beat:

| # | Beat | Mode C / A | Mode B |
|---|---|---|---|
| 1 | Lab | 'You can be my warm-up. Try not to cry on the grass.' | same |
| 2 | Crestfall | 'My family paid for this scene. Nobody is enjoying it.' | same |
| 3 | Gym town 3 | 'Go on. Lose politely.' / 'Nobody at home will believe this.' | 'My team is supposed to win. That was the whole plan.' |
| 4 | Gym town 5 | A: 'Five towns of peasants cheering for you. It's frankly rude.' | B: 'I sent the money. I signed the forms. Why does it keep happening?' |
| 5 | Tower city | A: 'I want you to lose where they can see it.' | B: 'Mother says I should be nicer. I don't know how.' |
| 6 | Gym town 7 | A: 'No jokes this time. No dog.' | B: 'You keep winning, and I don't know what you want from me.' |
| 7 | Victory Road | A: 'Fight me. Properly. Please.' | B: 'Everyone keeps telling me the rules. I keep missing them.' |
| 8 | League | A: 'Well fought. Go and be Champion.' | B: 'Did I do it right? I'll go and ask Grandfather.' |

**After the League:** Gatsby thanks the player for setting Troglodyte straight ([characters.md](characters.md)). In Option A that lands as a humbled boy; in Option B as a boy at last asking the right question. Open for the author.

**Swearing:** a little, as punctuation, per [dialogue-style.md](dialogue-style.md). Never at townsfolk.
