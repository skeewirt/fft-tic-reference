# NxdDataRefinedBgMeshNodeInvisTypeRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_bg_mesh_node_invis_type table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_0a"></a>`0xA` | unk_0a | `int16` | ? | Not decoded. Observed in the stock rows: 2048 in every row. |

## Referenced by

- Described by tables: [NxdDataRefinedBgMeshNodeInvisType](../tables/NxdDataRefinedBgMeshNodeInvisType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 4 columns not decoded.
