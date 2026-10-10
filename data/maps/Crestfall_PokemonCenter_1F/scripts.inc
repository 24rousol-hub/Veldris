Crestfall_PokemonCenter_1F_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Crestfall_PokemonCenter_1F_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, CableClub_OnResume
	.byte 0

Crestfall_PokemonCenter_1F_OnTransition:
	setrespawn HEAL_LOCATION_CRESTFALL
	end

Crestfall_PokemonCenter_1F_EventScript_Nurse::
	setvar VAR_0x800B, LOCALID_CRESTFALL_NURSE
	call Common_EventScript_PkmnCenterNurse
	waitmessage
	waitbuttonpress
	release
	end

Crestfall_PokemonCenter_1F_EventScript_Visitor::
	msgbox Crestfall_PokemonCenter_1F_Text_Visitor, MSGBOX_NPC
	end

Crestfall_PokemonCenter_1F_Text_Visitor:
	.string "I came here to see the gym.\n"
	.string "I stayed for the tomatoes.$"
