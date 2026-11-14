# JobScreen_BuildJobTabRows

- **Address:** `0x14028A6E8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int JobScreen_BuildJobTabRows(int16 partyIndex, int16 job, int tab, uint16 *out, int mode)`
- **Callers:** JobScreen_OpenJobPage, JobScreen_ShowJobAbilities, sub_14028A8B0, JobScreen_FindJobOfSkillset, JobScreen_BuildTabList, sub_140367AA0
- **Callees:** Unit_CollectJobSkillsetPairs, Job_BuildTabAbilityList, sub_14028A474

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The ability rows of one tab of a job on the job screen, for a party unit.

## Behavior

- V: mode 1 with tab 0: Unit_CollectJobSkillsetPairs(partyIndex, out) (the secondary skillsets).
- V: otherwise Job_BuildTabAbilityList(job, tab, unit flags B +112, the unit's secondary skillset B +94), then sub_14028A474 builds the rows from that list (JP from the party record, learned bits through the bit reader).

## State touched

- Calls: [Unit_CollectJobSkillsetPairs](Unit_CollectJobSkillsetPairs.md), [Job_BuildTabAbilityList](Job_BuildTabAbilityList.md), [sub_14028A474](sub_14028A474.md)

## Referenced by

- Called by: [JobScreen_BuildTabList](JobScreen_BuildTabList.md), [JobScreen_FindJobOfSkillset](JobScreen_FindJobOfSkillset.md), [JobScreen_ShowJobAbilities](JobScreen_ShowJobAbilities.md), [sub_14028A8B0](sub_14028A8B0.md), [sub_140367AA0](sub_140367AA0.md)
- Observed behaviours: [PassiveListsJoinTheCurrentAndStockJobs](../behaviors/PassiveListsJoinTheCurrentAndStockJobs.md)

## Open questions

None recorded.
