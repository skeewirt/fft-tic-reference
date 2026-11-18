# EventUnitBlock_RunTask

- **Address:** `0x140235D38`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventUnitBlock_RunTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x49
- **Callees:** SceneVar_Read, SceneTask_WaitFrame, SceneTask_Terminate, EventScript_InstructionLength, `sub_1402334FC`, `sub_1402FB7C8`, `sub_140300D74`, `sub_140300768`, ScenePreview_FindEntry, ScenePreview_SlotOfIndex, `sub_140241128`, ScenePreview_ShowEntry, ScenePreview_ClaimForUnit, `sub_14027294C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x49: runs the instructions after 0x49 up to 0x4A once, handling the unit opcodes 0x45 and 0x82 and skipping the rest, then ends.

## Behavior

- V: tags its task slot with the value 14 in `qword_140D40B38[256 * index]`.
- V: starts at its operand pointer (the instruction after 0x49) and walks the instructions by length with EventScript_InstructionLength until it reaches opcode 0x4A.
- V: runs once with no frame wait of its own; the only waits are inside the handlers below.
- V: opcode 0x82: when `SceneVar_Read(508)` is zero it sets `word_140D408F4` to 2, calls `sub_1402334FC(13)`, waits one frame, then calls `sub_1402FB7C8`, `sub_140300D74` and `sub_140300768`.
- V: opcode 0x45: reads a 16-bit unit id from instruction bytes 1 and 2 and a flag byte from byte 3. It resolves the id with ScenePreview_FindEntry; when that result is -2 or negative it searches the 21-entry preview unit table (512-byte entries from `g_BattleUnitTable`) for the record and ends the task if it is not there. Otherwise it calls ScenePreview_SlotOfIndex, then ScenePreview_ShowEntry or ScenePreview_ClaimForUnit (depending on the flag byte) and `sub_140241128`, and may start `sub_14027294C` in a task slot as opcode 0x28 does. It then waits frames while `word_140D407D0` is non-zero.
- V: `sub_1402334FC` waits while `dword_140D408B8` or `dword_140D408BC` is set, and calls SceneTask_Terminate when `word_140D408F8` is 1.
- V: the task ends through SceneTask_Terminate after the block.
- I: the flag byte of opcode 0x45 selects between two outcomes whose full logic was not traced.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md), [EventScript_InstructionLength](EventScript_InstructionLength.md), [sub_140300D74](sub_140300D74.md), [sub_140300768](sub_140300768.md), [ScenePreview_FindEntry](ScenePreview_FindEntry.md), [ScenePreview_SlotOfIndex](ScenePreview_SlotOfIndex.md), [ScenePreview_ShowEntry](ScenePreview_ShowEntry.md), [ScenePreview_ClaimForUnit](ScenePreview_ClaimForUnit.md)

## Referenced by

- Started by event opcodes: [0x49](../opcodes/README.md)

## Notes

The opcode record for 0x49 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

The full logic of opcode 0x45 and its flag byte, what the preview unit table and ScenePreview_FindEntry return, and the meaning of `word_140D407D0` and `word_140D408F4`.
