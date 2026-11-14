# AlphaCopy_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x0349C0`
- **DXBC hash:** `dc5737f5490cc1d005c9f0788145ae49`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Copies a layer's alpha into the effect alpha target: writes (0, 0, 0, source alpha).

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="source"></a>`t0` | `source` |  | V | The layer's own target, sampled at uv clamped to row 37.zw. |

## Behavior

- V: output = (0, 0, 0, T0.a).

## Referenced by

- Used in programs: [LayerAlphaCopy](../programs/LayerAlphaCopy.md)

## Open questions

None recorded.
