# SpriteClassicFileRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where one classic sprite file is and how long it is.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="file"></a>`0x0` | file | `uint32` | V | File number passed to the sector reader; its first 0x200 bytes are the palettes the HD sheet is drawn with. |
| <a id="size"></a>`0x4` | size | `uint32` | V | Byte length read from that file. |

## Referenced by

- Described by tables: [SpriteClassicFilesByShape](../tables/SpriteClassicFilesByShape.md), [SpriteClassicFilesByShapeB](../tables/SpriteClassicFilesByShapeB.md)

## Open questions

None recorded.
