# TextureObj_SetSource

- **Address:** `0x1403D0A80`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureObj_SetSource(TextureObj *t, void *pixels, int w, int h, int bpp, int a6, int a7, char a8)`
- **Callers:** CharaRender_BuildAtlasTexture, sub_1403D0F8C, sub_140415828, sub_140415D30, sub_14041E05C
- **Callees:** sub_1403D0C6C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a texture wrapper new source pixel data (pointer, size, bit depth): when the existing GPU texture has the same size and depth it is marked for update-in-place, otherwise it is reset.

## Behavior

- V: when dword t+48 (texture table index) != 0 and dword +56 == w, +60 == h, +52 == bpp: dword +76 = 1 (reuse flag). Otherwise sub_1403D0C6C (TextureObj_Reset).
- V: stores +36 = a6, +40 = a7, byte +80 = a8, +56 = w, +60 = h, +52 = bpp, +44 = bpp, qword +24 = pixels. Returns 0.

## Referenced by

- Called by: [HdGroup_BuildPiece](HdGroup_BuildPiece.md), [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [sub_14041E05C](sub_14041E05C.md)

## Notes

The name is ours (IDB: sub_1403D0A80). Used by the character atlas builder, so this class is not UI specific; it ran on the Job Tree because the chara portraits / icons share it. Field meanings of +36 / +40 / +80 are ?.

## Open questions

? a6 / a7 / a8 (+36 / +40 / +80).
