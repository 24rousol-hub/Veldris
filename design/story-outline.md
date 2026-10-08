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

The author has not decided which path the story takes. **Update (author, 2026-10-01): Troglodyte follows Arc A (contemptuous, then humbled), and the Champion is an aged Cynthia. See [troglodyte-arc.md](troglodyte-arc.md) and [postgame.md](postgame.md).** What is fixed: the Goldsworths are one of the obstacles, and Troglodyte starts contemptuous and may become oblivious and confused after certain story points that are not decided ([characters.md](characters.md)). Anything below Act I is a guess.

## Goldsworth presence (author notes 2026-09-29; details PROPOSED)

- **A Goldsworth house in every city** (author). **Towns get none, except Hollowbrook** (author), where the house is the grandfather's because it is his home town. A house is the one place in a warm settlement that is not warm, apart from the grandfather's, who is kind. Each house is a small interior with one to three NPCs and no trainer ids (open decision 11 in [game-bible.md](game-bible.md)). All of them share one layout ([map-plan.md](map-plan.md)), so the houses differ in who is inside and what they say.
- **The skyscraper** (author): the family business, in one **city** (TBD), and **Troglodyte's parents are in it** (author). They are oblivious rather than contemptuous: they live in luxury and do not understand the lower classes, unlike the rest of the family, who look down on them on purpose (author). Their schemes can come from not understanding what a gym or a town is (PROPOSED). That city has no separate house. What the player does there is TBD. It has several floors, which are separate interior maps.
- **The grandfather** (author): a kind old man, the former family head, retired to Hollowbrook because of his health. He was supposed to meet Troglodyte in Hollowbrook and was not there, which sets off the lab scene (author). See [characters.md](characters.md).
- **Who else is inside:** rich frat guys who are assholes and dislike the lower classes, and they swear a little (author). See [dialogue-style.md](dialogue-style.md).
- A house can carry its city's scheme beat (the 'setup' and 'reveal' in the formula above) or a small joke on its own. Which is up to each city.

## Act I: Hollowbrook to Crestfall  (first 3 towns, 3 routes)

| Beat | Where | Notes | Status |
|---|---|---|---|
| Troglodyte at Fennick's lab | Hollowbrook | **(author, 2026-09-29)** Troglodyte is in Hollowbrook to meet his grandfather, who was not there at the time. He takes his frustration out on Fennick and forces him to give him a Pokémon. It is one of three at random. Fennick then apologises to the player by revealing a fourth starter, and the player picks from what is left (author). Nobody in the family knows where the grandfather was (author); the post-game reveals he was meeting the previous region's Champion, an old friend (author). How the rest of the scene plays out is TBD | Beat fixed by the author, details PROPOSED |
| Intro and Prof. Fennick | Start town | Intro is C-driven. Text drafted in `data/text/birch_speech.inc` (built, fits the text box). Portrait art still shows Birch | BUILT (text). Tone approved by the author; portrait art still to do |
| Player learns Troglodyte got a head start | Start town | Sets the motive. The scene above shows it, and the grandfather in Hollowbrook's Goldsworth house could fill in the rest | PROPOSED |
| Route 1, first trainers | Route 1 | Gentle, farm-country. Now ends in Crestfall; the Scheme 1 surveyors walk it | PROPOSED |
| **Scheme 1 at Crestfall** | Crestfall | See below | PROPOSED |
| Gym 1: Greta (Normal), STANDARD BADGE | Crestfall | `TRAINER_CRESTFALL_GRETA`, 2 gym trainers | author fixed leader, type, badge name and trainer count |
| Route 8 gated | Route 8 (Wendlebury to Briarwick) | A ranger closes it over odd happenings in Mothwood; opens after badge 2 (author, 2026-10-08); Mothwood branches off it; R9 dropped | Author |
| Mothwood event | Mothwood | Required (author). The Drowned Crown steal a Time Gear-like piece of Dialga's seal; time stops in the forest; Shaymin encounter (leaning), Celebi post-game. See [factions.md](factions.md) | Author, details PROPOSED |
| Route 3 gated | Route 3 | **Blocked by the Commons** (the author wants the big bad here, 2026-10-04). The player goes to Wendlebury first; Route 3 opens after the Wendlebury beat. See [factions.md](factions.md) | Block by the villains: author. Details PROPOSED |

### The grandfather's whereabouts in Hollowbrook (author, 2026-09-29; scripting is PROPOSED)

