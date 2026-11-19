# Launcher_DrawControlsPage

- **Address:** `0x1401BB9D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Launcher_DrawControlsPage(void *launcher)`
- **Callers:** sub_1401BB5EC
- **Callees:** UIName_Key, GUINode_ApplyStateAtFrame, UIName_ReleaseKey, GUINode_StopState, GUINode_PlayStateAtFrame, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Switches the launcher guide to its controls panel.

## Behavior

- V: hides the info panel (+536) and shows the controls panel (+544), then continues into Launcher_FillControls.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Notes

Name is ours. The hand-over to Launcher_FillControls (sub_1401BBB30) is a tail jump, not a call.

## Open questions

None recorded.
