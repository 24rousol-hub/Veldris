@ Random and vague NPC dialogue pool DRAFT (2026-10-01). Status: PROPOSED, not wired into any map.
@ Author request: filler lines for ordinary people and trainers, nothing story-centric, usable in ANY town or road.
@ No Goldsworth, Troglodyte, gym or scheme references. Pokemon only (no real animals). Nobody swears.
@ Single curly quotes for speech.
@ Labels: Npc_Text_<Category>_<Name> for people, Npc_Text_<Class><N>_Intro/_Defeat/_After for trainers (3 sets per class).
@ Use any label on any NPC; reusing one line on two NPCs in different towns is fine. Do NOT put the same line on two
@ NPCs inside the same map. Check widths: python3 design/tools/dialogue_check.py design/dialogue/random_npcs.inc

@ ============================================================
@ Townsfolk (any town)
@ ============================================================

Npc_Text_Townsfolk_Gardener::
	.string "The flowers here grow best\nwhen you talk to them.\p"
	.string "Mine only reply with pollen.\nIt's a start.$"

Npc_Text_Townsfolk_Gardener2::
	.string "I water the beds twice a day.\p"
	.string "The beds have never thanked me.\nThe weeds do.$"

Npc_Text_Townsfolk_Baker::
	.string "Fresh loaves! Mostly fresh.\p"
	.string "Today's loaf has a crust you can\nknock on. Like a door.$"

Npc_Text_Townsfolk_Neighbour::
	.string "Lovely weather for staying in.\p"
	.string "I'm going out anyway.\nFor the contrast.$"

Npc_Text_Townsfolk_Neighbour2::
	.string "I put a sign on the gate:\n‘Mind the Pokémon.'\p"
	.string "Nobody minds it.\nThe Pokémon mind everyone.$"

Npc_Text_Townsfolk_Mailperson::
	.string "Letters, parcels, one very\nheavy brick.\p"
	.string "The brick is for the mayor.\nHe ordered it. On purpose.$"

Npc_Text_Townsfolk_Lamplighter::
	.string "I check the lamps at dusk.\p"
	.string "They all work. I check them\nanyway. It's relaxing.$"

Npc_Text_Townsfolk_Window::
	.string "A woman waves from her window.\p"
	.string "Then she closes it.\nThe wave was the whole message.$"

Npc_Text_Townsfolk_Bench::
	.string "I'm saving this seat for a friend.\p"
	.string "He's late.\nI've been saving it for years.$"

Npc_Text_Townsfolk_Fountain::
	.string "They throw coins in the fountain\nand wish for rare Pokémon.\p"
	.string "I just take the coins.\nAnd wish for rare Pokémon.$"

Npc_Text_Townsfolk_Shopper::
	.string "I came for one thing.\p"
	.string "I'm leaving with a hat.\nI don't know whose.$"

Npc_Text_Townsfolk_Reader::
	.string "I'm reading the same page again.\p"
	.string "It improves each time.\nThe page, I mean. Not me.$"

Npc_Text_Townsfolk_Painter::
	.string "I'm painting the square.\p"
	.string "It looks like a blur.\nI'm calling it ‘Impressions.'$"

Npc_Text_Townsfolk_Musician::
	.string "I practise the same song daily.\p"
	.string "The neighbours have learned it.\nSome hum along. Some leave.$"

Npc_Text_Townsfolk_Joker::
	.string "What's a Pokémon's favourite\nkind of tea?\p"
	.string "Chamomile, obviously.\n...No? Oh.$"

Npc_Text_Townsfolk_Dreamer::
	.string "I fell asleep on this bench.\p"
	.string "Woke up. Fell asleep again.\nBest Tuesday I've had.$"

Npc_Text_Townsfolk_Collector::
	.string "I collect buttons.\p"
	.string "Not the Pokémon kind.\nThe coat kind. People stare.$"

Npc_Text_Townsfolk_Greeter::
	.string "Welcome, welcome! I say it to\neveryone. It's my job.\p"
	.string "I'm not employed here.\nI just like the word.$"

Npc_Text_Townsfolk_Crier::
	.string "Oyez! Oyez! The market opens\nat nine!\p"
	.string "It's already ten.\nI'm very early for next week.$"

Npc_Text_Townsfolk_Tidy::
	.string "I sweep this path daily.\p"
	.string "The path stays tidy.\nThe leaves come back by lunch.$"

@ ============================================================
@ Elders
@ ============================================================

Npc_Text_Elders_Grandparent1::
	.string "In my day, we walked uphill\nboth ways.\p"
	.string "It was a very strange\nhill.$"

Npc_Text_Elders_Grandparent2::
	.string "I've seen many trainers pass.\p"
	.string "Most walk. Some run.\nA few trip. I like the trippers.$"

Npc_Text_Elders_Grandparent3::
	.string "My knees predict the weather.\p"
	.string "Today they say ‘maybe.'\nThey're usually right.$"

Npc_Text_Elders_Grandparent4::
	.string "I used to battle.\p"
	.string "Now I sit on this bench and\njudge those who do.$"

Npc_Text_Elders_Grandparent5::
	.string "Pokémon grow when you care for\nthem. Like soup.\p"
	.string "Stir often. Salt sparingly.$"

Npc_Text_Elders_Grandparent6::
	.string "Kids today have it easy.\p"
	.string "They have maps.\nWe had suspicion.$"

