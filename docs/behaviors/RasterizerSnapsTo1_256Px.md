# RasterizerSnapsTo1_256Px

- **Kind:** observed behaviour
- **Scope:** GPU (the test machine's GPU and driver)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md), [UIImage_VS](../shaders/UIImage_VS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Vertex positions are snapped to 1/256 of a pixel (rounded to nearest) before rasterization, so a UI quad at a third of a pixel (the 2/3 screen scale) is drawn from slightly moved corners and samples its texture at slightly moved positions.

## Behavior

- V (back-buffer captures 2026-10-30, the finger cursor's glove at 12 frozen phases, background captured with the glove hidden): redoing the glove's draw with corners rounded to 1/256 px and 1/256 texel weights reproduces 99.4 % of the glove's 10076 changed values exactly (max 1); exact corners give 93.3 %, truncated corners 84.7 %, a 1/16 px grid 65.4 %.
- I: D3D requires at least 8 bits of sub-pixel precision; this GPU uses exactly that, rounded.

## Open questions

None recorded.
