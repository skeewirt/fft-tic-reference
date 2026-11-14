# GUILayer_ApplyEffects

- **Address:** `0x1403B6204`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_ApplyEffects(UILayer *layer, unsigned char targetType, __int64 a3, __int64 a4, __int64 a5, __m128i *rect, __m128i *clampRect)`
- **Callers:** GUILayer_Composite
- **Callees:** GUILayer_EffectPass0, sub_1403B5170, sub_1403AEE0C, sub_1403B53C8, UIBlur_Run, GUILayer_CopyToTarget, GUILayer_BlurShadowPass, GUILayer_BlitFinal, GUILayer_GlowPass, UILayer_GetTarget

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the enabled effect passes of one finished layer in a fixed order, ping-ponging between two scratch render targets, then draws the layer's own pixels and finally the +178 effect group.

## Behavior

- V: order: +489 (GUILayer_EffectPass0), +320 (sub_1403B5170), +484 (sub_1403AEE0C), +486 (sub_1403B53C8), the +176 group (blur with radius +180, UIBlur_Run mode flag 1), the +177 group (GUILayer_CopyToTarget + GUILayer_BlurShadowPass, skipped when +486), the plain layer blit (GUILayer_BlitFinal) and last the +178 group (GUILayer_GlowPass, skipped when +486). Source and destination target indices (26 / 27, 29 replacing 26) swap after every pass.
- V: the swap bookkeeping: v7 = the render-target index holding the layer's pixels so far (starts 26), v11 = the next destination (starts 27). +489 (and +492 == 0 or (int)layer+36 >= 0): GUILayer_EffectPass0(layer, state, target, 27, 26), then v7 = 27, v11 = 29. +320: sub_1403B5170(layer, state, rect, target, v11, v7), then v7 and v11 exchange and a v11 equal to 26 becomes 29. +484: only when layer+80 == 0 is sub_1403AEE0C called (with v11, v7, and the flag +492 == 0); the exchange happens either way. +486: sub_1403B53C8(layer, state, target, v11, v7), then the exchange. +176: UIBlur_Run(layer, target, type, 30, 1, radius +180, rect, clamp, v11, v7, 28, -1), then the exchange. After an exchange the index 26 is replaced by 29 (for +320 only on the new v11; for +484, +486 and +176 on both v7 and v11), so 26 is never reused as a destination.
- V: +177 and not +486: GUILayer_CopyToTarget(layer, state, rect, target, junk, v7) copies the current scratch RT into the shadow scratch, then GUILayer_BlurShadowPass(layer, state, targetType, rect, clamp, target); there is no exchange after them (the layer's pixels stay in RT v7). The fourth argument of both is target = UILayer_GetTarget(layer).
- V: then the sort key is set to 0x6AC07600 and GUILayer_BlitFinal(layer, state, target, the rectangle at layer+240, junk, v7) draws RT v7 onto the target; last, when +178 is set and +486 is clear, GUILayer_GlowPass(layer, state, targetType, rect, clamp, target, v11, junk, junk, v7).
- V: flag bytes: layer+176 / +177 / +178 = BuildRecord record+152 / +153 / +154 (layer+k = record+(k-24); the layer array base is r + 303480 + 592 * index), i.e. +176 = the single float group (comp+96 -> ctx+112, radius layer+180), +177 = the drop-shadow group (comp+120 -> ctx+136: strength +184, radius +188, offset +192 / +196, colour +456..+464), +178 = the glow group (comp+172 -> ctx+156: strength +200, radius +204, colour +468.., mode +480).
- V (live read of the running Job Tree, 2026-10-29: layer bytes and census/trace hits): the Job Tree uses the +177 group: its title layer has +177 = 1, +176 = 0, +178 = 0; GUILayer_BlurShadowPass and GUILayer_CopyToTarget are hit for that layer while sub_1403B5170, sub_1403AEE0C, sub_1403B53C8 and GUILayer_GlowPass are not (see also GUILayer_EffectPass0, which records the same layer's flags).

## State touched

- Calls: [GUILayer_EffectPass0](GUILayer_EffectPass0.md), [sub_1403B5170](sub_1403B5170.md), [UIBlur_Run](UIBlur_Run.md), [GUILayer_CopyToTarget](GUILayer_CopyToTarget.md), [GUILayer_BlurShadowPass](GUILayer_BlurShadowPass.md), [GUILayer_BlitFinal](GUILayer_BlitFinal.md), [GUILayer_GlowPass](GUILayer_GlowPass.md), [UILayer_GetTarget](UILayer_GetTarget.md)
- Reads: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The +178 group is the component glow (flag +178, strength +200, radius +204, colour +468.., mode +480) by the constant 24 offset to the BuildRecord page. Of the +176 / +177 groups the Job Tree uses +177, the drop shadow (live read above).

## Open questions

? what the +489 / +320 / +484 / +486 groups draw (their passes were not decompiled here). ? where layer+36 / +492 (the source-layer reference of the +489 pass) are set.
