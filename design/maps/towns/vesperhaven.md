# VESPERHAVEN (city, post-game only, the hidden coast; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); the sketch's author note reads 'Only unlocks post game'. Template and rules: [../README.md](../README.md). Roads: R21 (centre group), R27 to R30 in [../routes-south.md](../routes-south.md). Post-game content comes from [../../postgame.md](../../postgame.md); Gatsby and the letters from [../../goldsworth.md](../../goldsworth.md); built teams in [../../trainer-roster.md](../../trainer-roster.md).

## Role in the story

- **The post-game hub.** Everything the player does after the Hall of Fame can be reached from here: the rematches, Cynthia's visit, the Troglodyte and Gatsby epilogue hooks, and the roads to Silverstrand, Echo Hollow and (by Fly) Argent Peak.
- **Why it is hidden.** The League keeps it off the signposts. Gatsby and Cynthia know it; the League's retired and off-duty staff holiday here. Before the League the four sea and land approaches are shut: a **coast guard cutter** (an NPC boat on a water tile) blocks the three straits (R27 west, R28 east, R29 south-west) and the north stair is a locked League service gate. After `FLAG_SYS_GAME_CLEAR` the cutters leave and the gate opens. The player's **first arrival is by R21**, the post-league road from the Pinnacle, as in the README's table. Later arrivals are by Fly, by the sea roads or by R30.
- **What the post-game gives here (from postgame.md, all PROPOSED):**
  1. **Rematches:** every gym leader, the Elite Four and Cynthia, at higher levels, in the League Lounge (table below).
  2. **Cynthia's visit:** she keeps a cottage here. Tea, a short story, her rematch, a letter to carry to Gatsby.
  3. **Gatsby epilogue hooks:** the thick envelopes on good paper (Mrs Pell's line), the faded photo with the trophy, the worn book on battling in another region, the locked drawer in Hollowbrook.
  4. **Troglodyte's job:** he works the Lounge cloakroom (sullen but trying, matches Arc A and `PostGame_Text_TrogEpilogue`). His rematch is not here; he trains at Argent Peak (see [landmarks-south.md](../landmarks-south.md)).
- No gym, no scheme, no Goldsworth house (post-game only; the family epilogue happens in the Gildhaven tower).

## Where it sits

South-centre on the sketch, between the Pinnacle (north) and the south coast. The only city that can be entered from four sides.

| Road | Edge of Vesperhaven | How |
|---|---|---|
| R21 from The Pinnacle | **North edge** | A long stone stair down the crater wall. The first arrival |
| R27 to Wendlebury (post-game) | **West edge** (water) | A sea gate with a pontoon |
| R28 to Ebbsworth (post-game) | **East edge** (water) | A sea gate with a pontoon |
| R29 to Silverstrand (post-game) | **South-west edge** (water) | A narrow strait with a lighthouse lamp (decoration) |
| R30 to Echo Hollow (post-game) | **South-east edge** (land) | A road down a cliff stair |

## Source and size

- **Vanilla base: Sootopolis City** (`SootopolisCity_Layout`, 60 x 60): a hidden crater city with a pool in the middle and houses on ledges, exactly 'hidden coast'. Trim to **about 52 x 44**: `(52 + 15) * (44 + 14) = 3886`, inside 10240.
- **Palladium:** none for the town (the names list says none). For the interiors:
  - `halloffamegscrevampzr1.png` (160 x 263 px, about 10 x 16): the **Hall of Past Champions** annex;
  - `Elm's House.png` (13 x 10): **Cynthia's Cottage**;
  - `championlacetq2.png` (240 x 512, about 15 x 32): a grand-hall look for the **League Lounge**, as a reference only.
  - Vanilla: `LilycoveCity_ContestLobby` (31 x 12) is a long hall for the Lounge.
- **Section id:** `MAPSEC_VESPERHAVEN` (name `VESPERHAVEN`, 11 chars).
- **Fly and heal:** a fly destination after the first arrival (Feather Badge). One row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_VESPERHAVEN`.

## Layout

In plain words:

- **The crater rim (top).** The R21 stair comes down from the north edge into a **north terrace** with a fountain. The Pokémon Center is on the terrace's west side, the Mart on its east.
- **The Lounge (middle left).** The League Lounge is a long stone building facing the pool. Its big door is on the south face, 5 tiles from the left corner.
- **The Pool (centre).** A big shallow pool, surf-able, with a ring path round it. A fountain statue of an old Champion stands in the middle. The harbours (west, east, south-west) feed into it by narrow channels.
- **Cynthia's Cottage (middle right).** A small cottage on a ledge, a garden of red flowers, a bench. Door faces west.
- **Boathouse (south edge).** A single-room boathouse with a bench, a kettle and a rowing boat. The post-game tea scene with Gatsby (optional, see Open questions).
- **South-east stair.** The R30 road leaves from the south-east corner by a cliff stair.
- **Hall of Past Champions (north-west).** A small museum building, one floor.
- **West, east and south-west sea gates.** Pontoons, a rope each until the League.

No tall grass (no wild encounters in town).

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared |
| Mart | `LAYOUT_MART` | Post-game stock: Max Revive, Full Restore, Max Potion, Ultra Ball, Max Repel, PP Up |
| League Lounge 1F | custom, base `LilycoveCity_ContestLobby` (31 x 12) | Elite Four rematches, the cloakroom, a bartender |
| League Lounge 2F (the Terrace) | custom, 31 x 12, a copy | The nine gym leaders, each at a table |
| Cynthia's Cottage | custom, `Elm's House.png` (13 x 10) | Cynthia, tea, her rematch, the letters |
| Boathouse | `LAYOUT_HOUSE1` | The bench, the kettle, optional Gatsby |
| Hall of Past Champions | custom, `halloffamegscrevampzr1.png` (about 10 x 16) | Portraits of past Champions; Cynthia's is the newest |
| Two ordinary houses | `LAYOUT_HOUSE1`, `_HOUSE2` | Staff families |

About nine maps. The Lounge is split in two so each stays under the 15-object limit.

## Rematch table (PROPOSED)

All via `cleartrainerflag` per fight (postgame.md), same species as the original teams in [../../trainer-roster.md](../../trainer-roster.md) plus one more Pokémon, no IVs, no EVs, ids reuse vanilla entries. Levels are the new **ace** level.

| Where | Who | Original ace | Rematch ace |
|---|---|---|---|
| Terrace | GRETA | 12 | 70 |
| Terrace | HACHIMEL | 19 | 71 |
| Terrace | SANZUFORD | 25 | 72 |
| Terrace | HAGANE | 31 | 73 |
| Terrace | WAKASAGI | 37 | 74 |
| Terrace | TOBIN | 42 | 75 |
| Terrace | ASEBY | 48 | 76 |
| Terrace | SUZURAN | 55 | 77 |
| Terrace | MIZZLE | 60 | 78 |
| Lounge 1F | OSSIAN | 66 | 80 |
| Lounge 1F | HYACINTH | 68 | 81 |
| Lounge 1F | DUNMORE | 70 | 82 |
| Lounge 1F | DRAYDEN | 71 | 83 |
| Cottage | CYNTHIA | 75 | 85 |

First win each pays a small gift (Rare Candy for a leader, PP Max for an Elite Four member, an Ability Capsule for Cynthia). Troglodyte's rematch is at Argent Peak.

## NPCs

12 to 20 for a city. Each Lounge floor holds at most 15 objects.

| Role | Where | Topic |
|---|---|---|
| Nine gym leaders | Lounge 2F, one table each | Deadpan holiday talk; rematch on request |
| Four Elite Four members | Lounge 1F | OSSIAN in a black armchair, HYACINTH reading, DUNMORE asleep (wake him), DRAYDEN with tea |
| Cynthia | Cottage | Dry, warm, sharp. Tea, a story, her rematch, a letter. Mentions the old friend who writes |
| Troglodyte | Lounge 1F cloakroom | Sullen, trying. Takes the player's coat, a sincere 'sir' that is clearly painful |
| Bartender | Lounge 1F | Pours for staff only. 'Nobody told you about this place.' |
| League clerk | Lounge 1F | Explains the rematch rules |
| Hall attendant | Hall of Past Champions | Names the Champions in order; the last portrait is unfinished (Veldris is seatless, Cynthia is the guest) |
| Coast guard cutter (pre-game) | Each sea gate | 'League business. Come back when you have finished.' Removed at game clear |
| Dockhand | West and east gates | Ferry times: the Kingsquay ferry reaches here post-game |
| Retired nurse | Pokémon Center | Remembers the Hoenn League; ordinary |
| Fisher | North terrace | 'We have the sea to ourselves.' Hint on Silverstrand |
| Kid | Pool path | Wants to know what Fly is |
| Gatsby (optional, post-reunion) | Boathouse bench | Kettle, a berry or a TM, thanks. See Open questions |
| Boatman | Boathouse | Rows the player to the R29 strait at night. Optional |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| Rematch gifts | Terrace, Lounge, Cottage | First win each |
| Letter for Gatsby | Cottage | Cynthia, after tea |
| Max Elixir | Behind the Lounge (hidden) | None |
| Rare Candy x2 | Hall of Past Champions (visible) | After the League |
| Pearl, Big Pearl | The Pool bottom (Dive spots) | Dive |
| Sea Incense | Cottage shelf | After tea |
| Ability Capsule | Cynthia rematch | Win |
| A berry and a TM (Hyper Beam, PROPOSED) | Boathouse kettle (Gatsby) | After the letter errand |

The kettle TM, rematch gifts and Mart stock are placeholders. Check the TM ledger for duplicates.

## Flags (not claimed)

- `FLAG_VISITED_VESPERHAVEN`.
- `FLAG_VESPERHAVEN_GATES_OPEN` (set at game clear: hides the cutters, opens the service gate).
- `FLAG_REMATCH_GRETA` to `FLAG_REMATCH_MIZZLE` (nine), `FLAG_REMATCH_OSSIAN` to `_DRAYDEN` (four), `FLAG_REMATCH_CYNTHIA`. These are the new defeat markers; the reused trainer ids carry the real trainer flags, which are cleared before each rematch.
- `FLAG_VESPERHAVEN_TEA_DONE` (Cynthia's tea scene played).
- `FLAG_VESPERHAVEN_LETTER_TAKEN`, `FLAG_VESPERHAVEN_LETTER_DELIVERED` (the errand).
- `FLAG_VESPERHAVEN_TROG_HIRED` (Troglodyte working at the Lounge, set at game clear).
- `FLAG_RECEIVED_ABILITY_CAPSULE_CYNTHIA`.
- Hidden items: `FLAG_HIDDEN_ITEM_VESPERHAVEN_MAX_ELIXIR`.

## Build order and effort

**Hard.** A large, unusual crater city; two long Lounge floors, a cottage and a museum. The cutters are ordinary objects with a hide flag, and the rematch table is data. **Build last** of the south group, after the Pinnacle and R21 exist.

## Open questions

1. **Where does Cynthia's tea and rematch happen: here (my pick) or in Hollowbrook** (postgame.md says 'Cynthia in Hollowbrook', also 'her house or a League lounge')? Both can happen: the reunion is at Hollowbrook, the rematch here.
2. Is the Vesperhaven approach by R21 only at first (my reading of 'only unlocks post game') or can the water roads open before the League?
3. Troglodyte's job as a cloakroom attendant is mine, from the post-game 'he has a job' line. Does it suit Arc A?
4. Do the rematch teams use new blocks (more work) or rewrite the old Hoenn rematch blocks (Roxanne 2 to 5 and so on)? The roster file says they hold old Hoenn teams and are never reached, but Greta, DALE and WREN already took some.
5. A second Gatsby location (the Boathouse) duplicates the kettle plan in Hollowbrook. Keep or cut?
