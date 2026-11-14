# UIRender_LoadShaders

- **Address:** `0x1403B7188`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char __fastcall UIRender_LoadShaders(__int64 ui)`
- **Callers:** sub_1403A143C (V: single xref)
- **Callees:** sub_1403A7AD8, sub_140091124 (load .tec), sub_1403A7B08, UIRender_CreateBuffers, UICommandRing_Reset, sub_14008C5D8, sub_140086DE4, sub_140086F64, sub_140089280, sub_1403B7E2C, sub_1403B7F64, sub_1403AE954, sub_1403B7888 (cleanup)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the five UI shader containers and creates the UI renderer, its command ring, the SMAA / down-sampling helpers and their constant buffers.

## Behavior

- V: first calls sub_1403A7AD8(ui); 0 -> returns 0. Then loads, via sub_140091124(qword_143CD9B88, name, hash, 0, opts), each container and stores it at ui+offset: 'shader/UIRender.tec' -> +24, 'shader/SMAA.tec' -> +32, 'shader/RadialBlur.tec' -> +40, 'shader/BahamutEffect.tec' -> +48, 'shader/DownSampling.tec' -> +56; each followed by sub_1403A7B08(ui, container). Any failure goes to cleanup sub_1403B7888 and returns 0.
- V: creates (once, qword_143CDAA00) a 24-byte Graphics::UIRender::Utility object; creates two buffers for it: sub_140086DE4 desc {224, 257, ...} (vertex-ish) and sub_140086F64 {96, 1025} (constant buffer); object+8 / +16 hold them. On failure both are released.
- V: creates the UI Renderer object: 216 bytes, vftable faith::Graphics::UIRender::Renderer, slot ids at +64..+74 init to 0xFFFF, stored at ui+8408. Calls UIRender_CreateBuffers(renderer, ?, shaderModule v20, {0x200000, 0x600000, 0x100000}); failure -> free renderer, cleanup, return 0. Then UICommandRing_Reset(*(ui+8408)). v20 comes from sub_14008C5D8(*(qword_140C696A8+5016), {0x0230000 / 0x0344 0C0 words...}, 4) (a shader / module lookup from an 8-byte+8-byte descriptor).
- V: sub_1403B7E2C(ui, *(u16*)(R+6568), *(u16*)(R+6572), 484176) and sub_1403B7F64(ui) (resolution-dependent setup; R = qword_143CDA098, 6568 / 6572 = screen width / height (I)). Creates a 96-byte object at ui+8600 with slot ids at +56..+70 = 0xFFFF and a float2 (width, height) at +80, byte +88 = 0; then sub_1403AE954.
- V: creates a 32-byte Graphics::DownSampling object at ui+8608: name 'spdLinearSamplerConstants' -> +16 (u16 slot), a 64-byte buffer desc {64, 66563} created at +8, 'tTexture1' -> +18 if the buffer was created.
- V: the renderer ui: 'tTexture0' slot -> ui+148, 'cConstant0' -> ui+150; creates {80, 66563} cbuffer -> ui+8416 and {192, 65794} buffer -> ui+8424. Returns 1.

## State touched

- Calls: [UIRender_CreateBuffers](UIRender_CreateBuffers.md), [UICommandRing_Reset](UICommandRing_Reset.md)
- Reads: [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [UIRender.slot_cUIRenderRemap](../structs/UIRender.md#slot_cuirenderremap), [UIRender.slot_cUIRender](../structs/UIRender.md#slot_cuirender), [UIRender.slot_cSDF](../structs/UIRender.md#slot_csdf), [UIRender.slot_g_Sampler](../structs/UIRender.md#slot_g_sampler), [UIRender.slot_tTexture0](../structs/UIRender.md#slot_ttexture0), [UIRender.slot_g_Sampler_tMaskBuffer](../structs/UIRender.md#slot_g_sampler_tmaskbuffer)

## Notes

Command memory sizes are 2 MiB commands, 6 MiB vertices, 1 MiB indices (V from v46). The renderer's cSDF / g_Sampler slots are resolved in UIRender_CreateBuffers, not here.

## Open questions

? contents of the 8408 / 8600 / 8608 objects beyond the offsets listed. ? purpose of constant 484176 (0x76350). ? what the descriptor passed to sub_14008C5D8 selects.
