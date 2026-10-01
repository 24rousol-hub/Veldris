VeldrisRoute1_MapScripts::
	.byte 0

@ ---- Signs ----

VeldrisRoute1_EventScript_SignWest::
	msgbox VeldrisRoute1_Text_SignWest, MSGBOX_SIGN
	end

VeldrisRoute1_EventScript_SignEast::
	msgbox VeldrisRoute1_Text_SignEast, MSGBOX_SIGN
	end

@ ---- Trainers (vanilla Route102 pattern: trainerbattle_single, then the after text) ----

VeldrisRoute1_EventScript_Youngster::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_YOUNGSTER, VeldrisRoute1_Text_Trainer1Intro, VeldrisRoute1_Text_Trainer1Defeat
	msgbox VeldrisRoute1_Text_Trainer1After, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Lass::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_LASS, VeldrisRoute1_Text_Trainer2Intro, VeldrisRoute1_Text_Trainer2Defeat
	msgbox VeldrisRoute1_Text_Trainer2After, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Farmer::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_FARMER, VeldrisRoute1_Text_Trainer3Intro, VeldrisRoute1_Text_Trainer3Defeat
	msgbox VeldrisRoute1_Text_Trainer3After, MSGBOX_AUTOCLOSE
	end

@ ---- Guide: gives 3 POTIONs once ----
@ The dialogue text GuideGive already says '{PLAYER} received 3 POTIONs!', so the gift is
@ made with giveitem_msg (which prints that text with the item fanfare) after checking
@ there is bag space. If the bag is full nothing is given and the flag stays clear, so
@ the guide offers again. (Vanilla 'giveitem' prints its own message and would repeat it.)
VeldrisRoute1_EventScript_Guide::
	lock
	faceplayer
	goto_if_set FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS, VeldrisRoute1_EventScript_GuideAfter
	checkitemspace ITEM_POTION, 3
	goto_if_eq VAR_RESULT, FALSE, VeldrisRoute1_EventScript_GuideBagFull
	giveitem_msg VeldrisRoute1_Text_GuideGive, ITEM_POTION, 3
	setflag FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS
	release
	end

VeldrisRoute1_EventScript_GuideAfter::
	msgbox VeldrisRoute1_Text_GuideAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_GuideBagFull::
	msgbox gText_TooBadBagIsFull, MSGBOX_DEFAULT
	release
	end

@ ---- Troglodyte sighting (optional, can be dropped) ----
@ A farmer who only makes sense after the first fight. Gated by state, not a hide flag:
@ before the fight he repeats the guide-style tip (GuideAfter, a stand-in). No extra flag.
VeldrisRoute1_EventScript_Sighting::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 4, VeldrisRoute1_EventScript_SightingTalk
	msgbox VeldrisRoute1_Text_GuideAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_SightingTalk::
	msgbox VeldrisRoute1_Text_TrogSighting, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_Text_SignWest:
	.string "ROUTE 1\n"
	.string "WEST: HOLLOWBROOK\lEAST: WENDLEBURY$"

VeldrisRoute1_Text_SignEast:
	.string "ROUTE 1\n"
	.string "Please keep off the crops.\l"
	.string "They bite.$"

VeldrisRoute1_Text_Trainer1Intro:
	.string "You've got a POKéMON now, right?\n"
	.string "Perfect. I've got one, too!$"

VeldrisRoute1_Text_Trainer1Defeat:
	.string "Mine's still learning.\n"
	.string "So am I, to be fair.$"

VeldrisRoute1_Text_Trainer1After:
	.string "I'll train harder. After lunch.$"

VeldrisRoute1_Text_Trainer2Intro:
	.string "I walk this road every day.\n"
	.string "Nobody ever battles me. Until now!$"

VeldrisRoute1_Text_Trainer2Defeat:
	.string "Oh. That's why nobody does.$"

VeldrisRoute1_Text_Trainer2After:
	.string "Tomorrow I'll ask someone easier.\n"
	.string "No offence.$"

VeldrisRoute1_Text_Trainer3Intro:
	.string "My crops are fine. My nerves\n"
	.string "aren't. Battle me, kid!$"

VeldrisRoute1_Text_Trainer3Defeat:
	.string "That felt better than\n"
	.string "shouting at the hedge.$"

VeldrisRoute1_Text_Trainer3After:
	.string "A rich boy in a fancy coat came\n"
	.string "through here. Stepped on my beans.$"

VeldrisRoute1_Text_GuideGive:
	.string "Heading to WENDLEBURY? It's\n"
	.string "a long walk. Take these.\p"
	.string "{PLAYER} received 3 POTIONs!$"

VeldrisRoute1_Text_GuideAfter:
	.string "Tall grass hides wild POKéMON.\n"
	.string "Short grass hides only beans.$"

VeldrisRoute1_Text_TrogSighting:
	.string "That boy in the big coat? He\n"
	.string "asked me where the ‘good road’ was.\p"
	.string "I pointed at this one. He looked\n"
	.string "disappointed.$"
