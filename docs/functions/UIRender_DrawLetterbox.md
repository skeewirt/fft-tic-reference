# UIRender_DrawLetterbox

- **Address:** `0x1403B93BC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIRender_DrawLetterbox(UIRenderer *ui)`
- **Callers:** UIRender_SubmitFrame
- **Callees:** UILayer_GetTarget, ShaderSelector_Apply, sub_1403A8468, sub_14003E120, sub_14003E228, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When the output surface is a different size than the UI target, fills the border regions (letterbox / pillarbox bars) with selector program 0.

## Behavior

- V: base = the renderer's current target; (baseW, baseH) = its u16 +20 / +22, (outW, outH) = dwords +40 / +44 of the frame target object (*(qword_140C696A8 + 88)). Does nothing when they are equal.
- V: bars: dx = (outW - baseW) * 0.5, dy = (outH - baseH) * 0.5 (floats, not rounded; a non-positive half difference becomes the full size); the two rectangles are (0, 0)-(dx, dy-or-H) and (outW - dx, outH - dy)-(outW, outH) converted to clip space (x * 2 / W - 1, 1 - y * 2 / H) into the 2-quad buffer ui[1055]; the draw uses the full output rect (0, 0, outW, outH) as the clamp in state+80 and queues a command of header type 5 with the key (targetByte << 43) | 0x1AB60000000.

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect)

## Referenced by

- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403B93BC; the letterbox role is inferred from the arithmetic: bars of half the size difference). The bars use fractional half differences, so an odd size difference puts the content boundary on a half pixel.

## Open questions

Where the base target is scaled to the output (not in this function); the fill colour.
