# GLOOMSBY (town, place 5)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); the rest is a brief. Gym: [../../gyms.md](../../gyms.md), leader SANZUFORD ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 3 and Troglodyte fight 3: [../../troglodyte-arc.md](../../troglodyte-arc.md). Roads: [../routes-west.md](../routes-west.md).

## Role in the story

- Third gym (**Ghost**, SANZUFORD, WISP BADGE, gives HM Flash and TM Shadow Ball). A **town**, so it has **no Goldsworth house** (the author's rule is one per city).
- **Scheme 3** (a film crew 'haunts' the gym) and **Troglodyte's fight 3** (his third battle, still in the 'Sneer' phase; fights 1 and 2 were the lab and Crestfall). He is level 20 to 22 here, with his starter at its **second stage**, per the schedule.
- Mood: damp, quiet, and politely morbid. A fog town with an old tower and a graveyard, where everyone talks about the dead as neighbours who happen to be late.
- The player arrives at about level 20 to 22 and leaves at about 24 to 26.

## Where it sits

| Edge | Road | Leads to |
|---|---|---|
| South-east (the **west gatehouse** on the render) | R4 | Briarwick |
| North-east (the **east gatehouse**) | R5 | Smeltham |

On the sketch Gloomsby (5) has one line down-right to Briarwick and one up-right to Smeltham. The Ecruteak render has a grey gatehouse on the west edge (middle, left) and another on the east edge (bottom right), so I give R4 the west one and R5 the east one. The map is a diagram not a compass, so swapping is harmless (Open question 1).

## Source and size

- Render: `Ecruteak City` (`ecruteakcity1xj.png`, **44 x 48 tiles**, 1 px grid). A second, larger image `ecruteak6cf.png` (61 x 50 by `px/16`, no grid) shows the same town; use the first for tracing and the second only if the author wants a bigger town. Credit Project Palladium team in `CREDITS.md`.
- Vanilla base: `LavaridgeTown` for the roof and path feel. Size check: (44 + 15) x (48 + 14) = 3,658, fine.
- Section: a new id (suggested `MAPSEC_GLOOMSBY`). **Weather:** set the map header weather to `WEATHER_FOG_HORIZONTAL` (an existing constant, no engine edit). Fly point and heal location: **yes**.

## Layout

From the render:

- **North: forest wall,** thick trees across the whole top. Two features break through it.
- **North-west: the Old Tower.** A ruined, charred-looking hall behind rocks and a low fence, with a dark door at the front. Becomes the **graveyard** (old gravestones as objects in the grass beside it) and the entrance to a one-room interior. The rocks in front (Strength boulders) hide an item.
- **North-east: the Long Hall.** A very tall wooden building standing alone in the trees at the right edge, built like a stack of floors. Door at its foot. It is the town's landmark. Proposed: the door is locked, with a sign 'CLOSED. PLEASE STOP KNOCKING'. Not a dungeon, no interior needed (author's call, Open question 3).
- **Centre-north:** a pale-brown theatre building (the Playhouse), then a row of two long houses and a small pond with three boulders beside it.
- **West block:** the blue-roofed house, a plain house, a larger house. The first of them could be SANZUFORD's family house (see NPCs).
- **South-west corner:** the **gym**, a large pale building with a gold roof and a double door facing south. The pavement in front is wide enough for the Scheme 3 crew's vans and cables (objects).
- **South-centre:** the **Pokémon Center** (red roof). **Mart** (blue roof) on the right. Two plain houses either side.
- **East gatehouse** at the bottom right (R5). **West gatehouse** at the far left (R4).
- The ground is pale and misty-looking: with fog weather on, it reads right.

