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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="width"></a>`0x4` | width | `int32` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 1280 to 7680, 9 distinct values. |
| <a id="height"></a>`0x8` | height | `int32` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 720 to 4320, 9 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataResolution](../tables/NxdDataResolution.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 4 columns not decoded.
