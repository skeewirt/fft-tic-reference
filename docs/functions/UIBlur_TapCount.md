# UIBlur_TapCount

- **Address:** `0x1403ACA7C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIBlur_TapCount(float sigma, float tail)`
- **Callers:** GUILayer_ExpandBounds
- **Callees:** GaussianKernel_Build

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the tap count of the Gaussian kernel for (sigma, tail) and throws the weights away.

## Behavior

- V: builds a 256-byte weight table on the stack with GaussianKernel_Build(sigma, tail, buf) and returns its result unchanged.
- I: used to size a blur (how many pixels it reaches) without running it; its only caller is GUILayer_ExpandBounds.

## State touched

- Calls: [GaussianKernel_Build](GaussianKernel_Build.md)

## Referenced by

- Called by: [GUILayer_ExpandBounds](GUILayer_ExpandBounds.md)

## Notes

The name is ours (IDB: sub_1403ACA7C).

## Open questions

Which sigma / tail GUILayer_ExpandBounds passes (?).
