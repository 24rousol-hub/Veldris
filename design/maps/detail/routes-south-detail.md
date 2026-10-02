# SOUTH ROADS R22 TO R31: detailed design

> **Open question (author, 2026-10-01): the Palladium and vanilla route renders named in this file are NOT decided.** Reusing route images may not give a quality hack, so every 'source render' for a road below is a mood and shape reference only until the author decides how each road is built.


Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md) ('Per road' list), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the road cards in [../routes-south.md](../routes-south.md) (species, levels, items and flags are theirs, kept as they are), the settlement files in this folder ([ebbsworth.md](ebbsworth.md), [kingsquay.md](kingsquay.md), [driftsands.md](driftsands.md), [beaconmouth.md](beaconmouth.md), [aldermere.md](aldermere.md), [vesperhaven.md](vesperhaven.md), [landmarks-south-detail.md](landmarks-south-detail.md)), and by rendering the vanilla route layouts named below with the tree's own tilesets and looking at the Palladium images `Route 33.png` (375 x 307, **22 x 18** tiles) and `Route 38.png` (681 x 477, **40 x 28**).

**New minor names and details introduced in this file are all PROPOSED:** the lamp-keeper, buoy keeper, signpost reader and other road NPCs, the sign texts, and every coordinate.

**Nothing here changes canon**: levels, species, trainer teams, items and flags are the card's. This file adds the shape of each map, where each thing stands, and what to build.

Conventions: coordinates are **(x, y) from each map's top-left (0,0)**, elevation 3 ground; `FACE_*` and **sight** (trainer sight range in tiles) are given for every trainer; all trainers reuse vanilla Hoenn ids, carry `IVs: 0` lines, and are Pokémon-only; trainer sight reaches only in the facing direction. **Every map keeps at most 15 live objects** (trainers, NPCs, item balls and strength boulders all count; I counted each road, see the 'Objects' line). Wild tables are in the card; here I only say where the grass or water they apply to goes.

---

## Findings that change the plan (read first)

I rendered the vanilla base maps and read them against the cards. Five real conflicts, none of which I have decided for the author:

1. **R22 on vanilla `Route122` has no 'long bridge'.** `Route122` (40 x 40) is a sea with **Mt Pyre as a mountain filling the middle** (x 4-33, y 7-31) and a small green landing pad at the south edge (x 18-21, y 37-39). The card says to use the bridge as Waymeet's dock and ignore Mt Pyre. I keep only the **ring of rocks and whirlpool rocks** that frames the map, fill the mountain with water and rebuild the interior as a switchback channel (R22 section).
2. **The card's weir contradicts its own geometry.** R22's south end enters Ebbsworth's north edge, but the card has 'the town beyond the top' of a cascade that is climbed northwards. A cascade cannot be the last thing before a town that lies to the south. My resolution: the weir is a **switchback inside R22** (down, a cascade up, down again) and the town is entered by a plain connection. If the author wants the weir inside Ebbsworth instead, say so.
3. **R23 on vanilla `Route109` has no land path.** It is a sea with a **beach spit in the north** (x 5-37, y 0-22, a house at x 10-14, y 2-5) and three **isolated sandbars** below it; the card's sand-and-pine path must be drawn by hand (R23 section).
4. **R26 and R29 on vanilla `Route134` and `Route126`.** `Route126` (80 x 80) has a **Sootopolis crater mountain** (x 27-60, y 33-60) in the middle that cannot be trimmed away by cropping columns; I delete it (or keep it as a plain reef). `Route134`'s water **currents** and shoals are good as they are.
5. **R30 and R31 edges.** The card gives edges that, read as map connections, put the cave and the camp on the wrong side. I keep the cards' *road logic* and choose connection types that work (R30: flip the render so the cave is at the south end; R31: a gate warp at Hollowbrook, a normal connection at the camp).

**Tilesets and imports in one place.** Every road's exterior uses `gTileset_General` (already the LeoB ORAS recolour) plus the vanilla secondary of its base, and the **LeoB ORAS recolour of that secondary** exists in the Team Aqua repo for all but Pacifidlog: `slateport` (R23), `lilycove` (R22, R25), `mossdeep` (R27, R29), `dewford` (R28), `fallarbor` (R31), `petalburg` (R24, R30: already imported for Hollowbrook). Same metatile ids as vanilla, so a trace of the vanilla map keeps working. **Each import needs a `CREDITS.md` row (leob0505) in the commit that first uses it, the matching `graphics/door_anims` file if a door shows, and a `design/engine-edits.md` entry** (it replaces vanilla tileset files in place). `Route134` (R26) uses vanilla `Pacifidlog`; the LeoB set has no Pacifidlog, so R26 stays vanilla. Import each secondary once, in the first commit that needs it (Slateport for Ebbsworth, Lilycove for Kingsquay and R22, Dewford for Driftsands and Beaconmouth).

## Overview table

| Road | Between | Kind | Base | Built size | Band | Objects |
|---|---|---|---|---|---|---|
| R22 | Waymeet, Ebbsworth | water, Waterfall weir | vanilla `Route122` | 40 x 40 | 52 to 55 | 13 |
| R23 | Ebbsworth, Kingsquay | water plus land path | vanilla `Route109` | 40 x 63 | 53 to 56 | 15 |
| R24 | Kingsquay, Driftsands | land | Palladium `Route 38` | 40 x 28 | 54 to 57 | 15 |
| R25 | Driftsands, Beaconmouth | land, two ponds | vanilla `Route121` trimmed | 64 x 20 | 56 to 58 | 15 |
| R26 | Beaconmouth, Aldermere | water, post-game | vanilla `Route134` | 80 x 40 | 62 to 68 | 11 |
| R27 | Vesperhaven, Wendlebury | water, post-game | vanilla `Route128` trimmed | 80 x 40 | 60 to 66 | 15 |
| R28 | Vesperhaven, Ebbsworth | water, post-game | vanilla `Route106` trimmed | 60 x 20 | 62 to 68 | 8 |
| R29 | Vesperhaven, Silverstrand | water, post-game | vanilla `Route126` trimmed | 48 x 80 | 64 to 70 | 14 |
| R30 | Vesperhaven, Echo Hollow | land, post-game | Palladium `Route 33` extended and flipped | 22 x 30 | 66 to 72 | 13 |
| R31 | Hollowbrook, Argent Peak | land, post-game | vanilla `Route115` trimmed | 40 x 70 | 68 to 74 | 15 |

Section ids `MAPSEC_VELDRIS_ROUTE_22` to `_31` (card). Palladium credit rule: a `CREDITS.md` row crediting the **Project Palladium team** with the file name in the first commit that traces `Route 33.png` or `Route 38.png`.

---

## R22: Waymeet to Ebbsworth (water, Waterfall weir)

**Description and walk-through.** The first sea road of the south, and its first lock. *Opening view from Waymeet:* the player leaves the south pier and slides into a brown tidal channel between two lines of rock, reed banks on the left and a pale sandbar with a lone fisher; across a wall of rock to the east, a thin white thread that is the weir. *Main path shape:* a **three-pass switchback**: south down a long channel, a turn into a broad foot pool, **north up a short cascade (Waterfall)** on the east side, across an upper basin, and **south again** down a second channel that doubles back **west along the bottom of the map** into Ebbsworth. *Set pieces and pacing:* the weir is visible from the first pass (a rock wall separates them), so the player knows what is coming and that Waterfall is the gate; the foot pool is the quiet pause before the climb; the upper basin has the barge pontoon (Scheme 9 seed); the last pass is the long, easy run in, with trainers thinning out.

**Base.** Vanilla `Route122` (`Route122_Layout`, 40 x 40, `General` + `Lilycove`): keep the **ring of rock and whirlpool-rock tiles** (about 30 rock tiles around the whole edge) as the map frame; **fill the Mt Pyre mountain** (x 4-33, y 7-31) with rock-and-water as the plan below needs; the green pad at the bottom edge becomes a reed bank. Copy the cascade pieces from vanilla Route 119 (the rock face with falling-water metatiles that Waterfall climbs). **The plan was checked with a small path program while writing:** with the cascade tiles blocked the player can reach the foot pool but not the upper basin or the exit; with them open the exit is reachable.

