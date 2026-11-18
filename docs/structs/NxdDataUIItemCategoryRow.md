# NxdDataUIItemCategoryRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_item_category table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 35 distinct values, 0 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 1.67772e+07 in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 33, 32 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="comment"></a>`0x1C` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataUIItemCategory](../tables/NxdDataUIItemCategory.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 8 columns not decoded.
