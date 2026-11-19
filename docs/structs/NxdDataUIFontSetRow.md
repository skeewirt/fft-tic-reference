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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="ui_font_type"></a>`0x4` | ui_font_type | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIFontType. Observed in the stock rows: 0 to 11, 8 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.465 to 0.7, 16 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 13 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 10, 12 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 5 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1.7, 12 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 2.4, 10 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.102, 6 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.2, 8 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `float32` | ? | Not decoded. Observed in the stock rows: 0.1 in every row. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `float32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown30"></a>`0x30` | unknown30 | `float32` | ? | Not decoded. Observed in the stock rows: 1 to 1.2, 3 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `float32` | ? | Not decoded. Observed in the stock rows: 0.2 to 0.5, 4 distinct values. |
| <a id="ui_font_type_2"></a>`0x38` | ui_font_type_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIFontType. Observed in the stock rows: 0 to 11, 4 distinct values. |
| <a id="unknown3c"></a>`0x3C` | unknown3c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown40"></a>`0x40` | unknown40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="ui_font_type_3"></a>`0x48` | ui_font_type_3 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIFontType. Observed in the stock rows: 0 to 13, 7 distinct values. |
| <a id="ui_font_type_4"></a>`0x4C` | ui_font_type_4 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIFontType. Observed in the stock rows: 0 to 15, 7 distinct values. |
| <a id="ui_font_type_5"></a>`0x50` | ui_font_type_5 | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIFontType. Observed in the stock rows: 0 to 17, 7 distinct values. |
| <a id="unknown54"></a>`0x54` | unknown54 | `uint32` | ? | Not decoded. Observed in the stock rows: 4.2828e+09 to 4.29497e+09, 8 distinct values. |
| <a id="unknown58"></a>`0x58` | unknown58 | `uint32` | ? | Not decoded. Observed in the stock rows: 0 to 4.29497e+09, 15 distinct values. |
| <a id="unknown5c"></a>`0x5C` | unknown5c | `uint32` | ? | Not decoded. Observed in the stock rows: 2.14748e+09 to 4.29497e+09, 22 distinct values. |
| <a id="unknown60"></a>`0x60` | unknown60 | `uint32` | ? | Not decoded. Observed in the stock rows: 0 to 4.29135e+09, 21 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIFontSet](../tables/NxdDataUIFontSet.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 20 of 25 columns not decoded.
