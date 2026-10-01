# HEMLOCK REACH (city, place 12, gym 7 Poison)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Everything else on this card is a suggestion for the author. Template and rules: [../README.md](../README.md). Gym and leader: [../../gyms.md](../../gyms.md), [../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md). Scheme 7 and Troglodyte's sixth fight: [../../troglodyte-arc.md](../../troglodyte-arc.md). Goldsworth houses: [../../goldsworth.md](../../goldsworth.md). Roads: [../routes-east.md](../routes-east.md). Neighbours: [primrose-vale.md](primrose-vale.md), [brinecombe.md](brinecombe.md).

## Role in the story

The cliff city of apothecaries and the seventh gym. A hillside of dispensaries, drying racks and brass pipes, where everyone reads the label first. It is the player's first city after Gildhaven's skyscraper, and the last place Troglodyte is seen before he starts training in earnest ('Work' phase of the arc).

- **Gym 7, Poison.** Leader **ASEBY**, a chemist who treats a battle as quality control. Ace level 48. Gives the VIAL BADGE and the TM for Sludge Bomb. No HM (Dive moved to badge 9, see [../../gyms.md](../../gyms.md)).
- **Scheme 7 (Goldsworth).** Inspectors in hazmat suits with clipboards and a very official stamp. Their 'regulatory review' lists 47 violations, written before they arrived. Details under Gym.
- **Troglodyte fight 6.** Outside the gym door, after the scheme collapses. Level 43 to 46, six Pokémon, 'no jokes this time, no dog' (arc table, fight 6).
- **Goldsworth house.** Yes: it is a city (CLAUDE.md and [../../map-plan.md](../../map-plan.md): one per city, except the skyscraper city).
- What the player does: learns that the water roads are the way on (Surf shore, the quay), clears the scheme, wins the badge, then chooses between the east sea (R14 to Brinecombe) and the north mere (R16 to Mirror Isle). Primrose Vale can only be reached by water from here (see Open questions).

## Where it sits

As drawn in the sketch, Hemlock Reach is the red city east of Waymeet, at the middle of the east cluster ([../../art/region_names_proposed.png](../../art/region_names_proposed.png)).

| Edge | Road | Notes |
|---|---|---|
| West | **R13** from Waymeet (land) | Enters low, in the south-west corner of the map, through a gap in the cliff line. Waymeet is south-west of the city. |
| East | **R14** to Brinecombe (water, Surf) | The quay and east shore. The player surfs out from the Lower Quay. Brinecombe is east-south-east. |
| North | **R16** to Mirror Isle (water, Surf) | A sea inlet at the north end of the map. Mirror Isle is due north (sketch 18 and 19). |
| South | none | Cliff and open sea, no connection. |

Walking order in the sketch: R13 in, then either R14 or R16 out. Primrose Vale (gym 8) is reached by R14 then R15, or R16 then R17. Both need Surf.

## Source and size

- **Base: vanilla `LavaridgeTown`** (20 x 20, `LAYOUT_LAVARIDGE_TOWN`). Lavaridge is Hoenn's cliff town with a herb shop and a gym, so it already looks like an apothecary hillside. [../../region-names.md](../../region-names.md) lists Palladium as 'none' for this city, so nothing to credit. Cliff terraces and rock walls come from the Lavaridge tileset in the tree.
- **Optional second reference:** Palladium `Cianwood City.png` (34 x 51: 579 x 868 px, 1 px grid, `(px-1)/17`) for its cliff ledges on a sea shore. It is the approved source for Brinecombe, so use it here only for the ledge shapes and only if the author agrees.
- **Size:** **44 wide x 40 tall** (after Change Dimensions on a duplicate of Lavaridge). Check: (44 + 15) x (40 + 14) = 3186, under 10240. A tall map is fine, but 40 rows of cliff costs real Porymap time (see Build effort).
- **Section id:** new section `MAPSEC_HEMLOCK_REACH` (PROPOSED name, not claimed), one of the new ids counted in [../../region-sketch.md](../../region-sketch.md) 'Map section budget'. Interiors use the town's section.
- **Fly:** yes, one row in `src/data/veldris_fly_towns.h` plus the checklist in [../../region-map.md](../../region-map.md). Heal location: in front of the Pokémon Center's door (write `respawn_map` before `respawn_npc` and give both, CLAUDE.md).
- **Water:** the quay and east shore, and a north inlet, are water tiles with Surf and fishing slots (see Wild Pokémon).

## Layout

Three terraces cut into one cliff, joined by stairs and one ramp. Brass pipes and drying racks decorate every wall.

