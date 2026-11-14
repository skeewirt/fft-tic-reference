# RenderStage3_End

- **Address:** `0x1403A26F8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage3_End(Renderer *r)`
- **Callers:** sub_1403A2774, sub_1403A2BA8, sub_1403D4954
- **Callees:** sub_1403C5194 (not read), scheduler vtable +72

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Twin of RenderStage1_End for stage 3: signals the last record of array r+37984 and submits callback sub_1403C5194, clears r+44420.

## Behavior

- V: if r+44420: record = r+37984[count r+38036 - 1] vtable +24; callback block {sub_14001B9D8, r, 0, sub_1403C5194} to scheduler vtable +72(block, 0); r+44420 = 0.

## State touched

- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Called by: [RenderFrame_Record](RenderFrame_Record.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A26F8).

## Open questions

? what sub_1403C5194 does.
