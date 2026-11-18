# SpriteLayerByteRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of SpriteLayerByteRows.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="row_a"></a>`0x0` | row_a | `uint8[24]` | I | byte stored in the sprite object at +19 for kinds 0..23 (0xC8 / 0xBC / 0xB0 groups) |
| <a id="row_b"></a>`0x18` | row_b | `uint8[24]` | I | byte stored at +18 (0x00, 0x10, 0x1E ... 0x8E steps) |
| <a id="row_c"></a>`0x30` | row_c | `uint8[24]` | I | second byte stored at +19 for the same kind in the other branch |

## Referenced by

- Described by tables: [SpriteLayerByteRows](../tables/SpriteLayerByteRows.md)

## Open questions

None recorded.
