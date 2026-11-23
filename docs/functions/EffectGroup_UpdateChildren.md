# EffectGroup_UpdateChildren

- **Address:** `0x140313390`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall EffectGroup_UpdateChildren(int kind)`
- **Callers:** EffectSequence_SpawnGroup16, EffectSequence_SpawnGroup10WithCue, EffectSequence_SpawnGroup6, EffectSequence_SpawnGroup7AtTile, EffectSequence_SpawnGroup8WithCue, EffectSequence_SpawnGroup5Rising, EffectSequence_SpawnGroup15, EffectSequence_SpawnGroup11
- **Callees:** EffectObject_Step, EffectObject_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steps each child effect object of the current effect group and frees the ones that report they are finished.

## Behavior

- V: the child count is the byte at 0x1408F2634 + 46*kind; the group record is `qword_14186D768` and its child indexes are bytes from +52.
- V: each child is stepped by `EffectObject_Step` (index, the group's u16 at +4); a zero result frees it with `EffectObject_Free`, clears its entry and decrements the group's live count word at +48.
- I: a non-zero result of the stepper means still running (rests on this caller keeping the child).

## State touched

- Calls: [EffectObject_Step](EffectObject_Step.md), [EffectObject_Free](EffectObject_Free.md)

## Referenced by

- Called by: [EffectSequence_SpawnGroup10WithCue](EffectSequence_SpawnGroup10WithCue.md), [EffectSequence_SpawnGroup11](EffectSequence_SpawnGroup11.md), [EffectSequence_SpawnGroup15](EffectSequence_SpawnGroup15.md), [EffectSequence_SpawnGroup16](EffectSequence_SpawnGroup16.md), [EffectSequence_SpawnGroup5Rising](EffectSequence_SpawnGroup5Rising.md), [EffectSequence_SpawnGroup6](EffectSequence_SpawnGroup6.md), [EffectSequence_SpawnGroup7AtTile](EffectSequence_SpawnGroup7AtTile.md), [EffectSequence_SpawnGroup8WithCue](EffectSequence_SpawnGroup8WithCue.md)

## Notes

Whole body read.

## Open questions

None.
