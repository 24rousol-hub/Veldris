# PRIMROSE VALE (city, place 13, gym 8 Fairy)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Everything else is a suggestion for the author. Template and rules: [../README.md](../README.md). Gym and leader: [../../gyms.md](../../gyms.md), [../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md). Scheme 8: [../../troglodyte-arc.md](../../troglodyte-arc.md). Goldsworth houses: [../../goldsworth.md](../../goldsworth.md). Roads: [../routes-east.md](../routes-east.md). Landmark: [../landmarks-east.md](../landmarks-east.md). Neighbours: [hemlock-reach.md](hemlock-reach.md), [brinecombe.md](brinecombe.md).

## Role in the story

The garden city of florists, the eighth gym, and the last stop before the sea road to Beaconmouth. Everything here is clipped, scented and laid out in rings. It is where Goldsworth plans reach for the one thing money usually cannot flatten: a meadow.

- **Gym 8, Fairy.** Leader **SUZURAN**, a florist who is much tougher than she looks and pretends not to notice that everyone underestimates her. Ace 55. Gives the CHARM BADGE, the HM for **Waterfall** and a TM for Calm Mind ([../../gyms.md](../../gyms.md)).
- **Scheme 8 (Goldsworth).** Surveyors stake orange flags between the flower beds. It is to be 'Glade Heights', luxury condominiums with a meadow view. A garden Pokémon turns every stake into a sapling and the blueprints into a hedge. The developers buy a bouquet and leave. (Detail under Gym.)
- **Goldsworth house.** Yes: it is a city.
- **Troglodyte.** No fight (his fights fall at gyms 1, 3, 5, 6, 7 only, [../../troglodyte-arc.md](../../troglodyte-arc.md)). PROPOSED optional sighting: he is seen training alone on the west pier, no dialogue about the dog, 'Work' phase. Can be cut.
- What the player does here: clears the scheme, wins gym 8, receives Waterfall, and can now return to Mirror Isle ([../landmarks-east.md](../landmarks-east.md)) for the waterfall chamber.

## Where it sits

The red city in the far north-east of the sketch, opposite Brinecombe across R15 ([../../art/region_names_proposed.png](../../art/region_names_proposed.png)).

| Edge | Road | Notes |
|---|---|---|
| South | **R15** from Brinecombe (land) | Enters through the south gate court, centred. Sketch 15 and 16 run straight down to Brinecombe. |
| West | **R17** from Mirror Isle (water, Surf) | The lakeshore and west pier. Mirror Isle lies west-north-west across the water. |
| North, East | none | North: hedged cliff behind the gym. East: the Goldsworth gate and a tree wall. |

Primrose Vale has **no land road to the rest of the region** except R15 (which starts at a Surf-only town), so the whole north-east is a Surf pocket (see Open questions).

## Source and size

- **Source: Palladium `nationalpark5lb.png`** (the National Park, 766 x 1072 px, 1 px grid, so `(px-1)/17` = **45 x 63 tiles**). Its features map directly onto this city: a central fountain with a cross-shaped pond; two big diamonds of meadow grass; fenced paths in a ring; a south gate building and an east gate building; a red flower bed bottom right; and forest on every side. I read the image by eye: the north end holds the signpost and the fenced oval.
- **Base tileset:** vanilla `VerdanturfTown` (20 x 20, `LAYOUT_VERDANTURF_TOWN`) is the closest vanilla garden town and the starting layout to duplicate, because the Palladium image has no map file. Palladium credit rule: [../../map-plan.md](../../map-plan.md) and `CREDITS.md` in the same commit as the first trace.
- **Size:** **56 wide x 63 tall.** The picture's 45 columns, plus 11 on the west for the lakeshore and pier. Check: (56 + 15) x (63 + 14) = 5467, under 10240.
- **Section id:** new `MAPSEC_PRIMROSE_VALE` (PROPOSED, not claimed). Fly: yes, one row in `src/data/veldris_fly_towns.h` and the [../../region-map.md](../../region-map.md) checklist; heal location at the Center door.