```
 north inlet (R16)    ~~~~~~~~~~~~
                  +---------------------------+
 UPPER LEDGE      | Gym (door S)   Goldsworth |      north-east corner
 (rows 2-13)      |   [G]            House [W] |
                  +--stairs--+----ramp--------+
 MIDDLE TERRACE   | Apothecary row: A1 A2 A3   |      centre, east-facing
 (rows 14-27)     | Mart  Center  House1       |
                  +--stairs--+----------------+
 LOWER QUAY       | Quay, boathouse, House2    |  ~~~ east shore (R14)
 (rows 28-39)     R13 gap (SW)                 |
```

- **Lower Quay (south).** The R13 gap enters at the south-west corner. A short boardwalk runs east to the quay, where the player can step onto water (Surf) heading for R14. A boathouse and one small house sit here. A fishing spot at the end of the pier.
- **Middle Terrace (centre).** The market street: three apothecaries in a row facing south over the quay, the Pokémon Center and Mart at the west end, a quiet house at the east end. Hanging herb racks, bubbling copper vats in the open air. A signpost 'LABEL EVERYTHING'.
- **Upper Ledge (north).** The gym stands in the north-centre with a vat-yard in front of it (where Scheme 7 plays out). The Goldsworth house is in the north-east corner behind a hedge, with a gold knocker and a view of nothing. A path to the north inlet shore leads to R16.
- **Connections between terraces:** stairs at the west side (Lower to Middle), a ramp in the centre (Middle to Upper), and a second small stair at the east for the Goldsworth house. Ledges on the north cliff are one-way jumps down to the Middle Terrace (shortcut back, not up).
- **Door positions in words:** Pokémon Center at the west end of the Middle Terrace, facing south. Mart beside it. The three apothecaries east of them, in a row, facing south. House 1 at the east end of the Middle Terrace. Gym door in the middle of the Upper Ledge, facing south. Goldsworth house door in the north-east, facing west. Boathouse and House 2 on the Lower Quay.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared, no painting. Heal and fly point. |
| Mart | `LAYOUT_MART` | Shared. Stock leans to Antidote, Full Heal, Super Potion, Max Repel. |
| Apothecary 1, 'The Old Dispensary' (PROPOSED name) | `LAYOUT_LAVARIDGE_TOWN_HERB_SHOP` (11 x 8) | Reuses vanilla Lavaridge's herb shop layout. Sells the powders and herbs (Energy Powder, Heal Powder, Energy Root, Revival Herb as in vanilla). One shopkeeper, one customer. |
| Apothecary 2, 'Stoppered and Sons' (PROPOSED) | `LAYOUT_HOUSE2` | A shop with shelves of jars. Gives one free ANTIDOTE from the cabinet, once only (see Items). |
| Apothecary 3, 'The Reading Room' (PROPOSED) | `LAYOUT_HOUSE1` | A tiny library of labels. Hints for the gym puzzle (the colour order of the valves is on a poster here, so the player can be tipped off a second time). |
| Gym 7 | custom, see Gym | About 15 x 21 tiles. |
| Goldsworth house | shared Goldsworth layout (`LAYOUT_HOUSE1` as a stand-in, [../../map-plan.md](../../map-plan.md)) | `HemlockReach_GoldsworthHouse`. NPC only, no trainer ids. |
| House 1 (retired chemist) | `LAYOUT_HOUSE1` | Ordinary resident, gives a hint about Strength boulders. |
| House 2 (ferry widow) | `LAYOUT_HOUSE2` | Ordinary resident. |
| Boathouse | `LAYOUT_HOUSE2` | A dock hand and a rowing boat model. Surf tutor of sorts: tells the player about the R14 and R16 water. |
| Hot kettle (exterior object only) | none | A giant copper kettle with steam, decorative. |

Map names follow [../../towns-and-routes.md](../../towns-and-routes.md): `HemlockReach`, `HemlockReach_Gym`, `HemlockReach_PokemonCenter_1F`, `HemlockReach_Mart`, `HemlockReach_GoldsworthHouse`, and so on.

## NPCs

16 roles (a city card asks for 12 to 20). Names are PROPOSED where given. Topics only, not dialogue. Max 15 live objects per map: the outdoor map holds about 12 at once (Scheme 7 inspectors replace some after the beat).

