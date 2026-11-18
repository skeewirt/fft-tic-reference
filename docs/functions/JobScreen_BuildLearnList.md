# JobScreen_BuildLearnList

- **Address:** `0x1402B9598`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobScreen_BuildLearnList(void)`
- **Callers:** sub_140367644
- **Callees:** sub_140303E4C, JobAbilityList_Build, sub_140327854, sub_14031EA20, Input_TestAction, JobScreen_ShowPopup, sub_140303E8C, sub_1402C0554, sub_1402B956C, sub_14031ED4C, Unit_SpendJp, sub_1403278EC, sub_14031DA24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the Learn page of the job screen: the job ability list, the JP cost and the learn action for the selected party unit.

## Behavior

- V: the selected party slot is 0x141811428 and the unit pointer is g_PartyUnits[slot].
- V: it clears the screen flag at 0x140D407C7 on the first call and fills the list callbacks once.
- V: JobAbilityList_Build supplies the job ability list; the list words are tested with the 0x3FF mask at 0x1402B976E and 0x1402B9842.
- V: Unit_SpendJp is called when the player confirms a learn, and sub_14031DA24 handles the resulting message.
- V: the level and JP columns come from the job menu readers and the page popup state.
- V: Input_TestAction is polled for navigation and confirm; sub_1403278EC draws the list.
- V: the two list lookups mask the word with 0x3FF before the table read, and the panel state dword at +0x44 is set to 0x100014 and later 0x100050.
- I: this is the Learn page rather than the ability page, because it is the only one that calls Unit_SpendJp.
- ?: the exact page mode that selects this builder from its caller; the caller switch was not read.

## State touched

- Calls: [JobAbilityList_Build](JobAbilityList_Build.md), [Input_TestAction](Input_TestAction.md), [JobScreen_ShowPopup](JobScreen_ShowPopup.md), [sub_1402C0554](sub_1402C0554.md), [Unit_SpendJp](Unit_SpendJp.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_JobTable](../globals/g_JobTable.md)

## Referenced by

- Reads tables: [JobLearnListScriptLang1](../tables/JobLearnListScriptLang1.md), [JobLearnListScriptLang2](../tables/JobLearnListScriptLang2.md), [JobLearnListScriptLang3](../tables/JobLearnListScriptLang3.md)

## Notes

Whole function read (1333 bytes). The two 0x3FF masks are the sites the ability-width study lists.

## Open questions

None recorded.
