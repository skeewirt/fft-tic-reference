# RenderStage3_Begin

- **Address:** `0x1403A25F4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage3_Begin(Renderer *r)`
- **Callers:** sub_1403A2774
- **Callees:** job-record vtable +8/+24, scheduler vtable +48/+64, fence vtable +8/+80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Begins render stage 3: closes stage 2 if still open (signal its last record, wait on its fence), then submits the third job array (r+37984, count r+38036) and the fence at r+38904; sets r+44420.

## Behavior

- V: if r+44419: last record of array r+37976 vtable +24 (signal), fence r+38632 vtable +80 (wait), r+44419 = 0.
- V: for each of r+38036 records (array r+37984) vtable +8 and, except the last, scheduler vtable +48; then fence r+38904 vtable +8 and scheduler vtable +64(0); r+44420 = 1.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A25F4).

## Open questions

None recorded.
