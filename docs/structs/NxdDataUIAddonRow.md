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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: -100 to 260, 40 distinct values. |
| <a id="path"></a>`0x8` | path | `string (int32 offset)` | M | Measured over every stock row: File paths. Observed in the stock rows: 124 distinct values, 140 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown0d"></a>`0xD` | unknown0d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown0e"></a>`0xE` | unknown0e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown0f"></a>`0xF` | unknown0f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown11"></a>`0x11` | unknown11 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown12"></a>`0x12` | unknown12 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown13"></a>`0x13` | unknown13 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown15"></a>`0x15` | unknown15 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown16"></a>`0x16` | unknown16 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown17"></a>`0x17` | unknown17 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown18"></a>`0x18` | unknown18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown19"></a>`0x19` | unknown19 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1a"></a>`0x1A` | unknown1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1b"></a>`0x1B` | unknown1b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1d"></a>`0x1D` | unknown1d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1e"></a>`0x1E` | unknown1e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1f"></a>`0x1F` | unknown1f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIAddon](../tables/NxdDataUIAddon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 23 of 24 columns not decoded.
