# RenderState_PackCommand

- **Address:** `0x14003A2B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderState_PackCommand(RenderThreadState *st, Command *cmd, ...)`
- **Callers:** draw / dispatch submission
- **Callees:** sub_14003A7D8, sub_14003A844

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Packs the current pipeline state (blend words, flags, shader constants, texture bindings) into the 8 KB command chunks the render thread consumes and stamps the command with a state hash.

## Behavior

- V: the first blend word is st+120 (masked with 0x7FFFFFFF); st+124 carries the count of extra per-target words ((st+124 >> 9) & 7), which are read from st+5964 + 4 * (i - 1); st+6008 is a per-target flag word.
- V: the packed words are hashed with FNV-1a (basis 0x811C9DC5, prime 16777619) over the bytes written, and the hash is stored at cmd+16; the command takes space from the current 8 KB chunk (st+24 pointer, st+52 used bytes) and requests a new chunk from the allocator when the chunk is full (qword_140C696A8 + 5108 / +5120 / +5144 / +5148).
- V: the packed blob also holds the constant data at st+80 (16 bytes) and an optional texture handle (*(st+6024) + 40), and the per-stage constant blocks via sub_14003A844.

## State touched

- Reads: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.blend_rt1_7](../structs/RenderContext.md#blend_rt1_7), [RenderContext.blend_factor](../structs/RenderContext.md#blend_factor), [RenderContext.command_block](../structs/RenderContext.md#command_block), [g_RenderDevice](../globals/g_RenderDevice.md)
- Writes: [RenderContext.command_block](../structs/RenderContext.md#command_block)

## Referenced by

- Called by: [GUILayer_BlurShadowPass](GUILayer_BlurShadowPass.md), [GUILayer_CopyToTarget](GUILayer_CopyToTarget.md), [GUILayer_EffectPass0](GUILayer_EffectPass0.md), [PostTarget_DrawFitted](PostTarget_DrawFitted.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md), [UIBlur_DrawPass](UIBlur_DrawPass.md), [UIBlur_DrawTexturedPass](UIBlur_DrawTexturedPass.md), [UIRender_DrawLetterbox](UIRender_DrawLetterbox.md), [UIRender_DrawOverlayQuads](UIRender_DrawOverlayQuads.md), [sub_1403B5170](sub_1403B5170.md)

## Notes

The packed blend words are unpacked by BlendDesc_FromWords when the pipeline state is created. Only the tail was read.

## Open questions

The head of the function (state diffing and the sizes v18 / v29 / v55) was not read (?).
