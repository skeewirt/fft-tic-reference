# NxdDataBookRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.book table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 818 to 832, 5 distinct values. |
| <a id="icon_id"></a>`0x10` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 217 to 231, 5 distinct values. |
| <a id="title"></a>`0x14` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 5 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 5 distinct values, 0 empty. |
| <a id="description_format"></a>`0x1C` | description_format | `string (int32 offset)` | I | Description format text. Observed in the stock rows: 5 distinct values, 1 empty. |
| <a id="novel_sound_id"></a>`0x20` | novel_sound_id | `int16` | I | Novel sound id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 225 to 233, 5 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 538 to 552, 5 distinct values. |

## Referenced by

- Described by tables: [NxdDataBook](../tables/NxdDataBook.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

4 of 11 columns not decoded.
