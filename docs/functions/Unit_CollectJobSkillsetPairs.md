# Unit_CollectJobSkillsetPairs

- **Address:** `0x14028A7C0`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int Unit_CollectJobSkillsetPairs(int16 partyIndex, uint16 *out)`
- **Callers:** JobScreen_BuildJobTabRows
- **Callees:** JobList_BuildForPartyUnit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lists (job, skillset) pairs of the jobs a party unit can take as its secondary skill: 8-byte entries, 0xFFFF in the second word ends the list.

## Behavior

- V: the job list is JobList_BuildForPartyUnit(partyIndex, list, 1); skips the unit's own job (B +36), 93, 161 and 164.
- V: each entry gets the job id and its JobTable row's skillset (row guard: job < 0xAE stock); returns the count.
- V: the job list is a 24-word stack buffer (rsp+0x28); the terminator is the qword at out[count] whose low dword is 0xFFFF0000 (the high dword is an uninitialised stack word); words 2 and 3 of an entry are not written.

## State touched

- Calls: [JobList_BuildForPartyUnit](JobList_BuildForPartyUnit.md)

## Referenced by

- Called by: [JobScreen_BuildJobTabRows](JobScreen_BuildJobTabRows.md)
- Observed behaviours: [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md), [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)

## Open questions

None recorded.
