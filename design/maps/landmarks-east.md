# Landmarks, the east

Status: **PROPOSED.** One section per landmark in the east group. Right now that is **MIRROR ISLE** only (the sketch's far north-east green circle). Name approved 2026-10-01 ([../region-names.md](../region-names.md)). Template: the settlement card in [README.md](README.md), trimmed for a landmark. Roads: [routes-east.md](routes-east.md). Cities: [towns/hemlock-reach.md](towns/hemlock-reach.md), [towns/primrose-vale.md](towns/primrose-vale.md).

---

## MIRROR ISLE (landmark, lake island shrine, optional)

### Role in the story

A small island in the north-east mere, reached **only by water**. A shrine of still pools that reflect the sky, and, past a waterfall, a hidden chamber. It is optional: nothing in the main story needs it. It is the east's reward for exploring, and the first place that **pays off Waterfall** (badge 8, given by SUZURAN in Primrose Vale). A rare, optional encounter is proposed here and is **a PROPOSAL only**, not canon.

- **When:** reachable as soon as the player has Surf (badge 5) and has reached Hemlock Reach. The outer isle and shrine hall can be explored then; the waterfall chamber and the rare encounter wait for Waterfall.
- **No trainers** on the island itself, apart from two Swimmers on the approach roads (see [routes-east.md](routes-east.md)). It is a quiet place. One hermit NPC, one fisherman.
- **Goldsworths:** none. A shrine is the one place nobody tried to buy.

### Where it sits

The green landmark at the top of the far north-east, joined by blue lines to Hemlock Reach (sketch 18 and 19, in-game R16) and to Primrose Vale (unnumbered blue line, in-game R17) ([../art/region_names_proposed.png](../art/region_names_proposed.png)).

| Edge | Road | Notes |
|---|---|---|
| South | **R16** from Hemlock Reach (water, Surf) | The isle's main landing, a small wooden jetty. |
| East | **R17** to Primrose Vale (water, Surf) | A second landing on the east shore, a rocky ledge. |
| North, West | none | Open water. |

No land road at all (the sketch has no brown line). Surf is mandatory.

### Source and size

Palladium `Whirl Islands.png` (a contact sheet of nine Whirl Islands rooms, 1424 x 1035 px) and the individual files below are **cave interiors only**. There is no outdoor island map in Palladium, so the outdoor island is a hand-built island, laid out by the author in Porymap, with vanilla Hoenn sea tiles. Sizes in tiles: `(px - 1) / 17` for the 1 px grid files.

| Map (PROPOSED name) | Source | Tiles | Notes |
|---|---|---|---|
| `MirrorIsle` (outdoor) | none in Palladium. Vanilla sea tiles (the island ring of `Route 129` or `Route 130` style) | about **30 x 26** | Check: (30 + 15) x (26 + 14) = 1800. Hand-built, shrine steps, jetty, standing stones. |
| `MirrorIsle_Shrine` (the hall) | `whirlislandsexit16uy.png` (171 x 154 px) | **10 x 9** | The small hall with the mirror pools. |
| `MirrorIsle_Hollow` (the cave under the isle) | `whirlislandsmain7yr.png` (715 x 630 px) | **42 x 37** | Big two-level cave, ladders and ledges. Check: (42 + 15) x (37 + 14) = 2907. |
| `MirrorIsle_Falls` (the waterfall chamber) | `whirlislandsmain25fz.png` (341 x 664 px) | **20 x 39** | Tall room with a water channel and a waterfall (the right-hand panel on `Whirl Islands.png`). |

- **Section id:** new `MAPSEC_MIRROR_ISLE` (PROPOSED, not claimed), shared by all four maps. One of the landmark ids that [../region-sketch.md](../region-sketch.md) says is tight; Mirror Isle could also **borrow a Hoenn cave or ruin section** instead (that note's suggestion for post-game landmarks), but it is not post-game, so a new id is better.
- **Fly:** no (landmark).
- Credit Project Palladium in `CREDITS.md` in the same commit as the first trace ([../map-plan.md](../map-plan.md)). Do not use `Whirl Islands` UI icons or hash-named images.

### Layout

```
 north: open water
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~   [standing stones x4]   ~~
        ~~       SHRINE STEPS       ~~    shrine door N
        ~~    (door to Shrine hall)  ~~
  R17 ->~~    rocky east ledge      ~~
        ~~      the isle               ~~
        ~~      jetty (S)  -> R16    ~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

- **Outdoor isle.** A grassy mound with four standing stones in a square. A flight of steps leads up the north side to the shrine door. A short jetty on the south, and a ledge on the east for the R17 side. Two visible items. There is no hut: the hermit lives in the shrine hall.
- **Shrine hall (10 x 9).** Three shallow pools in the floor, each an unmoving mirror. A hermit sits in the corner. A staircase at the north leads down to the Hollow. **Puzzle:** three brass mirrors on stands must be turned (interact, each has four positions) to carry a beam of light from a window to the carved door in the north wall. The standing stones outside are the hint: their shadows at 'evening' show the three bearings. Optional puzzle with a small reward.
- **Hollow (42 x 37).** A cave of two levels under the island, with ladders, ledges and a still pool. Wild encounters here. A **tall ledge** needs Strength for a boulder. Two item spots. The way on to the Falls chamber is a dark tunnel at the north end.
- **Falls chamber (20 x 39).** A long cave room divided by a channel and a **waterfall**. The player starts at the bottom, in a pool, and must **climb the falls** with Waterfall (badge 8) to reach the upper ledge with the reward and, in the proposal, the rare Pokémon.

Door positions in words: shrine door north-centre on the outdoor isle; shrine hall exit south; stairs down north in the hall; Hollow to Falls tunnel north end of the Hollow; Falls entry south end of the chamber.

### Maps and exits

| From | To | Where |
|---|---|---|
| `MirrorIsle` | `MirrorIsle_Shrine` | shrine door, north |
| `MirrorIsle_Shrine` | `MirrorIsle_Hollow` | stairs down, north |
| `MirrorIsle_Hollow` | `MirrorIsle_Falls` | dark tunnel, north end |
| `MirrorIsle_Falls` | top ledge | **Waterfall required**, then one-way drop back |

### NPCs

6 roles (a landmark needs few). Names PROPOSED where given.

| Role | Where | Topic |
|---|---|---|
| Hermit | Shrine hall | Says the pools only show what is above them, and the sky is 'free'. Explains the mirror puzzle once. |
| Fisherman | Jetty | Says the mere is quieter in the evening, and the fish are better than R16's. |
| Plaque (bg event) | Shrine steps | A one-line shrine inscription (flavour). |
| Standing-stone signs (4) | Outdoor | The bearing hint for the mirror puzzle. |
| Wanderer | Hollow ledge | Says Strength is easier than it looks, 'push it twice'. |
| Wanderer, after the falls | Falls chamber top | Asks where the way back is. |

### Items and secrets

| Item | Where | Gate |
|---|---|---|
| ELIXIR | outdoor isle, beside a standing stone | none |
| MAX REVIVE | outdoor isle, behind a Rock Smash rock | Rock Smash (badge 2) |
| TM Light Screen | the Shrine puzzle reward | solve the mirror puzzle |
| RARE CANDY | Hollow tall ledge | Strength (badge 4) |
| PP MAX | Hollow, hidden spot (hidden item flag in the reserved 0x264 block) | none |
| MIRROR HERB | Falls top ledge (item ball) | **Waterfall (badge 8)** |
| MAX ELIXIR | Falls channel, mid-level | Waterfall (badge 8) |
| **Rare encounter (PROPOSAL)** | Falls top ledge | Waterfall (badge 8) and the shrine puzzle |

### The rare encounter (author, 2026-10-01: Mirror Isle HAS a legendary encounter)

The species is still a PROPOSAL (MESPRIT recommended). The author confirmed the encounter exists. The idea is a **single static, legendary Pokémon** that stands for 'mirror' and 'lake'. Options:

| Option | Why | Notes |
|---|---|---|
| **MESPRIT** (recommended) | A lake guardian, calm, fits a still mere, and its own name is about reflection | Level **55**, matching SUZURAN's ace, a step below MIZZLE's 60. One static battle, not roaming, flag on catch or faint. |
| CRESSELIA | Dreams and light on water | Level 55. More dramatic, harder to justify beside a Fairy city. |
| MANAPHY | A water Pokémon of the open sea | Better if the author wants something non-legendary-adjacent. |

All three exist in this tree (checked in `include/constants/species.h` and `species_info`). Alternative if no legendary: a **cache of hidden items and a 5% encounter** in the cave table (see below). The static encounter would be a `setwildbattle` script with a flag.

### Wild Pokémon

**Water around the isle (Surf and fishing):** uses the **R16** table ([routes-east.md](routes-east.md)).

**Hollow cave floor (PROPOSED, levels 49 to 53).** Two cave floors share one table. 12 slots, rates 20/20/10/10/10/10/5/5/4/4/1/1. Species checked to exist.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | CHIMECHO | 49 to 50 |
| 2 | 20% | GOLBAT | 49 to 50 |
| 3 | 10% | DITTO | 49 to 50 |
| 4 | 10% | DITTO | 50 to 51 |
| 5 | 10% | SABLEYE | 49 to 50 |
| 6 | 10% | MR_MIME | 50 to 51 |
| 7 | 5% | CLAYDOL | 51 |
| 8 | 5% | MISMAGIUS | 51 to 52 |
| 9 | 4% | ABSOL | 52 |
| 10 | 4% | BANETTE | 51 to 52 |
| 11 | 1% | SIGILYPH | 53 |
| 12 | 1% | GALLADE | 53 |

Levels start 3 below SUZURAN's ace (55 minus 3 = 52) at the high end and sit a little lower at the low end, since the island can be visited before gym 8. No Rock Smash encounters here, to keep the tables small.

### Flags (not claimed)

- `FLAG_MIRRORISLE_PUZZLE_SOLVED`: the shrine mirror puzzle.
- `VAR_MIRRORISLE_MIRRORS` (three bearings, temp var).
- `FLAG_MIRRORISLE_TM_LIGHT_SCREEN`, `FLAG_MIRRORISLE_RARE_CANDY`, `FLAG_MIRRORISLE_MIRROR_HERB`, `FLAG_MIRRORISLE_ELIXIR`: one-shots.
- `FLAG_MIRRORISLE_RARE_ENCOUNTER` (only if the proposal is accepted): the static battle done.
- Hidden items: two flags in the reserved 0x264 block.

### Build order and effort

**Medium to hard.** Four maps. The outdoor isle is a hand-built island (easy but time to paint), the Hollow and Falls are traced from Palladium (medium; the Falls room's waterfall tiles need the vanilla waterfall metatile and the HM wiring), and the mirror puzzle is a script with four object states. Order: (1) outdoor isle and shrine hall; (2) the Hollow; (3) the Falls chamber and its gate; (4) the optional encounter last.

### Open questions

1. **Keep the legendary-style encounter, and which?** (Recommended MESPRIT.) Or leave the Falls top as an item cache only.
2. **Is Mirror Isle optional?** The sketch gives it two water roads (R16 and R17) that are also the player's way to Primrose Vale, so its island could be on the main path. I treat it as optional, entered from a landing.
3. **New section id or borrowed one?** A borrowed Hoenn cave id saves one of the tight 37 free ids, but the name would say something else on the Pokénav.
4. **Hermit and puzzle size.** Is a small mirror puzzle the right flavour, or too much script for a small island?

## Ditto (author, 2026-10-01): Mirror Isle is the ONLY place to catch DITTO

The cave table above carries DITTO in slots 3 and 4 (20 percent). **DITTO must appear in no other wild table, gift, trade or Safari-style table anywhere in the game.** The other cards were checked: none lists it. The Lunatone and Solrock slots were dropped to make room. If a Ditto is wanted for breeding earlier, it is a post-badge-8 reward by design (the isle needs Surf and the Waterfall return trip).
