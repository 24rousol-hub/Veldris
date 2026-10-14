# BEACONMOUTH (city, lighthouse city, GYM 9 Water; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); leader MIZZLE and his team are **BUILT** ([../../trainer-roster.md](../../trainer-roster.md)); the rest below is a suggestion. Template and rules: [../README.md](../README.md). Roads: R25 and R26 in [../routes-south.md](../routes-south.md). Gym facts: [../../gyms.md](../../gyms.md), pitch and badge. Scheme 9: [../../troglodyte-arc.md](../../troglodyte-arc.md). Cousins: [../../goldsworth.md](../../goldsworth.md).

## Role in the story

- **Gym 9, the last gym.** The player arrives at Beaconmouth with eight badges. MIZZLE (the old lighthouse keeper, big, jolly, deadpan; sprite Scott) holds the TIDE BADGE (teal ring, wave motif), **TM Water Pulse** and the **HM Dive** (badge 9, gyms.md). His ace Milotic is level 60, leading straight into the Elite Four at 65.
- **Scheme 9, the finale of the schemes.** A lawyer hands the gym a box of 400 permits and invoices: the combined invoice of every earlier scheme, billed to the last gym. Troglodyte reads the total aloud. Nobody has a response. The box is carried out to sea. Full beat below.
- **A Goldsworth house** (city rule). Two cousins: **Prescott** (wine snob) and **Kip** (pet owner with PERSIAN 'Duchess'). Before and after as in [../../goldsworth.md](../../goldsworth.md).
- **Where each HM is used.** Dive (earned here) opens the drowned city Aldermere (post-game, R26), the underwater cove behind the harbour (this card) and several treasure spots on R26 to R29. **Waterfall (badge 8, from gym 8) is needed in two places:** the Ebbsworth weir on R22 (the hard gate for the whole south chain, see R22) and the Beaconmouth rear cove (this card, an optional reward). It is not needed to enter Beaconmouth by the land road R25.
- After the badge the player needs the League: **Fly home** to Gildhaven (Feather Badge) and R20 to the Pinnacle. Beaconmouth is itself a fly destination, so there is no long walk back.
- Post-game: R26 and the ferry to Aldermere open. Mizzle can be rematched at Vesperhaven.

## Where it sits

The far south-east of the map, the end of the south road chain.

