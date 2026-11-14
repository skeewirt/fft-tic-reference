# LayerGlowHalfSize

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The glow of a UI layer with a blur radius from 3.2 to 6.4 (the Job Tree selection ring: radius 4.0), stage by stage, each stage reproduced from a mid-frame GPU capture (2026-10-30).

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [RT26_LayerContent](../render-targets/RT26_LayerContent.md) | V | The layer's sharp pixels. |
| <a id="2"></a>2 | [RT32_HalfBlur](../render-targets/RT32_HalfBlur.md) | V | 2 x 2 box average to half size, stored at 8 bits. |
| <a id="3"></a>3 | [RT37_HalfBlurTemp](../render-targets/RT37_HalfBlurTemp.md) | V | Horizontal Gaussian, sigma = radius / 2 (GaussianKernel_Build), stored at 8 bits. |
| <a id="4"></a>4 | [RT32_HalfBlur](../render-targets/RT32_HalfBlur.md) | V | Vertical Gaussian back into RT 32, stored at 8 bits. |
| <a id="5"></a>5 | [RT27_GlowBlurred](../render-targets/RT27_GlowBlurred.md) | V | Bilinear upscale to full size (stores round halves down). |
| <a id="6"></a>6 | [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md) | V | Glow pass (mode 3): target.rgb += 2 x strength x colour x A.rgb x (B.a x (1 - A.a) + (1 - B.a)); the ring draw is reproduced to +-1 on 4 of 19500 values. |

## Behavior

- V: the stages' +-1 residue is the same as in the drop shadow's blur (the blur shader's own taps, not decoded); everything else is exact.

## Referenced by

- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Open questions

None recorded.
