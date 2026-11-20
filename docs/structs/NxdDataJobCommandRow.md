# NxdDataJobCommandRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 36 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.job_command table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="icon"></a>`0x4` | icon | `int32` | V | Icon of the job's command (96x96 part). Observed in the stock rows: 0 to 27, 28 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 51 distinct values, 144 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 71 distinct values, 144 empty. |
| <a id="description_2"></a>`0x10` | description_2 | `string (int32 offset)` | M | Measured over every stock row: A second description text. Observed in the stock rows: 2 distinct values, 226 empty. |
| <a id="group"></a>`0x14` | group | `int32` | V | Read in the code: The command's group key: two JobCommand rows are the same command when this value is equal (variants of one command share it). Observed in the stock rows: 0 to 226, 114 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="user_situation"></a>`0x1C` | user_situation | `int32` | V | Read in the code: A UserSituation key; once that condition is met the job command detail window shows the second description (+0x10) instead of the first (+0x0C). Observed in the stock rows: 0 to 40010, 2 distinct values. |
| <a id="extra_text"></a>`0x20` | extra_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 19, 3 distinct values. |

## Referenced by

- Described by tables: [JobCommand](../tables/JobCommand.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
