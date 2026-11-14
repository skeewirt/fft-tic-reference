# NxdMultiKeyLookup

- **Kind:** flow
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a reader finds a row of a double or triple keyed table, and which parts of the file each path reads.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) | V | At load: one 16-byte entry per flat entry record (kind 2 or 3, pointer to the record); count = the flat table's count. |
| <a id="2"></a>2 | [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md) | V | By (key1, key2): binary search of the bound entries (NxdEntries_Search2); triple keyed: the first leaf of child (key1, key2). |
| <a id="3"></a>3 | [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md) | V | By (key1, key2, key3): binary search of the bound entries (NxdEntries_Search3). |
| <a id="4"></a>4 | [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md) | V | By key1 and position: NxdSets_Find2 / Find3 on the buffer's set table, the record at that position, then step 2 with its keys. |
| <a id="5"></a>5 | [NxdTable_GetSetEntries](../functions/NxdTable_GetSetEntries.md) | V | A whole set: the entry of its first record and the set's count; callers walk consecutive bound entries. |
| <a id="6"></a>6 | [NxdTable_GetEntryCount](../functions/NxdTable_GetEntryCount.md) | V | A set's record count (double: rows; triple: children); UITable_GetRowCount wraps it. |
| <a id="7"></a>7 | [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md) | V | The row: record + its row offset (+8 double, +16 triple). |

## Behavior

- V: NxdTable_GetRowById(table, id) of a double-keyed table returns the first row of set id; of a triple-keyed table the first leaf of child (id, 0).

## Open questions

None recorded.
