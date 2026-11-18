# GradientWindow_ColourFromPaletteA

- **Address:** `0x140220640`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GradientWindow_ColourFromPaletteA(void *prims)`
- **Callers:** many panel builders (Battle_UnitStatusFillAlt, StatsPanel_Build, ...)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Colours the 12 vertices of a gradient window from palette A.

## Behavior

- V: for each vertex takes a palette index from the vertex palette index table (0x140672610), expands that 15-bit colour of palette A (0x142FEC4D0) to 8-bit red, green and blue, and stores it (stride 24).
- V: sets a palette id word (+374) and returns it.

## Referenced by

- Called by: [LegacyTask12_Build](LegacyTask12_Build.md), [StatsPanel_Build](StatsPanel_Build.md)
- Reads tables: [GradientWindowVertexPalette](../tables/GradientWindowVertexPalette.md)

## Open questions

None recorded.
