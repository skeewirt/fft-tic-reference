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
- V: with mode 0 the units' copy goes to capture +0x4B0 (0x5480 bytes) and the 15 look pool records to capture +0x5A18 (0x2FA8A bytes), 0xE8 bytes after it.
- V: the restore's walks end at fixed addresses past the 16th record, not at a count: 0x140D354B8 (the block's end + 8) for the scratch walk (0x1401D4DB6, scratch 0x4200 bytes = 0x420 per record, 0x1401D4B71) and the relink (0x1401D50FD, 0x1401D511D), 0x140D358D0 (end + 0x420) for the pointer clear (0x1401D50E1); the size 0x5480 loaded into ebp (0x1401D4EA2) is both the copy's size and the fix-up loop's end (record TheBattleCaptureCopiesFixedCounts).

## Referenced by

- Observed behaviours: [BattleRetriesRestoreTheirOwnCapture](../behaviors/BattleRetriesRestoreTheirOwnCapture.md), [ResumeLoadsTheLookStateTwice](../behaviors/ResumeLoadsTheLookStateTwice.md), [SixteenSceneUnitsComeOnlyFromTheLookQueue](../behaviors/SixteenSceneUnitsComeOnlyFromTheLookQueue.md), [SlotIndexCarriersAreBytesAndFiveBits](../behaviors/SlotIndexCarriersAreBytesAndFiveBits.md), [TheBattleCaptureCopiesFixedCounts](../behaviors/TheBattleCaptureCopiesFixedCounts.md)
- Reads tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Open questions

None recorded.