Door positions in words: gym door south side, bottom-left; Center door south side, bottom-centre; Mart door south side, right; Playhouse door south side, centre-north; Old Tower door south side, top-left; houses' doors south side.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | shared |
| Mart | `LAYOUT_MART` | adds Awakening, Parlyz Heal, Ice Heal; no Revive yet |
| Gym (Ghost) | custom, base `Ecruteak City Gym.png` (15 x 23) | see Gym |
| The Playhouse | `LAYOUT_HOUSE2` | a small stage, 3 NPCs, a rehearsal for a play about someone who left |
| Old Tower | `LAYOUT_HOUSE1` or a small custom 1F | the graveyard keeper and a Spiritomb-lore NPC. No dungeon |
| House A (SANZUFORD's family) | `LAYOUT_HOUSE1` | mother, jokes about her daughter's job |
| House B | `LAYOUT_HOUSE2` | collector of ghost stories, trade NPC (see Items) |
| House C | `LAYOUT_HOUSE1` | ordinary couple, mention the film crew |
| R4 gatehouse, R5 gatehouse | route-gate layout | pass-through, 1 guard each |

## NPCs (12, roles PROPOSED, topics only)

| Role | Where | Topic |
|---|---|---|
| Sign: town | by the west gatehouse | 'GLOOMSBY. A quiet town. Please keep it that way' |
| Sign: gym | outside the gym | 'GLOOMSBY GHOST GYM. Leader: SANZUFORD. We do the dead right' |
| Film director (PROPOSED name Cormac Vane) | before Scheme 3, outside the gym | needs 'one more take' and 'real atmosphere' |
| Film assistant | outside the gym | carrying a bedsheet with eyes cut in it |
| Local mourner | square | says the gym went dark for filming and no one told her |
| Graveyard keeper | by the Old Tower | respectful of the 'new residents', after Scheme 3 laughs about the HAUNTER |
| Old man by the pond | pond | tells the player to leave the boulders alone before the right Pokémon, hints Strength |
| Kid with a lamp | west block | hunts Gastly in the fog, lets the player see the Dusk Stone spot |
| Nurse | Center | standard |
| Clerk | Mart | standard |
| SANZUFORD's mother | House A | after badge 3 says her daughter will finally tidy her room |
| Ghost-story collector | House B | story swap; gives a trade (see Items) |
| Playhouse actor | Playhouse | rehearses a line over and over, which turns out to be foreshadowing for Troglodyte's fight line |

Troglodyte: he is not an NPC here before the fight. The fight is scripted at the gym door (see Gym).

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| SPELL TAG | on the Old Tower steps, visible | none |
| POTION | visible, behind the pond | none |
| ESCAPE ROPE | hidden, by the west gate fence | none |
| TM Torment | graveyard, behind a gravestone (hidden) | none |
| DUSK STONE | behind the boulders in front of the Old Tower | Strength (badge 4), return visit |
| REVIVE | hidden, theatre side | none |
| HM Flash | from SANZUFORD | badge 3 |
| TM Shadow Ball | gym reward | badge 3 |
| Trade (PROPOSED) | House B swaps a DUSKULL for the player's ZUBAT | none, a flavour NPC |

## Gym

- **Leader: SANZUFORD** (`TRAINER_SANZUFORD`). Teenage mortician's apprentice, dry and unbothered, who thinks the dead are the better audience. Team: SHUPPET 23, LITWICK 24, MIMIKYU 25 (ace). WISP BADGE. Gives HM Flash and TM Shadow Ball.
- **Interior source:** Palladium **Ecruteak City Gym** (`Ecruteak City Gym.png`, 15 x 23 tiles). Also `gymplan.png` (58 x 64) is a gym floorplan sheet for ideas.
- **Puzzle idea:** a dark gym with pools of light; **some doors are fakes** that loop the player back to the entrance corridor. Set the map to `requires_flash` so the screen is dark without Flash: the player can still finish it, Flash is only a convenience on a revisit. The fake doors are warps that return to the start; the real door has a lit pool in front.
- **Gym trainers (2, levels 19 to 21, 3 to 4 below SANZUFORD's lowest of 23; each has 1 to 2 Pokémon):**

| Class | Team |
|---|---|
| Hex Maniac | SHUPPET 19, GASTLY 20 |
| Psychic | DROWZEE 20, DUSKULL 21 |

- **Gym guide statue** at the door: a joke about not whistling at the dead.
- **Scheme 3 beat (from [../../troglodyte-arc.md](../../troglodyte-arc.md), PROPOSED):**
  1. *Setup:* a film crew sets up a 'haunting' for a film in the gym at night. Cables, a van, a director.
  2. *Reveal:* the crew is actually frat guys in sheets, hired to scare the leader out of the building.
  3. *Collapse:* a real **HAUNTER** joins in, better. The sheets leave first. The HAUNTER takes the sheets.
  4. A **`coord_event` trigger** on the walkable tile outside the gym door starts it; the HAUNTER is a temporary object event with a battle-free cry and `applymovement`.
  5. **Troglodyte fight 3** follows at the gym door, before SANZUFORD lets the player in. He arrives in a good coat, annoyed at the fog.
- **Troglodyte fight 3 (PROPOSED, from the schedule):** party of 3, levels 20 to 22: starter at **stage 2** (Treecko line to Grovyle, Torchic to Combusken, Mudkip to Marshtomp, whichever the player did not pick; uses the existing `Pool Prune: Rival Starter`), **Sir Biscuit as HERDIER**, **MEOWTH**. Lines: 'Go on. Lose politely.' and 'Nobody at home will believe this.' Placeholder battle id; reuse a vanilla trainer id per CLAUDE.md. No IVs.

## Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_GLOOMSBY` | fly point |
| `FLAG_GLOOMSBY_SCHEME_DONE` | Scheme 3 resolved, After lines |
| `FLAG_DEFEATED_TROGLODYTE_3` (or the trainer-flag of the reused id) | fight 3 done |
| `FLAG_GLOOMSBY_RECEIVED_DUSK_STONE` etc. | one flag per item |
| Reuse `FLAG_BADGE03_GET`, `FLAG_RECEIVED_HM_FLASH` | no new ones |

## Build order and effort

**Medium.** The map itself is easy (the render is mostly gravel, houses and trees, near-matched by vanilla Lavaridge tiles). The gym darkness is a single header setting, the fake doors are warps. The Old Tower and Long Hall are exterior pieces only. Fog weather is data. Order: map, Center and Mart, gym, houses, Playhouse, Old Tower. Hard parts: the Scheme 3 cutscene (a temporary HAUNTER and the sheets) and the fight.

## Open questions

1. Which gatehouse for which road (my guess: west R4, east R5)?
2. Gloomsby is a town in the sketch, but `gyms.md` once listed it as a city with a Goldsworth house. This card follows the sketch (town, no house). Confirm.
3. Is the Long Hall an inaccessible prop, a small interior with a quest, or cut?
4. SANZUFORD's gym is dark by header setting. Is that acceptable, or does the author prefer lit rooms with a painted pool of light tiles (needs tile art)?
