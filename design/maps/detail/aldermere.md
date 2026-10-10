# ALDERMERE: detailed design (the Lost City, post-game, dead end)

Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the card [../towns/aldermere.md](../towns/aldermere.md), [../../postgame.md](../../postgame.md), road R26 ([../routes-south.md](../routes-south.md)), and by looking at the Project Palladium renders `Ruins of Alph.png` (443 x 681, **26 x 40** tiles gridded), `RuinChambers2/3/Open/Open2.png` (about 9 x 10 each), `ruinsofalphinside2bl.png` and `ruinsofalphinside39cd.png` (**22 x 29** each), and the Team Aqua examples named below. Templates **G4-A, G4-B, G4-C** are in [ebbsworth.md](ebbsworth.md) section 6.0. Neighbours: [beaconmouth.md](beaconmouth.md) (ferry, Dive), [kingsquay.md](kingsquay.md) (Maritime Museum, Winston's house), [vesperhaven.md](vesperhaven.md).

> **Villain teams (author, 2026-10-04):** Aldermere is the **ancestral seat of the Drowned Crown**: its kings and queens ruled the waters from here before time was recorded. **Dialga's anchor** lies in the sunken city, a moment frozen in time that holds back the flood so it cannot sink the whole region. Post-game, the **Crown's last people take refuge here**, docile now their leader has fallen, and offer **a Battle Tower or something else significant**. **Kyogre** can be met near the anchor at a random hour each day; one of them hints at the hour. **This changes parts of this file** (the 'ruins built by nobody's ancestors' tone, the Winston kiosk gag may stay or go). Not yet reconciled: rework this file when Aldermere is designed in detail. See [../../factions.md](../../factions.md).

**New minor names and details introduced in this file are all PROPOSED:** Excavation Office, Research Annex, Old Town Hall lobby, Drowned Hall, Chapel, the researchers' joke file 'The Pink Problem', the four plate orders, `Aldermere_Harbour` as a map name.

Conventions: **(x, y) from the top-left tile (0,0)** of each map; footprints `(x0,y0)-(x1,y1)` inclusive; a 4-wide building's door is `(x0+1, y1)`; interior mats two tiles wide; maps stay `layout_version` `emerald`, `REGION_HOENN`, section `MAPSEC_ALDERMERE`.

---

## 1. Quick facts

| | |
|---|---|
| Outdoor maps | **Two**, not one (see section 2 and open question 1): **`Aldermere`** (the plateau, **44 x 40**: the Alph render placed at x 9-34) and **`Aldermere_Harbour`** (the stilt quarter, **44 x 18**). Joined by a stair connection. `(44+15)*(40+14) = 3186` and `(44+15)*(18+14) = 1888`, both under 10240 |
| Why two | The card's single 44 x 56 map would hold 16 live objects (8 trainers plus 8 talkers), over the **15-object limit**. Splitting plateau and harbour gives 7 and 9 |
| Underwater / interiors | `Underwater_Aldermere` (40 x 30), 4 Glyph Chambers (9 x 10), Inner Sanctum (22 x 29), Old Town Hall lobby and Drowned Hall (22 x 29), Chapel, Pokémon Center, Mart, Fossil Scholar's Cottage, Harbour Master's Hut, two stilt houses: about **18 maps** |
| Exterior base | Plateau: Palladium `Ruins of Alph.png` traced. Harbour: vanilla `PacifidlogTown` (20 x 40, floating log walks) |
| Music | Plateau `MUS_MT_PYRE_EXTERIOR` (windswept ruins), harbour `MUS_LILYCOVE` (what vanilla Pacifidlog uses), chambers, Sanctum and Drowned Hall `MUS_SEALED_CHAMBER`, underwater `MUS_UNDERWATER`, the Mew battle `MUS_VS_MEW`. All exist in `include/constants/songs.h` |
| Weather | Plateau `WEATHER_FOG_HORIZONTAL` (the quiet, eerie mood of the card); harbour `WEATHER_SUNNY`; underwater `WEATHER_UNDERWATER_BUBBLES` |
| Gym / scheme | None. A one-gag Goldsworth presence (Winston's kiosk). A **static MEW, level 70**, re-offered until caught |
| Fly / heal | Fly town **after the first visit**; `HEAL_LOCATION_ALDERMERE` on the plateau outside the Center door, (30,12) |
| Roads | R26 only, at the harbour map's east edge, post-game. **The only way in or out** |
| Build effort | **Hard**; build late, after Beaconmouth and R26 |

---

## 2. Description

**First glance, from R26 (post-game, the harbour).** The ferry, or the player surfing, comes out of grey open water into a shallow lagoon: a boardwalk on stilts running across the shallows, four weathered houses on legs, a tent on the walk, and a patch of dark water the locals call the Hole. Behind, up a long flight of broken steps, a plateau of pale ruins with a fog on it. The harbour is lived-in and damp; the plateau is the thing everyone points at.

**Mood, colour, sound, time of day.** Quiet, a little eerie, still deadpan (card). Palette: bleached stone and sandy pavers, faded gold carved bands, green moss, pale sea; the plateau under a low mist; the harbour in flat afternoon light. Sound: wind and distant water; the **ruin themes** from the tree (`MUS_MT_PYRE_EXTERIOR`, `MUS_SEALED_CHAMBER`); nobody sings. The locals shrug at the ruins ('We lost a town and kept the name. It saves on signs').

**The one memorable view.** From the top of the steps at (14,36) on the plateau looking up the central stone road: six rows of statues, the glyph frieze, the sealed Sanctum door in the middle, a fog line at the top, and behind you, below the steps, the whole stilt harbour with the Hole as a dark coin in the water.

---

## 3. Street layout in words (a numbered walk)

### 3.1 The harbour (`Aldermere_Harbour`, 44 x 18)

1. **East quay and the R26 landing (x 38-43, y 8-13).** A stone quay at the east edge; R26's water connects at x 43, y 9-12. The **Ferry hand** (39,10) and **Old fisher** (40,8) stand here. **Harbour Master's Hut** (34,8)-(37,11), door (35,11).
2. **The stilt walk (x 12-41, y 6-7).** A 2-wide boardwalk of floating-log pieces (Pacifidlog tiles) over the shallows, running west to the foot of the steps.
3. **Houses along the walk (north side, doors on y 5):** **Fossil Scholar's Cottage** (16,2)-(19,5) door (17,5); **Relic Market** (22,2)-(25,5) door (23,5); **Stilt House A** (28,2)-(31,5) door (29,5); **Stilt House B** (34,2)-(37,5) door (35,5).
4. **Winston's kiosk (27,9)-(29,10)**: a striped tent with a clipboard, **Winston** at (28,11) facing up. A short jetty (24,8)-(25,10) beside it where the **Diver** stands.
5. **The Hole (x 20-24, y 11-15).** A dark patch of deep water south of the walk: the **Dive spot** at (22,13).
6. **The steps (x 13-16, y 0-5).** A flight of broken stone steps up to the plateau at the harbour map's north edge; the **Kid with a map** at (14,7) on the walk.

### 3.2 The plateau (`Aldermere`, 44 x 40)

The Alph render sits at **x 9-34**; a belt of trees and sheer cliff (x 0-8 and x 35-43) closes the sides, because 'North and west: sheer cliff' (card). Alph render coordinates are converted below (**map x = render x + 9, map y = render y**).

1. **The steps (x 13-16, y 36-39)** at the bottom connect south to the harbour (connection `down`, offset 0). The player arrives here.
2. **The central road.** A sand-and-flagstone path winds north through the ruin: past the left grass patch (x 11-12, y 20-24), the **Research Annex** (27,18)-(33,21), the bottom-right pond (23,26)-(26,30), and up to the sealed **Inner Sanctum** door at (22,14), centre-north.
3. **Four Glyph Chamber doors** (rock-built temple entrances): **Chamber 1** top-right, door (27,6); **Chamber 2** left, door (13,18); **Chamber 3** bottom-left, door (14,30); **Chamber 4** bottom-right, door (28,33).
4. **Research Hut (the Pokémon Center), top right (29,8)-(32,11), door (30,11).** The white-and-red pod of the render; the **Researcher A and B** are inside it.
5. **Excavation Office (17,0)-(23,4)** at the top: the grey glass-fronted building, exterior only, locked (a sign and a rope).
6. **Ponds:** west pond (13,6)-(16,13), bottom-right pond (23,26)-(26,30) (scenery and fishing spots).
7. **Guard post at the Sanctum door (22,15).** The **Guard** stands in front until `FLAG_ALDERMERE_SANCTUM_OPEN`.
8. **Plateau scrub.** Tall grass (wild encounters, the 'plateau scrub' table in the card): the render's patch at (11,20)-(12,24) plus two added patches (30,24)-(33,27) and (11,34)-(14,37). Everywhere else is stone path or bare sand.

---

## 4. Map plans

### 4.1 `Aldermere` (plateau), sketch at 1 char = 2 x 2 tiles

Legend: `T` cliff and trees, `X` Excavation Office, `a` Chamber 1, `~` pond, `P` Pokémon Center, `S` Inner Sanctum, `b` Chamber 2, `R` Research Annex, `g` scrub grass, `c` Chamber 3, `d` Chamber 4, `s` steps.

```
x:  0    1    2    3    4 
y0  TTTTT...XXXX.....TTTTT
y2  TTTTT...XXXX.aaa.TTTTT
y4  TTTTT...XXXX.aaa.TTTTT
y6  TTTTT.~~~....aaa.TTTTT
y8  TTTTT.~~~.....PPPTTTTT
y10 TTTTT.~~~.SSS.PPPTTTTT
y12 TTTTT.~~~.SSS....TTTTT
y14 TTTTT.bb..SSS....TTTTT
y16 TTTTT.bb.........TTTTT
y18 TTTTT.bb.....RRRRTTTTT
y20 TTTTTgg......RRRRTTTTT
y22 TTTTTgg..........TTTTT
y24 TTTTTgg..........TTTTT
y26 TTTTT......~~~...TTTTT
y28 TTTTT.cc...~~~...TTTTT
y30 TTTTT.cc...~~ddd.TTTTT
y32 TTTTT........ddd.TTTTT
y34 TTTTT............TTTTT
y36 TTTTT.sss........TTTTT
y38 TTTTTTsssTTTTTTTTTTTTT
```
(Header digits mark every 10 tiles. Generated from the footprints in this section.)

Connection: **south** edge x 13-16 to `Aldermere_Harbour` north edge x 13-16 (offset 0).

### 4.2 `Aldermere_Harbour`, sketch at 1 char = 2 x 2 tiles

Legend: `s` steps, `F` Fossil Scholar, `M` Relic Market, `A` Stilt House A, `B` Stilt House B, `=` stilt walk, `j` jetty, `k` kiosk tent, `H` Harbour Master, `q` stone quay, `~` water.

```
x:  0    1    2    3    4 
y0  ......sss.............
y2  ......ssFF.MM.AA.BB...
y4  ......ssFF.MM.AA.BB...
y6  ......===============.
y8  ~~~~~~~~~~~~jkk~~HHqqq
y10 ~~~~~~~~~~~~jkk~~HHqqq
y12 ~~~~~~~~~~~~~~~~~..qqq
y14 ~~~~~~~~~~~~~~~~~...~~
y16 ~~~~~~~~~~~~~~~~~...~~
```
Connections: **north** to the plateau (offset 0); **east** to `R26` (x 43, y 9-12, water; post-game).

---

## 5. Base, tilesets, palette notes

**Plateau.** Trace `Ruins of Alph.png` (gridded, 26 x 40) at x 9-34. The render is a mix of trees, rock-built temple doors, ponds and sand. Recommended painting:

| Where | Primary | Secondary | Source and credit |
|---|---|---|---|
| Plateau (exterior) | `gTileset_General` | **Autumn Ruins Secondary** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/Autumn Ruins Secondary` (example looked at: a courtyard of pale bricks with a long carved glyph frieze, standing pillars, three small temples with altar blocks and statues, sandy trees and grass, a stone gate). **Credits (its credits.md):** assembler **Yumekua**; main creators **Ekat99, Heartlessdragoon, Vurtax**; more creators **Redblueyellow, Morlockhater, Nemu**; credit **Rahtak** for the insertable reformat. **It is triple-layer** (`metatiles.bin` is 12288 bytes = 512 triple-layer metatiles, 512 tiles), so it needs the same **Porytiles conversion** Gen 4 Interior got (design/interiors.md). Needs a `CREDITS.md` row in the commit that imports it |
| Chambers, Sanctum, Drowned Hall, Chapel, Town Hall lobby | `gTileset_Building` | **Autumn Ruins Secondary** (same) | Same import. The example's three temples show interior altar floors and statue pairs, matching the 9 x 10 chambers almost exactly |
| Underwater streets | **Underwater Primary** (new pair) | **Underwater Secondary** | `.../Underwater Primary`, `.../Underwater Secondary`. Credits: Primary **Ekat, Vurtax, Heartlessdragoon**; Secondary **Hek (hek-el-grande), Ekat, Vurtax, Heartlessdragoon**; credit **Rahtak** for the insertable reformat. The example shows a drowned city: a hex-roofed hall with columns, two columned temples, broken pillars and benches, coral patches. Both `metatiles.bin` are 6144 bytes (384 two-layer or 256 triple-layer; the READMEs do not mention triple-layer, so expect two-layer: check in Porymap). Import as a **new pair**; do not replace the vanilla underwater tilesets, which the vanilla routes use. The Secondary has an `anim` folder (animated water): static first, animation only with an approved engine edit |
| Harbour | `gTileset_General` | vanilla `gTileset_Pacifidlog` | Vanilla (floating log walks). The Aldermere harbour can also use LeoB ORAS if the author imports it; **LeoB's `secondary/` set has no Pacifidlog**, so vanilla Pacifidlog it is |
| Pokémon Center, Mart | `gTileset_Building` | `PokemonCenter`, `Shop` | Vanilla |
| Houses, cottage, hut | `gTileset_Building` | `Gen4Interior` | Hollowbrook's |

**Fallback with no import at all:** plateau on `gTileset_General` + `gTileset_Slateport` stone paving (vanilla), chambers and Sanctum on the vanilla cave secondaries (the Desert Ruins and Ancient Tomb layouts are 17 x 33 caves in the same tree and already carry Braille), underwater on vanilla `gTileset_Underwater`. It is much plainer.

**Glyph tiles.** The four plate glyphs (wave, eye, key, circle) and the tablet need **four distinct carved-glyph metatiles**. The Autumn Ruins frieze band carries about six different spiral, ring and hook glyphs: pick four, build four plate metatiles (the glyph on a stone plate) and four tablet metatiles (the same glyph on the wall). If the author prefers, draw them: 8 small metatiles.

**Encounter tiles.** Wild encounters on foot need floor metatiles that carry the 'land encounter' attribute (cave floor does; building floor does not). In Porymap's tileset editor set **Encounter Type: Land** on the Autumn Ruins floor metatiles used in the chambers, Sanctum and Drowned Hall. Water and fishing encounters need the usual surf and fishing JSON only.

**Palladium credit.** The first commit that traces `Ruins of Alph.png`, a chamber image or an inside image adds a `CREDITS.md` row crediting the **Project Palladium team** with the file names.

---

## 6. Buildings and interiors

### 6.1 Overview

| # | Place | Map | Footprint / door | Layout |
|---|---|---|---|---|
| 1 | Research Hut (Pokémon Center) | `Aldermere_PokemonCenter_1F`, `_2F` | (29,8)-(32,11), door (30,11) | `LAYOUT_POKEMON_CENTER_1F`, `_2F` |
| 2 | Relic Market | `Aldermere_Mart` (harbour) | (22,2)-(25,5), door (23,5) | `LAYOUT_MART` |
| 3 | Fossil Scholar's Cottage | `Aldermere_FossilScholarsCottage` | (16,2)-(19,5), door (17,5) | custom G4-C style (12 x 9) |
| 4 | Harbour Master's Hut | `Aldermere_HarbourMastersHut` | (34,8)-(37,11), door (35,11) | G4-A (11 x 8) |
| 5 | Stilt House A | `Aldermere_StiltHouseA` | (28,2)-(31,5), door (29,5) | G4-A |
| 6 | Stilt House B | `Aldermere_StiltHouseB` | (34,2)-(37,5), door (35,5) | G4-B (10 x 8) |
| 7 | Winston's kiosk | none | (27,9)-(29,10) | exterior only |
| 8 | Glyph Chambers 1 to 4 | `Aldermere_Chamber1` to `_4` | doors (27,6), (13,18), (14,30), (28,33) | custom 9 x 10 each |
| 9 | Inner Sanctum | `Aldermere_InnerSanctum` | door (22,14) (sealed) | custom 22 x 29 |
| 10 | Underwater streets | `Underwater_Aldermere` | Dive at harbour (22,13) | custom 40 x 30 |
| 11 | Old Town Hall (sunken) lobby | `Aldermere_OldTownHall` | underwater door | custom 14 x 10 |
| 12 | Drowned Hall | `Aldermere_DrownedHall` | stair from the Town Hall | custom 22 x 29 (a copy of the Sanctum painting) |
| 13 | Chapel (sunken) | `Aldermere_Chapel` | underwater door | custom 9 x 8 |
| 14 | Excavation Office, Research Annex | none | exterior only | |

### 6.2 Pokémon Center (the Research Hut), Mart (the Relic Market)

Vanilla layouts, unmoved. The Center sits **on the plateau, not the harbour** (a long walk back is the card's joke). Positions (vanilla): nurse (7,2), mats (6,8),(7,8), stairs (1,6). **Researcher A** at (3,3) `FACE_DOWN` and **Researcher B** at (10,6) `FACE_LEFT`, studying the Unown on the walls ('There are twenty-eight of them. We counted twice.'). **Cynthia's note** (optional): a `bg_event` on the glass table at (11,6): a note on good paper signed 'C.' thanking the researchers (hooks the Cynthia and Gatsby thread in postgame.md). The Mart stocks Max Potion, Revive, Ultra Ball, Max Repel; the **Relic dealer** at the Mart counter (clerk (1,3)) rattles off relic prices (relics sell for vanilla item values; no special code). The card's joke file name contains a real-animal word, so I renamed it: the researchers' joke file is **'The Pink Problem'**, which means MEW (say 'the pink one').

### 6.3 Fossil Scholar's Cottage (custom, 12 x 9)

**Purpose.** One revived fossil Pokémon, a choice of four (card, PROPOSED: Lileep, Anorith, Omanyte or Kabuto, level 50). Plan:

```
     x0 1 2 3 4 5 6 7 8 9 10 11
y0   #  # # # # # # # # # #  #
y1   c  c . W . . . W . . c  c      c = fossil display case (bg_event; flavour text per fossil) at (0,1),(1,1),(10,1),(11,1)
y2   c  c . . . . . . . . c  c
y3   .  . . . . . . . . . .  .
y4   .  . . . . . . N . . .  .      N = Fossil Scholar (7,4) facing left
y5   .  P . R R f f R R . P  .      f = low table (5,5),(6,5)
y6   .  . . R R R R R R . .  .
y7   .  . . . . . . . . . .  .
y8   .  . . . . D D . . . .  .
```
Mats (5,8),(6,8). **Fossil Scholar** (7,4) `FACE_LEFT`: after a short talk offers the **gift** via a four-way menu (Lileep, Anorith, Omanyte, Kabuto) (`FLAG_RECEIVED_ALDERMERE_FOSSIL`); one choice only. Warps: mats to `Aldermere_Harbour` warp 0 (door (17,5)).

### 6.4 Harbour Master's Hut (G4-A) and the stilt houses

- **Harbour Master's Hut (G4-A 11 x 8).** The **Harbour master** is on the quay outside (section 8); the hut holds his **clerk** at (8,4) `FACE_LEFT` and the R26 ferry rules `bg_event` (7,2). Warps: mats (2,7),(3,7) to `Aldermere_Harbour` warp 4 (door (35,11)).
- **Stilt House A (G4-A).** A family (grumbling about the damp, proudly): mother (5,6) `FACE_UP`, father (8,3) `FACE_UP`, child (9,5) wandering; **Sea Incense** on the shelf as a visible item ball at (8,2) (no gate). Warps: mats (2,7),(3,7) to `Aldermere_Harbour` warp 2.
- **Stilt House B (G4-B 10 x 8).** An old couple: a woman (5,5) and a man (3,4) `FACE_RIGHT`; a barometer on the wall (bg_event (3,1)). Warps: mats (3,7),(4,7) to `Aldermere_Harbour` warp 3.

### 6.5 The four Glyph Chambers (9 x 10 each, from the `RuinChambers` images)

The four Palladium images (150 x 168 px) show a small stone room: a back wall with a carved tablet at the centre, two statues in front of it, a central altar block, a pale carpet, and a small door tile at the bottom. `RuinChambers2/3` are the closed state and `RuinChambersOpen/Open2` the **solved** state (the back wall shows a dark doorway). Build **one chamber layout**, duplicate it three times, and give each its own plate order. The plan (1 tile = 1 character; `T` tablet on the back wall as a `bg_event`, `S` statue, `A` altar block, `p` glyph plate = a `coord_event` tile, `D` exit mat):

```
     x: 0 1 2 3 4 5 6 7 8
y0    # # # # # # # # #
y1    # # # # T # # # #
y2    # . . . . . . . #
y3    # . S A A A S . #
y4    # . S A A A S . #
y5    # . . . . . . . #
y6    # . p p . p p . #
y7    # . . . . . . . #
y8    # . . . . . . . #
y9    # # # # D D # # #
```
The four plates at (2,6), (3,6), (5,6), (6,6) show four different glyphs (**Wave, Eye, Key, Circle**); the **tablet** at (4,1) shows the same four in a fixed order. The player stands at the mat (4,8), reads the tablet, then steps on the plates **in that order**; each correct step lights the plate; a wrong step resets all four with a soft scrape. When the fourth is right, the tablet is swapped for its 'open' variant (the `RuinChambersOpen` picture), a short chime plays and `FLAG_ALDERMERE_CHAMBER_n_SOLVED` is set. Progress is kept in a **map-scoped temp var** (`VAR_TEMP_0`, cleared on map load), so no spare var is spent. 16 `coord_event`s in total (4 per chamber). No sliding puzzle (the card keeps the tablets static).

| Chamber | Where (door on the plateau) | Floor, left to right (plates at x 2, 3, 5, 6) | **Tablet order (PROPOSED)** |
|---|---|---|---|
| 1 | Top right, door (27,6) | Wave, Eye, Key, Circle | Wave, Key, Eye, Circle |
| 2 | Left, door (13,18) | Key, Circle, Wave, Eye | Circle, Eye, Key, Wave |
| 3 | Bottom left, door (14,30) | Eye, Wave, Circle, Key | Key, Wave, Circle, Eye |
| 4 | Bottom right, door (28,33) | Circle, Key, Eye, Wave | Eye, Wave, Circle, Key |

Each order is a different permutation of its own floor, so none of them can be guessed from the others. Each chamber's exit mats (4,9),(5,9) warp to the plateau's door tile for that chamber. A **Relic** sits in each of Chambers 2 and 4 (visible: Relic Silver at (7,7) in Chamber 2, Relic Gold at (1,7) in Chamber 4); **Relic Copper** lies on the plateau at (31,26). Trainers: the **Psychic** in front of Chamber 3 (14,31) and the **Hex Maniac** in front of Chamber 4 (28,35), both on the plateau: 'Chamber 3 hall' and 'Chamber 4 hall' in the card are read as the yard in front of each door.

**Chamber encounters.** The card's 'Glyph Chambers and Inner Sanctum (cave)' table (levels 66 to 73) applies inside the chambers too: set the land-encounter attribute on the chamber floor metatiles (section 5). If the author would rather keep the chambers quiet, leave the attribute off in them.

### 6.6 The Inner Sanctum (22 x 29, `ruinsofalphinside…` image) and MEW

**Image choice.** The card assigns `ruinsofalphinside2bl.png` to the Sanctum and `ruinsofalphinside39cd.png` to the Drowned Hall. Looking at them, the two are the **same hall** with different decoration: `2bl` has **water channels** (teal strips), `39cd` has **carved glyph strips**. The glyph version is the right look for the Sanctum, the flooded one for the **Drowned Hall**. I recommend **swapping** the card's assignment (open question 2). Both halls share one layout, so paint once and duplicate.

**The plan** (1 tile = 1 character; `S` statue, `P` carved glyph strip (blocked), `X` the central stair tile (decoration, blocked), `D` entrance mats, `*` item balls). Validated with a small path check: from the entrance the whole hall, the top row and the spot beside the last statue are reachable, by a zigzag through four gaps.

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
y0    # # # # # # # # # # # # # # # # # # # # # #
y1    # # # # # # # # # # # # # # # # # # # # # #
y2    # . . . . . . . . . * . . . . . . . . . . #
y3    # . . S . . S . . S . . S . . S . . S . . #
y4    # . . . . . . . . . . . . . . . . . . . . #
y5    # P P P . . . P P P P P P P P P P P P P P #
y6    # P P P . . . P P P P P P P P P P P P P P #
y7    # . . . . . . . . . . . . . . . . . . . . #
y8    # . . . . . . . . . . . . . . . . . . . . #
y9    # . . S . . S . . S . . S . . S . . S . . #
y10   # P P P P P P P P P P P P P P . . . P P P #
y11   # P P P P P P P P P P P P P P . . . P P P #
y12   # . . . . . . . . . . . . . . . . . . . . #
y13   # . . . . . . . . . . . . . . . . . . . . #
y14   # . . . . . . . . . X . . . . . . . . . . #
y15   # . . S . . . . . . . . . . . . . . S . . #
y16   # . . . . . . . . . . . . . . . . . . . . #
y17   # P P P . . . P P P P P P P P P P P P P P #
y18   # P P P . . . P P P P P P P P P P P P P P #
y19   # . . . . . . . . . . . . . . . . . . . . #
y20   # . . . . . . . . . . . . . . . . . . . . #
y21   # . . S . . S . . S . . S . . S . . S . . #
y22   # P P P P P P P P P P P P P P . . . P P P #
y23   # P P P P P P P P P P P P P P . . . P P P #
y24   # . . . . . . . . . . . . . . . . . . . . #
y25   # . . . . . . . . . . . . . . . . . . . . #
y26   # . . S . . S . . S . . S . . S . . S . . #
y27   # . . . . . . . . . . . . . . . . . . . . #
y28   # # # # # # # # # # D D # # # # # # # # # #
```

- **Entrance** from the plateau door (22,14): mats (10,28),(11,28) (the plateau door warps to the Sanctum mat). The route is a **zigzag**: up through the gap at x 15-17 (strip at y 22-23), west to the gap at x 4-6 (y 17-18), east to the gap at x 15-17 (y 10-11), west to the gap at x 4-6 (y 5-6), then the top row.
- **MEW** (static, level **70**, PROPOSED) hovers at **(18,14)** over the isolated statue at (18,15), at the east end of the middle corridor, which the zigzag passes within one tile of (the gap at x 15-17, y 10-11 is reached from there). Object `SPECIES(MEW)` facing down, `OBJ_EVENT_GFX_...` of the species sprite. Script: `setwildbattle SPECIES_MEW, 70`, `dowildbattle`, then branch on the outcome: **caught** sets `FLAG_CAUGHT_MEW_ALDERMERE` (PROPOSED) and hides the object for good; **won, fled or ran** (any other result): the object disappears for the session and **reappears on the next visit** (author, 2026-10-01: re-offered until caught). The flag is set **only on a catch**. Music `MUS_VS_MEW`.
- **Chest items:** Rare Candy at (10,2) and **TM Dig** at (11,2), item balls (the card calls them the Inner Sanctum chest). They are reachable only after the zigzag, so the sanctum's door is the lock.
- **Sanctum door on the plateau.** The plateau tile (22,14) is a wall metatile (a sealed carved door) with a warp event placed on it; when all four `FLAG_ALDERMERE_CHAMBER_n_SOLVED` flags are set (checked when the player talks to the Guard, or on the next plateau load), the script sets `FLAG_ALDERMERE_SANCTUM_OPEN`, swaps the tile for the open-door metatile and the Guard (22,15) steps aside. Pre-placing the warp event means no runtime warp creation is needed.
- **Wild table:** the cave table (levels 66 to 73) with the land-encounter attribute on the hall's floor.

### 6.7 The sunken city: Dive, Town Hall, Drowned Hall, Chapel

**`Underwater_Aldermere` (40 x 30), Underwater Primary and Secondary.** A street grid under the sea. Entered by **Dive** at the harbour's Hole (22,13); the dive connection surfaces the player at (20,28) on the underwater map's south edge (the surfacing spot in Porymap's Dive and Emerge connections). Sketch (1 character = 2 x 2 tiles, generated from the positions below; `H` Old Town Hall, `C` Chapel, `T` ruined temple (decor), `=` streets, `w` seaweed (Dive encounter tiles), `*` items, `^` the surfacing spot):

```
x:  0    1    2    3    
y0  ....................
y2  .......HHHHHH.......
y4  .......*HHHHH.......
y6  .......HHHHHH.......
y8  .......HHHHHH.......
y10 .......HH==HH...*...
y12 .CCCCC...==...TTTTT.
y14 .CCCCC...==...TTTTT.
y16 .CCCCC...==...TTTTT.
y18 .==================.
y20 .==============*===.
y22 .wwwwww..==...wwwww.
y24 .w*wwww..==...wwwww.
y26 .wwwwww..==...wwwww.
y28 .wwwwww..^^...wwwww.
```

Exact positions:

- **Old Town Hall** exterior (hex-roofed hall with columns from the Underwater Secondary example): footprint (14,3)-(25,10), door (19,10). Warp to `Aldermere_OldTownHall`.
- **Chapel** exterior (columned temple): (3,13)-(10,17), door (6,17). Warp to `Aldermere_Chapel`.
- **Ruined temple** (decor, a second columned building): (28,13)-(36,18).
- **Streets:** a main street x 19-21 from the surfacing spot (20,28) north to the Town Hall door; a cross street y 19-20, x 3-37; a west street x 6-7 up to the Chapel.
- **Seaweed (encounter tiles):** patches at (2,22)-(12,28) and (28,22)-(37,28).
- **Items (Dive):** **Relic Statue** hidden at (33,10); **Relic Crown** hidden at (5,24); **Star Piece** visible at (30,20); **Nugget** hidden at (14,4). (The Chapel holds the Relic Vase and Relic Band; Old Town Hall and Drowned Hall chests hold Max Revive and PP Max.)
- **Wild (Dive), levels 66 to 70** (card): CLAMPERL 66 to 68 (60%), RELICANTH 67 to 69 (30%), HUNTAIL 68 to 69 (5%), GOREBYSS 68 to 69 (4%), TIRTOUGA 69 to 70 (1%).

**`Aldermere_OldTownHall` (14 x 10, dry air pocket).** A pale hall with fallen pillars: a **Max Revive** in a chest at (11,2) (item ball), a stair at (2,2) to the Drowned Hall, mats (6,9),(7,9) to the underwater door (19,10). No NPCs.

**`Aldermere_DrownedHall` (22 x 29).** A **copy of the Sanctum painting with the strips painted as water channels** (impassable) instead of glyph strips, no statue-Mew, no encounters needed (or the same cave table, card does not say). Entered from the Town Hall stair at (2,2) arriving at the bottom mats (10,28),(11,28); **PP Max** at (10,2) at the top. This is one hall, built twice. A visible puzzle-free zigzag.

**`Aldermere_Chapel` (9 x 8).** One room: an altar block at (4,2), two benches at (2,5),(6,5) (decor), **Relic Vase** at (3,2) and **Relic Band** at (5,2) (item balls), mats (4,7),(5,7) to the underwater door (6,17). The card's 'A one-room hold of Relics'.

---

## 7. Door and warp tables

`Aldermere` (plateau) outdoor warps:

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (30,11) | `Aldermere_PokemonCenter_1F` | 0 |
| 1 | (27,6) | `Aldermere_Chamber1` | 0 |
| 2 | (13,18) | `Aldermere_Chamber2` | 0 |
| 3 | (14,30) | `Aldermere_Chamber3` | 0 |
| 4 | (28,33) | `Aldermere_Chamber4` | 0 |
| 5 | (22,14) | `Aldermere_InnerSanctum` (sealed until `FLAG_ALDERMERE_SANCTUM_OPEN`) | 0 |

`Aldermere_Harbour` outdoor warps:

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (17,5) | `Aldermere_FossilScholarsCottage` | 0 |
| 1 | (23,5) | `Aldermere_Mart` | 0 |
| 2 | (29,5) | `Aldermere_StiltHouseA` | 0 |
| 3 | (35,5) | `Aldermere_StiltHouseB` | 0 |
| 4 | (35,11) | `Aldermere_HarbourMastersHut` | 0 |
| (dive) | (22,13) | `Underwater_Aldermere` (surface (20,28)) | |

(Follow Porymap's numbering if it differs from this table.)

Interior mats and stairs:

| Map | Tiles | Destination | Dest warp |
|---|---|---|---|
| `Aldermere_PokemonCenter_1F` | (6,8),(7,8) / stairs (1,6) | `Aldermere` 0 / `_2F` | |
| `Aldermere_Mart` | (3,7),(4,7) | `Aldermere_Harbour` | 1 |
| `Aldermere_FossilScholarsCottage` | (5,8),(6,8) | `Aldermere_Harbour` | 0 |
| `Aldermere_StiltHouseA` | (2,7),(3,7) | `Aldermere_Harbour` | 2 |
| `Aldermere_StiltHouseB` | (3,7),(4,7) | `Aldermere_Harbour` | 3 |
| `Aldermere_HarbourMastersHut` | (2,7),(3,7) | `Aldermere_Harbour` | 4 |
| `Aldermere_Chamber1` to `_4` | (4,9),(5,9) | `Aldermere` | 1 to 4 |
| `Aldermere_InnerSanctum` | (10,28),(11,28) | `Aldermere` | 5 |
| `Underwater_Aldermere` | (19,10) door | `Aldermere_OldTownHall` | 0 |
| `Underwater_Aldermere` | (6,17) door | `Aldermere_Chapel` | 0 |
| `Aldermere_OldTownHall` | (6,9),(7,9) / stair (2,2) | `Underwater_Aldermere` (19,10) / `Aldermere_DrownedHall` | |
| `Aldermere_DrownedHall` | (10,28),(11,28) | `Aldermere_OldTownHall` stair | |
| `Aldermere_Chapel` | (4,7),(5,7) | `Underwater_Aldermere` (6,17) | |

---

## 8. NPCs, trainers, objects

**Plateau (7 objects):** the 5 trainers and the two talkers.

| Object | Tile | Facing, sight | Role |
|---|---|---|---|
| Ruin Maniac A (Golem 66, Claydol 67) | (20,22) | `FACE_LEFT`, 4 | Plateau path |
| Ruin Maniac B (Bronzong 67, Runerigus 68, Golurk 68) | (16,27) | `FACE_UP`, 3 | Plateau path |
| Expert (Sigilyph 67, Beheeyem 68, Cofagrigus 68) | (17,12) | `FACE_LEFT`, 3 | Near the west pond |
| Psychic (Gallade 68, Alakazam 69) | (14,31) | `FACE_UP`, 3 | Yard of Chamber 3 |
| Hex Maniac (Dusknoir 68, Mismagius 69, Spiritomb 69) | (28,35) | `FACE_UP`, 3 | Yard of Chamber 4 |
| Researcher C | (24,17) | `FACE_DOWN` | Has a clipboard: 'the chambers need the tablet order' |
| Guard at the Sanctum door | (22,15) | `FACE_UP` | Stands there until solved (hidden after) |

**Harbour (9 objects):**

| Object | Tile | Facing, sight | Role |
|---|---|---|---|
| Swimmer male (Wailord 66, Tentacruel 67) | (41,15) | `FACE_UP`, 4 | In the water off the quay |
| Swimmer female (Milotic 67, Starmie 68) | (26,8) | `FACE_DOWN`, 4 | By the stilt walk; **post-game rematch trainer** (card) |
| Sailor (Pelipper 66, Kingdra 68) | (33,6) | `FACE_LEFT`, 3 | On the stilt walk |
| Harbour master | (36,12) | `FACE_DOWN` | On the quay by his hut: 'We lost a town and kept the name. It saves on signs.' |
| Ferry hand | (39,10) | `FACE_LEFT` | 'Sends the player back to Beaconmouth' |
| Winston Goldsworth | (28,11) | `FACE_UP` | Kiosk: 'It is a very small offer.' Optional; PROPOSED continuity: he lost the harbour at Kingsquay |
| Old fisher | (40,8) | `FACE_RIGHT` | The 'night the sea came' story |
| Kid with a map | (14,7) | `WANDER_AROUND` | Draws the street grid from memory, ends in a blue scribble |
| Diver | (25,9) | `FACE_DOWN` | 'Go down by the red buoy.' Dive hint |

Trainers reuse vanilla Hoenn ids (CLAUDE.md), `IVs: 0` lines, Pokémon only; classes are Ruin Maniac, Expert, Psychic, Hex Maniac, Swimmer, Sailor. The Swimmer and Sailor teams are the card's. **Winston** is a cousin; he may speak with mild swearing, nobody else.

Bg events: plateau signs at (29,6) and (25,15) (the render's two signs: 'RUINS' and 'CHAMBERS'), steps sign, harbour sign 'ALDERMERE', Winston's clipboard, the Hole's red buoy at (22,12) as a `bg_event`, pillars at the Sanctum door.

---

## 9. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| Fossil Pokémon (one of four, level 50) | Fossil Scholar | Post-game (the whole city is) |
| Rare Candy, TM Dig | Sanctum (10,2), (11,2) | Four chambers solved |
| Relic Copper | Plateau (31,26) | None |
| Relic Silver, Relic Gold | Chamber 2 (7,7), Chamber 4 (1,7) | None |
| Relic Vase, Relic Band | Chapel (3,2), (5,2) | Dive |
| Relic Statue, Relic Crown | Underwater (33,10), (5,24), hidden | Dive |
| Star Piece, Nugget | Underwater (30,20) visible, (14,4) hidden | Dive |
| Max Revive | Old Town Hall chest (11,2) | Dive |
| PP Max | Drowned Hall chest (10,2) | Dive |
| Sea Incense | Stilt House A shelf (8,2) | None |
| Heart Scale x3 (hidden) | Quay (41,12), plateau (10,17), stilt walk (20,7) | None |

(The Maritime Museum in Kingsquay accepts a Relic Statue for a Shell Bell, see [kingsquay.md](kingsquay.md).)

---

## 10. Scripts and events the build needs

- `Aldermere_MapScripts` (plateau): `ON_TRANSITION` sets `FLAG_VISITED_ALDERMERE` and the heal location; hides the Guard and swaps the Sanctum door when `FLAG_ALDERMERE_SANCTUM_OPEN`; checks the four chamber flags.
- Chamber maps: four `coord_event`s on the plates each, with `VAR_TEMP_0` as the step counter; tablet `bg_event` text; the solved swap.
- Sanctum: Mew object script as in section 6.6; item balls.
- Fossil Scholar: the four-way gift menu.
- Harbour: Winston, the Diver and Old fisher talk scripts; the rematch Swimmer uses `cleartrainerflag` per fight ([vesperhaven.md](vesperhaven.md) rematch policy).
- Dive: Porymap Dive and Emerge connections between the Hole and `Underwater_Aldermere`.

**Flags (not claimed, from the card):** `FLAG_VISITED_ALDERMERE`, `FLAG_ALDERMERE_CHAMBER_1_SOLVED` to `_4_SOLVED`, `FLAG_ALDERMERE_SANCTUM_OPEN`, `FLAG_ALDERMERE_DIVE_STREETS_DONE` (optional), `FLAG_RECEIVED_ALDERMERE_FOSSIL`, `FLAG_RECEIVED_RARE_CANDY_ALDERMERE`, `FLAG_RECEIVED_TM_DIG_ALDERMERE`, hidden `FLAG_HIDDEN_ITEM_ALDERMERE_HEART_SCALE_1` to `_3`; new (PROPOSED): `FLAG_CAUGHT_MEW_ALDERMERE` (set only on a catch), `FLAG_ITEM_ALDERMERE_*` for the visible items, `FLAG_HIDDEN_ITEM_ALDERMERE_RELIC_STATUE`, `_RELIC_CROWN`, `_NUGGET`. **Vars:** none (temp vars only).

---

## 11. Build checklist (in order)

1. Read flags.md, engine-edits.md. Decide the Autumn Ruins import (a Porytiles conversion; CREDITS row; engine-edits note) and the Underwater pair import.
2. Create `Aldermere` (44 x 40) and trace the Alph render at x 9-34; set `MAPSEC_ALDERMERE`. Create `Aldermere_Harbour` (44 x 18) from a duplicate of `PacifidlogTown`; delete duplicated heal locations before saving.
3. Paint the plateau, put the sealed Sanctum door as a wall metatile with a pre-placed warp; add the steps and the connection to the harbour.
4. Harbour: the stilt walk, the five houses and tent, the quay, the Hole.
5. Build **one chamber**, test the plate order with `coord_event`s, then duplicate three times and re-paint plate glyphs.
6. Build the **Sanctum**, then duplicate it for the **Drowned Hall** and repaint the strips as water.
7. Build `Underwater_Aldermere`, the Town Hall lobby and the Chapel; set up Dive and Emerge connections.
8. Shared Center and Mart; the Fossil Scholar, stilt houses and hut.
9. Warps (section 7) and the R26 connection (harbour east edge x 43, y 9-12; water).
10. Close and reload Porymap after Claude edits events.
11. Claude wires scripts, trainers and dialogue; dialogue_check; `make -j4`; test the Mew re-offer by running from it.
12. Update design docs (flags.md, engine-edits.md), credits; no ROM or save staged; commit and push.

---

## 12. Open questions

1. **Two outdoor maps, not one.** The 15-object limit is the reason (plateau 7, harbour 9). OK? The alternative is one 44 x 56 map with fewer talkers.
2. **Which inside image goes where.** The card says Sanctum = `2bl`, Drowned Hall = `39cd`; the pictures say the opposite (`2bl` is the water version). I recommend swapping.
3. **The researchers' joke file.** The card's title for it names a real animal; I renamed it 'The Pink Problem' (it means MEW). Confirm. Cynthia's optional note stays.
4. **Autumn Ruins is triple-layer** (needs Porytiles). The fallback is vanilla caves and Slateport paving, much plainer. Worth a third tileset conversion?
5. **Winston twice** (Kingsquay house, Aldermere kiosk): a deliberate gag. Fine, or give Aldermere's kiosk to Trip?
6. **Chambers have wild encounters** (card says Glyph Chambers use the cave table): I made it optional via the tile attribute. Keep?
7. **R26 is the only way in**, and the harbour map holds the whole ferry arrival. If the author wants the quay reachable by Surf earlier, only the Dive-gated sunken half stays post-game (card question 1).
