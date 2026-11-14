# UIRender_CreateBuffers

- **Address:** `0x1403AD990`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char __fastcall UIRender_CreateBuffers(__int64 r, __int64 a2, __int64 shaderModule, unsigned int *params)`
- **Callers:** UIRender_LoadShaders (V: single xref)
- **Callees:** sub_14001A2C4, sub_140011750 (alloc), sub_140086DE4, sub_140086E9C, sub_140086F64 (buffer creators), sub_14003E120 / sub_14003E228 (map / unmap), sub_140089280 (name -> slot), sub_14003ABD0 (release)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates the UI renderer's command and vertex buffers and its 32 UIContext objects, and looks up the cUIRender / cUIRenderRemap / cSDF constant buffers and the g_Sampler / tTexture0 slots.

## Behavior

- V: params[0..2] = v4 (command buffer bytes), v6 (vertex buffer bytes), v8 (index/extra buffer bytes); LoadShaders passes {0x200000, 0x600000 (6291456), 0x100000} (V from its v46 array). Copies params +16..+79 (4 x 16 bytes) to r+80..+143. r+144 / +148 / +152 = the three sizes; r+212 = 24.
- V: r+176 = allocation of v4 bytes (align 8) from heap qword_140C696D0 (command memory); null -> returns 0.
- V: allocates 2568 bytes = 8-byte count (32) + 32 UIContext objects of 80 bytes each (vftable faith::Graphics::UIRender::UIContext, zeroed fields); stored at r+200 (pointer past the count). Each context gets +8 = r (owner) and +40 (dword) = 24.
- V: shaderModule (a3) null -> frees r+8 if set and returns 0. Otherwise refcount +1 (dword at +12 atomic add), r+8 = module (previous released).
- V: buffer creation via sub_140086DE4 / 86E9C / 86F64 with {size, flags, kind} descriptors: r+16 = descriptor {size = v6, 65794 (0x10102)} 20 bytes (vertex buffer); r+24 = v6-byte CPU heap block; r+32 = {size = v8, 66050 (0x10202), 1} (index buffer); r+48 = {32, 66563 (0x10403)} and r+56 = {32, 1028 (0x404)} constant buffers. The 32-byte cbuffer at r+56 is mapped (type 2), zeroed (two 16-byte stores) and unmapped.
- V: r+40 = *(qword_140C696A8 + 5312) (a shared object, refcount +1). Slot lookups by name (sub_140089280): cUIRenderRemap -> r+64, cUIRender -> r+66, cSDF -> r+68 (all constant-buffer table at +5056 of the device object), g_Sampler -> r+70 and g_Sampler_tMaskBuffer -> r+74 (sampler table +5072), tTexture0 -> r+72 (texture table +5064). Returns 1.

## State touched

- Calls: [NameSlotTable_Lookup](NameSlotTable_Lookup.md)
- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)
- Writes: [UIRender.slot_cUIRenderRemap](../structs/UIRender.md#slot_cuirenderremap), [UIRender.slot_cUIRender](../structs/UIRender.md#slot_cuirender), [UIRender.slot_cSDF](../structs/UIRender.md#slot_csdf), [UIRender.slot_g_Sampler](../structs/UIRender.md#slot_g_sampler), [UIRender.slot_g_Sampler_tMaskBuffer](../structs/UIRender.md#slot_g_sampler_tmaskbuffer), [UIRender.slot_tTexture0](../structs/UIRender.md#slot_ttexture0)

## Referenced by

- Called by: [UIRender_LoadShaders](UIRender_LoadShaders.md)
- Reads file formats: [tec](../formats/tec.md)

## Notes

This is the only place the SDF pass's cbuffer name 'cSDF' and samplers 'g_Sampler' / 'g_Sampler_tMaskBuffer' are bound to slot ids; the text pipeline (SDFFontRenderer_Flush, UIRender_ApplyDrawState) uses these u16s. There is ONE sampler named g_Sampler (not per-pass); the mask buffer has its own.

## Open questions

? meaning of the kind words 65794 / 66050 / 66563 / 1028 (flag bits: usage / bind). ? what the shared object at device+5312 is. ? 'a2' unused.
