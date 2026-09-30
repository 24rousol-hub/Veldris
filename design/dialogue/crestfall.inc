@ Crestfall dialogue DRAFT: gym 1, Greta (Normal type, retired farmer), and Scheme 1.
@ Status: PROPOSED, not wired into any map (no map exists yet). Author fixed only: Greta is gym 1, Normal type,
@ a retired farmer, trainer constant TRAINER_CRESTFALL_GRETA. Everything else here is a proposal.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/crestfall.inc
@ Pokemon only: no real animals. The farm's animals are Pokemon (MILTANK, ZIGZAGOON, SKITTY, SLAKOTH).
@ Badge name is a PLACEHOLDER (badge names are not decided): 'FIELD BADGE'.
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
	.string "They say it's 'inefficient.'\n"
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
	.string "So you're {PLAYER}. The boy\n"
	.string "who's been chasing that other\l"
	.string "boy.\p"
	.string "I'm GRETA. I grew oats for\n"
	.string "forty years. Now I grow\l"
	.string "trainers. They're about as\l"
	.string "stubborn.$"

Crestfall_Text_GretaChallenge::
	.string "Normal types, that's my line.\n"
	.string "Nothing fancy. Nothing rare.\p"
	.string "Just good, steady POKéMON that\n"
	.string "show up every day and work.\p"
	.string "Let's see what you've got.$"

@ Battle texts (trainer window).
Crestfall_Text_GretaBattleIntro::
	.string "Right. Keep your boots on.$"

Crestfall_Text_GretaDefeat::
	.string "Well, I'll be. You've a good\n"
	.string "head on you.$"

@ After the battle: badge.
Crestfall_Text_GretaBadge1::
	.string "Here. The FIELD BADGE. It's\n"
	.string "made of honest metal.\p"
	.string "{PLAYER} received the FIELD BADGE\n"
	.string "from GRETA!$"

Crestfall_Text_GretaBadge2::
	.string "It also lets you use CUT out\n"
	.string "in the field. Handy for hay.\p"
	.string "Take this too. It's a TM. It'll\n"
	.string "do more than you'd think.$"

Crestfall_Text_GretaAfterBadge::
	.string "You'll want to keep an eye on\n"
	.string "that Goldsworth boy.\p"
	.string "He's not wicked. He's just\n"
	.string "never been told 'no.'\p"
	.string "You'd be doing him a favour.\n"
	.string "Every time you beat him.$"

Crestfall_Text_GretaIdleAfter::
	.string "Back again? The MILTANK are\n"
	.string "pleased. They like a winner.\p"
	.string "So do I. Go on. Get on with it.$"

@ ===================================================================
@ GYM TRAINERS (optional, each costs one of the 9 spare trainer ids)
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
