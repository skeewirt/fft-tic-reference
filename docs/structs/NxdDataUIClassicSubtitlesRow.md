# NxdDataUIClassicSubtitlesRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_classic_subtitles table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="subtitle"></a>`0x8` | subtitle | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 77 distinct values, 16 empty. |
| <a id="starts_at"></a>`0xC` | starts_at | `float32` | M | Measured over every stock row: Seconds, rising down the table, each before its end value. Observed in the stock rows: -1 to 216.5, 81 distinct values. |
| <a id="ends_at"></a>`0x10` | ends_at | `float32` | M | Measured over every stock row: Seconds, each after its start value. Observed in the stock rows: -1 to 223.8, 81 distinct values. |
| <a id="line_layout"></a>`0x14` | line_layout | `int32` | V | Read in the code: Picks the state the classic-movie subtitle window plays for the line: 0 -> 'Line01', 1 -> 'Line02', 2 -> 'Line03', 3 -> 'Line04', 4 -> 'Line05' (any other value -> 'Line01'). Observed in the stock rows: 0 to 4, 3 distinct values. |
| <a id="keep_shown"></a>`0x18` | keep_shown | `uint8` | V | Read in the code: When set, the subtitle stays on screen after its end time (the window is not hidden) until the next line replaces it. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIClassicSubtitles](../tables/NxdDataUIClassicSubtitles.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
