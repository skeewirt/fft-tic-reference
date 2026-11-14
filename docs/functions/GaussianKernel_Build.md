# GaussianKernel_Build

- **Address:** `0x1403ABD50`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall GaussianKernel_Build(float sigma, float cutoff, float *out64)`
- **Callers:** UIBlur_BlurPassOrCopy, UIBlur_BlurPassSingle, UIBlur_DrawPass, UIBlur_DrawTexturedPass, UIBlur_Pass, UIBlur_TapCount, sub_1403ACEBC (V: 7 xrefs)
- **Callees:** expf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the normalised one-sided 64-entry Gaussian weight table for the UI blur and returns the tap count.

## Behavior

- V: returns 0 if |sigma| <= 1.1920929e-7 (FLT_EPSILON).
- V: w[i] = expf(i*i * (-0.5/sigma^2)) for i in 0..63 into a 336-byte stack buffer; sum = w[0] + 2*sum(w[1..63]) (centre once, mirror taps twice). Returns 0 if |sum| <= FLT_EPSILON.
- V: tap count: scan i from 0 while cutoff <= w[i]/sum; first i with cutoff > w[i]/sum is the returned count (taps = i, i.e. weights >= cutoff are kept; if none drops below, count stays 0 (v6 = 0) after 64 iterations).
- V: second normalising sum s2 = sum over i < the scan stop of w[i]*(1 if i==0 else 2); returns 0 if |s2| <= FLT_EPSILON. Then all 64 floats (16 x __m128 divides) are divided by s2 and stored to out64 (so the table is normalised over the kept taps only, not the full 64).
- I: x and y of the blur use the same table; UIBlur_DrawPass uploads it as 2 x 128 bytes into cGaussianBlurPS.

## Referenced by

- Called by: [UIBlur_BlurPassOrCopy](UIBlur_BlurPassOrCopy.md), [UIBlur_BlurPassSingle](UIBlur_BlurPassSingle.md), [UIBlur_DrawPass](UIBlur_DrawPass.md), [UIBlur_Pass](UIBlur_Pass.md), [UIBlur_TapCount](UIBlur_TapCount.md)

## Notes

Edge case worth knowing: if every weight stays >= cutoff the returned tap count is 0 (the V reading of the code: v6 only assigned on break), while the normalised table is still written. A zero count is treated by callers (UIBlur_Pass) as 'no blur: copy'.

## Open questions

? what the caller's cutoff constant is (a7 of UIBlur_Pass); not read here.
