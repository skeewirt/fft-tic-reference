# RenderPass_Sort

- **Address:** `0x1403A3DCC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderPass_Sort(RenderPassMgr *m)`
- **Callers:** RenderFrame_Update
- **Callees:** sub_1403C2690, sub_14039F338, sub_14039F6D0, sub_14003ABD0, layer vtable +24/+32/+56

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sorts and buckets the frame's draw layers (pointer table m+80, count word m+7252) into the 4 per-group arrays, counts them, updates texture-pool residency, and returns 1 when the frame has something to draw.

## Behavior

- V: per target flagged 0x40000000 (v+4616) the layers of type 1 with flag 0x20 in byte +35 and group +87 == target group (+24) get byte +86 = target's +3337 (render-layer id). Layers with flag 0x10000000 (+80) get vtable +56 on their object (+40).
- V: the main layer's object (+40) with bytes +3345 and +3343 sets 3343 = 1 on all other visible layers; layers whose type (+28) is 1 get +3343 = 1.
- V: counts per group (+87 < 4) into m+6580.. and m+13734.. (type 0, or type 1 with flag 0x20000000), AddRefs each layer object (+40, vtable +24) into the table m+14048 releasing the old entry (vtable +32), and publishes the table length in m+14044 and the work counter m+14040 = 0.
- V: calls sub_1403C2690 (a sort over m+80, qword count + 10, with a comparison arg), writes each sorted layer's index back to byte/word +84, then builds the per-type index table at m+7254 (809 words per type, counts at m+13726).
- V: seeds qword_140C696A8: +13 = -256, +17 = 0, +19 = 3, +76 = 0; if there are flagged residency bits it calls sub_14039F338 / sub_14039F6D0 on g+20528, freeing cached per-layer resource slots (100 qwords at 800 * id + 2896 and 64 at id << 9 + 3696) through sub_14003ABD0 when a layer is no longer resident, and writes the minimum render-layer id to m+13742 + group.

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A3DCC). Only the control flow was read; field meanings are inferred from usage.

## Open questions

? the sort key (sub_1403C2690) and what qword_140C696A8 is (13 bytes of render state).
