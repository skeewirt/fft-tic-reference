# GradientWindowVertexPalette

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140672610`
- **Rows:** 12 rows of 1 bytes
- **Keyed by:** vertex 0..11 of a gradient window
- **Read by:** [GradientWindow_ColourFromPaletteA](../functions/GradientWindow_ColourFromPaletteA.md), [GradientWindow_ColourFromPaletteB](../functions/GradientWindow_ColourFromPaletteB.md)
- **Row layout:** [GradientWindowVertexPaletteIndex](../structs/GradientWindowVertexPaletteIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which palette colour each of the 12 vertices of a gradient window takes. Verdict: engine-data.

## Behavior

- V: loop bound 12 in both readers
- V: sub_140220640 and sub_1402206A8: colour the 12 vertices (stride 24) of a shaded window from one of two palettes

## Notes

Our names. Tags: V layout.

## Open questions

- ?: which window uses it
