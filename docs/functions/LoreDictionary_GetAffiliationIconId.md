# LoreDictionary_GetAffiliationIconId

- **Address:** `0x1401E4924`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int LoreDictionary_GetAffiliationIconId(void *screen, const int *key)`
- **Callers:** not recorded
- **Callees:** LoreDictionary_CurrentRow, LoreDictionary_GetEntry, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the affiliation icon id of a glossary entry's current row.

## Behavior

- V: LoreAffiliation (table 241) +8 of lore_affiliation (+0x14) of the current row; the glossary draws it as the icon at +976.

## State touched

- Calls: [LoreDictionary_CurrentRow](LoreDictionary_CurrentRow.md), [LoreDictionary_GetEntry](LoreDictionary_GetEntry.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Open questions

None recorded.
