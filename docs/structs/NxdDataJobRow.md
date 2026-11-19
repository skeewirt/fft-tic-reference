# NxdDataJobRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.job table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 104 distinct values, 40 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="description"></a>`0x10` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 107 distinct values, 48 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="job_type"></a>`0x18` | job_type | `int32` | M | Measured over every stock row: Every value is a key of nxd.JobType. Observed in the stock rows: 0 to 114, 115 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 24 distinct values. |
| <a id="job_command"></a>`0x20` | job_command | `uint32` | M | Measured over every stock row: Every value is a key of nxd.JobCommand-en. Observed in the stock rows: 0 to 223, 128 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 95, 49 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 96, 49 distinct values. |
| <a id="icon_part"></a>`0x2C` | icon_part | `uint32` | V | Job icon (48x48 part) shown by the 'IconJob' image nodes and the tree panel. 1..20 for the generic jobs, 24 (60x60) is the locked placeholder. Observed in the stock rows: 0 to 23, 24 distinct values. |
| <a id="ui_job_ability_help"></a>`0x30` | ui_job_ability_help | `uint32` | M | Measured over every stock row: Every value is a key of nxd.UiJobAbilityHelp-en. Observed in the stock rows: 0 to 34, 35 distinct values. |
| <a id="egg"></a>`0x34` | egg | `uint32` | M | Measured over every stock row: Every value is a key of nxd.Egg. Observed in the stock rows: 0 to 48, 49 distinct values. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 970, 86 distinct values. |
| <a id="hidden_from_job_list"></a>`0x3C` | hidden_from_job_list | `int32` | V | nonzero: the job is not offered in the job list / tree (JobList_Build returns only the current job for such a unit; Job_IsLockedForParty skips such units). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Job](../tables/Job.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 8 of 16 columns not decoded.
