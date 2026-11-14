# HdGroup_BuildPiece

- **Address:** `0x1403D0F8C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int64_t HdGroup_BuildPiece(HdSheetGroup *group, int index, uint32_t *palette, int hash, int x, int y, int w, int h, uint32_t *out, int pitch, int bpp)`
- **Callers:** HdLayer_BuildTextures
- **Callees:** TextureObj_SetSource, TextureObj_Commit, sub_1403D0BF8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds one texture of a sheet group: a rectangle of the group's sheet pixels, expanded through a converted palette into 32-bit texels.

## Behavior

- V: the source is the group's buffer pointer (+2696); the texture is the group's record `index` (144 bytes each from +2704).
- V: bpp 4: from byte y * (pitch / 2) + x / 2, w / 2 bytes a row, low nibble first, each nibble an index into `palette`; bpp 8: from byte y * pitch + x, w bytes a row, each byte an index.
- V: the texels go to `out`; a texture that exists with the same width and height is updated in place (sub_1403D0BF8), else it is given the buffer as a new 32-bit source (TextureObj_SetSource, TextureObj_Commit) and the group's texture count (+21136) goes up for a new one.
- V: then stores the hash, in-use 1, the age 60 and x, y, w, h in the record and returns the record's texture id (dword +48).

## State touched

- Calls: [TextureObj_SetSource](TextureObj_SetSource.md), [TextureObj_Commit](TextureObj_Commit.md)

## Referenced by

- Called by: [HdLayer_BuildTextures](HdLayer_BuildTextures.md)
- Observed behaviours: [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md)
- Reads file formats: [SpriteSheetEntries](../formats/SpriteSheetEntries.md)

## Notes

The name is ours (IDB: sub_1403D0F8C). Structure: HdSheetGroup. Any other bpp value writes no texels and still makes the texture.

## Open questions

None recorded.
