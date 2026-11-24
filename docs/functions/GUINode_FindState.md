# GUINode_FindState

- **Address:** `0x140409774`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `NodeState *GUINode_FindState(GUINode *node, NameKey *key)`
- **Callers:** JobTree_SetArrowState, JobTree_SetLabelState, JobTree_SetPanelRecord
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a named state (animation/visibility group) of a node in its state vector.

## Behavior

- V: state vector at node+616..+624 (8-byte pointers), rotating start index at node+640; matches by interned id (state+8) or by string compare. Returns the state or null.

## Referenced by

- Called by: [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md), [Battle_InitScene](Battle_InitScene.md), [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [BgmMode_DrawRow](BgmMode_DrawRow.md), [ClassicSubtitles_SetState](ClassicSubtitles_SetState.md), [ErrorBanner_Show](ErrorBanner_Show.md), [EventEndSlate_ShowTask](EventEndSlate_ShowTask.md), [EventNode_PlayShow](EventNode_PlayShow.md), [EventSubquestPanel_Run](EventSubquestPanel_Run.md), [GUIAddon_OnStateEvent](GUIAddon_OnStateEvent.md), [GUIComponentGauge_Step](GUIComponentGauge_Step.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUIComponent_Disable](GUIComponent_Disable.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_OnClick](GUIComponent_OnClick.md), [GUIComponent_OnDown](GUIComponent_OnDown.md), [GUIComponent_OnFocusGained](GUIComponent_OnFocusGained.md), [GUIComponent_OnFocusLost](GUIComponent_OnFocusLost.md), [GUIComponent_OnUp](GUIComponent_OnUp.md), [GUIList_SetCount](GUIList_SetCount.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [GUINode_PlayCursorOutState](GUINode_PlayCursorOutState.md), [GUINode_PlayCursorOverState](GUINode_PlayCursorOverState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUINode_PlayStateAtFrameEx](GUINode_PlayStateAtFrameEx.md), [GUINode_SetCursorOverState](GUINode_SetCursorOverState.md), [GUINode_StopState](GUINode_StopState.md), [GUIWidget_Tick](GUIWidget_Tick.md), [GuideWindow_ShowPage](GuideWindow_ShowPage.md), [JobChange_RunPreviewAnim](JobChange_RunPreviewAnim.md), [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md), [Launcher_DrawControlsPage](Launcher_DrawControlsPage.md), [Launcher_DrawInfoPage](Launcher_DrawInfoPage.md), [MainTab_SelectTab](MainTab_SelectTab.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [SaveLoadList_Refresh](SaveLoadList_Refresh.md), [ShopItemList_DrawRow](ShopItemList_DrawRow.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](SortieScreen_SetArea1Face.md), [SortieScreen_ShowAreaBoxes](SortieScreen_ShowAreaBoxes.md), [TabBar_Select](TabBar_Select.md), [TabBar_SetTable](TabBar_SetTable.md), [UIAddonFingerCursor_PlayDefault](UIAddonFingerCursor_PlayDefault.md), [UIAddonFingerCursor_PlayLoop](UIAddonFingerCursor_PlayLoop.md), [UIAddonFingerCursor_ResetPose](UIAddonFingerCursor_ResetPose.md), [UIAddonFingerCursor_SetPose](UIAddonFingerCursor_SetPose.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [WorldMapBaseList_SelectTab](WorldMapBaseList_SelectTab.md), [WorldMapNode_PlayTexChange](WorldMapNode_PlayTexChange.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [sub_1400F6148](sub_1400F6148.md), [sub_140107914](sub_140107914.md), [sub_14013DD70](sub_14013DD70.md), [sub_14013F71C](sub_14013F71C.md), [sub_1401D1E70](sub_1401D1E70.md), [sub_1402083B4](sub_1402083B4.md), [sub_1402A9C4C](sub_1402A9C4C.md), [sub_1402A9D5C](sub_1402A9D5C.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

The set-state idiom: FindState(node,key); state+104 = 1; GUINode_PlayState(state).

## Open questions

None recorded.
