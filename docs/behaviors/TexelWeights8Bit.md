# TexelWeights8Bit

- **Kind:** observed behaviour
- **Scope:** GPU (the test machine's GPU and driver)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bilinear filtering weights are the sub-texel fraction rounded to 1/256 (8 bits), not exact: the filtered colour of a texel pair at fraction f uses round(f * 256) / 256.

## Behavior

- V (same glove captures): with 1/256 px vertex snapping, rounded 1/256 weights give 99.4 % exact; truncated 1/256 weights 92.7 %, 1/512 weights 93.2 %, exact weights 93.5 %.
- V: the precision of the filtered result itself does not matter (rounding it to 1/(255 * 256) changes one value of 10076; coarser rounding is worse).
- I: other GPUs (vendors, drivers) may use other weight precisions: a viewer that matches this machine byte for byte may differ by 1 elsewhere, as the game itself does.

## Open questions

? the last 0.6 % (63 values, all +-1, interior and edge pixels alike) of the glove; the weight rule at exact ties.