## Layout

```
 north: hedge cliff, forest
        +--------------------------------------------------+
 GLADE  |   [Gym, door S]       lawn of flower beds        |   rows 2-17
 (N)    |   (Scheme 8 flags go in these beds)              |
        +--------------------------------------------------+
 CENTRE | west   fountain with cross pond          [Goldsworth gate]|  rows 18-47
 GARDEN | pier   four quarters, fenced paths        east: house  |
 (R17 ~)|        meadow diamonds (decorative)                   |
        +--------------------------------------------------+
 SOUTH  |  [Mart]   gate court, red bed   [Center]   [Florist] |   rows 48-62
 COURT  |             SOUTH GATE (R15)                          |
        +--------------------------------------------------+
```

- **South Gate Court.** The R15 road arrives through a gate arch at the bottom-centre. Benches and a fenced red flower bed. The **Pokémon Center** is on the west of the court, the **Mart** on the east, both facing north into the court. A small florist's shop at the far east end.
- **Central Garden.** The fountain with the cross-shaped pond is the heart. Four quarters of beds around it, a fenced path ring, and the two diamonds of grass from the picture become flower meadow (decorative tiles, not encounter grass). Two houses sit on the flanks.
- **Glade (north).** The gym stands at the top of a long lawn, door facing south. This lawn is where the surveyors' flags go in.
- **West shore.** The 11 added columns are a sandy lakeshore with a short wooden pier (the player surfs from here for R17). The one-way ledge on the north-west drops to the shore.
- **East.** The picture's east gate building becomes the Goldsworth house, standing apart behind iron railings.
- **Door positions in words:** Gym door north-centre facing south. Center west of the south court facing north. Mart east of the south court facing north. Florist at the south-east corner facing west. Houses A and B on the middle west and middle east flanks facing the fountain. Goldsworth house on the far east edge facing west. Gatehouse is the arch at the south edge (no building to enter).

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Heal and fly point. |
| Mart | `LAYOUT_MART` | Shared. Stock leans to Revive, Max Repel, Full Heal. |
| Florist 'Petal and Pot' (PROPOSED name) | `LAYOUT_ROUTE104_PRETTY_PETAL_FLOWER_SHOP` (15 x 9) | Reuses vanilla's flower shop layout. Gives the **WAILMER PAIL** (key item, watering) once. |
| Gym 8 | custom, see Gym | About 13 x 19 tiles. |
| Goldsworth house | shared Goldsworth layout (`LAYOUT_HOUSE1` stand-in, [../../map-plan.md](../../map-plan.md)) | `PrimroseVale_GoldsworthHouse`. NPC only. |
| House A (retired florist) | `LAYOUT_HOUSE1` | Ordinary resident. Hint about the gym's flower puzzle. |
| House B (petal-press family) | `LAYOUT_HOUSE2` | Ordinary residents; presses flowers into bookmarks. |
| Gate arch (exterior only) | none | The R15 gate. |
| Surveyors' hoarding (exterior object) | none | Appears on the north lawn during Scheme 8, then is replaced by a hedge. |

Map names: `PrimroseVale`, `PrimroseVale_Gym`, `PrimroseVale_PokemonCenter_1F`, `PrimroseVale_Mart`, `PrimroseVale_Florist`, `PrimroseVale_GoldsworthHouse`, and so on.

## NPCs

16 roles (12 to 20 for a city). Names PROPOSED where given. Topics only. Outdoor map holds at most 15 live objects: flags and saplings (Scheme 8) share a pool of 4 objects.

