# SceneUnits_SaveRestore

- **Address:** `0x1401D46B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SceneUnits_SaveRestore(void *capture, int restore)`
- **Callers:** Battle_SaveCapture, Battle_RestoreCapture
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the scene units, the scene list, the CLUT image and the CLUT manager to or from the battle capture.

## Behavior

- V: with restore = 1 it copies the 16 scene-unit records back (0x140D30030, 0x5480 bytes), recomputes their frame and sequence table pointers (+0x220 / +0x228 and the saved copies +0x230 / +0x238) from each record's sprite byte, rebuilds the scene list `qword_140D3A410` from the in-use flags, links each battle unit through g_UnitSceneSlotIndex (scene +0x148 = unit) and restores g_ClutImage (0x1C00 bytes) and g_ClutManager (0x86DC bytes).

## Referenced by

- Observed behaviours: [ResumeLoadsTheLookStateTwice](../behaviors/ResumeLoadsTheLookStateTwice.md), [SixteenSceneUnitsComeOnlyFromTheLookQueue](../behaviors/SixteenSceneUnitsComeOnlyFromTheLookQueue.md), [SlotIndexCarriersAreBytesAndFiveBits](../behaviors/SlotIndexCarriersAreBytesAndFiveBits.md)
- Reads tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Open questions

None recorded.
