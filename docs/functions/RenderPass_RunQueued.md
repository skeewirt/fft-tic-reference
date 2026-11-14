# RenderPass_RunQueued

- **Address:** `0x1403A4CD8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 RenderPass_RunQueued(RenderPassMgr *m)`
- **Callers:** RenderFrame_Update
- **Callees:** layer vtable +64 (Draw), +32 (Release)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Work-stealing loop that runs every queued layer object of the table m+14048: calls its vtable +64 with the per-group target pointer and then releases it (vtable +32).

## Behavior

- V: builds a table t[4] with t[group] = target's object (+48) for every target (m+48.., group byte at +24 < 4).
- V: n = dword m+14044. Loop: i = XADD(m+14040, 1); stop when i >= n. obj = *(m + 8*i + 14048); obj->vtable[+64](obj, t[obj+24]); then obj->vtable[+32](obj) (Release) and the slot is cleared.
- I: vtable +64 is the layer's Draw / Run; for a text layer it is the path that eventually reaches GUITextNode_Draw and SDFFontRenderer_Flush.

## Referenced by

- Called by: [RenderFrame_Update](RenderFrame_Update.md)

## Notes

None of the 21 functions of this group touches glyph quads, UVs, the SDF shader constants, the palette or the shadow: they are the renderer's per-frame job scheduler (stage fences, command-list recording across worker jobs). They were seen running every frame only because the text draw runs inside them. The name is ours (IDB: sub_1403A4CD8). This is the only function of the group in the call path of text drawing (as the generic dispatcher of layer objects).

## Open questions

? the class names of the layer objects (each a vtable with +64 Draw).
