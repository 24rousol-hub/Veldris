# HOARFELL (city, place 7)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Gym: [../../gyms.md](../../gyms.md), leader WAKASAGI ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 5 and Troglodyte fight 4: [../../troglodyte-arc.md](../../troglodyte-arc.md). Goldsworth houses: [../../goldsworth.md](../../goldsworth.md). Roads: [../routes-west.md](../routes-west.md). Ice cave: [../landmarks-west.md](../landmarks-west.md).

## Role in the story

- Fifth gym (**Ice**, WAKASAGI, FROST BADGE, gives **HM Surf** and TM Ice Beam). Surf opens every blue line on the sketch (Wendlebury to Vesperhaven and the water roads in the east and south).
- A **city**, so it gets a **Goldsworth house** (the author's rule is one per city, except the skyscraper city). Cousins here: PRESCOTT, BIFF and WINSTON from [../../goldsworth.md](../../goldsworth.md), none repeated from Briarwick.
- **Scheme 5** (drilled holes and flags across the frozen lake, 'angling rights') and **Troglodyte fight 4** (level 30 to 33, four Pokémon, starter at stage 2).
- It is also the **hub of the north**: three roads leave (R6 west back to Smeltham, R10 north-east to Cragdale, R18 south to Gildhaven).
- The player arrives at about level 33 and leaves at about 36 to 38.

## Where it sits

| Edge | Road | Leads to |
|---|---|---|
| West edge (a gap in the cliffs, lower left) | R6 | Smeltham (and the R7 mine spur) |
| East edge (the lane at the lower right, past the east house) | R10 | Cragdale (north-east) |
| South edge (the bottom-centre path) | R18 | Gildhaven (the thin line on the sketch, the skyscraper city) |

Sketch: Hoarfell (7) has a line west, a line east-north-east and a thin line straight down to Central City.

## Source and size

- Render: `blacthorncity.png` (Blackthorn City), **46 x 43 tiles** (px/16, no grid). Plus the Mahogany gym for the interior. Credit Project Palladium team in `CREDITS.md`.
- Vanilla base: `MossdeepCity` or `EverGrandeCity` rock walls, whichever has tiles for tall rocky cliffs; vanilla has no snow tileset, so ice and snow look need tile work (see Open questions). Size check: (46 + 15) x (43 + 14) = 3,477, fine.
- Section: new id (`MAPSEC_HOARFELL`). Fly point and heal location: **yes**. Map weather: `WEATHER_SNOW` (exists, marked unused but compiled) or none.

## Layout

From the render, Blackthorn is a town in a rock bowl:

- **North centre: the lake with the gym on it.** A big rectangular pond fills the top of the town and the **gym stands on the lake's southern shore with its feet in the water**. This becomes the **frozen lake**. The Scheme 5 crew drills holes across it. The leader's old fishing hole is by the gym's east wall. Keep the pond as one big water area; frozen look is tile art or palette.
- **Two cave doors** (small dark gaps in the cliffs): one at the very top centre above the lake, one up on the **north-east shelf**, reached by a dirt path from the town's right side. Together they are the two ends of the **Ice cave** (see [../landmarks-west.md](../landmarks-west.md)).
- **Middle:** a raised rock block in the centre, with dirt paths around it. Three boulders (Strength) sit along the paths.
- **Houses:** three grey-roofed houses (west, middle-right, south-west), plus the **Mart** (blue roof) and **Pokémon Center** (red roof) side by side in the middle, just below the central block.
- **South:** wide dirt ground, then cliffs and a gap at the bottom (R18).
- Gym sign near the gym's path.

Door positions in words: gym door south, on the lake shore at the top-middle; Center door south, middle-bottom; Mart door south, left of the Center; west house door south; east (Goldsworth) house door south; south-west house door south. Ice cave doors: north-centre and north-east shelf.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | shared |
| Mart | `LAYOUT_MART` | Great Ball, Ultra Ball (here first), Super Potion, Ice Heal, Hyper Potion, Repel, Super Repel |
| Gym (Ice) | custom, base `Mahogany Town Gym.png` (14 x 23) | see Gym |
| House A (west) | `LAYOUT_HOUSE1` | WAKASAGI's hut, thermos, spare rods |
| Goldsworth house | the shared Goldsworth layout | `Hoarfell_GoldsworthHouse`, east house on the render, NPC only |
| House B (south-west) | `LAYOUT_HOUSE2` | skier family, gift: Ice Heal |
| Ice cave 1F, B1F, ... | see landmarks | optional interior |

## NPCs (16, roles PROPOSED, topics only)

| Role | Where | Topic |
|---|---|---|
| Sign: town | by the south entrance | 'HOARFELL. Snow, Cliff and Tea. In that order' |
| Sign: gym | at the lake path | 'HOARFELL ICE GYM. Leader: WAKASAGI. Mind the ice. It minds you' |
| Sign: lake | on the shore | 'FISHING PERMITTED. FOR NOW' (Scheme 5 setup, becomes funny afterwards) |
| Drill man (hard hat) | on the lake, before Scheme 5 | drills tiny holes and plants a flag in each |
| Lake surveyor | shore | 'angling rights' paperwork (reveal) |
| Old angler | near the gym | WAKASAGI's friend, grumbles about the flags |
| Soup seller | shore, after Scheme 5 | sells soup at cost to the stranded crew |
| Skier kid | south | tells about the Ice cave's slippery floors |
| Cragdale-bound hiker | east road | hints R10 is long and windy |
| Nurse | Center | standard |
| Clerk | Mart | standard |
| Mountaineer | Center | says Surf is not allowed on the frozen lake before the Leader is beaten, 'sorry' |
| Boy with a flask | by House A | WAKASAGI's grandson, thermos hints for the gym |
| Goldsworth butler | Goldsworth house door | rules |
| Goldsworth cousins (3) | Goldsworth house | below |
| Troglodyte | by the lake, during fight 4 | see Gym |

### Goldsworth house (second one)

| Cousin | Type | Before | After (Scheme 5 beaten) |
|---|---|---|---|
| PRESCOTT | wine snob | a bottle of '1984', 'wasted on you' | has to pay for his own dinner |
| BIFF | gym rat | flexes in the mirror | even his form is better than Beau's |
| WINSTON | phone talker | tries to buy the lake | 'the lake was not for sale' |

Plus the sign `Goldsworth_Text_HouseSign`. Names from [../../goldsworth.md](../../goldsworth.md); swearing is mild and only in this house.

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| POTION | visible, by the Center | none |
| ICE HEAL x2 | visible, by the south entrance | none |
| HYPER POTION | behind a boulder, central block | Strength (badge 4) |
| NEVER-MELT ICE | on the north-east shelf, by the second cave door | none (walk up the dirt path) |
| PP UP | hidden under the soup seller's table, after Scheme 5 | none |
| PROTEIN | in the Ice cave | none |
| TM Hail | in the Ice cave (see landmarks) | none |
| HM Surf | from WAKASAGI | badge 5 |
| TM Ice Beam | gym reward | badge 5 |
| Surf-only item (a RARE CANDY on an islet in the lake) | lake | Surf (badge 5) |

Note on Surf: it is given here, so every earlier pond (R4, R5, R6, R8) becomes fully playable on a return, and the player learns it right before reaching the water roads.

## Gym

- **Leader: WAKASAGI** (`TRAINER_WAKASAGI`). An old fisherman, very relaxed, who leaves the ice-fishing hole for the battle and has a thermos. Team: SNEASEL 35, VANILLISH 36, LAPRAS 37, AVALUGG 37 (ace). FROST BADGE. Gives HM Surf and TM Ice Beam.
- **Interior source:** Palladium **Mahogany Town Gym** (`Mahogany Town Gym.png`, 14 x 23 tiles; `mahoganytowngym5jy.png`, 12 x 18, is an alternative). Both are ice-slide floors in Johto.
- **Puzzle idea:** a frozen lake floor with cracked patches. The floor is slippery. The thermos is the hint: wait by the heater tile for the ice to reset. Needs slide tile art, or use the vanilla Sootopolis-style ice tiles ([../../gyms.md](../../gyms.md), tile-art open question).
- **Gym trainers (3, levels 31 to 33, 2 Pokémon each):**

| Class | Team |
|---|---|
| Fisherman | SPHEAL 31, SEEL 32 |
| Hiker | SWINUB 31, SNORUNT 32 |
| Lass | VANILLITE 32, CUBCHOO 33 |

- **Scheme 5 beat (from [../../troglodyte-arc.md](../../troglodyte-arc.md), PROPOSED):**
  1. *Setup:* a man drills tiny holes across the lake and plants a flag in each.
  2. *Reveal:* he has 'bought the angling rights' and will close the lake to anyone without a membership.
  3. *Collapse:* the drill rig **freezes in place**, then the dock. The crew stands on a floating slab until the Leader's **GLALIE** thaws them, and sells them soup at cost. A `coord_event` trigger on the shore path starts it; the slab and rig are objects.
  4. Note: WAKASAGI's team has no GLALIE (SNORUNT is the closest; Open question 2).
- **Troglodyte fight 4 (PROPOSED, from the schedule):** party of 4, levels 30 to 33. Starter at stage 2, **Sir Biscuit as HERDIER**, **PERSIAN**, **KIRLIA**. Sneer line: 'Five towns of peasants cheering for you. It's frankly rude.' It happens on the shore, after the crew is thawed and before the player enters the gym. Reuse a vanilla trainer id; no IVs.

## Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_HOARFELL` | fly point |
| `FLAG_HOARFELL_SCHEME_DONE` | Scheme 5 resolved, After lines |
| `FLAG_DEFEATED_TROGLODYTE_4` (or the reused trainer flag) | fight 4 done |
| `FLAG_HOARFELL_ICE_CAVE_*` | item flags inside |
| Reuse `FLAG_BADGE05_GET`, `FLAG_RECEIVED_HM_SURF` | no new ones |

## Build order and effort

**Hard.** Rocky terrain is fine in the vanilla set, but the lake gym, ice slide floor, snow look and two cave doors all need tile work (the biggest custom-art risk in the west). Order: base map and cliffs, Center and Mart, houses, Goldsworth house, gym, the lake, then the Ice cave (optional, can be last).

## Open questions

1. Snow look: the vanilla Hoenn sets have none. Use the LeoB ORAS recolour, recolour tiles, or accept a bare rocky town with white palette, and let the lake be ice only?
2. WAKASAGI's team has no GLALIE (nor MAGNEZONE for HAGANE). Same answer as Smeltham's open question 2.
3. Which cave door is the main entrance, which the exit? I assumed top centre is the entrance and the north-east shelf is the far end.
4. Is the Goldsworth house on the east side (my guess) or does the author prefer another building?
