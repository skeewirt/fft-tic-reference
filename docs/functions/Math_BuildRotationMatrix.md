# Math_BuildRotationMatrix

- **Address:** `0x14027471C`
- **Area:** [Math](../areas/math.md)
- **Prototype:** `_WORD *__fastcall Math_BuildRotationMatrix(const uint16_t *angles, int16_t *out)`
- **Callers:** About 50 call sites in effects, camera and world-map code, among them EffectEmitter_Spawn, EventCamera_MoveTask and SceneColourPair_WriteVertexColours
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a 3x3 fixed-point rotation matrix (nine 16-bit values, scale 4096) from three angles using the sine and cosine tables.

## Behavior

- V: each angle is masked to 12 bits (4096 steps per turn) and looked up in `tbl_SineTable` and `tbl_CosineTable`; products are shifted right by 12.
- V: with angles (a, b, c): out[0] = cos b cos c, out[1] = -cos b sin c, out[2] = sin b, out[5] = -sin a cos b, out[8] = cos a cos b; out[3], out[4], out[6], out[7] are sums of products of sin/cos a with sin c, cos c and sin b.
- V: returns `out`.
- I: the matrix is row-major, because the helper of `Math_RotateTranslateVector` reads words 0..2 as the row for the x result.

## Referenced by

- Called by: [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectSequence_ProjectileFlight](EffectSequence_ProjectileFlight.md)

## Notes

Whole body read (288 bytes).

## Open questions

None.
