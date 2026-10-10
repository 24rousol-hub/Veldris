Crestfall_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Crestfall_OnTransition
	.byte 0

Crestfall_OnTransition:
	setflag FLAG_VISITED_CRESTFALL
	setflag FLAG_TEMP_11
	call_if_ge VAR_CRESTFALL_STATE, 1, Crestfall_EventScript_SetAfterScheme
	end

@ After Scheme 1 the photographer stays by the noticeboard.
Crestfall_EventScript_SetAfterScheme::
	setobjectxyperm LOCALID_CRESTFALL_PHOTOGRAPHER, 17, 12
	setobjectmovementtype LOCALID_CRESTFALL_PHOTOGRAPHER, MOVEMENT_TYPE_FACE_DOWN
	return

Crestfall_EventScript_TownSign::
	msgbox Crestfall_Text_TownSign, MSGBOX_SIGN
	end

Crestfall_EventScript_GymSign::
	goto_if_eq VAR_CRESTFALL_STATE, 0, Crestfall_EventScript_GymClosedSign
	msgbox Crestfall_Text_GymSign, MSGBOX_SIGN
	end

Crestfall_EventScript_GymClosedSign::
	msgbox Crestfall_Text_S1_GymClosedSign, MSGBOX_SIGN
	end

Crestfall_EventScript_Noticeboard::
	goto_if_eq VAR_CRESTFALL_STATE, 0, Crestfall_EventScript_NoticeboardBefore
	msgbox Crestfall_Text_S1_Noticeboard, MSGBOX_SIGN
	end

Crestfall_EventScript_NoticeboardBefore::
	msgbox Crestfall_Text_NoticeboardBefore, MSGBOX_SIGN
	end

Crestfall_EventScript_Photographer::
	lock
	faceplayer
	goto_if_eq VAR_CRESTFALL_STATE, 0, Crestfall_EventScript_PhotographerBefore
	msgbox Crestfall_Text_PhotographerAfter, MSGBOX_DEFAULT
	release
	end

Crestfall_EventScript_PhotographerBefore::
	msgbox Crestfall_Text_S1_Photographer, MSGBOX_DEFAULT
	release
	end

Crestfall_EventScript_Local::
	lock
	faceplayer
	goto_if_eq VAR_CRESTFALL_STATE, 0, Crestfall_EventScript_LocalBefore
	msgbox Crestfall_Text_S1_LocalAfter, MSGBOX_DEFAULT
	release
	end

Crestfall_EventScript_LocalBefore::
	msgbox Crestfall_Text_S1_Local, MSGBOX_DEFAULT
	release
	end

Crestfall_EventScript_FarmSign::
	msgbox Crestfall_Text_FarmSign, MSGBOX_SIGN
	end

Crestfall_EventScript_Route2Sign::
	msgbox Crestfall_Text_Route2Sign, MSGBOX_SIGN
	end

Crestfall_EventScript_Route3Sign::
	msgbox Crestfall_Text_Route3Sign, MSGBOX_SIGN
	end

