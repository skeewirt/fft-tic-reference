# SecondarySkillsetListsTakeEveryUnlockedJob

- **Kind:** observed behaviour
- **Scope:** engine (secondary skillset lists)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [Unit_CollectJobSkillsets](../functions/Unit_CollectJobSkillsets.md), [Unit_CollectJobSkillsetPairs](../functions/Unit_CollectJobSkillsetPairs.md), [JobList_BuildForPartyUnit](../functions/JobList_BuildForPartyUnit.md), [sub_140366FE0](../functions/sub_140366FE0.md), [JobScreen_FindJobOfSkillset](../functions/JobScreen_FindJobOfSkillset.md), [JobScreen_BuildTabList](../functions/JobScreen_BuildTabList.md), [g_MenuList](../globals/g_MenuList.md), [g_JobAbilityPairList](../globals/g_JobAbilityPairList.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Both secondary-skillset collectors build the unit's job list into a 24-word stack buffer, and write into lists that hold 145 entries: the three lists the game builds them into (g_MenuList, g_JobAbilityPairList, JobScreen_FindJobOfSkillset's frame list).

## Behavior

- V (disassembly): Unit_CollectJobSkillsets and Unit_CollectJobSkillsetPairs call JobList_BuildForPartyUnit(unit, list, 1) with a 24-word list in their own frame and walk it to the 0xFFFF terminator; each listed job except the unit's job word (+0x24), 93, 161 and 164 gives one output entry: the job row's skillset byte as a word, or the 8-byte entry (job, skillset).
- V: the Secondary choices of the ability screen are Unit_CollectJobSkillsets' output in g_MenuList (sub_140366FE0, tab 1, through JobAbilityList_Build with tab 0 and mode 1); the pair list goes into g_JobAbilityPairList (JobScreen_BuildTabList, tab 1) and into JobScreen_FindJobOfSkillset's 146-entry frame list, both through JobScreen_BuildJobTabRows with tab 0 and mode 1.
- V: g_MenuList is 256 words and the stock builders stop at 145 entries; g_JobAbilityPairList and the frame list hold 146 entries of 8 bytes (both initialised as 146 entries).

## Notes

The 145-entry limit is the game's list size (g_MenuList is shared with every shop and equip list; the frame list cannot grow in place).

## Open questions

? not run in the game: the Secondary list with more entries than a screenful (scrolling, choosing a late entry's skillset, the job shown for it); ? the other 24-word job lists (JobScreen_FillUnitRows' word_14375F800, sub_1400DCFE4's word_143CDAAE0, JobChange_FillUnitEntry's frame list) still end at 23 entries.
