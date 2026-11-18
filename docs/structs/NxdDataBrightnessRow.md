# NxdDataBrightnessRow

- **Kind:** structure
- **Area:** [Display](../areas/display.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.brightness table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="value"></a>`0x8` | value | `float32` | I | Value (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0.7 to 1.12, 11 distinct values. |

## Referenced by

- Described by tables: [NxdDataBrightness](../tables/NxdDataBrightness.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
