# UIBlur_CopyTarget

- **Address:** `0x1403ABEDC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIBlur_CopyTarget(UIBlurRenderer *b, __int64 layer, int srcSlot, int dstRT, int unused, int filterIdx, __m128i *srcRect, __int64 flag)`
- **Callers:** UIBlur_Run, UIBlur_Pass, UIBlur_BlurPassOrCopy, GUILayer_BlurEffect
- **Callees:** ShaderSelector_SetDigit, ShaderSelector_Apply, sub_14003E120, sub_14003E228, sub_14003E5D8, sub_14003E604, sub_14003F794, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a layer slot texture into a render target with a chosen filter index; the copy used between blur stages.

## Behavior

- V: returns when b+308 (enabled) is 0. dstRT 64 selects the layer's own target (g_Renderer + 40 * layer byte +86 + 23392); other values index g_Renderer + 40 * dstRT + 20832. The source texture is the slot g_Renderer + 8 * (srcSlot + (layer byte +86 << 6)) + 24224.
- V: binds the source (render state +96 / +144, its format bits into state+124 bits 9..11), then ShaderSelector_SetDigit(b+32, 0, 1) and, for filterIdx 0, 1 or 2, ShaderSelector_SetDigit(b+32, 1, filterIdx); any other filterIdx leaves slot 1 unchanged.
- V: srcRect and flag are optional. With srcRect the rectangle is scaled by the texture size into state +80 (state flag +112 bit 4 set); with neither, the constant xmmword_140723990 is written as the full-surface coordinates; the flag with srcRect also fills two more per-texel-size constants.
- V: finishes by binding the destination texture (state +1608 + 8 * index), resetting the state words (+124 mask, 0x6000) and queueing a draw command (sub_140069A38 size 96, header 3, RenderState_PackCommand, sub_140069980).

## State touched

- Calls: [ShaderSelector_SetDigit](ShaderSelector_SetDigit.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [Renderer.render_targets](../structs/Renderer.md#render_targets), [Renderer.slots_by_type](../structs/Renderer.md#slots_by_type), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words) [12, 13]

## Referenced by

- Called by: [GUILayer_CopyOffsetRegion](GUILayer_CopyOffsetRegion.md), [UIBlur_BlurPassOrCopy](UIBlur_BlurPassOrCopy.md), [UIBlur_Pass](UIBlur_Pass.md)

## Notes

The name is ours. The filter index is only a selector digit (slot 1); which sampler or shader variant each of 0 / 1 / 2 is was not traced. The decompile loses the arguments of some inlined helpers (texture size lookups).

## Open questions

What the filter values 0, 1, 2 mean; the 5th argument (unused in the decompile); what the sub_14003E5D8 / sub_14003E604 results are (texture width / height ?); the layout of the 96-byte command.
