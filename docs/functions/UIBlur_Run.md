# UIBlur_Run

- **Address:** `0x1403B1A10`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIBlur_Run(__int64 blur, __int64 shaderCtx, unsigned char a3, int a4, char a5, float radius, int *a7, __m128i *rect, int a9, int a10, int a11, int a12)`
- **Callers:** sub_1403B4990, sub_1403B4EA8, sub_1403B6204, sub_1403B6640
- **Callees:** UIBlur_Pass, sub_1403ACC64, sub_1403ACDBC, sub_1403ABEDC, sub_1403B4798

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the layer blur for one effect radius: chooses a downscale level from the radius and runs separable Gaussian passes through the render-target chain.

## Behavior

- V: radius > 51.2 -> 1/32 size with sigma = radius / 32; the thresholds 25.6 / 12.8 / 6.4 / 3.2 select 1/16, 1/8, 1/4, 1/2 and full size (sigma = radius / factor, i.e. radius in full-resolution pixels); each level calls UIBlur_Pass (kernel from GaussianKernel_Build with tail threshold 998277249 = ~0.004) horizontally and vertically.
- V: the rectangle is padded by 32 pixels before downscaling.

## State touched

- Calls: [UIBlur_Pass](UIBlur_Pass.md)
- Reads: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Appears in flows: [LayerDropShadow](../flows/LayerDropShadow.md)
- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md), [GUILayer_BlurEffect](GUILayer_BlurEffect.md), [GUILayer_BlurShadowPass](GUILayer_BlurShadowPass.md), [GUILayer_GlowPass](GUILayer_GlowPass.md)

## Notes

Only the head and the first level were read.

## Open questions

Where strength, colour and mode 3 enter the final composite (sub_1403B59D4 chain) (?).
