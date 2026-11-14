# GUIComponentList_SetScrollX

- **Address:** `0x14040C8B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponentList_SetScrollX(GUIComponentList *list, int x, char snap, char clamp)`
- **Callers:** sub_14028D7BC, sub_14028D8F4, sub_14028DAEC, sub_14028E850, sub_14040C7D8
- **Callees:** GUIComponentList_GetHScroll, ScrollBar_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the list's horizontal scroll offset, through the horizontal bar when there is one, and marks the layout dirty.

## Behavior

- V: bar = GUIComponentList_GetHScroll(list); when it exists ScrollBar_SetPosition(bar, x, snap, clamp) and x = (int)roundf(bar+672) (the bar's current smooth position, so the value is clamped / eased by the bar).
- V: list+676 = x; list+685 = 1 (layout dirty).

## State touched

- Calls: [GUIComponentList_GetHScroll](GUIComponentList_GetHScroll.md), [ScrollBar_SetPosition](ScrollBar_SetPosition.md)

## Notes

The name is ours (IDB: sub_14040C8B0). list+676 is the scroll offset the slot layout reads (x position = column * cell width - list+676).

## Open questions

None recorded.
