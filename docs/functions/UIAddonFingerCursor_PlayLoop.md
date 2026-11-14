# UIAddonFingerCursor_PlayLoop

- **Address:** `0x1401D3148`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_PlayLoop(UIAddonFingerCursor *addon)`
- **Callers:** UIAgentCursor_Show, UIAddonFingerCursor_ResetPose
- **Callees:** GUIWidget_FindFirstKind1Component2, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

(Re)starts the idle bob of the finger cursor: shows the cursor widget and plays the Loop state of its main component from frame 0 with looping switched on.

## Behavior

- V: sub_1401D1E30(addon, 0) first (GUIWidget_Show of the widget at addon+24).
- V: comp = GUIWidget_FindFirstKind1Component2(addon+24), the widget's main component (the file's Widget component, which owns the Loop state with the link to the Hand's Loop); with none the function ends here.
- V: state Loop of comp: byte +108 (loop) = 1 (set by this code; the file stores 0), +104 = 1, GUINode_PlayState: time, frame and previous frame = 0, running and dirty flags set.
- V: GUINode_PlayState only clears the pause flag when the state is paused, so a paused Loop would not restart; nothing in the code read sets +107 on the main component's Loop (the Hand's Loop is the one that is paused, by the link).
- V (data): the main component of ffto_finger_cursor.uib is Widget: 1920 x 1080, one Reference node CursorRef (to component Hand of ffto_common_cursor.uib), states HomePosition, Show, Hide and Loop; Loop is 40 frames with one state-link track (frames 0 to 40) to state Loop of CursorRef.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [UIAddonFingerCursor.widget](../structs/UIAddonFingerCursor.md#widget)
- Writes: [GUINodeState.loop](../structs/GUINodeState.md#loop), [GUINodeState.enabled](../structs/GUINodeState.md#enabled)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [UIAddonFingerCursor_ResetPose](UIAddonFingerCursor_ResetPose.md), [UIAgentCursor_Show](UIAgentCursor_Show.md)
- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)

## Notes

The name is ours (IDB: sub_1401D3148). This is the clock of the glove's bob: the Hand component's own Loop state is only scrubbed by it (flow CursorGloveFrame).

## Open questions

None recorded.
