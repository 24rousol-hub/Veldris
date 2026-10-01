# Landmarks of the centre

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../region-sketch.md](../region-sketch.md)), the approved names ([../region-names.md](../region-names.md)) and the League design ([../postgame.md](../postgame.md), [../trainer-roster.md](../trainer-roster.md), [../troglodyte-arc.md](../troglodyte-arc.md)). Format: [README.md](README.md). Nothing here is built. Roads: [routes-centre.md](routes-centre.md) (R20 arrives, R21 leaves). Town: [towns/gildhaven.md](towns/gildhaven.md). New minor names PROPOSED.

Sections in this file: **THE PINNACLE** (the Elite Four landmark between Gildhaven and Vesperhaven). The centre has no other landmark: the sketch's other green circles belong to the west (Mothwood, Slagwell Mine), the east (Mirror Isle) and the south (Silverstrand, Echo Hollow, Argent Peak).

---

## THE PINNACLE (landmark, the League, sketch 'Elite 4')

### Role in the story

- **The League.** The end of the main story: four Elite Four members, then **Troglodyte's last fight** in the corridor, then **CYNTHIA the Champion**, then the Hall of Fame. Order of the Elite Four: **OSSIAN (Dark), HYACINTH (Psychic), DUNMORE (Fighting), DRAYDEN (Dragon).**
- Reached by **R20** (the Victory Road gauntlet) from Gildhaven, after all nine badges ([routes-centre.md](routes-centre.md)). After the Hall of Fame the south side opens to **R21**, the post-league road to Vesperhaven.
- Tone: grand, a little ridiculous, and a bit sad. The Elite Four are each a character with a hobby (OSSIAN keeps a Honchkrow on the hearse, a Pokémon, as in [../leader-names.md](../leader-names.md)). It is the stage of the humiliation arc: Troglodyte's final conversion happens here ([../troglodyte-arc.md](../troglodyte-arc.md), 'Humbled').
- Champion CYNTHIA is an **aged guest champion**, Gatsby's old friend, defending the seat ([../postgame.md](../postgame.md)). The player does not learn who she is to Gatsby until after the League.

### Where it sits

South of Gildhaven, north-west of Vesperhaven. In the sketch, an arrow (33) runs from Gildhaven down to the small green circle labelled 'Elite 4', and then arrows '3c' (read as 31, R21) run on to the south-centre city.

| Edge of the exterior | Road | Notes |
|---|---|---|
| North | **R20** (cave exit stair) | the only way in |
| South | **R21** to Vesperhaven | a stone gap barred by two guards until `FLAG_SYS_GAME_CLEAR` |
| West, east | none | cliffs and a drop to the sea |

### Source and size

| Map | Source | Tiles |
|---|---|---|
| The Pinnacle (exterior plateau) | none in Palladium. Reference for the front: Palladium `Battle Tower.png` (409 x 443 px, 24 x 26, a glass-faced tower on a stone plaza), only as a mood. Vanilla `EverGrandeCity` (40 x 80, the Hoenn League island) is too large and a waterfall map. Plan a **new plateau, about 28 x 26**, in the Ever Grande tileset (League building, stone steps, tall fences) | `(28+15)*(26+14) = 1720`, fine |
| Lobby (1F) | vanilla `EverGrandeCity_PokemonLeague_1F` (19 x 12), nurse, clerk, two door guards | |
| Room 1, OSSIAN | Palladium `e4karenad5.png` (240 x 360 px, **15 x 22**): black and grey floor, a central emblem, a stepped entry | |
| Room 2, HYACINTH | Palladium `e4willja7.png` (**15 x 22**): purple floor with a pool on either side of the entry | |
| Room 3, DUNMORE | Palladium `e4brunoym3.png` (**15 x 22**): yellow floor with lava pits either side | |
| Room 4, DRAYDEN | Palladium `e4kogard3.png` (**15 x 22**): green floor with trees and grass either side (reads as a dragon-keeper's garden) | |
| The Last Corridor (Troglodyte) | vanilla `EverGrandeCity_Hall4` (11 x 34, the long hall to the Champion) | |
| Champion's Hall (CYNTHIA) | Palladium `championlacetq2.png` (240 x 512 px, **15 x 32**, Lance's room: a long red carpet, dragon-horn statues on both sides, a raised dais). Swap the statues for plain columns. Fallback: vanilla `EverGrandeCity_ChampionsRoom` (13 x 13) | |
| Hall of Fame | Palladium `halloffamegscrevampzr1.png` (160 x 263 px, about **10 x 16**, a gold diamond-pattern floor with the record machine). Fallback: vanilla `EverGrandeCity_HallOfFame` (15 x 17) | |

