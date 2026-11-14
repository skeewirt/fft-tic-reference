# RenderFrame_ResetFlags

- **Address:** `0x1403A2388`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderFrame_ResetFlags(Renderer *r)`
- **Callers:** sub_1403A143C (render-thread setup / job graph builder)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Atomically sets the 'started' flag r+38056 (dword index 9514) and, only if it was 0, clears the three neighbouring flags r+38060, +38064, +38068.

## Behavior

- V: result = InterlockedExchange(r+38056, 1); when the old value was 0, InterlockedExchange(r+38060, 0), (r+38064, 0), (r+38068, 0).
- I: r+38060 / +38064 / +38068 are the 'stage N may run' gates set by RenderStage1_SetGate, RenderStage2_SetGate and RenderStage3_SetGate (the three one-line setters below); this resets them once at the start of a frame.

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2388). Argument r is the renderer object (global qword_143CDA098).

## Open questions

? which caller reads the gates (not traced).
