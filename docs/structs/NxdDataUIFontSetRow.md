# NxdDataUIFontSetRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 100 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_font_set table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="font_type_id1"></a>`0x4` | font_type_id1 | `int32` | I | Font type id1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 11, 8 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.465 to 0.7, 16 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 13 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 10, 12 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 5 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1.7, 12 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 2.4, 10 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.102, 6 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.2, 8 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `float32` | ? | Not decoded. Observed in the stock rows: 0.1 in every row. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `float32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_30"></a>`0x30` | unk_30 | `float32` | ? | Not decoded. Observed in the stock rows: 1 to 1.2, 3 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `float32` | ? | Not decoded. Observed in the stock rows: 0.2 to 0.5, 4 distinct values. |
| <a id="font_type_id2"></a>`0x38` | font_type_id2 | `int32` | I | Font type id2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 11, 4 distinct values. |
| <a id="font_type_id3"></a>`0x3C` | font_type_id3 | `int32` | I | Font type id3 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="font_type_id4"></a>`0x40` | font_type_id4 | `int32` | I | Font type id4 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="font_type_id5"></a>`0x44` | font_type_id5 | `int32` | I | Font type id5 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="font_type_id6"></a>`0x48` | font_type_id6 | `int32` | I | Font type id6 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 13, 7 distinct values. |
| <a id="font_type_id7"></a>`0x4C` | font_type_id7 | `int32` | I | Font type id7 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 15, 7 distinct values. |
| <a id="font_type_id8"></a>`0x50` | font_type_id8 | `int32` | I | Font type id8 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 17, 7 distinct values. |
| <a id="unk_54"></a>`0x54` | unk_54 | `uint32` | ? | Not decoded. Observed in the stock rows: 4.2828e+09 to 4.29497e+09, 8 distinct values. |
| <a id="unk_58"></a>`0x58` | unk_58 | `uint32` | ? | Not decoded. Observed in the stock rows: 0 to 4.29497e+09, 15 distinct values. |
| <a id="unk_5c"></a>`0x5C` | unk_5c | `uint32` | ? | Not decoded. Observed in the stock rows: 2.14748e+09 to 4.29497e+09, 22 distinct values. |
| <a id="unk_60"></a>`0x60` | unk_60 | `uint32` | ? | Not decoded. Observed in the stock rows: 0 to 4.29135e+09, 21 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIFontSet](../tables/NxdDataUIFontSet.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

16 of 25 columns not decoded.
