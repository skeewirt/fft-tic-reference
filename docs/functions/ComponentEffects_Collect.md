# ComponentEffects_Collect

- **Address:** `0x1403E809C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 ComponentEffects_Collect(UIRenderer *r, ComponentCtx *ctx)`
- **Callers:** ComponentLayer_Begin
- **Callees:** Matrix2x3_Multiply, GUIWidget_FindComponentCached, GUIWidget_FindComponentByName, GUIWidget_FindResourceByName, GUINode_FindNthPartByKind, UIImage_ResolvePart, GUIFontSlots_GetTextureRect, roundf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies every enabled effect group of the component's property block into the draw context and reports whether an offscreen layer is needed.

## Behavior

- V: component = ctx+496. Blend type comp+16 (0 = none). Effect groups (runtime offsets in the component; each has an enable byte): +60 colour transform (mul comp+28..+40, add +44..+56 unless identity); +88 six floats +64..+84; +96 single float +92 (> 0); +120 floats +100/+104 (> 0) with a qword +108 and +116; +172 two floats +156/+160 (> 0) with colour +164 and mode +168 (this is the group the UnitSelect ring enables); +186 floats +176/+180 (> 0) with size comp+336/+340; +192 opacity float +188; +216 clip rectangle (margins +196..+212, size +336/+340); +244, +265.
- V: each enabled group sets its flag byte in the context (+76, +104, +112, +136, +156, +178, +184, +296) and makes the result 1 = a layer is required.
- V: colour transform (comp+60 set and not the identity): ctx+76 = 1, ctx+44..+59 <- comp+28..+43 (multiply), ctx+60..+75 <- comp+44..+59 (add). Offsets group (comp+88 set and any of comp+64..+84 non-zero): ctx+104 = 1, ctx+80..+103 <- comp+64..+87. Single float (comp+96 set and comp+92 > 0): ctx+112 = 1, ctx+108 <- comp+92.
- V: drop-shadow group: when comp+120 != 0 and (comp+100 > 0 or comp+104 > 0): ctx+136 = 1, ctx+116 <- comp+100 (blur radius), ctx+120 <- comp+104 (strength), the qword ctx+124 <- comp+108 / +112 (offset x / y), ctx+132 <- comp+116 (colour rgb, alpha 0xFF).
- V: glow group: when comp+172 != 0 and (comp+156 > 0 or comp+160 > 0): ctx+156 = 1, ctx+140 <- comp+156, ctx+144 <- comp+160, ctx+148 <- comp+164 (colour), ctx+152 <- comp+168 (mode). The +186 group (comp+186 set and comp+176 > 0 or comp+180 > 0): ctx+178 = 1, ctx+160 <- comp+176, ctx+164 <- comp+180, ctx+176 <- byte comp+184, ctx+177 <- byte comp+185, ctx+168 / +172 = half the size comp+336 / +340 mapped through the matrix at ctx+504. Group comp+192: ctx+184 = 1, ctx+180 <- comp+188.
- V (read 2026-10-30, decompile; checked against a live Job Tree frame): the mask group (comp+244): the Mask node is the first kind 9 node of the component's tree (GUINode_FindNthPartByKind(comp+272, 9, 0)); when it exists and its bytes +144 and +153 are set, an image mask is used when node+244 (font slot) is non-zero or its image name at node+216 resolves in the widget (ctx+384 = 1, no extra layer), otherwise the mask component named by node+248 / +264 (cache cell node+288) is stored (ctx+409 = 1, ctx+392 = component, ctx+400 = node, ctx+408 = node+280). With no usable Mask node the component's own name keys comp+224 (image) / comp+248 (component) are tried the same way. A component mask makes ComponentLayer_Begin draw that component into an extra layer record first (ComponentLayer_DrawMaskComponent). The +265 group clears ctx+296 / +384 / +409 again. The result is 1 also when the u16 comp+552 (layer id) is non-zero.

## State touched

- Calls: [Matrix2x3_Multiply](Matrix2x3_Multiply.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUIWidget_FindComponentByName](GUIWidget_FindComponentByName.md), [GUIWidget_FindResourceByName](GUIWidget_FindResourceByName.md), [GUINode_FindNthPartByKind](GUINode_FindNthPartByKind.md), [UIImage_ResolvePart](UIImage_ResolvePart.md), [GUIFontSlots_GetTextureRect](GUIFontSlots_GetTextureRect.md)

## Referenced by

- Called by: [ComponentLayer_Begin](ComponentLayer_Begin.md), [GUIComponentRef_Draw](GUIComponentRef_Draw.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

Only the head (the effect-group copies, lines up to the clip rectangle) of this 15 KB function was read. V (decompile, label LABEL_58, + live backtrace of the Job Tree title): for a component whose property block carries a Mask node (the TextMask component), it resolves the mask component by the node's two name keys (+248 / +264, cache cell +288) with GUIWidget_FindComponentCached and stores it in the draw context: ctx+409 = 1, ctx+392 = the mask component, ctx+400 = the Mask node (used as its property block). ComponentLayer_Begin then draws that component into its own layer first (ComponentLayer_DrawMaskComponent). The context groups feed GUILayer_BuildRecord one to one (shadow: ctx+136 -> record+153 = layer flag +177).

## Open questions

The remaining part (clip rect maths and flags) is not documented (?); how the Mask node is found among the component's nodes and what its other fields (+208..+216) do. ? whether the comp+192 group (ctx+184, ctx+180) is an opacity or a whole-layer blur radius: GUILayer_BuildRecord scales it by the pixel scale into layer+500, which GUILayer_BlurEffect reads as a radius, while GUICore_DrawWidget only draws the component when comp+188 > 0.
