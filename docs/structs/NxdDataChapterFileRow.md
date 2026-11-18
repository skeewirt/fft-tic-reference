# NxdDataChapterFileRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.chapter_file table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="chapter_number"></a>`0x5` | chapter_number | `uint8` | I | Chapter number (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 4, 5 distinct values. |

## Referenced by

- Described by tables: [NxdDataChapterFile](../tables/NxdDataChapterFile.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 3 columns not decoded.
