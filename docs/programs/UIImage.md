# UIImage

- **Kind:** shader program
- **Area:** [Graphics](../areas/graphics.md)
- **Selector:** UI technique (UIRender_ApplyDrawState)
- **Program index:** 0
- **Shaders:** [UIImage_VS](../shaders/UIImage_VS.md), [UIImage_PS](../shaders/UIImage_PS.md)
- **Applied by:** [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md), [UIImage_DrawTiled](../functions/UIImage_DrawTiled.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Draws every textured UI image: program 0 of the UI technique (shader objects 1 and 10).

## Behavior

- V (ShaderProgram_ApplyState sheet, live): program 0 = shader objects (1, 10) = the first vertex and the first pixel shader of uirender.tec in file order (0x001300, 0x001E9C).

## Open questions

None recorded.
