# EffectPaletteSeedsRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 3 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EffectPaletteSeeds table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="r5"></a>`0x0` | r5 | `uint8` | V | red, 0..31 |
| <a id="g5"></a>`0x1` | g5 | `uint8` | V | green, 0..31 |
| <a id="b5"></a>`0x2` | b5 | `uint8` | V | blue, 0..31 |

## Referenced by

- Described by tables: [EffectPaletteSeeds](../tables/EffectPaletteSeeds.md)

## Open questions

None recorded.
