# GUILayer_BlurShadowPass

- **Address:** `0x1403B4990`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char GUILayer_BlurShadowPass(UILayer *layer, __int64 stateCtx, unsigned char targetType, int *rect, __m128i *clamp, RenderTarget *target)`
- **Callers:** GUILayer_ApplyEffects
- **Callees:** UIBlur_Run, ShaderSelector_Apply, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Second step of the +177 (drop shadow) effect group: blurs the silhouette in RT 3 by the radius at layer+188, then draws it onto the layer's target with selector #10 program 1, which darkens the target by the shadow strength and tint and adds the shadow alpha.

## Behavior

- V: sets the sort key at state+8 = ((layer+12 & 0x1FF | ((layer+16 & 0x3F | targetType << 18) << 15) | 0x6AC02000) << 10) (targetType 1 treated as 0), runs UIBlur_Run(layer, target, targetType, 16, 1, radius = float layer+188, rect, clamp, 3, 3, 28, -1), then re-sets the key with the constant 0x6AC07600.
- I: in the UIBlur_Run call 16 is the base of the sub-ordinal added into the sort key ((a4 + k) & 0x3F terms), 3 / 3 are the output and source render-target indices (RT 3 in place, as GUILayer_GlowPass passes output and source), 28 is the scratch index.
- V: shifts the clamp rectangle in state+80..92 by minus the integer parts of layer+224 / +228 ((int) truncation toward zero) so it is in screen instead of atlas coordinates.
- V: destination = the entry at 800 * (byte target+86) + g_Renderer + 23736, stored at state+96 with its +40 member at state+144 (the render target the draw writes to: the layer's parent target, the same one GUILayer_BlitFinal draws into afterwards); the fourth argument is the render target object from UILayer_GetTarget, not a layer.
- V: source = RT 3 (g_Renderer + 20952, its +40 member) bound as the texture at state + 8 * (short layer+64) + 1608; the technique's default sampler words are copied as in GUILayer_CopyToTarget; the draw uses selector #10 (*(*(g_Renderer+37936) + 80)) with ShaderSelector_Apply(selector, state, 1): program index 1; no permutation digit is set in this function.
- V: vertex buffers: state+136 = the manager object's element [1060], state+200 = the +40 member of element [1062], stride 16 (state+208) and byte offset (layer+8) << 6 (state+212): this layer's 64-byte quad; state+124 = (& 0xFFC06FFF) | 0x6000, state+6016 = 0; a 96-byte command from sub_140069A38(state, 4, 96) with +8 = 4, packed and submitted.
- V: the only writes to the context's sampler words (+5704 + 4 * slot) in this function are the technique's own default words: the loop over the slot id list at technique+160 and the word list at technique+168 (count at technique+108), each stored & 0x7FFFFFFF, before ShaderSelector_Apply. It never writes slot 14 (g_Sampler) or slot 15.
- V (live read 2026-10-30): the selector #10 technique lists slots 13 (ccc_lln_sampler) and 16 (ccc_lln_sampler_tMaskBuffer), both with the word 0x26A = clamp on all axes, min / mag linear, mip point. Slot names: see NameSlotTable_Lookup.
- V (shader disassembly; not re-read here): pixel shader 035E50 samples its source (T0) through g_Sampler, slot 14, which this pass does not set.
- V (live trace 2026-10-30 at the ShaderSelector_Apply call 0x1403B4B6D): the word at context + 0x1680 (= +5704 + 4 * 14, slot 14) is 0 on all four Job Tree shadow passes, i.e. the default sampler word (0 at runtime, Sampler_DescFromWord): point filter, WRAP, MinLOD = MaxLOD = 0.
- I: slot 14 still holds the default word because the shadow commands are packed during GUILayer_Composite (UIRender_SubmitFrame), after RenderContext_ResetFrame wrote the default into every sampler slot at the start of the frame and before UICommandRing_Flush replays the UI draws (UIRender_ApplyDrawState writes g_Sampler per UI draw, UICommandRing_Flush writes the default to slots 14 and 15). Basis: the call order in UIRender_SubmitFrame and the live trace above; the order against RenderContext_ResetFrame was not re-read here.
- V (mid-frame GPU captures 2026-10-30): with shadow offsets 1.6 and 1.333 the blurred alpha lands 2 px and 1 px away from the layer pixels.
- I: consequence: the blurred alpha is point-sampled (not bilinear), so the texel read for output pixel x is floor(x + 0.5 - offset). Basis: the slot 14 word above and the two captures.
- V: the quad: element [1062] (byte offset 8496) of the UIRenderer object at g_Renderer + 37936 (the object UIRender_SubmitFrame is a virtual method of) is a buffer object that UIRender_SubmitFrame maps, storing the mapped pointer as element [1065] (offset 8520); GUILayer_FillQuadBuffers fills element [1065], at record 4 * (layer+8), with the layer rectangle moved by minus the atlas offset (position = rect - atlas offset, uv = that position / the target size g_Renderer+6568 / +6572). The vertex shader adds the shadow offset to the position, so the shadow is drawn over (rect - atlas offset) + offset.
- I: nothing outside (rect - atlas offset) + offset can be darkened by this pass, because no pixel outside that moved quad is rasterised. Basis: the quad geometry above.
- V (shader disassembly, ui_035e50 / ui_035438): the vertex shader 035438 passes the uv through and adds cb12.zw (the shadow offset in pixels, layer+192 / +196) to the quad position before the pixel-to-clip matrix (rows 4-7). The pixel shader 035E50 samples A = alpha of T0 at uv + cb34.zw (atlas offset in UV) and computes s = saturate(cb13.x * A) (cb13.x = layer+184, the shadow strength); with the distance mask off (cb20.x = 0) it rewrites the UAV target: rgb = rgb * ((1 - s) + cb31.rgb * A), a = s + a * (1 - s), cb31.rgb = the shadow colour (layer+456..+464). With a black colour this is a plain black 'over' composite of strength s under the layer.
- V (live read of the running game's selector, 2026-10-29, same walk): selector #10 program 1 = vertex shader 035438 + pixel shader 035E50.

## State touched

- Calls: [UIBlur_Run](UIBlur_Run.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [GUILayer.shadow_radius](../structs/GUILayer.md#shadow_radius), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [GUILayer.index](../structs/GUILayer.md#index), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.targets_by_type](../structs/Renderer.md#targets_by_type), [UIManager.effect_input_layout](../structs/UIManager.md#effect_input_layout), [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer), [UIManager.selector_10](../structs/UIManager.md#selector_10), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words) [13, 16] technique defaults

## Referenced by

- Applies shader programs: [LayerShadow](../programs/LayerShadow.md)
- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md)

## Notes

The name is ours (IDB: GUILayer_BlurShadowPass). The +177 group is the component drop shadow (flag +177, strength +184, radius +188, offset +192 / +196, colour +456..+464); layer+k = BuildRecord record+(k-24). Pixel exact: the atlas -> screen offset is truncated to integers. Direction: the per-target entry at 800 * byte + 23736 is the destination (the render target) and RT 3 the sampled source.

## Open questions

? the blend / raster words of program entry 1 (not read; the pixel shader writes the target through a typed UAV, so the fixed-function blend is probably unused). ? the exact UIBlur_Run argument meanings (a4 = 16, a5 = 1).
