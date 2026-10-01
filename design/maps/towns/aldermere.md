# ALDERMERE (city, the 'Lost City', post-game, dead end; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). The sketch calls it 'Lost City' with the roads 25 and 26 (my R26). Template and rules: [../README.md](../README.md). Road: R26 in [../routes-south.md](../routes-south.md). Post-game list: [../../postgame.md](../../postgame.md). Gate: Dive comes from [beaconmouth.md](beaconmouth.md).

## Role in the story

- **Post-game, dead end.** The player cannot reach Aldermere before the League: the ferry quay at Beaconmouth is roped off, and the city's sunken half needs **Dive (badge 9)**. R26 is the only road in or out.
- **The drowned ruins** are the point. Aldermere was a great old town the sea took in one night; the dry part is the headland, the rest is a street map under the water. The player explores a ruined plateau with four glyph chambers (a tablet puzzle), an inner sanctum, and, with Dive, the sunken streets and the old town hall.
- **No gym, no scheme, no Goldsworth house** (the city rule is waived for a post-game dead end, see Open questions). A one-gag Goldsworth presence: **Winston** (the phone-talking cousin) has set up a surveyor's kiosk to 'buy the ruins' and the locals ignore it.
- A **fossil gift** (one revived Pokémon) and a **relic market**. Post-game rewards sit here: items, TMs, a rematch trainer, rare Unown.
- Tone: quiet and slightly eerie but still deadpan. The ruins were not built by anyone's ancestors; the locals shrug.

## Where it sits

North-west of Beaconmouth, the far south-east cluster's dead end (the sketch's 'lost city'). Water only.

| Road | Edge of Aldermere | How |
|---|---|---|
| R26 from Beaconmouth | **East edge** (water) | A stone quay at the south-east corner, a short wooden pier |
| (none) | North and west | Sheer cliff. Palladium's Alph render has its roads leaving by the south; keep them closed |

## Source and size

- **Palladium: `Ruins of Alph.png`** (443 x 681 px, gridded, so **26 x 40 tiles**): the ruined plateau with its four stone chambers, a research centre in the top-right corner, a pond and a gatehouse. This is the **north half** of the city.
- **South half (new):** a harbour quarter of stilted houses on shallows, about 44 x 18, from Dewford or Pacifidlog (`PacifidlogTown_Layout`, 20 x 40, floating-log tiles) as the base; no Palladium match.
- **Total size:** about **44 x 56**: `(44 + 15) * (56 + 14) = 4130`, inside 10240.
- **Interiors (all Palladium images):**
  - `RuinChambers2.png`, `RuinChambers3.png`, `RuinChambersOpen.png`, `RuinChambersOpen2.png` (150 x 168 px, about 9 x 10 tiles each): the four small **glyph chambers**.
  - `ruinsofalphinside2bl.png`, `ruinsofalphinside39cd.png` (375 x 494 px, gridded, **22 x 29 tiles**): a long hall of statues and water channels, used for the **Inner Sanctum** and the **Drowned Hall**.
  - Vanilla alternatives: `DesertRuins` and `AncientTomb` layouts (17 x 33), and `Underwater_SootopolisCity` (20 x 10) as the base for the **underwater streets** (about 40 x 30 after resizing).
