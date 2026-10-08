VeldrisRoute1_MapScripts::
	.byte 0

@ ---- Signs ----

VeldrisRoute1_EventScript_SignWest::
	msgbox VeldrisRoute1_Text_SignWest, MSGBOX_SIGN
	end

VeldrisRoute1_EventScript_SignEast::
	msgbox VeldrisRoute1_Text_SignEast, MSGBOX_SIGN
	end

VeldrisRoute1_EventScript_FieldSign::
	msgbox VeldrisRoute1_Text_FieldSign, MSGBOX_SIGN
	end

@ ---- Trainers (vanilla Route102 pattern), with a different line once the player has badge 1 ----

VeldrisRoute1_EventScript_Youngster::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_YOUNGSTER, VeldrisRoute1_Text_Trainer1Intro, VeldrisRoute1_Text_Trainer1Defeat
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_YoungsterAfterBadge
	msgbox VeldrisRoute1_Text_Trainer1After, MSGBOX_AUTOCLOSE
	end
VeldrisRoute1_EventScript_YoungsterAfterBadge::
	msgbox VeldrisRoute1_Text_Trainer1AfterBadge, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Lass::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_LASS, VeldrisRoute1_Text_Trainer2Intro, VeldrisRoute1_Text_Trainer2Defeat
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_LassAfterBadge
	msgbox VeldrisRoute1_Text_Trainer2After, MSGBOX_AUTOCLOSE
	end
VeldrisRoute1_EventScript_LassAfterBadge::
	msgbox VeldrisRoute1_Text_Trainer2AfterBadge, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Farmer::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_FARMER, VeldrisRoute1_Text_Trainer3Intro, VeldrisRoute1_Text_Trainer3Defeat
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_FarmerAfterBadge
	msgbox VeldrisRoute1_Text_Trainer3After, MSGBOX_AUTOCLOSE
	end
VeldrisRoute1_EventScript_FarmerAfterBadge::
	msgbox VeldrisRoute1_Text_Trainer3AfterBadge, MSGBOX_AUTOCLOSE
	end

@ ---- Guide: gives 3 POTIONs once (giveitem_msg prints the 'received' line in the text) ----
VeldrisRoute1_EventScript_Guide::
	lock
	faceplayer
	goto_if_set FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS, VeldrisRoute1_EventScript_GuideAfter
	checkitemspace ITEM_POTION, 3
	goto_if_eq VAR_RESULT, FALSE, VeldrisRoute1_EventScript_GuideBagFull
	giveitem_msg VeldrisRoute1_Text_GuideGive, ITEM_POTION, 3
	setflag FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS
	goto VeldrisRoute1_EventScript_GuideJournal

VeldrisRoute1_EventScript_GuideAfter::
	checkitem ITEM_JOURNAL
	goto_if_eq VAR_RESULT, FALSE, VeldrisRoute1_EventScript_GuideJournal
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_GuideAfterBadge
	msgbox VeldrisRoute1_Text_GuideAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_GuideAfterBadge::
	msgbox VeldrisRoute1_Text_GuideAfterBadge, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_GuideBagFull::
	msgbox gText_TooBadBagIsFull, MSGBOX_DEFAULT
	release
	end

@ The Journal (design/journal.md): given once after the Potions, and again here if the bag was full or the save predates it.
VeldrisRoute1_EventScript_GuideJournal::
	checkitem ITEM_JOURNAL
	goto_if_eq VAR_RESULT, TRUE, VeldrisRoute1_EventScript_GuideJournalDone
	msgbox VeldrisRoute1_Text_GuideJournal, MSGBOX_DEFAULT
	call Veldris_EventScript_GiveJournal
VeldrisRoute1_EventScript_GuideJournalDone::
	release
	end

@ ---- Troglodyte sighting: gated by state, no flag ----
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

@ ---- Other people and Pokemon ----
VeldrisRoute1_EventScript_BucketKid::
	msgbox VeldrisRoute1_Text_BucketKid, MSGBOX_NPC
	end

VeldrisRoute1_EventScript_Walker::
	msgbox VeldrisRoute1_Text_Walker, MSGBOX_NPC
	end

VeldrisRoute1_EventScript_SentretLookout::
	lock
	faceplayer
	playmoncry SPECIES_SENTRET, CRY_MODE_NORMAL
	msgbox VeldrisRoute1_Text_SentretLookout, MSGBOX_DEFAULT
	waitmoncry
	release
	end

