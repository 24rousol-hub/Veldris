# NPC walk-up and talk

Status: **BUILT in a scratch clone and TESTED in the emulator robot, 2026-10-10** (author, 2026-10-08: 'NPC walk and talk looks great in theory'). Nothing is in the game yet: the test map was 26 throwaway NPCs on Route 1 of a clone that has been deleted. The recipe below works as written, the old one needed two fixes (see 'What changed'). Copy-paste file: [scripts/walkup_template.inc](scripts/walkup_template.inc) (its three scripts were run word for word). Optional checker: `design/tools/walkup_lint.py` (not wired into any hook).

## What it does

An ordinary NPC sees the player step into his line of sight, shows the '!' icon for about a second, walks up to the player, turns to face the player and talks. No battle. It is the trainer-approach machinery with a script that is not a `trainerbattle`. Measured at normal speed: '!' 1.0 s, then 0.25 to 0.3 s per tile walked, then the text. A 5-tile approach takes about 3 s before the first line.

After the scene the NPC stands next to the player, still looking the way he walked, and stays there until the map is loaded again (then he is back on his starting tile).

## Recipe (variant A, the default)

1. **`map.json`, object event** (close Porymap first, rule 2 in [CLAUDE.md](../CLAUDE.md); in Porymap the fields are Movement, Trainer Type, Sight Radius and Script):

```
{ "local_id": "LOCALID_MAP_WALKER", "graphics_id": "OBJ_EVENT_GFX_...", "x": 0, "y": 0, "elevation": 3,
  "movement_type": "MOVEMENT_TYPE_FACE_RIGHT", "movement_range_x": 0, "movement_range_y": 0,
  "trainer_type": "TRAINER_TYPE_NORMAL", "trainer_sight_or_berry_tree_id": "5",
  "script": "Map_EventScript_WalkerTalks", "flag": "0" }
```

`movement_type` is the way he looks (`FACE_*` only). `trainer_sight_or_berry_tree_id` is how many tiles he sees in that direction (see the range limits below). For an NPC who watches all four ways use `TRAINER_TYPE_SEE_ALL_DIRECTIONS` (tested: he turns towards the player first).

2. **`scripts.inc`**, upstream's own guard `cant_see_if_set` first (macro in `asm/macros/event.inc`):

```
Map_EventScript_WalkerTalks::
	cant_see_if_set FLAG_MAP_WALKER_DONE
	goto_if_set FLAG_MAP_WALKER_DONE, Map_EventScript_WalkerTalksAfter
	lock
	faceplayer
	msgbox Map_Text_WalkerFirst, MSGBOX_DEFAULT
	setflag FLAG_MAP_WALKER_DONE
	release
	end

Map_EventScript_WalkerTalksAfter::
	msgbox Map_Text_WalkerAfter, MSGBOX_NPC
	end
```

3. Claim the flag (rename a `FLAG_UNUSED_0x...`, `design/flags.md` rule 5), write the text (`dialogue_check.py`), keep `LOCALID_..._WALKER` unique across all maps.

**Variants** (all three are in the template and were run): **A** talks again when spoken to later. **B** says nothing later: `goto_if_set FLAG, Done` first, and `Done::` is only `end` (this is the old recipe, it works). **C** talks, walks away and is gone for good: the object's `flag` field is a hide flag, the script finishes with `applymovement`, `waitmovement 0`, `removeobject` and `setflag <hide flag>`; one flag does everything and he can never see the player again. Use C when he would block a path.

## How it works (what the code does)

- `CheckForTrainersWantingBattle` (`src/trainer_see.c`) runs **every frame the player has control**, first thing in `ProcessPlayerFieldInput`. For each active object with `TRAINER_TYPE_NORMAL` or `SEE_ALL_DIRECTIONS` it asks: is the player on a tile (the one he is **moving into**) within range in the NPC's facing direction, with nothing in between? Walls, other objects, ledges and elevation differences all block the line.
- If yes, it **runs his script ahead of time without showing anything** (`RunScriptImmediatelyUntilEffect` in `src/script.c`) until the first command that shows something or writes the save (`lock`, `faceplayer`, `msgbox`, `setflag`, `setvar`, `applymovement` ...). If that command is a `trainerbattle` he is an ordinary trainer. If it is anything else he counts as a 'non-battle approach': '!' icon, walk to the player (`DoTrainerApproach`), player turns to face him, then **his script runs from the first line** (`LoadTrainerObjectScript`). `gSelectedObjectEvent` and `VAR_LAST_TALKED` are set to him, so `removeobject VAR_LAST_TALKED` works.
- If the look-ahead reaches an `end` without showing anything, nothing happens. That is what the guard is for. `cant_see_if_set FLAG` is the engine's own way to say it: during the look-ahead it ends the script right there, and when the player talks to the NPC it does nothing, so the 'after' branch may show text. Variant B gets the same effect with a `goto` to a label that is only `end`. A third form also worked in the test (`goto_if_eq VAR_LAST_TALKED, LOCALID_NONE, Silent` in the done branch, because `VAR_LAST_TALKED` is 0 during the look-ahead) but is not needed now.
- Order each frame: the walk-up check, then `MAP_SCRIPT_ON_FRAME_TABLE`, then (only on a finished step) coord events and warps, then wild encounters. So a walk-up scene takes a step away from anything that waits for a step.