| Role | Where | Topic (one line) |
|---|---|---|
| Surveyor, chief | Glade lawn (Scheme 8 setup) | Plants orange flags, says the word 'vista' twice per sentence. |
| Surveyor, assistant | Glade lawn | Holds the tripod, has lost the site plan. |
| Developer's agent | Glade lawn | Hands the player a brochure for 'Glade Heights' with a bouquet in the artist's impression. |
| Garden warden's keeper (Florges) | by the fountain | Her FLORGES has been 'looking at the flags' since morning (hint). |
| Florist, owner | Florist | Gives the WAILMER PAIL, talks about every flower's meaning. |
| Florist's apprentice | Florist | Warns that the gym leader is 'stronger than the roses'. |
| Pokémon Center nurse | Center | Standard. |
| Mart clerk | Mart | Standard. |
| Retired florist | House A | Tells the player the petal trail in the gym follows the 'language of flowers'. |
| Petal-press mum | House B | Gives a bookmark flavour item (no effect), asks about the sea road. |
| Child with a watering can | Central Garden | Waters a flower, says it grows back faster after the surveyors stood on it. |
| Gardener (Parasol Lady, non-trainer) | Central Garden | Thinks Glade Heights is 'a lovely word for a car park'. |
| Pier angler | west pier | Mentions the lake is 'the mere' and R17 leads to Mirror Isle. |
| Gym guide | gym entrance, inside | Says SUZURAN is smaller than the trainers and warns it is a fake-out. |
| Cousin Trip / Winston | Goldsworth house | See below. |
| Troglodyte (optional sighting) | west pier | Trains alone, no jokes. No battle. |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| WAILMER PAIL | Florist | none, once |
| SOOTHE BELL | House B shelf (reward for fetching a flower) | none |
| TM Giga Drain | Central Garden, behind a Cut tree | Cut (badge 1) |
| TM Safeguard | Gym guide after the gym | after gym 8 |
| HM Waterfall | SUZURAN | after gym 8 |
| TM Calm Mind | SUZURAN | after gym 8 |
| CHARM BADGE | SUZURAN | after gym 8 |
| Hidden items | Central Garden: MAX REPEL; behind the gym: PP UP; fountain edge: REVIVE | none (hidden item flags in the reserved 0x264 block) |
| Strength boulder: RARE CANDY | north-west ledge | Strength (badge 4) |
| Rock Smash rock: NUGGET | south-west by the shore | Rock Smash (badge 2) |
| Waterfall use | **Mirror Isle** (not here) | Waterfall (badge 8, from this gym) |
| Fly point | the city | Fly (badge 6) |

**Goldsworth house** (`PrimroseVale_GoldsworthHouse`). PROPOSED cousins from [../../goldsworth.md](../../goldsworth.md): **Trip** (lounger, hammock in the conservatory, 'stand out of my light') and **Winston** (phone talker, tries to buy the garden). After the scheme: Trip says Beau 'couldn't plan a nap', and Winston discovers 'the town is not for sale', apparently as a surprise. Plus the house sign. No battle, no flags beyond the scheme stage.

## Gym

- **Leader:** **SUZURAN**, Fairy, ace 55. Team (built): Azumarill 52, Dachsbun 52, Ribombee 53, Hatterene 54, Gardevoir 55. Id `TRAINER_SUZURAN` ([../../trainer-roster.md](../../trainer-roster.md)). CHARM BADGE, TM Calm Mind, HM Waterfall.
- **Interior source:** Kanto gyms image, `KantoGyms3YearsLatercorrected.png`, the green panel with flower beds, hedges and a tiled path (second row, left). My reading is that it is the Celadon gym. The panel is roughly 205 x 307 px, about **13 x 19 tiles** (estimate from a thumbnail, trace to confirm). Greenery is decoration only: use non-encounter grass tiles.
- **Puzzle:** a glade of flower beds with a hidden door. A **petal trail** (drifting petals in five colours) hints at an order. Five **buds** (objects) are scattered around the beds: interact with them in the order the petals fall, **white, pink, yellow, blue, red**, and all five bloom and open the hedge door behind the leader. A wrong bud closes all five and the beds go quiet (reset). The Gym guide offers a hint after two resets. The 'cute fake-out' ([../../gyms.md](../../gyms.md)): **all the trainers are enormous.**
  - Objects: leader 1, trainers 4, buds 5, hedge door 1, guide 1 = 12 of 15.
