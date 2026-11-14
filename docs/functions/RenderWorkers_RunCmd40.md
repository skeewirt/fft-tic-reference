# RenderWorkers_RunCmd40

- **Address:** `0x1403A2B18`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderWorkers_RunCmd40(Renderer *r, unsigned int arg)`
- **Callers:** sub_1403A143C (job body)
- **Callees:** worker vtable +40

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same loop as RenderWorkers_RunCmd24 with its own counter (r+38076) and worker vtable +40, passing arg through.

## Behavior

- V: for (i = XADD(r+38076, 1); i < 4; ...) obj = r+37920[i]; obj->vtable[+40](obj, arg). RenderFrame_Record re-arms the counter with InterlockedExchange(r+38076, v1); the decompile shows v1 holding the loop remainder (0 after the palette loop), so I: the re-arm value is 0.

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2B18).

## Open questions

? whether the reset value is really 0 (v1 reuse in the decompile; assembly not checked).
