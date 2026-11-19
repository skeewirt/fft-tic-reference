# LoreDictionary_GetEntry

- **Address:** `0x1401E5018`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LoreDictionary_GetEntry(const uint8_t **out, int key, int subkey)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetEntryByKeys2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fetches a glossary row.

## Behavior

- V: *out = NxdTable_GetEntryByKeys2(237, key, subkey).

## State touched

- Calls: [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)

## Referenced by

- Called by: [LoreDictionary_CurrentRow](LoreDictionary_CurrentRow.md), [LoreDictionary_GetAffiliationIconId](LoreDictionary_GetAffiliationIconId.md), [LoreDictionary_GetIcon](LoreDictionary_GetIcon.md)

## Open questions

None recorded.