Sketch, **1 character = 2 x 2 tiles** (20 x 20 characters). `R` rock, `~` water, `F` waterfall tiles, `b` sandbar beach, `d` Waymeet dock stub, `i` rock islet, `p` pontoon, `s` foot-pool sandbar, `o` east sandbar.

```
x:  0    1    2    3    
y0  RRRRRRRRRR~~dRRRRRRR
y2  RRRRRRRRRR~~dRRRRRRR
y4  RRRRRRRbbb~~RRRRRRRR
y6  RRRRRRRbbb~~RRRRRRRR
y8  RRRRRRRbbb~~R~~~~~~R
y10 RRRRRRRRRR~~R~iii~~R
y12 RRRRRRRRRR~~R~iiippR
y14 RRRRRRRRRR~~R~~~~~~R
y16 RRRRRRRRRR~~R~~~~~~~
y18 RRRRRRRRRR~~RR~~R~~~
y20 RRRRRRRRRR~~RR~~R~~~
y22 RRRRRRRRRR~~RRFFR~~~
y24 RRRRRRRRRR~~RRFFoo~~
y26 RRRRRRRRRR~~RRFFoo~~
y28 RRRRRRRRRR~~RR~~R~~~
y30 RRRRRRRR~~~~~~~~~~~~
y32 RRRRRRRR~~~~ss~~~~~~
y34 RRRRRRRR~~~~ss~~~~~~
y36 RRRRRRRR~~~~~~~~~~~~
y38 RRRRRRRRRR~~~~~~~~~~
```
(Header digits mark every 10 tiles. The water is exact in the tables below; the rock between passes is solid.)

**Segments** (map x,y; water unless said):

1. **Waymeet pier and sandbar (y 0-8).** North edge water **x 20-23**, matching Waymeet's south pier at columns 20-23 ([waymeet.md](waymeet.md)): offset 0. A 2-tile dock stub (24,0)-(25,2) with the **Waymeet dock-gate guard** at (24,1). Sign 'EBBSWORTH: FOLLOW THE CHANNEL' at (24,3). **Sandbar beach** (14,4)-(19,8) west of the channel with the **fisher** (rumour about the Ebbsworth barge) at (17,6).
2. **First pass (x 20-23, y 0-30).** A 4-wide straight channel of 30 tiles between frame rock on the west and a rock wall (x 24-27) on the east. **Swimmer male** at (21,12). **Child watching the Wailord** at (18,14) on the west ridge. A west outcrop (17,20)-(19,23) with the **Fisherman** at (18,20) and the visible **Max Potion** at (18,24) on a lower rock. **Tuber female** drifting at (22,22).
3. **Foot pool (x 17-33, y 31-36).** The channel opens into a broad calm pool. A **sandbar** (24,33)-(27,35) with a visible **Revive** at (25,33), hidden **Pearl** at (24,35) and **Heart Scale** at (27,34). A rock at (30,32) holds the visible **Dive Ball** ('Dive Ball at the weir foot', card). Deep, calm water (a good place to cast a rod). A rock ridge along y 37 (x 17-34) separates the pool from the bottom lane.
4. **The cascade (x 29-30, y 21-27, with a 4-wide approach x 28-31).** From the pool's east end the water funnels north into a 2-wide, 5-tall **waterfall** (Waterfall tiles at x 29-30, y 22-26) between rock walls (x 28 and x 31, y 21-27); the channel is 4 wide again at the foot (y 28-30) and at the top (y 18-20). Sign 'LOCK BEYOND' at (27,28) on the rock; the **Swimmer female (at the weir)** at (29,28) faces up at the foot of the fall. Without Waterfall (badge 8) the player is stopped here: the **hard gate behind gym 8** (card). A line of whirlpool rocks (decoration) at (28..31,29).
5. **Upper basin (x 27-37, y 8-17).** A calm pool above the weir, with a **rock islet (29,10)-(32,13)** where the **Sailor** stands at (30,13), and a floating **pontoon (34,12)-(36,13)** with the **barge hand** at (35,12) ('Four hundred. Counted twice.').
6. **Second pass (x 35-38, y 17-37) and the bottom lane (y 38-39, x 20-38).** From the basin's south-east corner a 4-wide channel runs south with reed beds on both sides and an **east sandbar** (32,24)-(34,26) (scenery). **Swimmer female** at (36,28) faces up. At y 38 the channel turns **west along the bottom of the map** (2 tiles tall, a rock ridge on its north side) for 15 tiles and leaves by the south edge at **x 20-25**, Ebbsworth's river (offset 0).

