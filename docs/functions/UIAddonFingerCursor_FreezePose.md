# UIAddonFingerCursor_FreezePose

- **Address:** `0x1401D3550`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_FreezePose(UIAddonFingerCursor *addon)`
- **Callers:** UI_FrameUpdate (when agent+132 is set), UIAgentCursor_SetStatic, UIAddonFingerCursor_SetPose
- **Callees:** GUIWidget_FindFirstKind1Component2, GUINode_PlayStateAtFrame, GUIComponent_StopAllStates

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the main component's Loop state to its last frame and then stops every state of that component (the bob ends).

## Behavior

- V: comp = GUIWidget_FindFirstKind1Component2(addon+24); GUINode_PlayStateAtFrame(comp, Loop, -1) (frame = the state's frame count), then GUIComponent_StopAllStates(comp).
- I: the stop clears every enable byte (+104), so no later state application runs for these states; the nodes keep whatever the last application wrote. Whether that is the Loop's last-frame pose was not checked.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md)

## Referenced by

- Called by: [UIAddonFingerCursor_SetPose](UIAddonFingerCursor_SetPose.md), [UIAgentCursor_SetStatic](UIAgentCursor_SetStatic.md), [UI_FrameUpdate](UI_FrameUpdate.md)

## Notes

The name is ours (IDB: sub_1401D3550).

## Open questions

None recorded.
