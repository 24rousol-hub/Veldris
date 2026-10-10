# The Goldsworth houses and the tower (all PROPOSED)

Dialogue: [dialogue/goldsworth.inc](dialogue/goldsworth.inc), width-checked, not wired. Every name below is PROPOSED. Fixed by the author: a house in every city, Hollowbrook as the one town with a house, the skyscraper in one city with Troglodyte's parents, mild swearing for Goldsworths only, and the grandfather's post-game reveal. See [characters.md](characters.md) and [story-outline.md](story-outline.md).

> **Villain teams (author, 2026-10-04):** the growing anti-rich mood (the Commons and the Drowned Crown) has driven the other wealthy families out of Veldris; **only the Goldsworths stayed, and not even the whole family** (author). PROPOSED: some city houses are therefore empty or boarded up. The family is **not to blame** for the Crown's old grudge (its fame starts with Gatsby), but the Crown sees it as the biggest obstacle: in-region influence and ties to outside powers. The Commons leader comes to see the family is not evil after losing to the player and Troglodyte. See [factions.md](factions.md).

## 1. Hollowbrook_GoldsworthHouse (post-game only)

The door note and the bench scenes stay in [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc). The interior opens after `FLAG_SYS_GAME_CLEAR`.

| Who | Role | Labels |
|---|---|---|
| Gatsby Goldsworth | Kind, thanks the player, explains nothing about where he was yet, hints at an old friend who writes letters | `Hollowbrook_Text_GHGatsby*` |
| Mrs. Pell (housekeeper) | Fussy and warm, loyal, knows about the letters but never pried | `Hollowbrook_Text_GHHousekeeper*` |
| Photo, bookshelf | Object text | `Hollowbrook_Text_GHPhoto`, `GHBookshelf` |

What the player can learn: Gatsby is grateful and in no hurry to explain. He has an old friend who writes by post. The house was kept ready while he was away.

Foreshadowing secrets (the reveal is the author's; these only point at it):
- The letters come in thick envelopes on good paper, once with a League crest (Mrs. Pell).
- The faded photo shows a young Gatsby shaking hands with a stranger, a trophy behind them.
- The bookshelf has one worn book on battling in another region.
- A locked drawer that Gatsby keeps the key to. Suggested payoff: it holds the friend's letters, opened once the reveal happens.
- 'Not yet. Soon, perhaps.' leaves the door open for a later scene.

## 2. Cousin templates for the cities' houses

All share one layout ([map-plan.md](map-plan.md)), NPC only, no trainers, no ids. Before/after keys off the city's scheme being beaten. Six voices, so each house can pick two or three and none repeat. Swearing is light (hell, damn, shit) and never aimed at townsfolk.

| Cousin | Type | Before | After |
|---|---|---|---|
| Chad | Boaster | Vase worth more than your town | Lost a yacht's worth on the scheme |
| Trip | Lounger | Stand out of my light | Beau couldn't plan a nap |
| Biff | Gym rat | Flexes in the mirror | Even his form is better than Beau's |
| Prescott | Wine snob | 1984 vintage, wasted on you | Must pay for his own dinner |
| Kip | Pet owner (PERSIAN, Duchess) | Don't pet her | Duchess looks embarrassed |
| Winston | Phone talker | Tries to buy the town | Town was not for sale |

Plus `Goldsworth_Text_HouseSign`. Suggested split: Crestfall's existing BARNABY set stays separate, and these six cover the other cities. The player learns the family is loud, shallow and always a step behind its own schemes. Optional seed for later: they never mention the grandfather, or call him 'the old man who sold out'.

## 3. Troglodyte's parents (skyscraper city, name undecided)

Label prefix `Skyscraper_Text_`. Mr. Goldsworth (III) and Mrs. Goldsworth. Oblivious, patronising, never cruel. They do not swear. Whitmore is a PROPOSED assistant name, used only in one line.

- Scene 1, first meeting (`MrMeet*`, `MrsMeet*`): the player is offered a mailroom job, and they treat badges as a club. They admit to trying to buy gyms and cannot see why nobody sold.
- Scene 2, after their son's defeat (`MrAfter*`, `MrsAfter*`): they cannot work out who to fire and ask, sincerely, what ordinary people want. Mrs. Goldsworth thanks the player for being patient. Mr. Goldsworth wishes his father would pick up the phone.

What the player can learn: the parents are a different kind of problem from the cousins. They mean well, so the fix is understanding rather than punishment. It fits the arc where Troglodyte may turn oblivious and confused.

Foreshadowing: Mr. Goldsworth's father 'never picks up'. Nobody in the family knows Gatsby's whereabouts, matching the author's fixed beat.

## Open questions for the author

1. Names (Mrs. Pell, cousins, Whitmore, Mr. and Mrs.) and the skyscraper city.
2. Which cousins go in which city, and whether some houses carry a scheme beat instead of a joke.
3. Whether the locked drawer and photo are the right seeds for the Champion reveal.
