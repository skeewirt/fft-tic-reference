# GUILayer_GlowPass

- **Address:** `0x1403B4EA8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_GlowPass(UILayer *layer, __m128i *cmd, unsigned char targetType, int *rect, __m128i *clamp, __int64 target, int srcTex, int a8, int a9, int dstTex)`
- **Callers:** GUILayer_ApplyEffects
- **Callees:** UIBlur_Run, ShaderSelector_Apply, sub_1403C4AA8, sub_140069A38

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Glow composite: blurs the layer by the glow radius and draws the result with the glow shader permutation selected by the mode field.

## Behavior

- V: UIBlur_Run(layer, target, targetType, 44, 1, radius = layer+204, ..., a7 = blurred output, a10 = source, scratch 28); then selects the shader technique v12[11] of the UI selector, sets its permutation digit 0 from layer+480 (the mode: 3 for the Job Tree), binds the texture of the layer's slot +64 to the list entry srcTex and slot +66 to dstTex, takes the draw rectangle from layer+240 and queues a 96-byte command.
- V: strength (+200), colour (+468..+476) and the other group values reach the shader through the constant buffer filled by UILayer_FillConstants (sub_1403B08AC): strength to constant offset 212, colour to 512..520.

## State touched

- Calls: [UIBlur_Run](UIBlur_Run.md), [ShaderSelector_Apply](ShaderSelector_Apply.md)
- Reads: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.glow_radius](../structs/GUILayer.md#glow_radius), [GUILayer.glow_mode](../structs/GUILayer.md#glow_mode), [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [GUILayer.tex_slot_b](../structs/GUILayer.md#tex_slot_b), [GUILayer.index](../structs/GUILayer.md#index), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.targets_by_type](../structs/Renderer.md#targets_by_type), [Renderer.render_targets](../structs/Renderer.md#render_targets), [UIManager.effect_input_layout](../structs/UIManager.md#effect_input_layout), [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers)

## Referenced by

- Appears in flows: [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md), [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md)

## Notes

Shader (V): live read of the technique-11 selector (read-only debugger) gives programs for the digit-0 permutations 0..3 = pixel shader ids 53..56 (ids: 9 vertex shaders, then pixel shaders, in .tec file order), i.e. the 3rd to 6th pixel shader variants of the layer-effect family; the Job Tree glow (mode 3) is the 4th: add.rgb = 2 * strength * colour * A.rgb * (B.a * (1 - A.a) + (1 - B.a)), add.a = max(B.a, A.a), added to the UAV target (unorm) after textureLoad. Roles (V from the calls): T0 / A = slot +64 = the blurred output, T1 / B = slot +66 = the sharp source (UIBlur_Run reads a10 and writes a9). The target is the same object GUILayer_BlitFinal drew the layer into just before, so the add lands on top of the layer the layer content is premultiplied (V): the plain-image shader writes rgb * a and the default UI draw state blends ONE / INV_SRC_ALPHA (word 0x79420a11, see UIRender_ApplyDrawState), and the blur is linear.

## Open questions

None recorded.
