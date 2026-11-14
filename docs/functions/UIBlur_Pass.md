# UIBlur_Pass

- **Address:** `0x1403ACAB8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void __fastcall UIBlur_Pass(__int64 blur, __int64 layer, int srcTarget, int dstTarget, int tmpTarget, float sigma, float cutoff, __m128i *rect, __m128i *colour, unsigned int mode)`
- **Callers:** UIBlur_Run (V: single xref)
- **Callees:** GaussianKernel_Build, sub_1403ACEBC (blur pair), UIBlur_CopyTarget

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One blur step between two render targets: builds the kernel and runs the separable blur through sub_1403ACEBC, or plain-copies the target when the kernel is a single tap.

## Behavior

- V: does nothing unless *(u8*)(blur+308) != 0 (blur enabled).
- V: taps = GaussianKernel_Build(a6, a7, buf[32 qwords = 256 bytes]); stored in v20[0].
- V: taps > 1: target pointers come from the renderer array R = qword_143CDA098: src = *(R + 8*((layer+86 << 6) + a3) + 24224), tmp = *(R + 8*((layer+86 << 6) + a5) + 24224) (64 entries per layer group, 8 bytes each), plus dst = *(R + 40*a4 + 20832) and tmp2 = *(R + 40*a5 + 20832) (40-byte records). Then calls sub_1403ACEBC(blur, src, dst, tmp, tmp2, sigma, cutoff, rect, &copy_of_colour(a9), &taps, kernel, mode) with a 16-byte local copy of *a9.
- V: taps <= 1 and a3 != a4: UIBlur_CopyTarget(blur, layer, a3, a4, ..., 0, rect, 0) (a plain copy src -> dst, no blur). taps <= 1 and a3 == a4: nothing.
- I: sigma and cutoff are passed as float bit patterns in int args a6 / a7 (decompile types them int; they are forwarded to GaussianKernel_Build as floats).

## State touched

- Calls: [GaussianKernel_Build](GaussianKernel_Build.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md)
- Reads: [Renderer.render_targets](../structs/Renderer.md#render_targets), [Renderer.slots_by_type](../structs/Renderer.md#slots_by_type), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [UIBlur_Run](UIBlur_Run.md)

## Notes

The TLS touches in the decompile are only the thread-state init guard around UIBlur_CopyTarget.

## Open questions

? which of a8 (rect) / a9 (colour) is which: a9 is copied 16 bytes and handed on, a8 is passed through; their roles are decided in UIBlur_DrawPass (a9 -> command state +272 (index 17), a8 -> state +80 (index 5)). ? what mode a10 is (see UIBlur_DrawPass: first shader digit, -1 treated as 0).