The vanilla E4 rooms are only 13 x 14 each (`EverGrandeCity_SidneysRoom`, `_PhoebesRoom`, `_GlaciasRoom`, `_DrakesRoom`, tileset `gTileset_EliteFour`) and **cost nothing to build**. The Palladium rooms are bigger and more handsome but need floors, water, lava and tree tiles approximated from the tilesets in the tree ([../map-plan.md](../map-plan.md): about 70% matches). The author chooses. Each Palladium room's lower strip is its own **vestibule**, so no separate hall map is needed between rooms; vanilla's `EverGrandeCity_Hall1` to `Hall3` (11 x 13 short halls) are then unused.

**Section and fly.** Proposed section: rename the Hoenn entry `MAPSEC_EVER_GRANDE_CITY` to **'THE PINNACLE'** (12 characters), the same method used for R4 to R21 ([../region-sketch.md](../region-sketch.md)). That also reuses `FLAG_VISITED_EVER_GRANDE_CITY` and the two heal locations `HEAL_LOCATION_EVER_GRANDE_CITY` and `HEAL_LOCATION_EVER_GRANDE_CITY_POKEMON_LEAGUE` that already exist. **Unverified:** check that the vanilla fly icon, the type switch and the heal rows still work after the rename (CLAUDE.md and [../region-map.md](../region-map.md): the 16 vanilla fly towns keep their icons at vanilla x and y). The alternative is a new section (one of the 37 free). **Credit:** Project Palladium team, in the commit that first traces a room ([../map-plan.md](../map-plan.md)).

### Layout

**The exterior (about 28 x 26).** The cave exit stair from R20 arrives at the north edge on a stone landing. A wide flight of steps climbs a plateau to the League building, a long low glass-and-stone hall with a copper dome and a flag on each corner. Two rows of fenced lawns flank the approach; benches and two lamp posts stand beside the steps. The south side is a plain stone wall with an iron gate (the R21 gap), shut by two guards until the Hall of Fame. A Sign: 'THE PINNACLE: Nine badges. Mind the steps.'

```
   R20 stair (north)
          |
   [lawns]---steps---[lawns]
          [ LEAGUE ]
          lobby door
   [bench]          [bench]
   --- iron gate (R21, shut) ---
```

**The lobby (vanilla 1F, 19 x 12).** Reception, a Pokémon Center nurse's counter (the whole League shares one heal point), a Mart counter, two door guards in front of the inner door. This is the player's heal point if they blackout inside (`HEAL_LOCATION_EVER_GRANDE_CITY_POKEMON_LEAGUE` in vanilla, which respawns at the lobby).

**The run.** Lobby, then the four rooms in order, then The Last Corridor, then Champion's Hall, then the Hall of Fame. In vanilla each room's far door is closed until its trainer is beaten (`VAR_ELITE_4_STATE`, `FLAG_DEFEATED_ELITE_4_*`). There is no healing between rooms: the player enters the lobby, bets the whole run on their team, and can leave only by losing or walking back through the vestibules.

