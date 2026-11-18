# NxdDataUIColorRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_color table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 15 distinct values, 187 empty. |
| <a id="color"></a>`0x8` | color | `uint32` | I | Color (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 65535 to 4.29497e+09, 69 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIColor](../tables/NxdDataUIColor.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
