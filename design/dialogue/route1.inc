@ Route 1 dialogue DRAFT (Hollowbrook to Crestfall). Farm country, gentle, Normal types.
@ Status: PROPOSED, not wired into any map (the map is not built yet).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/route1.inc
@ Pokemon only: no real animals. Nobody here swears (only the Goldsworths can).

@ Signs (west end is Hollowbrook, east end is Crestfall).
VeldrisRoute1_Text_SignWest::
	.string "ROUTE 1\n"
	.string "WEST: HOLLOWBROOK\lEAST: CRESTFALL$"

VeldrisRoute1_Text_SignEast::
	.string "ROUTE 1\n"
	.string "Please keep off the crops.\l"
	.string "They bite.$"

@ Trainer 1: Youngster, one LILLIPUP (TRAINER intro / defeat / after).
VeldrisRoute1_Text_Trainer1Intro::
	.string "You've got a POKéMON now, right?\n"
	.string "Perfect. I've got one, too!$"

VeldrisRoute1_Text_Trainer1Defeat::
	.string "Mine's still learning.\n"
	.string "So am I, to be fair.$"

VeldrisRoute1_Text_Trainer1After::
	.string "I'll train harder. After lunch.$"

@ Trainer 2: Lass, two small Pokemon.
VeldrisRoute1_Text_Trainer2Intro::
	.string "I walk this road every day.\n"
	.string "Nobody ever battles me. Until now!$"

VeldrisRoute1_Text_Trainer2Defeat::
	.string "Oh. That's why nobody does.$"

VeldrisRoute1_Text_Trainer2After::
	.string "Tomorrow I'll ask someone easier.\n"
	.string "No offence.$"

@ Trainer 3: Farmer, one ZIGZAGOON and one SKITTY (the tougher one).
VeldrisRoute1_Text_Trainer3Intro::
	.string "My crops are fine. My nerves\n"
	.string "aren't. Battle me, kid!$"

VeldrisRoute1_Text_Trainer3Defeat::
	.string "That felt better than\n"
	.string "shouting at the hedge.$"

VeldrisRoute1_Text_Trainer3After::
	.string "A rich boy in a fancy coat came\n"
	.string "through here. Stepped on my beans.$"

@ Guide NPC: gives POTIONs once (a free item, flag needed, see route1.md).
VeldrisRoute1_Text_GuideGive::
	.string "Heading to CRESTFALL? It's\n"
	.string "a long walk. Take these.\p"
	.string "{PLAYER} received 3 POTIONs!$"

VeldrisRoute1_Text_GuideAfter::
	.string "Tall grass hides wild POKéMON.\n"
	.string "Short grass hides only beans.$"

@ Troglodyte sighting (optional, after the lab fight). Can be dropped.
VeldrisRoute1_Text_TrogSighting::
	.string "That boy in the big coat? He\n"
	.string "asked me where the ‘good road’ was.\p"
	.string "I pointed at this one. He looked\n"
	.string "disappointed.$"

@ ===================================================================
@ ADDED 2026-10-01: MORE ROUTE 1 PEOPLE AND THINGS (non-trainers, plus return-visit lines)
@ Suggested spots are in design/route1.md. Pokemon only, nobody swears.
@ ===================================================================

@ Child with a bucket near the Hollowbrook end.
VeldrisRoute1_Text_BucketKid::
	.string "I'm collecting berries for my\n"
	.string "ZIGZAGOON. It eats them all.\p"
	.string "I collect them again.\n"
	.string "It's a very full day.$"

@ Walker with a map, mid-route.
VeldrisRoute1_Text_Walker::
	.string "CRESTFALL is a farm town. Never\n"
	.string "walk straight through the hay.\p"
	.string "The hay has opinions.$"

@ A sleepy interactable Pokemon in the grass.
VeldrisRoute1_Text_SentretLookout::
	.string "SENTRET is standing up very\n"
	.string "straight, watching the horizon.\p"
	.string "There is nothing on the horizon.\n"
	.string "It is committed anyway.\p"
	.string "SENTRET: Sen!$"

@ A scarecrow-style sign by the fields.
VeldrisRoute1_Text_FieldSign::
	.string "‘This field is guarded by\n"
	.string "BIDOOF. Please do not wake it.’$"

@ A bench with a view, interactable.
VeldrisRoute1_Text_RestBench::
	.string "A bench with a view of the\n"
	.string "fields. Someone has carved\l"
	.string "‘Best seat in VELDRIS.’$"

@ Guide, on repeat visits after the first badge.
VeldrisRoute1_Text_GuideAfterBadge::
	.string "You came back with a badge!\n"
	.string "I remember when you were a\l"
	.string "small trainer with big shoes.\p"
	.string "...Those were last week.$"

@ Rematch-style after lines for each trainer once the player has the first badge.
VeldrisRoute1_Text_Trainer1AfterBadge::
	.string "I heard you beat a gym.\n"
	.string "I'll do it after I beat lunch.$"

VeldrisRoute1_Text_Trainer2AfterBadge::
	.string "You're famous now. People are\n"
	.string "talking. Mostly me.$"

VeldrisRoute1_Text_Trainer3AfterBadge::
	.string "The rich boy came back this way.\n"
	.string "Looked tired. Stepped on my\l"
	.string "beans again.$"

@ ADDED 2026-10-01 (Route 1 now ends in Crestfall): Scheme 1 foreshadowing moved here from Route 2.
@ Two surveyors in suits with clipboards, walking Route 1 toward Crestfall. Not trainers. They set up
@ Crestfall_Text_ConsultantOutside in crestfall.inc.
VeldrisRoute1_Text_SurveyorA::
	.string "Do not step on the markers.\n"
	.string "This road is under assessment.\p"
	.string "Our client finds it\n"
	.string "insufficiently profitable.$"

VeldrisRoute1_Text_SurveyorAAfter::
	.string "Forty paces from that post to\n"
	.string "this one. Wasteful. Very wasteful.$"

VeldrisRoute1_Text_SurveyorB::
	.string "Are you a stakeholder?\n"
	.string "No? Then please move along.\p"
	.string "We have a gym to rationalise.\n"
	.string "It's on the schedule.$"

VeldrisRoute1_Text_SurveyorBAfter::
	.string "I counted a hundred and four\n"
	.string "bushes. It felt like a lot.$"

VeldrisRoute1_Text_LocalWorried::
	.string "Those suits keep measuring our\n"
	.string "ditches. I like my ditches.$"
