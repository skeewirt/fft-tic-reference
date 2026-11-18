# JobAbilityList_Build

- **Address:** `0x1402867BC`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int64_t JobAbilityList_Build(uint16_t unit, int16_t jobId, int tab, int16_t *out, int mode)`
- **Callers:** JobTree_FillJobRecords, Job_LearnAbilityByMenu, sub_1400DC77C, sub_140286A78, sub_1402B9090, sub_1402B9598, sub_1402B9C20, sub_140366FE0
- **Callees:** Job_IdToIndex, Skillset_BuildAbilityList, Ability_GetJpCost, Job_IsHiddenFromTree, BitReader_ReadBits, sub_1402866E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of abilities shown for a job (skill-set abilities filtered by tab) for the job screen, learn menu and job-list availability tests.

## Behavior

- V: with mode 1 and tab 0 it returns JobSecondaryList (sub_1402866E4) instead.
- V: converts the job id with Job_IdToIndex, then scans g_JobTable (49-byte rows) for the row whose first byte matches; the skillset is that row's byte 0. A miss falls back to the unit's own job (unit+94).
- V: gets the abilities with Skillset_BuildAbilityList and zeroes every id outside the tab's range (tab 0: 1..421, tab 1: 422..453, tab 2: 454..485, tab 3: 486..509).
- V: 8 callers, including JobTree_FillJobRecords and Job_LearnAbilityByMenu.
- V: an entry carries the ability id plus one of three flags: 0x1000 is loaded at 0x140286A03 and ORed at 0x140286A2A; 0x4000 is loaded at 0x1402869ED and 0x140286A16 and ORed at 0x1402869F3; 0x6000 is loaded at 0x140286A25 and ORed at 0x140286A2A again. Mode 0 (tree/availability) writes 0x4000 or 0x6000, mode 2 (learn list) writes 0x4000 when the JP cost is above the unit's JP and 0x1000 otherwise, and mode 3 counts only.
- V: the flag word is appended without a further mask, and the list terminator 0xFFFF is produced from an all-ones register rather than from an immediate.

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [Skillset_BuildAbilityList](Skillset_BuildAbilityList.md), [Ability_GetJpCost](Ability_GetJpCost.md), [Job_IsHiddenFromTree](Job_IsHiddenFromTree.md), [Unit_CollectJobSkillsets](Unit_CollectJobSkillsets.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)
- Writes: [MenuListWord.cannot_equip](../structs/MenuListWord.md#cannot_equip), [MenuListWord.flag_0x1000](../structs/MenuListWord.md#flag_0x1000), [MenuListWord.flag_0x2000](../structs/MenuListWord.md#flag_0x2000)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [JobScreen_BuildLearnList](JobScreen_BuildLearnList.md), [JobScreen_RefreshLearnList](JobScreen_RefreshLearnList.md), [sub_140286A78](sub_140286A78.md), [sub_140366FE0](sub_140366FE0.md)
- Observed behaviours: [JobLearnedBitsPointerIsBuiltFromTheUnitRecord](../behaviors/JobLearnedBitsPointerIsBuiltFromTheUnitRecord.md), [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md)
- Reads tables: [AbilityAux](../tables/AbilityAux.md), [JobTable](../tables/JobTable.md)

## Notes

The tab filter (0x1402868DC..0x1402868F8) zeroes every entry outside [cx, ax], so an ability id of 512 or more would be dropped from every tab; the list words carry state flags 0x1000 / 0x2000 / 0x4000 and their readers mask with 0x3FF, so ids stay below 1024. The same loop exists twice more (Skillset_BuildTabAbilityList, sub_140392620).

The skillset of a job lives in the executable job table (byte 0), not in an nxd table.

The row guard and the search for the first row holding the job's skillset share one register loaded with the bound 0xAE; a job id of 0xAE or more reads no row (a null read; seen as a crash in the Jobs screen at +0x6A).

## Open questions

Tab boundary constants beyond tab 0 and 1 were read from the head of the function only.
