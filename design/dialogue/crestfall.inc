@ Crestfall dialogue DRAFT: gym 1, Greta (Normal type, young and sassy), and Scheme 1.
@ Status: PROPOSED, not wired into any map (no map exists yet). Author fixed: Greta is gym 1, Normal type,
@ young, rising fast in the gym hierarchy, a tad sassy but nice (2026-09-29, replaces 'retired farmer'),
@ trainer constant TRAINER_CRESTFALL_GRETA, the STANDARD BADGE, and two gym trainers.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/crestfall.inc
@ Pokemon only: no real animals. The farm's animals are Pokemon (MILTANK, ZIGZAGOON, SKITTY, SLAKOTH).
@ Badge 1 is the STANDARD BADGE (author): the standard you must meet to start the gym challenge.
@ Scheme 1 (PROPOSED): hired 'efficiency consultants' come to condemn Greta's farmyard gym. They get lost in the
@ hay maze, and the inspection ends when the farm's Pokemon take over the paperwork. Troglodyte arrives to watch
@ it work, it has not, and he has to battle the player anyway. Then the gym battle follows as normal.
@ {STR_VAR_2} = Troglodyte's species (set by the lab scene).

@ ===================================================================
@ SCHEME 1: setup, reveal, collapse (Crestfall town, before the gym)
@ ===================================================================

@ Setup: a stranger outside the gym.
Crestfall_Text_ConsultantOutside::
	.string "Excuse me. Are you a local?\n"
	.string "I'm conducting a site\l"
	.string "assessment. A very expensive one.\p"
	.string "This property is operating at\n"
	.string "sixty percent of its potential.$"

@ Town sign, gym sign.
Crestfall_Text_TownSign::
	.string "CRESTFALL\n"
	.string "‘Harvest home of the honest.’$"

Crestfall_Text_GymSign::
	.string "CRESTFALL POKéMON GYM\n"
	.string "Leader: GRETA\p"
	.string "‘Wipe your boots. Mind the\n"
	.string "hay. Don't feed the MILTANK.’$"

@ Locals reacting to the scheme (before the collapse).
Crestfall_Text_LocalWorried::
	.string "Those suited folk have been\n"
	.string "measuring the gym all morning.\p"
	.string "They say it's ‘inefficient.’\n"
	.string "It's a barn, love.$"

@ Reveal: the consultants at the gym door.
Crestfall_Text_ConsultantBoss::
	.string "I am the lead consultant.\n"
	.string "Our client wishes this site\l"
	.string "rationalised.\p"
	.string "Rows of hay, cleared. Barn,\n"
	.string "converted. Paddock, a car park.$"

Crestfall_Text_ConsultantJunior::
	.string "I'm only the junior. I've been\n"
	.string "in the hay maze since nine.\p"
	.string "Nobody told me it moves.$"

@ Collapse: after the player has found Greta (the scene at the gym door).
Crestfall_Text_GretaCollapse1::
	.string "Well now. It seems my MILTANK\n"
	.string "have read your paperwork.\p"
	.string "They've eaten most of it.\n"
	.string "They seemed to disagree.$"

Crestfall_Text_ConsultantCollapse::
	.string "That was the only signed copy!\n"
	.string "Our client will be furious!\p"
	.string "It is hay. Why is there hay\n"
	.string "in my briefcase?$"

Crestfall_Text_GretaCollapse2::
	.string "Whoever sent you, tell them\n"
	.string "the barn stays a barn.\p"
	.string "And the maze is a maze. You'll\n"
	.string "find your way out by dinner.$"

@ ===================================================================
@ TROGLODYTE ARRIVES TO WATCH IT WORK (then has to battle anyway)
@ ===================================================================

Crestfall_Text_TrogArrives1::
	.string "What. The hell. Is going on?\n"
	.string "Where is the demolition crew?\p"
	.string "My father's people were going\n"
	.string "to flatten this dump today!$"

Crestfall_Text_GretaToTrog::
	.string "So that's whose name was on\n"
	.string "the paperwork. I thought so.\p"
	.string "Young man, this is a farm. It\n"
	.string "doesn't flatten. It grows back.$"

Crestfall_Text_TrogToPlayer::
	.string "You! You again. Did you do\n"
	.string "this? Of course you did.\p"
	.string "Fine. I'll take my frustration\n"
	.string "out on you. Right here, right now.$"

@ Battle intro / defeat / after. Trainer text (battle window).
Crestfall_Text_TrogBattleIntro::
	.string "I'll show you how a Goldsworth\n"
	.string "battles! Go, {STR_VAR_2}!$"

Crestfall_Text_TrogBattleDefeat::
	.string "Impossible! I had the best\n"
	.string "everything! It's not fair!$"

Crestfall_Text_TrogAfterBattle1::
	.string "This isn't over. My family will\n"
	.string "hear about this.\p"
	.string "...Shut up. Both of you.$"

Crestfall_Text_TrogAfterBattle2::
	.string "Enjoy your little gym, peasant.\n"
	.string "I'll be back with better\l"
	.string "lawyers. And a better team.$"

