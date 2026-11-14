# GUILayer_CopyToTarget

- **Address:** `0x1403B4800`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char GUILayer_CopyToTarget(UILayer *layer, __int64 stateCtx, __int128 *rect, RenderTarget *target, int a5, int srcRT)`
- **Callers:** GUILayer_ApplyEffects
- **Callees:** ShaderSelector_Apply, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

First step of the +177 (drop shadow) effect group: draws the layer's current scratch render target RT[srcRT] into slot 3 of the layer target's slot table with selector #10, program 0, clipped to a rectangle (a silhouette copy of the layer's alpha, see the shader note).

## Behavior

- V: the fourth argument is not a layer: GUILayer_ApplyEffects passes UILayer_GetTarget(layer), the layer's render target object; its byte +86 selects the per-target slot table (g_Renderer + 512 * byte + 24224, 8-byte slots) used below.
- V: destination = the table entry g_Renderer + 512 * (byte target+86) + 24248 (slot 3). It is stored at state+96 and its +40 member at state+144 (the render-target binding of the draw); when that member's type (+8) is 1 or 2 the low 3 bits of its +16 go to state+124 bits 9..11.
- V: source texture = RT[srcRT] = the object at g_Renderer + 40 * srcRT + 20832 (its +40 member, 0 when the pointer is null), bound as the texture at state + 8 * (short layer+64) + 1608. srcRT is GUILayer_ApplyEffects' current scratch index (the one holding the layer's pixels so far).
- V: the selector is the one at index 10 of the UI manager's selector array (*(*(g_Renderer+37936) + 80)); the technique's default sampler words (count +108, ids +160, values +168 of the technique) are copied to state + 5704 + 4 * id (top bit cleared); then ShaderSelector_Apply(selector, state, 0): program index 0 of the selected permutation.
- V: no vertex buffers are bound (state+136 and +200 and the stride fields +208 / +212 are zeroed); state+112 |= 0x10 with its high bits cleared (clip enable) and the 16-byte int rectangle is copied to state+80; state+124 = (& 0xFFC06FFF) | 0x6000; state+6016 = 0; a 96-byte command is allocated with sub_140069A38(state, 4, 96), its +8 = 4 and +12 = 0, packed with RenderState_PackCommand and submitted with sub_140069980.
- V (shader disassembly of UIRender.tec): pixel shader 0349C0 samples T0 at the uv clamped to at most cb37.zw and writes (0, 0, 0, texture alpha), i.e. a black silhouette of the source alpha; its likely vertex partner 034080 builds an oversized triangle from SV_VertexID, so it needs no vertex buffer (consistent with the zeroed slots above).
- V (live read of the running game's selector, 2026-10-29: *(*(*(g_Renderer+37936): +80)+48/+56/+64/+40) program entries, program table, index list and shader objects): selector #10 program 0 = vertex shader 034080 + pixel shader 0349C0.

## State touched

- Calls: [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.render_targets](../structs/Renderer.md#render_targets), [UIManager.selector_10](../structs/UIManager.md#selector_10), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers)

## Referenced by

- Appears in flows: [LayerDropShadow](../flows/LayerDropShadow.md)
- Applies shader programs: [LayerAlphaCopy](../programs/LayerAlphaCopy.md)
- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md)

## Notes

The name is ours (IDB: GUILayer_CopyToTarget). Direction: state+96 / state+144 hold the render target the draw writes to (GUILayer_BlitFinal and sub_1403CB8BC use the same fields for the real target), and the texture bound at state+1608 + 8 * slot is the one sampled; so RT[srcRT] is the source and the slot-3 entry is the destination. I: GUILayer_Composite queues a type-0 32-byte command on the slot-3 texture once per layer id when the layer has +177 set and +486 clear (it looks like a clear before this copy). I: the slot table entries point at the same render-target objects as the RT array (GUILayer_EffectPass0 writes slot 27 and the next pass reads RT 27; the blur after this step works on RT 3).

## Open questions

? what a5 is (unused). ? whether slot 3 of the target slot table is the same object as RT[3] (g_Renderer + 20952), which the blur pass uses. ? the pipeline state words of program entry 0 (blend, raster, samplers) were not read. ? which constant buffer program 0 sees: the vertex shader declares a 720-byte buffer (reads cb11.xy as a uv scale) and none is bound in this function.
