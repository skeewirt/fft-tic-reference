# g_LanguageInfo

- **Kind:** global
- **Address:** `0x143CD9B10`
- **Type:** `LanguageInfo *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

+8 = language code: 0 Japanese, 1 English, 2 French, 3 German, 4 Simplified Chinese, 5 Traditional Chinese, 6 Korean. Set at start from the Windows user locale and Steam's game language, and again after settings.sav loads from the saved text language (registry TextLanguageCodes, behavior TextLanguage).

## Referenced by

- Observed behaviours: [TextLanguage](../behaviors/TextLanguage.md)
- Read by: [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [CharaRender_InitTargets](../functions/CharaRender_InitTargets.md), [EventEndSlate_ShowTask](../functions/EventEndSlate_ShowTask.md), [EventMapTitle_DrawSweep](../functions/EventMapTitle_DrawSweep.md), [EventMapTitle_LoadTexture](../functions/EventMapTitle_LoadTexture.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [EventMessage_Task](../functions/EventMessage_Task.md), [EventPanel_PickRow](../functions/EventPanel_PickRow.md), [EventScript_LoadFile](../functions/EventScript_LoadFile.md), [EventScript_LoadIntoBuffer](../functions/EventScript_LoadIntoBuffer.md), [EventTasks_Init](../functions/EventTasks_Init.md), [GUICore_Ctor](../functions/GUICore_Ctor.md), [GUIFontSet_FontTypeForLanguage](../functions/GUIFontSet_FontTypeForLanguage.md), [GUITextNode_Layout](../functions/GUITextNode_Layout.md), [GUITextNode_PlaceGlyph](../functions/GUITextNode_PlaceGlyph.md), [GUITextNode_WrapLine](../functions/GUITextNode_WrapLine.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [SaveSlot_BuildClassicTitle](../functions/SaveSlot_BuildClassicTitle.md), [SaveWork_ImportLegacyHeader](../functions/SaveWork_ImportLegacyHeader.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SceneTasks_Init](../functions/SceneTasks_Init.md), [TopLevelExceptionFilter](../functions/TopLevelExceptionFilter.md), [sub_140344B68](../functions/sub_140344B68.md)

## Open questions

None recorded.
