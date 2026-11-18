# NxdTable_BindRows

- **Address:** `0x1403D3F3C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int NxdTable_BindRows(NxdTable *table, NxdFile *file)`
- **Callers:** through a function pointer set by sub_1403D3E64
- **Callees:** sub_14041FB00, sub_140011750, sub_140011804

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds a loaded nxd file to its table object: reads the header's layout, row count and the contiguous-keys flag, and builds the 16-byte entry array (kind, row pointer).

## Behavior

- V: header byte 9 = 1 or 2 (single key): mode (+56) = header byte 8, row count (+40) = header dword +36; a non-zero header byte 10 sets +65 (rows by position) and +68 = header dword +12 (the first key).
- V: byte 9 = 3 or 4: count from dword +48; 5 or 6: count from dword +44; other values return error 0x96130006.
- V: mode 1: entry i = (1, rows + 8 * i) with rows at header dword +32; +72 = the last row's key; without the flag the caches at +24 and +32 are freed.
- V: mode 2: entry i = (2, header + dword +44 + 12 * i); other modes: (mode, header + dword +40 + 20 * i).
- V: grows the entry array when the new count is larger.
- V: can run again on a bound table: it reads the header of the handle's buffer (+56), sets the row count (+40) and kind (+56); only when the new count is larger than the old one it frees the entry array (+16, `sub_14041FB00(p, 16)`) and allocates another (`Mem_Alloc(16 * n, table heap +0, 8)`), else it rewrites the entries in place (kind, pointer into the new buffer); for a table without the contiguous-keys flag (header +10 = 0) it frees the lookup arrays +24 / +32 (built again on use).
- V (seen live 2026-11-14): an item name table bound again on the game thread at the title screen (same keys, a changed file) showed the new name in the Outfitter Buy list and the Inventory list on the next screen, with no crash, also after four rebinds in one session; the weapon power in the Outfitter's detail panel is read from the weapon record when drawn and followed a changed record on the next visit.

## State touched

- Reads: [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md), [NexResourceHandle.data](../structs/NexResourceHandle.md#data), [NxdSingleKeyHeader](../formats/NxdSingleKeyHeader.md)
- Writes: [NxdTable.entries](../structs/NxdTable.md#entries), [NxdTable.count](../structs/NxdTable.md#count), [NxdTable.by_position](../structs/NxdTable.md#by_position), [NxdTable.first_key](../structs/NxdTable.md#first_key), [NxdTable.last_key](../structs/NxdTable.md#last_key)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md), [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [NxdHandle_OnLoaded](NxdHandle_OnLoaded.md)
- Observed behaviours: [NxdTableRebinding](../behaviors/NxdTableRebinding.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md), [NxdSingleKeyHeader](../formats/NxdSingleKeyHeader.md), [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md)

## Notes

Retail files set byte 10 only when the keys are contiguous from the first key (all 188 single-key files checked). A table with a gap must clear it.

## Open questions

None recorded.
