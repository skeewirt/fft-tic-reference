# GUITabButton_Select

- **Address:** `0x14040AEE8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITabButton_Select(int64_t tab, unsigned __int8 instant)`
- **Callers:** WorldMapBaseList_SelectTab and other tab bars
- **Callees:** GUIOwners_PostEvent, GUINode_FindNthPartByKind, GUINode_StopState, GUINode_PlayStateAtFrame, GUIWidget_FindRefNodeForComponent, GUIWidget_FindComponentCached, GUITabButton_Deselect, GUIWidget_FindComponentById, Str_Format, UIName_Key, UIName_ReleaseKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects a tab label component and deselects every sibling tab label under the same parent node.

## Behavior

- V: does nothing when the selected byte +648 is already set; posts an owner event first and stops when an owner vetoes it.
- V: turns off the first kind-13 part's byte +144, sets +648, plays the selected state (instant when the flag is set).
- V: walks the sibling reference nodes (kind 12) of its own reference node and calls GUITabButton_Deselect on each one whose component is a tab label (kind 6).
- V: on its own component plays '<name>Active' after stopping '<name>Deactive', then posts a second owner event.

## State touched

- Calls: [GUIOwners_PostEvent](GUIOwners_PostEvent.md), [GUINode_FindNthPartByKind](GUINode_FindNthPartByKind.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIWidget_FindRefNodeForComponent](GUIWidget_FindRefNodeForComponent.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUITabButton_Deselect](GUITabButton_Deselect.md), [GUIWidget_FindComponentById](GUIWidget_FindComponentById.md), [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md), [UIName_ReleaseKey](UIName_ReleaseKey.md)

## Referenced by

- Called by: [WorldMapBaseList_SelectTab](WorldMapBaseList_SelectTab.md)

## Open questions

None recorded.
