# ShaderProgram_ApplyState

- **Address:** `0x1403A39CC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int ShaderProgram_ApplyState(ShaderTable *t, ThreadState *ts, unsigned program)`
- **Callers:** ShaderSelector_Apply (tail jump)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds one program: its shader objects into the thread state and the pipeline-state words (raster word, blend state word, the blend words of the render targets, blend-factor flags) from its 64-byte entry.

## Behavior

- V: t = sel + 24 of the calling ShaderSelector_Apply: t[2] = the shader object array (sel+40), t[3] = the 64-byte program entries (sel+48), t[4] = the program table of the current permutation (sel+56, 8 bytes per program), t[5] = the shader index list (sel+64, dwords). program is the index within the selected permutation.
- V: entry = t->entries + (program << 6); shader indices come from t->list at the offset stored in t->programs[program] (first dword), count = entry byte +57 starting at slot entry byte +56; each shader object pointer (t->shaders[index]) is written to ts + 8*slot + 152.
- V: when (entry byte +58 & 3) == 3 and the byte at (qword_140C696A8 + 3464) equals 2, the index list is read count entries further on (a second shader set for that program).
- V: entry dword +0 is both data and a mask of what to copy: its low 6 bits replace the low 6 bits of ts+124; bit 0x40 copies the raster word (entry+48 & 0xFFFFFFFFFFFF1FFF) to ts+112; bit 0x80 replaces the low 5 bits of the qword at ts+104 with those of the qword at entry+40; bit 0x100 replaces all bits of ts+104 except those under mask 0x100001FFF (bits 0..12 and bit 32, which keep their value) with the qword at entry+40; bits 0x200 and 0x3FC00 as in the next bullets.
- V: mask bit 0x200: the dword at entry+4 is stored at ts+120 and bit 0x100 of ts+124 is cleared.
- V: mask bits 0x3FC00 (bit 10 + i selects word i of the eight dwords at entry+8..+39): word 0 is stored whole at ts+120; word i = 1..7 is stored with its top bit cleared at ts + 5964 + 4 * (i - 1); afterwards ts+124 |= 0x100. The sampler words of the context (ts+5704 + 4 * slot, 64 slots, +5704..+5959) are not touched by this copy.
- V: for every word selected by 0x3FC00, bit i of the dword ts+6008 is set when any of four 5-bit fields of that word (masks 0x1F0, 0x3E00, 0x3E0000, 0x7C00000) equals 13 or 14, else cleared.
- I: the eight words are the blend words of render targets 0..7, not sampler words. Basis: RenderContext_ResetFrame fills the same slots (ts+120 and ts+5964..+5991) with one constant, 0x78020010, which the BlendDesc_FromWords decode reads as blending off, ONE / ZERO factors, write mask 0xF; RenderState_PackCommand packs ts+120 followed by ts+5964 + 4 * (i - 1) as one word array (the count is bits 9..11 of ts+124, used when bit 0x100 is set), the order of the words BlendDesc_FromWords takes; the render-thread side that hands the packed words to BlendDesc_FromWords was not read.
- I: the four 5-bit fields tested are the source, destination, source-alpha and destination-alpha factor fields of the BlendDesc_FromWords decode, whose stored value plus 1 gives the Direct3D 12 factor: 13 and 14 give BLEND_FACTOR (14) and INV_BLEND_FACTOR (15). So bit i of ts+6008 would mean that render target i's blend word uses the blend factor colour. Basis: that decode, and RenderState_PackCommand, which appends the 16-byte colour at ts+5992 to the command (command flag 0x80) when ts+6008 is non-zero.
- V (live, 2026-10-29: the mask program resolved to object 60 = PS 03DF10 and the shadow program to objects 5 / 52 = VS 035438 / PS 035E50, each the neighbour pair in file order): shader object index 10 + k = the k-th pixel shader of UIRender.tec in file order, and index 1..9 = the nine vertex shaders in file order.

## State touched

- Reads: [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [g_RenderDevice](../globals/g_RenderDevice.md)
- Writes: [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.blend_rt1_7](../structs/RenderContext.md#blend_rt1_7)

## Referenced by

- Called by: [ShaderSelector_Apply](ShaderSelector_Apply.md)

## Notes

Live UI technique: program 0 = shader objects (1, 10), 1 = (2, 11), 2 = (1, 12), 3 = (2, 13), 4.. = (3, 14..). Shader object index 10 + k is the k-th pixel shader of UIRender.tec in file order: programs 0..3 = 1E9C (plain image), 3964 (remap), 4990 (SDF), 5560 (SDF remap) (M: order match; programs 2 and 3 match the cSDF/cUIRenderRemap bindings). For selector #10 (GUILayer_CopyToTarget / GUILayer_BlurShadowPass) program 0 was read live as vertex 034080 + pixel 0349C0 and program 1 = vertex 035438 + pixel 035E50.

## Open questions

? the meaning of entry byte +58 and of the global byte at (qword_140C696A8 + 3464) (an alternate shader set). ? who sets bits 9..11 of ts+124 (the number of blend words) for a program that carries per-target words: this function only sets bit 0x100. ? what the render thread does with the ts+6008 bits beyond the blend-factor colour that RenderState_PackCommand appends.
