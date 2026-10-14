Crestfall_HouseB_MapScripts::
	.byte 0

Crestfall_HouseB_EventScript_Trainer::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Crestfall_HouseB_EventScript_TrainerAfter
	msgbox Crestfall_HouseB_Text_TrainerBefore, MSGBOX_DEFAULT
	release
	end

Crestfall_HouseB_EventScript_TrainerAfter::
	msgbox Crestfall_HouseB_Text_TrainerAfter, MSGBOX_DEFAULT
	release
	end

Crestfall_HouseB_Text_TrainerBefore:
	.string "I was going to challenge\n"
	.string "GRETA today. Really.\p"
	.string "Then I saw her MILTANK.\n"
	.string "I'm going to have lunch first.$"

Crestfall_HouseB_Text_TrainerAfter:
	.string "You won! Wow.\n"
	.string "I'll challenge her next year.\p"
	.string "Or the year after. Or I'll\n"
	.string "become a farmer. It's a nice\l"
	.string "life. Mostly.$"
