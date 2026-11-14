# UIBlur_DownsampleRegion

- **Address:** `0x1403B4798`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIBlur_DownsampleRegion(__int64 unused, __int64 stateCtx, __int64 layer, int srcRT, int *rect, int targetId, __m128i *clamp)`
- **Callers:** UIBlur_Run
- **Callees:** sub_1403B01F0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Wrapper for the half-size path of UIBlur_Run: converts the target id into a level count, runs sub_1403B01F0 on the downsample object and returns the level count used.

## Behavior

- V: obj = *(*(g_Renderer + 37936) + 8608); levels = min(targetId - 31, *(int *)(obj + 24)). With targetId = 32 that is 1.
- V: copies the 16-byte clamp rectangle to the stack and calls sub_1403B01F0(obj, stateCtx, layer, srcRT, rect, levels, &clamp); returns levels.
- V (sub_1403B01F0, when levels > 0): binds RT[srcRT] (g_Renderer + 20832 + 40 * srcRT, texture at +40) as an input, queues a constant record (levels, tile count, tile origin = rect >> 6, 1 / size read at g_Renderer+37936 -> +6568, the clamp rectangle, rect >> levels), applies a shader through ShaderSelector_Apply, calls sub_1403C49B0(state, tilesX, tilesY, 1) with the rect counted in 64 px tiles, and sets obj+28 = 1.
- I: the effect is a copy that downsamples the rect by 2^levels; the destination is the layer's own slot (800 * layer byte +86 + g_Renderer + 24184), not chosen by the id argument.

## State touched

- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (from the call context and the >> levels arithmetic; not verified live). The first argument is unused.

## Open questions

What sub_1403C49B0 does (a draw or a dispatch over a tile grid); whether the destination really is render target 32 (only the level count is derived from the id here); what obj+24 (maximum level) holds.
