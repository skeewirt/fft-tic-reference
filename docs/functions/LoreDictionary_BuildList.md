# LoreDictionary_BuildList

- **Address:** `0x1401E412C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LoreDictionary_BuildList(int category, void *out, int unused, int mode)`
- **Callers:** sub_1401703C0 (list refresh: mode = glossary +3488 + 4 * tab, category = dword_14070E768[tab]), sub_1401705E0 and sub_1401E4B24 (mode 1, all)
- **Callees:** UserSituation_IsMet, LoreDictionary_SortList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the glossary list of one category.

## Behavior

- V: category a2 (4 = all) gives up to 150 entries {key, -1}, one for every first key with at least one met row (the category filter reads +0x10); sorted by LoreDictionary_SortList with mode a4 (comparator LoreDictionary_CompareEntries).

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md), [LoreDictionary_SortList](LoreDictionary_SortList.md)
- Reads: [tbl_GlossaryTabCategory](../globals/tbl_GlossaryTabCategory.md)

## Referenced by

- Called by: [LoreDictionary_ClearNewMarks](LoreDictionary_ClearNewMarks.md)
- Observed behaviours: [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md)

## Open questions

None recorded.
