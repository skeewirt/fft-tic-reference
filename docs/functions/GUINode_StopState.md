# GUINode_StopState

- **Address:** `0x140409ECC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_StopState(GUINode *node, NameKey *key)`
- **Callers:** JobTree_Set*State, JobTree_SetPanelRecord
- **Callees:** GUINode_FindState, GUINode_FindDescendant

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stops a named state (+104 = 0, clears timers and flags) and recursively stops the nested states of kind 5.

## Behavior

- V: FindState, then zero +76/+80/+84/+104..+110; for each 64-byte entry in the state's child list (+176..+184) of type 5, look the child node up and stop it.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_FindDescendant](GUINode_FindDescendant.md)

## Referenced by

- Called by: [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md), [Battle_InitScene](Battle_InitScene.md), [FaceWidget_SetFace](FaceWidget_SetFace.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUIComponent_Disable](GUIComponent_Disable.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_OnDown](GUIComponent_OnDown.md), [GUIComponent_OnFocusGained](GUIComponent_OnFocusGained.md), [GUIComponent_OnFocusLost](GUIComponent_OnFocusLost.md), [GUIComponent_OnUp](GUIComponent_OnUp.md), [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md), [GUIList_SetCount](GUIList_SetCount.md), [GUINode_PlayCursorOutState](GUINode_PlayCursorOutState.md), [GUINode_PlayCursorOverState](GUINode_PlayCursorOverState.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [GUINode_SetCursorOverState](GUINode_SetCursorOverState.md), [GUINode_UpdateStates](GUINode_UpdateStates.md), [GUIWidget_Hide](GUIWidget_Hide.md), [GUIWidget_Show](GUIWidget_Show.md), [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md), [Launcher_DrawControlsPage](Launcher_DrawControlsPage.md), [Launcher_DrawInfoPage](Launcher_DrawInfoPage.md), [MainTab_SelectTab](MainTab_SelectTab.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [ShopItemList_DrawRow](ShopItemList_DrawRow.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](SortieScreen_SetArea1Face.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [TabBar_ClearClick](TabBar_ClearClick.md), [TabBar_Select](TabBar_Select.md), [TabBar_SetTable](TabBar_SetTable.md), [UIAddonFingerCursor_ResetPose](UIAddonFingerCursor_ResetPose.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [WorldMapRoute_SetGrey](WorldMapRoute_SetGrey.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [sub_1400F6148](sub_1400F6148.md), [sub_140107914](sub_140107914.md), [sub_1401319FC](sub_1401319FC.md), [sub_14013DD70](sub_14013DD70.md), [sub_14029BCD4](sub_14029BCD4.md), [sub_1402A9C4C](sub_1402A9C4C.md), [sub_1402A9D5C](sub_1402A9D5C.md)

## Open questions

None recorded.
