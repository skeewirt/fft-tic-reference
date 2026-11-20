# UnitThatBlocksItsAlliesInMoveRanges

- **Kind:** observed behaviour
- **Scope:** engine (job table row +25 bit 7)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [UnitWork_ApplyJobRow](../functions/UnitWork_ApplyJobRow.md), [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A job whose table row has bit 7 of byte +25 set makes its units block the tiles they stand on for their own side's movement, unless the moving unit has the bit too.

## Behavior

- V: UnitWork_ApplyJobRow copies row +25 bit 7 to unit byte +81 bit 0x40 (row +25 & 0x7F is the Jump).
- V: Battle_MoveRangeSetup stores the acting unit's bit in byte_141882622 and each blocker's bit in bit 7 of its blocker layer byte (the bit is cleared for a blocker whose +99 & 6 is non-zero).
- V: Battle_MoveRange_InitTiles: on a tile held by a same-side unit, tile flag 0x08 is set when the blocker has the bit and the acting unit has not; an enemy's tile gets the same flag in movement mode 0.
- I: flag 0x08 means the tile cannot be entered or crossed (it is the flag an enemy's tile gets).
- M: stock jobs with the bit: 72, 130..141, 145, 168.

## Open questions

? how the range expansion treats flag 0x08 on a same-side tile in every movement mode.
