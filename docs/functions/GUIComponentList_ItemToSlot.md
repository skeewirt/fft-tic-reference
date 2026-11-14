# GUIComponentList_ItemToSlot

- **Address:** `0x14040C158`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIComponentList_ItemToSlot(GUIComponentList *list, int item)`
- **Callers:** GUIComponentList_GetItemComponent
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps an item index to the recycled slot (a 'ListItem#n' node) that currently shows it, or -1 when the item is outside the window of shown items.

## Behavior

- V: columns C = list+652, first shown item F = list+668, slot grid = list+660 (columns) x list+664 (rows). col = item % C; row = item / C; firstCol = F % C; firstRow = F / C.
- V: returns -1 when col < firstCol, col >= firstCol + slotCols, row < firstRow or row >= firstRow + slotRows; otherwise (col % slotCols) + slotCols * (row % slotRows).

## Referenced by

- Called by: [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md)

## Notes

The name is ours (IDB: sub_14040C158). The same modulo mapping is used when the slots are placed (GUIComponentList_LayoutSlots), so a scrolled list reuses the slot nodes round-robin.

## Open questions

None recorded.
