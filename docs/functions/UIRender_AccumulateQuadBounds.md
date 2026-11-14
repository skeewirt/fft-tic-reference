# UIRender_AccumulateQuadBounds

- **Address:** `0x1403DF71C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIRender_AccumulateQuadBounds(UIRenderer *r, const float quad[8])`
- **Callers:** UIDraw_QuadTransformed, sub_1403DF9E0, sub_1403DFE34, sub_1403E00AC, sub_1403E0824 (the quad emitters)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Grows the renderer's running screen bounding box with the four transformed corners of a quad just queued.

## Behavior

- V: quad = four (x, y) float pairs. minX = min of the four x, minY = min of the four y, maxX, maxY likewise; the renderer's doubles r+152 (min x), r+160 (min y) are lowered, r+168 (max x), r+176 (max y) raised: r+152 = min(r+152, minX), r+160 = min(r+160, minY), r+168 = max(r+168, maxX), r+176 = max(r+176, maxY) (float values converted to double).
- I: r+152..+176 is the damage / layer rectangle in layout pixels that a layer or effect pass uses to limit its work.

## Referenced by

- Called by: [GUIQuad_EmitGouraud](GUIQuad_EmitGouraud.md), [UIDraw_QuadTransformed](UIDraw_QuadTransformed.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The name is ours (IDB: sub_1403DF71C). 9502 hits per 4 s on the Job Tree: one per emitted quad. It does not affect pixels itself.

## Open questions

Who reads r+152..+176 and when it is reset.
