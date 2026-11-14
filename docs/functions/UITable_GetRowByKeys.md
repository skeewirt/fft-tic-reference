# UITable_GetRowByKeys

- **Address:** `0x1403DBCE4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char *UITable_GetRowByKeys(int tableId, unsigned int key1, unsigned int key2)`
- **Callers:** EquipDetail_Refresh, GuideWindow_ShowPage, sub_1400F7378, sub_1400F74F4, sub_14011C940, sub_140125F38 and about fifteen more game-data readers
- **Callees:** NxdRegistry_Find, sub_1403D3A10, NxdTable_GetEntryByKeys2, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The row of (key1, key2) of a double-keyed table (for a triple-keyed table: the first leaf of child (key1, key2)), looked up by table id; its data pointer, or null.

## Behavior

- V: same registry, type (2 or 3) and state checks as UITable_GetRowCount. The entry is NxdTable_GetEntryByKeys2(table, key1, key2) (a binary search of the bound entries by the key pair); null returns null; first qword negative returns unk_1406F5ED0; else NxdEntry_GetRow(entry).
- V: unlike UITable_GetRowByIndex there is no count check: key2 is a key, not a position.
- V: GuideWindow_ShowPage reads GuidePage-en (table 188) with (guide, page) through it.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [GuideWindow_ShowPage](GuideWindow_ShowPage.md), [sub_1400F7378](sub_1400F7378.md)

## Notes

X6 (2026-10-30) decoded the callee and named it (IDB: sub_1403DBCE4).

## Open questions

None recorded.
