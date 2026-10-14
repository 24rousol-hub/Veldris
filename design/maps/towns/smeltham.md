# SMELTHAM (town, place 6)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Gym: [../../gyms.md](../../gyms.md), leader HAGANE ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 4: [../../troglodyte-arc.md](../../troglodyte-arc.md). Roads: [../routes-west.md](../routes-west.md). Landmark: Slagwell Mine in [../landmarks-west.md](../landmarks-west.md).

## Role in the story

- Fourth gym (**Steel**, HAGANE, RIVET BADGE, gives HM Strength and TM Iron Tail). A **town**: no Goldsworth house.
- **Scheme 4** (men in hard hats stick numbered tags on the foundry gym, to have it declared scrap). There is **no Troglodyte fight** here (his fights are at gyms 1, 3, 5, 6, 7). He may be glimpsed in a sighting line, no more.
- Mood: smoke, clanging and tea. A foundry and mining town, politely exhausted. Everyone is always on a break.
- Smeltham is the **fork of the west chain.** Beyond it the only road is R6 east to Hoarfell, with the R7 mine spur on the way. The player arrives at about level 28 and leaves at about 30 to 32.

## Where it sits

| Edge | Road | Leads to |
|---|---|---|
| South edge (bottom-centre path on the render) | R5 | Gloomsby |
| East edge (the wide lane east of the Center) | R6 | Hoarfell, with the R7 spur to Slagwell Mine on the way |

The render has more path stubs (north-west road, west lane). Close them off with cliffs or fences. Sketch: Smeltham (6) has one line down to Gloomsby and one long line east.

## Source and size

- Render: `Mahogany Town` (`Mahogany Town.png`, **24 x 25 tiles**, no grid, `px / 16`). It is small, so I recommend **widening to about 36 x 30** to fit a foundry yard and slag heaps. Size check at 36 x 30: (51) x (44) = 2,244, fine. Credit Project Palladium team in `CREDITS.md`.
- Vanilla base: `RustboroCity` (stone and industrial, the same mood). Reuse its roof tiles and its Devon Corp-style buildings for the foundry buildings.
- Section: new id (suggested `MAPSEC_SMELTHAM`). Fly point and heal location: **yes**.

## Layout

- **Top centre: the gym**, drawn as a big grey flat-roofed hall with a wide stair and gates. In the render it reads as a factory, which is the point: this **is the foundry gym**, with the gym sign on its door. Door faces south onto a short stair, with two bollards. Pine trees stand on the right of it.
- **Right of the gym, two houses** on a raised terrace (thatched roofs in the render). Keep as plain houses.
- **Centre:** a wide sand-coloured square, cut by one-tile ledges.
- **Bottom-left: the Mart.** The building with the pokéball sign in the render.
- **Bottom-right: the Pokémon Center** (red roof).
- **Bottom-left corner: one more house** with an old shop sign beside it (an ordinary resident).
- **The yard (new, added when widened):** a chain-linked foundry yard along the east side with two chimneys (object events or tile art), crates, a crane (a tall single object, used in Scheme 4), a gate and the mine office (a small building whose door leads to a one-room interior).
- **Rocks** in the render are the slag heaps. Keep them as Rock Smash targets for items.

Door positions in words: gym door south, top-centre; Mart door south, bottom-left; Center door south, bottom-right; two houses on the terrace with doors facing south; mine office door west side of the yard.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | shared |
| Mart | `LAYOUT_MART` | Great Ball, Super Potion, Repel, Antidote, Burn Heal, Parlyz Heal. Plain stock, no special shelf |
| Gym (Steel) | custom, base `Olivine City Gym.png` (11 x 20) | see Gym |
| Mine office | `LAYOUT_HOUSE2` | the Slagwell Mine staff: a clerk, a map, a hard-hat gift |
| House A (terrace) | `LAYOUT_HOUSE1` | a retired foreman |
| House B (terrace) | `LAYOUT_HOUSE2` | two workers 'on break', an eternal lunch |
| House C (bottom-left) | `LAYOUT_HOUSE1` | a hobbyist who collects scrap |

## NPCs (10, roles PROPOSED, topics only)

