# JobTable

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x140785E30`
- **Rows:** 174 rows of 49 bytes
- **Keyed by:** job id (0..73 special characters, 74..93 generic jobs, 94 and up monsters, 160 / 161 reserved)
- **Read by:** [EquipDetail_Refresh](../functions/EquipDetail_Refresh.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [JobAbilityList_Build](../functions/JobAbilityList_Build.md), [JobScreen_ShowJobAbilities](../functions/JobScreen_ShowJobAbilities.md), [Job_BuildTabAbilityList](../functions/Job_BuildTabAbilityList.md), [Job_LearnAbilityByMenu](../functions/Job_LearnAbilityByMenu.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [Party_CountMasteredJobs](../functions/Party_CountMasteredJobs.md), [SaveWork_UnpackToLive_Repair](../functions/SaveWork_UnpackToLive_Repair.md), [UIGadgetFFTOJobDetailWindow_SetJob](../functions/UIGadgetFFTOJobDetailWindow_SetJob.md)
- **Held in:** [g_JobTable](../globals/g_JobTable.md)
- **Row layout:** [JobTableRow](../structs/JobTableRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The stock job table: per job the skillset, always-on abilities, equipment classes, stat growth, base move / jump / evade, status and element sets and the look bytes of marker-130 units. The only copy of the job stats; the NXD Job table carries only names, descriptions and icons.

## Behavior

- V: read by about thirty functions; fifteen of them guard the job id against 0xAE and an id of 174 or more reads outside the table.
- V: the unit job byte (save record +2, work record +3) is the index.
- V: 28 functions read this table (cross-references in the database); the first ten are linked.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of jump flag bit 7
- I: the three status bytes sets and the element set are zero for every generic job, so their meaning is taken from the original layout
