# LayerBinds_Replay

- **Address:** `0x1403A8468`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 LayerBinds_Replay(LayerBinder *b, RenderCmd *cmd, Layer *layer)`
- **Callers:** SDFFontRenderer_Flush (0x1403AA196), GUILayer_Composite (0x1403B5C01), sub_1403B8BF4, sub_1403B8F20, sub_1403B93BC
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the recorded bind lists of a layer into a render command: resource pointers into cmd+328+8*slot, texture handles into cmd+1608+8*slot, and 31-bit constants into cmd+5704+4*slot.

## Behavior

- V: r = 200 * u8 layer+90; three (value vector, slot vector) pairs at b+352+r / b+384+r (qwords), b+416+r / b+448+r (qwords, dereferenced), b+480+r / b+512+r (dwords); the count is the slot vector's byte span >> 1.
- V: pair 1: cmd[328 + 8*slot] = resource pointer. Pair 2: cmd[1608 + 8*slot] = (resource ? *(resource + 40) : 0), the same slot field GUILayer_EffectPass0 writes at rc+1608 for textures. Pair 3: *(u32*)(cmd + 5704 + 4*slot) = value & 0x7FFFFFFF, the shader-selector constants of GUILayer_EffectPass0 (rc+5704, top bit cleared).

## State touched

- Writes: [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words)

## Referenced by

- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The name is ours (IDB: sub_1403A8468). Called once per draw command (per batch), so it is hot, but it only copies binds; it does not touch glyph positions. The same call is made by every layer draw (composite, effect passes), not only by SDF text.

## Open questions

? which of the 328 / 1608 / 5704 areas are constant buffers, textures and shader constants respectively beyond the equivalence with GUILayer_EffectPass0 (I).
