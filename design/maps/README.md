# Map detailing (PROPOSED, started 2026-10-01)

Status: **PROPOSED.** One card per place and per road, written from the author's hand-drawn sketch ([../region-sketch.md](../region-sketch.md)) and the approved names ([../region-names.md](../region-names.md)). Nothing here is built. The author builds maps in Porymap (CLAUDE.md rule 2): these cards are the brief for that, and for the events, trainers and dialogue Claude wires afterwards. Existing docs for the first four places and three roads stay the source of truth: Hollowbrook ([../porymap-walkthrough.md](../porymap-walkthrough.md)), [../crestfall.md](../crestfall.md), [../wendlebury.md](../wendlebury.md), [../route1.md](../route1.md), [../route2.md](../route2.md).

## Layout of this folder

| Path | What |
|---|---|
| `towns/<name>.md` | one card per settlement (towns and cities) |
| `landmarks-<group>.md` | one section per landmark (caves, shrine, mountain, League), grouped like the roads |
| `routes-<group>.md` | the road cards, grouped: west, centre, east, south |
| `index.md` | the overview table written last |

## Route numbering (my reading of the sketch, **needs the author's confirmation**)

The sketch's black numbers appear in pairs on one corridor (7 and 8, 14 and 17, 15 and 16, 18 and 19, 21 and 30, 22 and 29, 23 and 28, 24 and 27, 25 and 26). I read each pair as **one road, drawn with an arrow each way**, so there are about 31 roads, not 33. In-game route numbers here run in walking order. Unnumbered corridors in the sketch get numbers too.

| Route | Between | Kind | Sketch number(s) |
|---|---|---|---|
| R1 | Hollowbrook, Crestfall | land | 1 |
| R2 | Crestfall, Wendlebury | land | 2 |
| R3 | Crestfall, Briarwick | land | 3 |
| R4 | Briarwick, Gloomsby | land | 4 |
| R5 | Gloomsby, Smeltham | land | 5 |
| R6 | Smeltham, Hoarfell | land | 6 and 9 |
| R7 | spur off R6 to Slagwell Mine | land | 7 and 8 |
| R8 | Briarwick, Wendlebury | land | none |
| R9 | ~~spur off Briarwick to Mothwood~~ **dropped (author, 2026-10-08)**: Mothwood branches off R8 | - | - |
| R10 | Hoarfell, Cragdale | land | 10 |
| R11 | Cragdale, Lingmoor | land | 11 |
| R12 | Lingmoor, Waymeet | land | 12 |
| R13 | Waymeet, Hemlock Reach | land | 13 |
| R14 | Hemlock Reach, Brinecombe | water | 14 and 17 |
| R15 | Primrose Vale, Brinecombe | land | 15 and 16 |
| R16 | Hemlock Reach, Mirror Isle | water | 18 and 19 |
| R17 | Mirror Isle, Primrose Vale | water | none |
| R18 | Hoarfell, Gildhaven | land | none (thin line) |
| R19 | Waymeet, Gildhaven | water | 32 |
| R20 | Gildhaven, The Pinnacle (Elite 4) | land | 33 |
| R21 | The Pinnacle, Vesperhaven (post-league) | land | 34 |
| R22 | Waymeet, Ebbsworth | water | 21 and 30 |
| R23 | Ebbsworth, Kingsquay | water, with a land path | 22 and 29 |
| R24 | Kingsquay, Driftsands | land | 23 and 28 |
| R25 | Driftsands, Beaconmouth | land | 24 and 27 |
| R26 | Beaconmouth, Aldermere (post-game) | water | 25 and 26 |
| R27 | Vesperhaven, Wendlebury (post-game) | water | none |
| R28 | Vesperhaven, Ebbsworth (post-game) | water | none |
| R29 | Vesperhaven, Silverstrand (post-game) | water | none |
| R30 | Vesperhaven, Echo Hollow (post-game) | land | none |
| R31 | Hollowbrook, Argent Peak (post-game) | land | none |

R4 to R21 already map to renamed Hoenn section entries ([../region-sketch.md](../region-sketch.md)). R22 to R31 need new section ids.

## Route renders (open, author 2026-10-01)

The author doubts that tracing Palladium **route** images will produce a quality hack. Until each road is decided, treat the render named on a road card as a mood and shape reference, not a tracing source. Town, building, gym and cave renders are still planned as before.

