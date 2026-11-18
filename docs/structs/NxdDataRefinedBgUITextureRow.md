# NxdDataRefinedBgUITextureRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_bg_ui_texture table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="refined_bg_ui_texture_frames_ids"></a>`0x4` | refined_bg_ui_texture_frames_ids | `int32[] {int32 offset; uint32 count}` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 19 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int16` | ? | Not decoded. Observed in the stock rows: 1 to 3, 2 distinct values. |
| <a id="unk_0e"></a>`0xE` | unk_0e | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 29, 2 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 6, 2 distinct values. |
| <a id="unk_11"></a>`0x11` | unk_11 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 5, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataRefinedBgUITexture](../tables/NxdDataRefinedBgUITexture.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

4 of 6 columns not decoded.
