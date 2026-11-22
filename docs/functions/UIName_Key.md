# UIName_Key

- **Address:** `0x1403D87BC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `NameKey *UIName_Key(NameKey *out, const char *name)`
- **Callers:** JobTree_*, UI setters
- **Callees:** sub_1403D8A24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a lookup key for a node/state name: out->str = name, out->id = interned id (via the global name table qword_143CDA2A0).

## Behavior

- V: out+8 = 0, out+0 = Str1, then sub_1403D8A24(table, out, name, 0) interns the string. Callers release the key with sub_1403D8D1C when out+8 != 0.

## State touched

- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md), [Battle_InitScene](Battle_InitScene.md), [BgmMode_DrawRow](BgmMode_DrawRow.md), [ClassicSubtitles_SetState](ClassicSubtitles_SetState.md), [EventEndSlate_ShowTask](EventEndSlate_ShowTask.md), [EventNode_PlayShow](EventNode_PlayShow.md), [EventSubquestPanel_Run](EventSubquestPanel_Run.md), [FaceWidget_SetFace](FaceWidget_SetFace.md), [GUIList_SetCount](GUIList_SetCount.md), [GUINode_BuildFromFile](GUINode_BuildFromFile.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [GUINode_SetCursorOverState](GUINode_SetCursorOverState.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md), [GuideEntry_Fill](GuideEntry_Fill.md), [GuideSlot_DrawButtons](GuideSlot_DrawButtons.md), [JobChange_RunPreviewAnim](JobChange_RunPreviewAnim.md), [JobTreePanel_SetTextKey](JobTreePanel_SetTextKey.md), [JobTree_RefreshAddon](JobTree_RefreshAddon.md), [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md), [Launcher_DrawControlsPage](Launcher_DrawControlsPage.md), [Launcher_DrawInfoPage](Launcher_DrawInfoPage.md), [Launcher_DrawStartPage](Launcher_DrawStartPage.md), [MainTab_BindNodes](MainTab_BindNodes.md), [MainTab_SelectTab](MainTab_SelectTab.md), [ScrollHelper_Bind](ScrollHelper_Bind.md), [ShopItemList_FillRow](ShopItemList_FillRow.md), [SortieScreen_BindBoxes](SortieScreen_BindBoxes.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](SortieScreen_SetArea1Face.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [TabBar_ClearClick](TabBar_ClearClick.md), [TabBar_Select](TabBar_Select.md), [TabBar_SetTable](TabBar_SetTable.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [UIName_KeyIndexed](UIName_KeyIndexed.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md), [sub_1400F7378](sub_1400F7378.md), [sub_140107914](sub_140107914.md), [sub_1401319FC](sub_1401319FC.md), [sub_14013DD70](sub_14013DD70.md), [sub_1401560D0](sub_1401560D0.md), [sub_1402083B4](sub_1402083B4.md), [sub_14029BCD4](sub_14029BCD4.md), [sub_1402A9C4C](sub_1402A9C4C.md), [sub_1402A9D5C](sub_1402A9D5C.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1403DABF0](sub_1403DABF0.md)

## Notes

Every by-name lookup in the tree code is UIName_Key followed by a Find.

## Open questions

None recorded.
