# NxdSingleKeyHeader

- **Kind:** file format
- **Extension:** `.nxd`
- **Area:** [Data access](../areas/data.md)
- **Read by:** [NxdTable_BindRows](../functions/NxdTable_BindRows.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The header bytes of an nxd file that the game's loader (NxdTable_BindRows) reads for a single-key table, and the contiguous-keys flag that decides whether a key is read by position or searched.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="magic"></a>+0 | magic | `char[4]` | V | 'NXDF'. |
| <a id="mode"></a>+8 | mode | `uint8` | V | 1 for single-key tables (entry kind 1: the row is the entry pointer plus the dword at +4). |
| <a id="layout"></a>+9 | layout | `uint8` | V | 1 or 2: single key, row count at +36; 3 or 4: count at +48; 5 or 6: count at +44. |
| <a id="contiguous_keys"></a>+10 | contiguous_keys | `uint8` | V | Not 0: row i holds key first_key + i, and the game reads row (key - first_key) instead of searching. Retail files set it only when that is true. |
| <a id="first_key"></a>+12 | first_key | `int32` | V | The key of row 0 when +10 is set; 0 in every retail file without the flag. |
| <a id="rows_offset"></a>+32 | rows_offset | `int32` | V | Offset of the row table: 8 bytes per row, the key (uint32) first, sorted by key. |
| <a id="row_count"></a>+36 | row_count | `int32` | V | Number of rows (layouts 1 and 2). |

## Referenced by

- Read by: [NxdTable_BindRows](../functions/NxdTable_BindRows.md)

## Open questions

? the other header fields (+4 version 1, +16..+31, +40..).