Npc_Text_Elders_Grandparent7::
	.string "I don't need a Pokégear.\p"
	.string "I have a very loud neighbour\nwho knows everything.$"

Npc_Text_Elders_Grandparent8::
	.string "Slow and steady wins.\p"
	.string "Unless it's a race.\nThen fast wins. I checked.$"

@ ============================================================
@ Kids
@ ============================================================

Npc_Text_Kids_Kid1::
	.string "I'm going to be the best\ntrainer ever!\p"
	.string "Right after lunch.\nAnd maybe a nap.$"

Npc_Text_Kids_Kid2::
	.string "My Pokémon is the strongest!\p"
	.string "It sleeps a lot.\nThat's how it saves energy.$"

Npc_Text_Kids_Kid3::
	.string "I'm not scared of the tall grass.\p"
	.string "I just prefer the path.\nThe path is more... honest.$"

Npc_Text_Kids_Kid4::
	.string "Do you want to play tag?\p"
	.string "You're it.\nRun.$"

Npc_Text_Kids_Kid5::
	.string "I found a really shiny rock!\p"
	.string "It's a normal rock.\nBut it's shiny in my heart.$"

Npc_Text_Kids_Kid6::
	.string "I can count to a hundred!\p"
	.string "One, two, three...\p"
	.string "...okay, to ten.\nTen's a lot!$"

Npc_Text_Kids_Kid7::
	.string "Mum says I can't battle until\nI'm older.\p"
	.string "So I'm practising my\n‘older' face. See?$"

Npc_Text_Kids_Kid8::
	.string "I drew a Pokémon!\p"
	.string "It has seven legs and no face.\nIt's a very rare one.$"

Npc_Text_Kids_Kid9::
	.string "I'm hiding.\p"
	.string "You didn't see me.\nYou never saw me. Goodbye.$"

Npc_Text_Kids_Kid10::
	.string "I want a Pokémon that can fly!\p"
	.string "Or swim! Or dig!\nOr all three. Is that a thing?$"

Npc_Text_Kids_Kid11::
	.string "I jumped in a puddle.\p"
	.string "It was deeper than it looked.\nWorth it.$"

Npc_Text_Kids_Kid12::
	.string "I'm the king of this hill!\p"
	.string "It's a small hill.\nA very important one.$"

@ ============================================================
@ Workers and shops
@ ============================================================

Npc_Text_WorkersShops_Clerk1::
	.string "We're out of everything.\p"
	.string "Except the thing you want.\nWe have plenty of that.$"

Npc_Text_WorkersShops_Clerk2::
	.string "Everything's priced fairly.\p"
	.string "Fairly confusing, that is.\nAsk me anything.$"

Npc_Text_WorkersShops_Clerk3::
	.string "Buy two, get one free!\p"
	.string "The third one is a pamphlet.\nAbout buying two.$"

Npc_Text_WorkersShops_Cashier::
	.string "Receipt? It's longer than\nyou'd think.\p"
	.string "Mine are legendary.\nIn the sense that they're long.$"

Npc_Text_WorkersShops_Stocker::
	.string "I stack the shelves all day.\p"
	.string "Then someone buys the bottom\none. Everything falls.$"

Npc_Text_WorkersShops_Builder::
	.string "We're building something here.\p"
	.string "We won't say what.\nWe haven't decided.$"

Npc_Text_WorkersShops_Mason::
	.string "Stone by stone. Brick by brick.\p"
	.string "It's slow. But the wall\ndoesn't complain.$"

Npc_Text_WorkersShops_Carpenter::
	.string "I measure twice and cut once.\p"
	.string "Then I measure again.\nJust in case.$"

Npc_Text_WorkersShops_Farmhand::
	.string "The crops are growing nicely.\p"
	.string "Slowly. Which is the nicest\nspeed for crops.$"

Npc_Text_WorkersShops_Miller::
	.string "I grind the grain all day.\p"
	.string "It's very quiet work.\nI hum a lot. Don't tell anyone.$"

Npc_Text_WorkersShops_Cook::
	.string "The special is soup.\p"
	.string "The soup is the special.\nDon't ask which soup.$"

Npc_Text_WorkersShops_Waiter::
	.string "Today's menu is on the board.\p"
	.string "The board is at the back.\nThe back is across the road.$"

Npc_Text_WorkersShops_Mechanic::
	.string "I fix things that break.\p"
	.string "You'd be surprised how\nmany break. On purpose.$"

Npc_Text_WorkersShops_Tailor::
	.string "Hats, scarves, gloves.\p"
	.string "Any Pokémon that fits can\nborrow one. Politely.$"

Npc_Text_WorkersShops_Librarian::
	.string "Shh. This is a library.\p"
	.string "It has no books yet.\nIt has a lot of shushing.$"

Npc_Text_WorkersShops_Postmaster::
	.string "Your letter will arrive soon.\p"
	.string "Soon in the sense of\n‘eventually.'$"

@ ============================================================
@ Route walkers
@ ============================================================

Npc_Text_RouteWalkers_Walker1::
	.string "I walk to clear my head.\p"
	.string "It's working. Nothing's in it.\nIt's lovely.$"

Npc_Text_RouteWalkers_Walker2::
	.string "I'm training for a long walk.\p"
	.string "A very long one.\nStarts tomorrow. Maybe.$"

Npc_Text_RouteWalkers_Walker3::
	.string "The path is long, but the\nviews make up for it.\p"
	.string "The views are mostly trees.$"

