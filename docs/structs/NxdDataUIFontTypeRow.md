# NxdDataUIFontTypeRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_font_type table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="font_path"></a>`0x4` | font_path | `string (int32 offset)` | I | File path string. Observed in the stock rows: 15 distinct values, 5 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 56, 5 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `float32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `float32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `float32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUIFontType](../tables/NxdDataUIFontType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

4 of 6 columns not decoded.
