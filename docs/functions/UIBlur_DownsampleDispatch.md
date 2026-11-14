# UIBlur_DownsampleDispatch

- **Address:** `0x1403B01F0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIBlur_DownsampleDispatch(__int64 obj, __int64 stateCtx, __int64 layer, int rtIndex, int *rect, int levels, __m128i *clamp)`
- **Callers:** UIBlur_DownsampleRegion (0x1403B4798)
- **Callees:** sub_14003E120, sub_14003E228, ShaderSelector_Apply, sub_1403C49B0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues the tiled downsample of a rectangle by 2^levels (compute-style dispatch over 64-pixel tiles); the work done by UIBlur_DownsampleRegion.

## Behavior

- V: only when levels > 0. Binds RT[rtIndex] (g_Renderer + 40 * rtIndex + 20832, handle +40) at state + 8 * (short obj+18) + 1608 (the output) and the object's constant buffer (obj+8) at state + 8 * (short obj+16) + 328.
- V: tile arithmetic (integers): tx0 = rect.x0 >> 6, ty0 = rect.y0 >> 6, tilesX = ((rect.x1 - 1) >> 6) - tx0 + 1, tilesY likewise; constant record: [0] = levels, [4] = tilesX * tilesY, [8] = tx0, [12] = ty0, [16] = (1 / renderW, 1 / renderH) (floats; both 1.0 when the render size is <= 1.19e-7), [32..47] = clamp rectangle copy, [48..63] = (x0 >> levels, y0 >> levels, x1 >> levels, y1 >> levels) (arithmetic shifts, i.e. floor).
- V: source texture = slot 3 table entry of the layer (800 * layer byte +86 + g_Renderer + 24184, handle +40), sampler constants of the selected program copied to state + 5704 + 4 * id (& 0x7FFFFFFF), ShaderSelector_Apply(selector at +128 of the UI renderer table, state, 0), then sub_1403C49B0(state, tilesX, tilesY, 1) (the dispatch) and obj+28 = 1.

## State touched

- Calls: [ShaderSelector_Apply](ShaderSelector_Apply.md)
- Reads: [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [Renderer.render_targets](../structs/Renderer.md#render_targets), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words)

## Notes

The name is ours (IDB: sub_1403B01F0). Pixel snapping: the downsampled rectangle is floor(rect / 2^levels) with right / bottom floored too, so odd sizes lose a pixel at the far edge; the tile grid is 64 px aligned.

## Open questions

Exact semantics of sub_1403C49B0 (dispatch vs draw).
