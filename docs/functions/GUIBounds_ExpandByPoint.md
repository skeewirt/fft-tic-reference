# GUIBounds_ExpandByPoint

- **Address:** `0x1403DF670`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIBounds_ExpandByPoint(UIRenderer *r, const float p[2])`
- **Callers:** GUICore_DrawOutsideBars, UIImage_DrawTiled, UIAddonSoundVisualizer::CustomDrawNode_vfunc_2, sub_1403DFCF0, sub_1403E153C, sub_1403E1DB0, sub_1403E2278, sub_1403E3134, sub_1403E3BBC, sub_1403E40EC (13 total)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Grows the double-precision draw bounds in the renderer (r+152..+176) to include one float point.

## Behavior

- V: r+152 (min x) = min(r+152, p.x); r+160 (min y) = min(r+160, p.y); r+168 (max x) = max(r+168, p.x); r+176 (max y) = max(r+176, p.y), all as doubles (the float is widened exactly; ties keep the stored value).

## Notes

The name is ours (IDB: sub_1403DF670). 476 hits per 4 s. The four values are what GUILayer_BoundsToRect later clamps and converts to the integer rectangle of a flush; no rounding happens here (rounding is in BoundsToRect).

## Open questions

None recorded.
