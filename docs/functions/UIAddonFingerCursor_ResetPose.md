# UIAddonFingerCursor_ResetPose

- **Address:** `0x1401D3694`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_ResetPose(UIAddonFingerCursor *addon, int pose)`
- **Callers:** sub_14011A20C (job-change screen events), sub_1402ACE98
- **Callees:** GUINode_StopState, GUINode_PlayStateAtFrame, GUINode_FindState, GUINode_PlayState, UIAddonFingerCursor_PlayLoop

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes the glove out of a pose, back to Default, and restarts the bob.

## Behavior

- V: with the Hand component (addon+48) present: GUINode_StopState on the pose's state (0 Default, 1 Grab, 2 Vertical); for pose 2 also VerticalLoop is played to its last frame and stopped.
- V: then state Default of addon+48 is played (+104 = 1, GUINode_PlayState) and UIAddonFingerCursor_PlayLoop(addon) restarts the bob from frame 0.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [UIAddonFingerCursor_PlayLoop](UIAddonFingerCursor_PlayLoop.md)
- Reads: [UIAddonFingerCursor.hand_component](../structs/UIAddonFingerCursor.md#hand_component)

## Notes

The name is ours (IDB: sub_1401D3694).

## Open questions

None recorded.
