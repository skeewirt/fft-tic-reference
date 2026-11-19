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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 5, 6 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 331, 9 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 17 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 3 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 5 distinct values. |
| <a id="config_pad_list"></a>`0x28` | config_pad_list | `int32` | M | Measured over every stock row: Every value is a key of nxd.ConfigPadList. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 11, 12 distinct values. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 5, 2 distinct values. |
| <a id="name_text"></a>`0x38` | name_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 4021, 45 distinct values. |
| <a id="description_text"></a>`0x3C` | description_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 3643, 13 distinct values. |
| <a id="unknown40"></a>`0x40` | unknown40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4022, 35 distinct values. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4022, 40 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 15 of 18 columns not decoded.
