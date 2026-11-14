# JobListWord

- **Kind:** structure
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of g_RuntimeJobList: the job id in bits 0..9, bit 13 locked (not unlocked by any party member) and bit 14 current job. 0xFFFF ends the list.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="job_id"></a>bits 0..9 | job_id | `uint16` | V | Job id; JobTree_FillJobRecords masks it with 0x3FF at 0x1403687B6, JobList_IsSelectedEntryUnflagged uses the whole word in a not/and test. | [JobList_Build](../functions/JobList_Build.md) | [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md) |
| <a id="locked"></a>bit 13 | locked | `bit` | V | Set by JobList_Build when Job_IsLockedForParty returns non-zero (0x1402865C3-0x1402865CF); JobTree_FillJobRecords tests it at 0x140368861. | [JobList_Build](../functions/JobList_Build.md) | [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md) |
| <a id="current_job"></a>bit 14 | current_job | `bit` | V | Set by JobList_Build for the unit's own job when mode 2 (0x140286512, 0x14028659F); JobTree_FillJobRecords tests it at 0x140368884 and JobList_IsSelectedEntryUnflagged returns ~word & 0x4000 >> 14. | [JobList_Build](../functions/JobList_Build.md) | [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md) |
| <a id="terminator"></a>list end | terminator | `uint16` | V | 0xFFFF after the last entry (0x140286608). |  |  |

## Behavior

- V: the same flags are read as a state by JobTree_FillJobRecords: 2 = locked, 1 = current, 0 = free.
- V: the list is rebuilt per unit and is not saved.

## Referenced by

- Observed behaviours: [JobListEntryWordMeaning](../behaviors/JobListEntryWordMeaning.md)

## Notes

V: the sheets JobList_Build, JobTree_FillJobRecords and JobList_IsSelectedEntryUnflagged.

## Open questions

? whether a job can set both bits at once; the stock builder sets one or the other.
