@ Wendlebury dialogue DRAFT (town 3, the market crossroads, reached from Crestfall by Route 2). No gym.
@ Status: PROPOSED, not wired into any map (the map is not built yet).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/wendlebury.inc
@ Pokemon only: no real animals. Nobody here swears.

Wendlebury_Text_TownSign::
	.string "WENDLEBURY\n"
	.string "‘Everything for sale. Mostly.’$"

Wendlebury_Text_CenterSign::
	.string "POKéMON CENTER\n"
	.string "Rest your POKéMON. And yourself.$"

Wendlebury_Text_MartSign::
	.string "POKé MART\n"
	.string "Open. Probably.$"

Wendlebury_Text_CenterNurse::
	.string "Welcome to the POKéMON CENTER.\n"
	.string "We can heal your POKéMON.\p"
	.string "Would you like to rest them?$"

Wendlebury_Text_CenterNurseDone::
	.string "Your POKéMON are fully healed.\n"
	.string "We hope to see you again!$"

Wendlebury_Text_CenterVisitor::
	.string "The soup here is free for\n"
	.string "trainers. Nobody told the soup.$"

Wendlebury_Text_MartClerk::
	.string "Welcome! Everything here is\n"
	.string "priced fairly. Mostly to me.$"

Wendlebury_Text_Trader::
	.string "Fresh POKé BALLS! Well,\n"
	.string "not fresh. But round.$"

Wendlebury_Text_Kid::
	.string "I'm not allowed past the\n"
	.string "barricade. I checked twice.$"

Wendlebury_Text_Gossip::
	.string "Ever met a Goldsworth? Me\n"
	.string "neither. Everyone's heard of them.\p"
	.string "They own half the region. The\n"
	.string "other half hasn't noticed yet.$"

Wendlebury_Text_TravellerNorth::
	.string "Coming up from CRESTFALL? Then\n"
	.string "you've met the hay maze.\p"
	.string "Everyone gets lost in it once.\n"
	.string "It's practically a greeting.$"

Wendlebury_Text_TravellerNorthAfter::
	.string "CRESTFALL's tomatoes got here\n"
	.string "before you did. They're worth it.$"

Wendlebury_Text_BarricadeMan::
	.string "Road's closed. Official reasons.\n"
	.string "They keep changing.$"

Wendlebury_Text_ResidentA::
	.string "I moved here for the quiet.\n"
	.string "Then the market came.$"

Wendlebury_Text_ResidentB::
	.string "A boy in a very clean coat asked\n"
	.string "me for ‘the good inn’.\p"
	.string "We have one inn. He was not\n"
	.string "pleased.$"

@ ===================================================================
@ ADDED 2026-10-01: THE REST OF WENDLEBURY (houses, Center 2F, Mart, stalls, return-visit lines)
@ 'AfterCrestfall' = after the player has beaten Crestfall's gym (the first badge). Nobody swears.
@ ===================================================================

@ Market stall: a berry seller.
Wendlebury_Text_BerrySeller::
	.string "Berries! Grown on ROUTE 1,\n"
	.string "ripened by a very patient\l"
	.string "ZIGZAGOON.\p"
	.string "I won't say which part it did.$"

@ Market stall: a tea seller.
Wendlebury_Text_TeaSeller::
	.string "Tea, warm and strange. The\n"
	.string "strange is free.\p"
	.string "Don't ask what's in it. It asks\n"
	.string "the same of you.$"

@ Pokemon Center visitors.
Wendlebury_Text_CenterVisitor2::
	.string "I have been waiting for my\n"
	.string "POKéMON for an hour.\p"
	.string "The nurse says it's a nap.\n"
	.string "It isn't mine that's napping.$"

Wendlebury_Text_Center2FCounter::
	.string "Trades and battles are done\n"
	.string "upstairs, when the cables\l"
	.string "are untangled.\p"
	.string "Please be patient. They are\n"
	.string "very tangled.$"

@ Mart: a shopper.
Wendlebury_Text_MartShopper::
	.string "I came for one POTION. I'm\n"
	.string "leaving with eleven things.\p"
	.string "It's the lighting.$"

@ House 1: a resident, their POKéMON, and furniture.
Wendlebury_Text_House1Resident::
	.string "Come in, come in. Mind the\n"
	.string "doormat. It's a SLAKOTH.\p"
	.string "...Just kidding. It's a doormat.\n"
	.string "The SLAKOTH is by the stove.$"

Wendlebury_Text_House1Pokemon::
	.string "SLAKOTH is lying very still.\p"
	.string "It looks like it is thinking\n"
	.string "about something extremely slowly.\p"
	.string "SLAKOTH: ...Kyu.$"

Wendlebury_Text_House1Shelf::
	.string "A shelf of market receipts,\n"
	.string "filed by year. The oldest is a\l"
	.string "receipt for another shelf.$"

@ House 2: two residents and a TV.
Wendlebury_Text_House2Resident::
	.string "Every morning the market shouts\n"
	.string "outside my window.\p"
	.string "I've learned all the prices.\n"
	.string "None of them are right.$"

Wendlebury_Text_House2Child::
	.string "I know the secret of the\n"
	.string "market. The secret is: haggle.\p"
	.string "That's the whole secret.$"

Wendlebury_Text_House2TV::
	.string "A programme about a rich family\n"
	.string "that owns a lot of boats.\p"
	.string "It ends with a boat. It always\n"
	.string "ends with a boat.$"

@ Troglodyte sighting, after the lab fight (can be cut).
Wendlebury_Text_TrogSighting::
	.string "A boy in a spotless coat asked\n"
	.string "for ‘the best table’ at a stall.\p"
	.string "We don't have tables. He left\n"
	.string "in a huff. A very clean huff.$"

@ After Crestfall's gym: town gossip catches up (the consultants and the MILTANK, Scheme 1).
Wendlebury_Text_GossipAfterCrestfall::
	.string "Did you hear? Men in suits tried\n"
	.string "to buy the CRESTFALL gym.\p"
	.string "A MILTANK ate their paperwork.\n"
	.string "I'd have paid to see it.$"

Wendlebury_Text_TraderAfterCrestfall::
	.string "A badge holder at my stall!\n"
	.string "Fresh POKé BALLS, half price.\p"
	.string "...Half price of the price I\n"
	.string "put up this morning.$"

Wendlebury_Text_KidAfterCrestfall::
	.string "They say you went past the\n"
	.string "barricade. No, wait. That's\l"
	.string "the other barricade.\p"
	.string "I'm still not allowed. I checked.$"

Wendlebury_Text_ResidentAAfterCrestfall::
	.string "I hear you've made some noise\n"
	.string "on ROUTE 2. Keep it up.\p"
	.string "It's nice to have a hero. The\n"
	.string "market's lacking one.$"
