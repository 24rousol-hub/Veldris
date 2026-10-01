@ Crestfall EXTRA dialogue DRAFT: the rest of the city's NPCs. Status: PROPOSED, not wired into any map.
@ Companion to crestfall.inc (Scheme 1, Greta, gym trainers, a few townsfolk). No label here repeats one there.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/crestfall_extra.inc
@ Rules: Pokemon only, no real animals. Only the Goldsworth house residents swear (PG-13, a little).
@ Nobody else swears. Single curly quotes for speech. TROGLODYTE is written literally.
@ 'Before' = before the gym is beaten (STANDARD BADGE). 'After' = after it. Scheme 1 happens first, in town.
@ Plan: design/crestfall.md

@ ===================================================================
@ MARKET (stalls in the square)
@ ===================================================================

Crestfall_Text_MarketBerryBefore::
	.string "Fresh BERRIES! Picked this\n"
	.string "morning by people who care.\p"
	.string "The gym's hay maze has been\n"
	.string "bad for trade. Suits keep\l"
	.string "wandering out of it, lost.$"

Crestfall_Text_MarketBerryAfter::
	.string "The suits are gone, the maze is\n"
	.string "quiet, and my BERRIES sell out.\p"
	.string "I'd thank GRETA, but she'd say\n"
	.string "it was the BERRIES.$"

Crestfall_Text_MarketTomato::
	.string "Crestfall tomatoes. Ask anyone.\n"
	.string "No, not her. She's biased.\p"
	.string "Well. Ask anyone else.$"

Crestfall_Text_MarketMilk::
	.string "MOOMOO MILK, straight from the\n"
	.string "MILTANK. Six hundred a bottle.\p"
	.string "It's worth it. I've tried\n"
	.string "the cheap stuff. I'm still\l"
	.string "recovering.$"

@ ===================================================================
@ FARMHANDS (outside the gym, on the road to the farm)
@ ===================================================================

Crestfall_Text_FarmhandFenceBefore::
	.string "I'm meant to be fixing this\n"
	.string "fence. The MILTANK keeps\l"
	.string "helping. It leans on it.\p"
	.string "It's very supportive. And\n"
	.string "it's not helping.$"

Crestfall_Text_FarmhandFenceAfter::
	.string "Heard you beat the boss. Good.\n"
	.string "Maybe she'll be in a mood to\l"
	.string "give us Sunday off.\p"
	.string "...She won't. But it's nice to\n"
	.string "hope.$"

Crestfall_Text_FarmhandBarnBefore::
	.string "Don't go in the barn with\n"
	.string "those suited men. Last I saw,\l"
	.string "one of them was arguing\l"
	.string "with a SLAKOTH.\p"
	.string "The SLAKOTH was winning.\n"
	.string "It hadn't said a word.$"

Crestfall_Text_FarmhandBarnAfter::
	.string "The barn's ours again. The\n"
	.string "SLAKOTH is back in its spot.\p"
	.string "Nobody is sure it ever moved.$"

@ ===================================================================
@ GYM GUIDE STATUE (inside the gym entrance) AND SIGNS
@ ===================================================================

@ Guide statue. Before the gym is beaten.
Crestfall_Text_GymStatueBefore::
	.string "CRESTFALL POKéMON GYM\n"
	.string "Leader: GRETA\p"
	.string "Normal type. No weaknesses\n"
	.string "except FIGHTING. And nerves.\p"
	.string "Winners: no one has signed in\n"
	.string "yet today.$"

@ Guide statue. After the gym is beaten.
Crestfall_Text_GymStatueAfter::
	.string "CRESTFALL POKéMON GYM\n"
	.string "Leader: GRETA\p"
	.string "Winners:\n"
	.string "{PLAYER}$"

Crestfall_Text_FarmSign::
	.string "CRESTFALL FARM\n"
	.string "‘Pick your own. Pay on the\l"
	.string "honour system. We see you.’$"

Crestfall_Text_SquareSign::
	.string "CRESTFALL MARKET SQUARE\n"
	.string "‘Market day is every day.\l"
	.string "Haggling is encouraged.’$"

@ ===================================================================
@ HOUSES (two ordinary houses)
@ ===================================================================

@ House A: a retired couple.
Crestfall_Text_HouseAWifeBefore::
	.string "Those men in suits knocked\n"
	.string "on our door. Asked if we'd\l"
	.string "considered 'relocating.'\p"
	.string "We've lived here forty years.\n"
	.string "We've barely considered lunch.$"

Crestfall_Text_HouseAWifeAfter::
	.string "Quiet again. Lovely.\n"
	.string "The only visitors now are\l"
	.string "people who want tomatoes.\p"
	.string "I'd call that a good trade.$"

Crestfall_Text_HouseAHusband::
	.string "My SKITTY sleeps on the warm\n"
	.string "spot on the stairs. I sleep\l"
	.string "on the cold spot.\p"
	.string "We've agreed not to discuss it.$"

@ House B: a young trainer who is stuck.
Crestfall_Text_HouseBTrainerBefore::
	.string "I was going to challenge\n"
	.string "GRETA today. Really.\p"
	.string "Then I saw her MILTANK.\n"
	.string "I'm going to have lunch first.$"

