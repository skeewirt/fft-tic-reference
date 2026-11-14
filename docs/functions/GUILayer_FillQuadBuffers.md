# GUILayer_FillQuadBuffers

- **Address:** `0x1403B12CC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 GUILayer_FillQuadBuffers(UILayer *layer)`
- **Callers:** GUILayer_Composite
- **Callees:** sub_14003E120, sub_14003E228

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the layer's rectangle as quads into the eight per-layer vertex buffers of the UI renderer, slot index layer+8 (4 vertices per layer).

## Behavior

- V: W, H = (float) u32 at g_Renderer + 6568 / + 6572; (x, y, w, h) = floats layer +208 / +212 / +216 / +220 (no rounding here).
- V: buffer [1064] (vertices 16 bytes, record index 4 * layer+8): corners TL, TR, BL, BR of the rectangle as (px, py, px / W, py / H). Buffer [1066] gets the same quad.
- V: buffer [1065]: the same quad moved by (-layer+224, -layer+228) (the atlas offset): (x - dx, y - dy, ... / W, / H).
- V: buffer [1059]: only positions (8 bytes), the rectangle expanded by 2.0 on every side. Buffer [1072]: 6-vertex x 16-byte records (position + uv, two triangles) of the plain rectangle. Buffer [1069]: 4 x (x, y, 0|1, 1) records (position with clip-style z / w constants 0 / 1.0).
- V: buffer [1074]: the fixed full-surface quad (0,0) (W,0) (0,H) (W,H) with uv 0..1 in the same record; buffer [1075] (once, into a mapped constant): the u16 render size as floats and fixed unit corners.

## State touched

- Reads: [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [GUILayer.index](../structs/GUILayer.md#index), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_Renderer](../globals/g_Renderer.md)
- Writes: [UIManager.layer_quad_mapped](../structs/UIManager.md#layer_quad_mapped)

## Referenced by

- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The name is ours (IDB: sub_1403B12CC). Pixel-exact note: the vertices carry the layer rectangle as unrounded floats and the uv is simply px / size (no half-pixel offset); any snapping happens earlier, in GUILayer_PackAtlasRect, which overwrites +208..+220 with integer atlas coordinates for packed layers.

## Open questions

Which shader reads which of the buffers.
