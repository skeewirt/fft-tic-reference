# RenderPass_Build

- **Address:** `0x1403A48CC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderPass_Build(RenderPassMgr *m, PassBatch *batch, int mask, unsigned k, char *done)`
- **Callers:** RenderFrame_Record (loop over k)
- **Callees:** none (pure bookkeeping)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Packs up to 16 draw layers per target into one 240-byte batch entry (and at most 64 layers per round, counter m+6607) for the command-recording jobs; returns 1 while more batches remain for the round, 0 at the end.

## Behavior

- V: stores a3 (pass-enabled mask) in m+6568. If the layer count byte m+6607 < 64 and k < 4: for each of the 4 groups it updates the layer range (m+6588 begin, m+6596 end) from per-group counts (m+13734 pending, m+6580 total).
- V: for each target (byte m+6575) it writes into batch+240*group: +0 target pointer (v+48), +152 group, +160 bit mask of layers, and per layer slot (up to 0x10): +8+8*slot layer pointer, +136+slot render-layer id (+86), +176+4*slot = (layer+16 & 0x7FFFFFF) | (1 << type) << 27, bit 1 << id into a used-layer mask; +155 = running layer count (first slot).
- V: per layer it also records the layer index in m+6608 + 2*(type*64 + count) and m+7124 + 2*count, and layer+90 = global running index m+6607++.
- V: after each target it writes the per-type run table (+168/+169 start, end bytes at 2*(type + 120*group) ... , +162 type mask, +153 total) and +154 = single used layer id (popcount == 1) or 0xFF, +156 = (qword_140C696A8+32 & 0x7FFFFFF) ^ (id << 27).
- V: returns 1 while pending counts remain (m+13749 set) or when the number of groups handled differs from the number of targets; when all four group counts are zero it sets *done = 1 and clears m+13749. Otherwise clears m+13750 and returns 0.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Referenced by

- Called by: [RenderFrame_Record](RenderFrame_Record.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A48CC). Field meanings are inferred from the writes; the packed dword at +176 is 5 type bits over a 27-bit id.

## Open questions

? the structure names (240-byte entry, 960-byte batch of 4 groups), what layer+16 is.
