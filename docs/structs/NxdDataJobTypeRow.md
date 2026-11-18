# NxdDataJobTypeRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.job_type table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set (0 everywhere). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Null everywhere. Observed in the stock rows: empty in every row. |
| <a id="male_visual_icon_id"></a>`0x8` | male_visual_icon_id | `int32` | V | Icon key (701..719) of the job's male 'visual' image (job_visual/textureparts/jv_NN_m). Nonzero only for the 20 generic job types; JobRecord.out[0] = this when the unit is male. Observed in the stock rows: 0 to 719, 20 distinct values. |
| <a id="female_visual_icon_id"></a>`0xC` | female_visual_icon_id | `int32` | V | Icon key (720..738) of the female visual (jv_NN_f). Observed in the stock rows: 0 to 738, 20 distinct values. |

## Referenced by

- Described by tables: [NxdDataJobType](../tables/NxdDataJobType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