Crestfall_Text_HouseBTrainerAfter::
	.string "You won! Wow.\n"
	.string "I'll challenge her next year.\p"
	.string "Or the year after. Or I'll\n"
	.string "become a farmer. It's a nice\l"
	.string "life. Mostly.$"

@ ===================================================================
@ KID AND OLD FARMER
@ ===================================================================

@ A second kid, by the square (the first kid is in crestfall.inc).
Crestfall_Text_KidSquareBefore::
	.string "My ZIGZAGOON found a coin\n"
	.string "in the fountain! I'm rich!\p"
	.string "...It's a button. I'm still\n"
	.string "rich. In buttons.$"

Crestfall_Text_KidSquareAfter::
	.string "You're the one who beat GRETA!\n"
	.string "Can I hold your badge?\p"
	.string "Just for a second. I'll give it\n"
	.string "back. Probably.$"

Crestfall_Text_OldFarmerBefore::
	.string "I've farmed here sixty years.\n"
	.string "The soil never asks questions.\p"
	.string "Those suited fellows asked\n"
	.string "about a hundred. All wrong.$"

Crestfall_Text_OldFarmerAfter::
	.string "Sixty years, and I've never seen\n"
	.string "a lawyer flee from a MILTANK.\p"
	.string "Some days, it pays to get up.$"

Crestfall_Text_OldFarmerGoldsworth::
	.string "That big house with the shiny\n"
	.string "gate? The Goldsworths.\p"
	.string "Nobody's seen a Goldsworth\n"
	.string "pick up anything heavier than\l"
	.string "a phone.$"

@ ===================================================================
@ SHOPKEEPER (a second voice at the Mart, alongside the clerk in crestfall.inc)
@ ===================================================================

Crestfall_Text_ShopkeeperBefore::
	.string "I stock POTIONS, POKé BALLS,\n"
	.string "and a few things for hay fever.\p"
	.string "I'd advise a few POTIONS.\n"
	.string "GRETA's SKITTY hits harder\l"
	.string "than it purrs.$"

Crestfall_Text_ShopkeeperAfter::
	.string "A STANDARD BADGE! Fine work.\n"
	.string "I'll say what I tell everyone:\p"
	.string "The next town is further than\n"
	.string "it looks. Bring more POTIONS.$"

@ ===================================================================
@ GOLDSWORTH HOUSE (NPC only, PROPOSED). 2026-10-01: Crestfall is a town and gets NO Goldsworth house. These labels are
@ kept for Briarwick's Goldsworth house (approved 2026-10-01); rename the Crestfall_ prefix to Briarwick_ when that map is built. Cold, tidy, rich. Residents are frat guys who
@ look down on ordinary people. Mild PG-13 swearing, used as punctuation. No slurs.
@ Nobody here is cruel to innocent townsfolk, only rude to the player and to anyone poor.
@ ===================================================================

@ Door sign.
Crestfall_Text_GoldsworthHouseSign::
	.string "GOLDSWORTH RESIDENCE\n"
	.string "‘Deliveries to the side gate.\l"
	.string "Visitors: don't.’$"

@ Cousin 1: the boaster. Before the gym.
Crestfall_Text_GoldCousinBefore::
	.string "Oh, great. A local. Wipe your\n"
	.string "feet. Not on the rug.\p"
	.string "I'm BARNABY GOLDSWORTH. Yes,\n"
	.string "THAT family. Try to keep up.$"

@ Cousin 1: boasting, reads as a second talk.
Crestfall_Text_GoldCousinBoast::
	.string "My family owns this street.\n"
	.string "And the street after that.\p"
	.string "Dad bought a whole island once.\n"
	.string "He lost it. Bought another.\p"
	.string "That's how rich we are. Damn\n"
	.string "right we lose things.$"

Crestfall_Text_GoldCousinBoast2::
	.string "Cousin TROGLODYTE is making a\n"
	.string "real name for himself.\p"
	.string "Bad name, sure. Names cost\n"
	.string "money. He has plenty.$"

@ Cousin 1, after the gym.
Crestfall_Text_GoldCousinAfter::
	.string "You beat some farm girl and\n"
	.string "think it's a big deal?\p"
	.string "Fine. Whatever. Hell, I'd\n"
	.string "pay you to go away.$"

@ Cousin 2: the lounger on the couch.
Crestfall_Text_GoldLoungerBefore::
	.string "Shh. I'm resting. It's a full\n"
	.string "time job in this family.\p"
	.string "Go away. Take your muddy\n"
	.string "boots with you.$"

Crestfall_Text_GoldLoungerAfter::
	.string "Did TROGLODYTE's consultants\n"
	.string "really lose to a barn?\p"
	.string "That's the funniest crap I've\n"
	.string "heard all year. Don't tell him.$"

@ Cousin 3: the one fussing over a Pokémon.
Crestfall_Text_GoldPetOwner::
	.string "My PERSIAN has a better\n"
	.string "pedigree than your whole town.\p"
	.string "It's also bored. Just like me.\n"
	.string "Go entertain it. Or don't.$"

@ Butler. Does not swear, is tired.
Crestfall_Text_GoldButler::
	.string "Welcome to the GOLDSWORTH\n"
	.string "residence. Please do not touch\l"
	.string "anything. Or breathe loudly.\p"
	.string "I have worked here for twenty\n"
	.string "years. It has been an education.$"
