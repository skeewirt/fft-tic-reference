# EventSequencer_TakeTurn

- **Address:** `0x1402334FC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSequencer_TakeTurn(int tag)`
- **Callers:** EventPanel_ShowTask (tag 12, call at 0x140233E86); EventSequence_RecordTask (tag 6, call at 0x14023357A); EventScript_Run (tag 13 in the 0x91 handler at 0x14023DA7C; tag 14 at 0x14023C177 in a path not identified here); EventUnitBlock_RunTask (tag 13 at 0x140235DD0, the 0x82 path); and routines sub_140233954, sub_14023397C, sub_1402339A8, sub_140233A28, sub_140233B24, sub_140233DA0, sub_1402357C4 and sub_1402C7EA8 (tags read from their call sites).
- **Callees:** SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Waits for the shared sequencer to be free, claims it by writing the caller's tag, waits until it is released, and ends the caller when the flag word at word_140D408F8 is 1.

## Behavior

- V: while dword_140D408B8 or dword_140D408BC is non-zero, calls SceneTask_WaitFrame.
- V: writes the argument (the tag) to dword_140D408B8. This is the claim.
- V: while dword_140D408B8 is non-zero, calls SceneTask_WaitFrame. Nothing in this routine writes it back to zero; other code releases it. sub_140234360 clears it with a value taken from a callback result, and sub_140243A60 and BattleLoad_StepFresh also write it (not traced here).
- V: when word_140D408F8 is 1 after the release, calls SceneTask_Terminate, which ends the calling task. Otherwise it returns.
- V: the return value is whatever the last wait left in the result register; no value is set on purpose.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Notes

The tag is the number written to dword_140D408B8; the routine does not test the claim again after the first wait. Tag 12 is the 0x7D panel, tag 6 the 0x76 record task and tag 13 the 0x91 handler.

## Open questions

Which code clears dword_140D408B8 and dword_140D408BC for each tag, and what the release value is; what sets the flag word at 0x140D408F8 (SceneTasks_Init and others write it).