@ Scheme 1 surveyors: their main lines until the first badge, the 'After' lines once Greta's gym is saved
VeldrisRoute1_EventScript_SurveyorA::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_SurveyorAAfter
	msgbox VeldrisRoute1_Text_SurveyorA, MSGBOX_DEFAULT
	release
	end
VeldrisRoute1_EventScript_SurveyorAAfter::
	msgbox VeldrisRoute1_Text_SurveyorAAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_SurveyorB::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, VeldrisRoute1_EventScript_SurveyorBAfter
	msgbox VeldrisRoute1_Text_SurveyorB, MSGBOX_DEFAULT
	release
	end
VeldrisRoute1_EventScript_SurveyorBAfter::
	msgbox VeldrisRoute1_Text_SurveyorBAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_LocalWorried::
	msgbox VeldrisRoute1_Text_LocalWorried, MSGBOX_NPC
	end

VeldrisRoute1_Text_SignWest:
	.string "ROUTE 1\n"
	.string "WEST: HOLLOWBROOK\lEAST: CRESTFALL$"

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
	.string "Heading to CRESTFALL? It's\n"
	.string "a long walk. Take these.\p"
	.string "{PLAYER} received 3 POTIONs!$"

VeldrisRoute1_Text_GuideJournal:
	.string "And take this. Every walker on\n"
	.string "this road ends up wanting one.\p"
	.string "It keeps your badges and what\n"
	.string "comes next. Put it on SELECT.$"

VeldrisRoute1_Text_GuideAfter:
	.string "Tall grass hides wild POKéMON.\n"
	.string "Short grass hides only beans.$"

VeldrisRoute1_Text_TrogSighting:
	.string "That boy in the big coat? He\n"
	.string "asked me where the ‘good road’ was.\p"
	.string "I pointed at this one. He looked\n"
	.string "disappointed.$"

VeldrisRoute1_Text_BucketKid:
	.string "I'm collecting berries for my\n"
	.string "ZIGZAGOON. It eats them all.\p"
	.string "I collect them again.\n"
	.string "It's a very full day.$"

VeldrisRoute1_Text_Walker:
	.string "CRESTFALL is a farm town. Never\n"
	.string "walk straight through the hay.\p"
	.string "The hay has opinions.$"

VeldrisRoute1_Text_SentretLookout:
	.string "SENTRET is standing up very\n"
	.string "straight, watching the horizon.\p"
	.string "There is nothing on the horizon.\n"
	.string "It is committed anyway.\p"
	.string "SENTRET: Sen!$"

VeldrisRoute1_Text_FieldSign:
	.string "‘This field is guarded by\n"
	.string "BIDOOF. Please do not wake it.’$"

VeldrisRoute1_Text_GuideAfterBadge:
	.string "You came back with a badge!\n"
	.string "I remember when you were a\l"
	.string "small trainer with big shoes.\p"
	.string "...Those were last week.$"

VeldrisRoute1_Text_Trainer1AfterBadge:
	.string "I heard you beat a gym.\n"
	.string "I'll do it after I beat lunch.$"

VeldrisRoute1_Text_Trainer2AfterBadge:
	.string "You're famous now. People are\n"
	.string "talking. Mostly me.$"

VeldrisRoute1_Text_Trainer3AfterBadge:
	.string "The rich boy came back this way.\n"
	.string "Looked tired. Stepped on my\l"
	.string "beans again.$"

VeldrisRoute1_Text_SurveyorA:
	.string "Do not step on the markers.\n"
	.string "This road is under assessment.\p"
	.string "Our client finds it\n"
	.string "insufficiently profitable.$"

VeldrisRoute1_Text_SurveyorAAfter:
	.string "Forty paces from that post to\n"
	.string "this one. Wasteful. Very wasteful.$"

VeldrisRoute1_Text_SurveyorB:
	.string "Are you a stakeholder?\n"
	.string "No? Then please move along.\p"
	.string "We have a gym to rationalise.\n"
	.string "It's on the schedule.$"

VeldrisRoute1_Text_SurveyorBAfter:
	.string "I counted a hundred and four\n"
	.string "bushes. It felt like a lot.$"

VeldrisRoute1_Text_LocalWorried:
	.string "Those suits keep measuring our\n"
	.string "ditches. I like my ditches.$"
