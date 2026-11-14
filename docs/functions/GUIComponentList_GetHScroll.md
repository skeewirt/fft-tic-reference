# GUIComponentList_GetHScroll

- **Address:** `0x14040C0EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponentScrollBar *GUIComponentList_GetHScroll(GUIComponentList *list)`
- **Callers:** GUIComponentList_SetScrollX (0x14040C8B0), GUIComponentList_UpdateScrollBars and 11 list-user addon methods
- **Callees:** GUINode_FindPartByName, GUIWidget_FindComponentCached

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same as GUIComponentList_GetVScroll for the horizontal bar (key +5064 = 'HScroll').

## Behavior

- V: identical to GUIComponentList_GetVScroll apart from the name key (+5064).

## State touched

- Calls: [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentList_SetScrollX](GUIComponentList_SetScrollX.md), [GUIComponentList_UpdateScrollBars](GUIComponentList_UpdateScrollBars.md), [ListScroll_HandleStick](ListScroll_HandleStick.md)

## Notes

The name is ours (IDB: sub_14040C0EC).

## Open questions

None recorded.