- **Section id:** `MAPSEC_ALDERMERE` (name `ALDERMERE`, 9 chars). Interiors share it. The underwater map can share it too.
- **Fly and heal:** a fly destination after the first visit. One row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_ALDERMERE`.

## Layout

In plain words (north to south):

- **The Plateau (top, Palladium Alph).** A walled ruin with four stone chamber doors, a pond, trees, and a stone research building on the right. The tall statues are decoration. A path of broken tiles winds between the chambers. The Inner Sanctum door is in the centre of the northern wall, **sealed** until all four chambers are solved.
- **Research Hut (top right of the plateau).** A Pokémon Center-style shed (Pokémon Center layout `LAYOUT_POKEMON_CENTER_1F`) beside the Alph research building.
- **Stair (middle).** A flight of broken steps leads down from the plateau to the harbour quarter.
- **Harbour quarter (bottom).** Stilted houses on a wooden walk, a shop, the Fossil Scholar's cottage, the Relic Market, the harbourmaster's hut and the stone quay where R26 lands.
- **Deep-water patch (south-west of the quay).** A dark stretch of water the locals call the Hole. With Dive, the player goes down to the **sunken streets** (Underwater_Aldermere): a drowned street grid with two sunken buildings (the Old Town Hall and a Chapel). The **Old Town Hall's** stair goes up to the **Drowned Hall** (Alph inside image) beneath the plateau.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared. Placed in the Research Hut on the plateau, not the harbour (a long walk back is the joke) |
| Relic Market (Mart) | `LAYOUT_MART` | Sells Max Potion, Revive, Ultra Ball, Max Repel; buys Relic items at a high price |
| Fossil Scholar's Cottage | `LAYOUT_HOUSE2` | Gives one revived Pokémon (Lileep, Anorith, Omanyte or Kabuto, level 50, PROPOSED) |
| Harbour Master's Hut | `LAYOUT_HOUSE1` | R26 ferry rules |
| Stilt House A, B | `LAYOUT_HOUSE1`, `_HOUSE2` | Two ordinary households |
| Winston's Kiosk | exterior only | A tent with a clipboard. A one-NPC gag |
| Glyph Chambers 1 to 4 | custom, 9 x 10 each (`RuinChambers*` images) | The puzzle (below) |
| Inner Sanctum | custom, 22 x 29 (`ruinsofalphinside2bl.png`) | Wild encounters; the reward chest |
| Underwater Aldermere | custom, about 40 x 30 (`Underwater_SootopolisCity` base) | Dive. Items, wild Dive table |
| Old Town Hall | custom, 22 x 29 (`ruinsofalphinside39cd.png`) | The Drowned Hall, reachable only from underwater |
| Chapel (sunken) | `LAYOUT_HOUSE1` | A one-room hold of Relics |

## The legendary: MEW (author, 2026-10-01)

**Aldermere, the ancient city, holds a static MEW** (author's pick). It is the post-game's secret: inside the Inner Sanctum, behind the four solved Glyph Chambers (`FLAG_ALDERMERE_SANCTUM_OPEN`), floating over the sanctum's last statue. MEW exists in this tree (`SPECIES_MEW`, Gen 1).

- **Level (PROPOSED): 70**, in line with the Aldermere cave table (66 to 73). One static battle, `setwildbattle` plus a flag; MEW is shy, so it may flee (the battle can be re-triggered by leaving and re-entering until caught or defeated, decide when built).
- Fits the lore: a drowned city whose founders left no record. The researchers have a joke file called 'The Cat Problem' (a Pokémon, not an animal: say 'the pink one').
- The Inner Sanctum chest (Rare Candy, TM Dig) stays; MEW is the main prize.

## The puzzle (Glyph Chambers)

Four small chambers, each 9 x 10. Each has a **tablet** on the back wall showing four glyphs in a fixed order (a wave, an eye, a key, a circle). Four **glyph plates** sit on the floor in a row. The player steps on them in the tablet's order; a wrong plate resets all four with a soft scrape. When all four chambers are solved, the Inner Sanctum door in the plateau wall opens. Each chamber's order is different (PROPOSED, so they are not guessable). No sliding puzzles are required (the Palladium tablets slide; here they are static to save scripting).

## NPCs

12 to 20 for a city.

| Role | Where | Topic |
|---|---|---|
| Harbour master | Quay | 'We lost a town and kept the name. It saves on signs.' |
| Ferry hand | Quay | Sends the player back to Beaconmouth |
| Fossil Scholar | Cottage | Gives the fossil Pokémon after a short talk |
| Relic dealer | Relic Market | Buys relics. Rattles off prices |
| Researcher A, B | Research Hut | Studying the Unown on the walls. 'There are twenty-eight of them. We counted twice.' |
| Researcher C | Plateau | Has a clipboard; tells the player the chambers need the tablet order |
| Guard at Sanctum door | Plateau | Stands there until solved |
| Winston Goldsworth (cousin) | Kiosk | On the phone, trying to buy a drowned town. 'It is a very small offer.' Optional. Pre-set name from [../../goldsworth.md](../../goldsworth.md) |
| Old fisher | Quay | Tells the 'night the sea came' story |
| Kid with a map | Stilt walk | Draws the street grid from memory, ends in a blue scribble |
| Stilt house family | A house | Complain about the damp, proudly |
| Diver | Quay, near the Hole | Tips: 'Go down by the red buoy.' Dive hint |
| Rematch trainer (Swimmer) | Stilt walk | Post-game rematch from here |
| Cynthia's note (optional) | Research Hut table | A note: 'C.' on good paper, thanking the researchers. Hooks the Cynthia and Gatsby thread in [../../postgame.md](../../postgame.md) |

## Trainers (post-game, reuse vanilla Hoenn ids, no IVs)

| Class | Where | Team |
|---|---|---|
| Ruin Maniac | Plateau path | Golem 66, Claydol 67 |
| Ruin Maniac | Plateau path | Bronzong 67, Runerigus 68, Golurk 68 |
| Expert | Near the pond | Sigilyph 67, Beheeyem 68, Cofagrigus 68 |
| Psychic | Chamber 3 hall | Gallade 68, Alakazam 69 |
| Hex Maniac | Chamber 4 hall | Dusknoir 68, Mismagius 69, Spiritomb 69 |
| Swimmer male | Quay | Wailord 66, Tentacruel 67 |
| Swimmer female | Stilt walk | Milotic 67, Starmie 68 |
| Sailor | Stilt walk | Pelipper 66, Kingdra 68 |

## Wild Pokémon

**Plateau scrub (grass), levels 64 to 68**: all species exist in this tree.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 64 to 65 |
| 2 | 20% | PELIPPER | 64 to 65 |
| 3 | 10% | CLAYDOL | 65 |
| 4 | 10% | CRUSTLE | 65 to 66 |
| 5 | 10% | BRONZONG | 66 |
| 6 | 10% | CARBINK | 66 |
| 7 | 5% | SIGILYPH | 66 to 67 |
| 8 | 5% | RUNERIGUS | 67 |
| 9 | 4% | GOLURK | 67 to 68 |
| 10 | 4% | ABSOL | 68 |
| 11 | 1% | LUNATONE | 68 |
| 12 | 1% | SOLROCK | 68 |

**Glyph Chambers and Inner Sanctum (cave), levels 66 to 73**:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | UNOWN | 66 to 68 |
| 2 | 20% | UNOWN | 68 to 70 |
| 3 | 10% | CLAYDOL | 69 to 70 |
| 4 | 10% | BRONZONG | 69 to 70 |
| 5 | 10% | SIGILYPH | 70 to 71 |
| 6 | 10% | BEHEEYEM | 70 to 71 |
| 7 | 5% | COFAGRIGUS | 71 to 72 |
| 8 | 5% | GOLURK | 71 to 72 |
| 9 | 4% | DUSKNOIR | 72 |
| 10 | 4% | SOLROCK | 72 |
| 11 | 1% | LUNATONE | 72 |
| 12 | 1% | SPIRITOMB | 73 |

**Harbour (Surf), levels 64 to 68**: slots 60/30/5/4/1: TENTACRUEL 64 to 67, LUMINEON 64 to 67, MANTINE 65 to 68, GOREBYSS 66 to 68, RELICANTH 66 to 68.
**Old Rod**: MAGIKARP 25 to 30 (70%), TENTACOOL 25 to 30 (30%). **Good Rod**: LUVDISC 45 to 50 (60%), CORSOLA 45 to 50 (20%), FINNEON 45 to 50 (20%). **Super Rod**: LUMINEON 64 to 67 (40%), CLAWITZER 64 to 67 (40%), JELLICENT 65 to 67 (15%), KINGDRA 67 to 68 (4%), RELICANTH 67 to 68 (1%).
**Underwater (Dive), levels 66 to 70**: CLAMPERL 66 to 68 (60%), RELICANTH 67 to 69 (30%), HUNTAIL 68 to 69 (5%), GOREBYSS 68 to 69 (4%), TIRTOUGA 69 to 70 (1%).

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| Fossil Pokémon gift (one of four, level 50) | Fossil Scholar | Post-game |
| Rare Candy | Inner Sanctum chest | All four chambers solved |
| TM Dig | Inner Sanctum chest | All four chambers solved |
| Relic Copper, Silver, Gold | Plateau and chambers (visible) | None |
| Relic Vase, Band, Statue, Crown | Underwater streets (hidden or visible) | Dive |
| Star Piece, Nugget | Underwater streets | Dive |
| Max Revive | Old Town Hall chest | Dive |
| PP Max | Drowned Hall chest | Dive |
| Sea Incense | A stilt house shelf | None |
| Heart Scale x3 | Quay, plateau, stilt walk (hidden) | None |

Relics sell for a lot at the Relic Market (vanilla item values). The Maritime Museum in Kingsquay accepts one Relic Statue for a Shell Bell (see [kingsquay.md](kingsquay.md)).

## Flags (not claimed)

- `FLAG_VISITED_ALDERMERE`.
- `FLAG_ALDERMERE_CHAMBER_1_SOLVED` to `_4_SOLVED`, `FLAG_ALDERMERE_SANCTUM_OPEN`.
- `FLAG_ALDERMERE_DIVE_STREETS_DONE` (optional, for the Town Hall chest).
- `FLAG_RECEIVED_ALDERMERE_FOSSIL`.
- `FLAG_RECEIVED_RARE_CANDY_ALDERMERE`, `FLAG_RECEIVED_TM_DIG_ALDERMERE`.
- Hidden items: `FLAG_HIDDEN_ITEM_ALDERMERE_HEART_SCALE_1` to `_3`.
- A plateau-wide dive flag is not needed.

## Build order and effort

**Hard.** Two maps are big (the plateau city and the underwater streets) and there are five interiors from Palladium art. The chamber puzzle is four copies of the same small script. Build late, after Beaconmouth and R26.

## Open questions

1. Is Aldermere's R26 the only way in, with the quay closed until the League (my reading of the sketch's 'post-game')? Or should it open earlier, with only the sunken half Dive-gated?
2. A Goldsworth house for every city: I waived it here (post-game, dead end) and put Winston's kiosk instead. Fine?
3. The sketch draws a brown line beside R26 (two lines, 25 and 26). A land path along the cliff is possible; I made it water only, as README's table says.
4. Do you want a fossil gift? It needs one choice menu and four gift Pokémon.
