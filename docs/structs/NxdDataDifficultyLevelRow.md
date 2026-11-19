# NxdDataDifficultyLevelRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.difficulty_level table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 70 to 110, 3 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 50 to 120, 3 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 35 to 110, 3 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 50 to 120, 3 distinct values. |
| <a id="ui_text"></a>`0x18` | ui_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 3547 to 3549, 3 distinct values. |

## Referenced by

- Described by tables: [NxdDataDifficultyLevel](../tables/NxdDataDifficultyLevel.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 6 of 7 columns not decoded.
