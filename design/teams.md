# Trainer teams

Status: **PROPOSED** unless marked. Levels and the number of Pokémon per trainer are the author's (2026-09-29). Species and moves are my proposal. Blocks use the `src/data/trainers.party` format so they can be pasted in later. **None of these are in `src/data/trainers.party` yet**: there is no map, no pic or class is chosen, and each needs a trainer id (see `CLAUDE.md`, 'A new trainer').

Moves are checked against the learnsets this ROM actually uses (`P_LVL_UP_LEARNSETS` is `GEN_LATEST`, so `gen_9.h`). Each move is learned by that species at or below its level.

## Crestfall gym (gym 1, Normal type, STANDARD BADGE)

| Trainer | Pokémon | Level | Author fixed |
|---|---|---|---|
| Gym trainer 1 | 1 | 9 | count and level |
| Gym trainer 2 | 1 | 10 | count and level |
| Greta | 2 | 10 and 12 | count and levels |

Greenery in the gym is aesthetic only. Every Pokémon here is Normal type.

### Gym trainer 1: ZIGZAGOON, level 9
```
=== TRAINER_CRESTFALL_GYM_1 ===
Name: (TBD)
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: (TBD)
Music: (TBD)
Double Battle: No
AI: Basic Trainer

Zigzagoon
Level: 9
- Tackle
- Sand Attack
- Tail Whip
- Covet
```
The obvious first opponent: a quick Normal type that blinds you with Sand Attack.

### Gym trainer 2: SLAKOTH, level 10
```
=== TRAINER_CRESTFALL_GYM_2 ===
Name: (TBD)
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: (TBD)
Music: (TBD)
Double Battle: No
AI: Basic Trainer

Slakoth
Level: 10
- Scratch
- Yawn
- Encore
- Slack Off
```
It fits his draft lines ('I've been in here for three years. It's very relaxing.'). It is sleepy rather than dangerous, so Yawn is the trap.

### Greta: SKITTY level 10, MILTANK level 12
```
=== TRAINER_CRESTFALL_GRETA ===
Name: GRETA
Class: Leader
Pic: (her ORAS lass picture, see characters.md: needs the engine edits)
Gender: Female
Music: Female
Items: Potion / Potion
Double Battle: No
AI: Basic Trainer

Skitty
Level: 10
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Fake Out
- Tackle
- Sing
- Attract

Miltank @ Oran Berry
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Tackle
- Growl
- Rollout
- Defense Curl
```
- **Skitty opens with Fake Out** (a flinch), then Sing and Attract make it annoying rather than deadly.
- **Miltank is the ace.** Rollout plus Defense Curl is the classic early-game Miltank problem, and she learns nothing better by level 12. **The fight is probably tough for a player with a level 10 to 12 team.** Tell me if you want it softer (drop Defense Curl) or harder.
- IVs (12 each) and the Oran Berry copy the vanilla first gym leader, Roxanne.
- The 12 at level 12 matches Roxanne's first two Pokémon. Greta's two Pokémon are a level 10 and a level 12, as you asked.

## Troglodyte
His team is not drafted yet. His first battle is at Crestfall, in Scheme 1 (see [dialogue/crestfall.inc](dialogue/crestfall.inc)). His Pokémon is one of the three starters on show, at random, so he needs one trainer id per possible starter for each fight (see [story-outline.md](story-outline.md)).
