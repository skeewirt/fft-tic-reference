# UIBlur_BlurPassSingle

- **Address:** `0x1403ACDBC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIBlur_BlurPassSingle(UIBlurRenderer *b, __int64 layer, int slotA, __int64 unused, int rtB, float sigma, float tail, __m128i *clamp, int a9, unsigned flags)`
- **Callers:** UIBlur_Run
- **Callees:** GaussianKernel_Build, sub_1403AD710

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Variant of UIBlur_BlurPassOrCopy that always draws: builds the Gaussian kernel and hands one textured pass to sub_1403AD710.

## Behavior

- V: does nothing when b+308 (enabled) is 0.
- V: taps = GaussianKernel_Build(sigma, tail, weights); looks up the slot texture g_Renderer + 8 * (slotA + (layer byte +86 << 6)) + 24224 and the render target g_Renderer + 40 * rtB + 20832, and calls sub_1403AD710(b, slot texture, 5 * rtB, slotA + (layer byte +86 << 6), RT object, sigma, tail, clamp, ..., &taps, ..., flags).
- V: there is no copy fallback and no return value; the tap count is passed on even when it is 1 or less.
- V (sub_1403AD710, read in passing): ShaderSelector_SetDigit slot 1 = (clamp == null), slot 0 = flags (0 when -1), slot 2 = taps - 2 clamped to 7; then it applies the shader and queues the draw.

## State touched

- Calls: [GaussianKernel_Build](GaussianKernel_Build.md)
- Reads: [Renderer.slots_by_type](../structs/Renderer.md#slots_by_type), [Renderer.render_targets](../structs/Renderer.md#render_targets), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours.

## Open questions

Whether this is the horizontal or the vertical blur (no direction argument; the hypothesis is unverified); the meaning of the 5 * rtB argument; some arguments (rect, weights) are not clearly recovered in the decompile.
