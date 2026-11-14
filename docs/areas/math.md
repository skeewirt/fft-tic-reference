# Math

Matrix and conversion helpers.

Functions: 5.

## Functions (5)

| Name | Address | Purpose |
|---|---|---|
| [Matrix2x3_Invert](../functions/Matrix2x3_Invert.md) | `0x1403D8208` | Inverts a 2x3 affine matrix (1/det with det = m0*m3 - m1*m2). |
| [Matrix2x3_Multiply](../functions/Matrix2x3_Multiply.md) | `0x1403D82F0` | Concatenates two 2x3 affine matrices (a applied first, then b); the UI's node and layer transforms use this layout [m0 m1 m2 m3 tx ty]. |
| [Matrix2x3_Rotate](../functions/Matrix2x3_Rotate.md) | `0x1403D83FC` | Rotates a 2x3 matrix by angle radians (single-precision sinf / cosf), applied AFTER m. |
| [sub_1404D66E0](../functions/sub_1404D66E0.md) | `0x1404D66E0` | Releases one reference to a shared global work block. |
| [sub_1404D6720](../functions/sub_1404D6720.md) | `0x1404D6720` | Acquires the shared global work block. |
