# LINGMOOR (town, place 10, heather highland, no gym)

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../../region-sketch.md](../../region-sketch.md)) and the approved names ([../../region-names.md](../../region-names.md): 'heather highland', vanilla base Verdanturf, no Palladium render). Format: [../README.md](../README.md). Roads: [../routes-centre.md](../routes-centre.md). Minor names PROPOSED.

## Role in the story

- The **quiet middle of the northern loop**, between Cragdale and Waymeet. No gym, no scheme, no fight.
- **The Day Care.** Lingmoor is where the player can leave Pokémon with a keeper, using the vanilla Day Care layout and scripts. A slow, restful place for a slow, restful job.
- A soft **Goldsworth echo**: the villagers still keep the old stone walls, and a Goldsworth surveyor's flag (a single orange stake) stands in the middle of the green, left over from a scheme that was abandoned before it began. Nobody has moved it. A deadpan nod, not a beat.
- Gives one TM and the heather tea-rooms.

## Where it sits

North-east of centre. The sketch draws a purple town on the loop, with a brown road in from Cragdale (arrow 11, from the north-west) and one out to the south (arrow 12) towards Waymeet.

| Edge | Road | Notes |
|---|---|---|
| West (upper) | **R11** from Cragdale | arrives on a heather track |
| South | **R12** to Waymeet | a farm road through a stone gate |
| North and east | none | moor and a stone wall, with a fenced hill that looks climbable and is not |

## Source and size

- **No Palladium render.** Vanilla base: `VerdanturfTown` (20 x 20). Plan **about 34 x 28** (the base is too small). Size check: `(34+15)*(28+14) = 2058`, fine.
- Tilesets: `gTileset_General` plus `gTileset_Mauville` or the Verdanturf set (long grass for heather, stone walls). Section: `MAPSEC_LINGMOOR` (already added to `region_map_sections.json`). Fly destination: yes.
- Heather colour and stone walls are tile choices, not new art, as far as the author's tilesets allow.

## Layout

A scattered village on a plateau, no main street, just lanes between low walls:

```
   R11 (west)
  >---[Standing Stones]            heath, fenced hill
        |
   [Day Care]   [Tea Rooms]  green (stake)   [Pokemon Ctr] [Mart]
        |            |         |
   houses (3)      lane------[Peat Cutter's shed]
                        |
                    stone gate -> R12 (south)
```

- **The Green** at the centre: a bench, the abandoned stake, a signpost. The Center and Mart sit on its east side.
- **The Day Care** on the west lane, with a fenced yard (objects only).
- **The Tea Rooms** one lane south. **Peat Cutter's shed** a little off the path.
- **The Standing Stones** (north-west): five stones in a ring, one hidden item, a villager who says it is a Lunatone's seat (a Pokémon joke, no real animals).
- A **Cut tree** hides a back path behind the houses; a **Rock Smash rock** is in the shed's yard.

Door positions: Center and Mart face west onto the Green. Day Care door faces south into its yard. Tea Rooms door faces north onto the lane. Houses face the lanes. Shed door faces east.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Heal location PROPOSED `HEAL_LOCATION_LINGMOOR` |
| Mart | `LAYOUT_MART` | Shared. Stock: Poké Ball, Great Ball, Super Potion, Full Heal, Repel, Pecha Berry |
| **Day Care** | vanilla `Route117_PokemonDayCare` (12 x 9) | The region's Day Care. Keeper and an old couple in the yard |
| Tea Rooms | `LAYOUT_HOUSE2` | A berry given for a chat. Tea and scones as a joke, no more |
| Peat Cutter's shed | `LAYOUT_HOUSE1` | Small, the TM is here |
| House A, B, C | `LAYOUT_HOUSE1` / `HOUSE2` | ordinary residents |

No Goldsworth house.

## NPCs

Ten roles.

| Role | Where | Topic (one line) |
|---|---|---|
| Nurse, clerk | Center, Mart | standard |
| Day Care keeper | Day Care | takes and returns Pokémon. Dry about the fee |
| Day Care visitor | yard | complains her Pokémon likes it more than her |
| Tea Rooms host | Tea Rooms | gives a berry after a conversation; hints at R12's farm |
| Peat cutter | shed | gives **TM Secret Power** (see Items) |
| Villager at the stake | the Green | 'That stake's been there since before I got here. Nobody pulls it.' |
| Stone-ring guard | Standing Stones | a lunatone's seat, do not sit |
| Walker | R11 gate | warns about R11's long ledges |
| Child | lanes | collects heather, hides from the Day Care keeper |
| Old man on the bench | the Green | talks about the road to Waymeet and the trains that do not run |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| **TM Secret Power** (`ITEM_TM_SECRET_POWER`) | peat cutter | free, after a short errand (bring him a Pecha Berry from the Mart) |
| Soothe Bell | Tea Rooms host | talk twice (a friendly gift, hold item) |
| Pecha Berry | visible at the Green | none |
| Moon Stone (hidden) | Standing Stones | none |
| Revive | back path behind the houses | Cut (badge 1) |
| Max Elixir | shed yard rock | Rock Smash (badge 2) |
| Hyper Potion (hidden) | bench on the Green | none |

## Flags (not claimed)

| Proposed name | Meaning |
|---|---|
| `FLAG_VISITED_LINGMOOR` | fly flag |
| `FLAG_RECEIVED_TM_SECRET_POWER` | peat cutter's TM given |
| `FLAG_RECEIVED_SOOTHE_BELL` | tea rooms gift |
| `FLAG_ITEM_LINGMOOR_*` | Pecha Berry, Revive, Max Elixir |
| `FLAG_HIDDEN_ITEM_LINGMOOR_*` | Moon Stone, Hyper Potion |

The Day Care uses the vanilla Day Care state (no new flag needed beyond what upstream already has).

## Build order and effort

**Easy to medium.** Small, flat, three shared interiors plus the Day Care. The only fiddly parts are the stone walls and the Standing Stones ring. Order: trace and lanes, shared Center and Mart, Day Care, Tea Rooms and shed, then houses and scripts.

## Open questions

1. **Is the Day Care wanted** (and does it belong here rather than in Wendlebury or Waymeet)? It is the only thing the town is for.
2. The **abandoned stake** nods at a Goldsworth plan that never started. Keep as a joke, or cut?
3. **TM Secret Power** (a junk-ish TM in the 50 list) as the gift: confirm or swap for something more useful.
4. The fenced hill in the east that cannot be climbed: leave as a tease, or hide something on it for the post-game?
