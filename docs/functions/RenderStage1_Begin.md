# RenderStage1_Begin

- **Address:** `0x1403A23B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage1_Begin(Renderer *r)`
- **Callers:** sub_1403A2774 (RenderFrame_Update)
- **Callees:** job-record vtable (+8), scheduler vtable (+48, +64), fence vtable (+8, +80)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Begins render stage 1: finishes the pending stage-0 fence, runs the stage-1 job array, then calls the stage-1 fence object and sets r+44418.

## Behavior

- V: if r+44417 is set, calls the fence object at r+38088 through vtable +80 (wait) and clears the byte.
- V: n = dword r+38028; for each of n 264-byte job records at the array pointer r+37968 it calls vtable +8 (reset) on the record, and for every record except the last it calls vtable +48 of the application's job scheduler (g_Application+1168) with (index, record).
- V: then calls vtable +8 on the fence object at r+38360 and vtable +64(0) on the scheduler (kick / flush); sets r+44418 = 1.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A23B0).

## Open questions

? the record type (264-byte jobs) and what the last record is (it is not submitted, presumably the fence's own dependency).
