@ ===========================================================================
@ DRAFT, UNBUILT, not included in data/event_scripts.s.
@ Status: PROPOSED. Hand-written scripts.inc style (NOT Poryscript).
@
@ Hollowbrook_ProfFennickLab: Prof. Fennick's lab and the Troglodyte starter scene.
@ Paste into data/maps/Hollowbrook_ProfFennickLab/scripts.inc once the map is built in
@ Porymap. Needs hollowbrook_scripts.inc too (it defines the shared helper
@ Hollowbrook_EventScript_BufferTrogSpecies, called from here).
@
@ TEXT: labels come from design/dialogue/hollowbrook.inc. Append these to the lab's
@ scripts.inc (each label exactly once in the build):
@   AideNervous, AideDeadpan, AideNervousAfter, AideDeadpanAfter,
@   LabTrogScene1..6, LabTrogTakes, LabTrogSneer, LabTrogLeaves,
@   LabApology1..3, LabBallAsk, LabBallChosen, LabAfterChoice,
@   FennickIdleAfter, FennickIdleAfter2, LabBookshelf, LabComputer.
@ NEW text labels added at the bottom of THIS file (not in the dialogue draft; widths
@ checked with design/tools/dialogue_check.py): Hollowbrook_Text_LabExitBlocked,
@ Hollowbrook_Text_LabBallGone. Move them into dialogue/hollowbrook.inc if kept.
@
@ PLACEHOLDER FLAGS AND VARS (proposed names, NOT claimed; see design/scripts/README.md):
@   VAR_HOLLOWBROOK_STATE  0 new game, 1 mom woke player, 2 scene running/choosing,
@                          3 starter chosen, 4 Trog beaten outside (set in the town file)
@   VAR_TROG_STARTER       ALREADY CLAIMED (0x40F7): Troglodyte's pick, 0/1/2
@   VAR_STARTER_MON        existing vanilla var: the PLAYER's starter (0/1/2, see note)
@   FLAG_HIDE_HOLLOWBROOK_LAB_TROG       Troglodyte in the lab hidden (set when he leaves)
@   FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1..4  the four Poke Ball objects hidden
@   Existing vanilla: FLAG_SYS_POKEMON_GET, FLAG_ADVENTURE_STARTED, FLAG_HIDE_* via the
@   object events' flag field.
@   Also cleared here: FLAG_HIDE_HOLLOWBROOK_GRANDPA (defined in the town file).
@
@ PLACEHOLDER LOCAL IDS (object local_id in Porymap):
@   LOCALID_HOLLOWBROOK_LAB_FENNICK, _TROG, _AIDE_1, _AIDE_2,
@   LOCALID_HOLLOWBROOK_LAB_BALL_1 .. _BALL_4 (ball 4 placed on the table like the
@   others; it starts hidden, see OnTransition).
@
@ MAP EVENTS TO PLACE in Porymap (elevation 3, tile must be walkable):
@   coord_event (trigger), tile just inside the door, TWO rows of entries, one per
@     var_value 0 and 1 (so the scene also fires if the player skips mom):
@       var VAR_HOLLOWBROOK_STATE, var_value 0 and 1,
@       script Hollowbrook_ProfFennickLab_EventScript_TrogScene
@   coord_event on each door-side tile: var VAR_HOLLOWBROOK_STATE, var_value 2,
@       script Hollowbrook_ProfFennickLab_EventScript_ExitBlocker
@   Four Poke Ball object events (graphic = vanilla ball) with scripts Ball1 to Ball4
@   and flags FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1..4. Table must be 4 tiles wide with a free
@   tile in front of each ball (design/story-outline.md, 'The lab map has to support it').
@
@ ASSUMED LAYOUT (TODO(coords), rewrite the movements below once the map exists):
@   balls on the table row in a line, ball k reachable from the tile below it;
@   Troglodyte starts 1 tile below and left of ball 1; player enters from the door
@   and walks 2 tiles up to the trigger row.
@
@ SPECIES are Emerald stand-ins (Treecko/Torchic/Mudkip) until the author picks real
@ starters (story-outline.md). Ball order = Tag6/Tag7/Tag8 order in trainers.party.
@ ===========================================================================

Hollowbrook_ProfFennickLab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Hollowbrook_ProfFennickLab_OnTransition
	.byte 0

@ The fourth ball is revealed mid-scene, so it must start hidden. Doing it here avoids
@ editing EventScript_ResetAllMapFlags (an engine file).
Hollowbrook_ProfFennickLab_OnTransition:
	call_if_lt VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_ProfFennickLab_EventScript_HideBall4
	end

Hollowbrook_ProfFennickLab_EventScript_HideBall4::
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	return

@ ===========================================================================
@ THE TROGLODYTE SCENE (coord_event trigger, state 0 or 1)
@ Order (dialogue/hollowbrook.inc): Troglodyte rants -> Fennick spots the player ->
@ Troglodyte dismisses -> he demands one -> Fennick gives in -> random pick
@ (random 3) -> he takes it and leaves -> Fennick apologises -> ball 4 appears ->
@ the player chooses from what is left.
@ ===========================================================================

