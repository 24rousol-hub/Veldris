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

@ The wife (placed 2026-10-13, lines PROPOSED; the old consultant lines are superseded)
Crestfall_HouseA_EventScript_Wife::
	lock
	faceplayer
	goto_if_ge VAR_CRESTFALL_STATE, 1, Crestfall_HouseA_EventScript_WifeAfter
	msgbox Crestfall_HouseA_Text_Wife, MSGBOX_DEFAULT
	release
	end
Crestfall_HouseA_EventScript_WifeAfter::
	msgbox Crestfall_HouseA_Text_WifeAfter, MSGBOX_DEFAULT
	release
	end

Crestfall_HouseA_Text_Wife:
	.string "A rich boy has booked the whole\n"
	.string "gym. For a photo. A PHOTO.\p"
	.string "In my day you earned a badge.\n"
	.string "You didn't hire one.$"

Crestfall_HouseA_Text_WifeAfter:
	.string "That photo on the noticeboard!\n"
	.string "I've been to see it twice.\p"
	.string "The COMMONS lot would love it.\n"
	.string "They'd put it on a banner.$"

Crestfall_HouseA_Text_Husband:
	.string "My SKITTY sleeps on the warm\n"
	.string "spot by the stove. I sleep\l"
	.string "on the cold spot.\p"
	.string "We've agreed not to discuss it.$"

Crestfall_HouseA_Text_Skitty:
	.string "SKITTY: Mew!$"
