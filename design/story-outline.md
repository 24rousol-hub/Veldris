# Story outline

Status: **PROPOSED** unless marked. Only items marked (author) come from the author.

## The scheme formula

Every gym gets one Goldsworth scheme. Keep the beats the same so the joke builds:

1. **Setup.** The player notices something off in town (a stranger, a new sign, a shut door).
2. **Reveal.** The scheme becomes obvious. It is elaborate and expensive.
3. **Collapse.** It fails, through its own flaw, the townsfolk, or the leader. It never hurts an innocent.
4. **Troglodyte shows up** to see it work. It has not.
5. **Battle.** Troglodyte loses. The gym battle follows as normal.
6. **Humiliation beat.** A short line that lets the player enjoy it.

## The path is not decided (author, 2026-09-29)

The author has not decided which path the story takes. What is fixed: the Goldsworths are one of the obstacles, and Troglodyte starts contemptuous and may become oblivious and confused after certain story points that are not decided ([characters.md](characters.md)). Anything below Act I is a guess.

## Goldsworth presence (author notes 2026-09-29; details PROPOSED)

- **A Goldsworth house in every city** (author). **Towns get none, except Hollowbrook** (author), where the house is the grandfather's because it is his home town. A house is the one place in a warm settlement that is not warm, apart from the grandfather's, who is kind. Each house is a small interior with one to three NPCs and no trainer ids (open decision 11 in [game-bible.md](game-bible.md)). All of them share one layout ([map-plan.md](map-plan.md)), so the houses differ in who is inside and what they say.
- **The skyscraper** (author): the family business, in one **city** (TBD), and **Troglodyte's parents are in it** (author). They are oblivious rather than contemptuous: they live in luxury and do not understand the lower classes, unlike the rest of the family, who look down on them on purpose (author). Their schemes can come from not understanding what a gym or a town is (PROPOSED). That city has no separate house. What the player does there is TBD. It has several floors, which are separate interior maps.
- **The grandfather** (author): a kind old man, the former family head, retired to Hollowbrook because of his health. He was supposed to meet Troglodyte in Hollowbrook and was not there, which sets off the lab scene (author). See [characters.md](characters.md).
- **Who else is inside:** rich frat guys who are assholes and dislike the lower classes, and they swear a little (author). See [dialogue-style.md](dialogue-style.md).
- A house can carry its city's scheme beat (the 'setup' and 'reveal' in the formula above) or a small joke on its own. Which is up to each city.

## Act I: Hollowbrook to Crestfall  (first 3 towns, 3 routes)

| Beat | Where | Notes | Status |
|---|---|---|---|
| Troglodyte at Fennick's lab | Hollowbrook | **(author, 2026-09-29)** Troglodyte is in Hollowbrook to meet his grandfather, who was not there at the time. He takes his frustration out on Fennick and forces him to give him a Pokémon. It is one of three at random. Fennick then apologises to the player by revealing a fourth starter, and the player picks from what is left (author). Where the grandfather was, and how the rest of the scene plays out, are TBD | Beat fixed by the author, details PROPOSED |
| Intro and Prof. Fennick | Start town | Intro is C-driven. Text drafted in `data/text/birch_speech.inc` (built, fits the text box). Portrait art still shows Birch | BUILT (text). Tone approved by the author; portrait art still to do |
| Player learns Troglodyte got a head start | Start town | Sets the motive. The scene above shows it, and the grandfather in Hollowbrook's Goldsworth house could fill in the rest | PROPOSED |
| Route 1, first trainers | Route 1 | Gentle, farm-country | PROPOSED |
| Town 2 | Town 2 | Pokémon Center and shop. A Goldsworth house only if it turns out to be a city (open decision 12) | PROPOSED |
| Route 2 | Route 2 | Route leads to the gym town | PROPOSED |
| **Scheme 1 at Crestfall** | Crestfall | See below | PROPOSED |
| Gym 1: Greta (Normal) | Crestfall | `TRAINER_CRESTFALL_GRETA` | author fixed leader and type |
| Route 3 gated | Route 3 | Leads on to town 4. Blocked for now | PROPOSED |

