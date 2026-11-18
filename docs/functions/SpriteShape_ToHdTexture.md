# SpriteShape_ToHdTexture

- **Address:** `0x14027411C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int SpriteShape_ToHdTexture(long long unused, int shape)`
- **Callers:** the sprite and effect set-up code
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the HD texture id of a sprite shape number, or -1 when the shape has none.

## Behavior

- V: shape 205 is first replaced by 76.
- V: shapes 0..81 read exe.sprite.shape_hd_texture directly (the table has 82 entries).
- V: shapes 84..89, 104, 105 and 106..111 return fixed ids from 822 to 829 by compare chains; every other shape returns -1.

## Referenced by

- Reads tables: [SpriteShapeHdTexture](../tables/SpriteShapeHdTexture.md)

## Notes

Name is ours. The ids of the compare chain are not listed here.

## Open questions

?: what the ids of shapes above 81 are.
