# GUIComponentList_GetVScroll

- **Address:** `0x14040C080`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIComponentScrollBar *GUIComponentList_GetVScroll(GUIComponentList *list)`
- **Callers:** GUIComponentList_SetScrollY (0x14040C92C), GUIComponentList_UpdateScrollBars, and 13 list-user addon methods (sub_1400F56D8, sub_140112748, sub_140153874, sub_14028C5C4, ...)
- **Callees:** GUINode_FindPartByName, GUIWidget_FindComponentCached

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the list's vertical scroll bar component (the 'VScroll' child reference node), or null.

## Behavior

- V: part = GUINode_FindPartByName(list+272, key +5048 = 'VScroll'); it must be a reference node (kind +52 == 12); component = GUIWidget_FindComponentCached(list+496, part+208, part+224, part+304); the component must have kind (+536) 8 (ScrollBar), else null.

## State touched

- Calls: [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentList_SetScrollY](GUIComponentList_SetScrollY.md), [GUIComponentList_UpdateScrollBars](GUIComponentList_UpdateScrollBars.md), [ListScroll_HandleStick](ListScroll_HandleStick.md)

## Notes

The name is ours (IDB: sub_14040C080). 'List' is I: the function reads fields of a kind-9 style component (item count +648, columns +652); the ctor of kind 9 is the one that class has, the users were not each verified.

## Open questions

None recorded.
