# UIBlur_DrawTexturedPass

- **Address:** `0x1403AD710`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIBlur_DrawTexturedPass(UIBlurRenderer *b, __int64 slotTex, __int64 a3, __int64 a4, __int64 rtObj, int sigma, int tail, __m128i *clamp, int a9, int *taps, int a11, unsigned flags)`
- **Callers:** UIBlur_BlurPassSingle (0x1403ACDBC)
- **Callees:** ShaderSelector_SetDigit, ShaderSelector_Apply, sub_140069A38, RenderState_PackCommand, sub_140069980

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues one Gaussian blur draw of a layer slot texture into a render target, selecting the shader permutation from the tap count.

## Behavior

- V: does nothing when b+308 (enabled) is 0. flags -1 is treated as 0.
- V: selector digits on the selector at b+48: digit 1 = (clamp == null), digit 0 = flags, digit 2 = min(taps - 2, 7) (taps = *taps, or GaussianKernel_Build when taps == null).
- V: state+96 = slotTex, +144 = its +40 handle; texture format bits (dword +16 of the handle when kind +8 is 1 or 2, & 7) into state+124 bits 9..11; the sampler constants of the selected program (program +160 ids / +168 words, each & 0x7FFFFFFF) are copied to state + 5704 + 4 * id; then ShaderSelector_Apply(selector, state, 1).
- V: binds rtObj's handle (+40) at state +8 * (short b+252) + 800; when clamp is given the 16 bytes are copied into state+80 and the flag +112 |= 0x10 (clamp rectangle active); +124 is reset to (& 0xFFC06FFF) | 0x6000; the constant buffer b+56 is bound at slot (short b+292); queues a 96-byte command of header type 3.

## State touched

- Calls: [ShaderSelector_SetDigit](ShaderSelector_SetDigit.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.raster_word](../structs/RenderContext.md#raster_word)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles)

## Notes

The name is ours (IDB: sub_1403AD710). The clamp is passed to the pass as a rectangle in state+80, not as a sampler address mode; its units were not traced here. The sampler filter is not set in this function: the sampler words come from the selected program entry.

## Open questions

What the program's sampler words encode (point / linear); units of the clamp rectangle (pixels of the source texture, presumably).
