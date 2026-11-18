# JobMasteryIdRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One job id.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="job_id"></a>`0x0` | job_id | `uint32` | V | Job whose skillsets must be mastered to set mask bit 0x8 of the unlock mask. |

## Referenced by

- Described by tables: [JobMasteryIds](../tables/JobMasteryIds.md)

## Open questions

None recorded.
