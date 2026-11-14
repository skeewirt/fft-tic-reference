# NxdTable

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 80 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One table object of the nxd registry (NxdRegistry_LoadRootNxl allocates one per root.nxl line); NxdTable_BindRows fills its entries from the loaded file and every row lookup reads it.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="heap"></a>`0x0` | heap | `Heap *` | V | The registry's heap (NxdTable_CreateHandle allocates the handle from it). |  |  |
| <a id="id"></a>`0x8` | id | `uint32` | V | The table id, column 2 of root.nxl (Item 45, Job 46, JobCommand 41, Ability 39, GeneralJob 189); localised tables use the id of their base name. | [NxdRegistry_LoadRootNxl](../functions/NxdRegistry_LoadRootNxl.md) |  |
| <a id="state"></a>`0xC` | state | `int32` | V | 1 = not loaded (LoadRootNxl); NxdTable_OnReady sets 2 or 3, which readers accept. | [NxdRegistry_LoadRootNxl](../functions/NxdRegistry_LoadRootNxl.md), [NxdTable_OnReady](../functions/NxdTable_OnReady.md) |  |
| <a id="entries"></a>`0x10` | entries | `NxdEntry *` | V | 16 bytes per row: kind (1, 2 or 3 keys) and a pointer to the row's record in the loaded file: the single-key entry, or the double / triple keyed flat entry (BindRows); NxdEntry_GetRow adds the record's row offset. | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) | [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md), [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md) |
| <a id="dense_cache"></a>`0x18` | dense_cache | `void **` | V | Freed by BindRows for a single-key table without the contiguous-keys flag; GetRowById searches when it is null. |  |  |
| <a id="count"></a>`0x28` | count | `uint64` | V | Row count from the file header. | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) | [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md), [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md) |
| <a id="handle"></a>`0x30` | handle | `NexResourceHandle *` | V | The file's resource handle (LoadRootNxl). | [NxdRegistry_LoadRootNxl](../functions/NxdRegistry_LoadRootNxl.md) | [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](../functions/NxdTable_GetEntryByKeysIndex3.md), [NxdTable_GetSetEntries](../functions/NxdTable_GetSetEntries.md) |
| <a id="mode"></a>`0x38` | mode | `int64` | V | File header byte 8: 1 single key, 2 double, 3 triple. |  | [NxdTable_GetEntryByKeys2](../functions/NxdTable_GetEntryByKeys2.md), [NxdTable_GetEntryByKeys3](../functions/NxdTable_GetEntryByKeys3.md) |
| <a id="by_position"></a>`0x41` | by_position | `uint8` | V | Header byte 10 of a single-key file: rows are read by position (key - first key). | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) |  |
| <a id="first_key"></a>`0x44` | first_key | `uint32` | V | Header dword +12 when by_position is set. | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) |  |
| <a id="last_key"></a>`0x48` | last_key | `uint32` | V | The last entry's key (BindRows). | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) |  |

## Notes

The entries point INTO the loaded file buffer (for a double / triple keyed file: one entry per record of its flat entry table); multi-key lookups (NxdTable_GetEntryByKeyIndex, NxdTable_GetEntryByKeysIndex3, NxdTable_GetSetEntries, NxdTable_GetEntryByIndex) read the set index through handle +56 again.

## Open questions

? +0x20 (freed with the dense cache), +0x40 (byte), +0x4C..+0x4F.
