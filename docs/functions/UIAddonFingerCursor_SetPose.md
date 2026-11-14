# UIAddonFingerCursor_SetPose

- **Address:** `0x1401D35AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_SetPose(UIAddonFingerCursor *addon, int pose)`
- **Callers:** sub_14011A20C (job-change screen events), sub_1402ACE98
- **Callees:** UIAddonFingerCursor_FreezePose, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives the glove one of its poses: stops the bob and plays the pose's state on the Hand component.

## Behavior

- V: with the Hand component (addon+48) present: UIAddonFingerCursor_FreezePose(addon), then the state named by pose on addon+48: 0 Default, 1 Grab, 2 Vertical (any other value looks up an empty name): +104 = 1, GUINode_PlayState.
- V: pose 2 also plays state VerticalLoop the same way.

## State touched

- Calls: [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [UIAddonFingerCursor.hand_component](../structs/UIAddonFingerCursor.md#hand_component)

## Notes

The name is ours (IDB: sub_1401D35AC). The pose states are on the Hand component, the Loop on the main component.

## Open questions

None recorded.
