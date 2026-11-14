# Matrix2x3_Rotate

- **Address:** `0x1403D83FC`
- **Area:** [Math](../areas/math.md)
- **Prototype:** `float *Matrix2x3_Rotate(float out[6], const float m[6], float angle)`
- **Callers:** GUINode_BuildLocalMatrix
- **Callees:** sinf, cosf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rotates a 2x3 matrix by angle radians (single-precision sinf / cosf), applied AFTER m.

## Behavior

- V: s = sinf(a), c = cosf(a); out0 = m0*c - m1*s; out1 = m0*s + m1*c; out2 = m2*c - m3*s; out3 = m2*s + m3*c; out4 = m4*c - m5*s; out5 = m4*s + m5*c (in this operand order; all inputs read before any output is written, so out may alias m).

## Notes

The name is ours (IDB: sub_1403D83FC). With the point convention x' = m0*x + m2*y + m4, y' = m1*x + m3*y + m5 this rotates points by +angle in the usual maths sense, i.e. clockwise on the y-down screen.

## Open questions

None recorded.
