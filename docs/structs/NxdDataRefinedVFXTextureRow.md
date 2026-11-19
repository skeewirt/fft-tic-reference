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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.5 to 1, 2 distinct values. |
| <a id="depth_bias"></a>`0xC` | depth_bias | `int32` | M | Measured over every stock row: Every value is a key of nxd.DepthBias. Observed in the stock rows: 2 to 11, 5 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `float32` | ? | Not decoded. Observed in the stock rows: -1 to 2, 2 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown19"></a>`0x19` | unknown19 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1a"></a>`0x1A` | unknown1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1b"></a>`0x1B` | unknown1b | `uint8` | ? | Not decoded. Observed in the stock rows: 127 to 255, 2 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 10 of 11 columns not decoded.
