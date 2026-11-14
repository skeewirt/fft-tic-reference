# TextureObj_Reset

- **Address:** `0x1403D0C6C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureObj_Reset(TextureObj *t)`
- **Callers:** CharaRender_DrawFrame, sub_1400CAE10, sub_1400CE1AC, sub_1400CF1D4, sub_1401E7440, sub_1403CAB00, sub_1403D090C, TextureObj_SetSource, TextureObj_Commit, sub_1403D0E10, sub_1403D11DC, sub_140415D30, sub_1404175DC, sub_14060FD44..FDAC
- **Callees:** sub_140011804, sub_1403C5F08, sub_14041FB00, sub_14003ABD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets a texture wrapper: frees pending source buffer and loader object, releases its entry in the global texture table and restores the default state.

## Behavior

- V: frees qword +24 (flag +32) and the 304-byte object at +16 exactly as TextureObj_Commit does.
- V: clears qword +52 (bpp and +56 width), dword +60, dword +76, qword +36 (+36 and +40).
- V: when dword +48 != 0: entry = g_TextureTable[+8 * index + 8]; non-null: sub_14003ABD0(entry) (release the GPU texture) and the slot is zeroed; +48 = 0.
- V: sets floats +84 and +88 to 1.0 and fills the 4 groups of bytes at +96..+111 with 0xFF (word at +96 + 4k, byte at +98 + 4k, byte at +99 + 4k): a default tint / UV-rect state. Returns 4 or 0 (Hex-Rays loop counter).

## State touched

- Reads: [g_TextureTable](../globals/g_TextureTable.md)

## Referenced by

- Called by: [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [TextureObj_Commit](TextureObj_Commit.md)

## Notes

The name is ours (IDB: sub_1403D0C6C).

## Open questions

? the meaning of the 0xFF block at +96..111 (four RGBA bytes?).
