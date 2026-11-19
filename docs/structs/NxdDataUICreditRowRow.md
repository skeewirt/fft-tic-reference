# NxdDataUICreditRowRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_credit_row table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="line_type"></a>`0x4` | line_type | `int32` | V | Read in the code: The credit-roll line type: it picks which widget template builds the line (and 0 just advances the roll by the script line's spacing). Observed in the stock rows: 0 to 39, 12 distinct values. |
| <a id="captions"></a>`0x8` | captions | `string (int32 offset)[] {int32 offset; uint32 count}` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 988 distinct values. |
| <a id="icon"></a>`0x10` | icon | `int32` | V | Read in the code: For a line of layout 5 (picture), the Icon id (table 118) shown; the line is drawn only when it is non-zero. Observed in the stock rows: 0 in every row. |
| <a id="icon_height"></a>`0x14` | icon_height | `int32` | V | Read in the code: For a picture line (layout 5), the height given to the image node. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUICreditRow](../tables/NxdDataUICreditRow.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
