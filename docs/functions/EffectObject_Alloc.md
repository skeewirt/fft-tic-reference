# EffectObject_Alloc

- **Address:** `0x140310A60`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char EffectObject_Alloc(void)`
- **Callers:** EffectFlash_Start (two), EffectSprites_Spawn, EffectSequence_HitFlashSprites, EffectSequence_SpawnGroup4PerUnit, EffectSequence_SpawnGroup3Cluster, sub_140315B10, EffectSequence_SpawnGroup14Ring
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes one object from a pool of 976-byte effect objects and returns its index (0 when the pool is empty).

## Behavior

- V: objects sit in `word_14186D7B0`, 488 words each, index 0 being a sentinel; the first two words of each are link indexes.
- V: the free list head is `byte_140D408FE`; the used list tail is `byte_140D408FB`. The head object is unlinked from the free list and appended to the used list.
- V: the new object's word 432 is cleared; with an empty free list the sentinel's word is cleared and 0 returned.

## Referenced by

- Called by: [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md), [EffectSequence_SpawnGroup14Ring](EffectSequence_SpawnGroup14Ring.md), [EffectSequence_SpawnGroup3Cluster](EffectSequence_SpawnGroup3Cluster.md), [EffectSequence_SpawnGroup4PerUnit](EffectSequence_SpawnGroup4PerUnit.md), [sub_140315B10](sub_140315B10.md)

## Notes

Whole body read.

## Open questions

None.
