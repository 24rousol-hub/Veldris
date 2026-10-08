Crestfall_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Crestfall_OnTransition
	.byte 0

Crestfall_OnTransition:
	setflag FLAG_VISITED_CRESTFALL
	end

Crestfall_EventScript_TownSign::
	msgbox Crestfall_Text_TownSign, MSGBOX_SIGN
	end

Crestfall_EventScript_GymSign::
	msgbox Crestfall_Text_GymSign, MSGBOX_SIGN
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

Crestfall_Text_TownSign:
	.string "CRESTFALL\n"
	.string "‘Harvest home of the honest.’$"

Crestfall_Text_GymSign:
	.string "CRESTFALL POKéMON GYM\n"
	.string "Leader: GRETA\p"
	.string "‘Wipe your boots. Mind the\n"
	.string "hay. Don't feed the MILTANK.’$"

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
