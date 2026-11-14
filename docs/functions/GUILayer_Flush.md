# GUILayer_Flush

- **Address:** `0x1403E90A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUILayer_Flush(UIRenderer *r)`
- **Callers:** GUILayer_SetCurrent (sub_1403E9218, hence every layer switch), GUICore_CommitFrame
- **Callees:** GUILayer_BoundsToRect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Closes the layer being built: merges the draws recorded so far into the layer's dirty rectangle and advances the layer count.

## Behavior

- V: when r+606592 (the draw counter: +1 per emitted draw, see the node draw functions) > 0 it calls GUILayer_BoundsToRect (sub_1403DF8D8) for the integer rectangle of the quads accumulated since the last flush, resets the double bounds r+152..+176 to their sentinels, and merges the rectangle into the current slot's dirty rectangle at r + 512 * current + 41824 (four ints x0, y0, x1, y1): only when the new rectangle is non-empty (x0 < x1 and y0 < y1); when the slot's rectangle is empty it is replaced, otherwise it becomes the union (min of x0 / y0, max of x1 / y1). Then the counter is cleared and, when the current slot index r+606588 equals the slot count r+606584, the count is incremented.
- V: so a slot is consumed (the next layer opens at the next index) by any draw, also one without a quad (a text node counts before it emits glyphs, the letterbox bars of GUICore_CommitFrame count when they are empty): the live Job Tree frame ends with such an empty slot (count 27, last dirty rectangle (0, 0, 0, 0)); a layer that received no draw at all leaves the count alone and its slot is reused by the next layer.
- V (live 2026-10-30): the dirty rectangle of every used slot grown by the effect pad and 16 pixels (GUILayer_ExpandBounds) reproduced the integer layer rectangle of all 26 used layers of a Job Tree frame.

## State touched

- Calls: [GUILayer_BoundsToRect](GUILayer_BoundsToRect.md)

## Referenced by

- Called by: [GUILayer_SetCurrent](GUILayer_SetCurrent.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Open questions

None recorded.
