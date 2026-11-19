# NxdDataRefinedBgTextureRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_bg_texture table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `string (int32 offset)[] {int32 offset; uint32 count}` | ? | Not decoded. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)[] {int32 offset; uint32 count}` | ? | Not decoded. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. |

## Referenced by

- Described by tables: [NxdDataRefinedBgTexture](../tables/NxdDataRefinedBgTexture.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names. The two (names, frame counts) pairs are read by MapTextures_NameOfFrame; a name with no count at its index is never requested.

## Open questions

? 6 of 6 columns not decoded.
