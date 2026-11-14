# GUILayer_BuildRecord

- **Address:** `0x1403E6728`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUILayer_BuildRecord(UIRenderer *r, int layerIndex, ComponentCtx *ctx)`
- **Callers:** GUILayer_Select (called by the ComponentLayer_Begin chain)
- **Callees:** UIPartRef_GetTextureSize, UIPartRef_GetResource

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one 592-byte offscreen-layer record from a component draw context: size, blend, colour transform and every enabled effect.

## Behavior

- V: layer records live at r + 303504 + 592 * index (512 slots); +0/+2 = target size (r+184, r+188); +8 = blend type; +154 (byte) = glow enabled (ctx flag +156 AND the renderer feature byte r+606623); +176 (float) = glow strength = ctx+144; +180 (float) = glow radius = min(ctx scale x, y) * ctx+140; +444/+448/+452 = glow colour bytes / 255 (ctx+148..150); +456 = glow mode (ctx+152: 0 -> 3, 1 -> 1, 2 -> 2, any other value -> 3).
- V: the layer object that GUILayer_ApplyEffects and its passes receive is the record minus 24 bytes: for every slot GUIRenderer_ResetFrame initialises the index dword at r + 303492 + 592 * i (= layer+12 with layer = r + 303480 + 592 * i) and the target pointer at r + 304064 + 592 * i (= layer+584, the field UILayer_GetTarget reads), so layer+k = record+(k-24): record+152 / +153 / +154 = layer+176 / +177 / +178 and record+432..+440 = layer+456..+464. The ctx scale x / y used below are the floats at ctx+528 / +532 (the code indexes them as int elements 132 / 133); 'min scale' = the smaller of the two.
- V: drop-shadow group (ctx flag +136 AND the renderer feature byte r+606624): record+153 = 1 (layer+177), record+160 = the raw dword ctx+120 (strength, layer+184), record+164 = fabs(min scale * float ctx+116) (blur radius, layer+188), record+168 / +172 = ctx+124 * scale x / ctx+128 * scale y (offset in pixels, layer+192 / +196), record+432 / +436 / +440 = bytes ctx+132 / +133 / +134 divided by 255 (colour rgb, layer+456..+464). With the flag clear, only record+153 = 0 is written.
- V: other effect groups copied the same way, with their gates: colour transform ctx flag +76: record+64 / +80 <- the multiply / add blocks ctx+44 / ctx+60 (defaults 1,1,1,1 and 0 when clear); offsets group ctx flag +104 (no feature byte): three float pairs ctx+80.. each scaled by scale x / y into record+96 / +104 / +112 (layer+120 / +128 / +136); single float group ctx flag +112 AND r+606622: record+152 = 1 (layer+176), record+156 = min scale * ctx+108 (layer+180, the blur radius GUILayer_ApplyEffects passes to UIBlur_Run); ctx+178 group with r+606627: record+462 = 1 (layer+486) and the data block at record+480..+531 (three 16-byte blocks and a dword); ctx flag +184: record+4 = 1 and record+476 = min scale * ctx+180 (layer+500); clip ctx+296: four edge entries at record+232.. ; ctx+409: record+465 = 1, record+466 = ctx+408; ctx+412 with ctx+554 and r+606626: record+460 = 1, record+461 = ctx+413.
- V: ctx+384 with a non-empty part reference at ctx+336: texture and rectangle data from UIPartRef_GetTextureSize / UIPartRef_GetResource go to record+296 (flag) .. record+431.
- V: at the end 488 bytes of the context (ctx+0..+487) are copied to r + 512 * index + 41336, ctx+548 (layer id field) to r + 512 * index + 41840 and a byte 'any effect or blend active' to r + 512 * index + 41844; the function returns ctx+548.

## State touched

- Calls: [UIPartRef_GetTextureSize](UIPartRef_GetTextureSize.md), [UIPartRef_GetResource](UIPartRef_GetResource.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)
- Writes: [GUILayer.blend_mode](../structs/GUILayer.md#blend_mode), [GUILayer.offset_vectors](../structs/GUILayer.md#offset_vectors), [GUILayer.shadow_strength](../structs/GUILayer.md#shadow_strength), [GUILayer.shadow_radius](../structs/GUILayer.md#shadow_radius), [GUILayer.shadow_offset](../structs/GUILayer.md#shadow_offset), [GUILayer.shadow_colour](../structs/GUILayer.md#shadow_colour), [GUILayer.glow_strength](../structs/GUILayer.md#glow_strength), [GUILayer.glow_radius](../structs/GUILayer.md#glow_radius), [GUILayer.glow_mode](../structs/GUILayer.md#glow_mode), [GUILayer.rect](../structs/GUILayer.md#rect)

## Referenced by

- Appears in flows: [LayerDropShadow](../flows/LayerDropShadow.md)
- Called by: [GUILayer_Select](GUILayer_Select.md)

## Notes

Live check (read-only, UI renderer = [[g_GUICore]+208]): the Job Tree ring layer reads glow 1 / strength 0.8 / radius 4.0 (= 6.0 * 2/3) / colour (1.0, 0.937, 0.702) / mode 3, target 1280x720; three other layers read strength 0.5, radius 2.667 (= 4.0 * 2/3), white, mode 3. Feature-byte gates (V): single float r+606622, glow r+606623, shadow r+606624, ctx+412 group r+606626, ctx+178 group r+606627; the colour transform, the ctx+104 offsets group and the ctx+184 group are not gated.

## Open questions

Meaning of the modes 1/2/3 in the compositor (?). ? what the renderer feature bytes r+606622..r+606627 mean and where they are set. ? the exact role of the ctx+178 group (record+462 = layer+486) and of the data block it fills (record+480..+531).
