# RenderContext_ResetFrame

- **Address:** `0x140087C50`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall RenderContext_ResetFrame(RenderDevice *dev)`
- **Callers:** App_RunFrame
- **Callees:** sub_140069A38 (command allocate), sub_140069980 (command submit)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Start-of-frame reset of the renderer: clears the command-memory counters and puts every 6032-byte render context (the per-thread state the other sheets call the thread state) back to its default pipeline state, with empty binding tables and the default sampler word in all 64 sampler slots.

## Behavior

- V: dev = qword_140C696A8, the only argument its single caller passes. App_RunFrame calls it after sub_1400206FC, between the vtable slot +56 and the vtable slot +64 calls on the object at app+1152; the return value is not used.
- V: first it sets the three dword counters at dev+5144, +5148 and +5152 to 0 (atomic exchanges) and the byte at dev+5106 to 0.
- I: these are the command-memory pool counters. Basis: sub_140069A38 adds 0x2000 per 8 KB command block to +5144 and +5148, sub_140069980 adds 0xC00 to +5144 and 0x400 to +5152 per 1 KB list group, and both set dev+5106 and give up when the pool at dev+5120 (limit dev+5108) is exhausted; sub_140088280 (called later in App_RunFrame) switches dev+5120 between the two halves of the pool, dev+5112 and dev+5112 + dev+5108.
- V: then it loops over the dev+5088 (dword count) contexts of the array at dev+4984, stride 6032, and rewrites every context as listed in the next bullets (all offsets are inside the context). UIRender_GetThreadContext divides a context address by 6032 to find its index.
- V: command list fields: +8 (qword, the sort key stored with every submitted command) = 0; +16 = 0; +24 = 0; +40 = the address of +32; +48 = 0x8000; +52 = 0x2000; +56 (qword) = 1, which also clears the dword at +60; +64 = 0; +72 = 0. +32 is not written.
- I: +24 / +52 are the current 8 KB command block and the bytes used in it (0x2000 = full, so the next command allocation takes a fresh block); +32 / +40 are the head and the write pointer of the list of {sort key, command pointer} entries that sub_140069980 keeps in 1 KB groups; +56 is the entry count left before the next group and +60 the group count. Basis: the code of sub_140069A38 and sub_140069980.
- V: +80..+95 (four dwords) = 0, 0, 0x7FFFFFFF, 0x7FFFFFFF (an IDB constant) and +96 (qword) = 0.
- I: +80 is the clip rectangle (x0, y0, x1, y1), reset to unbounded; +96 / +144 hold the render target object and its handle. Basis: GUILayer_CopyToTarget and GUILayer_BlurShadowPass copy a rectangle to +80, set the clip-enable bit 0x10 in +112 and store the target at +96 / +144.
- V: +104 (qword): the low 5 bits are first set to 0xF, then the qword becomes qword_1407C28F0 (0xFFFF00001C000000 in the IDB) except for the bits covered by the mask 0x100001FFF (bits 0..12 and bit 32), which keep their current value. After the reset bits 0..4 are 0xF, bits 5..12 and bit 32 are unchanged and every other bit comes from the constant. UIRender_ApplyDrawState and UICommandRing_Flush use the same mask on the old value of +104.
- V: +112 (qword) = qword_1407C28F8 with bits 13..15 cleared (0x27 in the IDB); +120 (dword) = dword_1407C28E0 (0x78020010 in the IDB); +124 (dword) = 0x1003.
- I: +112 is the raster / flags word and +124 a state flag word whose bit fields the other sheets edit (the draw type bits; bits 9..11, which GUILayer_BlurShadowPass sets from the render target and BlendDesc_FromWords reads as the number of extra blend words); +120 is the render-target-0 blend word, which here has the enable bit clear and the write mask 0xF. Basis: UIRender_ApplyDrawState, BlendDesc_FromWords and GUILayer_BlurShadowPass.
- V: bindings: +128, +136, +144 (qwords), +152..+199 (48 bytes) and eight 16-byte slots from +200 up to +327 are zeroed (the loop writes the qword at +200 + 16 * k and the qword at +208 + 16 * k).
- I: +128 is the index buffer (UICommandRing_Flush stores ring+32, the index buffer object of UIRender_CreateBuffers, there); +136 is a second object the passes set per draw (ring+8 in Flush, element [1060] of the UI manager in GUILayer_BlurShadowPass; its role is open); +200 + 16 * k is the handle of vertex buffer k with its stride at +208 + 16 * k and its byte offset at +212 + 16 * k (Flush fills slots 0 and 1, GUILayer_BlurShadowPass slot 0).
- V: binding tables: +328..+1607 (0x500 bytes, 160 qwords) and +1608..+5703 (0x1000 bytes, 512 qwords) are cleared with memset.
- V (UIRender_CreateBuffers, UICommandRing_Flush, UIRender_ApplyDrawState): the first table is indexed by constant-buffer slot ids (cUIRenderRemap at ring+64 and cSDF at ring+68: handle at +328 + 8 * slot) and the second by texture slot ids (tTexture0 at ring+72: handle at +1608 + 8 * slot); both id sets come from NameSlotTable_Lookup.
- V: sampler words: all 64 dwords +5704..+5959 (+5704 + 4 * slot, slot = the id from the sampler name table) are set to dword_141D8BC7C & 0x7FFFFFFF, the default sampler word.
- V (live read 2026-10-30): the default word is 0 at runtime (the IDB image holds 0xFFFFFFFF, which would store 0x7FFFFFFF). After the reset every sampler slot therefore holds 0: point filter, WRAP addressing, MinLOD = MaxLOD = 0 (Sampler_DescFromWord).
- V: +5964..+5991 (seven dwords) = dword_1407C28E0 & 0x7FFFFFFF.
- I: these are the blend words of render targets 1..7 (BlendDesc_FromWords reads st+5964 + 4 * (i - 1)); together with +120 all eight targets start with blending off and write mask 0xF.
- V: +5992..+6007 (four floats) = 1.0, 1.0, 1.0, 1.0; +6008 = 0; +6012 = 0; +6016 (qword) = 0; +6024 (qword) = 0.
- I: +5992 is the blend factor colour; +6016 is a field the draw passes clear before packing a command (GUILayer_BlurShadowPass, UICommandRing_Flush). Basis: those sheets.
- V: +6008 is read by RenderState_PackCommand (at 0x14003A39E), not by BlendDesc_FromWords; I (ShaderProgram_ApplyState sheet): bit i marks a render target whose blend word uses the blend factor, and the packer then appends the colour at +5992.
- V: after the loop, when dev+32 <= dev+36 (unsigned dwords) and the member at (*(dev+88)) + 120 is non-null: a 32-byte command of kind 0 is allocated on context 0 (the first array element) with sub_140069A38, command +8 = the qword at (that member) + 40, command +16 (16 bytes) = all ones, and it is submitted with sub_140069980 under the sort key 0 (+8 of context 0, cleared above).
- V (sub_140088280): dev+32 is a frame counter incremented there modulo 2^31 (when the dword at dev+8 is 1).
- V (2026-10-30): kind 0 is the clear-target command: its executor RenderCommand_ClearTarget calls ClearRenderTargetView on the view in the second qword with the 16 colour bytes at +16 (here all ones = (1, 1, 1, 1); GUILayer_Composite fills them with zeros for the layer targets). I: the member is a render target handle of the main window object.

## State touched

- Reads: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md)
- Writes: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.blend_factor](../structs/RenderContext.md#blend_factor), [RenderContext.command_block](../structs/RenderContext.md#command_block), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words) all 64 slots = default, [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.blend_rt1_7](../structs/RenderContext.md#blend_rt1_7)

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md)

## Notes

The name is ours (IDB: sub_140087C50 until applied). sub_14003A048 (the initialiser of a fresh context) reads the same default sampler word. The constants named above are IDB values; only dword_141D8BC7C was read live (0 at runtime), the others were not re-read.

## Open questions

? what dev+36 is and whether the kind-0 command is queued every frame or only while the frame counter has not passed it; what the all-ones payload means (colour or mask). ? the meaning of +16, +48, +64, +72, +6012 and +6024 of the context (+48 and the zeroed qwords are not read by the two command helpers). ? whether the IDB values of qword_1407C28F0, qword_1407C28F8, dword_1407C28E0 and the 1.0 vector are the runtime values (dword_141D8BC7C is not).
