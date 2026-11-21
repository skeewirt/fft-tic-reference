# Job_IsHiddenFromTree

- **Address:** `0x1402CBED4`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int Job_IsHiddenFromTree(unsigned int jobId)`
- **Callers:** JobList_Build, Job_IsLockedForParty, PartyUnit_FillFromWork, sub_1401442FC, sub_140284F6C, sub_140289298, sub_14028A474, sub_14028ACD8, sub_1402867BC
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns 1 when the Job row (table 46, row = job id) has a nonzero hidden_from_job_list byte at +60, else 0.

## Behavior

- V: returns 0 when the registry or the Job table is missing, or the row cannot be fetched.
- V: reads row byte +60 and returns whether it is nonzero.
- V: the Job table object is cached in a global after the first lookup.

## Referenced by

- Called by: [JobAbilityList_Build](JobAbilityList_Build.md), [JobScreen_BuildLearnableList](JobScreen_BuildLearnableList.md), [PartyUnit_FillFromWork](PartyUnit_FillFromWork.md), [Party_GetSlotState](Party_GetSlotState.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [sub_14028A474](sub_14028A474.md), [sub_140392620](sub_140392620.md)

## Notes

Hidden jobs are skipped by the party-wide lock test and keep their stored unlock mask instead of a recomputed one.

## Open questions

None recorded.
