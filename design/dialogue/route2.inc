@ Route 2 dialogue DRAFT (Crestfall to Wendlebury). Farm country, a step up from Route 1.
@ Status: PROPOSED, not wired into any map (the map is not built yet).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/route2.inc
@ Pokemon only: no real animals. Nobody here swears (only the Goldsworths can).
@ 2026-10-01: Route 2 now runs from Crestfall (after gym 1) to Wendlebury. The Scheme 1 surveyors moved to Route 1 (route1.inc).

@ Signs (south end is Crestfall, north end is Wendlebury).
VeldrisRoute2_Text_SignSouth::
	.string "ROUTE 2\n"
	.string "SOUTH: CRESTFALL\lNORTH: WENDLEBURY$"

VeldrisRoute2_Text_SignMid::
	.string "ROUTE 2\n"
	.string "Fresh hay ahead. Please\l"
	.string "do not judge the smell.$"

VeldrisRoute2_Text_SignNorth::
	.string "WENDLEBURY, TOWN AHEAD\n"
	.string "‘Everything for sale. Mostly.’$"

@ Trainer 1: Youngster, PATRAT L5 and LILLIPUP L5.
VeldrisRoute2_Text_Trainer1Intro::
	.string "I trained all week for this road.\n"
	.string "I'm basically a veteran now!$"

VeldrisRoute2_Text_Trainer1Defeat::
	.string "A veteran of one week.\n"
	.string "That's a short war.$"

VeldrisRoute2_Text_Trainer1After::
	.string "WENDLEBURY is up ahead. The\n"
	.string "market there bites harder.$"

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
	.string "last week. Counted my posts. Twice.$"

@ Trainer 4: Camper, BIDOOF L7 and MEOWTH L8 (the toughest on the road).
VeldrisRoute2_Text_Trainer4Intro::
	.string "I sleep under the stars out here.\n"
	.string "It makes a person confident.$"

VeldrisRoute2_Text_Trainer4Defeat::
	.string "Confidence is cheaper than\n"
	.string "a proper tent, it turns out.$"

VeldrisRoute2_Text_Trainer4After::
	.string "Watch the road north. WENDLEBURY\n"
	.string "haggles even over the weather.$"

@ Leftovers of Scheme 1 (the player has already beaten Crestfall's gym on this road).
VeldrisRoute2_Text_SurveyorLeftover::
	.string "A clipboard lies in the ditch.\n"
	.string "The top page reads ‘Plan B.’\p"
	.string "Plan B is also crossed out.$"

@ Troglodyte sighting (optional, can be dropped). Stays off screen, no battle here.
VeldrisRoute2_Text_TrogSighting::
	.string "A boy in a huge coat stormed\n"
	.string "past, shouting at his shoes.\p"
	.string "Something about ‘the help’\n"
	.string "being late. He went north.$"

@ Guide NPC: gives a REPEL once (a free item, flag needed, see route2.md).
VeldrisRoute2_Text_GuideGive::
	.string "You came out of CRESTFALL well.\n"
	.string "Take this. It's nearly harvest.\p"
	.string "{PLAYER} received a REPEL!$"

VeldrisRoute2_Text_GuideAfter::
	.string "WENDLEBURY has the good market.\n"
	.string "Spend your prize money slowly.$"

@ Ambient NPC: a fan of the gym.
VeldrisRoute2_Text_FanTalk::
	.string "GRETA's the youngest leader\n"
	.string "in VELDRIS. And the sassiest.\p"
	.string "I heard you beat her. She'll\n"
	.string "be kind about it. Mostly.$"

@ Ambient NPC: a worried local.
VeldrisRoute2_Text_LocalWorried::
	.string "The suits left. My ditches are\n"
	.string "fine. I like my ditches.$"

@ Item pickup texts are the game's own. Hidden items are listed in route2.md.
