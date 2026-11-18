# UnitJobFlagsBlock

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 146 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job flag block (g_UnitJobFlags).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="job_new"></a>`0x0` | job_new | `uint8[21]` | V | One flag per generic job index 0..20 (saved as an array of is_new records). |
| <a id="type_disable"></a>`0x15` | type_disable | `uint8[125]` | V | One flag per job type 0..124 (saved as disable_flag); index 0 is never written by the recompute. |

## Referenced by

- Described by tables: [UnitJobFlags](../tables/UnitJobFlags.md)

## Open questions

None recorded.