**Connections.** North edge x 20-23, water, to `Waymeet` south edge (columns 20-23: offset 0, per Waymeet's file). South edge x 20-25, water, to `Ebbsworth` north edge (x 20-25: offset 0). No other exits.

**Trainers (6, levels per the card).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Swimmer male | Starmie 52, Seadra 52, Floatzel 53 | (21,12) | `FACE_DOWN` | 4 |
| Fisherman | Gyarados 52, Whiscash 53, Qwilfish 53 | (18,20) | `FACE_RIGHT` | 4 |
| Tuber female | Azumarill 52, Poliwrath 53 | (22,22) | `FACE_DOWN` | 2 |
| Swimmer female (at the weir) | Kingdra 54, Seaking 53, Milotic 54 | (29,28) | `FACE_UP` | 3 |
| Sailor | Pelipper 52, Tentacruel 53, Dewgong 53 | (30,13) | `FACE_DOWN` | 4 |
| Swimmer female | Mantine 52, Lanturn 53, Jellicent 53 | (36,28) | `FACE_UP` | 4 |

**NPCs (4):** Waymeet dock-gate guard (24,1) (the weir 'climbs, it does not carry'), fisher (17,6), child (18,14), barge hand (35,12). **Items:** visible Max Potion (18,24), Revive (25,33), Dive Ball (30,32); hidden Pearl (24,35), Heart Scale (27,34); post-game optional Big Pearl Dive spot (35,15 in the basin, optional underwater map). **Objects:** 6 + 4 + 3 = **13**.

**Water and fishing.** Surf slots (60/30/5/4/1 per the card) apply to every water tile; Old, Good and Super Rod everywhere there is water; good named fishing spots: the foot pool (20,33) and the second pass reeds (36,22). **Shore lines:** rock walls with the vanilla water-edge pieces along the three passes, reed beds (decoration) along the second pass and the bottom lane, sand where the three sandbars are. **Rocks and whirlpool rocks:** the frame ring (impassable swirl-and-rock tiles) round the whole edge, plus single rocks at (19,18), (22,28), (33,22) and (36,35). No grass on this road.

**Visual identity.** Tilesets `General` + `Lilycove` (LeoB `lilycove` when Kingsquay's import is done). Colours: brown-green tidal water, pale rock, reed yellow, a white thread of cascade. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE122` (vanilla's own Route 122 theme). Landmark silhouette: the weir on its rock wall, visible from the first pass.

**Goldsworth beat.** None (the barge is the seed). **Flags (not claimed):** `FLAG_R22_BARGE_HAND_SEEN`, `FLAG_ITEM_R22_MAX_POTION`, `_REVIVE`, `_DIVE_BALL`, `FLAG_HIDDEN_ITEM_R22_HEART_SCALE`, `_PEARL`. **Build effort:** medium (a water map with one hand-built weir). **Build order:** after Ebbsworth.

---

## R23: Ebbsworth to Kingsquay (water, with a land path)

**Description and walk-through.** The coast road. *Opening view from Ebbsworth:* by water, the lock gate opens onto a channel cut through a **sandy spit** crowded with parasols; by land, the East Gate drops the player onto the same spit's east half. *Main path shape:* the **land path** runs down the east side: the beach spit (parasols, pier), then a **pine-and-sand coast strip** about 8 tiles wide for 30 tiles, then a short jog west over a bottom island to Kingsquay's north gate; the **water path** is the open sea west of the strip, reached through the channel x 20-25. *Set pieces:* the beach with a pier (Fisherman and Sailor), the **rest house in the pines**, a clerk arguing with a barge hand over a manifest (Scheme 9 seed). *Pacing:* easy and sunny, two bands of trainers separated by the rest house.

**Base.** Vanilla `Route109` (`Route109_Layout`, 40 x 63, `General` + `Slateport`). It has: a **beach spit** in the north (x 5-37, y 0-22) with a house at x 10-14, y 2-5 and parasols and chairs, **isolated sandbars** at (24-33, 28-34) and (24-30, 42-47) and a small island at (14-22, 51-60), rock rings along both edges. **Not in the vanilla map (add by hand):** a continuous land path, pines, the channel through the spit.

**Segments** (map x,y):

1. **Channel and spit (y 0-22).** Carve a **water channel x 20-25** through the spit (north edge to y 22): water for Ebbsworth's lock gate. A **wooden footbridge** over it at (20..25, 10..12) joins the halves. The **West half** keeps the vanilla beach with parasols; the **East half (x 26-37)** is the beach the land path crosses. The East Gate warp arrives at **(31,3)**.
2. **Beach (x 26-37, y 2-20).** Parasol Lady at (28,10); a **picnicker** at (33,8); the **barge hand and clerk** arguing at (29,6) and (30,6) ('It says "permits (400)". It does not say whose.'); a **walker with a map** at (29,18). A **pier** (36,14)-(38,21) running into the sea: the **pier fisherman** (hint on Super Rod spots) at (36,12); **Sailor** at (37,16); **Fisherman** at the pier end (37,21).
3. **Pine strip, north (x 27-34, y 22-34).** Draw a 8-wide strip of pines with a 2-wide sandy path at x 30-31. **Bird Keeper** at (30,26); visible **Super Repel** at (31,24); hidden **Heart Scale** under a pine at (29,28); **Camper** at (31,31). The vanilla sandbar (24-33, 28-34) is absorbed into the strip.
4. **Rest stop (x 28-34, y 36-44).** The **rest house** (the Seashore House idea, `LAYOUT_HOUSE1`/`Route109_SeashoreHouse` 15 x 10 as the interior: a free drink, no healing) at (28,38)-(31,41), door (29,41); **Pokémon Ranger** at (32,41); a visible **Net Ball** on a stump at (34,36); visible **Max Ether** at (30,45); hidden **Star Piece** in the dunes at (33,44). The vanilla sandbar (24-30, 42-47) is absorbed.
5. **West sea lane (x 0-26, y 22-62).** The open water road: sandbar islets; **Swimmer male** at (12,32).
6. **South jog and bottom island (x 14-26, y 48-62).** The strip jogs west along the island to the south edge; the map ends at **land x 22-25** (Kingsquay's north gate) and **water x 0-8** (the bay).

**Connections.** North: water **x 20-25** to Ebbsworth's south edge (offset 0); the land path by **warp**: `Ebbsworth_EastGate` east door pair to R23 warp 0 at (31,3). South: **land x 22-25 and water x 0-8** to `Kingsquay` north edge (R23 is 40 wide, Kingsquay 64: offset 0, left aligned).

**Trainers (7).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Parasol Lady | Masquerain 53, Roserade 54 | (28,10) | `FACE_DOWN` | 3 |
| Sailor | Tentacruel 53, Pelipper 54, Cloyster 55 | (37,16) | `FACE_LEFT` | 3 |
| Fisherman | Seaking 53, Whiscash 54, Gyarados 54 | (37,21) | `FACE_UP` | 4 |
| Bird Keeper | Pelipper 53, Skarmory 54, Staraptor 54 | (30,26) | `FACE_DOWN` | 4 |
| Camper | Sandslash 53, Crawdaunt 54, Donphan 54 | (31,31) | `FACE_LEFT` | 3 |
| Pokémon Ranger | Heracross 54, Scizor 54, Wyrdeer 55 | (32,41) | `FACE_LEFT` | 3 |
| Swimmer male | Starmie 54, Kingdra 54 | (12,32) | `FACE_UP` | 4 |

**NPCs (5):** pier fisherman (36,12), barge hand (29,6), clerk (30,6), walker (29,18), picnicker (33,8). **Items:** visible Super Repel (31,24), Max Ether (30,45), Net Ball (34,36); hidden Pearl on the pier (37,19), Heart Scale (29,28), Star Piece (33,44). **Objects:** 7 + 5 + 3 = **15, the limit**. If anything is added, split the map at y 31 into R23 north and south.

**Grass.** 12-slot grass tables (card) apply to **tall-grass patches** along the pine strip: (28,24)-(29,27), (32,32)-(33,35), (29,42)-(31,43), (27,50)-(30,53). Surf and fishing as usual. **Water details.** *Surf patches:* the channel x 20-25 (y 0-22) and the whole west sea lane x 0-26, y 22-62 (the card's Surf table); the east side of the strip is also open sea (x 35-39). *Shore lines:* the spit's beach edge (wet-sand pieces), the strip's west edge (sand, then beach grass, then pines), the bottom island's rim. *Rocks and whirlpool rocks:* keep the vanilla rock ring along both edges (swirl-and-rock tiles, x 0-3 and x 36-39, every 4 to 6 tiles) and the larger rock stacks near (3,13), (4,29) and (7,36). *Fishing spots:* the pier end (37,22), the footbridge (22,11), the west sea lane at (14,40) and the bay at (4,60).

**Visual identity.** `General` + `Slateport` (LeoB when imported). Colours: sand, pine green, white parasol canopies, pier wood, sea blue. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE104` (what vanilla Route 109 uses). Silhouette: the pier and the line of pines.

**Goldsworth beat.** None; the argument at (29,6) continues the barge seed. **Flags (not claimed):** `FLAG_R23_BARGE_ARGUMENT_SEEN`, `FLAG_ITEM_R23_SUPER_REPEL`, `_MAX_ETHER`, `_NET_BALL`, `FLAG_HIDDEN_ITEM_R23_PEARL`, `_HEART_SCALE`, `_STAR_PIECE`. **Build effort:** medium. **Open:** the card asks whether a halfway Pokémon Center is wanted; the rest house is a drink, not a heal.

---

## R24: Kingsquay to Driftsands (land)

**Description and walk-through.** A fenced S-shaped lane through windbreak woods. *Opening view from Kingsquay:* the east gateway of the city, then a narrow sand lane between two hedges running west to east. *Main path shape (traced from `Route 38.png`):* from the west edge the lane runs a few tiles, **turns south down a hedged corridor**, **turns east along a flower-bed lane**, **rises** on the far side of a ledge and a grass pocket, then **runs east in a long straight lane to a timber gatehouse** at the east edge. A side loop climbs to a lookout. *Set pieces:* the grass pocket by the ledge, the lookout, the clerk with a broken hand-cart. *Pacing:* the first half is a maze of hedges with a trainer in each turn; the second half opens up and the sea air returns.

**Base.** Palladium `Route 38.png`: **681 x 477 px, gridded, 40 x 28 tiles**: a fenced lane (grey fence pieces along the top and bottom of the path), a sandy path, tall-grass patches, one brown ledge, signposts, trees all round, a gatehouse on the east edge (x 36-39, y 11-15). The picture is **green ground with a pale sandy path and a pine border**: the already-imported **LeoB General + Petalburg** look (Hollowbrook's) matches, so no new import. Credit Palladium in the first commit.

**Segments** (map x,y, from the picture):

1. **West gate lane (x 0-4, y 11-14).** The lane enters from the west edge at **y 12-13** (matching Kingsquay's lane; connection offset 10). A **gatekeeper-style old man** at (3,13) ('the road with sand in its shoes'). A signpost at (4,15): 'DRIFTSANDS: STRAIGHT ON'.
2. **Hedged corridor (x 1-4, y 14-24).** The lane drops south between a **hedge and the fence**. **Camper** at (3,18); **Picnicker** at (3,21).
3. **South flower-bed lane (x 4-24, y 22-25).** A broad lane with red flower beds. The **flower seller** at (9,23) (Pecha and Cheri berries); a **child chasing a Starly that keeps stealing his hat** at (14,24) (wanders); visible **Max Repel** at (12,22); visible **Rare Candy** under a tree in the flower bed at (23,23); hidden **Revive** at (7,25). The **lost clerk Pip with a hand-cart whose wheel has come off** (the card's optional Scheme 9 beat merged with Pip, one object) at (20,24), `FACE_RIGHT`, walking the wrong way.
4. **Grass pocket and ledge (x 10-20, y 8-18).** **Tall-grass patch** (the 12-slot table) at (6,8)-(13,10) and (16,10)-(30,12); a **ledge** (brown, jump-down) at (10,18)-(20,18); hidden **Heart Scale** at (19,13). **Bug Maniac** at (14,12).
5. **Lookout loop (x 24-30, y 6-12).** A sand loop to a lookout bench: **Collector** at (27,10); visible **PP Up** at (28,8); a tourist at (26,9).
6. **East lane and gatehouse (y 15-17, x 22-36).** The long straight lane; **Cooltrainer female** at (30,16) (`FACE_LEFT`, sight 5); **Bird Keeper** at (33,16); **Beauty** at (34,18) near the gate; hidden **Big Mushroom** at (32,19). The **gatehouse** (36,11)-(39,14), **door (37,14)**, leads to `Driftsands_WestGate`.

**Connections.** West edge x 0, y 12-13 to `Kingsquay` east edge (Kingsquay x 63, y 22-23): offset 10 (R24 shifted down 10). East end: a **door warp** at (37,14) to the `Driftsands_WestGate` west pair (1,5),(2,5) (no map connection). 

**Trainers (7).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Camper | Sandslash 54, Crustle 55, Golem 55 | (3,18) | `FACE_DOWN` | 4 |
| Picnicker | Kingler 55, Crabominable 55, Ludicolo 56 | (3,21) | `FACE_UP` | 3 |
| Bug Maniac | Heracross 55, Scizor 55, Kleavor 56 | (14,12) | `FACE_RIGHT` | 4 |
| Collector | Probopass 55, Magnezone 56, Bronzong 56 | (27,10) | `FACE_DOWN` | 3 |
| Cooltrainer female | Wyrdeer 56, Gallade 56, Roserade 56 | (30,16) | `FACE_LEFT` | 5 |
| Bird Keeper | Skarmory 56, Corviknight 56, Staraptor 56 | (33,16) | `FACE_LEFT` | 4 |
| Beauty | Lapras 55, Milotic 56, Gardevoir 56 | (34,18) | `FACE_LEFT` | 3 |

**NPCs (5):** old man (3,13), flower seller (9,23), child (14,24), tourist (26,9), Pip with the cart (20,24). **Items:** visible Max Repel (12,22), Rare Candy (23,23), PP Up (28,8); hidden Revive (7,25), Heart Scale (19,13), Big Mushroom (32,19). **Objects:** 7 + 5 + 3 = **15, the limit**.

**Visual identity.** `General` + `Petalburg` (LeoB, imported). Colours: green, pale sand lane, hedge green, red flower beds, grey fence, a timber gatehouse. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE120` (a Hoenn route track from the tree). Silhouette: the gatehouse at the end of a long straight lane.

**Goldsworth beat.** Optional: Pip's cart (the wheel). **Flags (not claimed):** `FLAG_ITEM_R24_RARE_CANDY`, `_MAX_REPEL`, `_PP_UP`, `FLAG_HIDDEN_ITEM_R24_REVIVE`, `_HEART_SCALE`, `_BIG_MUSHROOM`. **Build effort:** easy to medium. **Open:** the card's no-water question: the picture has none; fine.

---

## R25: Driftsands to Beaconmouth (land, two ponds, a stream)

**Description and walk-through.** A cliff road to the last gym. *Opening view from Driftsands:* the stone stair top, the sea a long way down on the right, a grassy shelf stretching east with a pond. *Main path shape:* a **rising diagonal**: it starts at the south-west corner, runs east along a grassy shelf past a pond, crosses a boulder shelf, passes a second pond, and climbs the last cliff to the north-east corner where it meets Beaconmouth's causeway. *Set pieces:* the **stuck hand-cart in the stream** (Scheme 9 beat), a **Strength boulder** guarding a Rare Candy at the east end, the Dragon Tamer just before the town. *Pacing:* two long shelves with trainers every 8 to 10 tiles; the last stretch is the toughest.

**Base.** Vanilla `Route121` (`Route121_Layout`, 80 x 20, `General` + `Lilycove`), trimmed to **64 x 20** (cut x 0-15). Vanilla has a grassy plain with fences and a Safari Zone entrance building (x 36-43, y 0-5, remove it). **Add by hand:** two ponds and a stream (the card).

**Segments** (map x,y; the road rises from (0..5,19) to (59..62,0)):

1. **Stair foot (x 0-10, y 12-19).** The SW corner: R25's bottom edge **x 0-5** meets Driftsands' north edge x 26-31 (offset 26). A cliff stair down at (2,16). A **Hiker** at (14,10) greets the player at the end of the shelf.
2. **West grass shelf (x 6-26, y 6-16).** The 12-slot grass tables apply to patches at (8,8)-(13,12) and (17,13)-(24,15). **Pond 1** (28,6)-(33,10) fed by a spring at (30,0). **Black Belt** at (22,14); **Hyper Potion** visible at (20,16); **Protein** visible at (25,5); hidden **Nugget** at (10,17).
3. **Stream and boulder shelf (x 28-44, y 4-14).** The stream leaves Pond 1 east along y 9 (x 34-44). **Hiker (second)** at (36,6); a ledge above the shelf (reached by a stair) with a visible **Max Revive** at (38,3); hidden **Star Piece** at (33,12).
4. **Pond 2 and the cliff shoulder (x 44-52, y 5-13).** **Pond 2** (45,7)-(50,12), the stream continues south-east. **Cooltrainer male** at (42,10) (Gallade 57, Skarmory 57, Aggron 58), **Cooltrainer female** at (48,5). Hidden **Max Ether** at (46,14). A **ranger** at (47,12) by the pond.
5. **The culvert and the cart (x 52-56, y 12-17).** The stream runs under the road at **(52..54, 14..15)** into the sea at the south edge x 53. The **clerk** stands at (55,14) with a **hand-cart** drawn as a decoration tile in the stream at (53,15) (not an object, to save a slot); the cart tips and the player sees a box stencilled 'PERMITS (400) TO THE LAST GYM'.
6. **The last climb (x 54-63, y 0-10).** A zigzag climb up the cliff. **Bird Keeper** at (56,10); **Dragon Tamer** at (60,4), the toughest on the road; **Rare Candy** at (61,3) behind a **Strength boulder** object at (61,4) (badge 4, the road's only boulder). The top edge **x 59-62** meets Beaconmouth's south edge (x 5-8) with offset -54.

**Connections.** South edge x 0-5 to `Driftsands` north edge (Driftsands x 26-31): in Driftsands' file `up`, offset 26. North edge x 59-62 to `Beaconmouth` south edge: in Beaconmouth's file `down`, offset -54. The lamplighter **hurries** along the road at (40,15) walking east (`WALK` pattern), the line 'The tower is dry in summer and wet in autumn'.

**Trainers (7).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Hiker | Golem 56, Steelix 57, Magcargo 56 | (14,10) | `FACE_RIGHT` | 4 |
| Black Belt | Hariyama 57, Machamp 57, Heracross 56 | (22,14) | `FACE_UP` | 4 |
| Hiker | Rhydon 57, Donphan 57, Probopass 57 | (36,6) | `FACE_DOWN` | 3 |
| Cooltrainer male | Gallade 57, Skarmory 57, Aggron 58 | (42,10) | `FACE_LEFT` | 4 |
| Cooltrainer female | Gabite 57, Dragonair 57, Weavile 57 | (48,5) | `FACE_DOWN` | 4 |
| Bird Keeper | Corviknight 57, Talonflame 57, Staraptor 57 | (56,10) | `FACE_LEFT` | 4 |
| Dragon Tamer | Gabite 57, Dragonair 57, Shelgon 58 | (60,4) | `FACE_DOWN` | 4 |

**NPCs (3 objects):** lamplighter (40,15), ranger (47,12), clerk (55,14). (The card's 'hiker with a view' is merged into the ranger's lines.) **Items:** visible Hyper Potion (20,16), Protein (25,5), Max Revive (38,3), Rare Candy (61,3); hidden Nugget (10,17), Star Piece (33,12), Max Ether (46,14). **Objects:** 7 + 3 + 4 + 1 boulder = **15, the limit**.

**Water and fishing.** Pond 1 and Pond 2: Surf (60/30/5/4/1) and rods per the card. **Visual identity.** `General` + `Lilycove` (LeoB when imported). Colours: grey cliff, grass shelf green, pond blue, stream silver. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE120`. Silhouette: the lighthouse appears in the last 10 tiles of the climb (decoration on the horizon at the top edge).

**Goldsworth beat.** The stuck cart (Scheme 9 seed, no battle). **Flags (not claimed):** `FLAG_R25_CART_SEEN`, `FLAG_ITEM_R25_MAX_REVIVE`, `_HYPER_POTION`, `_RARE_CANDY`, `_PROTEIN`, `FLAG_HIDDEN_ITEM_R25_NUGGET`, `_STAR_PIECE`, `_MAX_ETHER`. **Build effort:** medium. **Open:** hand-built ponds and stream (card). **Gate:** none (Waterfall is not needed here).

---

## R26: Beaconmouth to Aldermere (water, post-game)

**Description and walk-through.** A grey sea with a current. *Opening view from Beaconmouth:* the roped quay, the harbour mouth, grey water under a flat sky, a line of pale shoals leading away west. *Main path shape:* a **long west-running channel** with a field of **currents** in the middle that carry the player toward the ruins on the way out (and make the way back a slow grind, unless they hug the shoal edge); two **Dive spots** mid-route; a cliff face and stone quay at the west end. *Set pieces:* the **current field** (x 25-55), the **bobbing researcher** on a boat, the ruin cliff rising out of the fog. *Pacing:* a quiet start, a rush in the middle, a trainer cluster just before Aldermere.

**Base.** Vanilla `Route134` (`Route134_Layout`, 80 x 40, `General` + `Pacifidlog`, music `MUS_ROUTE119`). Rendered: rippled **current tiles** in broad bands (x 12-55, y 6-36), a sandy shoal island at (22-37, 22-33) with a small rock, a **sandbank** (x 44-65, y 12-18) with a strip of dry sand (x 43-60, y 15-16), a rock ring at the edges. Keep it; it is Hoenn's own route to a sealed ruin.

**Segments** (map x,y):

1. **Harbour approach (x 66-79, y 12-26).** The east edge: the **Beaconmouth west mouth** at **x 79, y 16-23** (Beaconmouth's x 0-4, y 31-38 mouth). Open grey water; **Swimmer male** at (63,22) just beyond. Visible **Max Revive** on a rock at (60,8).
2. **Shoal strait (x 44-66, y 8-24).** The sandbank (x 44-65, y 12-18). **Diver** by a **red buoy** (a `bg_event` and object) at (57,14); **Swimmer male (second)** at (51,14); **Old fisher** on the shoal at (44,18) telling you to stay off the current's edge.
3. **Current field (x 25-55, y 12-36).** Currents flow west. **Dive spot 1** at (50,28) (dark water); **Dive spot 2** at (38,12). **Swimmer female** at (46,26). A rock at (40,24) with the visible **Rare Candy** at (40,25) on the shoal.
4. **Shoal island (x 22-37, y 22-33).** Scenery: a small sandy island with one rock; **Swimmer female (second)** at (30,18).
5. **Ruin approach (x 0-22, y 0-26).** A cliff wall along the north (x 0-20, y 0-8) with a **bobbing researcher on a boat** at (22,14) (an `SS_TIDAL`-style or small boat object) talking about the Unown; **Fisherman** on a rock at (18,12); **Sailor** at (12,24) (four Pokémon, the toughest).
6. **West end (x 0-8, y 15-24).** The stone quay of Aldermere: the map's west edge **x 0, y 19-22** meets the harbour map's east edge (x 43, y 9-12): offset -10 (R26 y 19 = Harbour y 9).

**Connections.** East edge x 79, y 16-23 to `Beaconmouth` west edge (x 0, y 31-38): offset 15. West edge x 0, y 19-22 to `Aldermere_Harbour` east edge (x 43, y 9-12): offset -10. **Gate:** the quay rope on Beaconmouth's side until `FLAG_SYS_GAME_CLEAR`. Surf for the road, **Dive (badge 9)** for the underwater spots only.

**Underwater companion `Underwater_R26`.** Copy the pair pattern of `Route134`/`Underwater_Route134`: **check how Dive and Emerge place the player** (vanilla's underwater twin is only 18 x 10 while the route is 80 x 40, so confirm the mapping before positioning the two dive spots, and place the spots so the player lands inside the smaller map). Underwater items per the card: **Big Pearl, Pearl String, Relic Silver, Star Piece, Nugget** (visible and hidden spread over the underwater map). Dive encounter table per the card (levels 62 to 67). No tall grass on this road.

**Trainers (6).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Swimmer male | Starmie 63, Floatzel 64, Kingdra 64 | (63,22) | `FACE_LEFT` | 4 |
| Swimmer male | Wailord 64, Mantine 65 | (51,14) | `FACE_DOWN` | 4 |
| Swimmer female | Milotic 65, Jellicent 65, Lanturn 64 | (46,26) | `FACE_UP` | 4 |
| Swimmer female | Alomomola 64, Gastrodon 65, Walrein 65 | (30,18) | `FACE_RIGHT` | 4 |
| Fisherman | Gyarados 64, Whiscash 65, Sharpedo 65 | (18,12) | `FACE_DOWN` | 4 |
| Sailor | Pelipper 64, Tentacruel 65, Cloyster 65, Kingdra 66 | (12,24) | `FACE_RIGHT` | 4 |

**NPCs (3):** diver (57,14), old fisher (44,18), researcher on a boat (22,14). The 'ferry captain at Beaconmouth' lives on Beaconmouth's map ([beaconmouth.md](beaconmouth.md)). **Items:** visible Max Revive (60,8), Rare Candy (40,25). **Objects:** 6 + 3 + 2 = **11**.

**Water details.** *Surf patches:* the whole map except the shoals. *Currents:* the rippled current tiles of vanilla `Route134` (x 12-55, y 6-36) set to push west; the shoal edge along y 12-18 (x 44-65) has none, so the way back can follow it. *Shore lines:* pale shoal pieces round the sandbank (x 43-65, y 12-18), the island (x 22-37, y 22-33) and the Aldermere quay; the cliff face along the north-west (x 0-20, y 0-8) with water-edge pieces. *Rocks and whirlpool rocks:* the vanilla ring of swirl-and-rock tiles round the whole edge, plus single rocks at (40,24), (60,8) and (18,12). *Fishing spots:* the shoal island edge (30,24), the bank at (50,16), the quay (2,21) and the Dive spots' rims.

**Visual identity.** `General` + `Pacifidlog` (vanilla; no LeoB match). Colours: grey-blue, pale shoal sand, rock brown. Weather **`WEATHER_FOG_HORIZONTAL`** (a mist over the whole road leads into Aldermere's fogged plateau). Music `MUS_ROUTE119`. Silhouette: the ruin cliff in the mist at the west.

**Goldsworth beat.** None. **Flags (not claimed):** `FLAG_R26_OPEN` (with game clear), `FLAG_ITEM_R26_MAX_REVIVE`, `_RARE_CANDY`, `FLAG_HIDDEN_ITEM_R26_*` for the Dive items. **Build effort:** medium (a sea map plus its underwater twin). **Open:** the sketch's brown line beside R26 (a cliff path) is not built; water only.

---

## R27: Vesperhaven to Wendlebury (water, post-game)

**Description and walk-through.** The long open sea of the post-game. *Opening view from Vesperhaven:* the pontoon, a coast guard cutter at the strait (gone after the League), then open swells. *Main path shape:* an east-west road with **three rooms**: the swell (big, empty, a few rock arcs), a **ring lagoon** (a round shoal with a blue pool in the middle, the card's 'islets' as a set piece), and a narrow rocky gap before Wendlebury. *Pacing:* wide and easy; the lagoon is the reward.

**Base.** Vanilla `Route128` (`Route128_Layout`, 120 x 40, `General` + `Mossdeep`, music `MUS_ROUTE120`), trimmed to **80 x 40** (keep x 0-79). Rendered: rock arcs and shoals, a **ring island (x 25-35, y 14-24) enclosing a lagoon**, bands of currents. LeoB `mossdeep` is the recolour.

**Segments:** 1. **Vesperhaven end (x 66-79, y 14-24):** the cutter (`SS_TIDAL` object) at (72,19), hidden at game clear; **Sailor** at (66,19). 2. **The swell (x 40-66, y 8-32):** open water, rock arcs at the north (x 44-70, y 0-5); **Swimmer male** (58,22), **Swimmer female** (50,17), **Fisherman** (38,12). 3. **The lagoon (x 25-35, y 14-24):** **Tuber male** floats at (30,19); visible **Rare Candy** at (31,16) on the ring, **Max Elixir** (28,20), **Dive Ball** (34,23); optional Dive spot (a single Pearl String) at (30,21). 4. **The gap (x 10-24, y 26-36):** rocks and shoals; **Sailor (second)** at (14,30) (a Barraskewda and a Toxapex). 5. **Wendlebury end (x 0-9, y 14-26):** a pontoon with a **Wendlebury sailor** at (6,18) selling a rumour; a **fisher out of reach** on the rock arc at (45,6).

**Connections.** East edge x 79, y 18-21 to `Vesperhaven` west edge (x 0, y 28-30): offset 9 (R27's top at Vesperhaven y 9). West edge x 0 to `Wendlebury`'s **east edge**, which [wendlebury.md](wendlebury.md) keeps as open sea (its R8 is on the north edge and its barricade on the west; it leaves a sand tile at (31,12) walkable into the water for this road): offset set when Wendlebury is built. **Gate:** post-game, `FLAG_SYS_GAME_CLEAR` (the cutter leaves; shared with `FLAG_VESPERHAVEN_GATES_OPEN`). Surf only.

**Trainers (6).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Sailor | Pelipper 60, Tentacruel 61, Wailord 62 | (66,19) | `FACE_LEFT` | 4 |
| Swimmer male | Starmie 61, Floatzel 62, Kingdra 62 | (58,22) | `FACE_UP` | 4 |
| Swimmer female | Milotic 62, Mantine 62, Jellicent 63 | (50,17) | `FACE_DOWN` | 4 |
| Fisherman | Gyarados 61, Whiscash 62, Sharpedo 63 | (38,12) | `FACE_DOWN` | 4 |
| Tuber male | Politoed 61, Azumarill 62 | (30,19) | `FACE_LEFT` | 2 |
| Sailor | Cloyster 61, Barraskewda 62, Toxapex 62 | (14,30) | `FACE_UP` | 4 |

**NPCs (3):** cutter (72,19), Wendlebury sailor (6,18), fisher (45,6). **Items:** Rare Candy (31,16), Max Elixir (28,20), Dive Ball (34,23) (all visible). **Objects:** 6 + 3 + 3 = **12** (the optional underwater Pearl String is a hidden item, not an object). Wild tables per the card (no land).

**Water details.** *Surf patches:* everywhere outside the shoals and the lagoon; the lagoon itself is a separate calm surf patch (x 26-34, y 15-23) with its own fishing. *Shore lines:* pale shoal pieces round the ring island and the pontoons; the north rock arc (x 44-70, y 0-5) has water-edge pieces. *Rocks and whirlpool rocks:* arcs of swirl-and-rock tiles (vanilla) at the north (x 44-70, y 0-5), along the south (x 10-24, y 32-38) and around the ring island. *Fishing spots:* the lagoon (30,21), the swell (60,26), the gap (18,28).

**Visual identity.** `General` + `Mossdeep` (LeoB `mossdeep`). Colours: open blue, shoal sand, rock red-brown. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE120`. Silhouette: the ring lagoon. **Flags (not claimed):** `FLAG_R27_CUTTER_GONE` (or the shared gate flag), `FLAG_ITEM_R27_RARE_CANDY`, `_MAX_ELIXIR`, `_DIVE_BALL`. **Build effort:** easy to medium. **Open:** whether Vesperhaven opens before the League: the card's note says no.

---

## R28: Vesperhaven to Ebbsworth (water, post-game)

**Description and walk-through.** A short sheltered strait. *Opening view from Vesperhaven:* a pontoon, a cutter, then a channel of calm water with buoys on one side and a pale reef shelf with rocks on the other. *Main path shape:* a straight run with a **reef shelf** (the vanilla map's southern half is a sand shelf with rocks and a signboard) alongside; trainers anchor the buoys; an optional Dive spot under a reef rock. *Pacing:* quick, five encounters.

**Base.** Vanilla `Route106` (`Route106_Layout`, 80 x 20, `General` + `Dewford`, music `MUS_ROUTE104`), trimmed to **60 x 20**. Rendered: the **top half is open water with a rock and whirlpool-rock arc**, the **bottom half is a beach/shelf with a rock hill, a sign and pines** at x 20-60, y 10-19. Use the shelf as the **reef** (replace sand with shallows if wanted).

**Segments:** 1. **Vesperhaven end (x 0-10, y 1-8):** the cutter at (4,5) (hidden at game clear). 2. **Buoy channel (x 10-30, y 2-8):** a **buoy keeper** at (18,9) on a buoy (NPC); **Swimmer male** (22,5). 3. **Reef shelf (x 20-55, y 10-18):** a visible **Max Revive** on a reef rock (34,12); visible **Rare Candy** (46,14); optional Dive spot (Big Pearl) at (40,6); **Sailor** (36,6), **Fisherman** (48,7). 4. **Ebbsworth end (x 50-59, y 1-8):** **Swimmer female** (54,4); **Triathlete** at (57,6) (Poliwrath 64, Ludicolo 65, Swampert 66); a fisher with a story at (44,16).

**Connections.** West edge x 0, y 4-6 to `Vesperhaven` east edge (x 51, y 28-30): offset 24. East edge x 59, y 4-6 to `Ebbsworth` west edge (x 0, y 28-30): offset 24. **Gate:** post-game, `FLAG_SYS_GAME_CLEAR` (rope and cutter; Ebbsworth's Customs Officer). Surf.

**Trainers (5).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Swimmer male | Floatzel 63, Starmie 64, Kingdra 64 | (22,5) | `FACE_DOWN` | 4 |
| Sailor | Pelipper 64, Gastrodon 64, Dewgong 65 | (36,6) | `FACE_LEFT` | 4 |
| Fisherman | Qwilfish 63, Gyarados 65, Whiscash 64 | (48,7) | `FACE_UP` | 4 |
| Swimmer female | Lanturn 63, Alomomola 64, Milotic 64 | (54,4) | `FACE_LEFT` | 4 |
| Triathlete | Poliwrath 64, Ludicolo 65, Swampert 66 | (57,6) | `FACE_UP` | 3 |

**NPCs (3):** buoy keeper (18,9), cutter (4,5), fisher with a story (44,16). **Items:** visible Max Revive (34,12), Rare Candy (46,14). **Objects:** **10 at most** (5 + 3 + 2).

**Water details.** *Surf patches:* the channel y 0-9 (x 0-59) and the shallows over the reef (y 10-18, x 20-55). *Shore lines:* the reef shelf's edge (wet-sand pieces) along y 9-10, and a sand lip at each pontoon. *Rocks and whirlpool rocks:* the vanilla arc of swirl-and-rock tiles across the north (y 1-8) and the rock hill on the shelf. *Fishing spots:* the buoy channel (26,6), the reef edge (36,10), the Ebbsworth mouth (57,3).

**Visual identity.** `General` + `Dewford` (LeoB `dewford`, shared with Driftsands and Beaconmouth). Colours: light water, pale shelf, white buoys. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE104`. **Flags (not claimed):** `FLAG_R28_CUTTER_GONE` (or the shared flag), `FLAG_ITEM_R28_MAX_REVIVE`, `_RARE_CANDY`. **Build effort:** easy.

---

## R29: Vesperhaven to Silverstrand (water, post-game)

**Description and walk-through.** The hush. *Opening view from Vesperhaven:* a narrow strait with a lamp on a rock (a lamp-keeper beside it), then a wide quiet sea with islets. *Main path shape:* a **long north-south channel** in five rooms: the strait, islets, a reef with Dive Balls, a stretch of deep Dive water, and the approach to the beach. *Set pieces:* the lamp rock, the reef treasure, the Dive stretch.

**Base.** Vanilla `Route126` (`Route126_Layout`, 80 x 80, `General` + `Mossdeep`, music `MUS_ROUTE120`, with `Underwater_Route126` 80 x 80). Rendered: shoal ring islands, bands of currents, **a large white Sootopolis crater mountain in the middle (x 27-60, y 33-60)** and two big rock masses at the top corners. **Trimming to 48 columns does not remove the mountain**: either **delete it** (fill with water and a few reef rocks) or keep a small version as a decorative 'Silver Dome' reef with no entrance. I recommend deleting it. Crop the same 48 columns in the underwater twin.

**Segments** (map x,y; trimmed 48 x 80):

1. **Strait and lamp rock (y 0-12).** The top edge water **x 4-7** meets Vesperhaven's south-west strait (x 8-11, y 43): offset 4. A **lamp rock** with a decorative lantern at (20,6) and the **lamp-keeper** at (21,6); the cutter at (5,3) (hidden at game clear).
2. **Islets (y 12-34).** Scattered islets; **Swimmer male** (14,20), **Swimmer female** (28,28); visible **Max Revive** at (12,30).
3. **Reef (y 35-45).** A pale reef (x 28-36, y 36-42) with three visible **Dive Balls** at (30,38), (32,38), (31,40). **Sailor** at (20,44); the **fisher** ('where the sea keeps its sand') at (40,40).
4. **Deep stretch (y 46-62).** Dark water (the **Dive spots**) at (22,50) and (30,58); **Fisherman** at (36,52); visible **Rare Candy** (36,56); **Tuber female** at (22,60).
5. **Silverstrand approach (y 63-79).** Sandbars and shoals; **Cooltrainer male on a rock** at (34,70) (Milotic 68, Lanturn 66, Toxapex 67); the bottom edge water **x 22-25** meets `Silverstrand` north edge (x 20-23): offset -2.

**Connections.** Top edge x 4-7 to `Vesperhaven` south edge (x 8-11, y 43): offset 4. Bottom edge x 22-25 to `Silverstrand` north edge x 20-23 (offset -2). **Gate:** post-game, `FLAG_SYS_GAME_CLEAR` (cutter). Surf; **Dive (badge 9)** for the underwater spots. **Underwater companion `Underwater_R29`** (48 x 80, a crop of `Underwater_Route126`, same crop as the surface): items per the card: **Pearl String, Big Pearl, Relic Gold, Nugget**; Dive table per the card (levels 64 to 69).

**Trainers (6).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Swimmer male | Wailord 66, Starmie 66 | (14,20) | `FACE_DOWN` | 4 |
| Swimmer female | Lapras 67, Walrein 67, Dewgong 66 | (28,28) | `FACE_UP` | 4 |
| Sailor | Cloyster 66, Tentacruel 67, Kingdra 68 | (20,44) | `FACE_RIGHT` | 4 |
| Fisherman | Gyarados 67, Sharpedo 67, Barraskewda 66 | (36,52) | `FACE_LEFT` | 4 |
| Tuber female | Azumarill 66, Palafin 67 | (22,60) | `FACE_UP` | 2 |
| Cooltrainer male (on a rock) | Milotic 68, Lanturn 66, Toxapex 67 | (34,70) | `FACE_UP` | 4 |

**NPCs (3):** cutter (5,3), lamp-keeper (21,6), fisher (40,40). **Items (visible 5):** Max Revive (12,30), Rare Candy (36,56), Dive Ball x3 (30,38), (32,38), (31,40). **Objects:** 6 + 3 + 5 = **14**.

**Water details.** *Surf patches:* the whole map; dark-water Dive spots are marked on the surface by darker tiles at (22,50) and (30,58). *Shore lines:* pale shoals round every islet and the reef (x 28-36, y 36-42). *Rocks and whirlpool rocks:* the ring of swirl-and-rock tiles of vanilla `Route126`, kept at the edges, plus the lamp rock (20,6). *Fishing spots:* the reef edge (34,40), the deep stretch (24,52), the strait (6,10).

**Visual identity.** `General` + `Mossdeep` (LeoB `mossdeep`). Colours: deep blue, pale reef, white sand bars. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE120`. Silhouette: the lamp rock. **Flags (not claimed):** `FLAG_R29_CUTTER_GONE`, `FLAG_ITEM_R29_*`, `FLAG_HIDDEN_ITEM_R29_*`. **Build effort:** medium. **Open:** Dive spots here and on R26: keep both?

---

## R30: Vesperhaven to Echo Hollow (land, post-game)

**Description and walk-through.** A short cliff road to a cave. *Opening view from Vesperhaven:* the south-east service stair, a bare stone ridge, a feeling of being watched. *Main path shape (traced from `Route 33.png`, flipped):* a **stair down**, a bend, a small grass pocket, a signpost and a **ledge**, then the **cave door in the rock mass at the south end**. *Pacing:* a compact road with six trainers and the cave mouth guard.

**Base.** Palladium `Route 33.png` (375 x 307 px gridded, **22 x 18 tiles**): a hill with a rock cave door at the top (x 11, y 5), a signpost (x 11, y 7), a small ledge (x 8-14, y 9), a sandy path from the left edge (x 0-9, y 11-12), a grass pocket (x 9-12, y 13-14), a big rock formation on the right (x 14-21, y 6-16), trees all round. **Decision:** the card puts the cave at the north and Vesperhaven at the south, but Vesperhaven's stair is on its *south* edge, so the render must be **flipped top to bottom** (trace it bottom-up) with the cave door at the south end. The picture is extended by **12 rows at the Vesperhaven end** to reach 30 rows. LeoB `petalburg` (already imported) matches; the rocks are General.

**Segments** (map x,y after the flip and extension; the cave door ends at (11,24)):

1. **Stair foot and shelf (y 0-8).** The top edge **x 8-11** meets Vesperhaven's south edge x 44-47 (offset 36). A stair (the service stair) at (8..11, 0..3); a **signpost reader** at (10,6) ('R30: ECHO HOLLOW').
2. **Switchback (y 8-16).** Two hairpins down a bare hillside. **Hiker** at (9,10); **Black Belt** at (14,13); visible **Max Revive** at (6,11).
3. **Grass pocket (x 4-9, y 14-18).** The 12-slot table patch (the render's pocket, enlarged). A **hiker with a thermos** (NPC) at (7,16). **Psychic** at (12,16).
4. **Ledge and sign (y 18-22).** A one-way ledge (jump down south) at (6..13, 19); sign 'ECHO HOLLOW. SAY NOTHING YOU WOULD NOT HEAR AGAIN.' at (11,21); **Cooltrainer female** at (8,21); visible **Rare Candy** x2 at (3,20) and (18,20) (the right rock formation); hidden **Star Piece** at (16,18).
5. **Cave mouth (y 22-26).** The cave door at **(11,24)** in the rock mass; **Ruin Maniac** at (11,22) guarding it; the old woman who says the cave 'repeats you' at (13,22). Hidden **Max Elixir** at (5,24). The visible **Full Heal** lies at (15,10) on the shelf above the grass pocket.
6. **Right rock formation (x 14-21, y 6-16)** is decoration; one visible Rare Candy lies in its nook (18,20).

**Connections.** Top edge x 8-11 to `Vesperhaven` south edge x 44-47 (offset 36). The cave door (11,24) to `EchoHollow_1F` (see [landmarks-south-detail.md](landmarks-south-detail.md)). **Gate:** post-game, the service stair gate at Vesperhaven (`FLAG_VESPERHAVEN_GATES_OPEN`). No HM.

**Trainers (6).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Hiker | Golem 67, Steelix 68, Rhyperior 69 | (9,10) | `FACE_RIGHT` | 4 |
| Black Belt | Machamp 68, Hariyama 68, Heracross 69 | (14,13) | `FACE_LEFT` | 4 |
| Psychic | Alakazam 69, Gallade 69 | (12,16) | `FACE_DOWN` | 3 |
| Cooltrainer female | Weavile 70, Froslass 69, Mamoswine 70 | (8,21) | `FACE_RIGHT` | 4 |
| Ruin Maniac (cave mouth) | Sigilyph 69, Claydol 69, Golurk 70 | (11,22) | `FACE_DOWN` | 3 |
| Cooltrainer male | Dragonite 70, Hydreigon 70 | (16,12) | `FACE_LEFT` | 4 |

**NPCs (3):** signpost reader (10,6), hiker with a thermos (7,16), old woman (13,22). **Items:** visible Max Revive (6,11), Rare Candy x2 (3,20), (18,20), Full Heal (15,10); hidden Star Piece (16,18), Max Elixir (5,24). **Objects:** 6 + 3 + 4 = **13**.

**Visual identity.** `General` + `Petalburg` (LeoB) for the lower road and the rocks. Colours: bare grey-brown stone, a sliver of grass, the black mouth of the cave. Weather `WEATHER_SUNNY`. Music `MUS_ROUTE120`. Silhouette: the cave door in the rock face. **Flags (not claimed):** `FLAG_R30_OPEN`, `FLAG_ITEM_R30_*`, `FLAG_HIDDEN_ITEM_R30_*`. **Build effort:** easy to medium (a flipped, extended trace).

---

## R31: Hollowbrook to Argent Peak (land, post-game)

**Description and walk-through.** The mountain trail. *Opening view from Hollowbrook:* a ranger at a locked fence on the south-west edge of the village (open now), a trail that climbs out of green lowland with the sea on the left. *Main path shape:* a **long climb, south to north**, in six rooms: the Hollowbrook gate, the lowland plain, **tall-grass bends** between ledges, a **sea-cliff stretch** with the water on the left, a **rock face with optional nooks** (Cut, Strength, Rock Smash), and the camp gate at the top. *Set pieces:* the optional 'G + C' stones; the ranger; the view of the sea. *Pacing:* seven trainers spread over about 60 tiles, the toughest first meeting before the mountain.

**Base.** Vanilla `Route115` (`Route115_Layout`, 40 x 80, `General` + `Fallarbor`, music `MUS_ROUTE104`): rendered, the **west is sea** (x 0-8) with shoals, **pine forest** in the north-west (x 2-16, y 0-30), a **mountain of pale rock ledges** on the right (x 17-39, y 0-48) with several cave-mouth tiles (x 20, y 14), (x 14, y 18), a sand strip at x 8-14 (y 30-60), and a **green lowland** at the south with a pale sandy path (x 26-27, y 50-68) and flowers. Trim 80 rows to **70** by cutting the plain at y 52-61. LeoB `fallarbor` is the recolour.

**Segments** (map x,y after trimming):

1. **Hollowbrook gate (y 63-69).** The south end: a fence gate with the **ranger** at (24,65) ('It is closed in winter. It is also closed in summer. It is open now.'); the gate is a **warp pair** with a gate tile in Hollowbrook's south-west fence (Hollowbrook is already built; adding a warp event to the fence gap is an events edit, tell the author to close Porymap first). A flower bed at (22..28, 66..68).
2. **Lowland plain (y 52-63).** Pale path x 26-27; two ledges; **Black Belt** at (24,58); visible **Max Revive** at (30,60).
3. **Grass bends and ledges (y 36-52).** Tall-grass patches at (22,48)-(26,51), (28,40)-(32,43), (20,36)-(24,38) (the 12-slot table); ledges in between; **Hiker** (four Pokémon) at (26,46); **Cooltrainer female** at (30,42); **Psychic** at (22,38); **Expert** at (32,36); hidden **Star Piece** at (24,50). The **old woman who knew Gatsby** at (27,44) (a hint: he and a friend once climbed it).
4. **Sea-cliff stretch (y 22-36).** The trail hugs a cliff with sea on the left; **Pokémon Ranger** at (18,30); visible **Rare Candy** at (16,28); hidden **Nugget** at (14,26); an optional pile of old stones with 'G + C' scratched in one at (19,24) (`bg_event`, Gatsby and Cynthia, from postgame.md).
5. **Rock face and nooks (y 8-22).** A zigzag up the rock: a **Strength boulder** at (28,16) (optional nook with **PP Max** at (30,14)), a visible **Full Restore** at (24,12), hidden **Max Elixir** at (22,10); **Cooltrainer male** at (26,18) (Garchomp 73, Dragonite 73).
6. **Camp gate (y 0-8).** The top edge **x 24-27** meets `ArgentPeak_BaseCamp` south edge x 24-27 (offset 0): a ravine cut into the camp's rock wall (see landmarks-south-detail.md). A **sign** at (26,5) ('ARGENT PEAK BASE CAMP. NO DISHONOUR IN TURNING BACK.') closes the road; the camp's own trainers wait inside.

**Connections.** South: a **warp pair** to Hollowbrook's south-west fence gate (`FLAG_SYS_GAME_CLEAR`, `FLAG_R31_OPEN`). North: top edge x 24-27 to `ArgentPeak_BaseCamp` bottom edge x 24-27 (offset 0). **Gate:** post-game; earlier-badge HM nooks are optional.

**Trainers (7).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Black Belt | Machamp 71, Conkeldurr 72, Hariyama 71 | (24,58) | `FACE_RIGHT` | 4 |
| Hiker | Golem 70, Steelix 71, Rhyperior 72, Magcargo 71 | (26,46) | `FACE_LEFT` | 4 |
| Cooltrainer female | Mamoswine 72, Weavile 72, Glaceon 71 | (30,42) | `FACE_DOWN` | 4 |
| Psychic | Gardevoir 71, Alakazam 72, Gallade 72 | (22,38) | `FACE_RIGHT` | 3 |
| Expert | Tyranitar 73, Aggron 72, Lucario 73 | (32,36) | `FACE_LEFT` | 4 |
| Pokémon Ranger | Ursaluna 72, Wyrdeer 71, Scizor 72 | (18,30) | `FACE_RIGHT` | 4 |
| Cooltrainer male | Garchomp 73, Dragonite 73 | (26,18) | `FACE_DOWN` | 4 |

The road has exactly **seven trainers**, the card's list of classes.

**NPCs (3 objects):** ranger at the gate (24,65), old woman (27,44); the hiker with a flask (card) is merged with the Hiker's pre-fight line. (The card's child 'who has been told not to go' becomes a **sign** at the Hollowbrook gate.) **Items:** visible Max Revive (30,60), Rare Candy (16,28), Full Restore (24,12), PP Max (30,14); hidden Star Piece (24,50), Nugget (14,26), Max Elixir (22,10). **Objects:** 7 + 2 + 4 + 1 boulder = **14**. Add the optional Cut tree only by dropping one NPC (limit 15).

**Visual identity.** `General` + `Fallarbor` (LeoB `fallarbor`). Colours: lowland green, pale rock, sea on the left, thin snow dusting toward the top. Weather `WEATHER_SUNNY` (weather is per map; `WEATHER_SNOW` is marked Unused in `include/constants/weather.h`, so test before using it on the camp or this road). Music `MUS_ROUTE104`. Silhouette: the white peak on the horizon from the first step. **Flags (not claimed):** `FLAG_R31_OPEN` (or reuse `FLAG_ARGENT_PEAK_OPEN`), `FLAG_ITEM_R31_*`, `FLAG_HIDDEN_ITEM_R31_*`. **Build effort:** medium (a long trimmed trace). **Open:** the card asks if a 70-tile climb is too long; I kept it.

---

## Open questions (roads)

1. **R22's switchback instead of the card's 'town beyond the top'.** Confirm, or move the weir into Ebbsworth.
2. **R23's land path is hand-drawn** (vanilla has none). Is a big hand-drawn pine strip acceptable?
3. **R25, R24 and R23 sit exactly at the 15-object limit.** Anything added forces a split.
4. **R30 is traced flipped** and **R31's Hollowbrook end is a warp**. OK?
5. **R26's current field:** do you want the currents to push the player (vanilla behaviour) or to be decoration only?
6. **R27's Wendlebury connection.** Wendlebury's detail file keeps its east edge as sea; R27 attaches there, near the sand tile at (31,12) it leaves for it. Confirm the offset when Wendlebury is traced.
7. **'Bird Keeper' class name.** Used by R23, R24, R25 (vanilla trainer class, the cards use it). It contains a real animal word; the east-roads file raises the same question ([routes-east-detail.md](routes-east-detail.md) open question 3). Keep or rename the class.
8. **Underwater twins** (R26, R29, Aldermere, Beaconmouth, Vesperhaven): each is a map pair with Dive and Emerge connections; how the vanilla pair maps the player's position needs a check in Porymap before the spots are placed.
