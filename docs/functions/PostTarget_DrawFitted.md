# PostTarget_DrawFitted

- **Address:** `0x1403CB9C4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 sub_1403CB9C4(PostTargetDesc *desc, float width, float height, int filterMode, char stretch)`
- **Callers:** CharaRenderer_PostFrame, sub_1402F3284
- **Callees:** sub_14003E120, sub_14003E228, sub_1403C043C, sub_1403CC204, ShaderSelector_SetDigit, ShaderSelector_Apply, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one textured quad from a render-target descriptor (136-byte entries at unk_142C819D0) into the current UI render target, fitted into the 16:9 area of the window, with the layer-composite selector #9 in permutation digit 0 = 18.

## Behavior

- V: the current render target = the object at g_Renderer + 8 * (byte g_Renderer+13754) + 6560 (0 when the byte is 0xFF); its u16 width / height at +20 / +22 give W / H.
- V: maps the descriptor's constant buffer (desc+56) and fills the cUIRender layout like UILayer_FillConstants: rows 0-3 and 4-7 = the two pixel-to-clip matrices (scale 2/W, -2/H; atlas offset 0), +128 = 0, +136 = the float at desc+112, +144 (row 9) = (1, 1, 1, 1), +548 (34.y) = 18, +552 = (0, 0), +568 / +572 (35.zw) = 2.6 / 2.6, and zeros for the other rows UILayer_FillConstants writes (rows 36 and 37 are not written). The buffer is committed and bound at constant-buffer slot short(desc+40).
- V: the destination rectangle comes from sub_1403CC204(&rect, (int)width, (int)height, stretch): with the display size read from the object pointed to by (qword_140C696A8 + 88) (dwords +40 / +44) it takes the 16:9 box that fits the display (pillarbox or letterbox, centred), scales the source by box height / height, and the width is box width when stretch != 0, else width * that scale; rect = (left, top, right, bottom) in display pixels.
- V: maps the vertex buffer (desc+72) and writes four 16-byte vertices (x, y, u, v): (left, top, 0, 0), (right, top, width / desc+116, 0), (left, bottom, 0, height / desc+120), (right, bottom, width / desc+116, height / desc+120): the top-left width x height part of the descriptor's source texture is stretched to the rectangle (desc+116 / +120 = the source texture size).
- V: selector = the UI manager's selector #9 (+72); skipped when it is null. ShaderSelector_SetDigit(sel, 0, 18), SetDigit(sel, 1, 0); default sampler words copied; ShaderSelector_Apply(sel, state, 0).
- V: sampler word = dword_141D8BC7C with bits 0x3C0 cleared when filterMode == 0, bits 0x3C0 set to 0x240 when filterMode == 1, unchanged otherwise (top bit cleared); stored at state + 5704 + 4 * slot for the sampler slots short(desc+42) and short(desc+44).
- V: texture = the object at g_TextureTable + 8 * dword(desc+16) + 8 (+40 member, 0 when null), bound as texture slots short(desc+46) and short(desc+48) (state + 1608 + 8 * slot).
- V: state: +136 = desc+64, +200 = the +40 member of the object at desc+72, +208 = 16 (stride), +6016 = 0, +128 = desc+80, +124 = (& 0xFFC06FFF) | 0x6000; clip enable: state+112 |= 0x10 with the rectangle copied to state+80; a 96-byte command is allocated with sub_140069A38(state, 5, 96) (the layer passes pass 4 there) and its header words are written +4 = 4, +8 = 0, +12 = 0 (the layer passes write +8 = 4, +12 = 0), packed and submitted; afterwards the 0x10 clip bit is cleared again. The draw writes the render target that sub_1403CB8BC installed (state+96 / +144 = the current UI target, previous state+96 saved at desc+0).
- V: callers: CharaRenderer_PostFrame passes (descriptor unk_142C819D0 + 136 * v5, its second argument, the target height as float, the value at 0x142E7FC70 when dword_142E7FC68 != 0 else 0, a stretch flag that is 1 only when dword_142E7FC68 == 7 and dword_142E7FC6C == 0); sub_1402F3284 passes (unk_142C819D0, ..., (float)v6, the value at 0x142E7FC70, 0).

## State touched

- Calls: [ShaderSelector_SetDigit](ShaderSelector_SetDigit.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [UIManager.selector_9](../structs/UIManager.md#selector_9), [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md), [g_Renderer](../globals/g_Renderer.md), [g_TextureTable](../globals/g_TextureTable.md)
- Writes: [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer)

## Notes

Proposed name: PostTarget_DrawFitted. The two float arguments arrive in xmm1 / xmm2 (the IDB prototype shows the second argument as an unused integer a2 and only the third as a float). It is the final present-style quad of the unit-renderer post chain (CharaRenderer_PostFrame calls sub_1403CB8BC to set the target, then this). sub_1403CC204 (proposed UIRect_Fit16x9) is the rectangle helper. The scan that listed this function as referencing the layer record's shadow colour offset (303936) does not hold: the decompile and the disassembly contain no such displacement; that offset occurs only in GUILayer_BuildRecord.

## Open questions

? what digit-0 value 18 of selector #9 draws (which pixel shader / blend variant; UILayer_FillConstants feeds layer+32 to the same digit). ? what dword_141D8BC7C is and why bits 0x3C0 = 0x240 are set for filterMode 1 (probably a point / linear filter choice). ? the meaning of the value at 0x142E7FC70 / dword_142E7FC68. ? the descriptor fields +80, +112 and +116 / +120's producer.
