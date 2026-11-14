# Matrix2x3_Invert

- **Address:** `0x1403D8208`
- **Area:** [Math](../areas/math.md)
- **Prototype:** `float *Matrix2x3_Invert(float out[6], const float m[6])`
- **Callers:** GUIWidget_HitTestChildren
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Inverts a 2x3 affine matrix (1/det with det = m0*m3 - m1*m2).

## Behavior

- V: no check for det = 0.

## Referenced by

- Called by: [GUIWidget_HitTestChildren](GUIWidget_HitTestChildren.md)

## Open questions

None recorded.