| Step | Map | Trainer | Type | Team (levels) | Mood and look |
|---|---|---|---|---|---|
| 1 | Room 1, black and grey | **OSSIAN** | Dark | Houndoom 65, Honchkrow 65, Pangoro 65, Krookodile 66, Absol 66 | Cheerful undertaker. A hearse as an object |
| 2 | Room 2, purple and pools | **HYACINTH** | Psychic | Espeon 66, Meowstic 66, Reuniclus 67, Farigiraf 67, Alakazam 68 | Icy, deadpan, snow globes on the sideboard |
| 3 | Room 3, yellow and lava | **DUNMORE** | Fighting | Breloom 68, Hawlucha 68, Heracross 69, Annihilape 69, Conkeldurr 70 | Huge, gentle, naps between rounds. A cushion in the corner |
| 4 | Room 4, green garden | **DRAYDEN** | Dragon | Goodra 69, Kommo-o 69, Dragapult 70, Baxcalibur 70, Salamence 71, Dragonite 71 | Oldest, kind, quietly terrifying. Keeps dragons like pets |
| 5 | The Last Corridor | **TROGLODYTE** (final fight) | Rival | Stoutland 68, Gardevoir 69, Vaporeon 70, Tyranitar 70, Pyroar 70, plus one starter final form at 72 | See below |
| 6 | Champion's Hall | **CYNTHIA** | Champion | Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 | Dry, warm, sharp, long in the tooth |
| 7 | Hall of Fame | none | | | The machine, the attendant, the credits |

Teams are from [../trainer-roster.md](../trainer-roster.md) (built) and [../postgame.md](../postgame.md). The Palladium room colours suit each member: black and grey for OSSIAN (Dark), purple and pools for HYACINTH (Psychic), yellow and lava for DUNMORE (Fighting), a green garden for DRAYDEN. If the author prefers vanilla rooms, the vanilla E4 tileset has matching colours (dark, ghost, ice, dragon).

**Wiring note (for later).** The vanilla room scripts assume the order Sidney, Phoebe, Glacia, Drake. In Veldris the trainer ids sit in that same order (OSSIAN, HYACINTH, DRAYDEN, DUNMORE), but **the fight order is OSSIAN, HYACINTH, DUNMORE, DRAYDEN** ([../trainer-roster.md](../trainer-roster.md)). So rooms 3 and 4 must fight DUNMORE then DRAYDEN even though their ids run the other way: rewrite the room scripts' trainer references and defeated-flag checks. Vanilla flags are `FLAG_DEFEATED_ELITE_4_SIDNEY` (0x4FB), `_PHOEBE` (0x4FC), `_GLACIA` (0x4FD), `_DRAKE` (0x4FE); the hack may keep them under the old names or add aliases. Not claimed here.

### The final Troglodyte fight (corridor, Arc A)

- **Place:** `EverGrandeCity_Hall4` reused as **The Last Corridor** (11 x 34), the long hall between DRAYDEN's room and the Champion's Hall. He waits at the **far end**, in front of the Champion's door. A `coord_event` trigger (CLAUDE.md) at the corridor's south entrance walks him out.
- **Beats** ([../postgame.md](../postgame.md), labels in `dialogue/league.inc`, not wired): arrival ('He claims he bought a League pass, calls the player the help'), battle intro (money and breeding), defeat (denial, then a real admission: he never worked at it), after (he leaves, angry but quiet, promises to come back 'properly'). The arc's sample lines: 'Well fought. I mean it. Go and beat her. I'll write to Grandfather.' and 'I was a prat. You knew.' ([../troglodyte-arc.md](../troglodyte-arc.md), Humbled).
- **Team (from [../postgame.md](../postgame.md)):** Stoutland 'Sir Biscuit' 68, Gardevoir 69, Vaporeon 70, Tyranitar 70, Pyroar 70, plus one starter final form at level 72 (stand-in Sceptile, Blaziken or Swampert). Party Size 6, `Pool Prune: Rival Starter`. No held items. AI Basic Trainer (or the lowest that makes him lose). **Conflict to resolve:** the arc table says fight 8 is 'same six, Garchomp as ace' (Persian, Rapidash, Garchomp) while [../postgame.md](../postgame.md) lists Vaporeon, Tyranitar, Pyroar and moves Milotic to the Champion. This card follows [../postgame.md](../postgame.md), the later document. See Open questions.
- He appears nowhere else in the League.

