# design/ - the Veldris game bible

**Read the relevant files here before building any content. Update them in the same change (same commit) that adds or alters content.**

| File | What it holds | Update it when |
|---|---|---|
| [game-bible.md](game-bible.md) | Title, pitch, tone, pillars, scope, progression, **open decisions** | Scope, tone or a decision changes |
| [story-outline.md](story-outline.md) | Act-by-act beats and the Goldsworth sabotage schemes | You add or change a story beat, scheme or cutscene |
| [characters.md](characters.md) | Cast, voices, trainer constants, teams | A character or trainer is added or changed |
| [towns-and-routes.md](towns-and-routes.md) | The 18 towns and 33 routes, map names, build status | A map is added, renamed or changes status |
| [porymap-first-map.md](porymap-first-map.md) | A beginner's guide to building Hollowbrook in Porymap: setup, the git loop, a smoke test, pitfalls and a time estimate | You learn something new about Porymap or the workflow |
| [map-plan.md](map-plan.md) | Where each map comes from (Palladium references and vanilla bases) and who does what | A map is planned, traced or swapped for another source |
| [region-map.md](region-map.md) | How maps, the town map and fly destinations are wired, plus the Veldris layout proposal | You touch the region map or fly destinations |
| [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc) | PROPOSED draft of all Hollowbrook dialogue: mother, townsfolk, hens, the grandfather, the lab aides, Fennick, and the Troglodyte encounter. Width-checked, not wired into any map | The scene or an NPC changes, or the maps exist and the text moves into `scripts.inc` |
| [dialogue/crestfall.inc](dialogue/crestfall.inc) | PROPOSED draft of Crestfall: Scheme 1 (the consultants), the Troglodyte battle beats, Greta's gym dialogue and two optional gym trainers. Width-checked, not wired | Greta, the scheme or the gym trainers change, or the map exists |
| [dialogue-style.md](dialogue-style.md) | Voice rules, text format, charmap limits | A new text rule is found |
| [flags.md](flags.md) | Every flag and var the hack uses, plus the spare pool | **Any** flag or var is used, added or freed |
| [badges.md](badges.md) | Survey of hacks with more than 8 badges, and the IMPLEMENTED 9-badge table | Badge decisions or the badge plan change |
| [engine-limits.md](engine-limits.md) | Hard engine limits (badges, trainers, sections, tiles, space) and config switches | A limit is re-measured or an edit moves one |
| [engine-edits.md](engine-edits.md) | Every edit to upstream (non-hack) files | You edit anything outside hack content |
| [asset-inventory.md](asset-inventory.md) | What is usable in the asset repos, and what has been imported | An asset is imported |

Tool: [tools/dialogue_check.py](tools/dialogue_check.py) checks that dialogue fits the text box (see [dialogue-style.md](dialogue-style.md)).

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
