@ Route 2 dialogue DRAFT (Wendlebury north to Crestfall). Farm country, a step up from Route 1.
@ Status: PROPOSED, not wired into any map (the map is not built yet).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/route2.inc
@ Pokemon only: no real animals. Nobody here swears (only the Goldsworths can).
@ Scheme 1 foreshadowing: suited men with clipboards survey the road. They set up Crestfall_Text_ConsultantOutside.

@ Signs (south end is Wendlebury, north end is Crestfall).
VeldrisRoute2_Text_SignSouth::
	.string "ROUTE 2\n"
	.string "SOUTH: WENDLEBURY\lNORTH: CRESTFALL$"

VeldrisRoute2_Text_SignMid::
	.string "ROUTE 2\n"
	.string "Fresh hay ahead. Please\l"
	.string "do not judge the smell.$"

VeldrisRoute2_Text_SignNorth::
	.string "CRESTFALL, CITY AHEAD\n"
	.string "‘Wipe your boots.’$"

@ Trainer 1: Youngster, PATRAT L5 and LILLIPUP L5.
VeldrisRoute2_Text_Trainer1Intro::
	.string "I trained all week for this road.\n"
	.string "I'm basically a veteran now!$"

VeldrisRoute2_Text_Trainer1Defeat::
	.string "A veteran of one week.\n"
	.string "That's a short war.$"

VeldrisRoute2_Text_Trainer1After::
	.string "Crestfall's gym is up ahead.\n"
	.string "I'm not going in. Too many hooves.$"

@ Trainer 2: Lass, SKITTY L6 and PIDOVE L6.
VeldrisRoute2_Text_Trainer2Intro::
	.string "My SKITTY and I match.\n"
	.string "We're both tired of Route 1!$"

VeldrisRoute2_Text_Trainer2Defeat::
	.string "Oh dear. We match\n"
	.string "in defeat as well.$"

VeldrisRoute2_Text_Trainer2After::
	.string "I'd buy you a POTION, but I've\n"
	.string "spent it all on hair ribbons.$"

@ Trainer 3: Farmer, ZIGZAGOON L6 and SENTRET L7.
VeldrisRoute2_Text_Trainer3Intro::
	.string "Harvest is in, chores are done.\n"
	.string "Now I've got time to thrash you!$"

VeldrisRoute2_Text_Trainer3Defeat::
	.string "I should've stayed\n"
	.string "with the chores.$"

VeldrisRoute2_Text_Trainer3After::
	.string "Men in suits walked my fence line\n"
	.string "today. Counted my posts. Twice.$"

@ Trainer 4: Camper, BIDOOF L7 and MEOWTH L8 (the toughest on the road).
VeldrisRoute2_Text_Trainer4Intro::
	.string "I sleep under the stars out here.\n"
	.string "It makes a person confident.$"

VeldrisRoute2_Text_Trainer4Defeat::
	.string "Confidence is cheaper than\n"
	.string "a proper tent, it turns out.$"

VeldrisRoute2_Text_Trainer4After::
	.string "Watch the road north. It's\n"
	.string "busy with clipboards today.$"

@ Scheme 1 foreshadowing: men in suits with clipboards surveying the road.
VeldrisRoute2_Text_SurveyorA::
	.string "Do not step on the markers.\n"
	.string "This road is under assessment.\p"
	.string "Our client finds it\n"
	.string "insufficiently profitable.$"

VeldrisRoute2_Text_SurveyorAAfter::
	.string "Forty paces from that post to\n"
	.string "this one. Wasteful. Very wasteful.$"

VeldrisRoute2_Text_SurveyorB::
	.string "Are you a stakeholder?\n"
	.string "No? Then please move along.\p"
	.string "We have a gym to rationalise.\n"
	.string "It's on the schedule.$"

VeldrisRoute2_Text_SurveyorBAfter::
	.string "I counted a hundred and four\n"
	.string "bushes. It felt like a lot.$"

@ Troglodyte sighting (optional, can be dropped). Stays off screen, no battle here.
VeldrisRoute2_Text_TrogSighting::
	.string "A boy in a huge coat stormed\n"
	.string "past, shouting at his shoes.\p"
	.string "Something about ‘the help’\n"
	.string "being late. He went north.$"

@ Guide NPC: gives a REPEL once (a free item, flag needed, see route2.md).
VeldrisRoute2_Text_GuideGive::
	.string "You look ready for CRESTFALL.\n"
	.string "Take this. It's nearly harvest.\p"
	.string "{PLAYER} received a REPEL!$"

VeldrisRoute2_Text_GuideAfter::
	.string "The gym leader is young, but\n"
	.string "she runs that farm like a clock.$"

@ Ambient NPC: a fan of the gym.
VeldrisRoute2_Text_FanTalk::
	.string "GRETA's the youngest leader\n"
	.string "in VELDRIS. And the sassiest.\p"
	.string "She'll be kind about losing to\n"
	.string "her. Mostly.$"

@ Ambient NPC: a worried local.
VeldrisRoute2_Text_LocalWorried::
	.string "Those suits keep measuring our\n"
	.string "ditches. I like my ditches.$"

@ Item pickup texts are the game's own. Hidden items are listed in route2.md.
