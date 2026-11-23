# EffectObject_Free

- **Address:** `0x140310AE0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall EffectObject_Free(char index)`
- **Callers:** EffectFlash_Start, EffectGroup_UpdateChildren, EffectSequence_HitFlashSprites, EffectSequence_SpawnGroup4PerUnit, EffectSequence_SpawnGroup3Cluster, sub_140315B10
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns an effect object to the pool: unlinks it from the used list and pushes it on the free list head.

## Behavior

- V: does nothing for index 0.
- V: fixes the neighbours' links or moves the used-list tail, then sets the free head to the object with its links reset.

## Referenced by

- Called by: [EffectGroup_UpdateChildren](EffectGroup_UpdateChildren.md), [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md), [EffectSequence_SpawnGroup14Ring](EffectSequence_SpawnGroup14Ring.md), [EffectSequence_SpawnGroup3Cluster](EffectSequence_SpawnGroup3Cluster.md), [EffectSequence_SpawnGroup4PerUnit](EffectSequence_SpawnGroup4PerUnit.md)

## Notes

Whole body read.

## Open questions

None.
