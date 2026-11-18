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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="text_ui_id"></a>`0x4` | text_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 3983, 73 distinct values. |
| <a id="option1_text_ui_id"></a>`0x8` | option1_text_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 3911, 23 distinct values. |
| <a id="option2_text_ui_id"></a>`0xC` | option2_text_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 3893, 22 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 70, 2 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 17, 2 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 104, 5 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 261, 13 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 15, 3 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 15, 2 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 21008, 4 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 104, 3 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Not decoded. Observed in the stock rows: 256 to 1.68433e+07, 12 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 1.6843e+07, 6 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIDialog](../tables/NxdDataUIDialog.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

11 of 15 columns not decoded.
