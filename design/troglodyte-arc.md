# Troglodyte's arc (beat sheet)

Status: **AUTHOR DECISIONS (2026-10-01)** are marked as such. Everything else here (species, exact levels, scheme details, lines) stays **PROPOSED** until approved. Fixed facts from the author: he starts contemptuous; his parents are oblivious assholes, the wider family contemptuous; grandfather Gatsby is kind; every scheme fails; no IVs or EVs; his first fight is outside the lab with one Pokémon ([characters.md](characters.md), [game-bible.md](game-bible.md) decision 13).

Sample lines: [dialogue/troglodyte_arc_samples.inc](dialogue/troglodyte_arc_samples.inc) (width-checked, 0 errors, not wired).

## Decisions (author, 2026-10-01)

1. **Arc A: contemptuous, then humbled.** Arc B is not chosen (see the appendix).
2. **Gym order (Option B):** gym 1 Normal, then 2 Bug, 3 Ghost, 4 Steel, 5 Ice, 6 Flying, 7 Poison, 8 Fairy, 9 Water. Gym 6 is in the skyscraper city where Troglodyte's parents live.
3. **Level curve:** gym 1 leader ace 12, gym 9 leader ace 60, Elite Four starts at 65, Champion (an aged Cynthia, not Troglodyte) at 75. Troglodyte's last fight is just before the Champion, at about 68 to 72.
4. Fight 8 is the finale before Cynthia.

## Arc A

| Phase | Fights | Mode |
|---|---|---|
| Sneer | 1 to 4 | Looks down on locals, blames the grass, the referee, the player |
| Crack | 5 | Gym 6: his parents watch him lose, and fail to buy the badge. First real shame |
| Work | 6 to 7 | Trains for real (off-screen), drops the pet jokes, still stiff |
| Humbled | 8 | Concedes plainly, writes to his grandfather. Fits Gatsby's post-game thanks |

No story-point triggers or vars are needed: the phases hang on fight numbers. Nothing claimed in [flags.md](flags.md).

## Schemes 2 to 9

All Pokémon, no real animals. Scheme 1 (Crestfall: consultants, hay maze, MILTANK eat the paperwork) is already drafted. Format: deadpan setup, reveal, collapse. Leader details here are PROPOSED.

| # | Gym type and town | Setup | Reveal | Collapse |
|---|---|---|---|---|
| 2 | Bug | A polite crew in white suits seals the gym in a tent. | The tent is 'fumigation.' The gym is full of Bug types, which are the point of the gym. | A SPINARAK seals the tent from the inside. The crew is delivered to the Pokémon Center, gift-wrapped in String Shot. |
| 3 | Ghost | A film crew sets up a 'haunting' in the gym at night. | Frat guys in sheets try to scare the Leader out of the building. | A real HAUNTER joins in, better. The sheets leave first. The HAUNTER takes the sheets. |
| 4 | Steel (foundry) | Men in hard hats tag every beam of the foundry with numbered stickers. | The gym is to be declared 'scrap' and hauled off by crane, so the family can buy the lot cheap. | The Leader's MAGNEZONE takes hold of the crane and every truck. They fold into one neat cube outside the door, with a receipt. |
| 5 | Ice (frozen lake, fisherman Leader) | A man drills tiny holes across the lake and plants a flag in each. | He has 'bought the angling rights' and will close the lake to anyone without a membership. | The drill rig freezes in place, then the dock. The crew stands on a floating slab until the Leader's GLALIE thaws them, and sells them soup at cost. |
| 6 | Flying (skyscraper city) | Troglodyte's parents arrive with a gift basket. | They have come to buy the badge for their boy. They cannot see why it is not for sale. | The Leader explains it kindly, twice. The parents tip her, sincerely, and leave confused. |
| 7 | Poison (chemist Leader) | Inspectors in hazmat suits arrive with clipboards and a very official stamp. | A 'regulatory review' lists 47 violations, written before they arrived, meant to close the gym. | The Leader's WEEZING lets out one polite Smog. The suits are not rated for it. Only the clipboards leave in good order. |
| 8 | Fairy (florist glade) | Surveyors stake orange flags between the flower beds. | It is to be 'Glade Heights,' luxury condominiums with a meadow view. | The Leader's FLORGES turns every stake into a sapling and the blueprints into a hedge. The developers buy a bouquet and leave. |
| 9 | Water (lighthouse) | A lawyer hands the Leader a box of 400 permits and invoices. | It is every gym's invoice, billed to the last gym: the total of Schemes 1 to 8. | Troglodyte reads the total aloud. Nobody has a response. The Leader's LAPRAS carries the box out to sea, and he signs for it with a PSYDUCK stamp. |

