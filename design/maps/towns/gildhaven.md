# GILDHAVEN (city, place 8, gym 6 Flying, the skyscraper city)

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../../region-sketch.md](../../region-sketch.md)), the approved names ([../../region-names.md](../../region-names.md)) and [../README.md](../README.md). Nothing here is built. Related: [../../gyms.md](../../gyms.md), [../../trainer-roster.md](../../trainer-roster.md), [../../troglodyte-arc.md](../../troglodyte-arc.md) (Scheme 6, fight 5), [../../goldsworth.md](../../goldsworth.md) (the parents, the tower), [../routes-centre.md](../routes-centre.md) (R18, R19, R20), [../landmarks-centre.md](../landmarks-centre.md) (The Pinnacle). New minor names are marked PROPOSED.

## Role in the story

- **Gym 6, Flying.** Leader **TOBIN** (`TRAINER_TOBIN`, Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42). Gives the **FEATHER BADGE**, **HM Fly** and **TM Aerial Ace**. In this build Fly needs the Feather Badge, so Gildhaven is where fast travel starts.
- **The Goldsworth skyscraper city.** The tower is the family seat: Troglodyte's parents (Mr. Goldsworth III and Mrs. Goldsworth) live and work in it. **There is no separate Goldsworth house here** ([../../gyms.md](../../gyms.md), [../../goldsworth.md](../../goldsworth.md)). The cousin set goes to Briarwick instead.
- **Scheme 6:** the parents arrive at the gym with a gift basket to buy the badge for their son. Tobin explains kindly, twice. They tip him and leave confused. **Troglodyte fight 5** (his 'Crack' fight) happens with his parents watching.
- **The hub.** Gildhaven is the middle of the map: R18 from Hoarfell (north), R19 water road from Waymeet (east), R20 to The Pinnacle (south, nine badges). Fly arrives here.
- Tone: glossier and richer than the villages, still deadpan. Gold paint, a lot of glass, signs that sell things. Nothing is quite as good as it looks.

## Where it sits

In the middle of the sketch, west of Waymeet and south of Hoarfell (red circle labelled 'Central City w/ skyscraper'). Roads, by edge:

| Edge | Road | Notes |
|---|---|---|
| North, centre | **R18** from Hoarfell (thin line in the sketch) | through a grey gatehouse, the render's north gate. Private toll road: see the R18 card |
| East | **R19** water road from Waymeet (sketch 32) | harbour and quay on the east shore. The only edge that needs Surf |
| South, centre | **R20** to The Pinnacle (sketch 33) | through the **Pinnacle Gate**, a gatehouse that checks for all 9 badges |
| West | none | sea and sheer rock, scenery only |

Fly lands outside the Pokémon Center (heal location, PROPOSED `HEAL_LOCATION_GILDHAVEN`).

## Source and size

- **Main source:** Palladium `goldenrodcitytiled.png` (Goldenrod City, 1005 x 868 px, no grid, **62 x 54 tiles**). Alternative with a rail line and a bigger harbour: `goldenrodrodcity.png` (916 x 988 px, **57 x 61 tiles**). Size check: `(62+15)*(54+14) = 5236` (and 5400 for the alternative), both under 10240. Plan **about 60 x 50** after trimming the fringe of houses.
- **Mirror it.** The render has the sea on its **west**. Gildhaven's water road leaves on the **east**. Trace the render flipped left to right (it is only a picture to copy by eye), so the tower, the harbour and the cliffs swap sides. The description below uses the **flipped** orientation.
- **Skyscraper exterior** is the hard part (CLAUDE.md and [../../map-plan.md](../../map-plan.md) note that Emerald tilesets have no tall tower). Options, cheapest first: (1) the render's Radio Tower (about 5 to 7 wide, 15 tall) redrawn as new tiles, the author's call; (2) Palladium `Battle Tower.png` (24 x 26, a glass cylinder on a plaza) as a more glossy look, also new tiles; (3) a very large Devon Corp style block in an existing tileset, which reads as a big office, not a skyscraper. **Not decided.**
- **Vanilla base:** `MauvilleCity` (40 x 20) or `LilycoveCity` (80 x 40) for tilesets and the harbour. Tileset suggestion: `gTileset_General` plus `gTileset_Lilycove` (harbour, shop fronts). Sections: `MAPSEC_GILDHAVEN` (new, PROPOSED; one of the 37 free ids, [../../region-sketch.md](../../region-sketch.md)). All interiors use the same section.
- **Credit:** Project Palladium team, in the same commit as the first traced map ([../../map-plan.md](../../map-plan.md)). Interiors: Palladium `Goldenrod Dept Store 1F.png`, `President's Office Tiled.PNG`, `Violet City Gym.png`.

