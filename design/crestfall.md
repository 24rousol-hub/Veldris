# Crestfall (town 2, gym 1) - town plan

Status: **PROPOSED** except the name and Greta (approved earlier) and that Crestfall is a **town** (author, 2026-10-01, replacing the earlier 'city'; the sketch also draws it purple). The exterior map is **BUILT** (layout B 'village green', approved 2026-10-01, see 'As built' below). Everything else below is a suggestion. Map plan: [map-plan.md](map-plan.md) (reference `Azalea Town.png`, about 48 x 32, vanilla base `PetalburgCity`). Dialogue: [dialogue/crestfall.inc](dialogue/crestfall.inc) and [dialogue/crestfall_extra.inc](dialogue/crestfall_extra.inc).

## Role
Normal type farm town and the first gym, one road from Hollowbrook. It is a town, so it has **no Goldsworth house** (changed 2026-10-01): the NPC-only cousin set below moves to **Briarwick** (approved 2026-10-01). The Center and Mart here are the player's first. The skyscraper is **not** here unless the author says so. Greta is the leader (`TRAINER_CRESTFALL_GRETA`, STANDARD BADGE). Scheme 1 plays out here.

## Where it sits
West: Route 1 from Hollowbrook. East: Route 2 to Wendlebury, **the next stop in the story** (author, 2026-10-01). North: Route 3 to Briarwick, **blocked by the Commons** until the Wendlebury beat (author, 2026-10-04; details in [factions.md](factions.md)). Layout as built below.