| Road | Edge of Beaconmouth | How |
|---|---|---|
| R25 from Driftsands | **South edge, left** | A cliff road arrives at a gate beside the town sign. The stream from the cliff runs under the road here |
| R26 to Aldermere (post-game) | **West edge** (water) | The harbour mouth, a stone pier, a ferry quay. Sealed with a rope until `FLAG_SYS_GAME_CLEAR` |
| (Palladium Olivine City's top road) | not used | The Olivine render has a road leaving north; Veldris has no road there, wall it with trees |

## Source and size

- **Palladium: `Olivine City.png`** (705 x 653 px, no grid line, so about **44 x 41 tiles**). It is a harbour town with a lighthouse tower on a headland, a Pokémon Center, a Mart, a pier with a ship, and a large first-floor gym. Credit 'Project Palladium team' with the file name in `CREDITS.md` in the first commit that traces it (map-plan.md).
- **Vanilla tileset fallback: Sootopolis City** (`SootopolisCity_Layout`, 60 x 60) for the water-town feel, with Slateport's wooden jetty tiles.
- **Size:** keep about **44 x 41**, plus a strip of about 8 columns on the east side for the Waterfall cove, so **about 52 x 41**: `(52 + 15) * (41 + 14) = 3685`, fine.
- **Mapping the render:**
  - the large brown-roof building at top left (Olivine's gym) becomes the **Goldsworth house** (the grandest house in town);
  - the white eight-sided tower at bottom right on its own headland becomes the **Lighthouse (the gym)**;
  - the red-roof Pokémon Center at left stays the Center, the blue-roof Mart in the middle stays the Mart;
  - the two blue-roof houses at top right and the single house at bottom left are ordinary houses;
  - the wooden pier with the red-roofed ship at the bottom becomes the **Harbour** and the ferry quay.
- **The lighthouse art problem.** Emerald has no tall white lighthouse tileset. Options, cheapest first: (1) a white Devon Corp style block (about 6 wide, 9 tall) with a lantern roof drawn from a lamp metatile; (2) the Battle Tower or the Mossdeep Space Center exterior as a stand-in; (3) new tiles (not planned). The author decides. The interior does not depend on it.
- **Section id:** `MAPSEC_BEACONMOUTH` (name `BEACONMOUTH`, 11 chars).
- **Fly and heal:** a fly destination, one row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_BEACONMOUTH`.

## Layout

In plain words:

- **South gate (bottom left).** R25's cliff road arrives. A sign says BEACONMOUTH. The stream from the cliffs runs under the road and out to the sea on the west side.
- **Lower town (bottom centre).** The Pokémon Center door faces north on the left; the Mart is two blocks east; both open onto a sandy street that runs east to the lighthouse headland.
- **Market and houses (middle).** A small square with a well and four fish stalls. Two houses on the north side. A short alley leads to the Diver's Shed.
- **Goldsworth house (top left).** The big house, behind a fence with a nameplate. Its door is at the bottom of the building, four tiles in from the left corner.
- **Harbour (west and bottom).** The pier and the ferry quay. A deep-water patch in the harbour (Dive, post gym 9) leads to the underwater cove.
- **Lighthouse headland (right).** The gym stands alone at the end of a stone causeway three tiles wide, so the gym door can be a clean `coord_event` trigger tile in front of it for Scheme 9. The Keeper's cottage is at the foot of the causeway.
- **Rear cove (far east, behind the headland).** A small cove reached by climbing a cascade with Waterfall from the harbour side. Items on the ledge.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared |
| Mart | `LAYOUT_MART` | Stock: Max Potion, Full Heal, Revive, Ultra Ball, Dive Ball, Net Ball, Hyper Potion, Max Repel. Last Mart before the League |
| **Lighthouse Gym** 1F, 2F, 3F | custom, 3 maps (see Gym) | Base: `SootopolisCity_Gym_1F` and `_B1F` (17 x 26) for the water floor, Palladium Kanto gyms image top-centre panel for the look |
| Keeper's Cottage | `LAYOUT_HOUSE1` | Mizzle's home, his brass logbook, his LAPRAS ferry (see Open questions) |
| Goldsworth House | the shared Goldsworth layout | NPC only. See NPCs |
| Diver's Shed | `LAYOUT_HOUSE2` | Dive hint, a wetsuit rack, the Aldermere ferry clerk (post-game) |
| Lamplighters' Lodge | `LAYOUT_HOUSE1` | Local history; the tower's maintenance chief; gives the **Waterfall** hint |
| Two ordinary houses | `LAYOUT_HOUSE1`, `LAYOUT_HOUSE2` | A fishing family, an artist |

## Gym

**Leader:** MIZZLE, constant `TRAINER_MIZZLE` (built), Water. Team (built): Gyarados 58, Seismitoad 58, Araquanid 59, Barraskewda 59, Lanturn 59, Milotic 60. Rewards: TIDE BADGE (flag `FLAG_BADGE09_GET`), TM Water Pulse, HM Dive.

**Gym trainers (PROPOSED, four, 3 Pokémon each, levels 54 to 56, no IVs, all Water; classes reuse vanilla Hoenn entries):**

| Floor | Class (name PROPOSED) | Team |
|---|---|---|
| 1F | Swimmer male (Corrin) | Floatzel 54, Starmie 55, Octillery 55 |
| 1F | Swimmer female (Marlo) | Seaking 54, Jellicent 55, Mantine 55 |
| 2F | Sailor (Ivo) | Pelipper 54, Gastrodon 55, Cloyster 56 |
| 2F | Fisherman (Hobb) | Qwilfish 54, Whiscash 55, Sharpedo 56 |

The leader's lowest is 58, the gym trainers 3 to 4 below it (gyms.md). Species checked in this tree.

**Interior (the puzzle).** The gym is a flooded lighthouse. The player climbs by **draining the water floor by floor** with brass valve wheels. Idea:

- **1F, the Pump Room (about 17 x 26, from `SootopolisCity_Gym_1F`).** The floor is flooded to knee depth: water tiles are visible but impassable (Surf is not allowed in gyms). Three wheels (Brass, Red, Blue) sit on the walls (use `bg_event` tiles, not objects, to save object slots). Turning a wheel in the right order drops the water one step and the `setmetatile` swaps a strip of water for a sandbar. The right order is written in the **Keeper's logbook** lectern at the entrance: 'Brass, then Red, then Blue: the sea comes in the way it goes out' (PROPOSED wording). A wrong order floods it back with a joke line and a rewind. After the third wheel the stair is reachable. Two trainers on the sandbars watch and can be fought as they come into view.
- **2F, the Gallery (about 17 x 26, from `SootopolisCity_Gym_B1F`).** A raised walkway round a flooded pit. Two wheels, and the order is **reversed** from the log ('Mind the second pump: Blue, then Red'). Sailor and Fisherman on the walkway.
- **3F, the Lamp Room.** One big round chamber, a brass lamp in the middle, Mizzle on a platform. A final sluice lever (the wheel the player turned last) raises the platform to the lamp. No trainers.
- Vars: `VAR_BEACONMOUTH_GYM_WATER` (0 to 3 on 1F, 4 to 5 on 2F), `FLAG_BEACONMOUTH_GYM_1F_DRAINED`, `FLAG_BEACONMOUTH_GYM_2F_DRAINED`. 15 live objects per map respected: 1F has 2 trainers, 2F 2 trainers, 3F only Mizzle and the guide.
- **Gym guide statue** outside the door says 'The tide waits for no one. The pumps wait for the right one.'

**Interior source image.** `KantoGyms3YearsLatercorrected.png` (1137 x 928, no grid): the top-centre panel is a Water gym (a pool with a sandy walkway and the leader at the top). Use it as the 3F layout idea. For the actual floors start from `SootopolisCity_Gym_1F` and `_B1F` (17 x 26 each), vanilla, no credit needed. Palladium's Whirl Islands water-cave pieces (`whirlislandsarea11pw.png`, 10 x 6) are decoration reference only.

## Scheme 9: the invoice (from troglodyte-arc.md)

All Pokémon, deadpan, no battle in the scheme itself.

1. **Setup (town).** Locals say the Keeper had a letter a week ago. A Lamplighter has stacked the post: 'A box arrived by barge. Four hundred of something.' The dockhand from Kingsquay's pier (see [kingsquay.md](kingsquay.md)) said 'permits'.
2. **Reveal (the causeway, a `coord_event` trigger on the tile in front of the gym door).** **Mr Tallow** (PROPOSED), the Goldsworths' solicitor, stands on the causeway with two clerks and a hand-cart carrying **a box of 400 permits and invoices**. He addresses Mizzle, who has come out of the lighthouse. It is every gym's invoice, billed to the last gym: the total of Schemes 1 to 8. Tallow cannot read it, so he asks someone to. **Troglodyte** (he is in his 'Work' phase, [../../troglodyte-arc.md](../../troglodyte-arc.md)) is on the causeway to witness on behalf of the family, takes the sheet and **reads the total aloud**, getting quieter with each comma. (Optional: the 'minus four hundred' joke from the dropped Scheme 3 can be the final line item.)
3. **Collapse.** Nobody has a response. Mizzle's **LAPRAS** carries the box off the causeway and out to sea. Mizzle **signs for the receipt with a PSYDUCK stamp**. Tallow thanks him politely, the clerks follow the box with their eyes, and he leaves. Troglodyte walks off without a word. No battle with Troglodyte here (his fights are at gyms 1, 3, 5, 6, 7, the Victory Road and the finale).
4. **Then the gym fight.** Mizzle invites the player in. After the badge the town's NPCs switch to 'After' lines: the Lamplighters laugh, the cousins pay their own tab.

Notes: Mizzle's sprite is a big jolly man, but the beat in troglodyte-arc.md says 'she signs'. I wrote 'he'. Mizzle's team has no LAPRAS; see Open questions.

## NPCs

12 to 20 for a city.

| Role | Where | Topic |
|---|---|---|
| Mizzle (leader) | Gym 3F, causeway | Deadpan, cheerful, has seen the sea take things. 'Mizzle. Like the weather, but more of it.' |
| Gym guide statue | Outside the gym | Hint on the pump order |
| Lamplighter (chief) | Lamplighters' Lodge | Local pride. Waterfall hint: 'The back cove is for people who can climb water.' |
| Lamplighter apprentice | The causeway | Keeps polishing the same lens |
| Mr Tallow (PROPOSED) | Causeway, Scheme 9 | Courteous, never smiles, 'The matter is concluded.' |
| Two clerks | Causeway | Hold the cart, watch the box leave |
| Troglodyte | Causeway, Scheme 9 | Reads the total. Quiet |
| Prescott Goldsworth | Goldsworth house | Wine snob. 'The 1984 is wasted on this coast.' After: 'I must pay for my own dinner.' |
| Kip Goldsworth | Goldsworth house | Pet owner with PERSIAN 'Duchess'. 'Do not pet her.' After: 'Duchess looks embarrassed.' |
| Butler | Goldsworth house | Polite, long-suffering |
| Dockhand | Harbour | The ferry sells tickets to Aldermere after the League |
| Diver | Diver's Shed | Dive hint: 'The old city is a long way down, and nobody tidies it.' |
| Ferry clerk (post-game) | Diver's Shed | Opens R26 after `FLAG_SYS_GAME_CLEAR` |
| Fishing family (three) | A house | A grandmother who knows every fish by name; a boy who wants a Water-type; a father who wants his boat back |
| Artist | A house | Paints the lighthouse over and over; each time slightly crooked |
| Pokémon Center nurse, Mart clerk | Center, Mart | Standard |
| Cove ranger | Rear cove | 'You climbed it? Then it is yours.' Gives a PP Max after the climb |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| TIDE BADGE | Mizzle | Beat him |
| TM Water Pulse | Mizzle | Beat him |
| HM Dive | Mizzle | Beat him |
| Max Revive | Rear cove ledge (visible) | **Waterfall** (badge 8) |
| PP Max | Cove ranger | Waterfall |
| Mystic Water | A shelf in the Lamplighters' Lodge | After the badge |
| Sea Incense | Keeper's cottage chest | After the badge |
| Pearl x2 | Underwater cove behind the harbour | **Dive** (badge 9) |
| Big Pearl | Underwater cove | Dive |
| Max Elixir | Behind the Mart (hidden) | None |
| Heart Scale | Harbour post (hidden) | None |
| Net Ball x3 | Fish stall | None |
| Nugget | A pier barrel (hidden, post-game) | After the League |

## Flags (not claimed)

- `FLAG_VISITED_BEACONMOUTH`.
- `FLAG_BADGE09_GET` (the gym badge, already exists as a proposed constant in the badge table).
- `FLAG_BEACONMOUTH_SCHEME9_DONE` (the causeway scene has played; keys the cousins' After lines).
- `VAR_BEACONMOUTH_SCHEME9` (stage, 0 to 2) as an alternative to one flag.
- `FLAG_BEACONMOUTH_GYM_1F_DRAINED`, `FLAG_BEACONMOUTH_GYM_2F_DRAINED`, `VAR_BEACONMOUTH_GYM_WATER`.
- `FLAG_RECEIVED_TM_WATER_PULSE`, `FLAG_RECEIVED_HM_DIVE`, `FLAG_RECEIVED_PP_MAX_BEACONMOUTH`.
- `FLAG_BEACONMOUTH_FERRY_ALDERMERE_OPEN` (set at game clear).
- Trainer flags are the old Hoenn trainer id flags, as the other gyms.
- Hidden items: `FLAG_HIDDEN_ITEM_BEACONMOUTH_MAX_ELIXIR`, `_HEART_SCALE`, `_NUGGET`.

## Build order and effort

**Hard.** This is the biggest card in the south: a city, a three-floor gym with a water-draining puzzle, a Scheme 9 cutscene, a Goldsworth house, a Waterfall cove, an underwater cove and a lighthouse exterior with no existing art. Suggested order: the town map with a stand-in tower, the gym 1F pump puzzle (the hardest script), the cutscene, then the cove and the Dive cove. The gym's water puzzle uses `setmetatile` and needs the author to confirm there are suitable water/sand metatiles in the gym's secondary tileset.

## Open questions

1. **Mizzle has no LAPRAS.** The Scheme 9 beat in troglodyte-arc.md has the leader's LAPRAS carry the box to sea, but the built team has none. I propose a non-battle LAPRAS NPC (his ferry Pokémon) in the beat. OK, or change the beat, or add LAPRAS to his team?
2. The beat says 'she signs for it with a PSYDUCK stamp'. Mizzle's sprite is a man. I wrote 'he'. Is the stamp fine for him?
3. Lighthouse exterior: which art option (stand-in white block, Battle Tower, or new tiles)?
4. The Waterfall gate: I put the hard gate on R22 and a soft reward here. Is that where you wanted Waterfall to matter?
5. Does Troglodyte have to be present at the causeway, or should only the lawyer read the total? (My version has him read it: it fits the Work phase and his last appearance before the Victory Road.)
