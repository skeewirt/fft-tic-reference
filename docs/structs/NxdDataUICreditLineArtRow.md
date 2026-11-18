# NxdDataUICreditLineArtRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_credit_line_art table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="ui_name"></a>`0x4` | ui_name | `string (int32 offset)` | I | Ui name text. Observed in the stock rows: 18 distinct values, 2 empty. |

## Referenced by

- Described by tables: [NxdDataUICreditLineArt](../tables/NxdDataUICreditLineArt.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
