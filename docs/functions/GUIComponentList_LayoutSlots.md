# GUIComponentList_LayoutSlots

- **Address:** `0x14040CB60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentList_LayoutSlots(GUIComponentList *list)`
- **Callers:** sub_140160BE0, sub_140161A28, sub_1401A1AE4, sub_14028D7BC, sub_14028D870, sub_14028D8F4, sub_14028DAEC, sub_1402A48E8, sub_14040CFF4
- **Callees:** GUIComponentList_FindSlotNode, GUINode_SetPosition, GUIWidget_FindComponentCached, GUICore_IsFocusTarget, GUICore_SetFocusComponent, GUICore_IsCursorTarget, GUICore_SetCursorTarget, GUINode_StopState, GUINode_PlayStateAtFrame, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Places the recycled slot nodes of a list for the current scroll offset, re-binds slots that now show a different item (resetting their visuals and clearing focus / cursor on them) and posts event 31.

## Behavior

- V: C = list+652 columns, cell w = +688, cell h = +692, scroll x +676, scroll y +680, origin x +704, origin y +708, node size +336 / +340 (the clip test below), slot grid +660 columns x +664 rows, item count +648. firstCol = -((+704 - +676) / w), firstRow = -((+708 - +680) / h) (C truncating division). list+668 (first shown item) = C * firstRow + firstCol; the old value is kept for the rebind test.
- V: for each row r = firstRow .. firstRow + slotRows - 1 and column c = 0..slotCols-1: item = firstCol + c + C * r; slot = ((c + firstCol) % slotCols) + slotCols * (r % slotRows); node = GUIComponentList_FindSlotNode(list, slot). A missing node is skipped.
- V: cell position x = (item % C) * w - scrollX; y = (item / C) * h - scrollY; the node's visible byte (node+144) = item < count && -w < x + origin x < +336 && -h < y + origin y < +340; GUINode_SetPosition(node, x, y).
- V (re-bind): when the node is a reference node whose component has kind 10 (ListItem), the list's first shown item changed (+668 != previous) and the component's item index (+648) differs from `item`: if the component is the GUI focus target (GUICore_IsFocusTarget) the focus is cleared (GUICore_SetFocusComponent(core, 0, 0)); if it is the cursor target, GUICore_SetCursorTarget(core, 0, 0); component+652 = 0; states are reset with StopState + PlayStateAtFrame(-1, last frame): Active (+4936) -> Deactive (+4952), CursorOver (+4696) -> CursorOut (+4712), FocusIn (+4664) -> FocusOut (+4680); component+648 = item; when item < count event {30, item} is posted to the list's owners (list+584).
- V: at the end list+685 = 0 and event {31} is posted.

## State touched

- Calls: [GUIComponentList_FindSlotNode](GUIComponentList_FindSlotNode.md), [GUINode_SetPosition](GUINode_SetPosition.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUICore_IsFocusTarget](GUICore_IsFocusTarget.md), [GUICore_SetFocusComponent](GUICore_SetFocusComponent.md), [GUICore_IsCursorTarget](GUICore_IsCursorTarget.md), [GUICore_SetCursorTarget](GUICore_SetCursorTarget.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md), [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_14040CB60). Takeaway for hover / focus on a list: slots are recycled; when the scroll moves a slot to a new item, its focus, cursor and Active / CursorOver / FocusIn states are forced back to the idle pose in the same frame. A model of hover that keys on a slot node (not on the item) will see the highlight jump.

## Open questions

? the meaning of component +652.
