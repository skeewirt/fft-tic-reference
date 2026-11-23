# EffectCamera_SetVector

- **Address:** `0x1403823F0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void __fastcall EffectCamera_SetVector(__int16 mode, __int64 unused, int value, int *vec)`
- **Callers:** EffectScript_OpRunTimeline, EffectSequence_HitFlashSprites (three calls), sub_140383BFC
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects the effect view's target vector by a mode in bits 5..8 of the first argument and stores it, with a value and the upper mode bits, in the effect view globals.

## Behavior

- V: the mode is `mode & 0x1E0`. Modes 0, 64, 128, 320 and 384 copy the 16 bytes at `vec` to `xmmword_143C51D00` (no null check).
- V: mode 192: starts from the 16 bytes at `g_CharaRenderer + 147660` and, when `vec` is not null, adds the three dwords at `vec`; mode 256 does the same starting from `xmmword_143C51D20`. Other modes change nothing.
- V: for every handled mode it stores `value` in `dword_143C51CE8`, `mode & 0x1E00` in `dword_143C51CA4` and zero in `dword_143C51CEC`.
- I: the second argument is not used (rests on the pseudocode; the database over-declares the signature).

## Referenced by

- Called by: [EffectScript_OpRunTimeline](EffectScript_OpRunTimeline.md), [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md)

## Notes

V: whole body read. The name is ours; the vector is added to a base for the two relative modes, which is why the name says vector rather than position.

## Open questions

?: what the modes mean and who reads `dword_143C51CA4` and `dword_143C51CE8`.
