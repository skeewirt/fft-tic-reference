# LayerQuadOffset_VS

- **Kind:** shader
- **Stage:** vertex
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x035438`
- **DXBC hash:** `a0c2d348cb255a745a5789ee71b06903`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Vertex shader of the drop-shadow pass: moves the layer quad by the shadow offset and keeps its texture coordinates.

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="position"></a>`in0` | `POSITION` | [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer) | V | Quad position in target pixels. |
| <a id="texcoord"></a>`in1` | `TEXCOORD` |  | V | Passed through unchanged. |
| <a id="cuirender"></a>`cb0` | `cUIRender` |  | V | Row 12.zw the shadow offset in pixels (added to the position); rows 4-7 the projection (x 2 / width - 1, y 1 - 2 / height; no half-pixel term). |

## Behavior

- V: output position = (position + offset) x projection; texcoord unchanged, so the texture is sampled at the pixel minus the offset.

## Referenced by

- Used in programs: [LayerShadow](../programs/LayerShadow.md)

## Open questions

None recorded.
