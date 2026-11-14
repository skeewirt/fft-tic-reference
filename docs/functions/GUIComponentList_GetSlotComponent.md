# GUIComponentList_GetSlotComponent

- **Address:** `0x14040C228`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIComponentList_GetSlotComponent(GUIComponentList *list, int slot)`
- **Callers:** GUIComponentList_GetItemComponent and about 14 list-user addon methods (sub_1400F58A4, sub_1400F5974, sub_1400F6700, ...)
- **Callees:** GUIComponentList_FindSlotNode, GUIWidget_FindComponentCached

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The component (a ListItem) behind a slot node: the slot node must be a reference node (kind 12).

## Behavior

- V: node = GUIComponentList_FindSlotNode(list, slot); when node != 0 and node+52 == 12 returns GUIWidget_FindComponentCached(list+496, node+208, node+224, node+304), else 0.

## State touched

- Calls: [GUIComponentList_FindSlotNode](GUIComponentList_FindSlotNode.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md)

## Referenced by

- Called by: [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md), [GUIList_SetCount](GUIList_SetCount.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md)

## Notes

The name is ours (IDB: sub_14040C228).

## Open questions

None recorded.
