# UITable_GetRowCount

- **Address:** `0x1403DBC20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UITable_GetRowCount(int tableId, unsigned int key)`
- **Callers:** sub_1403DBB00 (table 125), sub_1402EE84C, sub_1402A5E38, sub_1402A62E4, sub_1402A876C and about ten more game-data readers
- **Callees:** NxdRegistry_Find, sub_1403D3A10, sub_1403D3A34

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Number of sub-rows of a key in a multi-row UI table (the count field of the key's entry), or 0 when the table or key does not exist.

## Behavior

- V: needs g_NxdRegistry != 0; NxdRegistry_Find(registry, tableId) must return a table whose type dword at +12 is 2 or 3; sub_1403D3A10 must return 0 (it is 'not in a locked / loading state': the status dword at (table+48)+80 is not 2 or 3); then the result is sub_1403D3A34(table, key).
- V: any failed step returns 0.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md)

## Referenced by

- Called by: [GuideWindow_ShowPage](GuideWindow_ShowPage.md)

## Notes

The name is ours (IDB: sub_1403DBC20). Paired with UITable_GetRowByIndex (row by key and position) and UITable_GetRowByKeys (row by two keys). Table 125 is the language / path override table used by the slot registry. Type 2 / 3 are the double / triple keyed files (format NxdMultiKeyIndex, V against all 58 retail files); the count is the set's record count (double: the rows of key; triple: its children).

## Open questions

None recorded.
