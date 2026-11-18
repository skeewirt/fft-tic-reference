# NxdDataGuideRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.guide table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 4 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 12, 10 distinct values. |
| <a id="guide_page_id"></a>`0x10` | guide_page_id | `int32` | I | Row id of GuidePage-en (a reference by column name). Observed in the stock rows: 0 to 3277, 226 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 59, 19 distinct values. |
| <a id="user_situation_id"></a>`0x18` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 60016, 13 distinct values. |
| <a id="user_situation_id2"></a>`0x1C` | user_situation_id2 | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 12700, 8 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 2.8, 14 distinct values. |
| <a id="title"></a>`0x24` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 166 distinct values, 77 empty. |
| <a id="sort_order"></a>`0x28` | sort_order | `int16` | I | Sort order value. Observed in the stock rows: 0 to 3600, 115 distinct values. |
| <a id="unk_2a"></a>`0x2A` | unk_2a | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 165, 166 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGuide](../tables/NxdDataGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

6 of 13 columns not decoded.
