# NxdDataMovieDataRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.movie_data table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="movie_file_path"></a>`0x8` | movie_file_path | `string (int32 offset)` | I | File path string. Observed in the stock rows: 15 distinct values, 8 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 22 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 8 distinct values, 15 empty. |
| <a id="movie_sound_file_id"></a>`0x1C` | movie_sound_file_id | `int32` | I | Movie sound file id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 120, 14 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 3 distinct values, 20 empty. |
| <a id="flag_24"></a>`0x24` | flag_24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_25"></a>`0x25` | flag_25 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_26"></a>`0x26` | flag_26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataMovieData](../tables/NxdDataMovieData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 11 columns not decoded.