**Cutscene-only Pokémon (author, 2026-10-01).** The Pokémon that win the schemes (Scheme 4 MAGNEZONE, Scheme 5 GLALIE, Scheme 8 FLORGES, Scheme 9 LAPRAS) are **cutscene-only**: they belong to the gym's staff or a local (a garden warden's FLORGES, a ferry LAPRAS) and never appear in the leader's battle team. So the built teams in [trainer-roster.md](trainer-roster.md) do not change. Scheme 9's leader MIZZLE is a man: where the table says 'she', read 'he'.

Notes: Scheme 3's old water joke (meters, POLITOED rain, invoice of minus four hundred) is dropped. The 'minus four hundred' could return as the Scheme 9 total if the author likes it. The old Electric, Rock, Psychic and Dragon schemes are retired with their types.

## Level curve and Troglodyte's battle schedule

**Curve (author, 2026-10-01):** gym 1 ace 12, gym 9 ace 60. The in-between aces below are PROPOSED, in even steps of 6.

| Gym | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | E4 | Champion |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Leader ace | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 65 start | 75 |

He trails the current leader's ace by a few levels. **No IVs, no EVs.** Each fight is **one trainer entry** using `Pool Prune: Rival Starter` (kept): `Party Size` is the fixed Pokémon plus one, and the three starter versions are tagged `Tag6` (1st on show), `Tag7` (2nd), `Tag8` (3rd) so exactly one survives. Each entry writes the right evolution stage for its level ([story-outline.md](story-outline.md), 'Starters and the lab scene'). Party size grows from 1 to 6 at fight 6.

Starter lines use Emerald stand-ins until the real species are chosen (Treecko, Torchic, Mudkip evolve at 16 and 36). Fixed species are **PROPOSED stand-ins** for 'well-bred, poorly trained'. Evolution levels checked against the stand-ins: Lillipup 16 and 32, Ralts 20 and 30, Eevee (Water Stone, any level), Litleo 35, Larvitar 30 and Pupitar 55. **Fixed 2026-10-01 (author): Troglodyte no longer has Garchomp.** Cynthia's ace is Garchomp, so his later fights now build up to the `postgame.md` team (Stoutland, Gardevoir, Vaporeon, Tyranitar, Pyroar plus his starter).

