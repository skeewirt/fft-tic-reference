# Launcher_DrawStartPage

- **Address:** `0x1401BBDD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Launcher_DrawStartPage(void *launcher, const void *row)`
- **Callers:** sub_1401BB5EC
- **Callees:** UIName_Key, GUINode_ApplyStateAtFrame, UIName_ReleaseKey, GUINode_FindPartByName, NxdEntry_GetRow, GUITextNode_SetTextExpandedTemp, UIGadgetFFTOVScrollText_Refit, GUINode_FindGadgetPart, GUICore_FocusNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the guide page that carries the Start button.

## Behavior

- V: plays the 'Start' state on node +520, puts the caption (+8) into the scrolling text and refits it, sets the gadget parts 'ButtonStart' and 'Title' to UI text 2214 and focuses the node at +560.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [UIGadgetFFTOVScrollText_Refit](UIGadgetFFTOVScrollText_Refit.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [GUICore_FocusNode](GUICore_FocusNode.md)

## Notes

Name is ours.

## Open questions

None recorded.