Npc_Text_RouteWalkers_Walker4::
	.string "Which way's the nearest town?\p"
	.string "I've been walking in circles.\nIt's a very nice circle.$"

Npc_Text_RouteWalkers_Walker5::
	.string "Watch for the tall grass.\p"
	.string "It makes wild Pokémon jump out.\nSometimes politely.$"

Npc_Text_RouteWalkers_Walker6::
	.string "I bring snacks on every walk.\p"
	.string "Pokémon smell them.\nIt's a negotiation.$"

Npc_Text_RouteWalkers_Walker7::
	.string "My shoes are worn out.\p"
	.string "I'm still wearing them.\nLoyalty.$"

Npc_Text_RouteWalkers_Walker8::
	.string "I got lost. Then I got found.\p"
	.string "Then I got lost again.\nIt's a hobby now.$"

Npc_Text_RouteWalkers_Walker9::
	.string "A short rest, then onward!\p"
	.string "Or maybe a longer rest.\nThen onward. Possibly.$"

Npc_Text_RouteWalkers_Walker10::
	.string "If you hear a rustle, don't\npanic.\p"
	.string "It's probably a Pokémon.\nPanic only if it's two.$"

Npc_Text_RouteWalkers_Camper1::
	.string "I slept under a tree last night.\p"
	.string "It rained. The tree didn't\nhelp. Good tree, though.$"

Npc_Text_RouteWalkers_Camper2::
	.string "The best camp is a flat one.\p"
	.string "I found a flat one.\nIt's also on a slope.$"

Npc_Text_RouteWalkers_Hiker1::
	.string "The air is cleaner up here.\p"
	.string "It's also thinner.\nI breathe a lot more.$"

Npc_Text_RouteWalkers_Hiker2::
	.string "I climbed this hill twice.\p"
	.string "The second time was to\nfetch my hat.$"

Npc_Text_RouteWalkers_Biker::
	.string "I'd cycle faster, but I'd miss\nthe scenery.\p"
	.string "There's a lot of scenery.\nIt's mostly hedge.$"

Npc_Text_RouteWalkers_Photographer::
	.string "I'm taking a photo of nothing.\p"
	.string "It's a very good nothing.\nLook at that horizon.$"

Npc_Text_RouteWalkers_Surveyor::
	.string "I'm counting the trees.\p"
	.string "I lost count at forty.\nStarting over.$"

Npc_Text_RouteWalkers_Traveller1::
	.string "Is this the road to somewhere?\p"
	.string "Everything's the road to somewhere.\nMine's the long one.$"

Npc_Text_RouteWalkers_Traveller2::
	.string "I'm moving house.\p"
	.string "By carrying one chair at a time.\nIt's going slowly.$"

Npc_Text_RouteWalkers_Traveller3::
	.string "I heard the next town has a\nnice market.\p"
	.string "I'll find out. In four days.$"

@ ============================================================
@ Water and coast
@ ============================================================

Npc_Text_WaterCoast_Angler1::
	.string "I've been fishing since dawn.\p"
	.string "Not one bite. Not even a\npolite nibble.$"

Npc_Text_WaterCoast_Angler2::
	.string "The trick is patience.\p"
	.string "And a bigger rod.\nMostly the rod.$"

Npc_Text_WaterCoast_Angler3::
	.string "A strong tug is a good sign.\p"
	.string "A strong tug on my sleeve is\na very bad sign.$"

Npc_Text_WaterCoast_Swimmer1::
	.string "The water's lovely once you're in!\p"
	.string "Getting in is the hard part.\nTake a breath.$"

Npc_Text_WaterCoast_Swimmer2::
	.string "I swim every day.\p"
	.string "I'm not fast.\nI'm very, very consistent.$"

Npc_Text_WaterCoast_Sailor1::
	.string "The sea's calm today.\p"
	.string "That's when it's most suspicious.\nMind the horizon.$"

Npc_Text_WaterCoast_Sailor2::
	.string "I've sailed these waters for years.\p"
	.string "Only once did I get seasick.\nThe year before that.$"

Npc_Text_WaterCoast_Beach1::
	.string "Sand gets everywhere.\p"
	.string "I found some in my sandwich.\nIt added a crunch.$"

Npc_Text_WaterCoast_Beach2::
	.string "I'm building a sandcastle.\p"
	.string "It's the largest in the region.\nBy about a thumb.$"

Npc_Text_WaterCoast_Beach3::
	.string "I come for the sunset.\p"
	.string "It's late today.\nI'll wait. It's worth it.$"

Npc_Text_WaterCoast_Dock1::
	.string "This dock has a loose plank.\p"
	.string "Third from the left.\nI won't say which left.$"

Npc_Text_WaterCoast_Dock2::
	.string "The boats come and go.\p"
	.string "I wave at all of them.\nA few wave back. It's nice.$"

Npc_Text_WaterCoast_Lighthouse::
	.string "The lamp turns all night.\p"
	.string "I've never seen it from the\noutside. Mysterious.$"

Npc_Text_WaterCoast_Shells::
	.string "I'm collecting shells.\p"
	.string "Not the Pokémon kind.\nThe pretty kind.$"

@ ============================================================
@ Caves and mountains
@ ============================================================

Npc_Text_CavesMountains_Miner1::
	.string "It's dark in here.\p"
	.string "I like it.\nIt's quiet, and I don't\lbump into anyone.$"

Npc_Text_CavesMountains_Miner2::
	.string "I dig for treasure.\p"
	.string "So far, I've found rocks.\nI'm still optimistic.$"

