# RenderStage1_End

- **Address:** `0x1403A2498`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage1_End(Renderer *r)`
- **Callers:** sub_1403A2774 (RenderFrame_Update), sub_1403D4954 (RenderFrame_Run)
- **Callees:** sub_1403C51CC (stage-1 completion callback, not read), scheduler vtable +72

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends render stage 1 when r+44418 is set: signals the last stage-1 job record and submits a callback pair to the scheduler.

## Behavior

- V: if r+44418: record = r+37968 array element (count r+38028 - 1), calls its vtable +24 (signal); builds a 40-byte callback block {sub_14001B9D8, r, 0, sub_1403C51CC} and calls scheduler vtable +72(block, 0); clears r+44418.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2498).

## Open questions

? what sub_1403C51CC does.