## Test log (2026-10-10, mGBA through the robot, scratch Route 1)

| # | Test | Result |
|---|---|---|
| 1 | Player steps into the line 6 tiles away, NPC sight 5 | Nothing happens |
| 2 | Same, 5 tiles away | The NPC sees the player on the first frame of the step (the step still finishes), '!' 1.0 s, walks 4 tiles, player turns to face him, text once, flag set, player free. NPC ends next to the player, facing the way he walked |
| 3 | Leave the line and cross it again after the scene (A, B, and the `VAR_LAST_TALKED` trick) | No new scene |
| 4 | Press A on the NPC afterwards | B: nothing at all, player not locked. A: 'after' line shown |
| 5 | **Bad variant**: a `msgbox` in the done branch | Endless loop: '!', text, '!', text ... at least 10 times in 25 s, the player can never leave |
| 6 | Step into the line right next to the NPC | '!', no walking, he faces the player, text |
| 7 | Player standing in the line with the flag set, flag cleared (a script, a debug poke) | The NPC fires within one frame, without the player moving |
| 8 | Arrive by warp on a tile inside the line, flag clear | Fade-in, then about 0.5 s later '!' and the walk-up |
| 9 | `SEE_ALL_DIRECTIONS` NPC looking down, player to his east | He turns east, '!', walks 2 tiles, text |
| 10 | **`coord_event` on the first tile of the line** (var guard clear) | The walk-up wins. The trigger did **not** run (its var stayed 0). Stepping off and on again ran it |
| 11 | Same tile, NPC already done | The trigger runs normally |
| 12 | Two walkers see the player on the same step | One after the other, lower local id first; the second '!' comes right after the first text |
| 13 | A real trainer and a walker share a tile, **walker listed first**, party of 1 and of 2 | Clean: the walker's scene, then the trainer walks up, his intro, the battle |
| 14 | Same, **trainer listed first**, party of 1 | The trainer alone; the walker is not even looked at (the code stops after one trainer when the player cannot do a double battle) |
| 15 | Same, trainer listed first, **2 usable Pokémon** | Messy: the trainer does the '!' and the walk, the walker's text then plays from where he stands (3 tiles away, facing the wrong way), then the trainer's '!' again and the battle. An idle `Task_RunTrainerSeeFuncList` is left behind. It resolves, but do not build it |
| 16 | Another NPC stands in the line between them | No trigger |
| 17 | Talk to the NPC from behind before he has seen the player | The script runs from the top, he turns round to the player, flag set, he stays turned |
| 18 | Script walks him 2 tiles away, then leave and re-enter the map | Back on his starting tile (the header position). The approach position is not kept across a map load |
| 19 | Script does `setflag HIDE`, `removeobject VAR_LAST_TALKED` | Gone, stays gone after a map load, no new scene in the old line |
| 20 | Player on the Acro bike | Same as on foot; the bike stays on |
| 21 | Player running (shoes) into the line | Same; he is caught on the first tile of the line, as when walking |
| 22 | **Real save, restart, Continue** (`special SaveGame`, new emulator) | Flag kept, a walker who had walked up is still on his new tile, no new scene, the 'after' line works |
| 23 | Sight 10, player walking towards him from far away | He does not exist until the player is 10 tiles away, then he fires at once (see limits) |
| 24 | NPC made invisible (still active) | He still sees the player and walks up, unseen, with the '!' showing |
| 25 | The three template variants, instantiated word for word | All pass (approach, no re-trigger, after-line, walk away and gone) |
| 26 | `MAP_SCRIPT_ON_FRAME_TABLE` becomes due during the walk-up | It waits, then runs after the scene |
| 27 | Crowded map (about 26 NPCs on one map) | At most 15 NPCs exist at once; an NPC listed late was not created until others left the window (he popped in 2 tiles away instead of 7) |