Npc_Text_CavesMountains_Spelunker1::
	.string "Follow the cave wall.\p"
	.string "Left hand on it.\nAlways left. Don't ask why.$"

Npc_Text_CavesMountains_Spelunker2::
	.string "I've been in here for hours.\p"
	.string "Or maybe minutes.\nHard to tell. It's dark.$"

Npc_Text_CavesMountains_Guide::
	.string "Mind the stalagmites.\p"
	.string "They're the pointy ones.\nThe ceiling ones are the other kind.$"

Npc_Text_CavesMountains_Echo::
	.string "Hello! Hello! Hello!\p"
	.string "It's always a bit rude\nwhen it repeats me.$"

Npc_Text_CavesMountains_Climber::
	.string "It's steeper than it looks.\p"
	.string "It's also higher than it looks.\nEverything looks smaller.$"

Npc_Text_CavesMountains_Rockhound::
	.string "I sort rocks by mood.\p"
	.string "This one's cheerful.\nThat one's a bit moody.$"

Npc_Text_CavesMountains_Geologist::
	.string "This ridge is very old.\p"
	.string "It's older than my uncle.\nAnd he's old.$"

Npc_Text_CavesMountains_Lost::
	.string "I'm looking for the exit.\p"
	.string "I think I came in from there.\nOr there.$"

@ ============================================================
@ Forest and fields
@ ============================================================

Npc_Text_ForestFields_Forester::
	.string "These trees are older than\nany of us.\p"
	.string "They're also very patient.\nI try to learn.$"

Npc_Text_ForestFields_Berry1::
	.string "The berries are ripe today.\p"
	.string "Some are ripe, some are\nenthusiastic. Be careful.$"

Npc_Text_ForestFields_Berry2::
	.string "I water the berry patch daily.\p"
	.string "The Pokémon eat the best ones.\nWe have an arrangement.$"

Npc_Text_ForestFields_Picker::
	.string "I'm picking flowers.\p"
	.string "Not many. Just the ones\nthat asked.$"

Npc_Text_ForestFields_Scarecrow::
	.string "A scarecrow stands in the field.\p"
	.string "It looks very relaxed.\nPerhaps it isn't a scarecrow.$"

Npc_Text_ForestFields_Farmer1::
	.string "The crops need rain.\p"
	.string "The sky disagrees.\nIt's a negotiation.$"

Npc_Text_ForestFields_Farmer2::
	.string "Harvest is soon.\p"
	.string "I'm preparing by\nworrying a lot.$"

Npc_Text_ForestFields_Shepherd::
	.string "I look after the Pokémon here.\p"
	.string "They don't need it.\nI'm there for moral support.$"

Npc_Text_ForestFields_Haystack::
	.string "A haystack has been rearranged.\p"
	.string "By someone enthusiastic.\nAnd small.$"

Npc_Text_ForestFields_Nature::
	.string "The wind carries seeds\nacross the field.\p"
	.string "Some land on your hat.\nWear it proudly.$"

@ ============================================================
@ Battle fans and tips
@ ============================================================

Npc_Text_BattleFansTips_Fan1::
	.string "I love watching battles!\p"
	.string "I'm not very good at them.\nWatching is easier.$"

Npc_Text_BattleFansTips_Fan2::
	.string "Type matchups are everything.\p"
	.string "Except when they aren't.\nThen it's luck.$"

Npc_Text_BattleFansTips_Fan3::
	.string "A strong Pokémon isn't always\nthe biggest.\p"
	.string "Some of the best are tiny.\nAnd grumpy.$"

Npc_Text_BattleFansTips_Tip1::
	.string "Always carry a spare POTION.\p"
	.string "Or three. It's cheaper\nthan a Pokémon Center nap.$"

Npc_Text_BattleFansTips_Tip2::
	.string "Don't forget to save often.\p"
	.string "Pokémon forget things.\nSo do I.$"

Npc_Text_BattleFansTips_Tip3::
	.string "If a Pokémon looks angry,\ngive it space.\p"
	.string "It's probably not angry.\nIt's probably hungry.$"

Npc_Text_BattleFansTips_Tip4::
	.string "Rest your Pokémon before a\nbig battle.\p"
	.string "A tired Pokémon is a\ngrumpy Pokémon.$"

Npc_Text_BattleFansTips_Tip5::
	.string "Wild Pokémon are shy.\p"
	.string "Say hello before you throw\na ball. It's polite.$"

Npc_Text_BattleFansTips_Tip6::
	.string "Look at the tall grass.\p"
	.string "If it moves for no reason,\nsomething's in there.$"

Npc_Text_BattleFansTips_Tip7::
	.string "Berries heal small hurts.\p"
	.string "Soup heals the rest.\nI'm told.$"

Npc_Text_BattleFansTips_Tip8::
	.string "Repels keep wild Pokémon away.\p"
	.string "They also keep conversation\naway. Choose wisely.$"

Npc_Text_BattleFansTips_Tip9::
	.string "Bring a map.\p"
	.string "Maps don't judge.\nThey only point.$"

Npc_Text_BattleFansTips_Tip10::
	.string "Pokémon that like you\ntry harder.\p"
	.string "It's not a trick.\nIt's just nice.$"

Npc_Text_BattleFansTips_Tip11::
	.string "If you lose, don't mope.\p"
	.string "Eat something and try again.\nThe best rule I know.$"

