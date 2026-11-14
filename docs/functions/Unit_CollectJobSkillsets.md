# Unit_CollectJobSkillsets

- **Address:** `0x1402866E4`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int64_t Unit_CollectJobSkillsets(int16_t unitSlot, uint16_t *out)`
- **Callers:** JobAbilityList_Build
- **Callees:** JobList_BuildForPartyUnit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the secondary-skillset choice list of a party unit: the skillset byte of every job the unit can take, except its own job and three excluded ids, terminated by 0xFFFF. Returns the count.

## Behavior

- V (decompile): reads the unit's job word at party record +36, then fills a 24-word list with JobList_BuildForPartyUnit(unit, list, 1).
- V: for each listed job id except the unit's own job, 93, 161 and 164, writes the byte at g_JobTable + 49*id (the skillset byte, row +0) to the output; ids >= 174 (0xAE) use a null row pointer and read address 0 (a null-page read, same finding as J7).
- V: writes 0xFFFF after the last entry and returns the number written.
- V: of the JobTable fields it reads only the skillset byte (+0).

## State touched

- Calls: [JobList_BuildForPartyUnit](JobList_BuildForPartyUnit.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [JobAbilityList_Build](JobAbilityList_Build.md)
- Observed behaviours: [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md), [PerJobSlotStateLayouts](../behaviors/PerJobSlotStateLayouts.md), [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md), [SpriteLookupFailuresPastTheTables](../behaviors/SpriteLookupFailuresPastTheTables.md)

## Notes

J5c/J5e: the list holds skillset ids (224 for job 160); the command NAME later comes from JobCommand key = skillset id. The function is one of the 15 JobTable bound-readers (its bound is a compare against 0xAE).

The bound 0xAE is loaded into a register and compared from there.

The job list is a 24-word stack buffer (rsp+0x20). The ability screen's Secondary list in g_MenuList is built by this function, called from sub_140366FE0 through JobAbilityList_Build.

## Open questions

What reads ids 93, 161, 164 specially (Mime-like and hidden jobs, I).
