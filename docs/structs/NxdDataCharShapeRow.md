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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="charshapeshadowsize_id1"></a>`0x8` | charshapeshadowsize_id1 | `uint32` | I | Row id of CharShapeShadowSize (a reference by column name). Observed in the stock rows: 1 to 5, 5 distinct values. |
| <a id="charclut_id"></a>`0xC` | charclut_id | `uint32` | I | Row id of CharCLUT (a reference by column name). Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="charshapelutparam_id1"></a>`0x10` | charshapelutparam_id1 | `uint32` | I | Row id of CharShapeLUTParam (a reference by column name). Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="charshapeshadowsize_id2"></a>`0x14` | charshapeshadowsize_id2 | `uint32` | I | Row id of CharShapeShadowSize (a reference by column name). Observed in the stock rows: 1 to 11, 6 distinct values. |
| <a id="charshapelutparam_id2"></a>`0x18` | charshapelutparam_id2 | `uint32` | I | Row id of CharShapeLUTParam (a reference by column name). Observed in the stock rows: 1 to 14, 7 distinct values. |
| <a id="charshapelutparam_id3"></a>`0x1C` | charshapelutparam_id3 | `uint32` | I | Row id of CharShapeLUTParam (a reference by column name). Observed in the stock rows: 2 to 23, 9 distinct values. |
| <a id="charshapelutparam_id4"></a>`0x20` | charshapelutparam_id4 | `uint32` | I | Row id of CharShapeLUTParam (a reference by column name). Observed in the stock rows: 2 to 32, 9 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `uint32` | ? | Not decoded. Observed in the stock rows: 2 in every row. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int8` | ? | Not decoded. Observed in the stock rows: 1 to 36, 35 distinct values. |
| <a id="unk_29"></a>`0x29` | unk_29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2a"></a>`0x2A` | unk_2a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2b"></a>`0x2B` | unk_2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="height"></a>`0x2C` | height | `uint8` | I | Height (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 108, 7 distinct values. |
| <a id="unk_2d"></a>`0x2D` | unk_2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2e"></a>`0x2E` | unk_2e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_2f"></a>`0x2F` | unk_2f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 36, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharShape](../tables/NxdDataCharShape.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

8 of 18 columns not decoded.