## Levels (author's gym curve)

Gym leader aces: gym 1 **12** (Crestfall), 2 **19** (Briarwick), 3 **25** (Gloomsby), 4 **31** (Smeltham), 5 **37** (Hoarfell), 6 **42** (Gildhaven), 7 **48** (Hemlock Reach), 8 **55** (Primrose Vale), 9 **60** (Beaconmouth). Elite 4 from 65, Champion 75. Wild Pokémon on a road run from about **ace of the gym behind it minus 3** to **ace of the gym ahead minus 3**, shifted up a little for roads that can be walked in either order. Gym trainers sit 3 or 4 below their leader's lowest Pokémon. Post-game places run 60 to 80. Trainers carry **no IVs** (explicit `IVs: 0` lines when built) and are Pokémon only.

## Rules every card follows

- **Pokémon only.** No real animals anywhere, even in names or jokes.
- Species must exist in this tree (`include/constants/species.h`, `src/data/pokemon/species_info/`). Check before listing one.
- **Trainers reuse vanilla Hoenn ids** (CLAUDE.md, author rule). The cards list class, team and level only. The id mapping is a later job.
- **Do not claim flags or vars.** Propose names and meanings in a 'Flags (not claimed)' line; they get claimed in [../flags.md](../flags.md) when built.
- **Do not generate map files.** A card describes a layout in words and a rough tile sketch at most.
- Interiors reuse vanilla layouts where possible (`LAYOUT_POKEMON_CENTER_1F`, `LAYOUT_MART`, `LAYOUT_HOUSE1`/`HOUSE2`). Max 15 live objects per map ([../engine-limits.md](../engine-limits.md)). Max map size: `(width + 15) * (height + 14) <= 10240`.
- **Map sources:** Project Palladium renders in `Team-Aquas-Asset-Repo/Maps/Project Palladium/` (images of a Johto remake; sizes in tiles are `(px - 1) / 17` when the image has a 1 px grid, otherwise `px / 16`) or a vanilla Hoenn map. Credit rule is in [../map-plan.md](../map-plan.md). Palladium has Routes 29 to 46 (minus 34 and 41), most Johto towns, gyms, Elite 4 rooms, caves and the Ruins of Alph.
- Goldsworth beats come from [../troglodyte-arc.md](../troglodyte-arc.md) (schemes 2 to 9, Troglodyte's fights) and [../goldsworth.md](../goldsworth.md). Gym and leader details: [../gyms.md](../gyms.md), [../trainer-roster.md](../trainer-roster.md), [../leader-names.md](../leader-names.md).
- HMs by badge: Cut 1, Rock Smash 2, Flash 3, Strength 4, Surf 5, Fly 6, Waterfall 8, Dive 9 ([../gyms.md](../gyms.md)). Surf at badge 5 opens the water roads.
- Dialogue tone: [../dialogue-style.md](../dialogue-style.md). Cards give **NPC roles and one-line topics**, not finished text.

## Settlement card template

```
# <NAME> (<town or city>, <place number>)
Status line: PROPOSED, links to related docs.
## Role in the story        (beat, gym, Goldsworth scheme, what the player does here)
## Where it sits            (which roads enter on which edge, matched to the sketch)
## Source and size          (Palladium render and/or vanilla base, tile size, section id, fly/heal)
## Layout                   (districts, landmarks, paths, a plain-words sketch of where each door is)
## Buildings                (table: building, layout, notes)
## NPCs                     (table: role, where, topic; 8 to 14 for a town, 12 to 20 for a city)
## Items and secrets        (hidden items, gifts, TMs, HMs, key items, with levels/badge gates)
## Gym                      (only gym places: leader, trainers, puzzle, interior source, scheme beat)
## Flags (not claimed)      (names and meanings)
## Build order and effort   (easy, medium, hard, and why)
## Open questions           (for the author)
```

## Road card template

```
## R<n>: <From> to <To> (<land or water>, sketch <numbers>)
Length and shape (tiles), terrain and mood, source render, section id.
Edges: which end enters which map edge, offsets, any side exit or ledge.
Wild table (land: 12 grass slots; water: surf and fish slots; levels per the curve), species checked.
Trainers (class, team, levels), NPCs, items (visible and hidden), signs.
Gate: HM, badge or story flag, if any. Goldsworth beat, if any.
Flags (not claimed). Build effort. Open questions.
```
