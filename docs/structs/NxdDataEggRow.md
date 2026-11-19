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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="job"></a>`0x8` | job | `int32` | M | Measured over every stock row: Every value is a key of nxd.Job-en. Observed in the stock rows: 0 to 139, 17 distinct values. |
| <a id="job_2"></a>`0xC` | job_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Job-en. Observed in the stock rows: 0 to 140, 17 distinct values. |
| <a id="job_3"></a>`0x10` | job_3 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Job-en. Observed in the stock rows: 0 to 141, 33 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 8 distinct values. |

## Referenced by

- Described by tables: [NxdDataEgg](../tables/NxdDataEgg.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 6 columns not decoded.
