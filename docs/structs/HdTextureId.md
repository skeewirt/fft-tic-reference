# HdTextureId

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventSpriteHdTextures table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="texture_id"></a>`0x0` | texture_id | `uint32` | V | HD texture id used for that event sprite (-1 = none); a second texture id = this + 140 |

## Referenced by

- Described by tables: [BattleSpriteHdTextures](../tables/BattleSpriteHdTextures.md), [EventSpriteHdTextures](../tables/EventSpriteHdTextures.md), [SpecialSheetHdTextures](../tables/SpecialSheetHdTextures.md)

## Open questions

None recorded.
