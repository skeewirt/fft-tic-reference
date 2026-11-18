# EventMessage_Task

- **Address:** `0x1402238C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventMessage_Task(void)`
- **Callers:** None directly; passed to SceneTask_Start by nine routines.
- **Callees:** SceneTask_WaitFrame, EventText_NextChar, `sub_140226A18`, `sub_140226664`, `sub_1402212B4`, `sub_140331EEC`, `sub_1400FC598`, `sub_14022347C`, `sub_140233368`, and others

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The dialogue-window task: it shows an event message in a speech window, pages through the text and waits for the player. It is the entry function of tasks started with SceneTask_Start and is by far the largest routine in the event code.

## Behavior

- V: started as a task entry from nine places through SceneTask_Start, including the event interpreter, where opcode 0x10 starts it on a slot chosen from the operand byte at offset 1; it has no direct callers.
- V: resolves who is speaking through `sub_140226A18`, which maps a speaker id to a unit in the preview table (special ids 104 and 105 search the preview table for a unit).
- V: reads the message through EventText_NextChar (15 uses) and builds the window with `sub_1402212B4`, `sub_140331EEC` and `sub_140332330`.
- V: animates the window with the rectangle interpolation `sub_140226664` and the frame routines `sub_1402262C0` and `sub_14025FCDC`.
- V: waits for the player with button-group tests (`sub_1400FC598` with ids 0x1A, 0x1B, 0x20, 0x21, 0x22 and 0x39) and calls SceneTask_WaitFrame 14 times.
- V: the decompilation has about 1,740 lines and no strings; its state lives in a local record and in the task's block in the second task table.
- I: this is the routine the older research called the main event loop; by what it does it is the message-window task, not a general event interpreter.
- V (2026-11-09, choice): in its byte switch `0xFB` stores the current line number as the first option row (local, 0xFFFF when unset) and `0xFC` runs the choice loop: each frame it places the glove sprite on the cursor line (sprite records of 584 bytes; the table base 0x142FEF870 is inside sub_14021F850, which this task calls, not in this body), waits one frame, then leaves on task tag 3 or `word_142FEC554`; otherwise it reads UP (action 0x21, mask 0x1000), DOWN (0x22, 0x4000) and confirm (0x1A, 0x20) with Input_TestAction. The cursor starts on the first option row and stays between it and the last line reached.
- V: on confirm it writes `cursor - first option row` to dword 24 of the event variable store (`off_1407830D8`, a pointer whose stored value is 0x140D40060, so the address is reached through the pointer, not as an immediate), event variable 24, sets the confirm sound, hides the glove and continues; a `0xFC` with no `0xFB` before it does nothing.
- V: the choice loop reads no fast-forward or auto-advance state and no cancel action; the ordinary page wait (`0xFE`) is the loop with those tests.
- V: while `word_142FEC554`, `word_141874530`, `word_1437F664C` is set, or `g_EventSkipEnabled` and the skip state (high dword of g_ScreenFade) are both non-zero, every byte read is replaced by 0xFE, so a choice is passed without being shown or answered.
- V: the message id is the dword at block +8 of its task block (kind = bits 11..15 picks the pool through g_TextPoolTable, decoder sub_140226208), the speaker reference the dword at +16.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [EventText_NextChar](EventText_NextChar.md), [Input_TestAction](Input_TestAction.md), [SceneVar_Write](SceneVar_Write.md), [sub_1401365AC](sub_1401365AC.md), [sub_140136654](sub_140136654.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_EventSkipEnabled](../globals/g_EventSkipEnabled.md)

## Referenced by

- Observed behaviours: [StoryChoiceBalloon](../behaviors/StoryChoiceBalloon.md)
- Reads tables: [PowersOfTen](../tables/PowersOfTen.md)
- Started by event opcodes: [0x10](../opcodes/README.md)

## Notes

Named for its observable job. The real event-script interpreter (the code that executes event opcodes) is a separate routine that is still unresolved.

## Open questions

Which routine interprets event opcodes, and how the message window picks its position and size.
