# Str_Format

- **Address:** `0x1400261CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int Str_Format(char *buf, size_t size, const char *fmt, ...)`
- **Callers:** JobTree_RefreshAddon
- **Callees:** sub_140026084

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

snprintf-style formatter (thin wrapper around sub_140026084). Builds arrow and label node names.

## Behavior

- V: 'Line%sLv%02d' / 'Line%s%s' for arrows; the four fixed names 'TextBoardJobLvB/T/R/L' are written with it at 0x140133B09.

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [Classic_BuildLaunchArguments](Classic_BuildLaunchArguments.md), [EventMusic_LoadTrack](EventMusic_LoadTrack.md), [FaceTexture_FormatName](FaceTexture_FormatName.md), [GUITabButton_Deselect](GUITabButton_Deselect.md), [GUITabButton_Select](GUITabButton_Select.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [IconBase_FormatPath](IconBase_FormatPath.md), [IconPath_FromIconId](IconPath_FromIconId.md), [Icon_FormatPath](Icon_FormatPath.md), [ItemIcon_FormatLargePath](ItemIcon_FormatLargePath.md), [ItemIcon_FormatSmallPath](ItemIcon_FormatSmallPath.md), [JobRecord_FromJobId](JobRecord_FromJobId.md), [JobTreePanel_SetJobIcon](JobTreePanel_SetJobIcon.md), [JobTree_RefreshAddon](JobTree_RefreshAddon.md), [MapTextures_NameOfFrame](MapTextures_NameOfFrame.md), [MovieSound_LoadBank](MovieSound_LoadBank.md), [NxdRegistry_LoadRootNxl](NxdRegistry_LoadRootNxl.md), [SaveSlot_LoadToLive](SaveSlot_LoadToLive.md), [SaveSlot_WriteFromLive](SaveSlot_WriteFromLive.md), [SortieScreen_BindBoxes](SortieScreen_BindBoxes.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [TabBar_SetTable](TabBar_SetTable.md), [TextTag_CountedNounArticle](TextTag_CountedNounArticle.md), [TextTag_CountedNounForms](TextTag_CountedNounForms.md), [TextTag_CountedNounIndexed](TextTag_CountedNounIndexed.md), [TextTag_CountedNounPlain](TextTag_CountedNounPlain.md), [TitleMenu_Build](TitleMenu_Build.md), [TurnPanel_SetTag](TurnPanel_SetTag.md), [TurnPanel_SetUnitPanel](TurnPanel_SetUnitPanel.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [UIName_KeyIndexed](UIName_KeyIndexed.md), [UITexturePath_FromRow](UITexturePath_FromRow.md), [WorldMapBaseScreen_Open](WorldMapBaseScreen_Open.md), [WorldMapLocationPanel_Init](WorldMapLocationPanel_Init.md), [WorldMapNode_PlayTexChange](WorldMapNode_PlayTexChange.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md), [WorldMapRoute_Refresh](WorldMapRoute_Refresh.md), [WorldMapRoute_SetGrey](WorldMapRoute_SetGrey.md), [WorldMapRoute_StartGrow](WorldMapRoute_StartGrow.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md), [sub_140036AE0](sub_140036AE0.md), [sub_1401321FC](sub_1401321FC.md), [sub_1402A9D5C](sub_1402A9D5C.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1403DABF0](sub_1403DABF0.md), [sub_1403DC8D0](sub_1403DC8D0.md)

## Open questions

None recorded.
