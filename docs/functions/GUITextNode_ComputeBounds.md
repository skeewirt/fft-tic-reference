# GUITextNode_ComputeBounds

- **Address:** `0x1403DEE64`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_ComputeBounds(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_AlignVertical (its tail call)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes the integer bounding box of the laid-out text (all glyphs and line extents) and stores it at layout+104..116.

## Behavior

- V (empty): when the glyph vector (+8 / +16) and the line vector (+40 / +48) are both empty, layout+104, +108, +112, +116 are set to 0.
- V (glyph extents): size = (float)(int16 node+304) with node = *st. Start xmin = ymin = +2^31, xmax = ymax = -2^31 (floats). For every glyph record (36 bytes): gx = line[rec+24].x + rec.x, gy = line[rec+24].y + rec.y (line records are 24 bytes: +0 x, +4 y); xmin = min(xmin, gx); ymin = min(ymin, gy); xmax = max(xmax, gx + rec.width (+8)); ymax = max(ymax, size * rec.f (+12) + gy). The glyph height is the node's size times the glyph multiplier, not a font metric.
- V (line extents): for every line record, xmin = min(xmin, line.x (+0)) and xmax = max(xmax, line.x + line.width (+8)). So a right- / centre-aligned or justified line widens the box to the line extent even when its glyphs are narrower, and a left-aligned line (x = 0) forces xmin <= 0.
- V (store): layout+104 = (int)(floor(xmin) + 0.5), +108 = (int)(floor(ymin) + 0.5), +112 = (int)(ceil(xmax) + 0.5), +116 = (int)(ceil(ymax) + 0.5); each value is first clamped to 2147483647. The conversion is a C truncation toward zero, so for non-negative values it is floor / ceil and for a negative value the +0.5 makes the result one larger (floor(-2.3) + 0.5 = -2.5 gives -2).
- V (reject): if left >= right or top >= bottom (checked after truncation) all four are set to 0.
- V: the return value is not meaningful as a result (the last int stored, or a stale pointer in the empty case); the only caller returns it and GUITextNode_Layout ignores it.

## Notes

The name is ours (IDB: sub_1403DEE64). Layout+104..116 are read after layout by sub_1403DCE74 (GUITextNode_Layout's follow-up, not traced). The bounds include icon records too (they are ordinary glyph records, width size * f).

## Open questions

? the consumer of the bounds (sub_1403DCE74 and the draw path). ? whether the float or double path is used for the +0.5 (the values involved are exact in both for |v| < 2^24).
