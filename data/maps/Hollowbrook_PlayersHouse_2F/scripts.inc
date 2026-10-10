Hollowbrook_PlayersHouse_2F_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Hollowbrook_PlayersHouse_2F_OnTransition
	.byte 0

@ A new game starts in this room at state 0: the first respawn point is Hollowbrook. Set once, here, never on every entry to the
@ town (that would pull a player back home after any visit, over a later Pokémon Center; found by the 2026-10-09 review).
Hollowbrook_PlayersHouse_2F_OnTransition:
	call_if_eq VAR_HOLLOWBROOK_STATE, 0, Hollowbrook_PlayersHouse_2F_EventScript_SetRespawn
	end

Hollowbrook_PlayersHouse_2F_EventScript_SetRespawn::
	setrespawn HEAL_LOCATION_HOLLOWBROOK
	return

Hollowbrook_PlayersHouse_2F_EventScript_PC::
	lockall
	setvar VAR_0x8004, PC_LOCATION_VELDRIS_HOME
	special DoPCTurnOnEffect
	playse SE_PC_ON
	msgbox gText_PlayerHouseBootPC, MSGBOX_DEFAULT
	special BedroomPC
	releaseall
	end

Hollowbrook_PlayersHouse_2F_EventScript_TurnOffPlayerPC::
	setvar VAR_0x8004, PC_LOCATION_VELDRIS_HOME
	playse SE_PC_OFF
	special DoPCTurnOffEffect
	releaseall
	end

Hollowbrook_PlayersHouse_2F_EventScript_Notebook::
	msgbox Hollowbrook_PlayersHouse_2F_Text_Notebook, MSGBOX_SIGN
	end

@ The TV on the back wall (signs at (7,2) and (8,2), added 2026-10-09). One line, no flags.
Hollowbrook_PlayersHouse_2F_EventScript_TV::
	msgbox Hollowbrook_Text_PlayerRoomTV, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_2F_Text_Notebook:
	.string "{PLAYER} flipped open the notebook.\p"
	.string "ADVENTURE RULE NO. 1\n"
	.string "Open the MENU with START.\p"
	.string "ADVENTURE RULE NO. 2\n"
	.string "Record your progress with SAVE.\p"
	.string "The remaining pages are blank…$"

Hollowbrook_Text_PlayerRoomTV::
	.string "Your little TV only gets one\n"
	.string "channel. It is the weather.\p"
	.string "Today: the same as yesterday.\n"
	.string "The host looks very proud.$"

@ Wall clock on the back wall (bg_event at (3,1), the author paints the clock metatiles 0x221 over 0x229 at (3,0)/(3,1)):
@ the player's own fake clock (author, 2026-10-09). The state is the vanilla system flag FLAG_SYS_CLOCK_SET, which the set
@ screen sets (a new game also sets it, see src/veldris_new_game.c). No new flag or var. See design/time-of-day.md.
Hollowbrook_PlayersHouse_2F_EventScript_WallClock::
	lockall
	checkplayergender @ the clock screens pick the blue or pink face from VAR_0x8004 (MALE = 0, FEMALE = 1), as the vanilla wrappers do
	copyvar VAR_0x8004, VAR_RESULT
	goto_if_unset FLAG_SYS_CLOCK_SET, Hollowbrook_PlayersHouse_2F_EventScript_ClockStopped
	msgbox Hollowbrook_PlayersHouse_2F_Text_ClockChangeAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, Hollowbrook_PlayersHouse_2F_EventScript_ClockSet
	incrementgamestat GAME_STAT_CHECKED_CLOCK
	fadescreen FADE_TO_BLACK
	special Special_ViewWallClock @ waitstate is implicit; the view screen reloads the field, so nothing after this runs
	releaseall
	end

Hollowbrook_PlayersHouse_2F_EventScript_ClockStopped::
	msgbox Hollowbrook_PlayersHouse_2F_Text_ClockStopped, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_PlayersHouse_2F_EventScript_ClockDone
	goto Hollowbrook_PlayersHouse_2F_EventScript_ClockSet
	end

Hollowbrook_PlayersHouse_2F_EventScript_ClockSet::
	call PlayersHouse_2F_EventScript_SetWallClock @ vanilla: fadescreen + special StartWallClock; the script resumes after the set screen
	delay 30
	msgbox Hollowbrook_PlayersHouse_2F_Text_ClockSet, MSGBOX_DEFAULT
	goto Hollowbrook_PlayersHouse_2F_EventScript_ClockDone
	end

Hollowbrook_PlayersHouse_2F_EventScript_ClockDone::
	releaseall
	end

Hollowbrook_PlayersHouse_2F_Text_ClockStopped:
	.string "The wall clock has stopped.\n"
	.string "Set the time and start it?$"

Hollowbrook_PlayersHouse_2F_Text_ClockChangeAsk:
	.string "The wall clock keeps its own\n"
	.string "time. Reset it?$"

Hollowbrook_PlayersHouse_2F_Text_ClockSet:
	.string "The wall clock is ticking.$"
