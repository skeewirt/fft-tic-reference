# ClassicCursorRows_Select

- **Address:** `0x14036E28C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `short *ClassicCursorRows_Select(int *state)`
- **Callers:** sub_14036E1D8, sub_14036E360
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the cursor of a legacy menu to the row chosen in the state record.

## Behavior

- V: the row table is the language 0 block (base 0x1408FB62E) or the block of the other languages (base 0x1408FB94E); rows are 24 bytes.
- V: stores x + 14 and y + 12 of the row as the cursor position and, when the row's key differs from the state's current key, resets the cursor animation (mode 120 when the key is non-zero, 2 otherwise).

## Referenced by

- Called by: [StatusGlossary_Input](StatusGlossary_Input.md), [StatusGlossary_Open](StatusGlossary_Open.md)
- Reads tables: [LegacyCursorRowsLang0](../tables/LegacyCursorRowsLang0.md), [LegacyCursorRowsLangOther](../tables/LegacyCursorRowsLangOther.md)

## Open questions

None recorded.