@ ===========================================================================
@ SCHEME 1, 'the private booking' (author approved the dialogue 2026-10-08)
@ coord_event on the tile in front of the gym door (20,10), VAR_CRESTFALL_STATE 0.
@ Hollis, Troglodyte and Greta are hidden by FLAG_TEMP_11 (set on every load) and spawned here.
@ Positions: Hollis stops at (19,10), the player is moved to (21,10), Troglodyte uses (20,10).
@ Losing the battle whites out with the state still 0, so the scene plays again.
@ ===========================================================================
Crestfall_EventScript_Scheme1::
	lockall
	addobject LOCALID_CRESTFALL_HOLLIS
	applymovement LOCALID_CRESTFALL_HOLLIS, Crestfall_Movement_HollisArrive
	waitmovement 0
	applymovement LOCALID_PLAYER, Common_Movement_FaceLeft
	waitmovement 0
	msgbox Crestfall_Text_S1_HollisStop, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Crestfall_Movement_PlayerStepAside
	waitmovement 0
	addobject LOCALID_CRESTFALL_TROG
	applymovement LOCALID_CRESTFALL_TROG, Crestfall_Movement_TrogArrive
	waitmovement 0
	msgbox Crestfall_Text_S1_TrogArrive, MSGBOX_DEFAULT
	msgbox Crestfall_Text_S1_HollisDoor, MSGBOX_DEFAULT
	closemessage
	opendoor 20, 9
	waitdooranim
	applymovement LOCALID_CRESTFALL_TROG, Crestfall_Movement_WalkIntoDoor
	waitmovement 0
	removeobject LOCALID_CRESTFALL_TROG
	applymovement LOCALID_CRESTFALL_PHOTOGRAPHER, Crestfall_Movement_PhotographerIn
	waitmovement 0
	removeobject LOCALID_CRESTFALL_PHOTOGRAPHER
	closedoor 20, 9
	waitdooranim
	applymovement LOCALID_CRESTFALL_HOLLIS, Common_Movement_FaceRight
	waitmovement 0
	msgbox Crestfall_Text_S1_HollisAside, MSGBOX_DEFAULT
	closemessage
	@ Greta's two-turn win happens off screen.
	fadescreen FADE_TO_BLACK
	delay 60
	fadescreen FADE_FROM_BLACK
	opendoor 20, 9
	waitdooranim
	setobjectxyperm LOCALID_CRESTFALL_PHOTOGRAPHER, 20, 9
	addobject LOCALID_CRESTFALL_PHOTOGRAPHER
	applymovement LOCALID_CRESTFALL_PHOTOGRAPHER, Crestfall_Movement_PhotographerOut
	applymovement LOCALID_PLAYER, Crestfall_Movement_PlayerWatchPhotographer
	waitmovement 0
	msgbox Crestfall_Text_S1_PhotographerOut, MSGBOX_DEFAULT
	closemessage
	addobject LOCALID_CRESTFALL_GRETA_OUTSIDE
	applymovement LOCALID_CRESTFALL_GRETA_OUTSIDE, Crestfall_Movement_StepOutOfDoor
	applymovement LOCALID_PLAYER, Common_Movement_FaceLeft
	waitmovement 0
	msgbox Crestfall_Text_S1_GretaDoor, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_CRESTFALL_GRETA_OUTSIDE, Crestfall_Movement_GretaStepDown
	waitmovement 0
	setobjectxyperm LOCALID_CRESTFALL_TROG, 20, 9
	addobject LOCALID_CRESTFALL_TROG
	applymovement LOCALID_CRESTFALL_TROG, Crestfall_Movement_StepOutOfDoor
	waitmovement 0
	closedoor 20, 9
	waitdooranim
	msgbox Crestfall_Text_S1_TrogToPlayer, MSGBOX_DEFAULT
	closemessage
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Crestfall_Text_S1_TrogBattleIntro, MSGBOX_DEFAULT
	trainerbattle_no_intro TRAINER_TROGLODYTE_CRESTFALL, Crestfall_Text_S1_TrogBattleDefeat
	msgbox Crestfall_Text_S1_TrogAfter, MSGBOX_DEFAULT
	msgbox Crestfall_Text_S1_HollisLeave, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_CRESTFALL_HOLLIS, Crestfall_Movement_HollisLeave
	applymovement LOCALID_CRESTFALL_TROG, Crestfall_Movement_TrogLeave
	waitmovement 0
	removeobject LOCALID_CRESTFALL_HOLLIS
	removeobject LOCALID_CRESTFALL_TROG
	applymovement LOCALID_CRESTFALL_PHOTOGRAPHER, Crestfall_Movement_PhotographerToBoard
	waitmovement 0
	msgbox Crestfall_Text_S1_PhotographerPin, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_CRESTFALL_GRETA_OUTSIDE, Crestfall_Movement_GretaStepUp
	waitmovement 0
	msgbox Crestfall_Text_S1_GretaInvite, MSGBOX_DEFAULT
	closemessage
	opendoor 20, 9
	waitdooranim
	applymovement LOCALID_CRESTFALL_GRETA_OUTSIDE, Crestfall_Movement_WalkIntoDoor
	waitmovement 0
	removeobject LOCALID_CRESTFALL_GRETA_OUTSIDE
	closedoor 20, 9
	waitdooranim
	setobjectmovementtype LOCALID_CRESTFALL_PHOTOGRAPHER, MOVEMENT_TYPE_FACE_DOWN
	setvar VAR_CRESTFALL_STATE, 1
	releaseall
	end

