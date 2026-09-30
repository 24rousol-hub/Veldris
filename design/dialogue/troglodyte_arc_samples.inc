@ Troglodyte arc SAMPLE LINES. Status: PROPOSED, not wired into any map. See design/troglodyte-arc.md.
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/troglodyte_arc_samples.inc
@ Naming: F1..F8 = his fights in order. _C = contemptuous mode, _A = Arc A, _B = Arc B.
@ Pokemon only, no real animals. Swearing stays PG-13 and is punctuation only. No {RIVAL}.

@ ---------- F1: outside the lab, Hollowbrook (contemptuous, both arcs) ----------
TroglodyteArc_Text_F1_Intro::
	.string "Don't look at me like that.\n"
	.string "I had a grandfather to meet.\p"
	.string "Fine. You can be my warm-up.\n"
	.string "Try not to cry on the grass.$"

TroglodyteArc_Text_F1_Defeat::
	.string "That's... a fluke. The grass\n"
	.string "was wet. It's the grass's fault.$"

@ ---------- F2: Crestfall, Scheme 1 (contemptuous, both arcs) ----------
TroglodyteArc_Text_F2_Intro::
	.string "My family paid for this scene.\n"
	.string "Nobody is enjoying it.\p"
	.string "Sir Biscuit and I will end it.\n"
	.string "Quickly, before the smell sets in.$"

TroglodyteArc_Text_F2_Defeat::
	.string "Sir Biscuit, stop looking at\n"
	.string "me like that. Damn it.$"

@ ---------- F3: gym town 3 (contemptuous) ----------
TroglodyteArc_Text_F3_Intro::
	.string "A third town. They all look\n"
	.string "the same. Smaller than my pool.\p"
	.string "Go on. Lose politely.$"

TroglodyteArc_Text_F3_DefeatA::
	.string "Again?! Nobody at home will\n"
	.string "believe this. I barely believe it.$"

TroglodyteArc_Text_F3_DefeatB::
	.string "Wait. My team is supposed to\n"
	.string "win. That was the whole plan.$"

@ ---------- F4: gym town 5 (Arc A: still contemptuous / Arc B: first cracks) ----------
TroglodyteArc_Text_F4_IntroA::
	.string "Five towns of peasants cheering\n"
	.string "for you. It's frankly rude.\p"
	.string "I'll put a stop to that.$"

TroglodyteArc_Text_F4_IntroB::
	.string "I sent the money. I signed\n"
	.string "the forms. Why does it keep\l"
	.string "happening to me?$"

TroglodyteArc_Text_F4_DefeatA::
	.string "You cheat. It has to be that.\n"
	.string "Nothing else makes sense.$"

TroglodyteArc_Text_F4_DefeatB::
	.string "Is this how it normally goes?\n"
	.string "Nobody ever told me.$"

@ ---------- F5: the tower city, meeting the parents (PROPOSED slot) ----------
TroglodyteArc_Text_F5_IntroA::
	.string "Mother and Father are watching\n"
	.string "from the window. Behave.\p"
	.string "...No. Don't. I want you to lose\n"
	.string "where they can see it.$"

TroglodyteArc_Text_F5_IntroB::
	.string "Mother says I should be nicer.\n"
	.string "I don't know how. Nobody\l"
	.string "showed me.$"

TroglodyteArc_Text_F5_DefeatA::
	.string "They saw that. Everyone saw\n"
	.string "that. I'm going to be sick.$"

TroglodyteArc_Text_F5_DefeatB::
	.string "Mother says it's a learning\n"
	.string "experience. What am I learning?$"

@ ---------- F6: gym town 7 (Arc A: cold and worn down / Arc B: lost) ----------
TroglodyteArc_Text_F6_IntroA::
	.string "No jokes this time. No dog.\n"
	.string "I've been training. Properly.\p"
	.string "Well. Sort of. There was a man.$"

TroglodyteArc_Text_F6_IntroB::
	.string "You keep winning, and I don't\n"
	.string "know what you want from me.\p"
	.string "I'd ask, but my phone has no\n"
	.string "number for that.$"

TroglodyteArc_Text_F6_DefeatA::
	.string "You were... better. I won't say\n"
	.string "it twice. Don't make me.$"

TroglodyteArc_Text_F6_DefeatB::
	.string "Oh. That's it, then. Is there\n"
	.string "a prize for second? Or third?$"

@ ---------- F7: Victory Road (the turn) ----------
TroglodyteArc_Text_F7_IntroA::
	.string "I walked here. All of it.\n"
	.string "My feet hurt. It's disgusting.\p"
	.string "Fight me. Properly. Please.$"

TroglodyteArc_Text_F7_IntroB::
	.string "Everyone keeps telling me\n"
	.string "the rules. I keep missing them.\p"
	.string "Shall we just get on with it?$"

TroglodyteArc_Text_F7_DefeatA::
	.string "I have lost to you, fairly.\n"
	.string "Gosh. That felt strange.$"

TroglodyteArc_Text_F7_DefeatB::
	.string "I lost. I think I lost. It was\n"
	.string "quite nice, in a way.$"

@ ---------- F8: the League finale (only if he is the last fight, open decision 2) ----------
TroglodyteArc_Text_F8_IntroA::
	.string "This is the last one. I've\n"
	.string "earned it. Nobody paid for it.\p"
	.string "Show me what you've got.$"

TroglodyteArc_Text_F8_IntroB::
	.string "I'm told this is the big one.\n"
	.string "I still don't know why I'm here.\p"
	.string "But I'll try my best.$"

TroglodyteArc_Text_F8_DefeatA::
	.string "Well fought. I mean it. Go and\n"
	.string "be Champion. I'll write to Grandfather.$"

TroglodyteArc_Text_F8_DefeatB::
	.string "Is that it? Did I do it right?\n"
	.string "I'll go and ask Grandfather.$"
