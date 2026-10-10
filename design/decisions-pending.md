# Decisions waiting for you

Status: **PROPOSED, nothing here is built or wired.** Written 2026-10-10 from the overnight work (briefs checked against the tree, most of them also tried in a scratch copy in mGBA). Reply with the codes, for example `Q1 B, 1 ladder, 2 zero, U1 B`. Anything you skip stays as it is today. Rule 10 applies: story beats (the starters, house fights, slide wording for gym leaders, the League, Cynthia, the Commons and the Crown) wait for your answer, they are not built.

## Quick-answer sheet

| Code | Question | Options | My pick | Full text |
|---|---|---|---|---|
| Q1 | Who gives the Journal? | A Route 1 guide (built) / B Mom, in the shoes scene / C Fennick (a key scene) | B | [story.md](decisions/story.md) |
| Q2 | Game-day length of the fake clock | A 72 real minutes (built) / B real time / C 24 minutes | keep A | [story.md](decisions/story.md) |
| Q3 | Rich jingle timing in Troglodyte's scenes (corrected: Crestfall already plays it once at battle start; Hollowbrook starts it at the shout and it restarts when the battle begins) | A keep as built / B Hollowbrook plays it once / C Crestfall starts it at the shout too | A unless you hear the restart and dislike it (then B) | [story.md](decisions/story.md) |
| Q4 | Victory tune after beating Troglodyte | A gym leader (built) / B Elite Four / C ordinary | keep A | [story.md](decisions/story.md) |
| Q5 | Wall clock spot in the bedroom | A x=3 (built) / B x=6 | keep A | [story.md](decisions/story.md) |
| Q6 | Clock hours | A Morning/Day/Evening/Night (built) / B Gen 4 style | keep A | [story.md](decisions/story.md) |
| Q7 | Route 1 night species | keep Hoothoot, Rattata, Spinarak, Murkrow / change | keep | [story.md](decisions/story.md) |
| Q8 | The 17 furniture lines | keep / richer / poorer | keep | [story.md](decisions/story.md) |
| S1 | The four starters (open decision 14) | A Johto + Togepi / B Sinnoh + Riolu / C Unova + Eevee / D Hoenn stand-ins | A (B if you want Cynthia seeded early) | [story.md](decisions/story.md) |
| S2 | Which places are cities, and the skyscraper (decisions 12 and 8) | adopt your sketch labels / tell me what changes | adopt | [story.md](decisions/story.md) |
| S3 | Goldsworth house fights (decision 11) | A NPC only / B one shared family trainer id for 2 or 3 loud houses | B | [story.md](decisions/story.md) |
| S4 | How cruel may a Goldsworth be (decision 10) | A never to innocent townsfolk / B rude to townsfolk, never cruel to children or animals | A | [story.md](decisions/story.md) |
| 1 | AI ladder: weak early, smart late | ladder / flat / custom | ladder | [battle.md](decisions/battle.md) |
| 2 | Default IVs when a block forgets `IVs:` | zero / explicit / leave | zero | [battle.md](decisions/battle.md) |
| 3 | Level caps | off / soft / hard / hardobey | soft | [battle.md](decisions/battle.md) |
| 4 | Stat boosts at the start of boss fights | none / legends / bosses | legends | [battle.md](decisions/battle.md) |
| 5 | Tag battles and two-opponent battles | none / tag / both | both | [battle.md](decisions/battle.md) |
| U1 | Hold a button to skip text | A no (just FAST default) / B hold R / C hold B | B | [ui.md](decisions/ui.md) |
| U2 | Story-unlockable move relearner | A leave / B Egg and Tutor tabs unlocked by flags / C Heart Scale tutors / D all on, then F filler NPC or S story person gives it | B F | [ui.md](decisions/ui.md) |
| U3 | Night lights | A none / B glowing Center and Mart signs and lamp orbs / C plus lit windows | B | [ui.md](decisions/ui.md) |
| U4 | 12 small comforts | A my items 1 to 6 / B none / C your numbers | A | [ui.md](decisions/ui.md) |
| U5 | Defaults for a fresh save | A FAST, STEREO, SET / B same with SHIFT / C today's | A | [ui.md](decisions/ui.md) |
| L1 | Tone for each of the nine gym leaders' mid-battle lines | A in voice / B wry / C theatrical, per leader | `GRE B, HAC A, SAN A, HAG A, WAK A, TOB B, ASE A, SUZ A, MIZ A` | [trainer-slide-options/leaders.md](trainer-slide-options/leaders.md) |
| L2 | Tone for the Elite Four, Cynthia, the Commons and Crown bosses | A / B / C per battle | `OSSIAN A, HYACINTH A, DUNMORE A, DRAYDEN B, CYNTHIA A, TEDDY A, Crown leader A`, Mothwood officer optional | [trainer-slide-options/league.md](trainer-slide-options/league.md) |
| H1 | The Hoenn purge (remove unreachable Hoenn content) | `LEAVE` / `SKIP` (tag Hoenn maps as another region, frees about 1.2 MiB) / `DELETE`; add `FRLG` to also delete the 421 unbuilt FRLG map folders (no code edits, no ROM change) | LEAVE (optionally `LEAVE FRLG`): nothing the purge helps is near a limit | [arch.md](decisions/arch.md) |
| H2 | Will Aldermere reuse the Battle Frontier tower (7 maps)? Matters only if SKIP is chosen | yes / no / undecided | undecided is fine for LEAVE | [arch.md](decisions/arch.md) |
| W1 | Keep the new Route 1 sighting-farmer line for saves that reach Route 1 before Troglodyte is beaten? | keep ('Harvest is soon. I'm preparing by worrying a lot.') / drop / give him another | keep | this file |
| W2 | Greta's gym-invite line: the draft you approved ended 'Mind the gates. They swing both ways.'; the wired text says 'They only open for winners.' (changed when it was wired on 2026-10-08, never signed off, a gym leader line is a key beat) | keep the wired line / restore the approved line / a third wording | restore the approved line unless you like the new one | `data/maps/Crestfall/scripts.inc`, `design/dialogue/crestfall_scheme1.inc` |
| T1 | Run the 2-minute robot check before every ROM you test on the phone? | every ROM / only after script, flag, clock or encounter changes / only when asked | after script, flag, clock or encounter changes | [../design/tools/emu/README.md](tools/emu/README.md) |

## What is in each file

- [decisions/story.md](decisions/story.md): the small calls (Q1 to Q8) and the story and world calls still open in the game bible (starters, cities, house fights, tone).
- [decisions/battle.md](decisions/battle.md): five battle briefs. Each was tried in a throw-away lab build in mGBA (AI thinking time per rung, hard and soft level cap, boss boost message, a tag battle, a two-opponent battle). The lab patch is `decisions/prototypes/battle_lab.patch` (never merged).
- [decisions/ui.md](decisions/ui.md): five briefs with pictures in `decisions/img/` and the prototype patches in `decisions/prototypes/` (hold-R skip, config and defaults bundle, Crestfall light sprites). Two filler-NPC drafts for U2 are in `decisions/relearn_giver_lines_DRAFT.inc`.
- [decisions/arch.md](decisions/arch.md): the Hoenn purge brief (what Hoenn costs, three options measured in a scratch clone and run in the robot, a recommendation). The tested SKIP recipe is in `decisions/prototypes/hoenn-skip/`.
- [trainer-slide-options/](trainer-slide-options/): PROPOSED mid-battle lines for all nine gym leaders and for the Elite Four, Cynthia and the villain bosses, three tones each, every line measured with the game's own line breaker. Nothing is wired. To approve, tell me the letters; I paste the matching rows from the `*_COMMENTED.h` files into `src/data/veldris_trainer_slides.h`.

## Notes that apply to all briefs

- Facts marked 'ran' were run in mGBA, not on Delta (VBA-M) or Miyoo. Differences in timing or drawing are possible.
- A new game keeps the options of an old save: option defaults (U5) only show on a fresh save file.
- Nothing here changes the save layout. If an answer ever would, I tell you first (Delta save states break on every rebuild anyway, in-game saves keep working).
