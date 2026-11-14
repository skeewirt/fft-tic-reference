# BlendFactorUsesStoredSourceAlpha

- **Kind:** observed behaviour
- **Scope:** GPU (the test machine's GPU and driver), UI draws into an 8-bit target
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The destination factor of a UI draw's blend (1 - source alpha) uses the source alpha as the 8-bit target stores it: result = round(source) + round(destination * (1 - round8(source alpha))), with round8 = the target's UNORM store.

## Behavior

- V (frame t4, the two black edge fades JobTree/BG/Rect00 and Rect01, alpha interpolated from 255 to 0 across 266.7 px over the floor): solving each screen column for the multiplier that reproduces the capture, the float alpha is outside the feasible range in 16 of 61 columns (left) and 10 of 43 (right); the alpha stored to 8 bits first in 4 and 4. Linear quantisations of the interpolated value (1/256, 1/512, 1/1024, half floats, truncation) all fit worse.
- V (studio, GameCompose.draw with this rule): frame t4 goes from 97.2 % to 97.9 % of pixels exact (chips 0.082 -> 0.037, ring box 0.124 -> 0.093, every region equal or better); the generic-male sweep frame from 96.9 % to 97.8 %.
- I: D3D lets the blend unit work at the render target's precision, which converts the shader's outputs to the format before blending; this record only states what the frames show.

## Open questions

? the remaining misses under the edge fades. V (2026-10-31, live: the Job Tree captured with JobTree/BG/Rect00 and Rect01 at opacity 0 and at 1, so the game's own floor under them is known): they are not in the floor; in the columns whose alpha x 255 has a fraction from about 0.5 to 0.8 the game stores one level less than the rounded exact alpha, over a vertical stretch that is longest at mid height (the game's interpolated alpha lies up to about 0.3 / 255 below the exact value and changes smoothly with y). I: the GPU's attribute interpolation precision; not modelled (it would be a fit).
