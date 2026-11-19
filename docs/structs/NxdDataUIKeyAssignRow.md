# NxdDataUIKeyAssignRow

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_key_assign table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 24, 25 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 60, 28 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 24, 20 distinct values. |
| <a id="key"></a>`0x10` | key | `int32` | M | Measured over every stock row: The keyboard key of the action (Windows key number). Observed in the stock rows: 0 to 161, 35 distinct values. |
| <a id="key_2"></a>`0x14` | key_2 | `int32` | V | Read in the code: The second keyboard key of the action. Observed in the stock rows: 0 to 164, 10 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 86 distinct values, 168 empty. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown20"></a>`0x20` | unknown20 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown21"></a>`0x21` | unknown21 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown22"></a>`0x22` | unknown22 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown23"></a>`0x23` | unknown23 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown24"></a>`0x24` | unknown24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown25"></a>`0x25` | unknown25 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown26"></a>`0x26` | unknown26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown27"></a>`0x27` | unknown27 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown28"></a>`0x28` | unknown28 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown29"></a>`0x29` | unknown29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2a"></a>`0x2A` | unknown2a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2b"></a>`0x2B` | unknown2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2d"></a>`0x2D` | unknown2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIKeyAssign](../tables/NxdDataUIKeyAssign.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 20 of 22 columns not decoded.
