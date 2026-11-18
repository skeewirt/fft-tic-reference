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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="names_a"></a>`0x8` | names_a | `string (int32 offset)[] {int32 offset; uint32 count}` | V | Texture names of this slot and type, one per map variation (the first pair). A name that ends in 0 starts a frame series. The file is the texture folder of the map, the name, and a .tga extension. Read by MapTextures_NameOfFrame. |
| <a id="frame_counts_a"></a>`0x10` | frame_counts_a | `int32[] {int32 offset; uint32 count}` | V | Frame count of the name at the same index in names_a: a frame is requested only while its index is below the count (1 = a single texture). The element at the name index is read; the array count is not. Stock values 1, 2, 3, 4, 5, 6, 8, 9, 10, 15, 16, 30, 32, 59; always as many counts as names except one row. |
| <a id="names_b"></a>`0x18` | names_b | `string (int32 offset)[] {int32 offset; uint32 count}` | V | Texture names of this slot and type, one per kind code (the second pair, used when the map selects by kind code instead of variation). Same naming as names_a. |
| <a id="frame_counts_b"></a>`0x20` | frame_counts_b | `int32[] {int32 offset; uint32 count}` | V | Frame count of the name at the same index in names_b (the same role as frame_counts_a). Stock values 1, 5, 8, 10, 30; as many counts as names in all 1,338 rows. Stored as integers, not as text offsets. |

## Referenced by

- Described by tables: [NxdDataRefinedBgTexture](../tables/NxdDataRefinedBgTexture.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names. The two (names, frame counts) pairs are read by MapTextures_NameOfFrame; a name with no count at its index is never requested.

## Open questions

? 2 of 6 columns not decoded (dlc_flags and comment are inferred, 0 / empty in every row).
