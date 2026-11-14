# EventPanel_ShowTask

- **Address:** `0x140233E64`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventPanel_ShowTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x7D.
- **Callees:** `sub_1402334FC`, `sub_14033D5C4`, `NaptrDnsRecordConvert_1`, `sub_14013B3AC`, `sub_1401DB4E4`, `sub_14033D4C0`, `sub_1402B2004`, `sub_1402B1DF0`, `sub_1402B1E40`, `sub_1402B1F08`, SceneCallback_Dispatch, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x7D: takes a turn in the shared sequencer, then shows a panel chosen by its operand from a language-dependent table and waits for that panel's work to finish.

## Behavior

- V: tags its task slot with the value 61 in qword_140D40B38[256 * dword_140D40948].
- V: calls sub_1402334FC(12, ...) to wait for and take the shared sequencer slot 12 before any work.
- V: sets the byte at qword_143CD9FD0 + 33 to 1.
- V: tail-calls sub_14033D5C4, which reads the first dword of its task block (the operand byte that EventScript_Run stored there) and uses it as a row index.
- V: the row table is unk_1407B4720 when the value at g_LanguageInfo + 8 is nonzero (or g_LanguageInfo is null), otherwise unk_1407B4A30; each row is 14 dwords, and the first dword of the row selects the branch.
- V: before the branch it calls NaptrDnsRecordConvert_1 with the same operand value; its result is not used.
- V: branch 0: looks up the title UI nodes by key (strings TitleL and TitleS, and Show) through sub_14013B3AC, runs sub_1401DB4E4 on qword_143CD9FD0, sets its fields (+34 to 257, +49 to 257, +51 to 1), waits frame by frame while a byte in the UI object is nonzero, then clears +49 and +51 and sets +34 to 256.
- V: branch 1: calls sub_14033D4C0, which runs sub_1402B2004, queues the value 50 with sub_1402B1DF0, and waits frame by frame while sub_1402B1E40 reports queued work (a queue entry exists and the high dword of `qword_141856AB0` is nonzero); it then sets the handler to sub_1402B1F08, calls SceneCallback_Dispatch(3, 1), and changes dword_1411A7D08 from 1 to 2.
- V: any other row value does nothing.
- V: at the end it clears the byte at qword_143CD9FD0 + 33 and ends through SceneTask_Terminate.

## State touched

- Calls: [SceneCallback_Dispatch](SceneCallback_Dispatch.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x7D](../opcodes/README.md)

## Notes

The opcode record for 0x7D (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the panel is (the UI nodes and the queued value 50); what NaptrDnsRecordConvert_1 really does (its IDB name may be wrong; not verified here); what the flag byte at qword_143CD9FD0 + 33 gates; the meaning of the table rows and fields.
