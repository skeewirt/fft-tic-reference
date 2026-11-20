# Status_ListSortKey

- **Address:** `0x1400FAB3C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Status_ListSortKey(unsigned int status)`
- **Callers:** CompareFunction
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the sort key of a status in the Status screen lists, from its UIStatusEffect text row.

## Behavior

- V: the same bound (-1 for an id above 39) and the same row lookup as Status_ListCategory (nxd 57, key status + 1).
- V: returns the signed word at row +0x20 (the sort_order column: 1 Protect, 2 Shell, 3 Regen, 21 Poison, 39 Doom ...).
- V: its only caller is CompareFunction, the qsort comparator of the Status screen lists (smaller key first).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md), [StatusSignalAndVoiceColumns](../behaviors/StatusSignalAndVoiceColumns.md)

## Notes

Name is ours.

## Open questions

None recorded.