| Role | Where | Topic (one line) |
|---|---|---|
| Hazmat inspector, lead | Upper Ledge (Scheme 7 setup) | Stamps things, reads 'Violation 1 of 47' aloud. |
| Hazmat inspector, junior | Upper Ledge | Cannot find the clipboard's 47th page. Holds the gym's name on a form. |
| Apothecary (old) | Apothecary 1 | Sells herbs, says every label is a promise. |
| Apothecary's customer | Apothecary 1 | Buys cough syrup for a Pokémon, reads the dose out loud. |
| Shopkeeper, Stoppered | Apothecary 2 | Hands out the one-time Antidote Cabinet item, bickers with his son about the sign. |
| Archivist | Apothecary 3 | Explains the colour order poster as a 'fire drill'. |
| Pokémon Center nurse | Center | Standard. |
| Mart clerk | Mart | Standard. Notes the Antidotes sell out when a Weezing is nearby. |
| Retired chemist | House 1 | Talks about ASEBY as a student. Hints a boulder on the North Ledge hides something. |
| Ferry widow | House 2 | Her husband's ferry now sits in the boathouse. Mentions Mirror Isle by name once. |
| Dock hand | Boathouse | Says R14 and R16 are Surf only, and tides are gentler in the morning (flavour). |
| Cliff kid | Lower Quay | Dares the player to jump the ledges. |
| Vat-yard worker | Upper Ledge | Stirs a vat and complains the inspectors are standing too close. |
| Fisherman | end of the pier | Gives a hint on the R14 sea (Tentacruel are common there). |
| Gym guide | gym entrance, inside | Says ASEBY has a clipboard for every move. |
| Troglodyte (scheme beat) | Upper Ledge | Fight 6, see Gym. |

The Goldsworth house NPCs are listed under Items and secrets / Goldsworth house below.

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| ANTIDOTE ('Cabinet', once) | Apothecary 2 shelf | none. One-time flag. |
| ETHER | behind a Cut tree at the west end of the Lower Quay | Cut (badge 1) |
| TM Rock Tomb | boulder room behind the Reading Room (Strength boulder on the North Ledge, PROPOSED) | Strength (badge 4) |
| Hidden item: POISON BARB | Upper Ledge, behind a vat | none (hidden item flag in the reserved 0x264 range) |
| Hidden item: PECHA BERRY | Middle Terrace, by the herb racks | none |
| Rock Smash rocks, two | North Ledge | Rock Smash (badge 2): hides a NUGGET and a PP UP |
| MAX ELIXIR | behind the north-shore Waterfall (a small falls on the inlet cliff) | **Waterfall (badge 8)**, a return-trip reward, PROPOSED |
| TM Sludge Bomb | from ASEBY | after the gym |
| VIAL BADGE | ASEBY | after the gym |
| Fly point | the town itself | Fly (badge 6) |

**Goldsworth house** (`HemlockReach_GoldsworthHouse`). PROPOSED cousins from [../../goldsworth.md](../../goldsworth.md): **Prescott** (wine snob) and **Kip** (pet owner, with a PERSIAN named Duchess). Before the scheme is beaten Prescott scorns the town's cough syrup and offers a vintage tonic he cannot name. Kip warns the player off Duchess. After the scheme: Prescott must pay for his own dinner, and Duchess looks embarrassed. Plus the house sign. No battle, no flag beyond the scheme stage.

## Gym

- **Leader:** **ASEBY**, Poison, ace 48. Team (built): Weezing 46, Crobat 47, Drapion 47, Garbodor 47, Toxapex 48. Id `TRAINER_ASEBY` ([../../trainer-roster.md](../../trainer-roster.md)). Pitch: a chemist who reads the ingredients on everything. VIAL BADGE, TM Sludge Bomb.
- **Interior source:** the Kanto gyms image, `KantoGyms3YearsLatercorrected.png`, the pink-floored panel with scattered trainers (bottom right of the sheet). My reading of that panel is that it is the Fuchsia gym. The sheet is 1137 x 928 px; the panel measures roughly 250 x 340 px, about **15 x 21 tiles** (my estimate from a thumbnail, check by tracing). Alternative for tile style: vanilla `LAVARIDGE_TOWN_GYM_1F` (17 x 19) is a Fire gym, not a fit.
- **Puzzle (from [../../gyms.md](../../gyms.md)):** four coloured vats stand in the corners of the floor (red, yellow, green, blue), each with a **valve**. Three gas curtains (shimmering, impassable) block the three corridors to the leader. A wall plaque and the Reading Room poster give a fixed order. The valves are bg events (signs), so they cost no objects. Turning them in the right order drops the curtains one at a time; a wrong valve vents a harmless puff, resets the stage, and the Gym guide gives a hint after two resets.
  - Order (PROPOSED): **blue, green, red, yellow** (cools, then vents, then seals, then drains). The order is on the plaque as 'Procedure 4'.
  - Objects: leader 1, trainers 4, gas curtains 3, guide 1 = 9 of 15.