Npc_Text_BattleFansTips_Tip12::
	.string "Moves you've forgotten can\nbe remembered.\p"
	.string "Ask the right person.\nThey love it.$"

@ ============================================================
@ Weather and time
@ ============================================================

Npc_Text_WeatherTime_Morning::
	.string "Good morning! The air\nsmells of toast.\p"
	.string "Someone's up early.\nI'm taking credit.$"

Npc_Text_WeatherTime_Evening::
	.string "The light is lovely at this\nhour.\p"
	.string "Everything looks like a\npainting. A tidy one.$"

Npc_Text_WeatherTime_Night::
	.string "It's late. The streets are\nempty.\p"
	.string "I love it. Everything\nechoes politely.$"

Npc_Text_WeatherTime_Rain::
	.string "It's raining.\p"
	.string "I brought an umbrella.\nI left it indoors.\lNaturally.$"

Npc_Text_WeatherTime_Sun::
	.string "The sun's out!\p"
	.string "I forgot my hat.\nAnd my sense of caution.$"

Npc_Text_WeatherTime_Wind::
	.string "The wind's quite strong today.\p"
	.string "My hat has gone to find\nitself a new home.$"

Npc_Text_WeatherTime_Fog::
	.string "Fog again.\p"
	.string "I can barely see my own\nhand. It's very polite.$"

Npc_Text_WeatherTime_Snow::
	.string "Snow! Everything's quiet.\p"
	.string "Even the Pokémon.\nEven the loud ones.$"

@ ============================================================
@ Pokémon-lovers
@ ============================================================

Npc_Text_PokmonLovers_Love1::
	.string "I adore every Pokémon.\p"
	.string "Even the grumpy ones.\nEspecially the grumpy ones.$"

Npc_Text_PokmonLovers_Love2::
	.string "My Pokémon follow me everywhere.\p"
	.string "Even to the bathroom.\nI've given up.$"

Npc_Text_PokmonLovers_Love3::
	.string "I talk to Pokémon all day.\p"
	.string "They don't answer.\nThey listen very loudly.$"

Npc_Text_PokmonLovers_Love4::
	.string "Have you ever hugged a\nPokémon?\p"
	.string "Some like it. Some pretend\nto. I respect that.$"

Npc_Text_PokmonLovers_Love5::
	.string "Look at that little face!\p"
	.string "It's judging me.\nI love it.$"

Npc_Text_PokmonLovers_Love6::
	.string "I feed the Pokémon in the\npark.\p"
	.string "Some are shy. Some are\npushy. I like both.$"

Npc_Text_PokmonLovers_Love7::
	.string "Pokémon are like people.\p"
	.string "Mostly. They're more honest\nabout snacks.$"

Npc_Text_PokmonLovers_Love8::
	.string "Naming a Pokémon is hard.\p"
	.string "I changed mine eleven times.\nIt still ignores all of them.$"

@ ============================================================
@ Odd and vague
@ ============================================================

Npc_Text_OddVague_Odd1::
	.string "Did you hear that?\p"
	.string "No? Good.\nNeither did I.$"

Npc_Text_OddVague_Odd2::
	.string "I forgot what I was saying.\p"
	.string "It was important.\nOr maybe it was soup.$"

Npc_Text_OddVague_Odd3::
	.string "Have you seen my hat?\p"
	.string "I'm wearing it.\nI just can't see it.$"

Npc_Text_OddVague_Odd4::
	.string "I walk around the town every\nday.\p"
	.string "It's still here.\nI check.$"

Npc_Text_OddVague_Odd5::
	.string "The fountain has no water.\p"
	.string "I'm worried about it.\nIt's been like that for weeks.$"

Npc_Text_OddVague_Odd6::
	.string "I'm waiting for something.\p"
	.string "I don't know what yet.\nI'll know when it arrives.$"

Npc_Text_OddVague_Odd7::
	.string "If you see a strange person,\ndon't worry.\p"
	.string "It's just me. Wearing\na different hat.$"

Npc_Text_OddVague_Odd8::
	.string "I'm on a very important\nerrand.\p"
	.string "I've forgotten what it is.\nIt's still important.$"

Npc_Text_OddVague_Odd9::
	.string "Everything is exactly where\nit should be.\p"
	.string "It's suspicious.\nCheck again.$"

Npc_Text_OddVague_Odd10::
	.string "I think I left something on.\p"
	.string "Maybe the kettle.\nMaybe the house.\lHard to say.$"

@ ============================================================
@ Trainer class: Youngster
@ ============================================================

Npc_Text_Youngster1_Intro::
	.string "I'm the best on this route!\p"
	.string "Well, second best.\nOkay, third.$"

Npc_Text_Youngster1_Defeat::
	.string "Okay, fourth.\nFine.$"

Npc_Text_Youngster1_After::
	.string "I'll beat you\nnext time!$"

Npc_Text_Youngster2_Intro::
	.string "My shorts are my lucky shorts!\p"
	.string "I wear them daily.$"

Npc_Text_Youngster2_Defeat::
	.string "The shorts failed.\nI'll wash them.$"

Npc_Text_Youngster2_After::
	.string "Maybe I need\nnew luck.$"

Npc_Text_Youngster3_Intro::
	.string "You looked tough.\p"
	.string "So I challenged you.\nBad idea.$"

Npc_Text_Youngster3_Defeat::
	.string "I should have\nchallenged someone smaller.$"

Npc_Text_Youngster3_After::
	.string "I'm taking a nap\nnow.$"

