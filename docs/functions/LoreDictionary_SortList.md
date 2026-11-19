# LoreDictionary_SortList

- **Address:** `0x1401E50D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LoreDictionary_SortList(void *list, int count, int mode)`
- **Callers:** not recorded
- **Callees:** LoreDictionary_CompareEntries

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sorts a glossary list by a mode.

## Behavior

- I: sorts with LoreDictionary_CompareEntries and the mode (the sort body was not read).

## State touched

- Calls: [LoreDictionary_CompareEntries](LoreDictionary_CompareEntries.md)

## Referenced by

- Called by: [LoreDictionary_BuildList](LoreDictionary_BuildList.md)

## Open questions

None recorded.
