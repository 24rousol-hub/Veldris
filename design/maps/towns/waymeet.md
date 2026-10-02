# WAYMEET (town, place 11, crossroads and rail stop, no gym)

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../../region-sketch.md](../../region-sketch.md)) and the approved names ([../../region-names.md](../../region-names.md): 'crossroads and rail stop', Palladium Goldenrod train station, vanilla base Mauville). Format: [../README.md](../README.md). Roads: [../routes-centre.md](../routes-centre.md). Minor names PROPOSED.

## Role in the story

- **The hub where land and water roads meet.** Four roads leave Waymeet: land north (R12) and east (R13), water west (R19) and south (R22). It is the one place in the north half of the map where the player chooses which way to go.
- No gym, no scheme, no fight. It is where the player realises the map is a loop: R12 arrives from Lingmoor, R19 leads to Gildhaven's tower, R13 to Hemlock Reach's gym 7 and R22 down to the south coast.
- **A rail stop with no trains.** The station is a handsome building with a parked train (a graphic only). The line is 'between timetables': the stationmaster is permanently apologetic. A private railcar with a gold G sits on a siding (a quiet Goldsworth nod).
- Walk order: Hoarfell (gym 5) to R10, R11, R12 into Waymeet, then R19 to Gildhaven (gym 6), then back by Fly to Waymeet and R13 to Hemlock Reach (gym 7). Surf comes from badge 5, so R19 and R22 are open from the start.

## Where it sits

Centre-right, a little south-east of Gildhaven and south-west of Hemlock Reach. The sketch shows a purple town with four roads: a brown road in from the north (arrow 12) and out to the east (arrow 13), and blue water roads to Gildhaven on the west (arrow 32) and to Ebbsworth on the south (arrows 21 and 30).

| Edge | Road | Notes |
|---|---|---|
| North | **R12** from Lingmoor | arrives through a farm gate |
| East | **R13** to Hemlock Reach | a plain road, the railway beside it |
| West | **R19** water road to Gildhaven | a ferry-style pier. Needs Surf |
| South | **R22** water road to Ebbsworth | a second pier. Needs Surf |

## Source and size

- **Palladium:** the Goldenrod train station renders: `trainstation2zi.png` (476 x 197 px, **29 x 12**, two halves: the waiting hall with and without a train) and `stacjajs7.png` (412 x 350 px, **25 x 21**, waiting room with a platform and a long white train). Both are 16 px tiles and no grid. Use them for the station interior only.
- **Vanilla base:** `MauvilleCity` (40 x 20, hub of roads in Hoenn). It is too small. Plan **about 44 x 34** with a canal along the west and south sides so the water roads can leave from piers. Size check: `(44+15)*(34+14) = 2832`, fine.
- Tilesets: `gTileset_General` plus `gTileset_Mauville` (and the `LilycoveCity` secondary if the piers need harbour tiles). Section `MAPSEC_WAYMEET` (new, PROPOSED, one of the 37 free ids). Fly destination: yes.
- Credit Project Palladium for the station if traced ([../../map-plan.md](../../map-plan.md)).

## Layout

```
                 R12 (north gate)
                     |
   [Cafe]   [Pokemon Ctr] [Mart]       [Station]=====rails=====> R13 (east)
      \         |                         |  siding: gold railcar
  R19 <pier  Junction Square (cross)-------+
  (west)        |
   [Dock Office] [Lost Property]  houses
                 |
              pier  R22 (south)
```

- **Junction Square** at the centre: a compass-rose paving stone, a signpost with four arrows (the 'Four Ways' sign, a joke on the name), benches, a clock.
- **The Station** on the north-east side, with its platform and the parked train (a long object or tile art, not a working train). The railway line runs east out of town beside R13 and fades off the map edge.
- **The canal** wraps the west and south edges. Two piers: west for R19, south for R22.
- **Cafe, Dock Office and Lost Property** line the square. Houses fill the south-east corner.
- A fenced siding behind the Station holds the gold railcar (an object, not enterable).

