# TheBattleCaptureCopiesFixedCounts

- **Kind:** observed behaviour
- **Scope:** engine (battle capture, mid-battle resume)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md), [BattleCapture_CopyFaceValues](../functions/BattleCapture_CopyFaceValues.md), [g_LookPool](../globals/g_LookPool.md), [g_AiCurrentAction](../globals/g_AiCurrentAction.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle capture (Battle_SaveCapture / Battle_RestoreCapture, the data a mid-battle save writes) copies fixed counts: 16 scene units, 15 look pool records, 10 face values and the AI block's first 0x19D0 bytes, which hold the AI's four per-number tables; the restore of the scene units walks them by pointer to fixed addresses past the 16th record. A battle with more of any of them needs the rest copied beside the capture, in the same order.

## Behavior

- V: SceneUnits_SaveRestore with mode 0 copies 0x5480 bytes of scene units (16 records of 0x548) to capture +0x4B0 and then 0x2FA8A bytes of look pool records (15 of 0x32D6) to capture +0x5A18, 0xE8 bytes after the units' copy (0x1401D532E, 0x1401D5343).
- V: with mode 1 it first keeps 0x420 bytes of every scene unit in a scratch of 0x4200 bytes (Mem_Alloc, 0x1401D4B71), walking the records by pointer until 0x140D354B8 (the block's end + 8, 0x1401D4DB6); copies the 16 records back with the size 0x5480 loaded into ebp (0x1401D4EA2), and the same register is the end of the fix-up loop over the records (compared with r8 at 0x1401D5074), which takes each record's +0x150 pointer from the scratch and recomputes its frame and sequence pointers; then clears three pointers per record up to 0x140D358D0 (the end + 0x420, 0x1401D50E1) and relinks the in-use records into the scene list up to 0x140D354B8 (0x1401D50FD, 0x1401D511D). The end addresses are the block's own, not a count.
- V: the restore order of a resume: Battle_RestoreSceneVars (its copy of the 15 look pool records from g_SnapshotLookPool, 0x1402CE783), then Battle_RestoreCapture: SceneUnits_SaveRestore, the AI block copy into g_AiCurrentAction (0x19D0 bytes, 0x1402CED5D, after which it zeroes qword_1418724D8 and qword_141872EA0), BattleCapture_CopyFaceValues. Battle_SaveCapture copies in the same order (SceneUnits_SaveRestore at 0x1402CDDB8, the AI block at 0x1402CE484, the face values at 0x1402CE4B8).
- V: BattleCapture_CopyFaceValues copies the 10 face values of g_LookPoolFaceValue (40 bytes) and the globals after them up to 0x1437A5A73, and 40 bytes at 0x1437A1348, each way (mode 0 save, 1 restore).
- V: the AI block copy holds g_AiUnitNumber (0x141873038, 21 bytes) and the four per-number tables (16 numbers each) at block +0xCD4, +0xE58, +0xEF8 and +0x1780.

## Open questions

None recorded.