### The Champion and the Hall of Fame

- **CYNTHIA** is a guest, a previous region's Champion, 'a grudge makes a good engine' ([../postgame.md](../postgame.md)). She stands at the head of the red carpet on the dais. She is fought once. No rematch here at first; her rematch comes later ([../postgame.md](../postgame.md): post-game, 'a League lounge', open question).
- **The Hall of Fame:** the standard vanilla flow: the player walks in, the machine records the team, the credits roll, the save sets `FLAG_SYS_GAME_CLEAR` (used by the grandfather's after-League lines). The attendant's line `League_Text_HofAttendant` and, once the player is back in Hollowbrook, the call from Fennick `League_Text_HofFennickCall` ([../postgame.md](../postgame.md)). The credits currently read `VAR_STARTER_MON`, so check the fourth starter there ([../postgame.md](../postgame.md)). Art and the stage are vanilla, no engine edit.
- After the Hall of Fame the vanilla game warps the player home. Veldris sends the player to Hollowbrook's door (the grandfather's scene starts there, [../postgame.md](../postgame.md)).

### Buildings and maps

| Map | Layout | Notes |
|---|---|---|
| The Pinnacle | new, about 28 x 26 | exterior plateau, no wild encounters. Connection to R20 (north), R21 (south, shut) |
| Pinnacle lobby (1F) | vanilla `EverGrandeCity_PokemonLeague_1F` (19 x 12) | nurse, clerk, 2 door guards, 1 attendant, 1 registrar |
| Room 1 OSSIAN | Palladium Karen room, 15 x 22 | trainer, door |
| Room 2 HYACINTH | Palladium Will room, 15 x 22 | |
| Room 3 DUNMORE | Palladium Bruno room, 15 x 22 | |
| Room 4 DRAYDEN | Palladium Koga room, 15 x 22 | |
| The Last Corridor | vanilla `EverGrandeCity_Hall4` (11 x 34) | Troglodyte |
| Champion's Hall | Palladium Lance room, 15 x 32 | CYNTHIA |
| Hall of Fame | Palladium HoF, about 10 x 16 | the machine |
| Pinnacle Lounge (optional) | small custom room or vanilla `EverGrandeCity_PokemonLeague_2F` re-skinned | post-game: Cynthia's rematch and the reunion if the author wants no Hollowbrook scene ([../postgame.md](../postgame.md) open question 4). Not required |

Nine required maps in all: the exterior, the lobby, four rooms, the corridor, the Champion's Hall and the Hall of Fame (ten with the optional Lounge). All use the Pinnacle's section.

### NPCs

| Role | Where | Topic (one line) |
|---|---|---|
| Door guards (2) | lobby | check for all nine badges, then step aside. `FLAG_ENTERED_ELITE_FOUR` once through |
| Nurse | lobby | the one heal point |
| Mart clerk | lobby | vanilla stock: Ultra Ball, Hyper Potion, Max Potion, Full Restore, Full Heal, Revive, Max Repel |
| League registrar | lobby | takes the name, offers a form, 'nobody has ever filled the form in correctly' |
| Hall of Fame attendant | the Hall | the standard farewell |
| Hopeful trainer | exterior | has lost four times and describes each room by its flaws |
| Photographer | exterior | photographs the building from three angles and the player from one |
| Retired Elite Four fan | exterior | gossip about each member's hobby |
| Sign painter | R20 stair | touches up 'THE PINNACLE: 1 MILE' |
| Flag-polisher | exterior | a caretaker who has polished the same flag for years |

### Items and secrets

