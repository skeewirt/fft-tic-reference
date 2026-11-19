# NxdDataCharShapeRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.char_shape table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="char_shape_shadow_size"></a>`0x8` | char_shape_shadow_size | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeShadowSize. Observed in the stock rows: 1 to 5, 5 distinct values. |
| <a id="char_clut"></a>`0xC` | char_clut | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharCLUT. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="char_shape_lut_param"></a>`0x10` | char_shape_lut_param | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="char_shape_shadow_size_2"></a>`0x14` | char_shape_shadow_size_2 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeShadowSize. Observed in the stock rows: 1 to 11, 6 distinct values. |
| <a id="char_shape_lut_param_2"></a>`0x18` | char_shape_lut_param_2 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="char_shape_lut_param_3"></a>`0x1C` | char_shape_lut_param_3 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 2 to 23, 9 distinct values. |
| <a id="char_shape_lut_param_4"></a>`0x20` | char_shape_lut_param_4 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 2 to 32, 9 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `uint32` | ? | Not decoded. Observed in the stock rows: 2 in every row. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int8` | ? | Not decoded. Observed in the stock rows: 1 to 36, 35 distinct values. |
| <a id="unknown29"></a>`0x29` | unknown29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2a"></a>`0x2A` | unknown2a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2b"></a>`0x2B` | unknown2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 108, 7 distinct values. |
| <a id="unknown2d"></a>`0x2D` | unknown2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2e"></a>`0x2E` | unknown2e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown2f"></a>`0x2F` | unknown2f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 36, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharShape](../tables/NxdDataCharShape.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 11 of 18 columns not decoded.
