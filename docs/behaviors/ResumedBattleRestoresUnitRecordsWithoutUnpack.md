# ResumedBattleRestoresUnitRecordsWithoutUnpack

- **Kind:** observed behaviour
- **Scope:** resuming a battle from an autosave: where the live unit records come from
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md), [Save_ResumeCheckpoint](../functions/Save_ResumeCheckpoint.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [sub_140210AF0](../functions/sub_140210AF0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle resumed from an autosave gets its live unit records (g_UnitSaveData) from the battle snapshot region through Battle_RestoreSceneVars, and SaveWork_UnpackToLive does not run for it: the resume entry unpacks only when the payload part count is 0, and otherwise only sets a flag.

## Behavior

- V: Battle_SnapshotLiveState(work, direction) moves the live state between the live globals and the work block with two memmoves of 0x7E90 bytes between g_UnitSaveData and the work base: direction 0 copies live to work (capture), direction 1 copies work to live (restore); the item stores follow in the same call.
- V: it is called by Battle_SaveCapture (capture) and by Battle_RestoreSceneVars (with the snapshot buffer at 0x14089BC68 and direction 1).
- V: Battle_RestoreSceneVars (0x1402CE5C8) is called from sub_140210AF0 at 0x140210C51; it restores seven scene variables, then the live unit records and item stores through Battle_SnapshotLiveState, the 21 battle units, the look queue and the look pool.
- V: Save_ResumeCheckpoint (0x1402D03D8) reads the payload part count (clamped to 2; a missing object counts as 2). Only when it is 0 does it copy the checkpoint copy into the work copy and tail-jump to SaveWork_UnpackToLive; otherwise it only sets dword_142E7FF68 = 1 (also when the header import fails).
- I: a battle autosave carries a battle snapshot (part count not 0), so a resumed battle takes the flag-only path: its live unit records come from the snapshot copy, and SaveWork_UnpackToLive does not run for it.
- V (seen live 2026-11-09): SaveWork_UnpackToLive did not run during a cold battle resume, while a world-map autosave load ran it.

## Notes

Evidence: IDA decompiles of Battle_SnapshotLiveState, Battle_RestoreSceneVars, Save_ResumeCheckpoint read in full on 2026-11-09; the live observation was made on 2026-11-09.

## Open questions

? what dword_142E7FF68 = 1 starts for the battle path; ? where the part count is set by the writer.
