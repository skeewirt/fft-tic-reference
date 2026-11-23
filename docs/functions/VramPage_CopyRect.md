# VramPage_CopyRect

- **Address:** `0x14025FA60`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int VramPage_CopyRect(int16 *rect, char *pixels)`
- **Callers:** EffectFile_UploadTexture, sub_140210AF0 and about ten more
- **Callees:** memmove, sub_14025F998, sub_14025FF68, sub_14026060C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a rectangle of 16-bit pixels into the 1024 by 512 video page (g_SaveYoxPage) and marks that area for upload.

## Behavior

- V: rect holds x, y, width, height in halfwords; a y of 512 or more is reduced by masking with 0x1FF and an x of 1024 or more has 1024 subtracted.
- V: the rectangle is clipped to the page (rows beyond 512 and columns beyond 1024 are dropped, a negative x skips source columns) and copied row by row with memmove at 2048 bytes per page row.
- V: afterwards it calls sub_14025F998, sub_14025FF68 and sub_14026060C on the rectangle, which update the area bookkeeping of the page.

## Referenced by

- Called by: [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md), [ClassicItemListPage_Run](ClassicItemListPage_Run.md), [EquipScreen_InitVram](EquipScreen_InitVram.md), [LegacyOptions_DrawTask](LegacyOptions_DrawTask.md), [OpeningTask_4](OpeningTask_4.md), [PanelScreen_InitVram](PanelScreen_InitVram.md), [SceneUnit_LoadExtraPage](SceneUnit_LoadExtraPage.md), [StatsPanel_Build](StatsPanel_Build.md), [WinRec_CopyToVram](WinRec_CopyToVram.md), [WindowPattern_Build](WindowPattern_Build.md)
- Reads tables: [ItemScreenPalette](../tables/ItemScreenPalette.md), [ShopScreenPalette](../tables/ShopScreenPalette.md)

## Notes

Name is ours. The page is the same one HdLayer_BuildTextures reads when it builds the Enhanced battle layer textures.

## Open questions

? what the three bookkeeping calls do exactly.
