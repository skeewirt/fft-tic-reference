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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="char_shape_shadow_size"></a>`0x8` | char_shape_shadow_size | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeShadowSize. Observed in the stock rows: 1 to 5, 5 distinct values. |
| <a id="char_clut"></a>`0xC` | char_clut | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharCLUT. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="char_shape_lut_param"></a>`0x10` | char_shape_lut_param | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="char_shape_shadow_size_2"></a>`0x14` | char_shape_shadow_size_2 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeShadowSize. Observed in the stock rows: 1 to 11, 6 distinct values. |
| <a id="char_shape_lut_param_2"></a>`0x18` | char_shape_lut_param_2 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="char_shape_lut_param_3"></a>`0x1C` | char_shape_lut_param_3 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 2 to 23, 9 distinct values. |
| <a id="char_shape_lut_param_4"></a>`0x20` | char_shape_lut_param_4 | `uint32` | M | Measured over every stock row: Every value is a key of nxd.CharShapeLUTParam. Observed in the stock rows: 2 to 32, 9 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `uint32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 2 in every row. |
| <a id="char_mouse_collision"></a>`0x28` | char_mouse_collision | `int32` | V | Read in the code: A key of CharMouseCollision (table 334): the shape's mouse hit area. Observed in the stock rows: 1 to 36, 35 distinct values. |
| <a id="height"></a>`0x2C` | height | `int8` | V | Read in the code: The unit's height above its tile (signed byte): the battle code adds it to the unit's base point to place things drawn over the unit (the tile cursor marker, the screen point above the unit, the formation-screen label). Observed in the stock rows: 0 to 108, 7 distinct values. |
| <a id="unknown2d"></a>`0x2D` | unknown2d | `int8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2e"></a>`0x2E` | unknown2e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="height_2"></a>`0x2F` | height_2 | `int8` | V | Read in the code: A second height used instead of height (+0x2C) by the formation screen when the unit's flag byte +0x15C & 4 is set and this value is non-zero. Observed in the stock rows: 0 to 36, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharShape](../tables/NxdDataCharShape.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 15 columns not decoded.
