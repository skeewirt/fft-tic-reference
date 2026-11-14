# NxdMultiKeyIndex

- **Kind:** file format
- **Extension:** `.nxd`
- **Area:** [Data access](../areas/data.md)
- **Read by:** [NxdTable_BindRows](../functions/NxdTable_BindRows.md), [NxdSets_Find2](../functions/NxdSets_Find2.md), [NxdSets_Find3](../functions/NxdSets_Find3.md), [NxdSet3_FindChild](../functions/NxdSet3_FindChild.md), [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md), [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md), [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](../functions/NxdTable_GetEntryByKeysIndex3.md), [NxdTable_GetSetEntries](../functions/NxdTable_GetSetEntries.md), [NxdTable_GetEntryCount](../functions/NxdTable_GetEntryCount.md), [NxdTable_GetEntryByIndex](../functions/NxdTable_GetEntryByIndex.md), [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The index of a double or triple keyed nxd file (header byte 8 = 2 or 3): sets by key1, per set an array (double) or children by key2 with their leaves (triple), and one flat entry table of every row sorted by the key tuple. The rows, strings and arrays are encoded as in a single-key file.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="kind"></a>+8 | kind | `uint8` | V | 2 double keyed (layout byte +9 = 3 or 4), 3 triple keyed (+9 = 5 or 6); 52 and 6 retail files. |
| <a id="sets_contiguous"></a>+10 | sets_contiguous | `uint8` | V | Double keyed: set only when the set keys are first_key, first_key + 1, ... (17 of the 52 files); the game does not read it for these kinds (BindRows reads +10 only for layouts 1 and 2). |
| <a id="first_key"></a>+12 | first_key | `int32` | V | The first set key when +10 is set, else 0. |
| <a id="sets"></a>+32 | sets | `{int32 offset; int32 count}` | V | The set table, offset relative to +32 (60 double, 56 triple in every retail file); the walkers take the address file + 32. |
| <a id="entries3"></a>+40 (triple) | entries3 | `{int32 offset; int32 count}` | V | Triple: the flat entry table at this ABSOLUTE offset and its count (BindRows binds one entry per record). |
| <a id="entries2"></a>+44 (double) | entries2 | `{int32 offset; int32 count}` | V | Double: the flat entry table at this ABSOLUTE offset, count at +48. |
| <a id="set2"></a>set record (double) | set2 | `{uint32 key1; int32 array; int32 count}` | V | 12 bytes, sorted by key1 (binary search NxdSets_Find2); array offset relative to the record; empty sets exist (usersituation: 10). |
| <a id="entry2"></a>array record and flat entry (double) | entry2 | `{uint32 key1; uint32 key2; int32 row}` | V | 12 bytes, row offset relative to the record; an array is sorted by key2; NxdEntry_GetRow (kind 2) adds +8. |
| <a id="set3"></a>set record (triple) | set3 | `{uint32 key1; int32 children; int32 count; int32 leaves; int32 zero}` | V | 20 bytes, sorted by key1 (NxdSets_Find3); children offset relative to the record; the set-level leaf count is 0 in every retail file (its offset is not read with count 0). |
| <a id="child3"></a>child record (triple) | child3 | `{uint32 key2; int32 offset; int32 zero; int32 leaves; int32 count}` | V | 20 bytes, sorted by key2 (NxdSet3_FindChild); leaves at +12 relative to the child, count +16; +4 equals +12 and +8 is 0 in every retail file (a walker descends while +8 is positive). |
| <a id="entry3"></a>leaf and flat entry (triple) | entry3 | `{uint32 key1; uint32 key2; uint32 key3; int32 zero; int32 row}` | V | 20 bytes, row offset relative to the record at +16; leaves sorted by key3; +12 is 0 everywhere; NxdEntry_GetRow (kind 3) adds +16. |

## Behavior

- V: in every retail file the arrays (double) or leaves (triple), concatenated in set order, are exactly the flat entry table (keys and row offsets), sorted by the key tuple; the game relies on it: NxdTable_GetSetEntries returns the entry of a set's first record and a count that its callers step through as consecutive bound entries.
- V: a lookup by keys searches the flat entries (NxdEntries_Search2 / 3); a lookup by key1 and position goes through the set, takes that record's keys and then searches the flat entries (NxdTable_GetEntryByKeyIndex): the array record's own row offset is not used by these paths.
- V: retail layout order: header, set table, per set its array (or children and leaves) followed by that set's rows, the flat entry table, the string pool. Only the offsets matter to the game.
- V: all 58 files decode with these invariants checked (every set, array and leaf is walked and compared with the flat table); 49 double and 5 triple keyed tables decode row for row against every stock row (15,372 and 6,451 rows).

## Referenced by

- Read by: [NxdSet3_FindChild](../functions/NxdSet3_FindChild.md), [NxdSets_Find2](../functions/NxdSets_Find2.md), [NxdSets_Find3](../functions/NxdSets_Find3.md), [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](../functions/NxdTable_GetEntryByKeysIndex3.md), [NxdTable_GetLeafCount3](../functions/NxdTable_GetLeafCount3.md), [NxdTable_GetSetEntries](../functions/NxdTable_GetSetEntries.md)

## Notes

Field names here are ours.

## Open questions

? layouts 4 and 6 versus 3 and 5 (the English text tables use 4; BindRows treats 3/4 and 5/6 alike; no file with layout 6).
