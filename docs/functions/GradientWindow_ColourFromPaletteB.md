# GradientWindow_ColourFromPaletteB

- **Address:** `0x1402206A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GradientWindow_ColourFromPaletteB(void *prims)`
- **Callers:** many panel builders
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

As GradientWindow_ColourFromPaletteA with palette B (0x142FEC4F0).

## Behavior

- V: same vertex palette index table and layout; only the source palette differs.

## Referenced by

- Called by: [LegacyTask12_Build](LegacyTask12_Build.md), [StatsPanel_Build](StatsPanel_Build.md)
- Reads tables: [GradientWindowVertexPalette](../tables/GradientWindowVertexPalette.md)

## Open questions

None recorded.
