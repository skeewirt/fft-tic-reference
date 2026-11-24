# GUITabButton_Deselect

- **Address:** `0x14040B128`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITabButton_Deselect(int64_t tab, unsigned __int8 instant)`
- **Callers:** GUITabButton_Select, WorldMapBaseList_SelectTab
- **Callees:** GUINode_FindNthPartByKind, GUINode_StopState, GUINode_PlayStateAtFrame, GUIWidget_FindRefNodeForComponent, GUIWidget_FindComponentById, Str_Format, UIName_Key, UIName_ReleaseKey, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Deselects a tab label component.

## Behavior

- V: only when +648 is set: turns the first kind-13 part's byte +144 back on, clears +648, plays the unselected state, plays '<name>Deactive' after stopping '<name>Active' on its own component, and posts an owner event.

## State touched

- Calls: [GUINode_FindNthPartByKind](GUINode_FindNthPartByKind.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIWidget_FindRefNodeForComponent](GUIWidget_FindRefNodeForComponent.md), [GUIWidget_FindComponentById](GUIWidget_FindComponentById.md), [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)

## Referenced by

- Called by: [GUITabButton_Select](GUITabButton_Select.md), [WorldMapBaseList_SelectTab](WorldMapBaseList_SelectTab.md)

## Open questions

None recorded.
