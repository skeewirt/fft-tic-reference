# GradientWindowVertexPaletteIndex

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the GradientWindowVertexPalette table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="palette_index"></a>`0x0` | palette_index | `uint8` | V | index into a 16-entry 15-bit colour palette (0x142FEC4D0 / 0x142FEC4F0); the colour is expanded to 8-bit RGB into the vertex |

## Referenced by

- Described by tables: [GradientWindowVertexPalette](../tables/GradientWindowVertexPalette.md)

## Open questions

None recorded.
