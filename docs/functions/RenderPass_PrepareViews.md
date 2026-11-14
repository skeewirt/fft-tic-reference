# RenderPass_PrepareViews

- **Address:** `0x1403A3CDC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderPass_PrepareViews(RenderPassMgr *m)`
- **Callers:** RenderFrame_Update
- **Callees:** sub_1400AE510, _multtenpow12 (CRT long-double helper; the decompile labels the next function by address only)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For each registered view / render target (count m+6575) it advances the double-buffered 20-byte size record (current / previous) from the target description, then calls _multtenpow12 on the global qword_143CD9B70. Always returns 1.

## Behavior

- V: for i < byte m+6575: v = *(m+8i+48). Calls sub_1400AE510(qword_143CD9B70, v+32, (v+4616 & 0x20000000) != 0), clears bit 0x20000000 of v+4616. t = *(v+32).
- V: if v+4616 bit 31 is set (first use): cur = (t+84 qword, t+92 dword), bit 31 cleared, previous = current = the same. Else previous = cur (v+4624..4635 -> +4636..4647), cur = (t+84 qword, t+92 dword).
- I: t+84..+95 is the target's width / height / format triple; the previous copy lets the pass know about a resize.

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A3CDC).

## Open questions

? what sub_1400AE510 does with qword_143CD9B70 (the call to _multtenpow12 may be a mislabelled symbol).
