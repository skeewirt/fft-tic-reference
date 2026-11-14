# ComponentLayer_DrawMaskComponent

- **Address:** `0x1403E647C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char ComponentLayer_DrawMaskComponent(UIRenderer *r, ComponentCtx *ctx)`
- **Callers:** ComponentLayer_Begin
- **Callees:** sub_1403E9218, GUILayer_ResetRecord, ComponentDrawContext_ComputeMatrix, Matrix2x3_Multiply, sub_1403E9A2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a component's mask component (ctx+392, with the Mask node as its property block ctx+400) into a fresh layer record; called by ComponentLayer_Begin the first time a layer with a mask is opened.

## Behavior

- V: returns 0 when the mask component is not loaded (+416 = 0) or hidden (+192 set and opacity +188 <= 0), or when the layer list is full (r+606584 + 2 >= 511). Otherwise sub_1403E9218 and GUILayer_ResetRecord prepare a layer record, the draw context is copied (0x258 bytes) and the mask component becomes its component (+496).
- V: when the Mask node is present its matrix is ComponentDrawContext_ComputeMatrix(component, m, scale, node) times the context matrix (+504), the scale and opacity are multiplied in, the node colour (+196) is multiplied into the context colour (+540 / the colour dword) and the node's +200 is added to the layer order (+544).
- V: sub_1403E9A2C draws the component's children (GUINode_DrawChildren at component +272) into the new layer; returns 1 when that produced a layer (the layer flag byte is set).
- V (disassembly and decompile, 2026-10-30): the copied context has the depth byte ctx+552 incremented and ctx+553 set to 1 ('the context already carries a layer'), so no component inside the mask opens a layer of its own (ComponentLayer_Begin returns 0 at once); the whole mask component is drawn into the one fresh record. The function returns 0 when the draw counter r+606592 is not positive afterwards (nothing was drawn), otherwise it sets the byte layer+487 of that record to 1: this is THE writer of the mask-layer flag +487 that the atlas sheets could not find (the flag is the high byte of the record's dword at record+484). The record itself is made by GUILayer_ResetRecord, not by GUILayer_BuildRecord: the effect groups of the mask layer are all off and the 488-byte context copy of its slot (r + 512 * slot + 41336) is not rewritten (it keeps the bytes of an earlier frame).
- V (live 2026-10-30, Job Tree frame): the TextMask component of the main tab draws its mask component TextBoard01 into slot 4 (+487 = 1, dirty (20, 11, 102, 44)); the next slot 5 holds TextMask itself (+489 = 1, drop shadow, ctx+409 = 1 and ctx+392 = the mask component pointer, the only component pointer the layer records contain); the atlas read +16 = 5, +20 = 0 for slot 4 and the secondary shelf {178, 0, 124, 0} (the model of LayerAtlasPlacement step 7: margin 32 from the stale radius bytes of the reset record, 114 + 64 = 178, 60 + 64 = 124).

## State touched

- Calls: [GUILayer_ResetRecord](GUILayer_ResetRecord.md), [ComponentDrawContext_ComputeMatrix](ComponentDrawContext_ComputeMatrix.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)
- Writes: [GUILayer.effect_flags](../structs/GUILayer.md#effect_flags)

## Referenced by

- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The name is ours. Live (debugger backtrace at the Job Tree title's GUITextNode_Draw): GUIComponentRef_Draw (TextMask reference) -> ComponentLayer_Begin -> this function -> GUINode_DrawChildren -> GUITextNode_Draw, so the title text is drawn into the mask layer, not into the screen. Live: every glyph record of the title text (node+328, 36 bytes each, byte +28) has the bold run flag = 1.

## Open questions

How the layer record this creates is consumed by the effect pass (GUILayer_EffectPass0): which slot holds it and how the shader combines it with the gradient layer. The mask layer's stale radius floats (+180 / +188 / +500 of a reset record) decide its atlas margin (live: 10.0 gave 32); whether that is intended is not known (?).