- **Gym trainers (4, levels 42 to 43, 3 to 4 below ASEBY's lowest 46):**

| Trainer class | Team | Notes |
|---|---|---|
| Aroma Lady | Victreebel 42, Amoonguss 42, Roserade 43 | The first corridor |
| Expert | Muk 43, Toxicroak 43 | Guards the red valve |
| Collector | Arbok 42, Skuntank 42, Venomoth 42 | Labels her Pokémon |
| Pokémaniac | Nidoking 43, Salazzle 43 | Last before ASEBY |

  All reuse vanilla ids (CLAUDE.md), no IVs.
- **Scheme 7 beat (arc table).**
  1. **Setup:** two hazmat inspectors with clipboards and a stamp ring the gym's vat-yard on the Upper Ledge. Locals mutter on the terraces. (Foreshadowed on R13, see [../routes-east.md](../routes-east.md): a dropped pass on the road.)
  2. **Reveal:** the lead inspector pins a 'regulatory review' to the gym door: **47 violations**, one is 'Existing'. The date at the top is **before** they arrived. A local points out the stamp is not dry.
  3. **Collapse:** **ASEBY's WEEZING** lets out one polite Smog (coord_event trigger at the door, CLAUDE.md: tile walkable, elevation 3). The suits are not rated for it. Only the clipboards leave in good order.
  4. **Troglodyte** (fight 6) arrives for his own gym challenge, and the player battles him on the ledge. He is quieter ('No jokes this time. No dog.'). Party: Stoutland, Persian, Gardevoir, Rapidash, Gabite, and his starter's third stage, levels 43 to 46, uses `TRAINER_TROGLODYTE_*` id reused from vanilla (to be mapped).
  5. ASEBY invites the player in; gym, badge, TM. After, NPCs switch to their 'After' lines.

## Wild Pokémon

None inside the city. Fishing and Surf from the quay and inlet use the **R14** and **R16** tables ([../routes-east.md](../routes-east.md)).

## Flags (not claimed)

Names only, claimed in [../../flags.md](../../flags.md) when built.

- `FLAG_VISITED_HEMLOCK_REACH`: the Fly flag (one of the town visit flags).
- `VAR_HEMLOCK_SCHEME7` (0 = not started, 1 = reveal seen, 2 = collapse done, 3 = Troglodyte fought): the cutscene stage.
- `FLAG_HEMLOCK_ANTIDOTE_TAKEN`: one-time cabinet pickup.
- `VAR_HEMLOCK_GYM_VALVES` (0 to 4): valve progress. (Or a temp var if reset on exit is fine.)
- `FLAG_BADGE07_GET`: already exists, set by ASEBY.
- `FLAG_HEMLOCK_TM_ROCK_TOMB`, `FLAG_HEMLOCK_ITEM_NUGGET`, `FLAG_HEMLOCK_ITEM_MAXELIXIR`: one-shot pickups.
- Hidden items: two flags in the reserved hidden-item block (0x264 and up).

## Build order and effort

**Hard.** Tall cliff map with three terraces, ledges and stairs (the author's Porymap time); a custom gym with gas and valve scripting; the Scheme 7 cutscene with a trigger and the Troglodyte fight. Order: (1) duplicate Lavaridge, change dimensions, paint the terraces; (2) Center, Mart, herb shop and houses on shared layouts; (3) the gym last, after the gas tile art is checked ([../../gyms.md](../../gyms.md) open question 2); (4) Goldsworth house on the shared layout.

## Open questions

1. **Primrose Vale needs Surf.** Both ways to gym 8 (R14 then R15, or R16 then R17) cross water, and there is no land road from Hemlock Reach to Primrose Vale in the sketch. Fine if Surf (badge 5) is long since owned, but check the sketch.
2. **Cianwood for Hemlock?** [../../region-names.md](../../region-names.md) says no Palladium match for this city. I propose Lavaridge vanilla only. Is a Cianwood-style cliff look wanted instead (and then Brinecombe needs a different source)?
3. **Valve order** is mine, and the poster in the Reading Room spoils it. Keep the spoiler, or move the hint behind a gate?
4. **ASEBY's pitch says 'middle-aged'** but the sprite is a young man ([../../leader-names.md](../../leader-names.md) note). Dialogue should not give an age.
5. **Troglodyte fight 6** is placed outside the gym after the scheme. If he should instead be inside the Reading Room (a quieter 'Work phase' scene), say so.
6. **Cousins** Prescott and Kip are unallocated elsewhere; Briarwick's set (BARNABY etc.) is separate. Confirm the split.
