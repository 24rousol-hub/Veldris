# CRAGDALE (town, place 9, ridge town, no gym)

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../../region-sketch.md](../../region-sketch.md)) and the approved names ([../../region-names.md](../../region-names.md): 'ridge town', vanilla base Fallarbor, no Palladium render). Format: [../README.md](../README.md). Roads: [../routes-centre.md](../routes-centre.md). All new minor names are PROPOSED.

## Role in the story

- A **breather between Hoarfell (gym 5) and the east**: no gym, no scheme. It is the first of the three quiet towns on the long northern loop (Cragdale, Lingmoor, Waymeet) that the player walks if they take R10 to R12 on foot instead of cutting through Gildhaven.
- A **viewpoint town.** From the ridge the player can see the tower at Gildhaven far to the south, the one thing in the region that is visibly out of scale. Everything else in town is small and weathered.
- Light Goldsworth thread: the weather station's logs show the tower's lights have been left on all night for years. A shopkeeper says a boy in loafers came through and asked whether they sold 'a nicer ridge'. No battle, no scheme (Troglodyte's fights are only at gyms 1, 3, 5, 6, 7 and the League, [../../troglodyte-arc.md](../../troglodyte-arc.md)).
- Practical: a Pokémon Center and Mart, a hostel to rest in, one TM, and optional items behind Cut, Rock Smash and Strength.

## Where it sits

North of centre, north-east of Hoarfell. The sketch draws a purple town at the top, with a brown land road in from Hoarfell (arrow 10) and one out to the south-east to Lingmoor (arrow 11).

| Edge | Road | Notes |
|---|---|---|
| West (lower half) | **R10** from Hoarfell | enters on a terrace path |
| East (lower half) | **R11** to Lingmoor | leaves through a notch in the ridge wall |
| North | none | cliff and sky |
| South | none | cliff, a one-way drop with a ledge (see Layout) |

## Source and size

- **No Palladium render** ([../../region-names.md](../../region-names.md)). Vanilla base: `FallarborTown` (20 x 20). Plan **about 34 x 28** (the base is too small for a town on terraces). Size check: `(34+15)*(28+14) = 2058`, fine.
- Tilesets: `gTileset_General` plus `gTileset_Fallarbor` (rock, ledges, ash-free grass). Section: `MAPSEC_CRAGDALE` (already added to `region_map_sections.json`). Fly destination: yes (a town).
- Mood: weathered stone, terraces, wind. No ash (that is Fallarbor's own look). Palladium could be used as mood only: Mahogany Town (24 x 25) is already assigned to Smeltham, so it is not used here.

## Layout

A long, narrow town stacked on three terraces, joined by short stairs and one Cut-tree shortcut:

```
 north cliff (impassable)
  [Weather Station]   [Climbers' Lodge]    upper terrace (viewpoint rail)
   ====== stairs ===========================
  [Hostel]   [Pokemon Ctr]  [Mart]         middle terrace (main street)
 R10 >==== stairs ============== < R11
  houses (3)   quarry office    ledge ->   lower terrace (south, drop)
```

- **Upper terrace:** the Weather Station and the Climbers' Lodge, with a viewpoint rail at the north-east end (a coin telescope object). The telescope shows Gildhaven's tower 'glinting like a sales pitch'.
- **Middle terrace (main street):** the Center and Mart side by side, the Hostel at the west end near R10.
- **Lower terrace:** three houses and a quarry office. A one-way ledge at the south-east corner drops into R11's first stretch (a shortcut one way only).
- **Cut tree** blocking a nook behind the Hostel. **Rock Smash rock** in front of a cave nook off the lower terrace. **Strength boulder** on the upper terrace that opens the Lodge's back yard.

Door positions in words: Center and Mart doors face south onto the main street. Hostel door faces east. Weather Station door faces south onto the viewpoint. Lodge door faces west. House doors face the lower terrace lane.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Heal location (PROPOSED `HEAL_LOCATION_CRAGDALE`) |
| Mart | `LAYOUT_MART` | Shared. Stock: Great Ball, Super Potion, Antidote, Repel, Super Repel, Escape Rope |
| Weather Station 1F, 2F | vanilla `Route119_WeatherInstitute_1F` (20 x 13), `_2F` (20 x 11) | Logs, a forecaster, the gift (see Items). Not a Team Aqua/Magma set: just the layout |
| Ridge Hostel | vanilla `LilycoveCity_CoveLilyMotel_1F` or `LAYOUT_HOUSE2` | Walkers' beds, tea. A cheap free rest for the player |
| Climbers' Lodge | `LAYOUT_HOUSE1` | A club of retired climbers. The TM is here |
| House A (quarryman) | `LAYOUT_HOUSE1` | ordinary resident |
| House B (grandmother) | `LAYOUT_HOUSE2` | ordinary resident |
| House C (young family) | `LAYOUT_HOUSE1` | ordinary resident |
| Quarry office | `LAYOUT_HOUSE2` | one clerk, sells nothing |

No Goldsworth house (a town gets none, [../../goldsworth.md](../../goldsworth.md)).

## NPCs

Eleven roles (8 to 14 for a town).

| Role | Where | Topic (one line) |
|---|---|---|
| Nurse, clerk | Center, Mart | standard |
| Forecaster | Weather Station 1F | forecasts wind; the ridge never has anything else |
| Station intern | Weather Station 2F | logs show the tower's lights never go off |
| Climbers' Lodge elder | Lodge | gives TM Rock Tomb after a Rock Smash errand (see Items) |
| Lodge member | Lodge back yard | complains the boulder is exactly where the view was |
| Hostel keeper | Hostel | tea, bunks, a thermos joke |
| Hiker (ambient) | upper terrace | recommends R10's ponds for a rest |
| Shopkeeper | Mart | 'A boy in loafers asked if we sold a nicer ridge' |
| Quarryman | House A | the quarry stone goes to Smeltham's foundry |
| Grandmother | House B | remembers when the road to Hoarfell was a footpath |
| Child | lower terrace | wants to see the tower through the telescope but is too short |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| **TM Rock Tomb** (`ITEM_TM_ROCK_TOMB`) | Lodge elder | Carry a message to the Hostel keeper and break the rock in front of the cave nook (Rock Smash, badge 2) |
| Max Ether | cave nook off the lower terrace | Rock Smash (badge 2) |
| Revive | nook behind the Hostel | Cut (badge 1) |
| Hyper Potion | Lodge back yard | Strength (badge 4) |
| Escape Rope (hidden) | upper terrace rail | none |
| Super Repel (hidden) | behind the Mart | none |
| Great Ball | visible, lower terrace | none |

Secret: using the telescope with the Feather Badge shows the tower's top-floor light and unlocks a one-line comment from Tobin's fans in Gildhaven later (optional, cut if not wanted).

## Flags (not claimed)

| Proposed name | Meaning |
|---|---|
| `FLAG_VISITED_CRAGDALE` | fly flag |
| `FLAG_RECEIVED_TM_ROCK_TOMB` | Lodge elder's gift |
| `FLAG_CRAGDALE_ERRAND_DONE` | message delivered to the Hostel |
| `FLAG_ITEM_CRAGDALE_*` | Max Ether, Revive, Hyper Potion, Great Ball (4) |
| `FLAG_HIDDEN_ITEM_CRAGDALE_*` | Escape Rope, Super Repel (2) |

## Build order and effort

**Medium.** Easier than a gym town, harder than Hollowbrook because the terraces and ledges need careful collision. Order: trace and terraces, shared Center and Mart, Weather Station, Lodge and Hostel, houses, then item and script wiring.

## Open questions

1. Is the **drop ledge** (a one-way shortcut into R11) wanted, or does it complicate backtracking?
2. Is the **Weather Station** a good use of Cragdale, or should the town be only a rest stop?
3. **TM Rock Tomb** as the town's gift (it is in the 50-TM list): confirm or swap.
4. The sketch gives the town two roads only. Confirm there is no spur or landmark off Cragdale.
