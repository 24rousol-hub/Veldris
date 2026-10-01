# Built trainer roster: leaders, Elite Four and Champion

Status: **BUILT 2026-10-01** (the ROM compiles; nothing has been fought in a game yet). Names approved by the author on 2026-10-01 ([leader-names.md](leader-names.md)). Teams and levels from [gyms.md](gyms.md) and [postgame.md](postgame.md). Movesets were hand-curated by agents from this tree's real learnsets, then checked by script: every move is level-up-legal at that level, or (from level 40 up) teachable. Source: `src/data/trainers.party`.

**How they were added.** They **reuse vanilla Hoenn trainer ids**, so they cost no new id and `TRAINERS_COUNT_EMERALD` is unchanged. Each vanilla block was rewritten and its header renamed. In `include/constants/opponents.h` the id now has the Veldris name, and the old Hoenn name is kept as an alias, so the untouched Hoenn map scripts still compile. Use the new names in scripts (`trainerbattle_single TRAINER_HACHIMEL, ...`). **Every Pokémon has `IVs: 0 ...`** (no IVs, per the author) and no EVs. Items: Potion up to Full Restore. AI: Basic Trainer. Elite Four and Champion keep the vanilla Mugshot colours.

| Constant | Name | Replaces | Type | Pic | Team (level) |
|---|---|---|---|---|---|
| `TRAINER_HACHIMEL` | HACHIMEL | Roxanne | Bug, gym 2 | Veldris Leader Bug | Kricketune 17, Vivillon 19 |
| `TRAINER_SANZUFORD` | SANZUFORD | Brawly | Ghost, gym 3 | Veldris Leader Ghost | Shuppet 23, Litwick 24, Mimikyu 25 |
| `TRAINER_HAGANE` | HAGANE | Wattson | Steel, gym 4 | Veldris Leader Steel | Bronzor 29, Pawniard 30, Tinkatuff 31 |
| `TRAINER_WAKASAGI` | WAKASAGI | Flannery | Ice, gym 5 | Veldris Leader Ice | Sneasel 35, Vanillish 36, Lapras 37, Avalugg 37 |
| `TRAINER_TOBIN` | TOBIN | Norman | Flying, gym 6 | Veldris Leader Flying | Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42 |
| `TRAINER_ASEBY` | ASEBY | Winona | Poison, gym 7 | Veldris Leader Poison | Weezing 46, Crobat 47, Drapion 47, Garbodor 47, Toxapex 48 |
| `TRAINER_SUZURAN` | SUZURAN | Tate and Liza (now a single battle) | Fairy, gym 8 | Veldris Leader Fairy | Azumarill 52, Dachsbun 52, Ribombee 53, Hatterene 54, Gardevoir 55 |
| `TRAINER_MIZZLE` | MIZZLE | Juan | Water, gym 9 | Veldris Leader Water | Gyarados 58, Seismitoad 58, Araquanid 59, Barraskewda 59, Lanturn 59, Milotic 60 |
| `TRAINER_OSSIAN` | OSSIAN | Sidney | Elite Four, Dark | **placeholder** (Sidney's vanilla pic) | Houndoom 65, Honchkrow 65, Pangoro 65, Krookodile 66, Absol 66 |
| `TRAINER_HYACINTH` | HYACINTH | Phoebe | Elite Four, Psychic | **placeholder** (Phoebe's vanilla pic) | Espeon 66, Meowstic 66, Reuniclus 67, Farigiraf 67, Alakazam 68 |
| `TRAINER_DUNMORE` | DUNMORE | Drake | Elite Four, Fighting | **placeholder** (Drake's vanilla pic) | Breloom 68, Hawlucha 68, Heracross 69, Annihilape 69, Conkeldurr 70 |
| `TRAINER_DRAYDEN` | DRAYDEN | Glacia | Elite Four, Dragon | Veldris Elite Four Drayden | Goodra 69, Kommo-o 69, Dragapult 70, Baxcalibur 70, Salamence 71, Dragonite 71 |
| `TRAINER_CYNTHIA` | CYNTHIA | Wallace | Champion | Veldris Champion Cynthia | Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 |

**Notes and caveats.**
- The three placeholder Elite Four pictures need art: ask for candidates when you want them.
- The ids are in vanilla order (Sidney, Phoebe, Glacia, Drake), so the id order is OSSIAN, HYACINTH, DRAYDEN, DUNMORE. The League script sets the actual fight order (DRAYDEN last), so nothing depends on the id order.
- The Hoenn rematch blocks (Roxanne 2 to 5 and so on) still hold the old Hoenn teams and are never reached in Veldris. Their data stays untouched.
- Gender and Music are placeholders chosen to fit each sprite (SANZUFORD uses the 'Girl' music).
- **Battle check (2026-10-01, mGBA, debug menu Trainers > Try Battle).** All 13 trainers were fought: intro text, class and name, picture and first send-out species and level were correct for each. CYNTHIA was played for several turns and used her curated moves (Payback seen). One bug found and fixed: MIZZLE's picture drew a light-blue box because the background was palette index 4, not 0. The indices were swapped in `veldris_leader_water.png` and the fix re-checked. Not checked: later team members, full fights, and the vanilla alias scripts.
- The gym trainers (DALE, WREN) and Greta are still unbuilt blocks ([teams.md](teams.md)).
- The movesets are in the file itself. Tune any set by editing its block.
