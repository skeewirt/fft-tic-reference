# NxdDataUISubtitlesTimelineRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_subtitles_timeline table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 26 distinct values, 6 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 79, 80 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 2 distinct values, 92 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUISubtitlesTimeline](../tables/NxdDataUISubtitlesTimeline.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 6 columns not decoded.
