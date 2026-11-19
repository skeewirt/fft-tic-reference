# UserSituation_IsMet

- **Address:** `0x1400FF8A4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool UserSituation_IsMet(void *unused, unsigned int situation)`
- **Callers:** BarTop_Setup and about 50 more (JobTree_FillJobRecords, Shop_GetUiRowId, sub_1401607D4, sub_140341094, ...)
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryCount, NxdTable_GetEntryByKeyIndex, NxdEntry_GetRow, UserSituation_TestCheck

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether a UserSituation condition (nxd table 90, keyed by situation and entry) holds; the UI asks it to show or lock features.

## Behavior

- V: 0 holds always; otherwise for each entry of the key (NxdTable_GetEntryCount / GetEntryByKeyIndex) it runs the checks k = 0..2 of the row in order through UserSituation_TestCheck: the kind at +8 + 4k, the ids at +24 + 8k and +60 + 8k, the values at +44 + 4k (fifth argument) and +80 + 4k (sixth argument); the values are passed only for kinds 3..11.
- V: per check k, in order: kind 0 returns false; a TestCheck result that differs from the byte at +92 + k (column blocking_result) abandons this entry and moves on to the next one; when all three checks equal their bytes the function returns false.
- V: after every entry was abandoned it returns true. So the byte at +0x5C + k is the result that blocks the situation, not a success value: an entry makes the situation unmet only when each of its checks returns exactly that byte.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_TestCheck](UserSituation_TestCheck.md)

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [CharaColorSkin_Resolve](CharaColorSkin_Resolve.md), [ChroniclePeriod_ListUnlocked](ChroniclePeriod_ListUnlocked.md), [GuideLessons_AnyNewlyUnlockable](GuideLessons_AnyNewlyUnlockable.md), [GuideLessons_UpdateUnlocked](GuideLessons_UpdateUnlocked.md), [GuideList_BuildLessons](GuideList_BuildLessons.md), [Guide_IsUnlocked](Guide_IsUnlocked.md), [Guide_TryAutoShow](Guide_TryAutoShow.md), [JournalList_Build](JournalList_Build.md), [LoreDictionary_BuildList](LoreDictionary_BuildList.md), [LoreDictionary_CurrentRow](LoreDictionary_CurrentRow.md), [LoreDictionary_PageCount](LoreDictionary_PageCount.md), [MapRow_SelectVariation](MapRow_SelectVariation.md), [TavernRumour_IsAvailable](TavernRumour_IsAvailable.md), [Unit_GetVoicePatternId](Unit_GetVoicePatternId.md), [WorldMapLocationPanel_Fill](WorldMapLocationPanel_Fill.md), [WorldMapRoute_Refresh](WorldMapRoute_Refresh.md), [WorldMap_ApplyProgressInfo](WorldMap_ApplyProgressInfo.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [ZodiacStone_AnyMet](ZodiacStone_AnyMet.md), [ZodiacStone_AnyMetAndNew](ZodiacStone_AnyMetAndNew.md), [ZodiacStone_ClearNewMarks](ZodiacStone_ClearNewMarks.md)
- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Name is ours (was sub_1400FF8A4). Situation 3220 (one entry: kind 6 on id 0, value 450, blocking_result 0) opens the tavern errand row.

## Open questions

? the meaning of the union type 121 in the row (the id is read alone).
