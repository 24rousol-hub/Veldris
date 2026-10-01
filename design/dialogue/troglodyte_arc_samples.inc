@ Troglodyte arc SAMPLE LINES. Status: PROPOSED, not wired into any map. See design/troglodyte-arc.md.
@ Author decision 2026-10-01: Troglodyte follows ARC A (contemptuous, then humbled). Arc B is NOT chosen.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/troglodyte_arc_samples.inc
@ Naming: F1..F8 = his fights in order. _A = Arc A (the chosen arc). _B = Arc B (UNUSED, kept at the end).
@ Fights: F1 Hollowbrook, F2 gym 1 Crestfall, F3 gym 3 Ghost, F4 gym 5 Ice, F5 gym 6 Flying (skyscraper city, parents),
@ F6 gym 7 Poison, F7 Victory Road, F8 finale just before the Champion (an aged Cynthia, not Troglodyte).
@ Pokemon only, no real animals. Swearing stays PG-13 and is punctuation only. No {RIVAL}.

@ ---------- F1: outside the lab, Hollowbrook (Sneer) ----------
TroglodyteArc_Text_F1_Intro::
	.string "Don't look at me like that.\n"
	.string "I had a grandfather to meet.\p"
	.string "Fine. You can be my warm-up.\n"
	.string "Try not to cry on the grass.$"

TroglodyteArc_Text_F1_Defeat::
	.string "That's... a fluke. The grass\n"
	.string "was wet. It's the grass's fault.$"

@ ---------- F2: gym 1, Crestfall, Scheme 1 (Sneer) ----------
TroglodyteArc_Text_F2_Intro::
	.string "My family paid for this scene.\n"
	.string "Nobody is enjoying it.\p"
	.string "Sir Biscuit and I will end it.\n"
	.string "Quickly, before the smell sets in.$"

TroglodyteArc_Text_F2_Defeat::
	.string "Sir Biscuit, stop looking at\n"
	.string "me like that. Damn it.$"

@ ---------- F3: gym 3, Ghost, the haunting film crew (Sneer) ----------
TroglodyteArc_Text_F3_Intro::
	.string "A third town. They all look\n"
	.string "the same. Smaller than my pool.\p"
	.string "Go on. Lose politely.$"

TroglodyteArc_Text_F3_DefeatA::
	.string "Again?! Nobody at home will\n"
	.string "believe this. I barely believe it.$"

@ ---------- F4: gym 5, Ice, the lake (Sneer, last of it) ----------
TroglodyteArc_Text_F4_IntroA::
	.string "Five towns of peasants cheering\n"
	.string "for you. It's frankly rude.\p"
	.string "I'll put a stop to that.$"

TroglodyteArc_Text_F4_DefeatA::
	.string "You cheat. It has to be that.\n"
	.string "Nothing else makes sense.$"

@ ---------- F5: gym 6, Flying, the skyscraper city, parents watch (Crack) ----------
TroglodyteArc_Text_F5_IntroA::
	.string "Mother and Father are watching\n"
	.string "from the window. Behave.\p"
	.string "...No. Don't. I want you to lose\n"
	.string "where they can see it.$"

TroglodyteArc_Text_F5_DefeatA::
	.string "They saw that. Everyone saw\n"
	.string "that. I'm going to be sick.$"

@ Optional beat after F5: the parents' tip fails, and he hears it.
TroglodyteArc_Text_F5_AfterA::
	.string "Father tried to buy the badge.\n"
	.string "They said no. Twice. Kindly.\p"
	.string "...Nobody has ever said no to\n"
	.string "him kindly. I didn't like it.$"

@ ---------- F6: gym 7, Poison (Work: trains for real, stiff) ----------
TroglodyteArc_Text_F6_IntroA::
	.string "No jokes this time. No dog.\n"
	.string "I've been training. Properly.\p"
	.string "Well. Sort of. There was a man.$"

TroglodyteArc_Text_F6_DefeatA::
	.string "You were... better. I won't say\n"
	.string "it twice. Don't make me.$"

@ ---------- F7: Victory Road (Work, nearly done) ----------
TroglodyteArc_Text_F7_IntroA::
	.string "I walked here. All of it.\n"
	.string "My feet hurt. It's disgusting.\p"
	.string "Fight me. Properly. Please.$"

TroglodyteArc_Text_F7_DefeatA::
	.string "I have lost to you, fairly.\n"
	.string "Gosh. That felt strange.$"

@ ---------- F8: the finale, just before the Champion, Cynthia (Humbled) ----------
TroglodyteArc_Text_F8_IntroA::
	.string "This is the last one before the\n"
	.string "Champion. I've earned it.\p"
	.string "Nobody paid for it. Show me\n"
	.string "what you've got.$"

TroglodyteArc_Text_F8_DefeatA::
	.string "Well fought. I mean it. Go and\n"
	.string "beat her. I'll write to Grandfather.$"

@ Optional beat after F8 (Option A: a plain concession).
TroglodyteArc_Text_F8_AfterA::
	.string "I was a prat. You knew. They\n"
	.string "all knew. Thank you for not saying.$"

@ =====================================================================
@ UNUSED: ARC B (oblivious and confused). NOT CHOSEN (author, 2026-10-01).
@ Kept for reference only. Nothing below may be wired in. Do not delete.
@ =====================================================================

TroglodyteArc_Text_F3_DefeatB::
	.string "Wait. My team is supposed to\n"
	.string "win. That was the whole plan.$"

TroglodyteArc_Text_F4_IntroB::
	.string "I sent the money. I signed\n"
	.string "the forms. Why does it keep\l"
	.string "happening to me?$"

TroglodyteArc_Text_F4_DefeatB::
	.string "Is this how it normally goes?\n"
	.string "Nobody ever told me.$"

TroglodyteArc_Text_F5_IntroB::
	.string "Mother says I should be nicer.\n"
	.string "I don't know how. Nobody\l"
	.string "showed me.$"

TroglodyteArc_Text_F5_DefeatB::
	.string "Mother says it's a learning\n"
	.string "experience. What am I learning?$"

TroglodyteArc_Text_F6_IntroB::
	.string "You keep winning, and I don't\n"
	.string "know what you want from me.\p"
	.string "I'd ask, but my phone has no\n"
	.string "number for that.$"

TroglodyteArc_Text_F6_DefeatB::
	.string "Oh. That's it, then. Is there\n"
	.string "a prize for second? Or third?$"

TroglodyteArc_Text_F7_IntroB::
	.string "Everyone keeps telling me\n"
	.string "the rules. I keep missing them.\p"
	.string "Shall we just get on with it?$"

TroglodyteArc_Text_F7_DefeatB::
	.string "I lost. I think I lost. It was\n"
	.string "quite nice, in a way.$"

TroglodyteArc_Text_F8_IntroB::
	.string "I'm told this is the big one.\n"
	.string "I still don't know why I'm here.\p"
	.string "But I'll try my best.$"

TroglodyteArc_Text_F8_DefeatB::
	.string "Is that it? Did I do it right?\n"
	.string "I'll go and ask Grandfather.$"
