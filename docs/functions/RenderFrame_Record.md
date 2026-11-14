# RenderFrame_Record

- **Address:** `0x1403A2BA8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void RenderFrame_Record(Renderer *r)`
- **Callers:** sub_1403D4954 (RenderFrame_Run), vtable slot at 0x143D3FF28
- **Callees:** RenderState_SeedCommands, sub_14039ECF4, RenderFrame_BeginStage4, RenderPass_Build, RenderStage3_End, sub_1403A82A8, sub_1403A8354, worker vtable +32, scheduler vtable +48/+56/+64, fence vtable +8/+80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Render-thread half of the frame: for each of the (up to) 4 submission rounds it builds the per-pass command batches (RenderPass_Build), runs the worker command loops, resets per-layer counters, and closes with the final fence stage (r+39992).

## Behavior

- V: runs only when r+44415 and not r+44416. Calls sub_1403A32F4 (RenderState_SeedCommands), sub_14039ECF4(r+20528), RenderFrame_BeginStage4.
- V: round v3 = 0, 1, ... while r+13758 is nonzero: clears 0xF00 bytes at r+40536 (a batch array of 960-byte entries), then calls RenderPass_Build(r+8, batch, v3, k, &flag) for k = 0, 1, ... advancing the batch pointer by 960 until it returns 0; the first batch of round 0 waits on fence r+39176.
- V: round 0 also calls RenderStage3_End and sub_1403A82A8(r+24760). Then r+24895 = 2; for each of the byte count at *(g+6615) (g = qword_143CDA098) passes it stores the pass object g+88+8*g[+7132+2i] into r+25096+200*i and calls sub_1403A8354(r+24760). Calls vtable +32(round) of each of the 4 worker objects at r+37920.
- V: InterlockedExchange(r+38076, v1) arms the Cmd40 loop; fence array r+38008 (count r+38048, 264-byte records) gets vtable +8, and unless the record's dword +40 is 1 its +256 = round; each is submitted with scheduler vtable +48; fence r+39720 is reset, queued (+56), the scheduler kicked (+64) and waited (vtable +80) with r+44422 set during the wait.
- V: after each round it zeroes/copies 6 qword pairs per pass (stride 200 at r+24920..25120: cur = prev), clears r+6615, 0x200 bytes at r+6616, r+7128 and 0x80 bytes at r+7132, and loops.
- V (final): InterlockedExchange(r+38080, 0); submits array r+38016 (count r+38052) and fence r+39992, r+44423 handling, waits (vtable +80), then r+24753 = 0 and r+13760 = 0, and clears the same 6 pairs for each layer-group object (g+13734 count, ids at g+7262, stride 200 at r+24896).

## State touched

- Calls: [RenderState_SeedCommands](RenderState_SeedCommands.md), [RenderFrame_BeginStage4](RenderFrame_BeginStage4.md), [RenderPass_Build](RenderPass_Build.md), [RenderStage3_End](RenderStage3_End.md)
- Reads: [g_Application](../globals/g_Application.md), [g_Renderer](../globals/g_Renderer.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2BA8). Only the structure was read; the 960-byte batch and 200-byte per-pass stride layouts are partly decoded in RenderPass_Build.

## Open questions

? exact meaning of the 200-byte per-pass records (cur/prev double buffers), the fence array r+38008 and r+38016.
