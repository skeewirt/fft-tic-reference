# GUILayer_BoundsToRect

- **Address:** `0x1403DF8D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUILayer_BoundsToRect(UIRenderer *r, int rect[4])`
- **Callers:** GUILayer_Flush
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts the double-precision draw bounds accumulated in the renderer (r+152..+176) into the integer rectangle {left, top, right, bottom} of the draws since the last flush.

## Behavior

- V: left = (int)clamp(r+152), top = (int)clamp(r+160), right = (int)clamp(r[+168] + 1.0 - DBL_MIN), bottom = (int)clamp(r[+176] + 1.0 - DBL_MIN); clamp = [-2147483648, 2147483647]; the casts are truncating (cvttsd2si). The - DBL_MIN is below double resolution, so right = trunc(maxX + 1) and bottom = trunc(maxY + 1).
- I: for non-negative coordinates this is floor(min) for the left / top edge and floor(max) + 1 for the right / bottom edge (an exact integer maximum still grows by one pixel).

## Referenced by

- Called by: [GUILayer_Flush](GUILayer_Flush.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The name is ours (IDB: sub_1403DF8D8). The four doubles are filled by UIRender_AccumulateQuadBounds (sub_1403DF71C): +152 min x, +160 min y, +168 max x, +176 max y over the four transformed corners of every quad.

## Open questions

None recorded.
