# tbl_AiStatusValue

- **Kind:** global
- **Address:** `0x1407B22F0`
- **Type:** `battle ai`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

int16[40]: how much each status (index = status id) is worth to a unit in the AI's score of a simulated outcome, on the scale where full HP is 128: Crystal / KO / Chest -192, Traitor -231, Stone / Vampire -116, Doom -103, Stop / Silence -90, Blindness / Confusion / Charmed / Disable -64, Toad -52, Undead / Berserk / Slow / Sleep / Immobilize -39, Critical -32, Poison / Chicken -26, Oil / Atheist -7, Faith 6, Float 12, Haste 19, Regen / Protect / Shell / Reflect 25, Invisibility 38, Reraise 51, id 31 64; Readying, Jumping, Evading, Performing and ids 0 / 14 0. Read only by Battle_AITurnRun

## Referenced by

- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md)

## Open questions

None recorded.
