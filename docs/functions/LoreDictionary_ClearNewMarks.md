# LoreDictionary_ClearNewMarks

- **Address:** `0x1401E4B24`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LoreDictionary_ClearNewMarks(void)`
- **Callers:** not recorded
- **Callees:** LoreDictionary_BuildList, LoreDictionary_IndexOfKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the new mark of every listed glossary entry.

## Behavior

- V: clears the byte at save block +7179 + 2 * index for every entry of the all-entries list.
- I: the byte is the per-entry 'new' mark (see SaveBlockUiMarks).

## State touched

- Calls: [LoreDictionary_BuildList](LoreDictionary_BuildList.md), [LoreDictionary_IndexOfKey](LoreDictionary_IndexOfKey.md)

## Open questions

None recorded.
