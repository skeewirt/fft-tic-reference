# NxdSingleKeyRows

- **Kind:** file format
- **Extension:** `.nxd`
- **Area:** [Data access](../areas/data.md)
- **Read by:** [NxdTable_BindRows](../functions/NxdTable_BindRows.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [NxdTable_BinarySearchRow](../functions/NxdTable_BinarySearchRow.md), [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The row area of a single-key nxd file (header byte 8 = 1, byte 9 = 1 or 2): the entry table, the rows and the string pool, and how a row refers to its strings and arrays. Completes NxdSingleKeyHeader.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="entries"></a>+48 | entries | `{uint32 key; int32 rel}[count]` | V | One per row, ascending keys; the row starts at the entry's own address + rel (NxdEntry_GetRow, kind 1). |
| <a id="rows"></a>+48 + 8 * count | rows | `bytes` | V | Each row: its fixed part (the columns in layout order, each aligned to min(size, 4), rounded up to 4), then that row's arrays. |
| <a id="string pool"></a>after the rows | string pool | `char[]` | V | NUL-terminated UTF-8 strings; an empty string stands for a null cell (27,103 such cells checked). |
| <a id="integer / float column"></a>row + column | integer / float column | `int8..uint32, float` | V | Little endian, in place. |
| <a id="string column"></a>row + column | string column | `int32` | V | Target minus a base: the row start, or for the relative columns the column's own position plus the layout's adjustment (Item: every name column relative to row +4). |
| <a id="array column"></a>row + column | array column | `{int32 offset; uint32 count}` | V | Elements at row start + offset; an empty array keeps an offset and count 0. |
| <a id="union column"></a>row + column | union column | `{int32 type; int32 id}` | V | A _uniontypes id and a row id. |
| <a id="string array column"></a>row + column | string array column | `{int32 offset; uint32 count}` | V | int32 elements at row start + offset, each a string offset relative to the ARRAY start (8 layout columns, every row checked). |
| <a id="struct array column"></a>row + column | struct array column | `{int32 offset; uint32 count}` | V | Elements of the struct's size (members placed like columns, size rounded up to 4) at row start + offset; a string member is relative to its ELEMENT start (4 layout columns, every row checked). |

## Behavior

- V: every reference inside the row area is relative (to the entry, the row or the column), so the whole area can move as one block.
- V: 186 of the 188 single-key retail files decode with this column order and alignment, checked against every stock row (all 32,752 rows, every column).
- V: the same row encoding holds in the double / triple keyed files (NxdMultiKeyIndex); only the index differs.
- V: RefinedBgTexture rows hold two pairs of (name list, count list) at +8/+16 and +24/+32; the counts are signed 32-bit frame counts read at the name's index, and the count list's own element count is never read (MapTextures_NameOfFrame). All 1,338 stock rows have as many counts as names.
- V: a layout can be longer than the rows: OverrideEntryData's layout ends at +0x9D (row size 160) but its rows are 156 bytes apart, so its last column is the next row's first byte (OverrideEntry_FillUnitEntry reads up to +0x99). A byte check against the stock rows cannot see this.

## Referenced by

- Read by: [NxdTable_BindRows](../functions/NxdTable_BindRows.md)

## Notes

The byte check against every stock row is what makes the column order and types V for these files. A cell typed as text can still hold numbers: the check passes when the bytes read as an offset to some text, as the last array of a RefinedBgTexture row did (it holds 32-bit frame counts, read by MapTextures_NameOfFrame; the counts 01 00 00 00 read as offsets to empty text inside the array itself). A byte-exact round trip does not prove a column's type; the reader's code does.

## Open questions

None recorded.
