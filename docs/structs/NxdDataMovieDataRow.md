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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="path"></a>`0x8` | path | `string (int32 offset)` | M | Measured over every stock row: File paths. Observed in the stock rows: 15 distinct values, 8 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="link"></a>`0x10` | link | `union {int32 kind; int32 id}` | V | Read in the code: A typed reference to the movie's subtitle set: a table id (16 bits at +0x10) and a key (+0x14); id 192 opens the classic subtitles window, 209 the subtitles window. Observed in the stock rows: 22 distinct values. |
| <a id="classic_path"></a>`0x18` | classic_path | `string (int32 offset)` | V | Read in the code: The path of the movie's classic version: when non-empty it is played instead of path (+8), the language track (+0x20) is not used and the classic subtitle style is set. Observed in the stock rows: 8 distinct values, 15 empty. |
| <a id="sound_bank"></a>`0x1C` | sound_bank | `int32` | V | Read in the code: The movie's sound number: Movie_Start loads sound/movie/movie%04d/movie%04d_bgm.sab, _voice.sab and _se.sab with this number (a negative value loads nothing). Observed in the stock rows: -1 to 120, 14 distinct values. |
| <a id="localized_path"></a>`0x20` | localized_path | `string (int32 offset)` | V | Read in the code: A second movie file used as the movie's language track for every language except language 0. Observed in the stock rows: 3 distinct values, 20 empty. |
| <a id="pausable"></a>`0x24` | pausable | `uint8` | V | Read in the code: When set, the movie can be paused: the movie controller runs its pause state machine (pause window, then resume or skip) while it plays. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="skippable"></a>`0x25` | skippable | `uint8` | V | Read in the code: The movie can be skipped from its pause window: MovieControl +25 (the skippable byte) is set while it plays. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="skip_on_press"></a>`0x26` | skip_on_press | `uint8` | V | Read in the code: When set, the movie has no pause window: pressing the confirm / skip action ends it at once. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataMovieData](../tables/NxdDataMovieData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