Hollowbrook_ProfFennickLab_EventScript_TrogScene::
	lockall
	applymovement LOCALID_PLAYER, Hollowbrook_ProfFennickLab_Movement_PlayerWalkIn
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene1, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene2, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene3, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene4, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene5, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene6, MSGBOX_DEFAULT
	closemessage
	@ His random pick: VAR_RESULT is 0, 1 or 2. VAR_TROG_STARTER is read later by the
	@ trainer pool prune (src/trainer_pools.c) in every Troglodyte battle.
	random 3
	copyvar VAR_TROG_STARTER, VAR_RESULT
	call Hollowbrook_EventScript_BufferTrogSpecies
	switch VAR_TROG_STARTER
	case 0, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall1
	case 1, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall2
	case 2, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall3
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall1::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall1
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_1
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	goto Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall2::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall2
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	goto Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall3::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall3
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_3
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	goto Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	end

@ Common tail. {STR_VAR_2} is already buffered with his species.
Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall::
	playse SE_PIN
	msgbox Hollowbrook_Text_LabTrogTakes, MSGBOX_DEFAULT
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogSneer, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogLeaves
	waitmovement 0
	@ TODO(coords): opendoor/closedoor x, y on the lab's door tile if it has a door animation.
	playse SE_DOOR
	removeobject LOCALID_HOLLOWBROOK_LAB_TROG
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_TROG
	delay 30
	msgbox Hollowbrook_Text_LabTrogLeaves, MSGBOX_DEFAULT
	@ Until the player picks a ball the exit is blocked (see ExitBlocker).
	setvar VAR_HOLLOWBROOK_STATE, 2
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabApology1, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabApology2, MSGBOX_DEFAULT
	closemessage
	@ The fourth ball appears. (It is a placed object that starts hidden; addobject after
	@ clearing its flag shows it, the same pattern as vanilla's starter table.)
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	addobject LOCALID_HOLLOWBROOK_LAB_BALL_4
	playse SE_PIN
	delay 30
	msgbox Hollowbrook_Text_LabApology3, MSGBOX_DEFAULT
	@ The old man appears on the bench from now on (hide flag lives in the town file).
	clearflag FLAG_HIDE_HOLLOWBROOK_GRANDPA
	releaseall
	end

@ TODO(coords): player walks 2 tiles in from the door to the trigger row.
Hollowbrook_ProfFennickLab_Movement_PlayerWalkIn:
	walk_up
	walk_up
	step_end

@ TODO(coords): Troglodyte to the tile below ball k, then face the ball (up). With the
@ assumed layout he starts below-left of ball 1, so ball k costs k walk_right steps.
Hollowbrook_ProfFennickLab_Movement_TrogToBall1:
	walk_right
	face_up
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogToBall2:
	walk_right
	walk_right
	face_up
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogToBall3:
	walk_right
	walk_right
	walk_right
	face_up
	step_end

@ TODO(coords): from wherever he stands (below his ball) to the door.
Hollowbrook_ProfFennickLab_Movement_TrogLeaves:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	step_end

@ While state is 2 the player may not leave without a starter.
Hollowbrook_ProfFennickLab_EventScript_ExitBlocker::
	lockall
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabExitBlocked, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Hollowbrook_ProfFennickLab_Movement_StepBackIn
	waitmovement 0
	releaseall
	end

Hollowbrook_ProfFennickLab_Movement_StepBackIn:
	walk_up
	step_end

@ ===========================================================================
@ THE FOUR POKE BALLS. Ball k (object event) runs BallK. Flow per ball:
@   buffer name -> show picture -> Yes/No -> (No: close) -> givemon -> party or PC ->
@   remove the ball -> nickname -> set VAR_STARTER_MON and the flags -> Fennick's thanks.
@ VAR_STARTER_MON: balls 1 to 3 store their index (0, 1, 2) like vanilla. Ball 4
@ stores 0 for now, because GetStarterPokemon(3) in src/starter_choose.c would read
@ past sStarterMon[3] (its guard is '>' not '>='). See README open questions.
@ VAR_0x8008 carries the ball number 1..4 into the shared tail.
@ ===========================================================================

Hollowbrook_ProfFennickLab_EventScript_Ball1::
	lockall
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	setvar VAR_0x8008, 1
	bufferspeciesname STR_VAR_1, SPECIES_TREECKO
	showmonpic SPECIES_TREECKO, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_TREECKO
	setvar VAR_STARTER_MON, 0
	givemon SPECIES_TREECKO, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_Ball2::
	lockall
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	setvar VAR_0x8008, 2
	bufferspeciesname STR_VAR_1, SPECIES_TORCHIC
	showmonpic SPECIES_TORCHIC, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_TORCHIC
	setvar VAR_STARTER_MON, 1
	givemon SPECIES_TORCHIC, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_Ball3::
	lockall
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	setvar VAR_0x8008, 3
	bufferspeciesname STR_VAR_1, SPECIES_MUDKIP
	showmonpic SPECIES_MUDKIP, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_MUDKIP
	setvar VAR_STARTER_MON, 2
	givemon SPECIES_MUDKIP, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

@ The fourth starter. SPECIES_TBD4 is a PLACEHOLDER: the author has not chosen it.
@ Replace all four occurrences with the real species constant.
Hollowbrook_ProfFennickLab_EventScript_Ball4::
	lockall
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	setvar VAR_0x8008, 4
	bufferspeciesname STR_VAR_1, SPECIES_TBD4
	showmonpic SPECIES_TBD4, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_TBD4
	setvar VAR_STARTER_MON, 0
	givemon SPECIES_TBD4, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_BallDeclined::
	hidemonpic
	releaseall
	end

@ After the choice, the two leftover balls stay on the table but are not for taking.
Hollowbrook_ProfFennickLab_EventScript_BallGone::
	msgbox Hollowbrook_Text_LabBallGone, MSGBOX_DEFAULT
	releaseall
	end

@ Shared tail. VAR_RESULT still holds givemon's answer here.
Hollowbrook_ProfFennickLab_EventScript_BallGiven::
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PARTY, Hollowbrook_ProfFennickLab_EventScript_ChosenToParty
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PC, Hollowbrook_ProfFennickLab_EventScript_ChosenToPC
	hidemonpic
	goto Common_EventScript_NoMoreRoomForPokemon
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenToParty::
	call Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice
	call Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	goto Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenToPC::
	call Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice
	call Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred
	call Common_EventScript_NameReceivedBoxMon
	goto Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred::
	call Common_EventScript_TransferredToPC
	goto Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	end

Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice::
	playfanfare MUS_OBTAIN_ITEM
	message Hollowbrook_Text_LabBallChosen
	waitmessage
	waitfanfare
	return

@ Hides the ball the player took (object and flag).
Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall::
	switch VAR_0x8008
	case 1, Hollowbrook_ProfFennickLab_EventScript_TakeBall1
	case 2, Hollowbrook_ProfFennickLab_EventScript_TakeBall2
	case 3, Hollowbrook_ProfFennickLab_EventScript_TakeBall3
	case 4, Hollowbrook_ProfFennickLab_EventScript_TakeBall4
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall1::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_1
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall2::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall3::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_3
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall4::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_4
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	return

@ State 3 lets Troglodyte appear outside and unblocks the door. SYS_POKEMON_GET turns
@ on the POKeMON menu; ADVENTURE_STARTED is what vanilla sets after the starter
@ (Pokedex/Pokenav handout is NOT covered here: Fennick gives no Pokedex in the draft).
Hollowbrook_ProfFennickLab_EventScript_ChoiceDone::
	hidemonpic
	setvar VAR_HOLLOWBROOK_STATE, 3
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_ADVENTURE_STARTED
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabAfterChoice, MSGBOX_DEFAULT
	releaseall
	end

@ ===========================================================================
@ LAB NPCs AND FURNITURE
@ ===========================================================================

@ Aides: before the choice (state under 3) and after. The 'after' lines use {STR_VAR_2}
@ for Troglodyte's species, so buffer it first.
Hollowbrook_ProfFennickLab_EventScript_AideNervous::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_AideNervousAfter
	msgbox Hollowbrook_Text_AideNervous, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideNervousAfter::
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Hollowbrook_Text_AideNervousAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideDeadpan::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_AideDeadpanAfter
	msgbox Hollowbrook_Text_AideDeadpan, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideDeadpanAfter::
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Hollowbrook_Text_AideDeadpanAfter, MSGBOX_DEFAULT
	release
	end

@ Fennick by state. He has no 'before' line (the scene fires on entry). While the player
@ is still choosing (state 2) he repeats the invitation. State 3: IdleAfter. State 4 and
@ up (Troglodyte beaten outside): IdleAfter2, the 'repeat visit' line.
Hollowbrook_ProfFennickLab_EventScript_Fennick::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 4, Hollowbrook_ProfFennickLab_EventScript_FennickRepeat
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_FennickAfter
	msgbox Hollowbrook_Text_LabApology3, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_FennickAfter::
	msgbox Hollowbrook_Text_FennickIdleAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_FennickRepeat::
	msgbox Hollowbrook_Text_FennickIdleAfter2, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_Bookshelf::
	msgbox Hollowbrook_Text_LabBookshelf, MSGBOX_SIGN
	end

Hollowbrook_ProfFennickLab_EventScript_Computer::
	msgbox Hollowbrook_Text_LabComputer, MSGBOX_SIGN
	end

@ ===========================================================================
@ NEW TEXT (not in design/dialogue/hollowbrook.inc yet)
@ ===========================================================================

Hollowbrook_Text_LabExitBlocked::
	.string "Oh, please don't leave yet.\n"
	.string "Choose one of the POKéMON first.$"

Hollowbrook_Text_LabBallGone::
	.string "The other POKé BALLS are not\n"
	.string "for taking. Nice try.$"