Evidence: [art/npc-walkup-exclamation.png](art/npc-walkup-exclamation.png) shows the '!' over the NPC 5 tiles away (game frozen at that moment).

## Traps (all found or confirmed in the test)

- **The done branch must show nothing.** Use `cant_see_if_set` (A) or a label that is only `end` (B). Never a `msgbox`, `lock`, `setflag` there: he walks up again every time (test 5). Also never forget to set the flag before `release`.
- **A step trigger inside his sight line is swallowed on the first step** (test 10). A `coord_event` tile there does not run until the player steps off and on again, so the cutscene is silently skipped if the tile is only stepped on once. Warps and doors use the same code (`TryStartStepBasedScript`), expect the same (not run: a plain tile has no warp behaviour). Keep trigger, warp and door tiles out of his line, or build that scene as `MAP_SCRIPT_ON_FRAME_TABLE` (test 26), or make the walk-up itself the scene. `walkup_lint.py` finds this.
- **Sight range and the screen.** The NPC only exists inside a window around the player: 9 tiles left, **10 right, 7 above, 9 below** (measured right, above and below; left read from `TrySpawnObjectEvents`). A longer range cannot fire earlier, he pops in and fires at once. The screen shows 7 tiles left and right, 4 above and 5 below, so keep the range at **7 sideways, 4 when he looks down, 5 when he looks up** and the '!' is on screen. Range 0 means he never sees anything.
- **At most 15 NPCs at once** (16 object slots, one is the player; shadows can cost sprites too, `design/engine-limits.md`). In a crowded map a walker listed late may not exist yet. Vanilla-sized maps (8 to 10 NPCs) are fine.
- **`movement_type` must be `FACE_*`.** The line follows his facing and the engine sets `FACE_*` on him after the walk, so a wanderer stops wandering until the map is loaded again (code reading; wanderers are also held still while the player runs close, `ObjectEventIsTrainerAndCloseToPlayer`).
- **He stays where he stopped**, next to the player, for the rest of the visit. In a one-tile path that blocks the way: use variant C or `applymovement` him aside. Moves made by the script are lost on the next map load (test 18); if he has to be somewhere else afterwards, use a flag and a second object.
- **Do not share a tile of two lines with a real trainer unless the walker is listed first** in `map.json` (the order is the local id order, the check goes by id). Tests 12 to 15.
- **Invisible is not gone.** `hideobjectat` or an invisible sprite keeps him active and he still walks up (test 24). Hide him with `removeobject` plus a hide flag.
- **A flag that flips while the player stands in the line fires within a frame** (test 7). A cutscene that clears the flag with the player in the line will start the walk-up at once.
- **`faceplayer` turns him to the direction opposite to the way the player faces**, not towards the player's tile. Fine next to the player, wrong from a distance (test 15).
- `lock` / `faceplayer` / `release`, as for any NPC; `lockall` is not needed. `MSGBOX_NPC` already contains all three. A sight line never crosses into a connected map (code reading: their NPCs are not loaded). The walk-up has no encounter music, only the '!'.

## Not tested

Surfing (no water on the test map; by code a land NPC cannot see a player on a water tile, elevation mismatch), a warp or door tile in the line (a plain tile does not warp), a save in the middle of the approach (not possible, the menu is locked), Delta (VBA-M based; the robot runs mGBA), the VS Seeker (`I_VS_SEEKER_CHARGING` is 0; if it is ever switched on, test a walker with it).

## What changed from the first draft

- The first draft recommended `goto_if_set ... Done` with an empty Done branch and a second NPC for an 'after' line. Upstream's `cant_see_if_set` does it in one NPC and is now the default (variant A). The old form still works (variant B).
- New traps: step triggers in the line (10), the spawn window and the 15-NPC cap (23, 27), trainer and walker on one tile (13 to 15), the NPC's position after the scene (2, 18), invisible NPCs (24).
- Nothing in the engine needs changing, no upstream file is edited.

## Good uses

Troglodyte's drive-by insults on routes, a Goldsworth footman handing over a 'gift', a villager who simply must tell the player something. An NPC who talks and then **fights** is just a normal trainer: his intro text is the talk, no walker needed. For key story beats (Troglodyte's fights, Goldsworth schemes) the author approves the wording first (rule 10).
