# GUINode_PlayStateAtFrame

- **Address:** `0x140409824`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_PlayStateAtFrame(GUINode *node, NameKey *key, int frame)`
- **Callers:** about 170 call sites: every addon that snaps a state (e.g. GUIWidget_Show / Hide, GUIComponent list slot reset in GUIComponentList_LayoutSlots, JobTree-range addons sub_1401D3550 ...)
- **Callees:** GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the named state and jumps it to a given frame (a negative frame = its last frame).

## Behavior

- V: state = GUINode_FindState(node, key); none = return. state+104 = 1; GUINode_PlayState(state).
- V: f = frame < 0 ? state+88 (frame count) : min(frame, state+88); f = max(f, 0). Then state+84 = state+80 = (float)f, state+76 = (float)f / 60.0 and state+106 = 1 (dirty).

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Called by: [Battle_InitScene](Battle_InitScene.md), [Battle_MenuHidePage](Battle_MenuHidePage.md), [Battle_MenuShowPage](Battle_MenuShowPage.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [GUIWidget_Hide](GUIWidget_Hide.md), [GUIWidget_Show](GUIWidget_Show.md), [Launcher_DrawControlsPage](Launcher_DrawControlsPage.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md), [UIAddonFingerCursor_ResetPose](UIAddonFingerCursor_ResetPose.md), [ZodiacStone_FillDetail](ZodiacStone_FillDetail.md)

## Notes

The name is ours (IDB: sub_140409824). Because GUINode_PlayState leaves the frame alone when the state is paused (+107) this can also scrub a paused state. Calling it with frame -1 right after a StopState is the idiom for 'jump to the end pose of this state' (the resting look).

## Open questions

None recorded.
