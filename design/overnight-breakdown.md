# Overnight breakdown (2026-10-09 to 2026-10-10)

You asked for a big pile of work to review: first a quality review of everything built, then new things in order, and drafts instead of guesses where you are needed. This is the plain-language result. Everything is on branch `claude/pokemon-pot-setup-evpysj` (draft PR 1), the build passes, and the ROM is 25.81 MiB of the 32 MiB limit (6.19 MiB free). It was 25.58 MiB before the other session imported 70 overworld sprites and 94 battle pictures; none of my changes added to it.

## 1. Review of what was already built

A 54-finding review (every finding was re-checked by a second reader against the tree before I acted) found **no crash in the intro or the Hollowbrook opening**, but it did find four real gameplay holes, one engine bug in each of two systems, and a lot of merge-risk and doc drift. What I did:

**Fixed and tried in the emulator (the robot, section 2):**

| Problem | Fix | Proof |
|---|---|---|
| You could walk out of Hollowbrook to Route 1 with no Pokémon | Three trigger tiles at the east edge push you back with a line while you have no starter | robot test, passes |
| The lab doorway is 4 tiles wide but only 2 started the Troglodyte scene, so you could skip it or leave with no starter | Side-door triggers on the other two tiles, exit blocker on both door mats | robot tests, pass |
| Your respawn point was reset every time you entered Hollowbrook, so a later Pokémon Center heal point was overwritten | Set once in your room at the start | robot test, passes |
| Your fridge could never be read (the pet stood on its only facing tile) | Pet moved one tile | robot test, passes |
| Karrablast and Shelmet could not both evolve (each waited for the other to still be un-evolved) | A third evolution rule each | data check |
| Troglodyte says 'Go, <starter>!' but his lead was random | His starter versions are tagged Lead | data check |
| Dive could never unlock, white-out money read past its table (found earlier, already pushed) | Fixed at the root with an enum from the badge table, so a non-contiguous badge flag cannot be mis-indexed | unit tests |
| Four upstream tests broke when we added the 9th badge and the fake clock | Tests rewritten for 9 badges, SaveBlock3 pin follows the fake clock | **4 repaired tests pass, plus 3 new hack tests** |

**Cleaned for the engine "done right" goal (you asked about this):** the hack now touches fewer upstream lines and the ones it touches are pure insertions.
- Field-move hooks keep upstream's loops byte-identical and only add after them (so upstream's coming `enum PartyMon` rewrite will not conflict).
- The Troglodyte starter logic moved into its own file; the obedience edit in `battle_util.c` was reverted (it never changed any outcome); the Hoenn cheat-start body is back and only relabelled; all hack lines in `event_scripts.s` sit in one block away from where upstream appends.
- **Map saves are fast again:** saving one `map.json` used to recompile about 764 C files (about 4 minutes); now it recompiles none (measured 4 seconds), because the generated headers are only rewritten when their content changes.
- Build-time guards (`src/veldris_checks.c`): the build fails if a SaveBlock size changes (this protects your Delta saves), if the trainer flag space shrinks, or the badge table goes out of step. A runbook for pulling upstream is in `design/engine-edits.md`.
- Stale numbers corrected in the docs (map sections left: about 8, not 37; spare flags 299; badge 9 cap 60; Dive on badge 9).

Left alone on purpose (after checking): swapping two flags to make badges contiguous (undoes your approved badge-table design), setting obedience via a config switch (would change gameplay for every Pokémon), renaming the Route 1 trainer aliases (more upstream lines for no gain).

## 2. New work

| What | Result | Where |
|---|---|---|
| **Robot player** | Plays the ROM in a hidden mGBA and checks it. 18 tests, all pass on the current ROM in 2 minutes (3 with the Route 1 night walk). Replaces the 40-tool-call hand walks: `scene.py` plays a scenario and takes a picture. Tests mGBA, not Delta | `design/tools/emu/` |
| **Filler pass: Hollowbrook houses and Route 1** | Audit found nothing unscripted. Fixed the fridge, furniture signs now work from any side, two new TV lines, the Route 1 farmer no longer repeats the guide's line | committed; see W1 in `decisions-pending.md` |
| **Mid-battle line options** | 97 lines for the nine gym leaders and 24 options for the Elite Four, Cynthia, the Commons and Crown bosses, three tones each, all measured to fit. Tried in mGBA: five of the six triggers played in a real battle. **Nothing wired** (your rule) | `design/trainer-slide-options/` |
| **Decision briefs** | About two dozen questions with pictures, patches and a one-letter answer each (AI ladder, default IVs, level caps, boss boosts, tag battles, text skip, move relearner, night lights, comforts, defaults, starters, cities) | `design/decisions-pending.md` first, then `design/decisions/` |
| **Trainer lint** | Checks alias targets, Journal rows for Troglodyte fights and `IVs:` lines on every Veldris block | `design/tools/trainer_lint.py` |
| **NPC walk-up recipe** (task 29) | Built and run in a scratch clone: 26 NPCs and about 30 scenarios in the robot. The recipe works; upstream's `cant_see_if_set` guard is the better default. New traps found (coord events in the sight line are skipped on the first step, an NPC only exists within a window around the player, 15 NPCs at most). Not in the real game yet, no engine edit needed | `design/npc-walkup.md`, `design/scripts/walkup_template.inc`, `design/tools/walkup_lint.py` |
| **Commit hook** | The ROM guard now catches saves, savestates, build output, archives, patch files and any staged file over 8 MB (the old one was filename-only and could be bypassed); lints run only when their files are staged; `VELDRIS_SKIP_LINTS=1` skips lints but keeps the guard; a merge without conflicts is guarded too | `.githooks/` |
| **Hoenn purge brief** | Measured in a scratch clone. Recommendation **LEAVE**: free ROM is 6.19 MiB and nothing the purge helps is near a limit. SKIP (tag Hoenn maps like FRLG) frees about 1.2 MiB and was run through the robot; DELETE fails with 63 build errors and breaks saves | `design/decisions/arch.md` |

## 3. What I need from you

Open `design/decisions-pending.md`: one table, one code per question, my pick beside each. The ones with the most effect on the game: **S1** the four starters, **1** the AI ladder, **3** level caps, **U1** hold-R text skip, **L1 and L2** the tone of the leaders' and League's mid-battle lines. Also needed: **close or reload Porymap before pulling**, because `map.json` event lists changed in Hollowbrook, the lab, the player's house, the neighbour's house and Route 1.

## 4. Second pass (landed 2026-10-10)

The leftovers that hit the usage limit overnight are done: the NPC walk-up test, the Hoenn purge brief, the commit-hook hardening and the remaining stale-doc fixes. Two things I found while integrating them and put to you in `decisions-pending.md`: Greta's wired gym-invite line differs from the draft you approved (W2), and the Rich jingle is heard twice in Hollowbrook (it restarts when the battle begins) but only once in Crestfall (Q3, corrected: Crestfall already plays it). Neither was heard in the robot (it has no audio), so Q3 is from reading the code.

## 5. Honest limits

- Everything was run in mGBA. Delta (VBA-M) and Miyoo can differ in timing and drawing.
- No line of the drafted leader or League dialogue was seen in a full playthrough, only the triggers in a test battle.
- The hold-R skip and the other prototypes are patches, not merged.
