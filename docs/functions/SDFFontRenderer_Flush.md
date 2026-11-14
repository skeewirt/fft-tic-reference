# SDFFontRenderer_Flush

- **Address:** `0x1403A9B20`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SDFFontRenderer_Flush(SDFFontRenderer *r, int mode)`
- **Callers:** GUI frame renderer
- **Callees:** sub_1403A8FBC, qsort, sub_14003E120 (map buffer), sub_14003E228 (unmap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Uploads the frame's glyph quads and palette entries to the GPU and issues the batched SDF text draws; rewrites every palette entry into the form the pixel shader uses.

## Behavior

- V: with mode 0 and a live renderer it closes the current batch (sub_1403A8FBC), sorts the batches, copies 192 bytes per glyph quad vertex group from +9552 and 192 bytes per palette entry from +9560 (count +9516) into the mapped GPU buffers.
- V: while copying, each palette entry is transformed in place (offsets in bytes of the entry): [96] = [96] * 0.005; [104] = ([68] * 128) * 0.5 (the outline layer's coverage cap = outline threshold * 64); [64] = ((1 - [64]) - 0.5) * 0.5 + 0.5 = 0.75 - T / 2; [68] = ((1 - [64] - [68]) - 0.5) * 0.5 + 0.5; [76] = 1 / [76]; [88] = ((1 - [88]) - 0.5) * 0.5 + 0.5; [92] = [92] * 0.5; [188] = 1 - [188]; and the shadow colour [112] is replaced by [128] when the shadow width [80] is 0.
- V: consequence: the shader's contour sits at d = 0.75 - T / 2 (T = UIFontSet.Unknown8, times Unknown30 = 1.1 for bold runs), so a larger T makes text HEAVIER (T 0.605 gives 0.4475), and the edge half-width is K = 0.1 * 0.005 * g * S. The CPU copy at +9560 (what a live memory read sees) is the untransformed one.
- V: also builds the quad UV corner table (+9544 / +9548 divisors) and binds up to 12 atlas pages (tTexture0..12) and the cSDFConstant buffer per batch.
- V: per batch it applies four programs of the SDFFont technique (ShaderSelector_Apply): program 2 with a 4-vertex draw on the target at g_Renderer + 23720 + 800 * block, program 4 with a 4-vertex draw on the target at g_Renderer + 23640 + 800 * block, program 1 with the glyph instances (sub_1400ADB20) on that same +23640 target, and program 0 with the glyph instances on the +23720 target.
- V (the technique file shader/SDFFont.tec, its five 64-byte program entries read with the ShaderProgram_ApplyState layout; blend word decoded with BlendDesc_FromWords, depth word with the depth-stencil decoder sub_140051438: bit 0 enable, bit 1 write, bits 2..4 + 1 = comparison): program 0 blend SRC_ALPHA / INV_SRC_ALPHA (alpha ONE / INV_SRC_ALPHA), depth off; program 1 blending off, depth on, written, LESS_EQUAL; programs 2 and 3 blend ONE / INV_SRC_ALPHA, depth off; program 4 blending off, depth written, ALWAYS.
- V: of the file's pixel shaders only the fill shader (blob at 0x3558) writes SV_Depth; the depth it writes is 1 - d (d = the distance at the pixel centre). I (shader index lists in file order: program 0 = VS 0x640 + PS 0x1450 the shadow, 1 = VS 0x2764 + PS 0x3558 the fill, 2 = VS 0x5EE4 + PS 0x67B0, 4 = VS 0x5EE4 + PS 0x7004): the fill glyphs are drawn without blending into a target whose depth was reset by program 4, so where glyph quads overlap the glyph with the largest d keeps the pixel, and the shadow glyphs are blended one by one. The studio models it so (behavior TextFillPassDrawnAsOneShape).

## State touched

- Reads: [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles)

## Referenced by

- Observed behaviours: [TextFillPassDrawnAsOneShape](../behaviors/TextFillPassDrawnAsOneShape.md)

## Notes

Found by following the SDFFont setup at sub_1403A87EC to the code that reads the +9552 / +9560 buffers.

## Open questions

? how the fill target reaches the layer: program 2's 4-vertex draw comes before the glyph draws of the same batch in this function, so the composite of the fill target (and its order against the shadow glyphs) is not settled by this function alone; the frames show the fill over the shadows. ? the depth format.
