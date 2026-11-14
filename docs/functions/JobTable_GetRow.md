# JobTable_GetRow

- **Address:** `0x1400F8574`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `char *JobTable_GetRow(unsigned int jobId)`
- **Callers:** JobList_RecomputeAvailability, JobRecord_FillIconAndGenericFlag, sub_1400F72F0, sub_1400FBB7C, sub_140117E1C, sub_14012F138, sub_14012FC6C
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the Job-en row for a job key (null if missing). Lazily caches table 46 in qword_143CDA2D8.

## Behavior

- V: registry lookup of table id (int)qword_143CDA2D8 + 46 = 46, then keyed row lookup (sub_1403D3AE8).
- V: in-memory Job row fields read by callers: +24 jobtype (JobType key, runtime flag index), +32 jobcommand (JobCommand key), +36 / +40 monster pair, +44 TexturePartsIndex, +48 uijobabilityhelp.

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [JobRecord_FromJobId](JobRecord_FromJobId.md)
- Reads tables: [Job](../tables/Job.md)

## Notes

Same getter shape as AbilityTable_GetRow. A second inlined copy of the lookup sits in sub_140270C58 and sub_1402CBF60.

## Open questions

Job +52 (egg) and +56 / +60 (Unknown15, HideJobTree) have no reader found.
