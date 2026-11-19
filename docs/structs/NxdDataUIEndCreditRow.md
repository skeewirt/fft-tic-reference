# NxdDataUIEndCreditRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_end_credit table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="ui_credit_line_art"></a>`0x4` | ui_credit_line_art | `int32` | V | Read in the code: A UICreditLineArt row (table 304) whose element is placed on the roll at this line; 0 = none. Observed in the stock rows: 0 to 18, 17 distinct values. |
| <a id="ui_credit_row"></a>`0x8` | ui_credit_row | `int32` | V | Read in the code: The UICreditRow (table 309) that gives this line's layout and captions. Observed in the stock rows: 0 to 1226, 890 distinct values. |
| <a id="sound_enhanced"></a>`0xC` | sound_enhanced | `int32` | V | Read in the code: Music started at this line: on the first line it is started at once, later it is queued to start at the line's position. Observed in the stock rows: 0 to 252, 2 distinct values. |
| <a id="spacing"></a>`0x10` | spacing | `int32` | V | Read in the code: The vertical space in pixels this line adds to the roll position. Observed in the stock rows: 0 to 26, 4 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIEndCredit](../tables/NxdDataUIEndCredit.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
