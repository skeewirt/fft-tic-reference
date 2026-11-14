# UIBlur_BlurPassOrCopy

- **Address:** `0x1403ACC64`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char UIBlur_BlurPassOrCopy(UIBlurRenderer *b, __int64 layer, int srcRT, int dstRT, int slot, float sigma, float tail, __m128i *clamp, __m128i *rect, unsigned flags)`
- **Callers:** UIBlur_Run
- **Callees:** GaussianKernel_Build, UIBlur_CopyTarget, UIBlur_DrawPass

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One Gaussian blur pass toward dstRT; when the kernel has 1 tap or less it degenerates to a plain copy.

## Behavior

- V: returns 0 at once when b+308 (enabled) is 0.
- V: taps = GaussianKernel_Build(sigma, tail, weights). When taps <= 1: if srcRT != dstRT it calls UIBlur_CopyTarget(b, layer, srcRT, dstRT, ..., filter 0, clamp, 0) and returns 0.
- V: otherwise copies the rect, looks up the layer slot texture at g_Renderer + 8 * (slot + (layer byte +86 << 6)) + 24224 and the render target at g_Renderer + 40 * dstRT + 20832, and calls UIBlur_DrawPass(b, g_Renderer, RT object, slot texture, ..., sigma, tail, clamp, rect, &taps, weights, flags); its result is the return value.

## State touched

- Calls: [GaussianKernel_Build](GaussianKernel_Build.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md), [UIBlur_DrawPass](UIBlur_DrawPass.md)
- Reads: [Renderer.slots_by_type](../structs/Renderer.md#slots_by_type), [Renderer.render_targets](../structs/Renderer.md#render_targets), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours. Same argument list as UIBlur_Pass (0x1403ACAB8) but the pass is a single UIBlur_DrawPass instead of sub_1403ACEBC. UIBlur_Run calls it as (ctx, layer, 32, 32, 37, radius * 0.5, 0.004, rect, rect, a12).

## Open questions

Whether this is the horizontal or the vertical pass (there is no direction argument here); what the slot argument (37) selects in the layer slot table; the return value is 0 on the copy path and whatever UIBlur_DrawPass returns otherwise.
