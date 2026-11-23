# Math_RotateTranslateVector

- **Address:** `0x140274BC0`
- **Area:** [Math](../areas/math.md)
- **Prototype:** `__int64 __fastcall Math_RotateTranslateVector(const int16_t *in, int32_t *out, int32_t *flag)`
- **Callers:** About 90 call sites, among them EffectEmitter_Spawn, EffectFlash_Start, WorldRoads_BuildMarkers
- **Callees:** sub_14027460C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Transforms a 3-component 16-bit vector by the current rotation matrix and translation held in globals and returns the result as three 32-bit values.

## Behavior

- V: copies 8 bytes of input (three words plus padding) into `qword_1411A38F0` and calls `sub_14027460C`.
- V: that helper multiplies the vector by the 3x3 word matrix at `byte_1411A3870`, shifts by 12 and adds three dwords starting at 0x1411A3884; results land in `dword_1411A3954`, `dword_1411A3958` and `dword_1411A395C`; it also sets `dword_1411A38EC` to 0 and writes the sign-truncated 16-bit results to `dword_1411A3914`, `dword_1411A3918` and `dword_1411A391C`.
- V: copies the three results to `out[0..2]` and `dword_1411A38EC` to `*flag`; returns that flag value.
- V: the output pointer is the second argument (the decompile shows it as an unnamed register; the disassembly keeps a saved copy of the second argument register).

## Referenced by

- Called by: [EffectEmitter_Spawn](EffectEmitter_Spawn.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectSequence_ProjectileFlight](EffectSequence_ProjectileFlight.md), [WorldRoads_BuildMarkers](WorldRoads_BuildMarkers.md), [sub_14034DE90](sub_14034DE90.md)

## Notes

Whole body and the helper read. The translation dwords start at 0x1411A3884, which is dword 1 of the 0x1411A3880 operand the helper uses; the matrix ends in the word at 0x1411A3880.

## Open questions

What the flag value means (it is always 0 in the helper).
