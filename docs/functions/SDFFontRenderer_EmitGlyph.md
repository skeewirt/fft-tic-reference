# SDFFontRenderer_EmitGlyph

- **Address:** `0x1403A94C8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SDFFontRenderer_EmitGlyph(SDFFontRenderer *r, unsigned short glyph)`
- **Callers:** GUITextNode_Draw
- **Callees:** SDFFontRenderer_AccumulateBounds, cosf, sinf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Emits the quad of one glyph (position, atlas UV, node alpha, palette index, per-vertex factor g = atlasWidth / 8192) for the SDF text shader, and advances the pen.

## Behavior

- V: does nothing unless r+189 (batch open) is set and the glyph index is non-zero.
- V: run state read from the renderer: pen x / y floats at +9492 / +9496, run scale x / y floats at +9500 / +9504 (SEPARATE x and y scales), colour dword +9508, a dword at +9512 copied into every vertex's w, italic flag byte +9530 with the shear factor float +9524 (zero when the flag is clear), rotation angle float +9536 (radians), palette / font slot dword +9540, vertex buffer pointer +9552, quad count dword +9520. The font object is *(r + 8 * slot + 64).
- V: font object: 32-byte glyph records at *(font + 208) (+8 x offset float, +12 y offset float, +16 advance float, +24 / +26 / +28 / +30 atlas x, y, w, h as u16), atlas inverse size (1 / W, 1 / H) at *(font + 224), font scale float at +232 (multiplies both run scales).
- V: quad corners = pen + rotate(angle, (xoff * sx, yoff * sy) + (0 or w * sx * fs) in x / (0 or h * sy * fs) in y), i.e. the glyph offsets use the run scale only and the glyph size also the font scale fs (+232); when the italic flag is set the x of the top corners shifts by -(yoff * sy + corner height) * shear. UV = atlas rect * (1 / W, 1 / H).
- V: each of the 4 vertices is 48 bytes: position xy, node-alpha dword (w), UV, a float4 (sx * fs, sy * fs, slot, 1 / (invW * 8192) = W / 8192 = g), colour dword. The quad is written at index 4 * count; then SDFFontRenderer_AccumulateBounds is called and the count incremented.
- V: the pen then advances by rotate(angle, (sx * advance, 0)) (advance = record +16), so the pen advance uses the x scale only.
- V (fit against the GPU back buffer, 2026-10-29): the title's effective on-screen scale is 0.41667 = 0.3125 / 0.75, i.e. the traced run scale (+9500, = size / 64 x 2/3) divided by the font's metric unit (unit_px_per_metric 0.75); a replica of the shader with quads at the traced pen positions and that scale lands within 0.03 px and 1.0001 x of the GPU glyph geometry. So fs (font + 232) is 1 / unit_px_per_metric = 1.3333 (I: the value itself was not read from memory) and the record offsets / advances in the extractor JSON are the metric-unit values the studio multiplies by the same effective scale.
- V: the per-vertex float4 carries sx * fs and sy * fs separately: the pixel shader's UV derivatives (and therefore K and the five tap offsets) see an anisotropic run. Live trace 2026-10-29 of the Job Tree: the title run is square (0.3125 x 0.3125); the Lv prefix / chip / badge runs of the overflow-mode-2 nodes are 0.2053 x 0.25 (x = box width / natural width). The studio now samples with separate sx / sy (GameFont.draw xscale; sdfParams xk).

## State touched

- Calls: [SDFFontRenderer_AccumulateBounds](SDFFontRenderer_AccumulateBounds.md)

## Referenced by

- Called by: [GUITextNode_Draw](GUITextNode_Draw.md)

## Notes

Run state was read live by tracing this function with --mem rcx+9500 (the rcx object is stable across glyphs of a frame).

## Open questions

K = 0.1 * 0.005 * g * S: the 0.005 comes from SDFFontRenderer_Flush's palette rewrite (see fonts.md). The quad geometry was read from the decompile, not checked against a captured vertex buffer. (The title's former 1.1 edge residual was a studio bug, not the game: GameFont's run cache was blitted at a fractional y; fixed 2026-10-29, title 0.30.)
