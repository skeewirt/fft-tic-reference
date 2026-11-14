# PackFile_ReadEntry

- **Address:** `0x1403D25D8`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `__int64 PackFile_ReadEntry(PackFile *pack, unsigned index, char *out)`
- **Callers:** CharaRender_BuildAtlasTexture, sub_140415D30, sub_14041E05C
- **Callees:** PackEntry_Inflate, PackFile_EntryPtr, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies (and, when needed, inflates) one entry of an index-addressed pack into a caller buffer.

## Behavior

- V: PackEntry_Inflate(state with window 0x8000, out, PackFile_EntryPtr(index)).
- V (2026-11-10): the pack handle of all three callers is the g2d.dat reader `qword_140D3AD58` (see sub_1403D2450); the result is the inflated length, -1 makes the callers load the entry again once.

## State touched

- Calls: [PackEntry_Inflate](PackEntry_Inflate.md), [PackFile_EntryPtr](PackFile_EntryPtr.md)

## Referenced by

- Called by: [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [sub_14041E05C](sub_14041E05C.md)
- Observed behaviours: [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md), [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md)
- Reads file formats: [SpriteSheetEntries](../formats/SpriteSheetEntries.md)

## Notes

The unit renderer's sheet index (dword_1407151F0[shape] + which) is passed here; these are the entry numbers of g2d.dat (V 2026-11-10: the handle is the g2d.dat reader).

## Open questions

None recorded.
