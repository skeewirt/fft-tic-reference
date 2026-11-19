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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 4 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 12, 10 distinct values. |
| <a id="guide_page"></a>`0x10` | guide_page | `int32` | M | Measured over every stock row: Every value is a key of nxd.GuidePage-en. Observed in the stock rows: 0 to 3277, 226 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 59, 19 distinct values. |
| <a id="user_situation"></a>`0x18` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 60016, 13 distinct values. |
| <a id="user_situation_2"></a>`0x1C` | user_situation_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 12700, 8 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 2.8, 14 distinct values. |
| <a id="title"></a>`0x24` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 166 distinct values, 77 empty. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 3600, 115 distinct values. |
| <a id="unknown2a"></a>`0x2A` | unknown2a | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 165, 166 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGuide](../tables/NxdDataGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 9 of 13 columns not decoded.
