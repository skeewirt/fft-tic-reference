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
| <a id="unk_00"></a>`0x0` | unk_00 | `int32` | ? | Always 0. Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `string (int32 offset)` | I | Alternate-text slot (null in every row). Observed in the stock rows: empty in every row. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | I | Job name. Inline (English table). Observed in the stock rows: 104 distinct values, 40 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | I | Alternate-text slot (null in every row). Observed in the stock rows: empty in every row. |
| <a id="description"></a>`0x10` | description | `string (int32 offset)` | I | Job description for the job-change / tree detail. Observed in the stock rows: 107 distinct values, 48 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `string (int32 offset)` | ? | Text column, null in every row. Observed in the stock rows: empty in every row. |
| <a id="jobtype_id"></a>`0x18` | jobtype_id | `int32` | V | JobType row. Also indexes a party-wide runtime flag array (byte_1411A7490[type+21], type < 125) and is compared across jobs ('same type'). Observed in the stock rows: 0 to 114, 115 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | I | Monster family id (78..93, 99, 100, 94..97 for story monsters); 0 for generic jobs. I. Observed in the stock rows: 0 to 100, 24 distinct values. |
| <a id="jobcommand_id"></a>`0x20` | jobcommand_id | `uint32` | V | The job's command (battle menu entry + skillset name). Generic jobs: key - 69 (5..24). Observed in the stock rows: 0 to 223, 128 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | I | Monster sprite/portrait pair, first element (1..95, odd); 0 for non-monsters. I. Observed in the stock rows: 0 to 95, 49 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | I | Monster sprite/portrait pair, second element (2..96, even = first + 1). Observed in the stock rows: 0 to 96, 49 distinct values. |
| <a id="texture_parts_index"></a>`0x2C` | texture_parts_index | `uint32` | V | Job icon (48x48 part) shown by the 'IconJob' image nodes and the tree panel. 1..20 for the generic jobs, 24 (60x60) is the locked placeholder. Observed in the stock rows: 0 to 23, 24 distinct values. |
| <a id="uijobabilityhelp_id"></a>`0x30` | uijobabilityhelp_id | `uint32` | V | Row of the job help text (the 'Job Overview / Usable Equipment / Select Abilities' page). 0 = none. Observed in the stock rows: 0 to 34, 35 distinct values. |
| <a id="egg_id"></a>`0x34` | egg_id | `uint32` | V | Egg row (monster family stage set); 0 for non-monsters. Observed in the stock rows: 0 to 48, 49 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | ? | Probably an ordering key (generic jobs 200..390 step 10, monsters 500..970, story 10..150, -1 none): I. It is NOT an Icon key (V by data: Icon 200..231 are treasure parts). No reader found by J1 or J3. Observed in the stock rows: -1 to 970, 86 distinct values. |
| <a id="hide_job_tree"></a>`0x3C` | hide_job_tree | `int32` | V | nonzero: the job is not offered in the job list / tree (JobList_Build returns only the current job for such a unit; Job_IsLockedForParty skips such units). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Job](../tables/Job.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

3 of 16 columns not decoded.
