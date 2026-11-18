# PaletteFormat

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the PaletteFormats table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="colours"></a>`0x0` | colours | `uint32` | V | number of palette entries converted (16 or 256) |
| <a id="format"></a>`0x4` | format | `uint32` | V | format code passed to the texture upload (2 or 32) |
| <a id="unknown_a"></a>`0x8` | unknown_a | `uint32` | ? | 5 / 1 |
| <a id="unknown_b"></a>`0xC` | unknown_b | `uint32` | ? | 1 / 1 |

## Referenced by

- Described by tables: [PaletteFormats](../tables/PaletteFormats.md)

## Open questions

None recorded.