### Starters and the lab scene (author, 2026-09-29; the build is PROPOSED)

The draft dialogue for this scene, and for the rest of Hollowbrook, is in [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc) (PROPOSED).

**What the author fixed:**
- There are **four** starters. Three are on show in the lab.
- Troglodyte forces a Pokémon out of Fennick and takes **one of the three on show, at random**.
- Fennick then reveals the **fourth** as an apology to the player, and the player picks from what is left.
- **Which species: undecided.** The author will decide once the Hollowbrook map, the lab and the houses are done. Until then Emerald's Treecko, Torchic and Mudkip are stand-ins.

**How it can be built, and what it costs (checked in this tree):**
- **The vanilla starter screen cannot do it.** `src/starter_choose.c` is hard-wired to exactly three balls (`STARTER_MON_COUNT` is 3, and the ball positions, labels and left/right selection all assume it). A fourth ball, a ball already taken and a mid-scene reveal would mean rewriting that screen in C, an engine edit.
- **Proposal: Poké Ball objects on a table in the lab, script only.** Four ball objects on a table, the fourth hidden by a flag. The scene: Troglodyte walks to a random one of the three and takes it (its ball disappears), Fennick apologises and the fourth ball appears, and the player talks to a ball, confirms, and gets the Pokémon with `givemon`. That is how Oak's lab works in FRLG. That lab's script, `data/maps/PalletTown_ProfessorOaksLab_Frlg/scripts.inc`, is in the tree as a reference (it is not built into this ROM). No engine edit.
- **The random pick:** `random 3` in the lab script (the command exists, for example in `data/scripts/interview.inc`), stored in one spare var. Every later Troglodyte battle switches on that var, the way vanilla switches on `VAR_STARTER_MON` in `data/maps/Route103/scripts.inc`. Troglodyte can only have one of the three on show, so he needs three variants per battle, not four.
- **Trainer ids:** three per Troglodyte battle. With 9 spare ids the likely answer is to reuse the 15 vanilla `TRAINER_BRENDAN_*` ids, since nothing in `src/` refers to them by name. See open decisions 3, 6 and 14 in [game-bible.md](game-bible.md).
- **Flags and vars (planned, not claimed):** one var for Troglodyte's pick, and a flag or two for the lab scene (fourth ball revealed, player has chosen).
- **`VAR_STARTER_MON` and `GetStarterPokemon`** hold three species (`sStarterMon[3]`), and `credits.c`, `field_specials.c` and `battle_setup.c` read them. Check what needs them once the species are chosen. If the player can end up with the fourth species, the table may need a fourth entry (a one-line engine edit).
- **The lab map has to support it.** It needs a table with room for four ball objects. `Elm's Lab.png` has a table (green, three tiles wide), so paint it at least four wide, with a free tile in front of each ball spot. The balls are events, and I place them. See [map-plan.md](map-plan.md).

### Scheme 1 (PROPOSED example, easy to replace)

Hired "efficiency consultants" turn up to condemn Greta's farmyard gym. Greta lets them inspect it. They get lost in the hay maze, and the inspection ends when her livestock take over the paperwork. Troglodyte arrives to watch, finds the consultants tangled in the barn, and has to battle anyway.

## Acts II to IV

| Act | Gyms | Notes |
|---|---|---|
| II | 2 to 4 | TBD |
| III | 5 to 7 | TBD |
| IV | 8 and 9, Elite Four, Champion | See decision 1 (resolved: 9 badges) and 2 (Champion) in [game-bible.md](game-bible.md) |

## Schemes 2 to 9

| # | Gym town | Type | Scheme | Status |
|---|---|---|---|---|
| 1 | Crestfall | Normal | See above | PROPOSED |
| 2 to 9 | TBD | TBD | TBD | Not started |

## Post-game

TBD by the author.

## Cutscene rule

Cutscenes fire from `coord_event` triggers, not `MAP_SCRIPT_ON_TRANSITION`. Every trigger needs a flag or var in [flags.md](flags.md).
