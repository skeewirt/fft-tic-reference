# UILayer_FillConstants

- **Address:** `0x1403B08AC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char UILayer_FillConstants(UILayer *layer, __int64 a2, __int64 a3, __int64 a4)`
- **Callers:** GUILayer_Composite
- **Callees:** UILayer_GetTarget, sub_14003E120, sub_14003E228, sub_1403C043C, sub_1403BFC48, sqrtf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the layer shader's constant buffer from the layer object (matrices, colour transform, effect values, texture size reciprocals). Offsets below are byte offsets in the mapped buffer; row = offset / 16.

## Behavior

- V: the buffer is the cUIRender cbuffer: 608 bytes = 38 rows of 16 bytes (size and field types read from the DXIL metadata of the UIRender.tec shaders: 2 x [4 x float4], float2, float, float, float4, float4, float2 x 4, floats, ints ...). W / H below = the u16 width / height at +20 / +22 of UILayer_GetTarget(layer).
- V: rows 0-3 (+0..+63) = a pixel-to-clip matrix (scale 2/W and -2/H, translation (2 * atlasX / W - 1, 1 - 2 * atlasY / H) with the atlas offset (layer+224, layer+228)); rows 4-7 (+64..+127) = the same scale with the fixed translation (-1, +1) and no atlas offset; both go through sub_1403C043C. The vertex shader 035438 reads rows 4-7 (V, shader disassembly).
- V: +128 qword = layer+224 / +228 (atlas offset, pixels; row 8.xy); +136 = 1.0f when layer+28 == 1, else the float at (UI manager + 144) (row 8.z); +140 = the float at +144 of the object at (qword_140C696A8 + 88) when its byte +157 is set, else 400.0f (row 8.w).
- V: +144 / +160 = layer+88..+103 and layer+104..+119 (rows 9 and 10): the colour multiply and add blocks (defaults 1,1,1,1 and 0; GUILayer_BuildRecord fills them from ctx+44 / ctx+60, which ComponentEffects_Collect copies from comp+28 / comp+44).
- V: +176 / +184 / +192 (rows 11.xy, 11.zw, 12.xy) = (-layer+120 / W, -layer+124 / H), (-layer+128 / W, -layer+132 / H), (-layer+136 / W, -layer+140 / H): the three pixel offset vectors of the comp+88 group converted to UV and negated; GUILayer_BlitFinal switches shader digit 1 on when any of them is non-zero.
- V: shadow group: +200 qword = layer+192 / +196 (shadow offset in pixels; row 12.zw); +208 = layer+184 (shadow strength; row 13.x); +496 / +500 / +504 = layer+456 / +460 / +464 (shadow colour rgb; row 31.xyz). Glow group: +212 = layer+200 (glow strength; row 13.y); +512 / +516 / +520 = layer+468 / +472 / +476 (glow colour rgb; row 32.xyz).
- V: +216..+244 (rows 13.zw, 14, 15.xy) = layer+144..+172 copied raw (eight floats; UILayer_Ctor defaults 0.4, 1.0, 0.08, 0.5, 1.0, 1.0, 0.04, 0.5); +248 = byte layer+490 as int (15.z); +252 = (byte layer+320 != 0) (15.w); +256..+271 = layer+336..+351 (row 16); +272 / +276 = layer+352 / W, layer+356 / H and +280 / +284 = layer+360 / W, layer+364 / H (row 17).
- V: distance-mask rows: for i = 0..3, +320 + 16i = (byte layer+256 + 16i != 0) as int (rows 20-23 .x, the entry enable), +324 + 16i = raw dword layer+260 + 16i (rows 20-23 .y, a curve index 1 / 2 / 3 in the pixel shader), +384 + 16i = layer+264 + 16i divided by e (rows 24-27 .x), +388 + 16i = e divided by layer+268 + 16i (rows 24-27 .y) with e = layer+404 for i < 2 and layer+400 otherwise (infinity when the divisor is below 1.2e-7), and +392 + 16i / +396 + 16i = layer+192 / W and layer+196 / H (rows 24-27 .zw: the shadow offset in UV).
- V: two quad-edge sets: +448 qword = layer+368 (28.xy), then with P0 = layer+376, P1 = layer+384, P2 = layer+392 the lengths |P1-P0| and |P2-P0| at +456 / +460 (28.zw) and their unit vectors (sub_1403BFC48) at +464 / +472 (29.xy, 29.zw), +480 qword = layer+448 (30.xy), +488 qword = layer+408 (30.zw); the second set: +288 qword = layer+416 (18.xy), P0 = layer+424, P1 = layer+432, P2 = layer+440, lengths +296 / +300 (18.zw), unit vectors +304 / +312 (19.xy, 19.zw).
- V: +544 = 2 when byte layer+491 is set else 0 (34.x); +548 = layer+32 (34.y, the digit-0 value GUILayer_BlitFinal gives the selector); +552 qword = (layer+224 / W, layer+228 / H) (34.zw, the atlas offset in UV); +560 qword (35.xy) = 0, or when layer+489 and layer+492 are set and (int)layer+36 >= 0 the second atlas offset of the source layer (manager layer array at +216) minus layer+224 / +228, divided by W / H; +568 qword (35.zw) = (layer+576 * 2.6, layer+580 * 2.6); +576 (row 36) = (0, 0, 1, 1), or in that same +489 case the source layer's rectangle in UV inset by half a pixel; +592 (row 37) = this layer's rectangle (layer+208..+220) in UV inset by half a pixel: ((x + 0.5) / W, (y + 0.5) / H, (x + w - 0.5) / W, (y + h - 0.5) / H).
- V: not written by this function: bytes 508, 524 and 528..543 (31.w, 32.w, 33.x..33.w). At the end the buffer is committed (sub_14003E228), stored in the thread state's constant-buffer table at slot short(layer+72) and layer+572 is set to 1 (cleared at entry); returns 1, or 0 when the buffer could not be mapped.
- V (shader disassembly): the shadow composite pixel shader 035E50 reads cb13.x (strength), cb31.xyz (colour), cb34.zw (atlas offset added to the sample uv) and, when cb20.x != 0, the distance-mask rows 20-30; the vertex shader 035438 reads cb12.zw (offset pixels added to the quad position) and rows 4-7; pixel shader 0349C0 reads cb37.zw (the clamp corner).

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md)
- Reads: [GUILayer.shadow_strength](../structs/GUILayer.md#shadow_strength), [GUILayer.shadow_offset](../structs/GUILayer.md#shadow_offset), [GUILayer.shadow_colour](../structs/GUILayer.md#shadow_colour), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.offset_vectors](../structs/GUILayer.md#offset_vectors), [GUILayer.glow_strength](../structs/GUILayer.md#glow_strength), [GUILayer.blend_mode](../structs/GUILayer.md#blend_mode), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles)

## Referenced by

- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The row / field layout is the cUIRender struct recovered from the UIRender.tec shader metadata (types only, no field names), matched to the writes here. sub_1403CB9C4 (proposed name PostTarget_DrawFitted) fills the same buffer layout for a plain textured quad.

## Open questions

? meaning of the eight floats layer+144..+172 and of layer+336..+364 (rows 13.zw..15.xy, 16, 17). ? what layer+490 / +491 select. ? which shaders consume the second quad-edge set (rows 18-19) and layer+416. ? what the float at (UI manager + 144) and the config float for row 8.w are.
