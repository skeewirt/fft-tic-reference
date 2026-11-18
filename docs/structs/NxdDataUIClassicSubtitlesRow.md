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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="subtitle"></a>`0x8` | subtitle | `string (int32 offset)` | I | Subtitle text. Observed in the stock rows: 77 distinct values, 16 empty. |
| <a id="start_second"></a>`0xC` | start_second | `float32` | I | Start second (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 216.5, 81 distinct values. |
| <a id="end_second"></a>`0x10` | end_second | `float32` | I | End second (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 223.8, 81 distinct values. |
| <a id="type"></a>`0x14` | type | `int32` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 4, 3 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIClassicSubtitles](../tables/NxdDataUIClassicSubtitles.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 7 columns not decoded.
