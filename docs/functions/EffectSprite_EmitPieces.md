# EffectSprite_EmitPieces

- **Address:** `0x140380878`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectSprite_EmitPieces(EffectSpritePrim *prim, int16 *pos, int64 a3, int64 a4, int64 *list)`
- **Callers:** EffectSprite_StepAnimation
- **Callees:** Effect_PatchPolygonSeams, sub_1400D372C, sub_140380840

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns an effect sprite's current frame pieces into textured quads at the sprite's position.

## Behavior

- V: one quad per piece (count = prim byte +3); a piece is 24 bytes: +0 u16 palette row (low 4 bits, bit 0x10 = the second bank: palette id (w & 0xF) + 4 * ((w & 0x10) | 0x1EC0)), +1 bit 0x02 semi-transparent, +2 u16 texture page, +4 u, +5 v, +6 width, +7 height in the texture, +8..+23 four corners as s16 x, y (top-left, top-right, bottom-left, bottom-right).
- V: the corners are rotated / projected by the camera matrix (sub_1400D372C) around the sprite position.
- I (data, the PlayStation primitive layout): texture page bits 5-6 = blend (0 average, 1 add, 2 subtract, 3 add a quarter), bits 7-8 = depth (0 = 4 bits, 1 = 8 bits); the stock files use x = 6 (video page x 384), where the file's texture is uploaded.
- V: for effects 467..472 with 4 pieces it widens the pieces by 2 / 4 units (seam fix); Effect_PatchPolygonSeams runs first.

## State touched

- Calls: [Effect_PatchPolygonSeams](Effect_PatchPolygonSeams.md)

## Referenced by

- Called by: [EffectSprite_StepAnimation](EffectSprite_StepAnimation.md)

## Notes

Name is ours (was sub_140380878).

## Open questions

None recorded.
