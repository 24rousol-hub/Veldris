# EBBSWORTH (town, river port; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); everything else here is a suggestion for the author. Template and rules: [../README.md](../README.md). Road cards: R22, R23, R28 in [../routes-south.md](../routes-south.md). Related: [../../gyms.md](../../gyms.md) (Waterfall at badge 8), [../../troglodyte-arc.md](../../troglodyte-arc.md) (Scheme 9 setup).

## Role in the story

- The first stop of the south coast. The player arrives by water from Waymeet (R22) after at least gym 8: **Waterfall (badge 8) is needed to climb the weir into the Ebbsworth basin**, so the south chain stays behind gym 8 (see R22).
- **No gym, no scheme beat of its own.** It plants the first hint of Scheme 9: crates and sacks stencilled 'TALLOW & CRANE, SOLICITORS: PERMITS (400)' are being lowered onto a barge bound for Beaconmouth. Nobody on the quay knows what they are. The player does not have to react.
- It is where the player gets the **Super Rod** (PROPOSED: check the item ledger, the earlier rods may already have been given elsewhere) and where the sea starts to feel like a trade route.
- **'The Surf gate south'** (author's sketch note, my reading): the quay's south side is a **lock gate** (a sluice across the channel) that a lock-keeper opens for anyone who can surf. It is the doorway from the town onto R23. See Open questions: it could instead mean a Surf badge check, which is redundant here because R22 already needs Surf.
- Post-game: R28 arrives from Vesperhaven at the **west harbour mouth**, so the harbour has two sea entrances.

## Where it sits

One of the 20 places on the sketch. The purple circle south of Waymeet (sketch roads 21 and 30).

| Road | Edge of Ebbsworth | How |
|---|---|---|
| R22 from Waymeet | **North edge** | Water. The channel enters the north quay, with the weir cascade just before it (the player surfs up it with Waterfall, so the arrival is on the town's upper basin) |
| R23 to Kingsquay | **East edge, lower half** (land path) and the **south-east lock gate** (water) | Two exits: a gatehouse on the east road for the land path, and the lock gate on the south quay for the water road |
| R28 from Vesperhaven (post-game) | **West edge** (water) | Harbour mouth, a sea gate with a ferry-style pontoon. Closed with rope until `FLAG_SYS_GAME_CLEAR` |

## Source and size

- **Vanilla base: Slateport City** (`SlateportCity_Layout`, 40 x 60). Slateport is a harbour town with a shipyard row and a boardwalk, which is exactly the river-port look. Cut it down to **about 40 x 36 tiles**: `(40 + 15) * (36 + 14) = 2750`, far under the 10240 limit. Use **Change Dimensions**, not the duplicate dialog (map-plan.md).
- **Palladium:** none matches. Use Route 32's wooden pier (`Route 32.png`, 28 x 94) as a mood reference for the jetty, and Olivine City's harbour for the bollards and moored ship (see [beaconmouth.md](beaconmouth.md), which uses the same image).
- **Section id:** `MAPSEC_EBBSWORTH` (name `EBBSWORTH`, 9 chars).
- **Fly and heal:** a fly destination (town). One row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_EBBSWORTH` in `heal_locations.json` (write `respawn_map` before `respawn_npc`). Checklist in [../../region-map.md](../../region-map.md).

## Layout

A tidal river splits the town in two with a stone bridge in the middle. In plain words, north to south:

- **North quay (top centre).** R22 arrives here. A bollard row, a signpost, a ramp up from the water. Two NPCs on the quay.
- **West bank (left).** The market and homes. Pokémon Center door faces the bridge on the west side, about 4 tiles from the bridge end. The Mart is one block south of it. A fish market (open-air stalls) sits between the two.
- **Bridge (centre).** Three tiles wide, one NPC, a sign saying 'MIND THE TIDE'.
- **East bank (right).** Boatyard and warehouses. The Boatyard's big door is at the east end of the bank; the Harbour Master's house is its neighbour. Crates stencilled with the Scheme 9 hint are stacked outside the warehouse and on a barge tied up to the quay.
- **South quay (bottom).** The **lock gate**: a stone sluice with two tall wheels. The lock-keeper's hut is on the east wheel. Beyond the gate is open water (R23). The land path starts at the east gatehouse (middle right) and runs along the shore.
- **West harbour mouth (left edge).** A sea gate, roped off until the post-game.

Surfable water is the river and the harbour. The two trees and the pier are decoration. No tall grass in town (no wild encounters inside town limits).

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared, no painting |
| Mart | `LAYOUT_MART` | Shared. Stock: Ultra Ball, Super Potion, Hyper Potion, Super Repel, Net Ball, Dive Ball, Revive |
| Boatyard 1F and 2F | `SlateportCity_SternsShipyard_1F` and `_2F` (21 x 15 and 17 x 15) | A shipwright and an apprentice. The Super Rod man lives upstairs |
| Lock House | small custom room, or `LAYOUT_HOUSE2` | The lock-keeper's hut on the south quay. The gate script lives on the outside. Interior optional |
| Harbour Master's House | `LAYOUT_HOUSE1` | Harbour Master, a ledger, the TM Rain Dance gift |
| Net Menders' Cottage | `LAYOUT_HOUSE2` | Two old net menders, a tide table, a rod display |
| Old Captain's House | `LAYOUT_HOUSE1` | The Dive and Aldermere hint (see NPCs) |
| Fish Market stalls | exterior objects | Three stalls. Berries and Pokémon Fish snacks, no real animals involved |
| Customs Shed (post-game) | exterior only | Roped-off sea gate, a Customs Officer lifts the rope after the League |

No Goldsworth house (a town gets none).

## NPCs

| Role | Where | Topic (one line) |
|---|---|---|
| Quay lookout (PROPOSED: Dunstan) | North quay | Counts boats. 'You came up the weir? Nobody comes up the weir.' Praises Waterfall |
| Lock-keeper (PROPOSED: Maud) | South quay hut | Opens the gate for anyone with the Surf badge. Sets the 'gate open' flag. Complains the gate has not been shut since the Goldsworth barges came |
| Barge hand | East quay | Loading the crates. 'Four hundred permits. The foreman counted.' Scheme 9 seed |
| Foreman | Warehouse door | Sticks to the crates. Will not say what is in them, because he does not know. Does not like being asked |
| Harbour Master | Her house | Gives **TM Rain Dance** (PROPOSED) once the player has seen the barge, because 'someone should write down where it is going' |
| Shipwright | Boatyard 1F | Boasts about the keel he is building. Mentions a sunken town to the south-east (Aldermere), 'the one the tide took' |
| Apprentice | Boatyard 1F | Cannot find the Wailmer pail. Gag |
| Rod man | Boatyard 2F | Gives the **Super Rod** after a short fishing question. Tells you which rod catches what on the south coast |
| Net menders (two) | Cottage | One mends nets, one mends the first one's work. Tide table: 'The sea is always out for something' |
| Old Captain | His house | Says that Beaconmouth's lighthouse keeper (Mizzle) once pulled him out of a wreck. Tells you that a Dive-capable trainer can enter the old city (post-game hint) |
| Market vendor | Fish market | Berry seller. Sells Oran, Pecha, Sitrus at ordinary prices |
| Kid on bridge | Bridge | Races the player to the other bank. Fast, rude, gives nothing |
| Customs Officer (post-game) | West sea gate | Unhooks the rope after the League. 'Vesperhaven? Never heard of it. Mind the rope.' |
| Nurse and clerk | Center, Mart | Standard |

12 to 14 objects across the town, each map under the 15 limit.

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| Super Rod | Boatyard 2F | Story: badge 8 plus talking to the harbour master first (PROPOSED) |
| TM Rain Dance | Harbour Master's house | Story, after the barge is seen |
| Pearl | Under the north quay bollard (hidden) | None |
| Heart Scale | East quay, behind the crates (hidden) | None |
| Max Ether | Behind the Lock House (hidden) | None |
| Net Ball x3 | Net Menders' shelf | None |
| Big Pearl | A rock in the harbour (visible, post-game, Dive spot) | Dive (badge 9), post-game |
| Sea Incense | In the Old Captain's house chest | After the League |

## Flags (not claimed)

Proposed names only. Claim in [../../flags.md](../../flags.md) when built.

- `FLAG_VISITED_EBBSWORTH` (the fly flag).
- `FLAG_EBBSWORTH_LOCK_OPEN` (gate raised once for good).
- `FLAG_EBBSWORTH_BARGE_SEEN` (Scheme 9 hint seen, unlocks the Rain Dance TM).
- `FLAG_RECEIVED_SUPER_ROD`, `FLAG_RECEIVED_TM_RAIN_DANCE`.
- `FLAG_EBBSWORTH_SEA_GATE_OPEN` (post-game, set at game clear).
- Hidden items: `FLAG_HIDDEN_ITEM_EBBSWORTH_PEARL`, `_HEART_SCALE`, `_MAX_ETHER`.

## Build order and effort

**Medium.** Slateport is bigger than needed, so cutting it down and keeping a good river-port feel is the work. The lock gate is only a script and a metatile swap. Interiors are all vanilla layouts. Build after Kingsquay's road is mapped, since the barge story points that way.

## Open questions

1. What does 'the Surf gate south' mean? My reading is a lock gate the keeper opens for surfers. If you meant a hard stop, we can make the lock refuse anyone without a badge, but R22 already needs Surf, so I put the real hard gate (Waterfall) on R22's weir instead.
2. Is Ebbsworth reached only through the Waterfall weir on R22 (my pick), or is the weir elsewhere (R23)?
3. Slateport is a city-sized base for a town. OK to trim it hard, or would you rather start from a Dewford-sized base and enlarge it?
4. Are rods earned elsewhere earlier? If the Super Rod is already given earlier, the Rod man here should give something else (a Net Ball set or the Rain Dance TM).
