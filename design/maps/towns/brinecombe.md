# BRINECOMBE (town, place 14, no gym)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Everything else is a suggestion for the author. Template and rules: [../README.md](../README.md). Roads: [../routes-east.md](../routes-east.md). Neighbours: [hemlock-reach.md](hemlock-reach.md), [primrose-vale.md](primrose-vale.md).

## Role in the story

A salt-working fishing town on the far east coast, the quiet link between the two east cities. It has no gym and no scheme of its own. It is where the player first sees the sea road pay off, collects the **Super Rod** (PROPOSED), and walks north to Primrose Vale on R15.

- **Beat:** a rest stop between gyms 7 and 8, with a Pokémon Center and a harbour. The Scheme 7 hazmat crew can be seen here afterwards (see Items and secrets) buying salt, as a one-line aftermath gag.
- **Goldsworth angle:** no house (it is a town). A rich cousin's yacht sits aground on the salt pans, a purely ambient joke (PROPOSED).
- **Troglodyte:** not here. A fisherman may mention that a boy in a very clean jacket rowed past 'with a lot of luggage' (optional sighting line, no battle).

## Where it sits

The purple town in the far east, south-east of Primrose Vale and east of Hemlock Reach ([../../art/region_names_proposed.png](../../art/region_names_proposed.png)).

| Edge | Road | Notes |
|---|---|---|
| West | **R14** from Hemlock Reach (water, Surf) | The harbour. Hemlock Reach is west-north-west across the sea (sketch 14 and 17). |
| North | **R15** to Primrose Vale (land) | A gap in the cliff line at the north end of the town. Sketch 15 and 16 run straight north. |
| East, South | none | Cliffs and open sea. |

## Source and size

- **Source: Palladium `Cianwood City.png`**, the approved pairing in [../../region-names.md](../../region-names.md) (579 x 868 px, 1 px grid, so `(px-1)/17` = **34 x 51 tiles**). It is a sand-coloured coastal town with six buildings, a cliff wall on one side and sea on the other. **Trace it mirrored left to right** so the sea is on the west (the picture has it on the east), then open a gap in the north cliff for R15.
- **Vanilla alternative:** `PacifidlogTown` (20 x 40, `LAYOUT_PACIFIDLOG_TOWN`) as the duplicate base, since the Palladium picture has no map file.
- **Size:** **34 wide x 51 tall.** Check: (34 + 15) x (51 + 14) = 3185, under 10240.
- **Section id:** new `MAPSEC_BRINECOMBE` (PROPOSED, not claimed). Fly: yes (towns are fly destinations, [../../crestfall.md](../../crestfall.md) note), one row in `src/data/veldris_fly_towns.h` and the [../../region-map.md](../../region-map.md) checklist. Heal location in front of the Center.
- Credit: Project Palladium in `CREDITS.md` in the same commit as the first trace ([../../map-plan.md](../../map-plan.md)).

## Layout

```
 north: cliff line, gap (R15)
   +---------------------------------+
   |        path from R15            |
   | House A      Harbour Office     |   north third
   |                                 |
 ~ |   SALT PANS (shallow, raked)    |   middle third
 ~ |      Salt Works (big roof)      |
 ~ |  Center        House B  Chandlery|   south third
 ~ |  quay, boats                    |
   +-- cliff south ------------------+
 ~ = sea, west edge (R14)
```

- **North third.** The R15 path enters through the cliff gap and runs south past a house and the Harbour Office. A signpost.
- **Middle third.** A flat of **salt pans**: shallow rectangular pools with white heaps, raked by workers (decorative tiles: sand with water inlays, no encounters). The big-roofed **Salt Works** takes the place of the picture's large building (the one the gym would be).
- **South third.** The Pokémon Center near the quay, the Chandlery (Mart) and a second house. The quay and a few moored boats are on the west edge. A cliff and rocky ledge closes the south.
- **Door positions in words:** Salt Works door south-facing in the middle. Pokémon Center door south-facing near the quay, south-west. Chandlery south-facing, south-east. Harbour Office north-west facing the quay. House A north-east facing west. House B south-centre facing east.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Heal and fly point. |
| Chandlery (Mart) | `LAYOUT_MART` | Shared. Stock leans to Great Ball, Super Potion, Repel, Net Ball. |
| Salt Works | `LAYOUT_HOUSE2` stand-in, or a custom 11 x 8 | A workshop with drying racks. The foreman and two workers. Free item here (see Items). |
| Harbour Office | `LAYOUT_HOUSE1` | Harbour master. Gives the **Super Rod** (PROPOSED). |
| House A (retired boatman) | `LAYOUT_HOUSE1` | Ordinary resident. Tells the legend of Mirror Isle in one line. |
| House B (net-mender) | `LAYOUT_HOUSE2` | Ordinary resident. |
| Boats and cranes (exterior only) | none | Decor. |
| Grounded yacht (exterior object) | none | A cousin's yacht stuck on the salt pans, ambient. |

