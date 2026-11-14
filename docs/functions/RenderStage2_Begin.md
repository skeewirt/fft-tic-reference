# RenderStage2_Begin

- **Address:** `0x1403A2514`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage2_Begin(Renderer *r)`
- **Callers:** sub_1403A2774
- **Callees:** job-record vtable +8, scheduler vtable +48/+56/+64, fence vtable +8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same pattern as RenderStage1_Begin for the second job array (r+37976, count r+38032, fence r+38632): resets and submits every record, sets r+44419 and kicks the scheduler.

## Behavior

- V: for each of dword r+38032 records (264 bytes, array r+37976): vtable +8, and for all but the last scheduler vtable +48(index, record).
- V: r+44419 = 1; fence at r+38632: vtable +8, then scheduler vtable +56(fence) (queue the fence); scheduler vtable +64(0).

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2514).

## Open questions

? stage 2's role (probably the main UI command recording).
