# RenderFrame_Update

- **Address:** `0x1403A2774`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderFrame_Update(Renderer *r)`
- **Callers:** sub_1403D4954 (RenderFrame_Run), vtable slot at 0x143D3FEE0
- **Callees:** sub_1403A317C, RenderPass_PrepareViews, RenderPass_Sort, RenderQueue_Flush, RenderStage1_Begin/End, sub_1403A7E48, RenderPass_RunQueued, RenderStage2_Begin, sub_14008EDEC, RenderStage3_Begin, sub_1403B85B0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Main-thread half of the frame: latches per-frame flags, converts each pending timer's float seconds to a 1024-tick integer range, runs the pass sorting / stage 1-3 begin calls, then notifies every registered listener. Returns v14 & v3DCC result (1 = frame was drawn).

## Behavior

- V: returns 0 at once when r+44416 (frame disabled) is set. Copies r+44413 to r+44412. If the dword mask r+44376 is nonzero it sets r+24870 = 1 and, when mask bit 0x40 is set and the slot r+13754 is not 0xFF, sets byte +3732 of that slot's object (+40) to 1. Clears the mask.
- V: when r+44415 is 0 it calls sub_1403A317C; a 0 result sets r+44416 = 1 and returns 0, otherwise (r+44415 still 0) it returns 1 without drawing.
- V (timers): for each of r+6583 entries in the pointer table r+56: x = float at obj+4600. If x <= 0: flag +4652 = 1, x = 0. Else obj+4612 = old obj+4608, obj+4608 += (int64)(x * 1024.0), obj+4600 = 0, flag = 0. obj+4604 = x. If obj+4653 is set and obj+64 != obj+56 it clears +4653; then ++obj+56 (frame counter).
- V (order): v14 = RenderPass_PrepareViews(r+8) & 1; v15 = v14 & RenderPass_Sort(r+8); then RenderQueue_Flush(r+8) (sub_1403A4308), RenderStage1_Begin, sub_1403A7E48(r+24760), RenderStage1_End, RenderPass_RunQueued(r+8) (sub_1403A4CD8), vtable +80 of the object at r+13776, RenderStage2_Begin, sub_14008EDEC(r+40264), RenderStage3_Begin (if r+44420 = 0), sub_1403B85B0(r+37936).
- V (tail): obj = *(r+37936)+8608; obj+24 = index of the first set bit (max 5) of the 64-bit mask at renderer +6568 (the pass-enabled mask, also the a3 argument of RenderPass_Build, sub_1403A48CC); then for each listener in the vector at (*(r+37920))+32..+40 whose vtable +88 returns true it calls vtable +16.

## State touched

- Calls: [RenderPass_PrepareViews](RenderPass_PrepareViews.md), [RenderPass_Sort](RenderPass_Sort.md), [RenderQueue_Flush](RenderQueue_Flush.md), [RenderStage1_Begin](RenderStage1_Begin.md), [RenderPass_RunQueued](RenderPass_RunQueued.md), [RenderStage2_Begin](RenderStage2_Begin.md), [RenderStage3_Begin](RenderStage3_Begin.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_Renderer](../globals/g_Renderer.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2774). The 1024 constant converts seconds to ticks for the timer ranges; unrelated to the 64-unit glyph grid of the SDF atlas.

## Open questions

? what the timer objects at r+56.. are (4600..4653 fields), the meaning of the mask r+44376 bits.
