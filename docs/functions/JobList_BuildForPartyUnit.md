# JobList_BuildForPartyUnit

- **Address:** `0x14028662C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int JobList_BuildForPartyUnit(uint8 partyIndex, uint16 *list, int mode)`
- **Callers:** 7 (job tree, job change screen, sub_14028A7C0, sub_14028A8B0, sub_1402B90D4, Unit_CollectJobSkillsets, sub_1400DCFE4)
- **Callees:** JobList_Build

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the job list of one party unit: points the bit reader at its unlock mask and calls JobList_Build with its job, marker and flags.

## Behavior

- V: the unit is g_PartyUnits[partyIndex]; the bit reader pointer becomes its record +120 (the unlock mask).
- V: passes a 6-byte summary (job word +36, marker +114, flags +112, and whether +62 is positive) and returns JobList_Build's count.

## State touched

- Calls: [JobList_Build](JobList_Build.md)

## Referenced by

- Called by: [JobScreen_FillUnitRows](JobScreen_FillUnitRows.md), [Unit_CollectJobSkillsetPairs](Unit_CollectJobSkillsetPairs.md), [Unit_CollectJobSkillsets](Unit_CollectJobSkillsets.md), [sub_14028A8B0](sub_14028A8B0.md)
- Observed behaviours: [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md), [JobTreeLockState](../behaviors/JobTreeLockState.md), [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)

## Open questions

None recorded.
