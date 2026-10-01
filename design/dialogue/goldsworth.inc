@ GOLDSWORTH dialogue DRAFT: Hollowbrook house (post-game), cousin templates, the parents. Status: PROPOSED, not wired.
@ Plan: design/goldsworth.md. No label here repeats one in hollowbrook.inc or crestfall_extra.inc.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/goldsworth.inc
@ Rules: Pokemon only, no real animals. Only Goldsworths swear (PG-13, a little). Gatsby never swears.
@ Single curly quotes for speech. TROGLODYTE is written literally. Names are PROPOSED.

@ ===================================================================
@ 1. HOLLOWBROOK_GOLDSWORTHHOUSE (post-game only, after FLAG_SYS_GAME_CLEAR)
@ Gatsby sits in the armchair. The housekeeper is MRS. PELL (name PROPOSED).
@ ===================================================================

Hollowbrook_Text_GHGatsbyWelcome::
	.string "{PLAYER}. Come in, come in.\n"
	.string "Mind the rug. It's older than\l"
	.string "my grandson's manners.\p"
	.string "Thank you for coming. I wanted\n"
	.string "to do this properly, indoors.$"

Hollowbrook_Text_GHGatsbyThanks::
	.string "You were kind to him, in your\n"
	.string "way. You beat him, but you\l"
	.string "never crushed him.\p"
	.string "That is harder than it looks,\n"
	.string "and I am grateful.$"

Hollowbrook_Text_GHGatsbyWhere::
	.string "You're wondering where I was\n"
	.string "the day he came. I know.\p"
	.string "Not yet. It's not a story for\n"
	.string "a tea break. Soon, perhaps.$"

Hollowbrook_Text_GHGatsbyFriend::
	.string "I have an old friend who still\n"
	.string "writes to me, the proper way.\p"
	.string "Paper, stamps, terrible\n"
	.string "handwriting. I do love it.$"

Hollowbrook_Text_GHGatsbyIdle::
	.string "Sit, {PLAYER}. Have a biscuit.\n"
	.string "SKITTY has had two already,\l"
	.string "so hurry.$"

Hollowbrook_Text_GHHousekeeperHello::
	.string "Oh, you're the one from the\n"
	.string "lab. Wipe your feet, dear.\p"
	.string "He's been smiling all week.\n"
	.string "I don't know what to do\l"
	.string "with him.$"

Hollowbrook_Text_GHHousekeeperGone::
	.string "When he was away, I kept the\n"
	.string "lamp lit and the post sorted.\p"
	.string "He never said where. I never\n"
	.string "asked. That's the job.$"

Hollowbrook_Text_GHHousekeeperLetters::
	.string "The letters from that friend\n"
	.string "always come in thick envelopes.\p"
	.string "Good paper. Sealed with a\n"
	.string "little League crest, once.\l"
	.string "I didn't look. Much.$"

Hollowbrook_Text_GHHousekeeperDrawer::
	.string "That drawer is locked, dear.\n"
	.string "Not by me. He has the key.\p"
	.string "Don't look at me like that.$"

Hollowbrook_Text_GHPhoto::
	.string "A faded photo. A young man in\n"
	.string "a grand coat shakes hands with\l"
	.string "a smiling stranger.\p"
	.string "A trophy glints behind them.$"

Hollowbrook_Text_GHBookshelf::
	.string "Ledgers, atlases and one very\n"
	.string "worn book about POKéMON\l"
	.string "battling in another region.$"

