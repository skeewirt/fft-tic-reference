# Save_ResumeCheckpoint

- **Address:** `0x1402D03D8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Save_ResumeCheckpoint(__int64 arg)`
- **Callers:** UISaveLoad_StateLoad, UIAgentFFTOTitle_Update
- **Callees:** sub_14021849C, sub_140257354, memmove, SaveWork_UnpackToLive (tail)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

After a slot load, decides whether the auto-slot checkpoint is a plain world-map one: only then it copies the checkpoint into the save work block and unpacks it to the live records. For every other case (including a battle resume) it only raises a flag.

## Behavior

- V: calls sub_14021849C(arg, 0) (the classic auto-slot header import); when that returns false the function sets dword_142E7FF68 = 1 and returns (it does not return silently).
- V: otherwise reads the payload part count: qword_143CD9EE0 is a pointer to the auto-slot object; the pointer at +0x3D5188 (4,018,568) of it points at an object whose dword at +12 is read (I: the payload part count, as the earlier sheet named it), clamped to 2. A null object or null header counts as 2.
- V: when the part count is not 0, the function only sets dword_142E7FF68 = 1 and returns: SaveWork_UnpackToLive does not run.
- V: when the part count is 0: calls sub_140257354, points Src at g_SaveWorkCurrent, copies 0x9CE4 bytes from g_SaveCheckpointCopy to it with memmove and tail-jumps to SaveWork_UnpackToLive(0).
- I: a battle autosave has payload parts (a battle snapshot), so a battle resumed from it takes the flag-only path and its live unit records come from the battle snapshot (Battle_RestoreSceneVars), not from SaveWork_UnpackToLive; a world-map autosave has part count 0 and unpacks. Seen live 2026-11-09: a hook on SaveWork_UnpackToLive logged nothing during a cold battle resume, while a world-map autosave load logged. See the behaviour ResumedBattleRestoresUnitRecordsWithoutUnpack.
- V: the two callers are the title-screen load state and a load-confirmation path.
- ?: what dword_142E7FF68 = 1 triggers for the battle path (its readers were not traced).

## State touched

- Calls: [sub_14021849C](sub_14021849C.md), [sub_140257354](sub_140257354.md), [SaveWork_UnpackToLive](SaveWork_UnpackToLive.md)
- Reads: [g_SaveCheckpointCopy](../globals/g_SaveCheckpointCopy.md)
- Writes: [g_SaveWorkCurrent](../globals/g_SaveWorkCurrent.md)

## Referenced by

- Observed behaviours: [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md)

## Notes

Whole function read (decompiled in IDA, 2026-11-09), rewritten: the earlier sheet said the function returns when the header import fails and that a "check byte at 0x143CD9EE0" must be set (it is a pointer), and that memcpy is used (it is memmove).

## Open questions

? the readers of dword_142E7FF68; ? the payload header fields other than the part count.
