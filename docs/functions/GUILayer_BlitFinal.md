# GUILayer_BlitFinal

- **Address:** `0x1403B4C2C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_BlitFinal(UILayer *layer, __m128i *cmd, __int64 target, __m128i *rect, int a5, int dstTex)`
- **Callers:** GUILayer_ApplyEffects, GUILayer_BlurEffect
- **Callees:** ShaderSelector_Apply, sub_1403C4AA8, sub_140069A38

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the layer's own pixels onto its parent with the layer blend mode (the pass after the +176 / +177 effects).

## Behavior

- V: copies the rectangle into the command, sets selector digit 0 from layer+32 and digit 1 from whether any of the three offset vectors at +120..+140 is non-zero, binds the texture slots +64 / +66 (and +320's texture when enabled), blend type = layer+8 << 6, and queues a 96-byte command.
- V (read 2026-10-30): destination = the entry at g_Renderer + 800 x (byte target + 86) + 23736 (row slot 2, the frame target), stored at state+96 with its +40 member at state+144; the source texture of both texture slots is RT[a6] (g_Renderer + 40 x a6 + 20832, +40 member) with a6 = the index GUILayer_ApplyEffects passes (26, RT 26 the layer content, for a layer with no pass that moved it).
- V: the blend word stored after the program apply is 2013397009 = 0x78020011 (enabled, source ONE, destination ZERO, add, alpha the same, write mask 0xF, decoded with the BlendDesc_FromWords field layout). The program's pixel shader writes no render-target output but the UAV u0 (the frame target), so the compositing arithmetic is in the shader: see the program LayerBlit and the behavior LayerBlitOverFrameTarget.
- V: the quad is vertex slot (layer+8) << 6 of the layer quad buffer (stride 16): the layer's integer screen rectangle (rect - atlas offset), uv = position / target size; the shader adds the atlas offset to the uv, so it reads texel (pixel + atlas offset) of RT 26.
- V: the sort key in force when the command is submitted is the caller's (GUILayer_ApplyEffects sets 0x6AC07600, pass 59), so the blits of an atlas page run after all the draws of the page.

## State touched

- Calls: [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderCommand_Allocate](RenderCommand_Allocate.md), [RenderCommand_Submit](RenderCommand_Submit.md)
- Reads: [GUILayer.blend_mode](../structs/GUILayer.md#blend_mode), [GUILayer.offset_vectors](../structs/GUILayer.md#offset_vectors), [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [GUILayer.tex_slot_b](../structs/GUILayer.md#tex_slot_b), [GUILayer.index](../structs/GUILayer.md#index), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.targets_by_type](../structs/Renderer.md#targets_by_type), [Renderer.render_targets](../structs/Renderer.md#render_targets), [UIManager.selector_9](../structs/UIManager.md#selector_9), [UIManager.effect_input_layout](../structs/UIManager.md#effect_input_layout), [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.state_flags](../structs/RenderContext.md#state_flags)

## Referenced by

- Appears in flows: [LayerDropShadow](../flows/LayerDropShadow.md), [UiLayerComposite](../flows/UiLayerComposite.md)
- Applies shader programs: [LayerBlit](../programs/LayerBlit.md)
- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md), [GUILayer_BlurEffect](GUILayer_BlurEffect.md)
- Observed behaviours: [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md)

## Open questions

None recorded.
