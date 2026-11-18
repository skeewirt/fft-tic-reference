# GUINode_SetPosition

- **Address:** `0x1403EF684`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_SetPosition(GUINode *node, int x, int y)`
- **Callers:** GUINode_ApplyAnimChannels (track a[6]), GUICursorHand_StepToward, GUICursorHand_Update
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a node's integer position; the track sampler, the finger cursor's glide and the smooth-scroll animation all use it.

## Behavior

- V: the arguments are integers (the earlier prototype with floats was wrong): when x or y differs from the stored pair, both are written to node+56 / +60 and the dirty byte +149 is set; when the low two bits of node+140 (the pin layout flags) are set, the cached pin result at +116 / +120 is reset to FLT_MAX.
- V: so every animated or glided node position is an integer; fractions never reach the matrices through the position.

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md), [JobScreenFrame](../flows/JobScreenFrame.md)
- Called by: [CharaRender_PlaceSlotImage](CharaRender_PlaceSlotImage.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUICursorHand_StepToward](GUICursorHand_StepToward.md), [GUICursorHand_Update](GUICursorHand_Update.md), [GUINode_ApplyAnimChannels](GUINode_ApplyAnimChannels.md), [GUINode_BuildFromFile](GUINode_BuildFromFile.md), [GUITextBoardComponent_Update](GUITextBoardComponent_Update.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md), [UIGadgetFFTOVScrollText_ApplyScroll](UIGadgetFFTOVScrollText_ApplyScroll.md), [UIPosFollow_Snap](UIPosFollow_Snap.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md), [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

V (live): called on the Job Tree widget's root node (no parent) it moves every panel, arrow, label, the floor and the title together.

## Open questions

None recorded.
