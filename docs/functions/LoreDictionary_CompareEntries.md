# LoreDictionary_CompareEntries

- **Address:** `0x1401E4370`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool LoreDictionary_CompareEntries(const void *a, const void *b, int mode)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Comparator of two glossary list entries.

## Behavior

- V: mode 3: strcmp of family_name_first (+0x40), then the key; mode 2: sort_order_2 (+0x8, 0 sorts last); otherwise sort_order (+0x48, 0 sorts last).

## Referenced by

- Called by: [LoreDictionary_SortList](LoreDictionary_SortList.md)
- Observed behaviours: [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md)

## Open questions

None recorded.
