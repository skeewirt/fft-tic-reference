# LayerShadow_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x035E50`
- **DXBC hash:** `855988b49cb49541e2b0e84f446e16c0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Drop-shadow pass of a UI layer: darkens the target in place under the layer's blurred alpha, before the layer itself is drawn.

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="cuirender"></a>`cb0` | `cUIRender` |  | V | Row 13.x strength, rows 31.xyz colour, 34.zw atlas offset / target size, 20.x distance-mask switch (off on the Job Tree). |
| <a id="source"></a>`t0` | `source` | [RT3_EffectAlpha](../render-targets/RT3_EffectAlpha.md) | V | The blurred layer alpha (alpha channel). |
| <a id="g_sampler"></a>`s0` | `g_Sampler` | [SamplerSlots.g_Sampler](../registries/SamplerSlots.md#g_sampler) | V | Not set by the pass: holds the default word, so the read is point-filtered. |
| <a id="target"></a>`u0` | `target` |  | V | The target under the layer, read and written in place (UNORM). |

## Behavior

- V: A = alpha of t0 at uv + atlas offset; s = saturate(strength x A); target.rgb = target.rgb x ((1 - s) + colour x A); target.a = s + target.a x (1 - s).
- V (mid-frame capture, four Job Tree layers): with the point read, 8-bit blurred alpha and the half-down UNORM store, the formula reproduces every changed value.

## Referenced by

- Observed behaviours: [UnormStoreRoundsHalfDown](../behaviors/UnormStoreRoundsHalfDown.md)
- Used in programs: [LayerShadow](../programs/LayerShadow.md)

## Open questions

None recorded.
