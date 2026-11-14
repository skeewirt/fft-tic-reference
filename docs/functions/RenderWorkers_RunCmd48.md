# RenderWorkers_RunCmd48

- **Address:** `0x1403A2B68`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderWorkers_RunCmd48(Renderer *r)`
- **Callers:** sub_1403A143C (job body)
- **Callees:** worker vtable +48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same loop with counter r+38080 and worker vtable +48.

## Behavior

- V: for (i = XADD(r+38080, 1); i < 4; ...) obj = r+37920[i]; obj->vtable[+48](obj). The counter is reset to 0 by RenderFrame_Record before the final stage.

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2B68).

## Open questions

None recorded.
