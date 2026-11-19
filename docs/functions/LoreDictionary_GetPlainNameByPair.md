# LoreDictionary_GetPlainNameByPair

- **Address:** `0x1401E5934`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `const char *LoreDictionary_GetPlainNameByPair(int pair)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the plain name of the glossary row that a table 283 pair names.

## Behavior

- V: plain_name (the string at +0x3C, dword index 15 of the row, stored relative to +0x34) through the pair.

## Open questions

None recorded.