Crestfall_Text_GretaAfterTrog::
	.string "Well. That's him put in his\n"
	.string "place. For about a week.\p"
	.string "Come and see me, {PLAYER}.\n"
	.string "Gym's open. Mind the hay.$"

@ ===================================================================
@ GRETA (gym leader)
@ ===================================================================

@ First talk, before the battle.
Crestfall_Text_GretaIntro::
	.string "Well, hello. You must be {PLAYER}.\n"
	.string "The whole town has been talking.\p"
	.string "I'm GRETA. Crestfall's gym leader.\n"
	.string "Yes, I know. I look too young.\p"
	.string "I get that a lot. Usually right\n"
	.string "before I win.$"

Crestfall_Text_GretaChallenge::
	.string "Normal types. Don't look so\n"
	.string "disappointed. Normal is reliable.\p"
	.string "Flashy gets you a cool entrance.\n"
	.string "Reliable gets you badges.\p"
	.string "This is the first gym. Everyone\n"
	.string "starts here. Even me. For now.$"

@ Battle texts (trainer window).
Crestfall_Text_GretaBattleIntro::
	.string "Try to keep up. No pressure.$"

Crestfall_Text_GretaDefeat::
	.string "Wow. Okay. That was good.\n"
	.string "Really good.$"

@ After the battle: badge.
Crestfall_Text_GretaBadge1::
	.string "Here. The STANDARD BADGE.\n"
	.string "Congratulations!\p"
	.string "{PLAYER} received the STANDARD\n"
	.string "BADGE from GRETA!$"

Crestfall_Text_GretaBadge2::
	.string "That badge means you've met the\n"
	.string "standard to start the gym\l"
	.string "challenge. The real work begins.\p"
	.string "It also lets you use CUT. Handy\n"
	.string "for hay. Take CRUNCH, too.$"

Crestfall_Text_GretaAfterBadge::
	.string "That Goldsworth boy? Bit of a\n"
	.string "mess, honestly. Not wicked.\p"
	.string "He's just never been told ‘no.’\n"
	.string "So you'd be doing the region a\l"
	.string "favour, every time you beat him.$"

Crestfall_Text_GretaIdleAfter::
	.string "Back already? Flattering.\n"
	.string "I have paperwork to do.\p"
	.string "The real kind. Not the kind\n"
	.string "the MILTANK eat.$"

@ ===================================================================
@ GYM TRAINERS (author: two; each costs one of the 9 spare trainer ids)
@ ===================================================================

Crestfall_Text_Trainer1Intro::
	.string "I shovel the hay. She does\n"
	.string "the thinking. Come on, then!$"

Crestfall_Text_Trainer1Defeat::
	.string "I'll shovel the loss, too.$"

Crestfall_Text_Trainer1After::
	.string "GRETA's tougher than she looks.\n"
	.string "Also tougher than she sounds.$"

Crestfall_Text_Trainer2Intro::
	.string "You'll never find the door in\n"
	.string "the maze! Fight me instead!$"

Crestfall_Text_Trainer2Defeat::
	.string "Oh. It's that way. I see.$"

Crestfall_Text_Trainer2After::
	.string "I've been in here for three\n"
	.string "years. It's very relaxing.$"

@ ===================================================================
@ CRESTFALL TOWNSFOLK AND POKEMON CENTER (PROPOSED; before the gym is beaten,
@ then after). Nobody here swears. Pokemon only.
@ ===================================================================

Crestfall_Text_TrogPetBattle::
	.string "SIR BISCUIT, you're up. Try not\n"
	.string "to look so nervous.$"

Crestfall_Text_FarmhandBefore::
	.string "The boss is out back. Follow\n"
	.string "the hay. Don't trust the hay.$"

Crestfall_Text_FarmhandAfter::
	.string "The hay maze fixed itself after\n"
	.string "the suits left. Nobody asked it to.$"

Crestfall_Text_KidBefore::
	.string "MILTANK is my favourite.\n"
	.string "It's like a big, pink stove.$"

Crestfall_Text_KidAfter::
	.string "You beat GRETA? She beat me once.\n"
	.string "I wasn't crying. It was hay fever.$"

Crestfall_Text_GrandmaBefore::
	.string "Those men in suits walked right\n"
	.string "through my tomato patch.\p"
	.string "The TOMATO PATCH. Unforgivable.$"

Crestfall_Text_GrandmaAfter::
	.string "Since GRETA saw them off, the\n"
	.string "tomatoes have never been better.$"

Crestfall_Text_CenterNurse::
	.string "Welcome to the POKéMON CENTER.\n"
	.string "We can heal your POKéMON.\p"
	.string "Would you like to rest them?$"

Crestfall_Text_CenterNurseDone::
	.string "Your POKéMON are fully healed.\n"
	.string "We hope to see you again!$"

Crestfall_Text_CenterVisitor::
	.string "I came here to see the gym.\n"
	.string "I stayed for the tomatoes.$"

Crestfall_Text_MartClerk::
	.string "Welcome! Hay is not for sale.\n"
	.string "Everything else is.$"