@ (14,10) to (19,10), facing the player on the door tile.
Crestfall_Movement_HollisArrive:
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

@ (20,10) to (21,10), then look back at the door tile.
Crestfall_Movement_PlayerStepAside:
	walk_right
	face_left
	step_end

@ (14,11) along the road to (20,11), up onto the door tile, then a glance at the player.
Crestfall_Movement_TrogArrive:
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_up
	face_right
	step_end

Crestfall_Movement_WalkIntoDoor:
	walk_up
	step_end

@ (23,11) to (20,11), then in through the door.
Crestfall_Movement_PhotographerIn:
	walk_left
	walk_left
	walk_left
	walk_up
	walk_up
	step_end

@ Out of the door to (20,11), then (21,11), under the player.
Crestfall_Movement_PhotographerOut:
	walk_down
	walk_down
	walk_right
	face_up
	step_end

Crestfall_Movement_PlayerWatchPhotographer:
	delay_16
	delay_16
	face_down
	step_end

Crestfall_Movement_StepOutOfDoor:
	walk_down
	face_right
	step_end

Crestfall_Movement_GretaStepDown:
	walk_down
	face_up
	step_end

Crestfall_Movement_GretaStepUp:
	walk_up
	face_right
	step_end

@ Both walk west along row 10, down the side of the square and off along the main road.
Crestfall_Movement_HollisLeave:
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_left
	walk_left
	walk_left
	step_end

Crestfall_Movement_TrogLeave:
	delay_16
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	walk_down
	walk_down
	walk_down
	walk_down
	walk_down
	walk_left
	walk_left
	step_end

@ (21,11) down to row 12 and west to (17,12), beside the noticeboard at (16,13).
Crestfall_Movement_PhotographerToBoard:
	walk_down
	walk_left
	walk_left
	walk_left
	walk_left
	face_down
	step_end

Crestfall_Text_TownSign:
	.string "CRESTFALL\n"
	.string "‘Harvest home of the honest.’$"

Crestfall_Text_GymSign:
	.string "CRESTFALL POKéMON GYM\n"
	.string "Leader: GRETA\p"
	.string "‘Normal is reliable.’$"

Crestfall_Text_FarmSign:
	.string "CRESTFALL FARM\n"
	.string "‘Pick your own. Pay on the\l"
	.string "honour system. We see you.’$"

Crestfall_Text_Route2Sign:
	.string "ROUTE 2\n"
	.string "EAST: WENDLEBURY$"

Crestfall_Text_Route3Sign:
	.string "ROUTE 3\n"
	.string "NORTH: BRIARWICK$"

Crestfall_Text_NoticeboardBefore:
	.string "CRESTFALL NOTICEBOARD\p"
	.string "‘Harvest fair next month.\n"
	.string "Bring your own basket.’$"

Crestfall_Text_PhotographerAfter:
	.string "The family wanted that photo\n"
	.string "gone. The town wanted it framed.\p"
	.string "I know who pays better. I know\n"
	.string "who I'd rather work for.$"

@ Scheme 1 lines, author approved 2026-10-08 (draft: design/dialogue/crestfall_scheme1.inc).
Crestfall_Text_S1_GymClosedSign::
	.string "CLOSED TODAY.\n"
	.string "Private session booked by the\l"
	.string "GOLDSWORTH family.\p"
	.string "Underneath, in pencil:\n"
	.string "‘Says who?’ - G.$"

@ The hired photographer, setting up a tripod outside the gym.
Crestfall_Text_S1_Photographer::
	.string "Don't mind me. I've been hired\n"
	.string "for a very important photo.\p"
	.string "‘The future Champion's first\n"
	.string "badge.’ Their words, not mine.\p"
	.string "I was told to bring the good\n"
	.string "lens. And a lot of flattery.$"

@ A local by the square.
Crestfall_Text_S1_Local::
	.string "Some rich family booked the\n"
	.string "whole gym. For one boy.\p"
	.string "My grandson's been waiting for\n"
	.string "a challenge since breakfast.$"

@ ===================================================================
@ REVEAL (coord trigger in front of the gym door)
@ ===================================================================

