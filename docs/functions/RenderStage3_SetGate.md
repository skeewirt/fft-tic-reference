# RenderStage3_SetGate

- **Address:** `0x1403A26EC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderStage3_SetGate(Renderer *r)`
- **Callers:** sub_1403A143C
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One-line helper: InterlockedExchange(r+38068, 1).

## Behavior

- V: returns the old value.

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A26EC).

## Open questions

None recorded.
