# SpriteKindFlagRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of SpriteEffectKindFlags.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flag"></a>`0x0` | flag | `uint8` | I | 1 for kinds 4, 5 and 20..28; the effect position code skips copying the position when the flag is set |

## Referenced by

- Described by tables: [SpriteEffectKindFlags](../tables/SpriteEffectKindFlags.md)

## Open questions

None recorded.
