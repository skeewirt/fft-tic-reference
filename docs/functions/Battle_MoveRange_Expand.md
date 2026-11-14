# Battle_MoveRange_Expand

- **Address:** `0x14027C138`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRange_Expand(void)`
- **Callers:** Battle_MoveRange_Build, sub_14027DDB8
- **Callees:** Battle_MoveRange_OutOfBounds, Battle_MoveRange_CheckSource, Battle_MoveRange_CheckStep, the four direction setters sub_14027BA20 / sub_14027BA34 / sub_14027BA48 / sub_14027BA68 (through a table)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Spreads the budget from the current frontier tile to its four neighbours.

## Behavior

- V: caches the tile's height * 2, slope (byte +3 low 5 bits) and corner byte (+4) in the scratch.
- V: loops the direction count (8, or 36 from a mounted start): direction = index mod 4 in the order +x, +y, -x, -y (four small setters store the step and two corner shifts: 0 / 2, 6 / 4, 2 / 0, 4 / 6 for the edge left / the edge entered); indices 4 and above set the 'from a unit' byte.
- V: skips the direction when the neighbour is off the map (Battle_MoveRange_OutOfBounds) or Battle_MoveRange_CheckSource returns non-zero; otherwise calls Battle_MoveRange_CheckStep for the four variants 0..3 with extra cost 0.

## State touched

- Calls: [Battle_MoveRange_OutOfBounds](Battle_MoveRange_OutOfBounds.md), [Battle_MoveRange_CheckSource](Battle_MoveRange_CheckSource.md), [Battle_MoveRange_CheckStep](Battle_MoveRange_CheckStep.md)

## Referenced by

- Called by: [Battle_MoveRange_Build](Battle_MoveRange_Build.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Open questions

None recorded.