Door positions: Center and Mart face south onto the square, side by side. Station door faces west onto the square. Cafe faces east onto the west lane. Dock Office faces south onto the south pier. Lost Property faces west. Houses face the lane.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Heal location PROPOSED `HEAL_LOCATION_WAYMEET` |
| Mart | `LAYOUT_MART` | Shared. Stock: Great Ball, Ultra Ball, Super Potion, Hyper Potion, Full Heal, Revive, Repel, Super Repel |
| **Station** | custom, Palladium `stacjajs7.png` (25 x 21) or `trainstation2zi.png` (29 x 12) | Ticket desk, waiting hall, platform with a parked train. Stationmaster, a few waiting NPCs. Not a working train in this build |
| Cafe ('The Junction') | `LAYOUT_HOUSE2` | Chat, a drink gift |
| Dock Office | `LAYOUT_HOUSE1` | Harbourmaster for the two piers |
| Lost Property Office | `LAYOUT_HOUSE2` | Gives TM Thief (a joke: 'nobody has claimed it') |
| House A, B | `LAYOUT_HOUSE1` / `HOUSE2` | ordinary residents |

No Goldsworth house.

## NPCs

Twelve roles (8 to 14 for a town).

| Role | Where | Topic (one line) |
|---|---|---|
| Nurse, clerk | Center, Mart | standard |
| Stationmaster | Station | permanently apologetic, the line is between timetables |
| Ticket clerk | Station | tickets for nowhere; sells you a platform ticket as a joke item (no real item) |
| Waiting passenger | Station | has waited since the old timetable |
| Railwayman | siding | polishes the gold railcar, 'private, not mine' |
| Harbourmaster | Dock Office | explains the piers: west for Gildhaven, south for Ebbsworth. Surf required |
| Cafe host | Cafe | cheap tea, comments on every direction a traveller takes |
| Lost Property clerk | Lost Property | the unclaimed TM |
| Signpost reader | Junction Square | reads the sign aloud: 'north is Lingmoor, east is Hemlock Reach' |
| Fisherman | west pier | bored, comments on R19's long water |
| Hiker | north gate | has just come down from Cragdale and is dramatic about it |
| Child | square | tries to count the arrows on the sign and gets five |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| **TM Thief** (`ITEM_TM_THIEF`) | Lost Property clerk | free, after a short chat ('unclaimed') |
| Super Potion | visible, behind the Cafe | none |
| Escape Rope (hidden) | station platform bench | none |
| Rare Candy (hidden) | under the gold railcar's siding | none (peek, not enter) |
| Max Repel | pier, west | Surf (badge 5), on a tile off the pier |
| Pearl | south pier islet | Surf (badge 5) |
| Heart Scale | canal rock | Rock Smash (badge 2) |
| Revive | by the north gate | Cut (badge 1) |

Secret: the signpost says 'FOUR WAYS' but the arrows only list three destinations (the fourth, the Station, is not a destination). Reading it twice is a one-line joke.

## Flags (not claimed)

| Proposed name | Meaning |
|---|---|
| `FLAG_VISITED_WAYMEET` | fly flag |
| `FLAG_RECEIVED_TM_THIEF` | lost property gift given |
| `FLAG_ITEM_WAYMEET_*` | Super Potion, Max Repel, Pearl, Heart Scale, Revive (5) |
| `FLAG_HIDDEN_ITEM_WAYMEET_*` | Escape Rope, Rare Candy (2) |

## Build order and effort

**Medium.** One shared Center and Mart and five small interiors, but the canal, the two piers and the station building need careful Surf entry tiles. Order: trace with the canal, piers, the station exterior, shared interiors, then the four connections (two land, two water).

## Open questions

1. **Does the player ever use the train?** The card makes the station dressing only (no engine work). A working rail link would be a new system and needs the author's say first.
2. **Pier entry points:** is Surf enough, or does the author want a ferry? R19 and R22 as drawn need Surf (badge 5).
3. **Which of R19 and R22 should be tried first** by a new player? The card does not gate either; the sketch's arrows suggest R19 first (to Gildhaven).
4. The sketch writes **12 twice**: once on the Lingmoor to Waymeet road, once beside 13 on the Waymeet to Hemlock Reach road. I read the second as the return arrow of that road (the pair 12/13), as the other paired corridors do, so it is not a separate route. The README's other guess was that it is a mistaken 20. Confirm.
