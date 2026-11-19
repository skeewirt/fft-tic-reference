# NxdDataConfigItemResolutionRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.config_item_resolution table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="resolution"></a>`0x4` | resolution | `int32` | M | Measured over every stock row: Every value is a key of nxd.Resolution. Observed in the stock rows: 1 to 9, 9 distinct values. |

## Referenced by

- Described by tables: [NxdDataConfigItemResolution](../tables/NxdDataConfigItemResolution.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 2 columns not decoded.
