# LayerDropShadow

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The drop shadow of a UI layer, end to end (decoded and reproduced from mid-frame GPU captures).

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [GUILayer_BuildRecord](../functions/GUILayer_BuildRecord.md) | V | UIB property block: radius x min(scale), offset x scale per axis, strength, colour go to the layer. |
| <a id="2"></a>2 | [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md) | V | Layer alpha copied into RT3_EffectAlpha inside the layer's atlas rectangle (program LayerAlphaCopy). |
| <a id="3"></a>3 | [UIBlur_Run](../functions/UIBlur_Run.md) | V | Radius <= 3.2: full-resolution Gaussian (GaussianKernel_Build, sigma = radius), horizontal into RT28_BlurScratch, vertical back into RT 3; each pass stored at 8 bits. |
| <a id="4"></a>4 | [LayerShadow](../programs/LayerShadow.md) | V | Quad = rect - atlas offset + shadow offset; A read through g_Sampler = default = point: texel floor(x + 0.5 - offset); target darkened in place (offsets 1.6 / 1.333 / 2.667 move the shadow 2 / 1 / 3 px). |
| <a id="5"></a>5 | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md) | V | The layer itself is drawn over the darkened target. |

## Open questions

None recorded.
