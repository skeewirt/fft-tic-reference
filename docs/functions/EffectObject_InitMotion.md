# EffectObject_InitMotion

- **Address:** `0x140387268`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall EffectObject_InitMotion(__int64 params, __int64 object)`
- **Callers:** EffectFlash_Start, EffectSprites_Spawn, EffectSequence_HitFlashSprites (two calls), EffectSequence_SpawnGroup4PerUnit, EffectSequence_SpawnGroup3Cluster, EffectSequence_SpawnGroup14Ring; also a data reference at 0x143D3F5F8
- **Callees:** EffectAnchor_GetPoint, sub_140272AA8, Math_BuildRotationMatrix, Math_RotateTranslateVector, sub_140274B34, sub_140384058, atan2f, sqrtf, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes the start position, velocity and a few scalar fields of a spawned effect object from a parameter record, using the effect's anchor points and a random spread.

## Behavior

- V: reads the caster and target anchor points with `EffectAnchor_GetPoint(0, -1, ...)` and `(0, 0, ...)`, and takes a base point from `qword_14186D768 + 16 / + 28`.
- V: the orientation is chosen by `*(u16*)(params + 8) & 0x410`: 0x410 builds a heading from `sub_140272AA8` in steps of 1024; 0x400 builds one from the anchor difference with `atan2f` and `sqrtf` (4096 units per turn); 0 and 0x10 leave it unset.
- V: draws three random 15-bit values from a 128-bit xorshift generator at `xmmword_1408E5FC8` (shifts of 11 and 8), builds a rotation with `Math_BuildRotationMatrix` and rotates vectors with `Math_RotateTranslateVector`; the spread length is the signed value of whichever of the params words at +16, +18, +20 has the largest magnitude; when that value is not positive it becomes 1.
- V: writes into `object`: word 0 = 4096; word 1 = `sub_140384058(params[+34], params[+36])`; dwords at +4, +8, +12 = the position components shifted left by 12; bytes +28..+51 zeroed.
- V: the velocity dwords at object +16, +20, +24: when `*(u16*)(params + 8) & 0x410` is 0x10 they point from the position to the base point (normalised by `sub_140274B34` and scaled by `sub_140384058(params[+38], params[+40])` shifted right by 9; with a zero offset only +20 is set, to 8 times the speed); for 0, 0x400 and 0x410 they are 8 times a rotated vector whose middle component is `sub_140384058(params[+38], params[+40])`.
- V: returns `sub_140384058(params[+44], params[+45])` (signed bytes).
- I: `sub_140384058(a, b)` returns a random value between its arguments (rests on its use with (x/2, -x/2) pairs as a symmetric spread; not read).
- ?: the full layout of the parameter record beyond the offsets used above.

## State touched

- Calls: [EffectAnchor_GetPoint](EffectAnchor_GetPoint.md), [Math_BuildRotationMatrix](Math_BuildRotationMatrix.md), [Math_RotateTranslateVector](Math_RotateTranslateVector.md)

## Referenced by

- Called by: [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md), [EffectSequence_SpawnGroup14Ring](EffectSequence_SpawnGroup14Ring.md), [EffectSequence_SpawnGroup3Cluster](EffectSequence_SpawnGroup3Cluster.md), [EffectSequence_SpawnGroup4PerUnit](EffectSequence_SpawnGroup4PerUnit.md)

## Notes

V: read in full. The name is ours. The output offsets are into the object passed as the second argument.

## Open questions

?: the parameter record's field meanings and the exact types of the helper results.
