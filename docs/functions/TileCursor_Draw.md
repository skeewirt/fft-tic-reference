# TileCursor_Draw

- **Address:** `0x140264658`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void TileCursor_Draw(void *scene)`
- **Callers:** sub_1402701D8
- **Callees:** sub_1402641DC, sub_140028B10, Battle_FindUnitNodeAt, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1400D3150, sub_140261E28, sub_1402642F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the tile cursor marker over the unit at the cursor tile.

## Behavior

- V: the marker position is the same base plus CharShape height sum as CursorUnit_TopPoint, plus the bob offset from the table indexed by the frame.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
