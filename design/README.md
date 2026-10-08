# design/ - the Veldris game bible

**Read the relevant files here before building any content. Update them in the same change (same commit) that adds or alters content.**

| File | What it holds | Update it when |
|---|---|---|
| [game-bible.md](game-bible.md) | Title, pitch, tone, pillars, scope, progression, **open decisions** | Scope, tone or a decision changes |
| [story-outline.md](story-outline.md) | Act-by-act beats and the Goldsworth sabotage schemes | You add or change a story beat, scheme or cutscene |
| [characters.md](characters.md) | Cast, voices, trainer constants, teams | A character or trainer is added or changed |
| [interiors.md](interiors.md) | The built Hollowbrook interiors (player house 1F/2F, Fennick's lab): contents, tileset notes, which tile is what | An interior or the Gen 4 interior tileset changes |
| [towns-and-routes.md](towns-and-routes.md) | The 18 towns and 33 routes, map names, build status | A map is added, renamed or changes status |
| [porymap-first-map.md](porymap-first-map.md) | A beginner's guide to building Hollowbrook in Porymap: setup, the git loop, a smoke test, pitfalls and a time estimate | You learn something new about Porymap or the workflow |
| [wendlebury.md](wendlebury.md) | Town 3 plan: role, position, buildings, NPCs; dialogue in `dialogue/wendlebury.inc` | The map or the town plan changes |
| [dialogue/briarwick.inc](dialogue/briarwick.inc), [dialogue/route3.inc](dialogue/route3.inc) | Dialogue drafts for Briarwick (Scheme 2 tent, gym 2 and HACHIMEL, the first Goldsworth house, Apiary, houses) and Route 3 | The maps or the cards change |
| [dialogue/random_npcs.inc](dialogue/random_npcs.inc) | A pool of 295 filler lines for vague, random NPCs and trainers (townsfolk, elders, kids, shops, walkers, coast, caves, fields, battle tips, weather, Pokémon lovers, odd lines, and 3 intro/defeat/after sets for 16 trainer classes). Nothing story-centric | The author wants more or fewer lines |
| [maps/detail/index.md](maps/detail/index.md) | The detailed design pass: every town, building interior, gym, road and landmark in builder-level detail, with decisions and open questions | The author decides the open questions |
| [setup-budget.md](setup-budget.md) | Map sections, flags and trainer budgets for everything past Hollowbrook and Route 1, and the checks done | The cards or counts change |
| [region-sketch.md](region-sketch.md) | The author's hand-drawn region sketch, my reading, section budget, suggested terrain | The sketch or the map changes |
| [region-names.md](region-names.md) | PROPOSED names, themes, gyms and map sources (Palladium and vanilla) for every settlement and landmark | The author picks or changes names |
| [scripts/README.md](scripts/README.md) | DRAFT, UNBUILT map scripts for Hollowbrook, the lab, Route 1 and Wendlebury, with the proposed new flags and vars. Not in `data/event_scripts.s` | The maps are built and the scripts move into their `scripts.inc`, or a scene changes |
| [crestfall.md](crestfall.md) | Town plan (a town, gym 1): buildings, NPC list, Scheme 1 beats, and the exterior as built (layout B). Map BUILT, the rest PROPOSED | The map or the city plan changes |
| [dialogue/crestfall_scheme1.inc](dialogue/crestfall_scheme1.inc) | DRAFT for review: Scheme 1, the private booking (Hollis the attendant, the photographer, Greta, Troglodyte's fight 2, the noticeboard). Replaces the consultant lines in crestfall.inc | The author reviews it |
| [factions.md](factions.md) | The villain teams: The Commons (land) and the Drowned Crown (sea), their alliance, where they appear, open questions. Core points from the author, details PROPOSED | The villain story changes |
| [troglodyte-arc.md](troglodyte-arc.md) | PROPOSED arc options, schemes 2 to 9 and his fight schedule; samples in `dialogue/troglodyte_arc_samples.inc` | The story path is decided |
| [gyms.md](gyms.md) | PROPOSED options for gyms 2 to 9 (types, leaders, badges, HMs, TMs, teams) | The author picks a type order |
| [goldsworth.md](goldsworth.md) | Goldsworth houses and parents, PROPOSED; lines in `dialogue/goldsworth.inc` | The family plan changes |
| [postgame.md](postgame.md) | Elite Four, Champion (aged Cynthia, author-chosen), finale and post-game; lines in `dialogue/league.inc` | The League plan changes |
| [dialogue/crestfall_extra.inc](dialogue/crestfall_extra.inc) | PROPOSED draft for the rest of Crestfall's NPCs: market, farmhands, gym statue, houses, kids, shopkeeper and the Goldsworth house. Width-checked, not wired | An NPC changes, or the map exists |
| [dialogue/hollowbrook_houses.inc](dialogue/hollowbrook_houses.inc) | PROPOSED draft for Hollowbrook's neighbour house and the player-house extras, with starter variants. Width-checked, not wired | An NPC changes, or the maps exist |
| [route1.md](route1.md) | Route 1 draft: wild Pokémon, three trainers, NPCs and items; dialogue in `dialogue/route1.inc` | The map or the route plan changes |
| [route2.md](route2.md) | Route 2 draft: wild Pokémon, four trainers, NPCs, items and the Scheme 1 surveyors; dialogue in `dialogue/route2.inc` | The map or the route plan changes |
| [porymap-walkthrough.md](porymap-walkthrough.md) | Click-by-click Porymap guide for Hollowbrook, the lab and Route 1, with where everything goes; preview picture in `art/first_maps_preview.png` | Porymap behaviour or the map plan changes |
| [gym-leader-art.md](gym-leader-art.md) | Candidate trainer pictures (3 to 5 per leader), sources, licence warning | A leader or art source is picked |
| [trainer-roster.md](trainer-roster.md) | The 13 built leader, Elite Four and Champion trainer blocks: ids, pictures, teams | A block changes |
| [leader-names.md](leader-names.md) | DRAFT name options (3 per leader) for gyms 2 to 9 | The author picks names |
| [map-plan.md](map-plan.md) | Where each map comes from (Palladium references and vanilla bases) and who does what | A map is planned, traced or swapped for another source |
| [region-map.md](region-map.md) | How maps, the town map and fly destinations are wired, plus the Veldris layout proposal | You touch the region map or fly destinations |
| [teams.md](teams.md) | PROPOSED trainer teams with level-legal moves (Crestfall gym first) | A team, level or trainer changes |
| [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc) | PROPOSED draft of all Hollowbrook dialogue: mother, townsfolk, hens, the grandfather, the lab aides, Fennick, and the Troglodyte encounter. Width-checked, not wired into any map | The scene or an NPC changes, or the maps exist and the text moves into `scripts.inc` |
| [dialogue/crestfall.inc](dialogue/crestfall.inc) | PROPOSED draft of Crestfall: Scheme 1 (the consultants), the Troglodyte battle beats, Greta's gym dialogue and two optional gym trainers. Width-checked, not wired | Greta, the scheme or the gym trainers change, or the map exists |
| [dialogue-style.md](dialogue-style.md) | Voice rules, text format, charmap limits | A new text rule is found |
| [flags.md](flags.md) | Every flag and var the hack uses, plus the spare pool | **Any** flag or var is used, added or freed |
| [trainer-slides.md](trainer-slides.md) | Mid-battle trainer lines (BUILT mechanism, no lines yet): where rows live, triggers, traps, text rules, PROPOSED options | A slide row is added, or the author approves wording |
| [field-moves.md](field-moves.md) | BUILT: field moves (Cut, Surf, Flash, Sweet Scent, ...) work when a party Pokémon can learn them, no move slot needed. Rule, code, test results | The move set, the rule or the party menu behaviour changes |
| [running-shoes.md](running-shoes.md) | BUILT: Running Shoes given by Mom, and the L-button run-by-default toggle. Flags, code, options not taken | The gift, the toggle or its default changes |
| [journal.md](journal.md) | BUILT: the Journal key item (badges, next-goal hint, TROGLODYTE loss tally). Item slot, giver, how to add a fight, hint rows, open questions | A TROGLODYTE fight is added, the gym order changes, or the giver changes |
| [exp-share.md](exp-share.md) | BUILT (config): Gen 6 Exp. Share key item and its flag. Giver undecided | The giver is decided, or the Exp. Share setup changes |
| [time-of-day.md](time-of-day.md) | BUILT (config): time-of-day wild encounters, TIME_DAY fallback, hours, label rules, how to add a Night table, `design/tools/wild_lint.py` | A table is split by time, or the clock source changes |
| [debug-presets.md](debug-presets.md) | BUILT: the tracked pre-commit hook (ROM guard, dialogue and wild-table checks), the Veldris cheat start and the eight debug Script presets | A debug preset or a hook check changes |
| [npc-walkup.md](npc-walkup.md) | DOCUMENTED, not built: an NPC that spots the player, walks up and talks (trainer-approach machinery, no battle). Recipe and traps | The first walk-up NPC is built or tested |
| [furniture-lines.md](furniture-lines.md) | EXPLAINED, not built: cabinets, dressers, paintings and TVs that speak when the player presses A. What exists, what it takes | The author asks for it |
| [badges.md](badges.md) | Survey of hacks with more than 8 badges, and the IMPLEMENTED 9-badge table | Badge decisions or the badge plan change |
| [engine-limits.md](engine-limits.md) | Hard engine limits (badges, trainers, sections, tiles, space) and config switches | A limit is re-measured or an edit moves one |
| [engine-edits.md](engine-edits.md) | Every edit to upstream (non-hack) files | You edit anything outside hack content |
| [asset-inventory.md](asset-inventory.md) | What is usable in the asset repos, and what has been imported | An asset is imported |

Tool: [tools/dialogue_check.py](tools/dialogue_check.py) checks that dialogue fits the text box (see [dialogue-style.md](dialogue-style.md)).
Map builders for the LeoB exteriors (Route 1, Crestfall): [tools/leob/](tools/leob/README.md).

## Status words

Everything an assistant suggests starts as **PROPOSED**. It only becomes canon when the author says so.

- **PROPOSED** - suggested, not yet approved. Safe to rename or drop.
- **APPROVED** - the author said yes. Build against it.
- **BUILT** - it exists in the game and builds.

## Order of work for any content change

1. Read the relevant design files.
2. Make the change (scripts, events, warps, trainers, dialogue; maps are the author's, in Porymap).
3. Update design files, `flags.md` and `CREDITS.md` in the same change.
4. Run `make -j4`. It must pass.
5. Commit, push.
