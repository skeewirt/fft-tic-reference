# NxdDataRefinedVFXTextureRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_vfx_texture table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.5 to 1, 2 distinct values. |
| <a id="depth_bias_id"></a>`0xC` | depth_bias_id | `int32` | I | Row id of DepthBias (a reference by column name). Observed in the stock rows: 2 to 11, 5 distinct values. |
| <a id="refined_vfx_camera_control_id"></a>`0x10` | refined_vfx_camera_control_id | `int32` | I | Row id of RefinedVFXCameraControl (a reference by column name). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `float32` | ? | Not decoded. Observed in the stock rows: -1 to 2, 2 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_19"></a>`0x19` | unk_19 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1a"></a>`0x1A` | unk_1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1b"></a>`0x1B` | unk_1b | `uint8` | ? | Not decoded. Observed in the stock rows: 127 to 255, 2 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 11 columns not decoded.
