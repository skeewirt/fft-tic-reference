# UIRender_DrawOverlayQuads

- **Address:** `0x1403B8F20`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIRender_DrawOverlayQuads(__int64 ui)`
- **Callers:** UIRender_SubmitFrame
- **Callees:** UILayer_GetTarget, sub_1403A8468, ShaderSelector_Apply, sub_14003E120, sub_14003E228, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws up to three textured rectangles registered at ui+8672 (48-byte records) over the base target with selector program 5.

## Behavior

- V: runs when any of the three records at ui+8672 + 48 * i has a texture. The target size is the u16 +20 / +22 of the base target (UILayer_GetTarget of layer 0, or the current one); sort key state+8 = (targetByte << 43) | 0x1AB00080000.
- V: per record: texture at record+0, pixel rect ints (x0 = +8, y0 = +12, x1 = +16, y1 = +20), uv floats at +24 / +28 / +32 / +36. Positions are written to the vertex buffer ui+8424 in clip space with x = px * (2 / W) - 1 and y = 1 - py * (2 / H); no half-pixel offset and no rounding. The command copies a clamp rect from record+8 (4 ints) into state+80, uses stride 16 and a 64-byte buffer offset per quad and queues command type 4.

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [UIManager.effect_input_layout](../structs/UIManager.md#effect_input_layout), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles)

## Referenced by

- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403B8F20; purpose I: overlay / cursor-like quads, unverified). The pixel-to-clip mapping is useful as a reference for how integer pixel rectangles become vertices.

## Open questions

What the three records contain at runtime.
