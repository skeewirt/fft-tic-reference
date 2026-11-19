# ActiveUnit_OverheadMark

- **Address:** `0x140265284`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void ActiveUnit_OverheadMark(void *scene)`
- **Callers:** sub_1402707A8
- **Callees:** sub_1402607C0, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1400D3150, sub_140028B10, sub_1400FDC48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Places the overhead mark of the active unit.

## Behavior

- V: reads the CharShape row's height (+0x2C) of the active unit's shape as a float for the mark's height.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours; only the height read was examined.

## Open questions

None recorded.
