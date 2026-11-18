# NxdDataConfigItemRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 76 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.config_item table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 5, 6 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 331, 9 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 17 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 3 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 5 distinct values. |
| <a id="config_pad_list_id"></a>`0x28` | config_pad_list_id | `int32` | I | Row id of ConfigPadList (a reference by column name). Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 11, 12 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 5, 2 distinct values. |
| <a id="item_name_text_ui_id"></a>`0x38` | item_name_text_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 4021, 45 distinct values. |
| <a id="description_text_ui_id"></a>`0x3C` | description_text_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 3643, 13 distinct values. |
| <a id="unk_40"></a>`0x40` | unk_40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4022, 35 distinct values. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4022, 40 distinct values. |
| <a id="unk_48"></a>`0x48` | unk_48 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

14 of 18 columns not decoded.
