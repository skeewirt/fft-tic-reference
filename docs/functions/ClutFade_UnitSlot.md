# ClutFade_UnitSlot

- **Address:** `0x1402F7C20`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void ClutFade_UnitSlot(int mode, int duration, int slot, int16 r, int16 g, int16 b)`
- **Callers:** Deployment_ResetState, sub_1401EF0D8, sub_1401F014C, SceneObjects_StepStates, SceneUnit_ResetAndQueue4, EffectScript_RunColourTracks, EventSubScript_RunTask
- **Callees:** sub_1402F7ACC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a colour fade on a drawing slot's rows of palette banks 3 and 4 (sub_1402F7ACC), or on every slot when the slot is 16 or more.

## Behavior

- V: a slot below 16 is one slot; anything else loops sub_1402F7ACC over slots 0..15 (count at 0x1402F7C72).
- V: four callers ask for every slot with 16: Deployment_ResetState (0x1401EE677), sub_1401EF0D8 (0x1401EF35B, 0x1401EF416), sub_1401F014C (0x1401F0625); sub_1401EF0D8 also passes 47 (0x1401EFE67). Others pass a scene unit's slot byte (+8) or an effect script's byte.
- V: sub_1402F7ACC finds the slot's scene object and calls ClutFade_SetTarget on bank 3 and bank 4 row = slot.

## Referenced by

- Called by: [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md)
- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Open questions

None recorded.
