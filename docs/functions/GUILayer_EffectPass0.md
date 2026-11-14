# GUILayer_EffectPass0

- **Address:** `0x1403B5818`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_EffectPass0(GUILayer *layer, RenderCtx *rc, void *target, int outSlot, int inSlot)`
- **Callers:** GUILayer_ApplyEffects (only; called first with outSlot 27, inSlot 26 when layer+489 is set and (layer+492 = 0 or layer+36 >= 0); argument 3 is the target object from UILayer_GetTarget)
- **Callees:** ShaderSelector_Apply, RenderState_PackCommand, sub_140069A38, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

First layer-effect pass of GUILayer_ApplyEffects (run when the layer's props flag +489 is set): sets up one render command that binds two layer textures and a shader selector and queues a 96-byte command.

## Behavior

- V: reads the shader selector from the renderer global (qword_143CDA098+37936, then +96) and the render target it WRITES from the per-target table at global+24224 indexed by (byte target+86 << 6) + outSlot (27 in the only call); stores it at rc+96 and its +40 member at rc+144; rc+124 bits 9..11 take the low 3 bits of that member's +16 when its type (+8) is 1 or 2.
- V: copies the selector's constant list (count at +108, index array +160, value array +168) into rc+5704+4*index with the top bit cleared, then calls ShaderSelector_Apply(selector, rc).
- V: binds the two textures it SAMPLES into rc+1608 at the slots given by layer+64 and layer+66 (global+20832+40*inSlot = RT 26, +40 member; and global+22032 = RT 30, the mask buffer, an R8 target (live: GPU resource 47, R8_UNORM 1280x720), +40 member); sets rc+136, rc+200, rc+208 = 16, rc+212 = layer+8 << 6, rc+120 = 0x77FD0010 and flag bits in rc+124 (0x6000), rc+6016 = 0.
- V: allocates a command with sub_140069A38(rc, 4, 96), sets its +8 = 4 and +12 = 0, packs it with RenderState_PackCommand and submits it with sub_140069980 when the pack returns nonzero.
- V (live 2026-10-29, Job Tree): exactly ONE layer goes through this pass per frame (layer object 0x294523B2AE8 that run, the title's TextMask layer); the same layer also runs GUILayer_CopyToTarget, GUILayer_BlurShadowPass, UIBlur_Run (from the shadow pass) and GUILayer_BlitFinal, but not the glow pass. Its effect bytes: +176 = 0 (blur off), +177 = 1 (shadow blur ON), +178 = 0 (glow off), +179 = 1, +484 = 3, +489 = 1 (this pass), +492 = 1; floats +180 = 1.0, +184 = 1.0, +188 = 2.0 (the shadow blur radius), +196 = 2.6667, +200 = 0.3, +204 = 1.0, +208 = 2.0.
- V (shader: shader/UIRender.tec split into its blobs, the DXIL disassembled with dxc -dumpbin): the 2-texture mask pixel shaders of UIRender.tec (for example the blob at file offset 0x3D41C) read tTexture0 and the mask texture at the same uv, take the MASK TEXTURE'S ALPHA (optionally 1 - alpha, selected by a cbuffer word at cUIRender register 15 .z) and output tTexture0.rgba * mask for all four channels: result = gradientLayer.rgba * textLayer.a. The mask uses alpha only, not luminance. (I: which of the 2-texture blobs this pass selects (selector index 3) was not matched to a blob.)
- V (studio test against the GPU frame): changing the mask alpha (alpha^0.8, ^1.5, ^2, smoothstep) makes the title error worse (2.7 / 4.3 / 6.7 / 2.4 against 1.105), so the layer alpha is the straight text coverage, as the studio models it.

## State touched

- Calls: [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [GUILayer.tex_slot_b](../structs/GUILayer.md#tex_slot_b), [GUILayer.index](../structs/GUILayer.md#index), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.slots_by_type](../structs/Renderer.md#slots_by_type), [Renderer.render_targets](../structs/Renderer.md#render_targets), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0)

## Referenced by

- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md)

## Notes

The name is ours. ApplyEffects swaps the slot numbers (26/27, then 29) after this pass, so the slots look like ping-pong layer textures (I). I: this is the mask pass: the Job Tree title (TextMask) is the one component here with a Mask node, its mask component (TextBoard01, the text) is drawn into a separate layer first (ComponentLayer_DrawMaskComponent) and this pass binds two layer textures; the studio models it as the gradient rect times the text coverage, which matches the retail capture to a mean error of 0.65 (header region).

## Open questions

Which UIRender.tec blob selector 3 picks; the meaning of the 0x77FD0010 word and of the 96-byte type-4 command; what +489 means in the props file (it enables this mask pass).
