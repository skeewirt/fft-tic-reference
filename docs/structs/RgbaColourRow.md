# RgbaColourRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of GfxColourCubePalette.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="colour"></a>`0x0` | colour | `uint32` | V | red, green, blue, alpha (always 0xFF) of the entry; red, green and blue climb in steps of 8 (a colour cube) |

## Referenced by

- Described by tables: [GfxColourCubePalette](../tables/GfxColourCubePalette.md)

## Open questions

None recorded.
