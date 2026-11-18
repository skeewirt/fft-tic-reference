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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set (0 everywhere). Observed in the stock rows: 0 in every row. |
| <a id="icon_id"></a>`0x4` | icon_id | `int32` | V | Icon of the job's command (96x96 part). Observed in the stock rows: 0 to 27, 28 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | V | Command name (e.g. Fundaments, Items, Arts of War). Observed in the stock rows: 51 distinct values, 144 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | I | Command description. Observed in the stock rows: 71 distinct values, 144 empty. |
| <a id="description2"></a>`0x10` | description2 | `string (int32 offset)` | I | Second description slot (null in every row). Observed in the stock rows: 2 distinct values, 226 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | V | Group / sort number. Equals the key for rows 1..~170; compared across commands. Observed in the stock rows: 0 to 226, 114 distinct values. |
| <a id="comment"></a>`0x18` | comment | `string (int32 offset)` | I | Null everywhere. Observed in the stock rows: empty in every row. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | V | Nonzero => secondary text/id; 0 in every stock row. Observed in the stock rows: 0 to 40010, 2 distinct values. |
| <a id="ui_dialog_id"></a>`0x20` | ui_dialog_id | `int32` | V | UIText key of an extra description shown in the job-change list (0, 18 or 19). A 0 means 'use the Description'. Observed in the stock rows: 0 to 19, 3 distinct values. |

## Referenced by

- Described by tables: [JobCommand](../tables/JobCommand.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
