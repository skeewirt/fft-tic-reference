# SpritePaletteLimit

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the SpritePaletteLimits table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="max_palette"></a>`0x0` | max_palette | `uint8` | V | upper bound for the palette number a unit of this sheet may use (unit palette + 8 is clamped to it) |

## Referenced by

- Described by tables: [SpritePaletteLimits](../tables/SpritePaletteLimits.md)

## Open questions

None recorded.
