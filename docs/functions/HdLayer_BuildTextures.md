# HdLayer_BuildTextures

- **Address:** `0x140415D30`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int64_t HdLayer_BuildTextures(void)`
- **Callers:** sub_1402569F8
- **Callees:** HdGroup_BuildPiece, Pixels_ExpandToRgba, Rgb555ToRgba8888, PackFile_ReadEntry, TextureObj_SetSource, TextureObj_Commit, TextureObj_Reset, Mem_Alloc, sub_1403D2450, sub_1403D25A4, sub_1403D090C, sub_1403D0BF8, sub_1403D11DC, sub_140415BF4, sub_140415CFC, sub_140418F20, sub_14041DBCC, sub_14041DF24, sub_14041DF84, sub_14041DFB4, sub_14041E05C, sub_14041E3D8, sub_14041EA74, sub_1400C7734, sub_1400C92C8, sub_1400CB45C, sub_1400D575C, sub_1400D578C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle HD layer's texture pass: for every draw record of the frame it finds or builds the texture of its sheet piece and palette, and writes the texture id into the record.

## Behavior

- V: walks the draw records (152 bytes each) of the list at +936 of the object at qword_140D3AD60; a record's texture slot is its dword +44 minus 2048, its sheet entry the dword +64, its palette id the word +68 and its piece number the dword +72.
- V: the palette colours are read from the emulated video memory at g_SaveYoxPage + 32 * (id & 0x3F) + 2048 * (id >> 6).
- V: slots 0..2, 7 and 8..58 are single textures: the cache keys are the entry (dword_143CC96C0[slot]) and the palette id (word_143CC9CB0[slot]); on a miss the entry is read, 16 colours go through Rgb555ToRgba8888 and the 4-bit pixels through Pixels_ExpandToRgba (512 x 512 for slot 7, 96 x 96 in 128 x 128 for 8..58, 96 x 64 or 64 x 96 otherwise); slots 5 and 6 hand the entry's bytes to sub_1403D090C with no palette.
- V: slots 59 and up belong to the 20 sheet groups (g_HdSheetGroups, 21144 bytes each), 16 slots per group: 59.. group 0, 75.. group 1, 91.. group 2, 107.. group 3, 123..266 groups 4 to 12, 267.. group 13, 283.. group 14, 299..346 groups 15 to 17, 347.. group 18, 363.. group 19.
- V: a group whose entry number (+2692) differs from the record's frees its 128 textures and reads the new entry into its buffer (+2696, 0x80000 bytes, allocated once).
- V: a group texture is looked up by the hash of the palette colours (sub_14041DBCC, FNV-1a over 2 bytes per colour) and, for a piece, the piece's four rectangle values; on a miss a free texture is taken and HdGroup_BuildPiece builds it.
- V: groups 15 to 17 hash and convert 256 colours and build with 8-bit pixels (pitch 512 or 256 by a per-group flag); every other group 16 colours and 4-bit pixels with pitch 512.
- V: at its start it clears the per-frame tables, releases the single textures of the slots 3..7 no record names, and ages the group textures: a texture used in the last pass gets the age 60, an unused one counts down and is freed at 0, or at once while its group holds more than 64 textures (sub_1403D11DC).
- V: records with a slot below 2048 (+44 up to 0x116) take another path through sub_14041DFB4, sub_14041EA74 and the character renderer's tables, not read here.
- V (2026-11-20): the slot tables hold exactly 379 slots (0..378; the release loop stops at 379, a record past slot 0x17A takes the other path) and lie back to back: dword_143CC96C0[379] is followed at once by word_143CC9CB0, the texture objects are 379 x 112 bytes from 0x142E9BDA0 with other data right after, and the 20 groups end where qword_142F0D7C0 begins (the ageing loop's end address).

## State touched

- Calls: [HdGroup_BuildPiece](HdGroup_BuildPiece.md), [Pixels_ExpandToRgba](Pixels_ExpandToRgba.md), [Rgb555ToRgba8888](Rgb555ToRgba8888.md), [PackFile_ReadEntry](PackFile_ReadEntry.md), [TextureObj_SetSource](TextureObj_SetSource.md), [TextureObj_Commit](TextureObj_Commit.md), [TextureObj_Reset](TextureObj_Reset.md), [Mem_Alloc](Mem_Alloc.md), [sub_1403D2450](sub_1403D2450.md), [sub_1403D25A4](sub_1403D25A4.md), [sub_14041E05C](sub_14041E05C.md)

## Referenced by

- Observed behaviours: [HdLayerUnitSheetsAreTenFixedGroups](../behaviors/HdLayerUnitSheetsAreTenFixedGroups.md), [HdSheetFromSlotColoursFromRecord](../behaviors/HdSheetFromSlotColoursFromRecord.md), [HeldWeaponsDrawFromOneSheetPageByAByteRow](../behaviors/HeldWeaponsDrawFromOneSheetPageByAByteRow.md), [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md), [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md), [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Notes

The name is ours (IDB: sub_140415D30). Read: the slot and group paths of the texture pass (the parts that turn sheet pixels and palette colours into textures); the path of records below slot 2048 only in outline. For the entries 602 and 425 it replaces the 16 colours in the video memory by the constants at 0x140722AD0 before it converts them. Which unit uses which group is set where the draw primitives are made (sub_140260CF0): sheet page 4 / 5 -> groups 0 / 1, pages 20..28 -> groups 4..12, page 0x11 -> group 13, with the slot inside the group from sub_14041E448(group, palette id) (HdSheetGroup_ClaimClutEntry).

## Open questions

? the path of the records below slot 2048; ? what the groups 2, 3, 14 to 19 hold in play (their entries are fixed numbers or set elsewhere).