| When | Where he is | How it is done (proposal) |
|---|---|---|
| Start until the lab scene | Not in town. The house door is locked, with a note signed 'GG' | Object hidden by a flag; the door is a sign/trigger that reads the note |
| After the lab scene, before the first badge | An old man on a bench outside the house, unnamed | The flag is cleared when the lab scene ends |
| After the first badge until the League is beaten | Not in town, even if the player returns | Town `OnTransition`: if `FLAG_BADGE01_GET` is set and `FLAG_SYS_GAME_CLEAR` is not, set the hide flag again |
| After the League | Back, and the house is open. He thanks the player and reveals his name, GATSBY GOLDSWORTH | Clear the hide flag when `FLAG_SYS_GAME_CLEAR` is set; remove the door note |

The house interior is reachable only in the post-game, so it can be built last. One hide flag is needed (planned, not claimed, see [flags.md](flags.md)).

### Starters and the lab scene (author, 2026-09-29; the build is PROPOSED)

**Troglodyte's first battle is right outside the lab (author, 2026-09-30),** with one Pokémon, the usual rival opener (optional gag: a level 1 LILLIPUP pet). His Crestfall fight in Scheme 1 is then his second. Team and dialogue: [teams.md](teams.md), [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc).

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
- **BUILT 2026-09-30 (author approved): one trainer entry per fight instead of three, using the expansion's trainer party pool. The entry lists his fixed Pokémon plus the three starter versions, each starter version tagged with a spare tag, and a small custom 'prune' function reads the saved starter var and drops the two that do not match. The engine edit is two files, `include/trainer_pools.h` (one enum line) and `src/trainer_pools.c` (about 15 to 20 lines), additive, to be logged in [engine-edits.md](engine-edits.md). The function compiles and a throwaway test trainer generated the right pool data (Party Size 2 of a pool of 4, prune set), but no battle has been run. **How to write a Troglodyte entry:** `Party Size: N`, `Pool Prune: Rival Starter`, his fixed Pokémon untagged, and the three starter versions tagged `Tag6`, `Tag7`, `Tag8` (1st, 2nd, 3rd on show), with N equal to the fixed Pokémon plus one. Each fight is still its own entry with the right evolution stage for its level. Rogue Emerald does not help here: it builds all teams in C from its own table, a much bigger system.
- **Trainer ids (the no-code fallback):** three per Troglodyte battle. With 9 spare ids the likely answer is to reuse the 15 vanilla `TRAINER_BRENDAN_*` ids, since nothing in `src/` refers to them by name. See open decisions 3, 6 and 14 in [game-bible.md](game-bible.md).
- **Flags and vars (planned, not claimed):** one saved var for Troglodyte's pick (separate from `VAR_STARTER_MON`, which holds the player's), and a flag or two for the lab scene (fourth ball revealed, player has chosen). In the dialogue, `{STR_VAR_1}` is the player's species and `{STR_VAR_2}` is Troglodyte's. They are scratch text buffers, not saved, so each message is preceded by a `bufferspeciesname` for the right one.
- **`VAR_STARTER_MON` and `GetStarterPokemon`** hold three species (`sStarterMon[3]`), and `credits.c`, `field_specials.c` and `battle_setup.c` read them. Check what needs them once the species are chosen. If the player can end up with the fourth species, the table may need a fourth entry (a one-line engine edit).
- **The lab map has to support it.** It needs a table with room for four ball objects. `Elm's Lab.png` has a table (green, three tiles wide), so paint it at least four wide, with a free tile in front of each ball spot. The balls are events, and I place them. See [map-plan.md](map-plan.md).

### Scheme 1 (PROPOSED example, easy to replace)

Dialogue draft: [dialogue/crestfall.inc](dialogue/crestfall.inc).

Hired "efficiency consultants" turn up to condemn Greta's farmyard gym. Greta lets them inspect it. They get lost in the hay maze, and the inspection ends when her livestock take over the paperwork. Troglodyte arrives to watch, finds the consultants tangled in the barn, and has to battle anyway.

## The villain teams (author, 2026-10-04)

The Commons (land) and the Drowned Crown (sea), a reluctant alliance against the rich that breaks between badges 5 and 7. The Commons leader is fought by the player and Troglodyte together. The Crown is the climax after badge 9 and before the League. Full notes: [factions.md](factions.md).

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

Mostly TBD by the author. **Fixed (author, 2026-09-29):** the reveal of where the grandfather was the day Troglodyte came to Hollowbrook. He was meeting the previous region's Champion, an old friend of his. The family never knew. **Also fixed (author):** the grandfather's name stays '???' until the player beats the League, and he is grateful that the player set Troglodyte straight.

## Cutscene rule

Cutscenes fire from `coord_event` triggers, not `MAP_SCRIPT_ON_TRANSITION`. Every trigger needs a flag or var in [flags.md](flags.md).
