# NxdDataUIAddonRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 36 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_addon table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: -100 to 260, 40 distinct values. |
| <a id="ui_file_path"></a>`0x8` | ui_file_path | `string (int32 offset)` | I | File path string. Observed in the stock rows: 124 distinct values, 140 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_0d"></a>`0xD` | unk_0d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_0e"></a>`0xE` | unk_0e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_0f"></a>`0xF` | unk_0f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_11"></a>`0x11` | unk_11 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_12"></a>`0x12` | unk_12 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_13"></a>`0x13` | unk_13 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_15"></a>`0x15` | unk_15 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_16"></a>`0x16` | unk_16 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_17"></a>`0x17` | unk_17 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_18"></a>`0x18` | unk_18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_19"></a>`0x19` | unk_19 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1a"></a>`0x1A` | unk_1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1b"></a>`0x1B` | unk_1b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1d"></a>`0x1D` | unk_1d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1e"></a>`0x1E` | unk_1e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1f"></a>`0x1F` | unk_1f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIAddon](../tables/NxdDataUIAddon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

22 of 24 columns not decoded.
