# Battle_MoveRange_ExpandJump

- **Address:** `0x14027C5E0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRange_ExpandJump(void)`
- **Callers:** Battle_MoveRange_Build, sub_14027DDB8
- **Callees:** Battle_MoveRange_CheckSource, Battle_MoveRange_OutOfBounds, Battle_MoveRange_GapBlocked, Battle_MoveRange_CheckStep, the four direction setters (through a table)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Spreads the budget from the current frontier tile by horizontal jumps: in each of the four straight lines, over 1 up to Jump / 2 tiles.

## Behavior

- V: same direction loop as Battle_MoveRange_Expand; a direction is tried only when Battle_MoveRange_CheckSource returns 0.
- V: for n = 1 .. horizontal jump (scratch byte 0x141882605): stops when the source budget - n is below 2, when the tile n steps away is off the map, or when Battle_MoveRange_GapBlocked says that column blocks the jump at the height the unit leaves from; then takes the tile n + 1 steps away, stops when it is off the map, and calls Battle_MoveRange_CheckStep for the four variants with extra cost n.
- V: so every tile jumped over must itself be clear, in order; a blocked column ends the whole line.
- V: Battle_MoveRange_Build does not call it when the no-jump byte is set (Fly and Teleport).

## State touched

- Calls: [Battle_MoveRange_CheckSource](Battle_MoveRange_CheckSource.md), [Battle_MoveRange_OutOfBounds](Battle_MoveRange_OutOfBounds.md), [Battle_MoveRange_GapBlocked](Battle_MoveRange_GapBlocked.md), [Battle_MoveRange_CheckStep](Battle_MoveRange_CheckStep.md)
- Reads: [MoveRangeScratch.horizontal_jump](../structs/MoveRangeScratch.md#horizontal_jump)

## Referenced by

- Called by: [Battle_MoveRange_Build](Battle_MoveRange_Build.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Captures: with Jump 3 (horizontal jump 1) the lit sets need this routine in three of eight captures, and a jump of 2 would light too much in two.

## Open questions

None recorded.
