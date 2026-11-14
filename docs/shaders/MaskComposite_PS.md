# MaskComposite_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x03DF10`
- **DXBC hash:** `9f813f3c7cc78909f83f803cce5b0aec`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Mask pass of a masked layer (the screen title): the layer's gradient times the mask buffer.

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="mask"></a>`texture` | `mask` | [RT30_MaskBuffer](../render-targets/RT30_MaskBuffer.md) | I | Mask coverage in the red channel (register not recorded; RT 30 is the R8 target the mask pass reads). |

## Behavior

- V: output = gradient.rgba x mask.r.

## Open questions

None recorded.
