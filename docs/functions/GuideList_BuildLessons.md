# GuideList_BuildLessons

- **Address:** `0x1400DAD58`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideList_BuildLessons(int tab, int *out)`
- **Callers:** not recorded
- **Callees:** NxdEntry_CopyKeys, NxdSets_Find2, NxdSets_Find3, NxdTable_GetEntryByIndex, NxdEntry_GetRow, UserSituation_IsMet, sub_1400DBB5C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the lesson list of one Lessons tab.

## Behavior

- V: lessons of tab (category +0xC - 7) that pass the tests, stored as {id, new}; new = the +146 read bit is clear. At most 128 entries, sorted by Guide sort_order (+0x28).

## State touched

- Calls: [NxdEntry_CopyKeys](NxdEntry_CopyKeys.md), [NxdSets_Find2](NxdSets_Find2.md), [NxdSets_Find3](NxdSets_Find3.md), [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_IsMet](UserSituation_IsMet.md)
- Reads: [g_GuideLessonReadBits](../globals/g_GuideLessonReadBits.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
