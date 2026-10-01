# KINGSQUAY (city, big harbour city; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); the rest is a suggestion. Template and rules: [../README.md](../README.md). Roads: R23 and R24 in [../routes-south.md](../routes-south.md). Goldsworth material: [../../goldsworth.md](../../goldsworth.md), [../../troglodyte-arc.md](../../troglodyte-arc.md) (Scheme 9). Next stops: [driftsands.md](driftsands.md), [beaconmouth.md](beaconmouth.md).

## Role in the story

- A **no-gym city**: the busiest harbour in Veldris, the place where goods, ferries and paperwork meet. It is the last big shop before the final gym.
- **Scheme 9 setup (the lawyer's office).** The Goldsworths' solicitors, **Tallow & Crane** (PROPOSED firm name), keep a branch here. The clerks are tallying every earlier scheme's invoice: Crestfall's consultants, the Briarwick fumigation tent, the Gloomsby film crew, the Smeltham crane, the Hoarfell drill rig, the Gildhaven gift basket, the Hemlock Reach clipboards, the Primrose Vale surveyors. The player sees the pile, learns the total is 'nearly finalised', and sees the senior solicitor (**Mr Tallow**, PROPOSED) leave on the Beaconmouth ferry. At Beaconmouth that lawyer hands over the box (see [beaconmouth.md](beaconmouth.md)).
- **A Goldsworth house** (city rule). Two cousins from the template set in [../../goldsworth.md](../../goldsworth.md): **Chad** (boaster, now with a yacht) and **Winston** (phone talker, tries to buy the harbour). Before the Beaconmouth scheme: they boast. After it: the yacht has a FOR SALE sign and the harbour 'was not for sale'.
- A **ferry hub**: a ferry from the Kingsquay pier to Beaconmouth (after the player has walked there once) and to Vesperhaven (post-game).
- Post-game: the Emporium restocks; one trainer (a ferry hand) gives rematch fights.

## Where it sits

South-east of Ebbsworth, west of Driftsands. A city on the sea.

| Road | Edge of Kingsquay | How |
|---|---|---|
| R23 from Ebbsworth | **North edge** (land path, a gatehouse, north-west corner) and **north-west coast** (water, a slipway) | The land path comes down a hill into the north gate. The water road lands at a slipway beside the harbour wall |
| R24 to Driftsands | **East edge**, a gatehouse | A fenced lane (Palladium Route 38), see R24 |
| Ferry | **South pier** | Warp to the ferry deck (Lilycove-style) |

## Source and size

- **Vanilla base: Lilycove City** (`LilycoveCity_Layout`, 80 x 40). It is the harbour-and-department-store city. Cut to about **64 x 40**: `(64 + 15) * (40 + 14) = 4266`, well inside 10240.
- **Palladium reference (images only, not importable):** `Olivine City.png` (44 x 41) for the dock and the moored ship, `Cianwood City.png` (34 x 51, gridded) for a cliff-side residential street. The Olivine image is also the plan for Beaconmouth; use its dock here and its lighthouse there, do not paint two lighthouses.
- **Section id:** `MAPSEC_KINGSQUAY` (name `KINGSQUAY`, 9 chars).
- **Fly and heal:** a fly destination, one row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_KINGSQUAY` (write `respawn_map` before `respawn_npc`).

## Layout

- **North gate and hill (top left).** R23's land path arrives here. The Goldsworth house is on the hill beside it, a big pale villa, so a visitor sees it first.
- **Market square (centre).** The Emporium (a department store) fronts the square. A fountain in the middle. Tallow & Crane's office is on the square's east side, a brass plate on the door.
- **Museum and Fan Club row (west, middle).** The Maritime Museum, the Trainer Fan Club and the Move Reminder's house in a short street.
- **Harbour (south).** A long quay with three piers. The **Ferry Terminal** is on the middle pier. Cranes and containers (decoration), a yacht in the east berth (Chad's, later FOR SALE), a smaller moored ship.
- **East end.** The road to R24 leaves through a gatehouse past the Pokémon Center, which stands at the east end of the square so a player leaving for Driftsands heals on the way.
- **Slipway (north-west coast).** The water arrival from R23.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared |
| Kingsquay Emporium 1F to 3F and Rooftop | `LilycoveCity_DepartmentStore_1F` to `_3F`, `_Rooftop` (18 x 8, 18 x 12) | Use three floors and the rooftop, not five: the vanilla elevator script is tied to a five-floor list, so use stairs only. 1F services, 2F balls and medicines, 3F TM counter, rooftop vending corner |
| Mart | (counters inside the Emporium) | The Emporium is the Mart. No separate `LAYOUT_MART` |
| Ferry Terminal | `LilycoveCity_Harbor` style (harbour deck) | Ticket counter, a ferry hand, the pier warp |
| Maritime Museum 1F, 2F | `LilycoveCity_LilycoveMuseum_1F` and `_2F` (21 x 14, 22 x 13) | Ship models, a drowned-city exhibit (Aldermere) |
| Pokémon Trainer Fan Club | `LilycoveCity_PokemonTrainerFanClub` (12 x 14) | Fans who ask how many badges the player has |
| Move Reminder's House | `LAYOUT_HOUSE2` | Moves relearned for Heart Scales |
| Tallow & Crane Solicitors | `RustboroCity_DevonCorp_1F` style (19 x 9) or `LAYOUT_HOUSE2` | The invoices. Clerks. One locked inner door |
| Goldsworth House | the shared Goldsworth layout ([../../map-plan.md](../../map-plan.md)) | NPC only, no trainer ids |
| Harbour Master's Hut | `LAYOUT_HOUSE1` | Ferry rules, a timetable |
| Two ordinary houses | `LAYOUT_HOUSE1`, `LAYOUT_HOUSE2` | A dockhand's family, a retired pilot |

That is about 13 maps. All use the Kingsquay section.

## NPCs

12 to 20 for a city. The ones that matter:

| Role | Where | Topic |
|---|---|---|
| Chad Goldsworth (cousin, PROPOSED per goldsworth.md) | Goldsworth house | Boasts about his yacht and a vase. After Scheme 9: 'It was a very good yacht.' |
| Winston Goldsworth (cousin) | Goldsworth house | On the phone, buying the harbour. After: 'The harbour was not for sale. I was told so by a crane.' |
| Butler | Goldsworth house | Ordinary, polite, long-suffering |
| Senior solicitor Mr Tallow (PROPOSED) | Tallow & Crane, then Beaconmouth | Courteous, never smiles. 'Our clients prefer the matter be concluded in person.' |
| Junior clerk (PROPOSED: Pip) | Tallow & Crane | Counts stamped invoices out loud. Mentions one is missing, which he later loses on Driftsands beach (see that card) |
| Second clerk | Tallow & Crane | Says the total is 'a number with a lot of commas' |
| Emporium shopkeepers (3) | Floors 1 to 3 | Ordinary, one points the TM counter out |
| Rooftop kid | Emporium rooftop | Asks for a drink from the vending corner |
| Museum guide | Museum 1F | Explains Aldermere: a town the sea took in a night. 'Two thousand years and a bad tide.' |
| Museum curator | Museum 2F | Shows a ship's wheel and asks for a donation of relics (ties to Aldermere's relics) |
| Fan Club chair and members (3) | Fan Club | 'Seven badges?' 'Eight?' Reacts to your badge count with different lines. Gives a Soothe Bell at 9 badges |
| Move Reminder | His house | Relearns moves for a Heart Scale |
| Ferry hand | Terminal | Sells tickets. Beaconmouth only after the player has been there once. Vesperhaven after the League |
| Harbour Master | Hut | Says R24 is 'the road with the sand in its shoes' |
| Dockhand with crates | Pier | Says the crates are 'permits'. Another Scheme 9 seed |
| Retired pilot | A house | Gives the hint that the lighthouse keeper drains the tower by hand, floor by floor (gym 9 hint) |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| TM Hyper Beam | Emporium 3F TM counter (price, PROPOSED) | None |
| TM Rock Tomb | Emporium 3F TM counter | None |
| Soothe Bell | Fan Club chair | 9 badges |
| Dive Ball, Net Ball | Emporium 2F | None |
| Heart Scale | Behind a crate on the east pier (hidden) | None |
| Pearl | Fountain (hidden) | None |
| Max Revive | Rooftop corner (visible) | None |
| Shell Bell | Museum 2F, a display case in the corner; the curator gives it for a Relic (post-game, Aldermere) | Post-game, Relic item in the bag |

The Emporium prices are placeholders. TM stocks must be checked against the TM ledger (design/gyms.md) for duplicates before wiring.

## Flags (not claimed)

- `FLAG_VISITED_KINGSQUAY`.
- `FLAG_KINGSQUAY_SAW_INVOICES` (the player saw the office pile).
- `FLAG_KINGSQUAY_TALLOW_LEFT` (Tallow has sailed; set when the player first arrives at Beaconmouth).
- `FLAG_KINGSQUAY_FERRY_BEACONMOUTH` (the ferry route opens after the first Beaconmouth arrival on foot).
- `FLAG_KINGSQUAY_FERRY_VESPERHAVEN` (post-game).
- `FLAG_RECEIVED_SOOTHE_BELL`.
- `VAR_KINGSQUAY_GOLDSWORTH` (before and after for the cousins). Could reuse `FLAG_BADGE09_GET`.
- Hidden items: `FLAG_HIDDEN_ITEM_KINGSQUAY_HEART_SCALE`, `_PEARL`.

## Build order and effort

**Hard.** Lilycove is a big base and needs trimming. The Emporium is three floors plus the rooftop, and the museum is two floors. The ferry is a warp plus a small script. Build the town first without the ferry. Build the cousin house when the shared Goldsworth layout exists.

## Open questions

1. Is the ferry welcome? It lets a returning player jump from Kingsquay to Beaconmouth and skip R24 and R25. I gate it on having walked there once. Alternatively no ferry until post-game.
2. Kingsquay's role as a Scheme 9 setup is my idea; the author's notes only say Beaconmouth has the lawyer. Keep, or move the pile to Beaconmouth only?
3. The Emporium with TMs for sale: do you want TMs in shops, or only as found items?
4. Do you want the Move Reminder here, or would you rather not add that system?
