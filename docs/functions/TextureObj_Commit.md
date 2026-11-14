# TextureObj_Commit

- **Address:** `0x1403D0B10`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureObj_Commit(TextureObj *t)`
- **Callers:** CharaRender_BuildAtlasTexture, sub_1400CAF20, sub_1400CEB4C, sub_1403CA874, sub_1403D0F8C, sub_140415828, sub_140415D30, sub_14041E05C
- **Callees:** sub_1403D0BF8, TextureTable_Create32, TextureObj_Reset, sub_140011804, sub_1403C5F08, sub_14041FB00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns the pending source pixels into a GPU texture (or updates the existing one), then frees the source buffer and the loader object.

## Behavior

- V: +76 != 0: sub_1403D0BF8(t, *(+24), 0, 0, +36, +40) updates the existing texture in place; the rest is skipped.
- V: otherwise +64 = 0; bpp +52 == 8: texture index = 0 (no GPU creation); bpp == 32: index = TextureTable_Create32(g_TextureTable, 32, w, h, pixels); any other depth: TextureObj_Reset and return 0xFFFFFFFF. Stores +48 = index, floats +68 = w, +72 = h.
- V: then frees the source buffer: when qword +24 is non-null, if dword +32 != 0 sub_140011804(ptr, 0, 0) frees it, +32 = 0; +24 = 0. If qword +16 (a 304-byte loader object) is non-null it is cleared, destroyed with sub_1403C5F08 and freed with sub_14041FB00(ptr, 304).
- V: returns 0.

## State touched

- Calls: [TextureTable_Create32](TextureTable_Create32.md), [TextureObj_Reset](TextureObj_Reset.md)
- Reads: [g_TextureTable](../globals/g_TextureTable.md)

## Referenced by

- Called by: [HdGroup_BuildPiece](HdGroup_BuildPiece.md), [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [sub_14041E05C](sub_14041E05C.md)

## Notes

The name is ours (IDB: sub_1403D0B10). Only 32-bit RGBA textures are created; 8-bit sources (palette indexed) get index 0 here (handled elsewhere: ?).

## Open questions

? what an index 0 texture means for 8-bit sources; ? sub_1403D0BF8.