@ ===================================================================
@ 2. COUSIN TEMPLATES (NPC only, reused by the cities' Goldsworth houses)
@ Before = before the player beats Troglodyte's scheme in that city. After = once it has failed.
@ ===================================================================

@ Cousin A: CHAD (the boaster)
Goldsworth_Text_ChadBefore::
	.string "Oh, great. A commoner in the\n"
	.string "foyer. Don't touch anything.\p"
	.string "That vase is worth more than\n"
	.string "your whole damn town.$"

Goldsworth_Text_ChadAfter::
	.string "Beauregard's plan fell apart?\n"
	.string "Shit. I had money on it.\p"
	.string "Actual money. Not a lot.\n"
	.string "Like, a yacht's worth.$"

@ Cousin B: TRIP (the lounger)
Goldsworth_Text_TripBefore::
	.string "Bro. You're standing in my\n"
	.string "light. Move. Yeah, there.\p"
	.string "Nobody told me the help could\n"
	.string "battle. Adorable.$"

Goldsworth_Text_TripAfter::
	.string "So the big scheme flopped.\n"
	.string "Hell, I'm not even surprised.\p"
	.string "Beau couldn't plan a nap.$"

@ Cousin C: BIFF (the gym rat who never wins)
Goldsworth_Text_BiffBefore::
	.string "I bench more than your whole\n"
	.string "team, bud. Watch me flex.\p"
	.string "No, wait, the mirror's better.\n"
	.string "Stay there, be my audience.$"

Goldsworth_Text_BiffAfter::
	.string "Beau lost to YOU? Damn.\n"
	.string "And I thought my form was bad.\p"
	.string "Fine. Good for you. Get out.$"

@ Cousin D: PRESCOTT (the wine snob)
Goldsworth_Text_PrescottBefore::
	.string "Careful, that's a 1984 vintage.\n"
	.string "Older than you, and classier.\p"
	.string "I'd offer you a glass, but it\n"
	.string "would be wasted. Sorry.$"

Goldsworth_Text_PrescottAfter::
	.string "The scheme collapsed, I hear.\n"
	.string "How very... inconvenient.\p"
	.string "Hell. Now I have to pay for\n"
	.string "my own dinner again.$"

@ Cousin E: KIP (the pet owner, with a Pokémon)
Goldsworth_Text_KipBefore::
	.string "This is my PERSIAN, Duchess.\n"
	.string "She eats better than you.\p"
	.string "Don't pet her. Your hands are\n"
	.string "probably full of dirt.$"

Goldsworth_Text_KipAfter::
	.string "Duchess and I saw the news.\n"
	.string "Another Goldsworth flop.\p"
	.string "She looks embarrassed. I'm not.\n"
	.string "Okay, a little. Damn it.$"

@ Cousin F: WINSTON (the talker on the phone)
Goldsworth_Text_WinstonBefore::
	.string "Hold on, I'm on the phone.\n"
	.string "No, not you. The other you.\p"
	.string "Yes, I'll buy the town. Is it\n"
	.string "for sale? Everything is.$"

Goldsworth_Text_WinstonAfter::
	.string "Cancel the purchase. The\n"
	.string "scheme's dead, the town's\l"
	.string "not for sale. Shit.\p"
	.string "Some people are just rude\n"
	.string "about money.$"

@ Shared sign, any city's Goldsworth house.
Goldsworth_Text_HouseSign::
	.string "GOLDSWORTH RESIDENCE\n"
	.string "Deliveries round the back.\l"
	.string "Visitors, not at all.$"

@ ===================================================================
@ 3. TROGLODYTE'S PARENTS (the skyscraper city, name undecided)
@ MR. GOLDSWORTH (III) and MRS. GOLDSWORTH. Oblivious and patronising, not cruel.
@ ===================================================================

@ Scene 1: first meeting, in the top-floor office.
Skyscraper_Text_MrMeet1::
	.string "Ah. A visitor. Splendid.\n"
	.string "Did Whitmore send you? No?\p"
	.string "Then you must be the person\n"
	.string "our boy keeps mentioning.$"

Skyscraper_Text_MrMeet2::
	.string "He says you're 'a nuisance.'\n"
	.string "I told him that's what hired\l"
	.string "people are for.\p"
	.string "Have you considered a job?\n"
	.string "We have a mailroom.$"

Skyscraper_Text_MrsMeet1::
	.string "Darling, don't frighten the\n"
	.string "child. Such a plucky little\l"
	.string "thing, with all those badges.\p"
	.string "Do they give those away?\n"
	.string "Is it a sort of club?$"

Skyscraper_Text_MrsMeet2::
	.string "We only want Beauregard to have\n"
	.string "a fair chance, you understand.\p"
	.string "We just bought a few gyms.\n"
	.string "Well, tried. Nobody would sell.\p"
	.string "Isn't that odd?$"

Skyscraper_Text_MrMeet3::
	.string "Well, off you run. Do see\n"
	.string "yourself out. The lift is\l"
	.string "the shiny door.$"

@ Scene 2: after their son's defeat.
Skyscraper_Text_MrAfter1::
	.string "So. Beauregard lost again.\n"
	.string "To you, of all people.\p"
	.string "I'd be furious, but I simply\n"
	.string "can't work out who to fire.$"

Skyscraper_Text_MrsAfter1::
	.string "He rang us, in tears. We\n"
	.string "offered to buy him a new\l"
	.string "League. He said that wasn't\l"
	.string "the point.\p"
	.string "What is the point, then?$"

Skyscraper_Text_MrAfter2::
	.string "You seem a decent sort.\n"
	.string "Tell me honestly. What do\l"
	.string "people like you want?$"

Skyscraper_Text_MrsAfter2::
	.string "Yes, we're curious. Not in an\n"
	.string "unkind way. We've simply never\l"
	.string "asked anyone before.$"

Skyscraper_Text_MrsAfterThanks::
	.string "Well. Thank you for being so\n"
	.string "patient with us. Most people\l"
	.string "just send a lawyer.\p"
	.string "Do take a sandwich. They're\n"
	.string "very small, but very dear.$"

Skyscraper_Text_MrAfterIdle::
	.string "I'm told I ought to call my\n"
	.string "father more often. Hm.\p"
	.string "He never picks up. Odd.$"
