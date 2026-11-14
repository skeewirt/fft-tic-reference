# UIBlur_DrawPass

- **Address:** `0x1403AD3A4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char __fastcall UIBlur_DrawPass(__int64 blur, __int64 layer, __int64 srcTex, __int64 dstTarget, int a5, float sigma, float cutoff, __m128i *rect, __m128i *colour, int *tapsIn, _OWORD *kernelIn, int mode)`
- **Callers:** UIBlur_BlurPassOrCopy (V: single xref)
- **Callees:** GaussianKernel_Build, sub_14003E120 (map), sub_14003E228 (unmap), sub_14003E604, sub_14003E5D8, ShaderSelector_SetDigit, ShaderSelector_Apply, sub_140069A38 (alloc cmd), RenderState_PackCommand, sub_140069980 (submit)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one direction of the separable Gaussian blur: uploads the cGaussianBlurPS constants (sigma, cutoff, tap count and the 64 weights), selects the shader permutation by tap count and records a draw command.

## Behavior

- V: returns 0 if *(u8*)(blur+308) == 0. mode = a12, where -1 is treated as 0. ts = thread state *(TLS+56) (the per-thread draw state, cf. UIRender_FlushBatch).
- V: tap count: from *tapsIn if a10 given (kernel from a11), else GaussianKernel_Build(sigma, cutoff, local 256 bytes) and uses that.
- V: constant buffer: map = sub_14003E120(*(blur+56), 2) (map, type 2). Writes sigma at +0, cutoff at +4, taps at +8 (dword), and copies the 64 weights (16 x 16 bytes = 256 bytes) starting at +16. Then unmap sub_14003E228(*(blur+56)). Buffer id stored at blur+56 (created with 0x400 flags in UIRender_LoadShaders path of the shared blur: see CreateBuffers cSDF-style 32-byte layout; ? the blur constant buffer size).
- V: shader selector (blur+48) digits: digit 1 = (rect == null) (1 when no rect/scissor), digit 0 = mode, digit 2 = taps-2 clamped to 7 when (taps-2) > 6 as unsigned (so taps 2..8 select permutations 0..6 and any bigger count, 9 or more, selects 7).
- V: state setup on ts: ts+96 (v17[6]) = dstTarget, ts+144 (v17[9]) = *(dstTarget+40); format-type field of that object (+8 == 1 or 2) takes its dword at +16 and puts (v & 7) into bits 9..11 of ts+124; per-slot values from the shader's table at *(shader+160) (u16 slot ids) and *(shader+168) (dwords) are written masked & 0x7FFFFFFF into ts + 16*356 + 8 + 4*slot (resource slots).
- V: after ShaderSelector_Apply: source texture *(srcTex+40) stored at ts+1600 + 8*(*(s16*)(blur+252)+1) (texture slot); if rect != null: ts+112 flags |= 0x10 (& 0xFFFF1FFF), ts+80 = *rect (16 bytes). ts+124 &= 0xFFC06FFF | 0x6000 (draw-call type bits set to 6 in the 0x6000 field, i.e. same field UIRender_FlushBatch sets to 2 / 5). Constant buffer bound at ts+320 + 8*(*(s16*)(blur+292)+1) = *(blur+56).
- V: allocates a 96-byte command with sub_140069A38(ts, 4, 96); sets *(cmd+8) = 3, packs state with RenderState_PackCommand(cmd+16) and submits with sub_140069980. Returns 1.
- V: colour a9 is copied to ts+272 (v17[17]) and ts+60-ish word 3 gets sub_14003E5D8 result added: v27->m128i_i32[3] (ts+12) = result of sub_14003E5D8 + v26 (? two sub-results added; not resolvable from the decompile, registers lost).

## State touched

- Calls: [GaussianKernel_Build](GaussianKernel_Build.md), [ShaderSelector_SetDigit](ShaderSelector_SetDigit.md), [ShaderSelector_Apply](ShaderSelector_Apply.md), [RenderState_PackCommand](RenderState_PackCommand.md)
- Reads: [RenderContext.raster_word](../structs/RenderContext.md#raster_word)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.vertex_buffers](../structs/RenderContext.md#vertex_buffers), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles)

## Referenced by

- Called by: [UIBlur_BlurPassOrCopy](UIBlur_BlurPassOrCopy.md)

## Notes

The constant layout uploaded to the GPU is: float sigma, float cutoff, int taps, pad dword, then 64 floats at +16 (total >= 272 bytes: 16 + 256). Gaussian weights are therefore NOT computed in the shader; the shader loops over `taps` entries.

## Open questions

? the unsplit decompile of sub_14003E604 / 5D8 arguments (ts+12 write uses lost registers). ? size of the blur cbuffer (struct above is 272 bytes with 16-byte header; confirm in cGaussianBlurPS). ? ts offsets are given from v17[n] = n*16 byte indexing: v17[6] = +96, v17[9] = +144, v17[7] = +112, v17[5] = +80, v17[17] = +272.