@ ============================================================
@ Trainer class: Lass
@ ============================================================

Npc_Text_Lass1_Intro::
	.string "I like cute Pokémon.\p"
	.string "Also strong Pokémon.\nMostly cute.$"

Npc_Text_Lass1_Defeat::
	.string "Oh, I lost!\p"
	.string "They're still cute.$"

Npc_Text_Lass1_After::
	.string "I'm telling\neveryone how cute\lyou are.$"

Npc_Text_Lass2_Intro::
	.string "My Pokémon and I are best\nfriends.\p"
	.string "Fight us if you dare!$"

Npc_Text_Lass2_Defeat::
	.string "We lost. But we\nstayed friends.$"

Npc_Text_Lass2_After::
	.string "Ice cream\nsolves everything.$"

Npc_Text_Lass3_Intro::
	.string "I practise every morning.\p"
	.string "Mostly stretching.$"

Npc_Text_Lass3_Defeat::
	.string "I should practise\nthe battle part.$"

Npc_Text_Lass3_After::
	.string "I'll stretch\nharder next time.$"

@ ============================================================
@ Trainer class: Bug Catcher
@ ============================================================

Npc_Text_BugCatcher1_Intro::
	.string "I'm looking for rare Pokémon.\p"
	.string "Do you have one?\nI'll battle you for it!$"

Npc_Text_BugCatcher1_Defeat::
	.string "I didn't win.\p"
	.string "I'll look under\nanother rock.$"

Npc_Text_BugCatcher1_After::
	.string "The best catches\nare under rocks.$"

Npc_Text_BugCatcher2_Intro::
	.string "My net is my weapon!\p"
	.string "It's also my hat.$"

Npc_Text_BugCatcher2_Defeat::
	.string "The net has failed me.\p"
	.string "Time for a bigger one.$"

Npc_Text_BugCatcher2_After::
	.string "I'll find a rare\none yet.$"

Npc_Text_BugCatcher3_Intro::
	.string "I love small Pokémon.\p"
	.string "They fit in my pockets.\nMostly.$"

Npc_Text_BugCatcher3_Defeat::
	.string "Okay, that was a\nbig one.$"

Npc_Text_BugCatcher3_After::
	.string "I'll go check\nmy pockets.$"

@ ============================================================
@ Trainer class: Camper
@ ============================================================

Npc_Text_Camper1_Intro::
	.string "I sleep outdoors every night.\p"
	.string "It's good for the soul.\nBad for the back.$"

Npc_Text_Camper1_Defeat::
	.string "My soul needs a\nrest. So does my back.$"

Npc_Text_Camper1_After::
	.string "I'm making soup.\nWant some?$"

Npc_Text_Camper2_Intro::
	.string "Welcome to my campsite!\p"
	.string "Admission is one battle.$"

Npc_Text_Camper2_Defeat::
	.string "Admission paid.\p"
	.string "Enjoy the view.$"

Npc_Text_Camper2_After::
	.string "Sit by the fire\nif you like.$"

Npc_Text_Camper3_Intro::
	.string "I'm a nature expert.\p"
	.string "I once identified a puddle.$"

Npc_Text_Camper3_Defeat::
	.string "Hm. Apparently I\nlack practice.$"

Npc_Text_Camper3_After::
	.string "Nature's\ncomplicated.$"

@ ============================================================
@ Trainer class: Picnicker
@ ============================================================

Npc_Text_Picnicker1_Intro::
	.string "It's a lovely day for a\npicnic!\p"
	.string "And a battle, I suppose.$"

Npc_Text_Picnicker1_Defeat::
	.string "Oh well.\nThe sandwiches are\lstill good.$"

Npc_Text_Picnicker1_After::
	.string "Have a sandwich.\nIt's egg.\lSorry, mostly crumbs.$"

Npc_Text_Picnicker2_Intro::
	.string "My picnic is perfectly\narranged.\p"
	.string "Please don't disturb it.$"

Npc_Text_Picnicker2_Defeat::
	.string "You disturbed it\nbeautifully.$"

Npc_Text_Picnicker2_After::
	.string "I'll re-arrange\nit. Slowly.$"

Npc_Text_Picnicker3_Intro::
	.string "I like the sunshine.\p"
	.string "I like Pokémon.\nI like battles.\lIn that order.$"

Npc_Text_Picnicker3_Defeat::
	.string "Battles are\nthird now.$"

Npc_Text_Picnicker3_After::
	.string "I'll finish my\ntea.$"

@ ============================================================
@ Trainer class: Hiker
@ ============================================================

Npc_Text_Hiker1_Intro::
	.string "I climb mountains for fun.\p"
	.string "You should try it.\nFirst, a battle.$"

Npc_Text_Hiker1_Defeat::
	.string "The summit's\neasier than you.$"

Npc_Text_Hiker1_After::
	.string "I'll take a rest.\nOn a hill.$"

Npc_Text_Hiker2_Intro::
	.string "Rocks are my friends.\p"
	.string "My hat is also my friend.\nI have many friends.$"

Npc_Text_Hiker2_Defeat::
	.string "I lost a friend\ntoday. Me.$"

Npc_Text_Hiker2_After::
	.string "I'll sit down\nand think.$"

Npc_Text_Hiker3_Intro::
	.string "The air's thin up here.\p"
	.string "So is my patience.\nPrepare yourself.$"

Npc_Text_Hiker3_Defeat::
	.string "My patience is\nthinner now.$"

