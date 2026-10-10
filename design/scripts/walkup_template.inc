@ ===========================================================================
@ TEMPLATE, not included in data/event_scripts.s (same status as the other files in design/scripts).
@ An ordinary NPC that spots the player, shows '!', walks up and talks. No battle.
@
@ Status: TESTED. Variants A, B and C below were instantiated word for word in a scratch clone and
@ run in the emulator on 2026-10-10. Test log, traps and limits: design/npc-walkup.md.
@
@ HOW TO USE
@  1. Pick variant A, B or C. Copy its object event (map.json) and its script block.
@  2. Rename Map_ to the map's label prefix (for example VeldrisRoute1_), Walker to the NPC's name.
@     LOCALID_MAP_WALKER must be unique across ALL maps (CLAUDE.md, Engine rules).
@  3. Claim the flag(s): rename a FLAG_UNUSED_0x... in include/constants/flags.h and log it
@     (design/flags.md rule 5). Write the text (voice rules in design/dialogue-style.md), then run
@     python3 design/tools/dialogue_check.py on the file.
@  4. Close Porymap before you edit map.json, and reload it afterwards.
@  5. Read the traps in design/npc-walkup.md first, above all: no step trigger (coord_event or door) inside
@     the NPC's sight line, sight range 7 at most, movement_type FACE_* only, and nothing visible in a
@     'done' branch.
@
@ map.json object event for A and B (the NPC stays on the map). `movement_type` is the way he looks,
@ `trainer_sight_or_berry_tree_id` is how many tiles he sees in that direction (0 = never sees anything):
@
@   {
@     "local_id": "LOCALID_MAP_WALKER",
@     "graphics_id": "OBJ_EVENT_GFX_...",
@     "x": 0, "y": 0, "elevation": 3,
@     "movement_type": "MOVEMENT_TYPE_FACE_RIGHT",
@     "movement_range_x": 0, "movement_range_y": 0,
@     "trainer_type": "TRAINER_TYPE_NORMAL",
@     "trainer_sight_or_berry_tree_id": "5",
@     "script": "Map_EventScript_WalkerTalks",
@     "flag": "0"
@   }
@
@ For a NPC that watches all four directions use "trainer_type": "TRAINER_TYPE_SEE_ALL_DIRECTIONS".
@ ===========================================================================


@ ======== VARIANT A: talks again when the player speaks to him afterwards (the default choice) ========
@ cant_see_if_set is upstream's own switch for this (asm/macros/event.inc): while the game looks ahead to
@ decide whether the NPC sees the player it ends the script there, and when the player talks to him it
@ does nothing. So the After branch may show text.

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

Map_Text_WalkerFirst:
	.string "First line, when he walks up.$"

Map_Text_WalkerAfter:
	.string "Line when the player talks to him later.$"


@ ======== VARIANT B: says nothing when the player speaks to him afterwards ========
@ The guard is the first command, and its 'done' label is only `end`. Nothing visible may ever be added
@ to that branch (a msgbox there makes him walk up and talk again, forever; see the traps).

Map_EventScript_WalkerSilent::
	goto_if_set FLAG_MAP_WALKER_DONE, Map_EventScript_WalkerSilentDone
	lock
	faceplayer
	msgbox Map_Text_WalkerSilentFirst, MSGBOX_DEFAULT
	setflag FLAG_MAP_WALKER_DONE
	release
	end

Map_EventScript_WalkerSilentDone::
	end

Map_Text_WalkerSilentFirst:
	.string "First line, when he walks up.$"


@ ======== VARIANT C: talks, walks away and is gone for good ========
@ Use this where he would block a path, or for a drive-by. The object event's "flag" is the hide flag:
@   "script": "Map_EventScript_WalkerLeaves", "flag": "FLAG_HIDE_MAP_WALKER"
@ and FLAG_HIDE_MAP_WALKER must be CLEAR at the start. One flag does everything: once it is set the NPC
@ is not created at all, so he cannot spot the player again. The walk goes the way he came (opposite to his
@ facing); change walk_up to match (walk_left for a NPC that looks right, and so on).

Map_EventScript_WalkerLeaves::
	lock
	faceplayer
	msgbox Map_Text_WalkerLeaves, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_MAP_WALKER, Map_Movement_WalkerLeaves
	waitmovement 0
	removeobject LOCALID_MAP_WALKER
	setflag FLAG_HIDE_MAP_WALKER
	release
	end

Map_Movement_WalkerLeaves:
	walk_up
	walk_up
	walk_up
	step_end

Map_Text_WalkerLeaves:
	.string "Line before he leaves.$"