| Item | Where | Gate |
|---|---|---|
| Max Elixir (hidden) | exterior, behind the east bench | none |
| Rare Candy (hidden) | exterior, west lawn | none |
| PP Max | lobby, behind the Mart counter | free, after the Hall of Fame (the registrar hands it over with a certificate) |
| Master-class gift: a Nugget | Hall of Fame attendant | after the Hall of Fame |

**Secret:** DUNMORE's cushion. Examine it in his room before the fight: 'It is still warm.' (He naps between rounds.)

### Gating

- **R20 gate:** nine badges, counted through the badge table (`GetBadgeCount()`), at the Pinnacle Gate in Gildhaven ([towns/gildhaven.md](towns/gildhaven.md)). Vanilla door guards test only `FLAG_BADGE06_GET`; Veldris needs a count.
- **Lobby door:** the guards check again (nine badges) so a Fly arrival cannot skip the check.
- **R21 (south gate):** shut until `FLAG_SYS_GAME_CLEAR`.

### Flags (not claimed)

| Proposed name | Meaning |
|---|---|
| `FLAG_VISITED_THE_PINNACLE` (or the renamed `FLAG_VISITED_EVER_GRANDE_CITY`) | fly flag if the Pinnacle is a fly point |
| `FLAG_ENTERED_ELITE_FOUR` | vanilla, exists |
| `VAR_ELITE_4_STATE` | vanilla, exists (0 to 4 run progress) |
| `FLAG_DEFEATED_ELITE_4_*` | vanilla, four exist (see wiring note) |
| `FLAG_DEFEATED_TROGLODYTE_FINAL` | derived from the trainer id (alias `TRAINER_TROGLODYTE_PINNACLE`) |
| `FLAG_DEFEATED_CYNTHIA` | derived from `TRAINER_CYNTHIA` |
| `FLAG_SYS_GAME_CLEAR` | vanilla, exists (Hall of Fame) |
| `FLAG_PINNACLE_PP_MAX_GIVEN` | the post-Hall PP Max gift |
| `FLAG_HIDDEN_ITEM_PINNACLE_*` | the two hidden items |

### Build order and effort

**Hard (long, not tricky).** Order: (1) decide vanilla rooms or Palladium rooms (the vanilla set builds almost for free), (2) the lobby and exterior, (3) rooms 1 to 4 and the warp and door chain, (4) the corridor, Champion's Hall and Hall of Fame, (5) the scripts: vanilla's chain adapted to the new fight order, (6) the Troglodyte coord-event, (7) Hollowbrook's after-scene is a separate card. Why hard: nine maps, a precise warp and door chain, and the League script rewrite. With vanilla rooms and halls reused, most of it is renaming.

### Open questions

1. **The final Troglodyte team.** [../troglodyte-arc.md](../troglodyte-arc.md) lists 'same six, Garchomp as ace' for fight 8, but [../postgame.md](../postgame.md) lists Stoutland, Gardevoir, Vaporeon, Tyranitar, Pyroar and a starter. Which is canon? This card follows postgame.md. Fight 7 (R20) uses the arc table's six (Persian, Rapidash, Garchomp), so the two fights then differ on purpose.
2. **Palladium rooms or vanilla rooms?** Vanilla is free; Palladium is more handsome and needs tile work.
3. **Is The Pinnacle a fly point?** The card proposes yes (the League sends the player to the lobby when they lose, and the heal location already exists in vanilla). Rename `MAPSEC_EVER_GRANDE_CITY` or add a new section?
4. **Badge count for the League:** all nine, or eight (the vanilla guard tests one flag)? R20's levels assume nine.
5. **The Lounge** (post-game Cynthia): a League lounge, or only Gatsby's house ([../postgame.md](../postgame.md), question 4)?
6. **Sketch labels:** the road past the Pinnacle reads '3c' in the sketch; I read it as 31, with R21 named for it in the README. Confirm. The sketch's arrow from Gildhaven reads '33'.
7. The sketch draws the Pinnacle as one small green circle with no side path. I assume the exterior is a dead end apart from the two roads.
