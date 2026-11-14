# GUIComponentList_GetItemComponent

- **Address:** `0x14040C270`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponent *GUIComponentList_GetItemComponent(GUIComponentList *list, int item)`
- **Callers:** about 90 call sites in the UI addons (the most used list accessor)
- **Callees:** GUIComponentList_ItemToSlot, GUIComponentList_GetSlotComponent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The component currently showing item `item`, or null when that item is not in the shown window.

## Behavior

- V: slot = GUIComponentList_ItemToSlot(list, item); slot < 0 returns 0; otherwise GUIComponentList_GetSlotComponent(list, slot).

## State touched

- Calls: [GUIComponentList_ItemToSlot](GUIComponentList_ItemToSlot.md), [GUIComponentList_GetSlotComponent](GUIComponentList_GetSlotComponent.md)

## Referenced by

- Called by: [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [sub_14022F868](sub_14022F868.md), [sub_140338060](sub_140338060.md)

## Notes

The name is ours (IDB: sub_14040C270).

## Open questions

None recorded.
