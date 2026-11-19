# LoreDictionary_GetIcon

- **Address:** `0x1401E47A0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int LoreDictionary_GetIcon(void *screen, const int *key)`
- **Callers:** not recorded
- **Callees:** LoreDictionary_CurrentRow, LoreDictionary_GetEntry, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the icon of a glossary entry's current row.

## Behavior

- V: returns icon (+0x24) of the entry's current row (LoreDictionary_CurrentRow); the glossary then sets it with GuiImage_SetIconById on the node at +1792.

## State touched

- Calls: [LoreDictionary_CurrentRow](LoreDictionary_CurrentRow.md), [LoreDictionary_GetEntry](LoreDictionary_GetEntry.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Open questions

None recorded.