| # | Where | Behind ace | Party | Level range | Starter stage | Fixed team (PROPOSED) |
|---|---|---|---|---|---|---|
| 1 | Outside lab, Hollowbrook | n/a | 1 (+ optional Sir Biscuit, level 1) | 5 | Basic | none (starter only) |
| 2 | Gym 1, Crestfall (Scheme 1) | ace 12 | 2 | 8 to 9 | Basic | Lillipup 'Sir Biscuit' (7 to 8) |
| 3 | Gym 3, Ghost (Scheme 3) | ace 25 | 3 | 20 to 22 | Stage 2 (16) | Sir Biscuit as Herdier, Eevee |
| 4 | Gym 5, Ice (Scheme 5) | ace 37 | 4 | 30 to 33 | Stage 2 | Herdier, Vaporeon (he bought a Water Stone), Kirlia |
| 5 | Gym 6, Flying (Scheme 6, parents watch) | ace 42 | 5 | 37 to 40 | Stage 3 (36) | Stoutland 'Sir Biscuit' (32 min), Vaporeon, Gardevoir, Pyroar |
| 6 | Gym 7, Poison (Scheme 7) | ace 48 | 6 | 43 to 46 | Stage 3 | Stoutland, Vaporeon, Gardevoir, Pyroar, Pupitar |
| 7 | Victory Road (R20) | ace 60 | 6 | 55 to 57 | Stage 3 | same six, Pupitar has become Tyranitar |
| 8 | Finale, just before the Champion | E4 65 | 6 | 68 to 72 | Stage 3 | Stoutland 68, Gardevoir 69, Vaporeon 70, Tyranitar 70, Pyroar 70, starter 72 ([postgame.md](postgame.md)). **No Garchomp: that is Cynthia's ace** |

Fight 8 is fixed as the finale before Cynthia (open decision 2 in [game-bible.md](game-bible.md) is settled on the Champion: not Troglodyte). Eight encounters. Fights fall at gyms 1, 3, 5, 6, 7 only, so he is not at every gym; the other gyms only get the scheme.

**Trainer ids:** eight fights cost 8 ids if new. Reuse vanilla entries (for example the `TRAINER_BRENDAN_*` set) via `#define` per [CLAUDE.md](../CLAUDE.md); nothing here claims ids. Blocks for fights 1 and 2 in [teams.md](teams.md) still show level 8 for fight 2 and Sir Biscuit at 7: both fit the new range (8 to 9, 7 to 8) and are untouched.

## What he says at each beat (Arc A)

Full lines, each under 208 px, in the `.inc` file. Labels are unchanged from the earlier draft.

| # | Beat | Phase | Sample line |
|---|---|---|---|
| 1 | Lab | Sneer | 'Fine. You can be my warm-up. Try not to cry on the grass.' |
| 2 | Gym 1, Crestfall | Sneer | 'My family paid for this scene. Nobody is enjoying it.' |
| 3 | Gym 3, Ghost | Sneer | 'Go on. Lose politely.' / 'Nobody at home will believe this.' |
| 4 | Gym 5, Ice | Sneer | 'Five towns of peasants cheering for you. It's frankly rude.' |
| 5 | Gym 6, Flying | Crack | 'I want you to lose where they can see it.' / after: 'Nobody has ever said no to him kindly. I didn't like it.' |
| 6 | Gym 7, Poison | Work | 'No jokes this time. No dog.' |
| 7 | Victory Road | Work | 'Fight me. Properly. Please.' |
| 8 | Finale, before Cynthia | Humbled | 'Well fought. I mean it. Go and beat her. I'll write to Grandfather.' / after: 'I was a prat. You knew.' |

**After the League:** Gatsby thanks the player for setting Troglodyte straight ([characters.md](characters.md)). Under Arc A this lands as a humbled boy.

**Swearing:** a little, as punctuation, per [dialogue-style.md](dialogue-style.md). Never at townsfolk. Note: [dialogue-style.md](dialogue-style.md) and [characters.md](characters.md) still describe the contemptuous-or-oblivious option as open. They should be updated to say Arc A is chosen when the author next approves a doc pass (not done here).

## Appendix: Arc B (NOT CHOSEN)

Kept for reference only. Arc B was 'oblivious and confused': the same fights 1 to 3, then Turn (fight 4, his script breaks), Drift (5 to 7, polite and bewildered, asks the player the rules, repeats his parents' phrases), Lost (8, goes to ask his grandfather). Possible Turn triggers were the tower city, a Scheme 4 collapse met with kindness, or Gatsby's 'GG' note. Its sample lines survive in the `.inc` under a comment marked UNUSED (the `_B` labels). Do not wire them in.
