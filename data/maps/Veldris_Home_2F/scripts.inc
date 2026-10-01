Veldris_Home_2F_MapScripts::
	.byte 0

Veldris_Home_2F_EventScript_PC::
	lockall
	setvar VAR_0x8004, PC_LOCATION_VELDRIS_HOME
	special DoPCTurnOnEffect
	playse SE_PC_ON
	msgbox gText_PlayerHouseBootPC, MSGBOX_DEFAULT
	special BedroomPC
	releaseall
	end

Veldris_Home_2F_EventScript_TurnOffPlayerPC::
	setvar VAR_0x8004, PC_LOCATION_VELDRIS_HOME
	playse SE_PC_OFF
	special DoPCTurnOffEffect
	releaseall
	end

Veldris_Home_2F_EventScript_Notebook::
	msgbox Veldris_Home_2F_Text_Notebook, MSGBOX_SIGN
	end

Veldris_Home_2F_Text_Notebook:
	.string "{PLAYER} flipped open the notebook.\p"
	.string "ADVENTURE RULE NO. 1\n"
	.string "Open the MENU with START.\p"
	.string "ADVENTURE RULE NO. 2\n"
	.string "Record your progress with SAVE.\p"
	.string "The remaining pages are blank…$"
