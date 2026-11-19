# NxdDataRefinedBgMeshPolygonRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_bg_mesh_polygon table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 60, 3 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 716, 489 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="refined_bg_mesh_polygon_cond"></a>`0x10` | refined_bg_mesh_polygon_cond | `int32` | M | Measured over every stock row: Every value is a key of nxd.RefinedBgMeshPolygonCond. Observed in the stock rows: 0 to 78, 79 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 65535, 15 distinct values. |

## Referenced by

- Described by tables: [NxdDataRefinedBgMeshPolygon](../tables/NxdDataRefinedBgMeshPolygon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 5 of 6 columns not decoded.
