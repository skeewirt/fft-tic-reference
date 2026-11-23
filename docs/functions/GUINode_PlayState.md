# GUINode_PlayState

- **Address:** `0x1404000D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_PlayState(NodeState *state)`
- **Callers:** JobTree_Set*State, JobTree_SetPanelRecord, GUINode_PlayStateAtFrame, GUINode_PlayStateAtFrameEx, GUIAddon_OnStateEvent, UIAddonFingerCursor_PlayLoop, the finger cursor pose functions
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a state: resets its time, sets the running flags (+105/+106) and the 60 fps frame time.

## Behavior

- V: byte +107 (paused) is read and cleared. When it was set, nothing else happens: a paused state keeps its clock and only the pause is lifted.
- V: otherwise time +76 = 0, frame +80 = 0, previous frame +84 = 0, +105 = 1 (running), +106 = 1 (dirty / restarted), +110 = 0 (hold). When the loop range start +92 is below its end +96, the frame is then set to (float)+92 and the time to +92 / 60.0 (the state starts inside its range).
- V: it does not touch +104 (enabled), +108 (loop) or +72 (rate): callers set +104 = 1 first, and UIAddonFingerCursor_PlayLoop sets +108 = 1.
- V: nothing is applied to the nodes here.
- I: the first application happens in the next component update, after GUINodeState_Advance has moved the frame by one tick, so the first applied frame is about 1 (one tick of 60 fps frames), not 0.
- V: sets the state's +105 / +106 to 1 (running), time 0 (or the start frame / 60 when +92 < +96).

## State touched

- Reads: [GUINodeState.paused](../structs/GUINodeState.md#paused), [GUINodeState.range_start](../structs/GUINodeState.md#range_start), [GUINodeState.range_end](../structs/GUINodeState.md#range_end)
- Writes: [GUINodeState.paused](../structs/GUINodeState.md#paused), [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.prev_frame](../structs/GUINodeState.md#prev_frame), [GUINodeState.running](../structs/GUINodeState.md#running), [GUINodeState.dirty](../structs/GUINodeState.md#dirty), [GUINodeState.hold](../structs/GUINodeState.md#hold)

## Referenced by

- Called by: [Battle_InitScene](Battle_InitScene.md), [BgmMode_DrawRow](BgmMode_DrawRow.md), [BookShelf_Fill](BookShelf_Fill.md), [ChronicleTimeline_LayoutChapters](ChronicleTimeline_LayoutChapters.md), [ClassicSubtitles_SetState](ClassicSubtitles_SetState.md), [ErrorBanner_Show](ErrorBanner_Show.md), [EventEndSlate_ShowTask](EventEndSlate_ShowTask.md), [EventNode_PlayShow](EventNode_PlayShow.md), [GUIAddon_OnStateEvent](GUIAddon_OnStateEvent.md), [GUIComponent_Disable](GUIComponent_Disable.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_OnClick](GUIComponent_OnClick.md), [GUIComponent_OnDown](GUIComponent_OnDown.md), [GUIComponent_OnFocusGained](GUIComponent_OnFocusGained.md), [GUIComponent_OnFocusLost](GUIComponent_OnFocusLost.md), [GUIComponent_OnUp](GUIComponent_OnUp.md), [GUIList_SetCount](GUIList_SetCount.md), [GUINode_PlayCursorOutState](GUINode_PlayCursorOutState.md), [GUINode_PlayCursorOverState](GUINode_PlayCursorOverState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUINode_PlayStateAtFrameEx](GUINode_PlayStateAtFrameEx.md), [GUINode_SetCursorOverState](GUINode_SetCursorOverState.md), [GlossaryDetail_Fill](GlossaryDetail_Fill.md), [GlossaryList_DrawRow](GlossaryList_DrawRow.md), [GuideWindow_ShowPage](GuideWindow_ShowPage.md), [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md), [JournalDetail_Fill](JournalDetail_Fill.md), [JournalList_DrawRow](JournalList_DrawRow.md), [Launcher_DrawControlsPage](Launcher_DrawControlsPage.md), [Launcher_DrawInfoPage](Launcher_DrawInfoPage.md), [MainTab_SelectTab](MainTab_SelectTab.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [SaveLoadList_Refresh](SaveLoadList_Refresh.md), [ShopItemList_DrawRow](ShopItemList_DrawRow.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](SortieScreen_SetArea1Face.md), [SortieScreen_ShowAreaBoxes](SortieScreen_ShowAreaBoxes.md), [TabBar_Select](TabBar_Select.md), [TabBar_SetTable](TabBar_SetTable.md), [UIAddonFingerCursor_PlayDefault](UIAddonFingerCursor_PlayDefault.md), [UIAddonFingerCursor_PlayLoop](UIAddonFingerCursor_PlayLoop.md), [UIAddonFingerCursor_ResetPose](UIAddonFingerCursor_ResetPose.md), [UIAddonFingerCursor_SetPose](UIAddonFingerCursor_SetPose.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [WorldMapLocationPanel_Fill](WorldMapLocationPanel_Fill.md), [WorldMapNode_PlayTexChange](WorldMapNode_PlayTexChange.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md), [WorldMapRoute_Refresh](WorldMapRoute_Refresh.md), [WorldMapRoute_SetGrey](WorldMapRoute_SetGrey.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [sub_140107914](sub_140107914.md), [sub_14013DD70](sub_14013DD70.md), [sub_14013F71C](sub_14013F71C.md), [sub_14016FFC8](sub_14016FFC8.md), [sub_1402083B4](sub_1402083B4.md), [sub_1402A9C4C](sub_1402A9C4C.md), [sub_1402A9D5C](sub_1402A9D5C.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

State fields: struct GUINodeState.

## Open questions

None recorded.
