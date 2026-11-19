# LoreDictionary_CurrentRow

- **Address:** `0x1401E4BDC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int LoreDictionary_CurrentRow(int key, int page)`
- **Callers:** not recorded
- **Callees:** UserSituation_IsMet, LoreDictionary_GetEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the second key of the glossary row shown for an entry and page.

## Behavior

- V: the n-th met row with replaces_previous (+0x4E) == 0, then replaced by any later met rows with replaces_previous set, until the next met page row; 0 when none.

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md), [LoreDictionary_GetEntry](LoreDictionary_GetEntry.md)

## Referenced by

- Called by: [GlossaryList_DrawRow](GlossaryList_DrawRow.md), [LoreDictionary_GetAffiliationIconId](LoreDictionary_GetAffiliationIconId.md), [LoreDictionary_GetIcon](LoreDictionary_GetIcon.md)
- Observed behaviours: [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md)

## Open questions

None recorded.
