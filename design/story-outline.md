# Story outline

Status: **PROPOSED** unless marked. Only the premise and Greta come from the author.

## The scheme formula

Every gym gets one Goldsworth scheme. Keep the beats the same so the joke builds:

1. **Setup.** The player notices something off in town (a stranger, a new sign, a shut door).
2. **Reveal.** The scheme becomes obvious. It is elaborate and expensive.
3. **Collapse.** It fails, through its own flaw, the townsfolk, or the leader. It never hurts an innocent.
4. **Troglodyte shows up** to see it work. It has not.
5. **Battle.** Troglodyte loses. The gym battle follows as normal.
6. **Humiliation beat.** A short line that lets the player enjoy it.

## Act I: Hollowbrook to Crestfall  (first 3 towns, 3 routes)

| Beat | Where | Notes | Status |
|---|---|---|---|
| Intro and Prof. Fennick | Start town | Intro is C-driven. Text drafted in `data/text/birch_speech.inc` (built, fits the text box). Portrait art still shows Birch | BUILT (text). Tone approved by the author; portrait art still to do |
| Player learns Troglodyte got a head start | Start town | Sets the motive | PROPOSED |
| Route 1, first trainers | Route 1 | Gentle, farm-country | PROPOSED |
| Town 2 | Town 2 | Pokémon Center, shop, first sight of Goldsworth money | PROPOSED |
| Route 2 | Route 2 | Route leads to the gym town | PROPOSED |
| **Scheme 1 at Crestfall** | Crestfall | See below | PROPOSED |
| Gym 1: Greta (Normal) | Crestfall | `TRAINER_CRESTFALL_GRETA` | author fixed leader and type |
| Route 3 gated | Route 3 | Leads on to town 4. Blocked for now | PROPOSED |

### Scheme 1 (PROPOSED example, easy to replace)

Hired "efficiency consultants" turn up to condemn Greta's farmyard gym. Greta lets them inspect it. They get lost in the hay maze, and the inspection ends when her livestock take over the paperwork. Troglodyte arrives to watch, finds the consultants tangled in the barn, and has to battle anyway.

## Acts II to IV

| Act | Gyms | Notes |
|---|---|---|
| II | 2 to 4 | TBD |
| III | 5 to 7 | TBD |
| IV | 8 and 9, Elite Four, Champion | See open decision 1 (badges) and 2 (Champion) in [game-bible.md](game-bible.md) |

## Schemes 2 to 9

| # | Gym town | Type | Scheme | Status |
|---|---|---|---|---|
| 1 | Crestfall | Normal | See above | PROPOSED |
| 2 to 9 | TBD | TBD | TBD | Not started |

## Post-game

TBD by the author.

## Cutscene rule

Cutscenes fire from `coord_event` triggers, not `MAP_SCRIPT_ON_TRANSITION`. Every trigger needs a flag or var in [flags.md](flags.md).
