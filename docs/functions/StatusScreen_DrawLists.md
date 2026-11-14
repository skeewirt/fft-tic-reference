# StatusScreen_DrawLists

- **Address:** `0x140112B48`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 StatusScreen_DrawLists(int64 screen)`
- **Callers:** sub_140112A04
- **Callees:** sub_1400F5828, UIName_Key, GUINode_FindPartByName, UIName_ReleaseKey, GUINode_FindDescendant, sub_1400F56D8, GUIComponentList_GetSlotComponent, sub_140112E84, sub_140113388, GUIWidget_FindFirstKind1Component2, GUINode_StopState, GUINode_PlayStateAtFrame, GUIComponentList_GetItemComponent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the Status screen's status list: one list item per gain, then per ailment, and the caption of the first.

## Behavior

- V: finds the parts ListStatus and ListItem of the screen's widget, sizes the component list to the two counts together, and fills slot k with StatusScreen_SetEntry for the k-th gain, then the ailments after them.
- V: selects entry 0 when there is any (+0x190) and shows its caption with StatusScreen_SetCaption (-1 when the lists are empty).
- V: plays the ShowNone / HideNone state of the StatusCondition node (the "none" text when both lists are empty).

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUIComponentList_GetSlotComponent](GUIComponentList_GetSlotComponent.md), [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours.

## Open questions

None recorded.