Npc_Text_Hiker3_After::
	.string "I need a snack\nand a sit.$"

@ ============================================================
@ Trainer class: Fisherman
@ ============================================================

Npc_Text_Fisherman1_Intro::
	.string "I've been waiting all day for\na bite.\p"
	.string "You'll have to do.$"

Npc_Text_Fisherman1_Defeat::
	.string "You were a better\nbite than I hoped.$"

Npc_Text_Fisherman1_After::
	.string "Back to the water\nfor me.$"

Npc_Text_Fisherman2_Intro::
	.string "My rod is my pride.\p"
	.string "Please do not touch it.$"

Npc_Text_Fisherman2_Defeat::
	.string "I'll keep it dry.$"

Npc_Text_Fisherman2_After::
	.string "The water is\ncalm. So am I.\lMostly.$"

Npc_Text_Fisherman3_Intro::
	.string "The sea gives and the sea\ntakes.\p"
	.string "Mostly it takes my bait.$"

Npc_Text_Fisherman3_Defeat::
	.string "I lost, but I got\nsome wisdom.$"

Npc_Text_Fisherman3_After::
	.string "I'll try again\ntomorrow.$"

@ ============================================================
@ Trainer class: Swimmer
@ ============================================================

Npc_Text_Swimmer1_Intro::
	.string "The water's perfect!\p"
	.string "Let's battle in it!\nOr near it. Close enough.$"

Npc_Text_Swimmer1_Defeat::
	.string "I'm all wet.\p"
	.string "Not from the water.$"

Npc_Text_Swimmer1_After::
	.string "I'll dry off\nand try again.$"

Npc_Text_Swimmer2_Intro::
	.string "I'm a strong swimmer!\p"
	.string "Okay, I'm an enthusiastic\nswimmer.$"

Npc_Text_Swimmer2_Defeat::
	.string "Enthusiastic isn't\nthe same as winning.$"

Npc_Text_Swimmer2_After::
	.string "I'll just float\nfor a bit.$"

Npc_Text_Swimmer3_Intro::
	.string "I'm training for the big swim.\p"
	.string "It's next month.\nOr next year.$"

Npc_Text_Swimmer3_Defeat::
	.string "I'm still\ntraining.$"

Npc_Text_Swimmer3_After::
	.string "The big swim\nawaits.$"

@ ============================================================
@ Trainer class: Sailor
@ ============================================================

Npc_Text_Sailor1_Intro::
	.string "Ahoy! Prepare to be boarded!\p"
	.string "By a battle, that is.$"

Npc_Text_Sailor1_Defeat::
	.string "I've been sunk.\p"
	.string "Politely.$"

Npc_Text_Sailor1_After::
	.string "The sea\nforgives all.\lMostly.$"

Npc_Text_Sailor2_Intro::
	.string "I've sailed everywhere.\p"
	.string "Twice. In circles.$"

Npc_Text_Sailor2_Defeat::
	.string "I should have used\na compass.$"

Npc_Text_Sailor2_After::
	.string "I'll try the\nother direction.$"

Npc_Text_Sailor3_Intro::
	.string "A sailor never loses.\p"
	.string "He just docks early.$"

Npc_Text_Sailor3_Defeat::
	.string "I've docked.$"

Npc_Text_Sailor3_After::
	.string "Back out to sea\ntomorrow.$"

@ ============================================================
@ Trainer class: Ace Trainer
@ ============================================================

Npc_Text_AceTrainer1_Intro::
	.string "I've trained for years.\p"
	.string "You'll need to do the same.$"

Npc_Text_AceTrainer1_Defeat::
	.string "Impressive.\p"
	.string "I'll train harder.$"

Npc_Text_AceTrainer1_After::
	.string "You have promise.\nDon't waste it.$"

Npc_Text_AceTrainer2_Intro::
	.string "Strength is nothing without\ndiscipline.\p"
	.string "Show me yours.$"

Npc_Text_AceTrainer2_Defeat::
	.string "That was disciplined.$"

Npc_Text_AceTrainer2_After::
	.string "Keep it up.\nIt shows.$"

Npc_Text_AceTrainer3_Intro::
	.string "A true trainer never gives up.\p"
	.string "I'm still here. So are you.$"

Npc_Text_AceTrainer3_Defeat::
	.string "Well fought.$"

Npc_Text_AceTrainer3_After::
	.string "We'll meet\nagain, I'm sure.$"

@ ============================================================
@ Trainer class: Gentleman
@ ============================================================

Npc_Text_Gentleman1_Intro::
	.string "A battle? How delightful.\p"
	.string "Do let me finish my tea.$"

Npc_Text_Gentleman1_Defeat::
	.string "Splendid.\nI lost with\ldignity.$"

Npc_Text_Gentleman1_After::
	.string "One must lose\ngracefully. It's\lvery in.$"

Npc_Text_Gentleman2_Intro::
	.string "I prefer a calm battle.\p"
	.string "Without shouting.\nOr hurry.$"

Npc_Text_Gentleman2_Defeat::
	.string "A calm defeat.\p"
	.string "My favourite kind.$"

Npc_Text_Gentleman2_After::
	.string "Do come again.\nBring biscuits.$"

Npc_Text_Gentleman3_Intro::
	.string "I was born for this.\p"
	.string "Or for the tea.\nPossibly both.$"

Npc_Text_Gentleman3_Defeat::
	.string "I'm well beaten.\p"
	.string "Thank you.$"