## Buildings
| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F` and `_2F` | Shared, no painting. Nurse, visitor (in `crestfall.inc`) |
| Mart | `LAYOUT_MART` | Shared. Clerk (in `crestfall.inc`) plus shopkeeper (extra) |
| Gym | custom, base `Azalea Town Gym.png` (see map-plan) | Greta, two trainers, hay maze, guide statue |
| ~~Goldsworth house~~ | removed 2026-10-01 | A town gets none. Its draft lines (`GoldCousin*` and the rest in `crestfall_extra.inc`) are reused for the first city |
| House A (retired couple) | `LAYOUT_HOUSE1` | Ordinary residents |
| House B (stuck trainer) | `LAYOUT_HOUSE2` | Ordinary resident |
| Market square | exterior objects only | Three stalls, a fountain, signs |
| Farm and tomato patch | exterior objects only | Farmhands, old farmer, grandma |

Map names follow [towns-and-routes.md](towns-and-routes.md): `Crestfall`, `Crestfall_Gym`, `Crestfall_PokemonCenter_1F`, `Crestfall_GoldsworthHouse`, and so on.

## NPCs (all PROPOSED)
| NPC | Where | Label prefix `Crestfall_Text_` | File |
|---|---|---|---|
| Consultants (outside, boss, junior) | Town, gym door | `Consultant*` | crestfall |
| Local worried, farmhand, kid, grandma, visitor, clerk, nurse | Town, Center, Mart | `Local*`, `Farmhand*`, `Kid*`, `Grandma*` | crestfall |
| Greta and two gym trainers | Gym | `Greta*`, `Trainer1*`, `Trainer2*` | crestfall |
| Market berry, tomato, milk stalls | Square | `Market*` | extra |
| Two farmhands (fence, barn) | Farm road | `FarmhandFence*`, `FarmhandBarn*` | extra |
| Gym guide statue, signs | Gym, town | `GymStatue*`, `FarmSign`, `SquareSign` | extra |
| Retired couple | House A | `HouseA*` | extra |
| Stuck trainer | House B | `HouseB*` | extra |
| Second kid, old farmer | Square, farm | `KidSquare*`, `OldFarmer*` | extra |
| Shopkeeper | Mart | `Shopkeeper*` | extra |
| Goldsworth cousins (boaster, lounger, pet owner), butler | Goldsworth house | `GoldCousin*`, `GoldLounger*`, `GoldPetOwner`, `GoldButler` | extra |

Goldsworth house: the boaster cousin (BARNABY, name PROPOSED) brags about the family, per author. Residents swear mildly (PG-13) and are rude to the player, not cruel to townsfolk. No battle, no flag needed beyond the before/after-gym check.

## As built (2026-10-01): layout B 'village green'

Map `Crestfall` (`MAP_CRESTFALL`), layout `LAYOUT_CRESTFALL`, **40 x 32**, LeoB ORAS tiles: `gTileset_General` + `gTileset_Petalburg` (same primary as Route 1, so the connection draws correctly). `MUS_PETALBURG`, `MAPSEC_CRESTFALL`, `MAP_TYPE_TOWN`, sunny. Border copied from Route102. Built by `design/tools/leob/crestfall_build.py` (author asked for the map to be built; edit in Porymap from now on). Every piece is a vanilla Petalburg or Oldale metatile.

A sand square with a pond on a grass-and-flower island in the middle, the path looping round it. The gym stands at the head of the square. House A, the Center, the Mart and House B sit along the main road with their doors on the road (the Mart one tile left, so a grass gap separates it from House B). South of the square: two benches looking over a crop field, with a fence along the top of the field so the player cannot walk down there. No hedges.

| What | Tile |
|---|---|
| Route 1 (west edge) | rows 15-16; connection `left` to `MAP_VELDRIS_ROUTE1` offset +5 (Route 1 has `right` offset -5) |
| Route 2 (east edge) | rows 15-16; no connection until Route 2 exists |
| Route 3 (north edge) | x 27-28; no connection, so it is a dead end for now |
| Gym door | (20, 9) |
| House A / Center / Mart / House B doors | (3, 14) / (9, 14) / (31, 14) / (36, 14) |
| Signs: town / gym / Route 3 / Route 2 / field | (1, 17) / (22, 10) / (26, 2) / (38, 17) / (19, 22) |
| Benches / fence | (15-17, 22) and (22-24, 22) / (14-23, 25) |

**Interiors (built 2026-10-08, author asked for the maps):**

| Map | Layout | Who is inside | Door |
|---|---|---|---|
| `Crestfall_PokemonCenter_1F` | `LAYOUT_VELDRIS_POKEMON_CENTER_1F` (vanilla Center with the escalator painted out, see below) | Nurse (`LOCALID_CRESTFALL_NURSE`), a hiker visitor ('I stayed for the tomatoes'). **No 2F** (author, 2026-10-08) | Crestfall warp 1, (9,14) |
| `Crestfall_Mart` | vanilla `LAYOUT_MART` | Clerk ('Hay is not for sale'), stock POKé BALL, POTION, ANTIDOTE, PARALYZE HEAL, AWAKENING; shopkeeper with a before/after-badge line | warp 2, (31,14) |
| `Crestfall_HouseA` | H1 cottage | The retired husband (old man) and his SKITTY by the stove. **The wife is not placed yet:** her lines are about the Scheme 1 consultants, which are not approved | warp 0, (3,14) |
| `Crestfall_HouseB` | H5 bedroom house | The stuck young trainer (before/after badge) | warp 3, (36,14) |

**Fly point:** `FLAG_VISITED_CRESTFALL` (set on entering the town), `HEAL_LOCATION_CRESTFALL` lands on (9,15) outside the Center, whiteout returns to the nurse. **Checked in mGBA:** entering and leaving every door, the nurse heal, the Mart menu. **Not checked:** Fly itself, the town-map picture (still Hoenn art). **The gym is not built** (Greta's story beat and Scheme 1 need the author first).

Sign scripts are in `data/maps/Crestfall/scripts.inc` (town and field text from the drafts, gym sign 'Leader: GRETA', Route 2 'EAST: WENDLEBURY', Route 3 'NORTH: BRIARWICK'). **Not yet built:** door warps (the interiors do not exist yet), NPCs, Scheme 1, the fly point and heal location (they need the Center), and the Route 3 block. **Checked in mGBA:** the town renders, the gym sign reads correctly, and walking west crosses into Route 1 cleanly. The town roads are sand and Route 1's path is pale grass path: the grass path runs in to x 1 and blends into the sand at x 2-3 (custom blend tiles, author asked 2026-10-01).

**Path blend tiles** (Petalburg secondary, made by `design/tools/leob/path_blend.py`, seen in game). East-west road, grass path west and sand east, two tiles wide (A then B): top edge 656/657, middle 658/659, bottom edge 660/661. Mirrored (sand west): 662/663, 664/665, 666/667. North-south road, grass path north and sand south, two tiles tall (upper, lower): west edge 668/669, middle 670/671, east edge 672/673. Flipped (sand north): 674/675, 676/677, 678/679. In Porymap they sit at the end of the Petalburg metatiles.

## Gym and Scheme 1 decisions (author, 2026-10-08)

- **Gym puzzle: C, the fence pens.** Livestock-style fenced pens with gates; beating each gym trainer (DALE, then WREN) swings a gate open, and the path zigzags to Greta. Silver outside, blue inside, greenery decorative only (author, earlier).
- **Greta has no farm link:** she just happens to be posted here.
- **Opening beat of Scheme 1:** when the player tries to go in, **Troglodyte's attendant pushes the player out of the way: 'the golden boy goes first.'** Troglodyte is used to this and thinks nothing of it; it is how he was raised. **Scheme 1 is 'the private booking' (author, 2026-10-08):** the parents booked the whole gym for a private session, with a photographer ready for 'the future Champion's first badge' photoshoot. Greta refuses to go easy and beats Troglodyte in two turns; the photo of his loss ends up on the town noticeboard (the humiliation beat). He storms out and battles the player to 'prove it was a fluke' (his fight 2). PROPOSED beats in the formula: **setup** a 'CLOSED: PRIVATE SESSION' sign and the photographer setting up; **reveal** the attendant's shove at the door; **collapse** Greta's two-turn win; **Troglodyte battles** the player outside; **humiliation** the noticeboard photo (it can stay up for the rest of the game). **Superseded:** the consultant draft below, the hay maze, the Route 1 surveyors' foreshadowing and House A wife's 'men in suits' lines all belong to the old scheme and need rewriting.

## The gym, as built (2026-10-08)

`Crestfall_Gym` (`LAYOUT_CRESTFALL_GYM`, 15 x 23), vanilla Petalburg Gym tiles (the vanilla Normal-type gym), door (20,9) in Crestfall (warp 4). Author's choices: the 'green-B' layout, a railed aisle up the middle whose **two centre gates open once Greta is beaten** (a shortcut for return visits), and a pen each side with a gym trainer by its gap. **One trainer required:** the player picks a side and beats that trainer; the other is optional. Beating Greta marks both as beaten, so an unbeaten one just chats afterwards.

| What | Where |
|---|---|
| Greta (`TRAINER_CRESTFALL_GRETA`, overworld LASS) | (7,4) on the blue mat |
| WREN (`TRAINER_CRESTFALL_GYM_2`), left pen, sight 3, faces right | (1,12) |
| DALE (`TRAINER_CRESTFALL_GYM_1`), right pen, sight 3, faces left | (13,14) |
| Pen gaps | (4,13) left, (10,15) right |
| Centre gates (shut, opened by `setmetatile` on load once `FLAG_BADGE01_GET` is set) | (6-8,11) and (6-8,16) |
| Statues (signs) / exit mat | (3,21), (11,21) / (7-8,22) |

Rewards: STANDARD BADGE (`FLAG_BADGE01_GET`), **HM CUT** (`FLAG_RECEIVED_HM_CUT`, the vanilla flag reused) and **TM CRUNCH** (new **TM51**, flag `FLAG_RECEIVED_TM_CRUNCH` = the unused vanilla Rock Tomb flag). The aisle walls are new north-south railing tiles (metatiles 736-740 in the Petalburg Gym tileset, drawn the way vanilla draws Route 117's fence), built by `design/tools/gym/gym_rails.py`; the map by `design/tools/gym/crestfall_gym.py`. Greta's lines are the earlier drafts (PROPOSED); DALE's and WREN's were reworded because the hay maze is gone. **Checked in mGBA:** entering, the new railings, the shut centre gates. **Not yet checked:** the battles, the badge and gifts, the gates opening. **Not built:** Scheme 1 (the dialogue draft is waiting for the author's review).

## Where Scheme 1 beats happen
1. **Setup** (before the gym): consultant outside in town; locals and the old farmer grumble; the two surveyors on Route 1 hint first.
2. **Reveal**: consultant boss and junior at the gym door, with the junior lost in the hay maze.
3. **Collapse**: Greta's MILTANK eat the paperwork, at the gym door (coord_event trigger, per CLAUDE.md).
4. **Troglodyte arrives and battles** (his second fight), then Greta invites the player in.
5. **Gym battle**, badge and CUT. Afterward the town NPCs switch to their 'After' text.

## Flags (not claimed)
One flag or var for the Scheme 1 stage is needed, and one for the gym-beaten state (`FLAG_BADGE01_GET` already exists for the After text). Claim them in [flags.md](flags.md) when the map is built.

## Open questions
- Flying: Crestfall is a town, so this is settled: it is a fly destination.
- The skyscraper is in Central City (sketch), not here.
- Greta's farm link (see [characters.md](characters.md)).
