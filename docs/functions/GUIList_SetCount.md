# GUIList_SetCount

- **Address:** `0x1402A3230`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIList_SetCount(void *list, int count, int column, char rebuild)`
- **Callers:** sub_14012EF90, sub_1401AAC74, sub_1401AAD50, sub_1401AEEF0, sub_1401AFC20, sub_1401AFDE4, sub_1402A62E4, ShopList_BuildEntries
- **Callees:** GUICore_FocusNode, sub_14028D7BC, sub_14028D870, sub_14040C7D8, UIName_Key, GUINode_StopState, UIName_ReleaseKey, GUINode_FindState, GUINode_PlayState, GUIComponentList_GetSlotComponent, sub_1400F6068, sub_1402A89C0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sizes and refreshes a list gadget: it stores the row count and column, rebinds the name key of the list node, and toggles the empty-list label.

## Behavior

- V: the first argument is the list object; its +0x510 pointer must be non-zero or the function returns at once.
- V: it clears the selected-row word at +0x541 and calls GUICore_FocusNode before any rebuild.
- V: when the rebuild flag is zero it calls the list virtual method at +0x40, stores the count and jumps to the refresh.
- V: when the rebuild flag is set it uses the existing node, releases the old name key and binds a new one through UIName_Key.
- V: the strings ShowNoItem and HideNoItem are the two states of the empty-list label the function toggles.
- V: the row count and column are stored in the list object and the node state is replayed with GUINode_PlayState.
- V: the eight callers are the shop, item and menu list builders, so this is the common list sizer.
- I: the column argument is the number of cells per row, because the same value is written to the gadget layout field.
- ?: what sub_1402A89C0 changes after the count; it runs only on the rebuild path.

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md), [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIComponentList_GetSlotComponent](GUIComponentList_GetSlotComponent.md)

## Notes

Whole function read (573 bytes). The two label strings are the only string operands in the body.

## Open questions

None recorded.
