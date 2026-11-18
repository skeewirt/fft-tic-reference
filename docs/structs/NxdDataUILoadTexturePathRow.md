# NxdDataUILoadTexturePathRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_load_texture_path table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="path"></a>`0x4` | path | `string (int32 offset)` | I | File path string. Observed in the stock rows: 30 distinct values, 3 empty. |

## Referenced by

- Described by tables: [NxdDataUILoadTexturePath](../tables/NxdDataUILoadTexturePath.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