Map names: `Brinecombe`, `Brinecombe_PokemonCenter_1F`, `Brinecombe_Chandlery`, `Brinecombe_SaltWorks`, `Brinecombe_HarbourOffice`, and so on. No Goldsworth house (it is a town).

## NPCs

12 roles (8 to 14 for a town). Names PROPOSED where given. Topics only.

| Role | Where | Topic (one line) |
|---|---|---|
| Harbour master | Harbour Office | Gives the Super Rod, says sea roads close in rough weather (flavour). |
| Salt foreman | Salt Works | Complains about flat-pack condominiums on the next coast. Gives an item for fetching a lost sieve. |
| Salt raker | Salt pans | Rakes in rows, never in circles. Hints at a hidden Big Pearl off the pier. |
| Salt raker's apprentice | Salt pans | Mixes up salt with sugar. Harmless. |
| Pokémon Center nurse | Center | Standard. |
| Mart clerk | Chandlery | Standard. |
| Retired boatman | House A | Tells the Mirror Isle legend: 'the shrine has no door, only a doorstep'. |
| Net-mender | House B | Says her mother taught her knots at 'about the same time as walking'. |
| Fisherman | Quay | Tells the player Tentacruel gather off the Hemlock side. Optionally mentions a rowing boy. |
| Child with a bucket | Salt pans | Collects shells, swaps one for nothing. |
| Cousin on the yacht | Quay (ambient, optional) | Shouts at a tide table. Before the player has beaten gym 7 only (flag). |
| Hazmat inspector, returned | Salt pans (after Scheme 7 only) | Buys salt, clipboard under one arm, avoids eye contact. |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| **SUPER ROD** | Harbour master | none. PROPOSED, see Open questions |
| SEA INCENSE | Salt foreman (fetch the lost sieve from the pier) | none |
| ETHER | behind a Cut tree at the south ledge | Cut (badge 1) |
| TM Reflect | a hidden nook behind House B | Rock Smash (badge 2) rock |
| Hidden items | pier end: BIG PEARL (Dive spot); salt heap: PEARL; beach: SUPER POTION | the BIG PEARL needs **Dive (badge 9)**, a return-trip item, PROPOSED |
| Rare reward | Strength boulder on the south ledge: PP UP | Strength (badge 4) |
| Fly point | the town | Fly (badge 6) |

## Wild Pokémon

None in the town. The harbour and pier use the **R14** surf and fishing tables ([../routes-east.md](../routes-east.md)); the salt pans have no encounters.

## Flags (not claimed)

- `FLAG_VISITED_BRINECOMBE`: Fly flag.
- `FLAG_RECEIVED_SUPER_ROD`: one-shot (may reuse an existing vanilla flag if the author wants the rod there).
- `FLAG_BRINECOMBE_SIEVE_RETURNED`, `FLAG_BRINECOMBE_SEA_INCENSE`: the foreman's fetch quest.
- `FLAG_BRINECOMBE_INSPECTOR_BACK`: reads `VAR_HEMLOCK_SCHEME7 >= 2` from [hemlock-reach.md](hemlock-reach.md) rather than its own flag (no new flag needed).
- Hidden items: three flags in the reserved 0x264 block. One uses the Dive gate.

## Build order and effort

**Medium.** One map traced from a Palladium picture (flipped), mostly shared interiors, one custom small interior (Salt Works, may use `LAYOUT_HOUSE2`), no gym and no cutscenes. A good early build in the east: it can be built and tested with only R14 and R15.

## Open questions

1. **Is the Super Rod here?** I do not know where the Old and Good Rods come from in this plan. If Surf at badge 5 is meant to coincide with the Good Rod, the Super Rod suits Brinecombe. Tell me where the rods go.
2. **Cianwood mirrored.** Approved pairing, but I flip it to put the sea on the west. If the author prefers the picture unflipped, move R14 to the east edge and mirror the sketch reading.
3. **A Dive item at the pier** is a return-trip reward (badge 9) and is only needed if the author wants post-badge-9 hidden items in the east.
4. **The grounded yacht** and the returned inspector are PROPOSED gags. Cut freely.
