# NxdDataPostEffectDepthLUTRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.post_effect_depth_lut table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.498 to 1, 19 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.561, 20 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.834, 23 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `float32` | ? | Not decoded. Observed in the stock rows: 0.063 to 0.7, 23 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `float32` | ? | Not decoded. Observed in the stock rows: 0.26 to 0.762, 21 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.735, 24 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `float32` | ? | Not decoded. Observed in the stock rows: 0.136 to 0.619, 24 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 0.742, 21 distinct values. |

## Referenced by

- Described by tables: [NxdDataPostEffectDepthLUT](../tables/NxdDataPostEffectDepthLUT.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 10 of 10 columns not decoded.
