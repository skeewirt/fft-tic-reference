# GUIComponentList_SetScrollY

- **Address:** `0x14040C92C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponentList_SetScrollY(GUIComponentList *list, int y, char snap, char clamp)`
- **Callers:** sub_140112748, sub_140153874, sub_14028D7BC, sub_14028D8F4, sub_14028DAEC, sub_14028E720, sub_14040C7D8
- **Callees:** GUIComponentList_GetVScroll, ScrollBar_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vertical twin of GUIComponentList_SetScrollX: via the 'VScroll' bar, stores list+680 and sets the layout-dirty byte +685.

## Behavior

- V: bar = GUIComponentList_GetVScroll(list); when present ScrollBar_SetPosition(bar, y, snap, clamp), y = (int)roundf(bar+672); list+680 = y; list+685 = 1.

## State touched

- Calls: [GUIComponentList_GetVScroll](GUIComponentList_GetVScroll.md), [ScrollBar_SetPosition](ScrollBar_SetPosition.md)

## Referenced by

- Called by: [ListScroll_Step](ListScroll_Step.md)

## Notes

The name is ours (IDB: sub_14040C92C). This is the call the job-change / ability list code makes when it scrolls a list (see ScrollBar_SetPosition's notes).

## Open questions

None recorded.