@ Hollis, the attendant, steps in front of the player. Gentle, apologetic, firm.
Crestfall_Text_S1_HollisStop::
	.string "Ah. Terribly sorry, young one.\n"
	.string "Might I ask you to step aside?\p"
	.string "The young master goes first.\n"
	.string "He always has, I'm afraid.$"

@ Troglodyte walks up. The player is moved aside (scripted step), Troglodyte barely notices.
Crestfall_Text_S1_TrogArrive::
	.string "HOLLIS. The door.\p"
	.string "Oh, it's you. Wait behind me.\n"
	.string "That's where people stand.$"

Crestfall_Text_S1_HollisDoor::
	.string "Of course, young master.\n"
	.string "Mind the step.$"

@ Hollis, to the player once Troglodyte is inside. Quietly.
Crestfall_Text_S1_HollisAside::
	.string "Forgive the manners. I served\n"
	.string "his father the very same way.\p"
	.string "Golden boys go first. It's how\n"
	.string "they were raised. And I raised\l"
	.string "a fair few of them.\p"
	.string "I don't expect this will take\n"
	.string "long. One way or another.$"

@ ===================================================================
@ COLLAPSE (after a short fade: Troglodyte comes back out)
@ ===================================================================

@ The photographer comes out first.
Crestfall_Text_S1_PhotographerOut::
	.string "Well. I got the shot.\p"
	.string "It's just not the shot they\n"
	.string "paid for.$"

@ Greta at the door.
Crestfall_Text_S1_GretaDoor::
	.string "Two turns. I didn't even get\n"
	.string "to stretch.\p"
	.string "Booking's over, by the way.\n"
	.string "My gym is open. To everyone.$"

@ ===================================================================
@ TROGLODYTE BATTLES THE PLAYER (his fight 2)
@ ===================================================================

Crestfall_Text_S1_TrogToPlayer::
	.string "That was a fluke. The light was\n"
	.string "wrong. The floor was wrong.\p"
	.string "You. You're going to help me\n"
	.string "prove it. Battle me. Now.$"

@ Battle window texts.
Crestfall_Text_S1_TrogBattleIntro::
	.string "Watch closely. This is how a\n"
	.string "Goldsworth wins! Go, {STR_VAR_2}!$"

Crestfall_Text_S1_TrogBattleDefeat::
	.string "No! That's two flukes in a row!\n"
	.string "That's not even possible!$"

Crestfall_Text_S1_TrogAfter::
	.string "This town is broken. The gym is\n"
	.string "broken. You are broken.\p"
	.string "HOLLIS! Bring the car round.\n"
	.string "And delete that photo.$"

Crestfall_Text_S1_HollisLeave::
	.string "Right away, young master.\p"
	.string "...You battle very well.\n"
	.string "Please don't tell him I said so.$"

@ ===================================================================
@ HUMILIATION (the noticeboard by the square, from now on)
@ ===================================================================

@ The photographer pins the photo up as the car leaves.
Crestfall_Text_S1_PhotographerPin::
	.string "The family didn't want this\n"
	.string "photo. The town, however...\p"
	.string "There. Best work I've done\n"
	.string "all year.$"

@ The noticeboard (bg event), for the rest of the game.
Crestfall_Text_S1_Noticeboard::
	.string "CRESTFALL NOTICEBOARD\p"
	.string "A photo of a rich boy mid-yell,\n"
	.string "his POKéMON fainted at his feet.\p"
	.string "Someone has written underneath:\n"
	.string "‘The future Champion.’$"

@ A local after the scheme.
Crestfall_Text_S1_LocalAfter::
	.string "Did you see the photo? Framed\n"
	.string "it'd look lovely in the inn.\p"
	.string "My grandson finally got his\n"
	.string "challenge. Lost, mind. Happily.$"

@ ===================================================================
@ GRETA lines that mentioned the old scheme (replacements)
@ ===================================================================

@ Replaces GretaAfterTrog: she sends the player in.
Crestfall_Text_S1_GretaInvite::
	.string "That's him sorted. For about\n"
	.string "a week, I'd guess.\p"
	.string "Come on in, {PLAYER}. Mind the\n"
	.string "gates. They only open for winners.$"
