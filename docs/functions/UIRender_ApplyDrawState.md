# UIRender_ApplyDrawState

- **Address:** `0x1403AE1A0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIRender_ApplyDrawState(UIRenderer *r, UIDrawState *state)`
- **Callers:** UIRender_FlushBatch
- **Callees:** sub_14039EC9C, sub_14003E120, sub_14003E228, sub_14002931C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Programs the graphics pipeline from a draw state: shader permutation, blend/raster bits, texture, samplers and the cSDF constant buffer.

## Behavior

- V: shader permutation index = 4 * ((flags & 0xF) + 8 * ((flags >> 4) & 7)) (stored at thread state +228 when it changes); the ring flags 0x52 give 168.
- V: binds the texture at state+16 (texture+40 handle) and its sampler constant (state+4 & 0x7FFFFFFF); state+0 goes to thread state +120; blend words from state+8 (mask 0x100001FFF).
- V (0x1403AE419..0x1403AE488): when the draw has a texture (draw+0x10 != 0) it binds the texture handle (texture+40) at the tTexture0 slot (UIRender object +72, context + 1608 + 8 * slot) and writes the draw's sampler word (draw+4 & 0x7FFFFFFF) to the g_Sampler slot (UIRender +70, context + 5704 + 4 * slot) and to the g_Sampler_tMaskBuffer slot (+74).
- V (same range): when the draw has no texture it binds the default texture instead (the object at UIRender +0x28, its +40 handle, or 0 when that object is null) and writes the default sampler word (dword_141D8BC7C & 0x7FFFFFFF) to both slots.
- V (live 2026-10-30): the sampler word of a textured UI draw is 0x2C0 (min / mag linear, mip point, WRAP; see Sampler_DescFromWord); the default word is 0 at runtime (point, wrap). The slot ids are 14 (g_Sampler) and 15 (g_Sampler_tMaskBuffer) in the live sampler name table (NameSlotTable_Lookup).
- V: only when flag bit 0x800 is set the cSDF buffer (r+48) is written: {1, state+28, state+32 * 0.005, state+36, state+40 (float2)}; otherwise a zeroed 32-byte buffer (r+56) is bound.
- V: the draw state's FIRST word (state+0) is the render-target blend word, stored straight into the thread state at +120; sub_140051284 (BlendDesc_FromWords) later unpacks every blend word into a Direct3D 12 render-target blend description: enable = bit 0, blend op = ((w >> 1) & 7) + 1, colour source / destination factor = ((w >> 4) & 0x1F) + 1 / ((w >> 9) & 0x1F) + 1, alpha op = ((w >> 14) & 7) + 1, alpha source / destination factor = ((w >> 17) & 0x1F) + 1 / ((w >> 22) & 0x1F) + 1, write mask = (w >> 27) & 0xF (each factor field is the D3D12_BLEND value minus 1: 0 ZERO, 1 ONE, 4 SRC_ALPHA, 5 INV_SRC_ALPHA, 13 / 14 BLEND_FACTOR / INV_BLEND_FACTOR).
- V (live read of the default draw state at 0x1408FF878, copied by GUIRenderer_ResetFrame at the start of every frame): word0 = 0x79420a11 = enabled, ADD, source ONE, destination INV_SRC_ALPHA, alpha ONE / INV_SRC_ALPHA, mask RGBA, i.e. premultiplied-over blending. state+4 is the sampler word (UIDraw_SetStateFromSlot's 0x2C0 mask acts on it), not a blend word.

## State touched

- Reads: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [UIRender.slot_cSDF](../structs/UIRender.md#slot_csdf), [UIRender.slot_tTexture0](../structs/UIRender.md#slot_ttexture0), [UIRender.slot_g_Sampler_tMaskBuffer](../structs/UIRender.md#slot_g_sampler_tmaskbuffer), [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md), [g_Renderer](../globals/g_Renderer.md), [UIRender.slot_g_Sampler](../structs/UIRender.md#slot_g_sampler)
- Writes: [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words) [14, 15] per draw

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md), [UiLayerComposite](../flows/UiLayerComposite.md)
- Applies shader programs: [UIImage](../programs/UIImage.md)
- Called by: [UIRender_FlushBatch](UIRender_FlushBatch.md)
- Observed behaviours: [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md)

## Notes

cSDF is read by two SDF image pixel shaders (shader_4990 and shader_5560). No live texture has the flag set.

## Open questions

None recorded.
