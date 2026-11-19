# NxdDataScionLabelsRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.scion_labels table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="scion_files"></a>`0x4` | scion_files | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionFiles. Observed in the stock rows: 1129 to 2160, 152 distinct values. |
| <a id="scion_labels"></a>`0x8` | scion_labels | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 302152 to 357594, 3323 distinct values. |

## Referenced by

- Described by tables: [NxdDataScionLabels](../tables/NxdDataScionLabels.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 3 columns not decoded.
