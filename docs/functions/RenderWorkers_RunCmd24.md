# RenderWorkers_RunCmd24

- **Address:** `0x1403A2AB0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderWorkers_RunCmd24(Renderer *r)`
- **Callers:** sub_1403A143C (as a job body)
- **Callees:** worker vtable +24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Work-stealing loop over the 4 per-pass worker objects: atomically takes the next index from r+38072 and calls vtable +24 on worker r+37920[i] while i < 4.

## Behavior

- V: for (i = XADD(r+38072, 1); i < 4; i = XADD(r+38072, 1)) obj = *(r + 8*i + 37920); obj->vtable[+24](obj).

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A2AB0). The four objects are indexed by the pass / layer-group 0..3 (the same 0..3 as obj+24 in RenderPass_Build). Job threads run it concurrently, hence the atomic index.

## Open questions

? the worker class (vtable +24).
