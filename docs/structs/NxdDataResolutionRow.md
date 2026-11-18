# NxdDataResolutionRow

- **Kind:** structure
- **Area:** [Display](../areas/display.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.resolution table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="width"></a>`0x4` | width | `int32` | I | Width (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 1280 to 7680, 9 distinct values. |
| <a id="height"></a>`0x8` | height | `int32` | I | Height (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 720 to 4320, 9 distinct values. |
| <a id="comment"></a>`0xC` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataResolution](../tables/NxdDataResolution.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
