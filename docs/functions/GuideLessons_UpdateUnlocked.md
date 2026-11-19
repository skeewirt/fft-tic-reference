# GuideLessons_UpdateUnlocked

- **Address:** `0x1400DA5D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideLessons_UpdateUnlocked(void)`
- **Callers:** not recorded
- **Callees:** NxdEntry_CopyKeys, NxdSets_Find2, NxdSets_Find3, NxdTable_GetEntryByIndex, NxdEntry_GetRow, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks the lessons whose conditions are met as unlocked.

## Behavior

- V: from the entry index of guide 3001 onward, for lessons (category +0xC of 7 or more, seen_bit +0x2A non-zero): when the job-type test (+0x14) passes and user_situation (+0x18) is 0 or met, sets bit +0x2A in g_UnitJobFlags +169.

## State touched

- Calls: [NxdEntry_CopyKeys](NxdEntry_CopyKeys.md), [NxdSets_Find2](NxdSets_Find2.md), [NxdSets_Find3](NxdSets_Find3.md), [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_IsMet](UserSituation_IsMet.md)
- Writes: [g_GuideLessonUnlockedBits](../globals/g_GuideLessonUnlockedBits.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
