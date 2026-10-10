Crestfall_HouseA_MapScripts::
	.byte 0

Crestfall_HouseA_EventScript_Husband::
	msgbox Crestfall_HouseA_Text_Husband, MSGBOX_NPC
	end

Crestfall_HouseA_EventScript_Skitty::
	lock
	faceplayer
	waitse
	playmoncry SPECIES_SKITTY, CRY_MODE_NORMAL
	msgbox Crestfall_HouseA_Text_Skitty, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Crestfall_HouseA_Text_Husband:
	.string "My SKITTY sleeps on the warm\n"
	.string "spot by the stove. I sleep\l"
	.string "on the cold spot.\p"
	.string "We've agreed not to discuss it.$"

Crestfall_HouseA_Text_Skitty:
	.string "SKITTY: Mew!$"
