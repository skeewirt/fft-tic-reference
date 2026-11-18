# NxdDataEggRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.egg table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set. Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Null. Observed in the stock rows: empty in every row. |
| <a id="job_id1"></a>`0x8` | job_id1 | `int32` | V | job id given to the hatched monster at stage 1. Observed in the stock rows: 0 to 139, 17 distinct values. |
| <a id="job_id2"></a>`0xC` | job_id2 | `int32` | V | job id at stage 2. Observed in the stock rows: 0 to 140, 17 distinct values. |
| <a id="job_id3"></a>`0x10` | job_id3 | `int32` | V | job id at stage 3. Observed in the stock rows: 0 to 141, 33 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | I | modulus of a random draw: n = rand % Unknown14 + 1 (min 2); the unit's A+5 value becomes 17*n (<= 365). Observed in the stock rows: 0 to 9, 8 distinct values. |

## Referenced by

- Described by tables: [NxdDataEgg](../tables/NxdDataEgg.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
