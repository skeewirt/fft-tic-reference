# RenderFrame_BeginStage4

- **Address:** `0x1403A29E8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderFrame_BeginStage4(Renderer *r)`
- **Callers:** sub_1403A2BA8 (RenderFrame_Record)
- **Callees:** job-record vtable +8, scheduler vtable +48/+56/+64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Begins the fourth job stage: zeroes the work counter r+38072, resets and submits every record of array r+37992 (count r+38040, including the last), queues the fence r+39176 and sets r+44421.

## Behavior

- V: InterlockedExchange(r+38072, 0). For each of r+38040 records (264 bytes): vtable +8, scheduler vtable +48(index, record). Then fence r+39176: vtable +8, scheduler vtable +56(fence), +64(0); r+44421 = 1.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Record](RenderFrame_Record.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A29E8).

## Open questions

None recorded.
