# Launcher_DrawInfoPage

- **Address:** `0x1401BB77C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Launcher_DrawInfoPage(void *launcher, const void *row)`
- **Callers:** sub_1401BB5EC
- **Callees:** UIName_Key, GUINode_ApplyStateAtFrame, GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUINode_FindGadgetPart, NxdEntry_GetRow, GUITextNode_SetTextExpandedTemp, UIGadgetFFTOVScrollText_Refit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws an information page of the launcher's guide.

## Behavior

- V: plays the 'Info' state, puts the caption into the info text and shows the picture with GuiImage_SetIconById(+624, the row's icon (+4)).

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [UIGadgetFFTOVScrollText_Refit](UIGadgetFFTOVScrollText_Refit.md)

## Notes

Name is ours.

## Open questions

None recorded.
