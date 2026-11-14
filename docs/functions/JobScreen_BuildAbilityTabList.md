# JobScreen_BuildAbilityTabList

- **Address:** `0x14028A770`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `int JobScreen_BuildAbilityTabList(int tab, int job_id, int mode)`
- **Callers:** JobScreen_OpenJobPage, JobScreen_ShowJobAbilities, sub_140367768
- **Callees:** Skillset_BuildTabAbilityList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the ability list of one tab for the party member the job screen has selected, then hands it to the job screen list builder.

## Behavior

- V: the selected party slot is the signed word at 0x141811428; the unit pointer is g_PartyUnits[slot].
- V: the job id and the tab come from the arguments, and the unit skillset flags byte +0x70 is passed to Skillset_BuildTabAbilityList.
- V: the call returns a list pointer, which is passed to the job screen list builder with the job id and the mode.
- V: the function tail-jumps to the list builder, so its return value is the builder result.
- V: the three callers are the job page, the ability page and the tree page, so the same tab builder serves all three.
- I: the tab argument is the page tab (action, support, movement, reaction) because the builder it calls applies the tab mask.
- ?: what the mode argument changes; the tail callee owns it.

## State touched

- Calls: [Skillset_BuildTabAbilityList](Skillset_BuildTabAbilityList.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_SelectedUnitIndex](../globals/g_SelectedUnitIndex.md)

## Notes

Whole function read (78 bytes).

## Open questions

None recorded.
