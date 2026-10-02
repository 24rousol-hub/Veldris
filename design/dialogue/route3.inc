@ Route 3 dialogue DRAFT (Crestfall to Briarwick). Status: PROPOSED, not wired. Brief: design/maps/routes-west.md, R3.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/route3.inc
@ A short wooded lane. The Crestfall end is closed by road works (GOLDSWORTH ROADWAYS) until FLAG_BADGE01_GET.
@ Pokemon only (no real animals), nobody here swears. TROGLODYTE written literally.

VeldrisRoute3_Text_SignCrestfall::
	.string "ROUTE 3\n"
	.string "WEST: BRIARWICK\lSOUTH: CRESTFALL$"

VeldrisRoute3_Text_SignBriarwick::
	.string "ROUTE 3\n"
	.string "BRIARWICK, CITY AHEAD\p"
	.string "‘Please step round the trees.’$"

VeldrisRoute3_Text_RoadworksSign::
	.string "ROAD CLOSED\n"
	.string "Resurfacing by\l"
	.string "GOLDSWORTH ROADWAYS$"

@ The barrier at the Crestfall end (before badge 1). Foreman at the barrier.
VeldrisRoute3_Text_ForemanBefore::
	.string "Road's closed. Resurfacing.\n"
	.string "Won't be long. Maybe a month.\p"
	.string "Try WENDLEBURY and ROUTE 8.\n"
	.string "It's the long way round.$"

VeldrisRoute3_Text_ForemanBefore2::
	.string "I'm paid by the day. Not by\n"
	.string "the road. I'm in no hurry.$"

VeldrisRoute3_Text_WorkerBreak::
	.string "On my break. Don't tell the\n"
	.string "foreman it's a long one.\p"
	.string "This is the best seat on the\n"
	.string "whole site. It's a cone.$"

@ After badge 1 the barrier, workers and lorry are removed. These NPCs remain.
VeldrisRoute3_Text_HikerBefore::
	.string "Briarwick has the biggest trees\n"
	.string "in all of Veldris.\p"
	.string "I'd tell you more but I've been\n"
	.string "lost since Thursday.$"

VeldrisRoute3_Text_HikerAfter::
	.string "The road works are gone. I\n"
	.string "found Briarwick. It's very big.\p"
	.string "I'm on my way home. By Tuesday.$"

VeldrisRoute3_Text_GirlNet::
	.string "I lost my net. It was a good\n"
	.string "net. I named it ‘Net.’\p"
	.string "If you see it, say hello.\n"
	.string "Don't take it.$"

VeldrisRoute3_Text_GirlNetAfter::
	.string "NET came back by itself. A\n"
	.string "Pokémon dragged it home.\p"
	.string "I'm not sure which of them\n"
	.string "owns the other now.$"

@ Troglodyte sighting (optional, can be cut).
VeldrisRoute3_Text_TrogSighting::
	.string "A boy in a smart coat went\n"
	.string "through before the cones went up.\p"
	.string "Then he complained about the\n"
	.string "cones. From the other side.$"

@ Trainer 1: Bug Catcher, WURMPLE 10 and KRICKETOT 11.
VeldrisRoute3_Text_Trainer1Intro::
	.string "I've caught every small Pokémon\n"
	.string "on this road. Twice.\p"
	.string "Let's see how you handle a swarm.$"

VeldrisRoute3_Text_Trainer1Defeat::
	.string "A swarm of two. Fair enough.$"

VeldrisRoute3_Text_Trainer1After::
	.string "HACHIMEL up in BRIARWICK is\n"
	.string "kind. Don't let that fool you.$"

@ Trainer 2: Youngster, PATRAT 11 and PIDOVE 12.
VeldrisRoute3_Text_Trainer2Intro::
	.string "I'm on my way to BRIARWICK's\n"
	.string "gym. Almost. Not quite yet.\p"
	.string "Practice first!$"

VeldrisRoute3_Text_Trainer2Defeat::
	.string "Maybe a bit more practice.$"

VeldrisRoute3_Text_Trainer2After::
	.string "The gym there is full of webs.\n"
	.string "I'll need a new plan.$"

@ Trainer 3: Camper, ODDISH 12 and POOCHYENA 12.
VeldrisRoute3_Text_Trainer3Intro::
	.string "I sleep under these trees. It's\n"
	.string "free. The ground isn't, though.\p"
	.string "Battle me for the pillow money!$"

VeldrisRoute3_Text_Trainer3Defeat::
	.string "No pillow money tonight.$"

VeldrisRoute3_Text_Trainer3After::
	.string "The trees get bigger the closer\n"
	.string "you get. It's an optical thing.$"

@ Pond (fishing spot) and items are the game's own texts. Hidden items: PECHA BERRY by the pond,
@ ANTIDOTE in the gap clearing, GREAT BALL behind the Cut tree (Cut, badge 1).
VeldrisRoute3_Text_CutTreeHint::
	.string "A tree blocks a side path.\n"
	.string "Perhaps it could be cut down.$"
