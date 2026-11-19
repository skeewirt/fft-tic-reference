# Guide_IsUnlocked

- **Address:** `0x1400DAA64`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool Guide_IsUnlocked(int id)`
- **Callers:** not recorded
- **Callees:** NxdEntry_GetRow, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether a guide counts as unlocked.

## Behavior

- V: true when seen_bit (+0x2A, 1-based number n, below 80) is set in the config bytes g_ConfigData +204, or when unlocked_by_story (+0x2C) is non-zero and UserSituation_IsMet(10200).

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_IsMet](UserSituation_IsMet.md)
- Reads: [g_ConfigData](../globals/g_ConfigData.md)

## Referenced by

- Called by: [GuideList_BuildCategory](GuideList_BuildCategory.md)
- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