| Role | Where | Topic |
|---|---|---|
| Sign: town | south entrance | 'SMELTHAM. Please mind the cranes. They mind you' |
| Sign: gym | outside the gym | 'SMELTHAM FOUNDRY GYM. Leader: HAGANE. Workers are at lunch. Back at one. Probably' |
| Sticker man (hard hat) | before Scheme 4, at the gym | attaches numbered stickers to beams, treats the player as a nuisance |
| Site supervisor (suit and hard hat, PROPOSED name Mr Quill) | gym door | explains the gym 'is to be declared scrap' |
| Local worker 'on lunch' (x2) | square | HAGANE's staff, never present when he needs them |
| Mine clerk | Mine office | explains R7 is the way to the mine, the gate opens when the player has Strength or a Rock Smash TM (hint, not a hard gate) |
| Nurse | Center | standard |
| Clerk | Mart | standard |
| Retired foreman | House A | the story of the last strike that ended by tea |
| Scrap collector | House C | gives a trade or a flavour item |

The **crane operator** at the yard is an object that vanishes during Scheme 4. Total live objects outdoors during the scene: about 12 (stickers are tile or sprite props, count them).

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| POTION | visible, near the square | none |
| ANTIDOTE | hidden, behind a terrace wall | none |
| HARD STONE | behind a slag heap (rock) | Rock Smash (badge 2) |
| REPEL | hidden, the south entrance path | none |
| METAL COAT | in the foundry yard, behind a Strength boulder | Strength (badge 4) |
| HM Strength | from HAGANE | badge 4 |
| TM Iron Tail | gym reward | badge 4 |
| TM Rock Tomb | the mine clerk after the player has seen Slagwell | none |

## Gym

- **Leader: HAGANE** (`TRAINER_HAGANE`). A middle-aged foundry foreman, exhausted and very patient. His workers are always at lunch. Team: BRONZOR 29, PAWNIARD 30, TINKATUFF 31 (ace). RIVET BADGE. Gives HM Strength and TM Iron Tail.
- **Interior source:** Palladium **Olivine City Gym** (`Olivine City Gym.png`, 11 x 20 tiles). The Olivine image is narrow, so it suits a foundry corridor.
- **Puzzle idea:** conveyor belts and crusher presses carry the player around the floor on a timing puzzle. Needs belt art ([../../gyms.md](../../gyms.md), open question about tiles). If no belt tiles exist, use the vanilla forced-walk arrow tiles (as in the Mossdeep-style puzzles) to move the player along a lane, and press tiles that are only walkable when a switch flips (the existing 'toggle' tiles). Workers 'at lunch' leave open lanes.
- **Gym trainers (3, levels 25 to 27, 2 Pokémon each):**

| Class | Team |
|---|---|
| Hiker | BRONZOR 25, ARON 26 |
| Black Belt | MACHOP 26, TIMBURR 26 |
| Guitarist | MAGNEMITE 26, KLINK 27 |

- **Scheme 4 beat (from [../../troglodyte-arc.md](../../troglodyte-arc.md), PROPOSED):**
  1. *Setup:* men in hard hats tag every beam of the foundry with numbered stickers.
  2. *Reveal:* the gym is to be declared 'scrap' and hauled off by crane so the family can buy the lot cheap.
  3. *Collapse:* the Leader's **MAGNEZONE** takes hold of the crane and every truck. They fold into one neat cube outside the door, **with a receipt.**
  4. A `coord_event` trigger on the walkable tile in front of the gym door starts it. The cube is one big object (a boulder-style sprite) that stays as scenery.
- **Note for the author:** HAGANE's built team (see the trainer roster) has no MAGNEZONE. Treat it as his **work Pokémon**, an object that appears only in the cutscene (an overworld Pokémon, no battle). The other option is to rework the Scheme to use BRONZOR or TINKATUFF, or to add a MAGNEZONE to his team (Open question 2).
- No Troglodyte fight here.

## Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_SMELTHAM` | fly point |
| `FLAG_SMELTHAM_SCHEME_DONE` | Scheme 4 resolved, After lines, cube stays |
| `FLAG_SMELTHAM_RECEIVED_*` | one per item and the mine hint |
| Reuse `FLAG_BADGE04_GET`, `FLAG_RECEIVED_HM_STRENGTH` | no new ones |

## Build order and effort

**Medium to hard.** The map is easy once widened (small render, plain tiles). The hard part is the gym (belts and presses need art or tile behaviours) and the crane scene (a tall object plus a cube). Order: map, Center and Mart, houses, mine office, gym, then the cutscene.

## Open questions

1. The Mahogany render is small (24 x 25). Is widening to about 36 x 30 acceptable?
2. HAGANE's team has no MAGNEZONE. Work Pokémon, change the Scheme, or add one to the team?
3. Which belt solution: new tile art, or forced-walk arrows plus toggle tiles?
4. Should the player be able to enter Slagwell Mine from the Mine office (a second door) as well as from R7, or only from R7?
