# NumberFields_Draw

- **Address:** `0x140242C84`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void NumberFields_Draw(void *buffer, const NumberField *fields, short *pos, int count)`
- **Callers:** Battle_UnitStatusFillAlt, StatsPanel_Build and seven other panel builders
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a list of number fields (32-byte records) into a staging buffer.

## Behavior

- V: for each field sets the pen to its x / y, reads the s16 value through the field's pointer and draws it with the digit count / style word, using mode 0 or mode 1 (two digit routines).

## Referenced by

- Called by: [LegacyTask12_Build](LegacyTask12_Build.md), [StatsPanel_Build](StatsPanel_Build.md)
- Reads tables: [StatsPanelNumbers](../tables/StatsPanelNumbers.md)

## Open questions

None recorded.
