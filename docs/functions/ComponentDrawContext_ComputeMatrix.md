# ComponentDrawContext_ComputeMatrix

- **Address:** `0x14040A914`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void ComponentDrawContext_ComputeMatrix(Component *comp, float *outMatrix2x3, float *outScale2, PropBlock *props)`
- **Callers:** ComponentDrawContext_Build (outScale preset to 1, 1), sub_1403E647C
- **Callees:** Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives ComponentDrawContext_Build the component's local 2 x 3 matrix and a two-float scale; when comp+540 = 1 it scales the matrix by the ratio of two sizes, otherwise it copies both straight from the property block.

## Behavior

- V: if comp+540 == 1: sx = (int)props+64 / (int)comp+336 and sy = (int)props+68 / (int)comp+340 (each 1.0 when the divisor is 0); builds the matrix [sx 0 0 sy 0 0] and calls Matrix2x3_Multiply(outMatrix, that, props+80); outScale = (sx * props+96, sy * props+100).
- V: otherwise: copies 16 bytes from props+80 and 8 bytes from props+176 to outMatrix (6 floats) and 8 bytes from props+184 to outScale.

## State touched

- Calls: [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [ComponentLayer_DrawMaskComponent](ComponentLayer_DrawMaskComponent.md)

## Notes

The name is ours. Reading: comp+336/+340 is the authored size and props+64/+68 the actual size, so mode 1 is a stretch to fit (I). Operand order of Matrix2x3_Multiply(out, a, b) is taken from the call.

## Open questions

What comp+540 = 1 means in the file; the meaning of props+176 / +184 (precomputed matrix tail and scale?); how sub_1403E647C uses the result was not read.
