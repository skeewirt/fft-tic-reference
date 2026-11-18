# SpriteMotionByKindRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of SpriteMotionByKind.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="motion_a"></a>`0x0` | motion_a | `uint8[16]` | I | row A: motion number for the kind class (used when the request mask hits the sprite's flag) |
| <a id="motion_b"></a>`0x10` | motion_b | `uint8[16]` | I | row B: motion number for the kind class otherwise |

## Referenced by

- Described by tables: [SpriteMotionByKind](../tables/SpriteMotionByKind.md)

## Open questions

None recorded.
