# NxdDataUIDialogRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 60 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_dialog table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="ui_text"></a>`0x4` | ui_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 3983, 73 distinct values. |
| <a id="option_1_text"></a>`0x8` | option_1_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 3911, 23 distinct values. |
| <a id="option_2_text"></a>`0xC` | option_2_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 3893, 22 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 70, 2 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 17, 2 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 104, 5 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 261, 13 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 15, 3 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 15, 2 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 21008, 4 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 104, 3 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 256 to 1.68433e+07, 12 distinct values. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 1.6843e+07, 6 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIDialog](../tables/NxdDataUIDialog.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 12 of 15 columns not decoded.