- **Gym trainers (4, levels 48 to 49, 3 to 4 below SUZURAN's lowest 52):**

| Trainer class | Team | Notes |
|---|---|---|
| Hiker (enormous) | Clefable 48, Mawile 48, Wigglytuff 49 | Brandishes a garden spade |
| Black Belt (enormous) | Slurpuff 48, Alcremie 48, Aromatisse 49 | Knits |
| Parasol Lady | Whimsicott 48, Floette 49, Florges 49 | Guards the yellow bud |
| Beauty | Dedenne 48, Granbull 49, Klefki 49 | Last before SUZURAN |

  All reuse vanilla ids (CLAUDE.md), no IVs. Species checked in this tree (all exist; Floette, Florges and Alcremie are form aliases).
- **Scheme 8 beat (arc table).**
  1. **Setup:** surveyors stake orange flags between the beds on the north lawn, in daylight, with a theodolite. The player has seen one surveyor's foreshadow on R15's north end. Locals say the flags were not there on Tuesday.
  2. **Reveal:** a hoarding goes up on the lawn: **'Glade Heights, luxury condominiums with a meadow view.'** The meadow is the thing the condominiums would be built on.
  3. **Collapse:** the garden's **FLORGES** turns every stake into a sapling and the blueprints into a hedge (coord_event trigger on the lawn). The developers buy a bouquet and leave. **Note:** the arc doc calls it 'the Leader's FLORGES', but SUZURAN's built team has none. See Open questions.
  4. SUZURAN invites the player in. No Troglodyte fight. Afterwards flags and hoarding are gone, saplings stay.

## Wild Pokémon

None inside the city. The west shore uses the **R17** surf and fishing tables ([../routes-east.md](../routes-east.md)). The fountain pond is decoration (no encounters).

## Flags (not claimed)

- `FLAG_VISITED_PRIMROSE_VALE`: Fly flag.
- `VAR_PRIMROSE_SCHEME8` (0 not started, 1 flags up, 2 hoarding seen, 3 collapse done): cutscene stage.
- `VAR_PRIMROSE_GYM_BUDS` (0 to 5): bloom progress (temp var if reset on exit is fine).
- `FLAG_BADGE08_GET`: already exists.
- `FLAG_RECEIVED_WAILMER_PAIL` (an existing vanilla flag may be reused), `FLAG_PRIMROSE_SOOTHE_BELL`, `FLAG_PRIMROSE_RARE_CANDY`: one-shots.
- `FLAG_PRIMROSE_TROG_SIGHTED` (optional): sighting seen.
- Hidden items: three flags in the reserved 0x264 block.

## Build order and effort

**Hard.** A 56 x 63 map with a park layout traced from the Palladium image (the biggest decorative job in the east), a custom gym with a flower sequence, the Scheme 8 cutscene with object swaps, and a Goldsworth house. Order: (1) trace the garden from `nationalpark5lb.png` on a Verdanturf duplicate and Change Dimensions; (2) shared Center, Mart, florist and houses; (3) gym last; (4) Goldsworth house. Credit Project Palladium in `CREDITS.md` in the same commit as the first trace.

## Open questions

1. **Scheme 8 names FLORGES, SUZURAN's team has none.** Is the Florges a garden-warden NPC Pokémon (my proposal), or should her team change?
2. **Primrose Vale is Surf-only.** There is no land road from the rest of the region. Is that intended, or should R15 also connect elsewhere?
3. **Waterfall use is on Mirror Isle**, a return trip. Confirm that is where HM Waterfall pays off first ([../landmarks-east.md](../landmarks-east.md)).
4. **Palladium licence caveat** from [../../map-plan.md](../../map-plan.md) still applies to the National Park trace.
5. **Troglodyte sighting** on the pier: keep or cut?
6. **Cousins** Trip and Winston are my allocation; confirm.
