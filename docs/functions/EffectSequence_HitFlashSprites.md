# EffectSequence_HitFlashSprites

- **Address:** `0x1403138DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool EffectSequence_HitFlashSprites(void)`
- **Callers:** EffectSequence_Run (slot 2 of the effect sequence handler table (0x140682F30))
- **Callees:** ClutFade_UnitSlot, EffectObject_Alloc, EffectObject_InitMotion, EffectObject_Step, EffectObject_Free, EffectCamera_SetVector, sub_140381F50, sub_140381A54, ResourcePool_AllocBlocks, sub_1402F3A04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 2 handler: flashes the target unit's palette and spawns two sets of sprites, with extra screen values set on the first, third and fifth frames of one sub-kind.

## Behavior

- V: state 1: if the sub-kind byte (+33) is 4 it returns 0 at once. Otherwise it frees any buffer at +88, allocates a 0x28-byte buffer there (ResourcePool_AllocBlocks), clears it, sets the state to 2, calls sub_140381A54 and returns 1.
- V: state 2 works on that buffer (v4 is read from +88 only in state 2; in state 3 it is null and every buffer block is guarded): dword +0 is a frame counter, +4 a finished flag, +8 the live count of the first sprite set (up to 8 slot bytes at +12), +20 the live count of the second set (up to 16 slot bytes at +24).
- V: when the sub-kind (+33) is not 3 it calls ClutFade_UnitSlot(5, 0, unit slot, 31, 31, 31) on buffer frame 0 and ClutFade_UnitSlot(8, 2, unit slot, 0, 0, 0) on frame 1 (both calls are inside that test), with the unit slot at entry +32.
- V: while the frame is below 4 it spawns up to the spawn count (byte +42) of EffectSpriteSpawnRecords group 0 into the first set, and up to the spawn count of group 1 (group 9 when the sub-kind is 3) into the second set, each through a free sprite slot (EffectObject_Alloc) and EffectObject_InitMotion; the first-set sprites take word +4 of the record from the entry's selector word (+6) plus 31424 (entry +4, the effect kind, is only the second argument of the animation-end check EffectObject_Step), the second-set sprites a fixed value (31434).
- V: both sets are checked every frame: a sprite slot whose animation has ended (EffectObject_Step returns 0) is freed (EffectObject_Free) and the live count lowered. The three renderer globals are saved, set to fixed values and restored around this.
- V: when the sub-kind (+33) is 1 it also calls EffectCamera_SetVector on buffer frames 0 and 2 with fixed values (-128 on frame 0, 740 on frame 2) and on frame 4 calls EffectCamera_SetVector with zeros and sub_140381F50 with the value 4.
- V: each frame adds 1 to the buffer frame counter; when both live counts are 0 and the frame is above 30 it adds 1 to the finished flag. It returns whether the finished flag was not 1, so the entry ends one frame after it is set.
- V: state 3 only swaps the renderer globals as described and returns 0.
- I: nothing in this function sets state 3 (latent here); the owner would have to.
- I: the unit-palette fade and the sprite sets are the hit mark on the target; the screen values set for sub-kind 1 are unread (EffectCamera_SetVector, sub_140381F50).

## State touched

- Calls: [ClutFade_UnitSlot](ClutFade_UnitSlot.md), [EffectObject_Alloc](EffectObject_Alloc.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectObject_Step](EffectObject_Step.md), [EffectObject_Free](EffectObject_Free.md), [EffectCamera_SetVector](EffectCamera_SetVector.md), [ResourcePool_AllocBlocks](ResourcePool_AllocBlocks.md)

## Notes

Name is ours. The IDB signature declares two arguments (a1, a2); the code takes none (a2 is only passed on as scratch to EffectCamera_SetVector).

## Open questions

?: what EffectCamera_SetVector and sub_140381F50 change; the meaning of sub-kinds 1, 3 and 4.
