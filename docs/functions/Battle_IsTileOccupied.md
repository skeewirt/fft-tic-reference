# Battle_IsTileOccupied

- **Address:** `0x140282A7C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_IsTileOccupied(int x, int y, int layer, int flags)`
- **Callers:** sub_14027192C, sub_140271AC0, sub_140271D80, sub_140271EFC, sub_140280170, sub_1402804D8, sub_140281A64, sub_140304F44
- **Callees:** Unit_HasStatusGroup

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests a map tile for the targeting cursor: bounds, terrain passability, the unit standing there and the large-monster exception for jobs 94..96.

## Behavior

- V: the arguments are x in ecx, y in edx, layer in r8d and a flag byte in r9b; negative x or y is rejected.
- V: x is bounded by the map width byte at 0x140C6AD6A and y by the height byte at 0x140C6AD6B; a layer above 1 is rejected.
- V: the cell is indexed as x plus y times width plus layer times 0x100 (a shl by 8) and read from the tile block at 0x140D8DCB0 with a stride of eight bytes.
- V: cell byte +6 bits 0 and 1 must be clear for the tile to be usable.
- V: when the flag byte has bit 2, the cell terrain byte +3 must be below 0x20 and its low five bits at most 2.
- V: it walks the 21 unit records with a stride of 0x200 and returns the slot index of a live unit whose x, y and layer match the tile; the flag byte decides which units can match (bits 0x40, 0x01 and 0x10 test three consecutive marker bytes starting at unit +0x61).
- V: for a job 94..96 unit (job byte +3) Unit_HasStatusGroup(unit, 0xA) is consulted, and a unit that has that group is skipped.
- V: the returns are -2 for a rejected tile, -1 when no unit matches, and on a match the slot index, or byte +0x1B4 masked to 0x1F when that byte is 0x80 or above.
- I: the job 94..96 branch is a monster-specific exemption, which is why this function appears in the monster-test census.
- ?: what status group 0xA contains; the mask table was not decoded here.

## State touched

- Calls: [Unit_HasStatusGroup](Unit_HasStatusGroup.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [MoveFind_ProbeTile](MoveFind_ProbeTile.md), [sub_140271AC0](sub_140271AC0.md), [sub_140271EFC](sub_140271EFC.md)

## Notes

Whole function read (351 bytes). The map dimensions and tile stride come from the cursor-range study; the monster test is in this body.

## Open questions

None recorded.
