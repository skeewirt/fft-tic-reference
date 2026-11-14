# GUIComponentList_IsItemVisible

- **Address:** `0x14040C2FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUIComponentList_IsItemVisible(GUIComponentList *list, int item)`
- **Callers:** sub_14028E720, sub_14028E850, sub_14028F320 (list cursor movement code)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the item's cell lies inside the list's viewport with at most half a cell cut off at each edge.

## Behavior

- V: C = list+652 (columns), cell w = list+688, cell h = list+692, scroll x = list+676, scroll y = list+680, viewport w = list+696, h = list+700. x = (item % C) * w - scrollX; y = (item / C) * h - scrollY.
- V: returns -w/2 <= x && x + w/2 <= viewportW && -h/2 <= y && y + h/2 <= viewportH (integer halves, C truncating division).

## Referenced by

- Called by: [ListScroll_Step](ListScroll_Step.md)

## Notes

The name is ours (IDB: sub_14040C2FC). 'At least half visible' decides whether the cursor can sit on an item without scrolling.

## Open questions

None recorded.
