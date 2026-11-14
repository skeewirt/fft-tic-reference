# UICommandRing_Flush

- **Address:** `0x1403ADF04`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UICommandRing_Flush(__int64 ring, __int64 a2)`
- **Callers:** UIRender_SubmitFrame
- **Callees:** sub_14003E120, sub_14003E228, UICommand_ExecuteBatches

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Uploads the collected command stream into the ring's constant buffer, sets the base pipeline state and executes the batches.

## Behavior

- V: maps ring+16 (sub_14003E120, kind 2) and memmoves ring+168 bytes from ring+184 into it; sets thread-state +208 = ring+212, +200 = the buffer handle (+40), +216 = the handle of qword_143CDAA00+8.
- V: draw state words: +124 = (& 0xFFFFFFC3) | 3, +128 = ring+32, +136 = ring+8, +120 = dword_1407C28E4 (0x20010794 20a41 as a qword: low dword 0x79420a41, i.e. the default UI blend word 0x79420a11 with a different low byte), +104 = low 5 bits 0xC then the 0x100001FFF-masked qword_1407C28F0 (0 after the mask), +112 = qword_1407C28F8 (0x27) & ~0xE000.
- V: samplers: before the batches are executed it writes the default sampler word (dword_141D8BC7C & 0x7FFFFFFF) to the g_Sampler slot (the short at UIRender object ring+70, state + 5704 + 4 * slot) and to the g_Sampler_tMaskBuffer slot (ring+74). The value is 0x7FFFFFFF with the IDB image of the global and 0 at runtime (live read 2026-10-30, see Sampler_DescFromWord); the slot ids are 14 and 15 in the live sampler name table (NameSlotTable_Lookup).
- V: other bindings: a buffer handle at state + 8 * (short ring+64) + 328 (ring+64 is the cUIRenderRemap slot id from UIRender_CreateBuffers, so +328 is the constant-buffer handle table; an earlier version of this sheet called it textures) and the texture handle of ring+40 at state + 8 * (short ring+72) + 1608 (ring+72 = tTexture0).
- V: calls the ring callback (ring+112)(ring+120, ring+128, &state), then UICommand_ExecuteBatches(ring); resets ring+208 to 0 and unmaps.

## State touched

- Calls: [UICommand_ExecuteBatches](UICommand_ExecuteBatches.md)
- Reads: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [UIRender.slot_cUIRenderRemap](../structs/UIRender.md#slot_cuirenderremap), [UIRender.slot_tTexture0](../structs/UIRender.md#slot_ttexture0), [UIRender.slot_g_Sampler_tMaskBuffer](../structs/UIRender.md#slot_g_sampler_tmaskbuffer), [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md), [UIRender.slot_g_Sampler](../structs/UIRender.md#slot_g_sampler)
- Writes: [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words) [14, 15] = default

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md)
- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403ADF04). The sampler constants 0x7FFFFFFF here are for the command-stream buffer, not for layer textures.

## Open questions

What the callback at ring+112 does.