Npc_Text_Gentleman3_After::
	.string "Say hello to\nyour Pokémon\lfrom me.$"

@ ============================================================
@ Trainer class: Beauty
@ ============================================================

Npc_Text_Beauty1_Intro::
	.string "I'm only battling because\nthe light is nice.\p"
	.string "Let's begin.$"

Npc_Text_Beauty1_Defeat::
	.string "Oh. Well.\nThat was a\lsurprise.$"

Npc_Text_Beauty1_After::
	.string "I look good\nlosing. Don't I?$"

Npc_Text_Beauty2_Intro::
	.string "A beautiful day for a\nbattle.\p"
	.string "Do try to keep up.$"

Npc_Text_Beauty2_Defeat::
	.string "I lost. The\nlighting is to blame.$"

Npc_Text_Beauty2_After::
	.string "I'll try the\nother side.$"

Npc_Text_Beauty3_Intro::
	.string "I train my Pokémon in the\nmornings.\p"
	.string "The afternoons are for tea.$"

Npc_Text_Beauty3_Defeat::
	.string "A fair defeat.\p"
	.string "Tea time.$"

Npc_Text_Beauty3_After::
	.string "Sit and watch\nthe clouds.$"

@ ============================================================
@ Trainer class: Scientist
@ ============================================================

Npc_Text_Scientist1_Intro::
	.string "This is purely for research.\p"
	.string "Please remain scientifically\ncalm.$"

Npc_Text_Scientist1_Defeat::
	.string "Interesting results.$"

Npc_Text_Scientist1_After::
	.string "I'll write this\ndown. In detail.$"

Npc_Text_Scientist2_Intro::
	.string "My hypothesis is that I'll\nwin.\p"
	.string "Let's test it.$"

Npc_Text_Scientist2_Defeat::
	.string "The hypothesis\nfailed.$"

Npc_Text_Scientist2_After::
	.string "Back to the\nlab.$"

Npc_Text_Scientist3_Intro::
	.string "I study Pokémon behaviour.\p"
	.string "Your behaviour is next.$"

Npc_Text_Scientist3_Defeat::
	.string "Observation: you\nwin.$"

Npc_Text_Scientist3_After::
	.string "I need a bigger\nnotebook.$"

@ ============================================================
@ Trainer class: Cooltrainer
@ ============================================================

Npc_Text_Cooltrainer1_Intro::
	.string "Trainer to trainer: let's\nsee who's tougher.\p"
	.string "Don't hold back.$"

Npc_Text_Cooltrainer1_Defeat::
	.string "Tough. You're\ntougher.$"

Npc_Text_Cooltrainer1_After::
	.string "I'll be back\nstronger.$"

Npc_Text_Cooltrainer2_Intro::
	.string "I've beaten everyone around\nhere.\p"
	.string "You'll be the next.$"

Npc_Text_Cooltrainer2_Defeat::
	.string "Well, I'm not\nbeating you.$"

Npc_Text_Cooltrainer2_After::
	.string "I need to\nrecalibrate.$"

Npc_Text_Cooltrainer3_Intro::
	.string "Strategy beats strength.\p"
	.string "If you're lucky.$"

Npc_Text_Cooltrainer3_Defeat::
	.string "Your luck's\nstrategic.$"

Npc_Text_Cooltrainer3_After::
	.string "I'll consider\nmy moves.$"

@ ============================================================
@ Trainer class: Psychic
@ ============================================================

Npc_Text_Psychic1_Intro::
	.string "I knew you'd challenge me.\p"
	.string "I saw it coming.\nA bit late.$"

Npc_Text_Psychic1_Defeat::
	.string "I foresaw this loss.\p"
	.string "A little late\nagain.$"

Npc_Text_Psychic1_After::
	.string "I keep seeing\nthe future too\llate.$"

Npc_Text_Psychic2_Intro::
	.string "Close your mind.\p"
	.string "No, open it.\nNo, close it.$"

Npc_Text_Psychic2_Defeat::
	.string "My mind is open\nnow. Thanks.$"

Npc_Text_Psychic2_After::
	.string "I'll close it\nagain later.$"

Npc_Text_Psychic3_Intro::
	.string "I sense great potential.\p"
	.string "In myself, mainly.$"

Npc_Text_Psychic3_Defeat::
	.string "My senses were\nwrong.$"

Npc_Text_Psychic3_After::
	.string "Back to\nmeditation.$"

@ ============================================================
@ Trainer class: Black Belt
@ ============================================================

Npc_Text_BlackBelt1_Intro::
	.string "Hiya! I'll test your spirit!\p"
	.string "Also your ankles.$"

Npc_Text_BlackBelt1_Defeat::
	.string "Spirit tested.\nAnkles fine.$"

Npc_Text_BlackBelt1_After::
	.string "Train hard.\nRest harder.$"

Npc_Text_BlackBelt2_Intro::
	.string "My Pokémon and I train at\ndawn.\p"
	.string "We're now fully awake.$"

Npc_Text_BlackBelt2_Defeat::
	.string "I'm awake now.$"

Npc_Text_BlackBelt2_After::
	.string "I'll sleep\ntomorrow.$"

Npc_Text_BlackBelt3_Intro::
	.string "A strong body, a strong mind.\p"
	.string "Mostly the body.$"

Npc_Text_BlackBelt3_Defeat::
	.string "The mind needs\nwork.$"

Npc_Text_BlackBelt3_After::
	.string "Back to the\ndojo.$"
