# SDFFontRenderer_AccumulateBounds

- **Address:** `0x1403A9248`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SDFFontRenderer_AccumulateBounds(SDFFontRenderer *r, float *quad)`
- **Callers:** SDFFontRenderer_EmitGlyph (0x1403A99CA, after storing the 4 vertices and before the quad count is incremented)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Grows the current batch's 2D bounding box (r+7928..7940) by the four vertices of the quad that SDFFontRenderer_EmitGlyph just wrote.

## Behavior

- V: quad is the first of four 48-byte vertices (12 floats each; x at index 0, y at 1 of each); it reads x / y of vertex 0, 1, 2, 3 (quad[0,1], [12,13], [24,25], [36,37]) and takes the min and max of x and of y.
- V: if the box is not initialised (max x r[1984] = r+7936 is not > 0) it stores minX, minY, maxX, maxY into r+7928 / +7932 / +7936 / +7940 (floats r[1982..1985]); else it replaces each stored value by the min of the mins and the max of the maxes.
- V: quirk: initialisation is tested by 'maxX > 0', not by a flag, so a batch whose glyphs all lie entirely at x <= 0 is overwritten again by every glyph (box = the last glyph) rather than grown.

## Referenced by

- Called by: [SDFFontRenderer_EmitGlyph](SDFFontRenderer_EmitGlyph.md)

## Notes

The name is ours (IDB: sub_1403A9248). Operates on the vertex positions in the renderer's pen space (pen * r+9544 / +9548); Flush divides by those factors. The positions include the italic shear and the rotation (r+9536), so the box is the true quad extent. Nothing is rounded.

## Open questions

? the consumer of the per-batch box on the GPU side.