## Layout

Rough districts (flipped orientation, north at the top, not to scale):

```
                 [North Gate: R18]
        gym forecourt     |      garden, flower beds
        [GYM]             |
                          |     (Goldsworth Plaza)
   ------- cross street (fenced) --------------------[TOWER]--
                    avenue|                          harbour
   [Hotel]   [Pokemon Ctr]|[Emporium]      quay >>>>>> R19 (east, Surf)
   houses            avenue                  houses, pavilion
                          |
                 [Pinnacle Gate: R20]
```

- **North Gate and Causeway Plaza.** R18 arrives through a grey gatehouse at the top centre, onto a wide plaza with a fountain (hidden item) and four fenced lawns.
- **The Avenue.** A paved promenade runs the full height of the town, north gate to south gate. Everything important is on it or one street off it.
- **Gym forecourt (north-west).** A fenced forecourt about 6 x 4 tiles in front of the gym's single door, which faces south. A bench, a windsock-style banner (an object), a flower bed. **Scheme 6 happens here.** The giant gift basket (object) blocks the door until the scene is done.
- **Goldsworth Plaza and the Tower (east).** The tower stands on the harbour front, its lobby door at the foot of broad steps facing west onto a paved plaza with a statue plinth (the statue is of nobody yet: a deadpan joke). The two satellite-dish props from the render sit on the roof.
- **Harbour and quay (east edge).** A stone quay with bollards and a pier. Surf starts from the end of the pier: R19 begins in open water. A rock islet just off the quay (Surf only) holds a Star Piece.
- **Market quarter (centre-south).** The Emporium (department store) and the Pokémon Center face each other across the avenue. The Hotel sits one block south-west. A glass-roofed pavilion (render's bike shop) is dressed as a shop with its shutters down.
- **Residential quarter (south-west and south-east).** Streets of small, richly painted houses. Five enterable buildings, the rest are scenery doors that do nothing.
- **Pinnacle Gate (bottom centre).** A gatehouse across the avenue's south end. R20 begins beyond it.
- **Cliffs.** The west and east fringes are rock walls and ledges (one Cut tree, one Rock Smash rock, one Strength boulder, see Items).

Door positions in words: Pokémon Center door faces north onto the avenue, just south of the cross street, west side. Emporium door faces west onto the avenue, opposite it. Hotel door faces east onto a side street, one block south of the Center. Gym door faces south onto its forecourt. Tower lobby door faces west onto Goldsworth Plaza. North Gate and Pinnacle Gate are doorways on the avenue (two warps each).

## Buildings

Interiors reuse vanilla layouts where possible (README). Max 15 live objects per map. Counting the maps: about 27 for a lean build.

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared, no painting. Heal location outside |
| Gildhaven Emporium 1F to 5F and Roof | base Palladium `Goldenrod Dept Store 1F.png` (six floor panels each about 19 x 14, plus a roof). Cheapest: vanilla `LilycoveCity_DepartmentStore_1F` to `_5F` (18 x 8), `_Rooftop` (18 x 12), elevator `LilycoveCity_DepartmentStoreElevator` (5 x 6) | The Mart. 1F services, 2F Medicine, 3F Tools, 4F TMs, 5F Vitamins and gifts, Roof vending machines (Fresh Water, Soda Pop, Lemonade). Vanilla elevator script is tied to a fixed five-floor list: if the floors change, check the script. Six floors is optional, five is enough |
| Gym | custom, base Palladium `Violet City Gym.png` (208 x 288 px, **13 x 18**) | See Gym |
| **Goldsworth Tower** | see 'The tower' below | 6 maps lean, 10 full. No trainers |
| Hotel 1F, 2F ('Gildhaven Grand') | vanilla `LilycoveCity_CoveLilyMotel_1F`, `_2F` | Lobby and rooms. Free rest for the player is a joke ('compliments of the house', which it is not) |
| Pilots' Club | vanilla `LilycoveCity_PokemonTrainerFanClub` (12 x 14) | Tobin's flying friends. Chat and a hint about R20 |
| House A (retired navigator) | `LAYOUT_HOUSE1` | Ordinary resident |
| House B (window cleaner's flat) | `LAYOUT_HOUSE2` | Ordinary resident |
| Move Deleter's house | vanilla `LilycoveCity_MoveDeletersHouse` | Optional service, one NPC |
| North Gate, Pinnacle Gate | small gatehouse, one room each (about 8 x 5) | Warp pair plus guard. The Pinnacle Gate holds the badge check |

Map names follow [../../towns-and-routes.md](../../towns-and-routes.md): `Gildhaven`, `Gildhaven_Gym`, `Gildhaven_PokemonCenter_1F`, `Gildhaven_Emporium_1F`, `Gildhaven_GoldsworthTower_1F`, and so on. Do **not** name anything `Gildhaven_GoldsworthHouse`: the town has none.

### The tower (Goldsworth Tower, PROPOSED name)

The family seat, an enormous glass and gold office block. Public on the lower floors, family offices above. No battles inside; it is a place to talk, read and be mildly patronised. Interior base: vanilla Devon Corp (`RustboroCity_DevonCorp_1F` to `3F`, 19 x 9 each, stairs) for the office floors, Palladium `President's Office Tiled.PNG` (324 x 366 px, **20 x 22**, the executive floor) for the top.

| Floor | Name | Layout | What is there |
|---|---|---|---|
| 1F | Lobby | Devon Corp 1F style, or Palladium Dept Store panel | Reception desk, security gates, a directory board, a wall of family portraits where **one rectangle of wall is much cleaner than the rest** (Gatsby's portrait, taken down: foreshadowing, [../../goldsworth.md](../../goldsworth.md)) |
| 2F | Mailroom and Legal | Devon Corp 2F style | The 'mailroom job' joke (Mr. Goldsworth's offer from Scene 1 lands here: the player can see the desk). Legal clerk: a file labelled 'Schemes, in progress' |
| 3F | Accounts and Acquisitions | Devon Corp 3F style | A wall chart 'Gym Acquisition Programme' that updates with the player's badge count (see Items and secrets). The accountant holds the running total that Scheme 9 reads out later ([../../troglodyte-arc.md](../../troglodyte-arc.md)) |
| 4F | Boardroom | new, one long table | Hidden PP Up in a desk. Empty chairs, one with a cushion |
| 5F | President's Office (the family suite) | Palladium `President's Office Tiled.PNG` | **Scene 2** (after the gym): Mr. and Mrs. Goldsworth, Whitmore. Window view of the harbour |
| Roof | Sky Terrace | vanilla `LilycoveCity_DepartmentStoreRooftop` style (18 x 12) | Two satellite dishes, a helipad painted with an enormous G. Hidden Rare Candy. Tobin's wind sock is visible |

Lean build (recommended): 1F, 2F-3F merged into one wide office floor, 4F merged into 5F, plus the Roof, so **4 maps**. Full build: 6 floors plus a small elevator map: **7 maps**. The author decides.

## NPCs

12 to 20 for a city. Names marked PROPOSED are new. Existing names: Tobin, Troglodyte, Mr. and Mrs. Goldsworth ([../../goldsworth.md](../../goldsworth.md)); Whitmore is PROPOSED there.

| Role | Where | Topic (one line) |
|---|---|---|
| Basket porters (2, staff in livery) | plaza, then gym forecourt | Scheme 6 setup: they carry a gift basket the size of a sofa, complain about the stairs |
| Mr. Goldsworth III | forecourt (Scene 1), Tower 5F (Scene 2) | Wants to buy the badge, offers the player a mailroom job, wonders why nothing is for sale |
| Mrs. Goldsworth | forecourt, Tower 5F | Warm, vague, thanks the player for being patient, asks what ordinary people want |
| Whitmore (PROPOSED, assistant) | with the parents | Carries the basket, apologises on everyone's behalf, takes notes |
| TOBIN | forecourt (Scene 1), gym | Explains kindly, twice. Talks about the battle as a flight plan |
| Gym guide | gym entrance | Hint about the wind lanes: 'step off the arrows and stand still' |
| Tower receptionist | Tower 1F | Visitors' passes, lists the floors, pointedly does not mention the clean rectangle |
| Mailroom clerk | Tower 2F | The job on offer is sorting rejections from gyms |
| Accountant | Tower 3F | The running total of the Programme; a reaction to each badge you hold |
| Window cleaner | outside the tower, on a rope | Deadpan: 'don't look up', recites what he sees through the windows |
| Emporium floor guide | Emporium 1F | Lists the floors, 'Vitamins are on 5F, prices are on 5F' |
| TM clerk | Emporium 4F | Sells TMs (see Items) |
| Roof vending kid | Emporium Roof | Complains about the machine's prices, gives a tip for free |
| Hotel receptionist | Hotel 1F | Offers a room 'complimentary, for guests of the family' |
| Harbourmaster | quay | Surf hint: open water to the east is R19. Mentions Waymeet's ferries that do not exist |
| Pilot friend | Pilots' Club | Teases Tobin, warns R20 is only for nine-badge holders |
| Retired navigator | House A | Old charts, tells the player where the Pinnacle is |
| Move Deleter | his house | Forgets a move for you, free |
| Gate guard, North Gate | North Gate | R18 toll road: closed to the public until the player has the Feather Badge, then waved through |
| Gate guard, Pinnacle Gate | Pinnacle Gate | Checks for all nine badges (see Gating) |
| Townsfolk (3) | avenue, plaza | A glossy shopper who loves the tower, a commuter in a hurry, a jogger who has seen Troglodyte 'sulk past' |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| **HM Fly** (`ITEM_HM_FLY`) | Tobin, after the gym | Win the badge |
| **TM Aerial Ace** (`ITEM_TM_AERIAL_ACE`) | Tobin, with the badge | Win the badge |
| **Amulet Coin** | Mrs. Goldsworth, Scene 2 (Tower 5F) | After the gym and Scene 1 |
| Nugget (hidden) | the plaza fountain | none |
| Max Revive (hidden) | behind the Emporium | none |
| Ultra Ball (hidden) | pier bollard | none |
| Star Piece | rock islet off the quay | Surf (badge 5) |
| Revive | tree in the west cliff garden | Cut (badge 1) |
| Max Ether | behind a cracked boulder at the east cliff | Rock Smash (badge 2) |
| Big Nugget | shelf behind a Strength boulder in the harbour yard | Strength (badge 4) |
| PP Up (hidden) | Tower 4F boardroom desk | none |
| Rare Candy (hidden) | Tower roof, under the helipad | none |
| Mart stock | Emporium: 1F Potion line, balls to Ultra Ball, Repels. 2F Antidote, Full Heal, Revive. 3F X items, Escape Rope. 4F TMs: Protect, Light Screen, Reflect, Double Team, Rest, Torment (each priced as a TM). 5F HP Up, Protein, Iron, Calcium, Zinc, Carbos, expensive. Roof: vending Fresh Water, Soda Pop, Lemonade | Badge counts may gate the 4F and 5F stock (PROPOSED: 6 badges, always met here) |

**Secret: the Programme chart (Tower 3F).** A board titled 'Gym Acquisition Programme' lists the eight earlier schemes. It rewrites itself as the player's badge count rises: 'Crestfall: consultants, pending' becomes 'consultants, returned, MILTANK, ate'. A cheap, deadpan reward for the curious. Only the first six rows can show before Gildhaven; rows 7 to 9 read 'not yet scheduled' until the player returns after those gyms.

**Secret: the clean rectangle (Tower 1F).** Examining it: 'Something large was removed from here. It was not a window.' It points at Gatsby.

## Gym

- **Leader:** TOBIN, Flying, FEATHER BADGE, HM Fly and TM Aerial Ace. A young pilot in a leather jacket, dry and a little vain, never raises his voice. Team (aces from [../../trainer-roster.md](../../trainer-roster.md)): Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42.
- **Interior source:** Palladium `Violet City Gym.png`, 208 x 288 px, **13 x 18 tiles**. The render is a hangar: an entrance with two statues at the bottom, a black pit field with a serpentine grey bridge (three horizontal crossbars joined by two vertical links), and a raised, windowed platform at the top for the leader. Tile art: bridge and statues exist in the render; the pit is black. Check that the wind arrows can use the vanilla forced-movement tile behaviours (walk east, west, north, south).
- **Puzzle idea (PROPOSED): wind lanes.** Each crossbar is a wind lane: arrow tiles push the player along it, left on one bar, right on the next. A short **rest pad** (a normal tile) sits in the middle of each lane and at each link. You step on, get blown, and have to leave the lane at the right pad or be carried to the end and have to walk back. The pit is impassable (no falling), so the puzzle cannot soft-lock. The trainers stand at the lane ends and **see along the lane**: being blown past one starts the battle, so the player times the push. Hint on the wall: 'Stand still. The wind will do the talking.'
- **Gym trainers (3, levels 36 to 38, 3 or 4 below Tobin's lowest 40):** vanilla ids reused, no IVs ([../README.md](../README.md)). Classes avoid animal words.

| # | Class | Team | Where |
|---|---|---|---|
| 1 | Cooltrainer | Pelipper 36, Altaria 37 | bottom lane, left end |
| 2 | Pokémon Ranger | Dodrio 36, Fearow 38 | middle lane, right end |
| 3 | Cooltrainer | Noctowl 37, Staraptor 38 | top lane, left end, just below the leader |

- **Objects:** leader, 3 trainers, a gym guide, 2 statues and a sign: 8 objects, well under 15. There is no healing inside the gym; the Pokémon Center is one street away.

### Scheme 6: the gift basket (beat sheet from [../../troglodyte-arc.md](../../troglodyte-arc.md), details PROPOSED)

Setup, reveal, collapse, in this order. The scene is a `coord_event` trigger on the forecourt (CLAUDE.md), not an `OnTransition`.

1. **Setup (anywhere in town, before the gym).** Two staff in gold livery carry a basket the size of a sofa across the plaza towards the gym. Townsfolk comment. The basket is then set down **across the gym door** as an object that blocks it.
2. **Reveal (trigger on the forecourt).** Mr. and Mrs. Goldsworth and Whitmore meet the player on the forecourt: the offer of the mailroom job, a remark that badges are 'a sort of club'. Tobin steps out of the gym. The parents explain they have come 'to buy the badge for our boy'. They cannot see why it is not for sale.
3. **Collapse.** Tobin explains kindly, twice: it is not for sale, and why. They tip him sincerely (a folded note into his jacket) and wait on the bench 'for the receipt'. The basket is cleared from the door (it goes to the Pokémon Center, where the nurse eats the biscuits).
4. **Troglodyte fight 5, with his parents watching.** Troglodyte arrives: 'I want you to lose where they can see it.' The parents stay on the bench. Team (arc table, PROPOSED): five Pokémon, levels 37 to 40, 'behind ace 42': **Stoutland 'Sir Biscuit' 37, Persian 37, Gardevoir 38, Ponyta 39, plus one stage-3 starter at 40** (the starter pool pruned by `VAR_TROG_STARTER`). After the fight his line: 'Nobody has ever said no to him kindly. I didn't like it.' Mrs. Goldsworth: 'Beau, darling, did you lose on purpose?' They leave. Tobin invites the player in.
5. **Gym battle,** badge, HM, TM. After it the town switches to its 'After' text and Mrs. Goldsworth in the tower can give the gift (**Scene 2**: they cannot work out who to fire, ask what ordinary people want; Mr. Goldsworth wishes his father would pick up the phone).

## Gating

- **North Gate (R18)** closed for the public from the Hoarfell side until the Feather Badge. Walking the other way (Gildhaven to Hoarfell) is always allowed.
- **Pinnacle Gate (R20):** all **9 badges** (checked through the badge table, `GetBadgeCount()`, not by a hard-coded flag list, CLAUDE.md badges rule). Vanilla's door guards only test one badge flag; this is a count.
- **Surf (badge 5)** for the harbour and R19.

## Flags (not claimed)

Names and meanings only. Claim in [../../flags.md](../../flags.md) when built.

| Proposed name | Meaning |
|---|---|
| `FLAG_VISITED_GILDHAVEN` | fly flag (set in the town's OnTransition) |
| `VAR_GILDHAVEN_STATE` | 0 arrival, 1 basket delivered, 2 reveal done, 3 Troglodyte beaten, 4 gym beaten, 5 Scene 2 seen |
| `FLAG_RECEIVED_HM_FLY` | Tobin's HM given |
| `FLAG_RECEIVED_TM_AERIAL_ACE` | badge TM given |
| `FLAG_RECEIVED_AMULET_COIN` | Scene 2 gift taken |
| `FLAG_GILDHAVEN_R18_GATE_OPEN` | optional, if not just testing `FLAG_BADGE06_GET` (which exists) |
| `FLAG_HIDDEN_ITEM_GILDHAVEN_*` | five hidden items (fountain, behind the Emporium, pier, tower 4F, tower roof) |
| `FLAG_ITEM_GILDHAVEN_*` | Star Piece, Revive, Max Ether, Big Nugget |
| `TRAINER_TROGLODYTE_GILDHAVEN` | trainer constant, reusing a vanilla id (alias), defeated flag is that id's |
| `TRAINER_GILDHAVEN_GYM_1` to `_3` | the three gym trainers (aliases) |

`FLAG_BADGE06_GET` already exists and is the 'Feather' flag in the badge table; reuse it for the gates.

## Build order and effort

**Hard. The biggest card.** Order: (1) exterior trace and the skyscraper art decision, (2) Pokémon Center and Emporium (shared layouts, quick), (3) gate houses and warps, (4) gym (needs wind-arrow tiles and rest pads), (5) tower floors, (6) the scene scripts and Scheme 6 triggers, (7) dialogue. Why hard: a 60 x 50 map with a unique building, about 27 maps, three coord-event scenes, and a tower exterior that has no tile art.

## Open questions

1. **Skyscraper exterior art:** new tiles (Radio Tower, Battle Tower) or a very large office block in an existing tileset? Affects the whole city's look.
2. **Mirror the render?** Traced flipped, the harbour is on the east, matching R19. Confirm or keep the render's orientation and move R19's connection.
3. **Gate rule on R18:** the sketch draws R18 as a thin line. The card makes it a private toll road closed from the Hoarfell side until the Feather Badge. Is that what the thin line means?
4. **Lean or full tower** (4 maps or 7)?
5. **Elevator:** needs a small script change if the floor list differs from vanilla's five. Wanted?
6. **Troglodyte fight 5 species** follow the arc table (Stoutland, Persian, Gardevoir, Ponyta). Still PROPOSED.
7. **Amulet Coin as the Scene 2 gift:** OK, or would the author prefer something else?
8. Palladium's Gildhaven source is an image of Goldenrod's gym fronts and dept store: the 'Dept Store' becoming 'Emporium' is a name change only.
