# EventPanel_PickRow

- **Address:** `0x14033D5C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventPanel_PickRow(void)`
- **Callers:** EventPanel_ShowTask (tail call at 0x140233E9A). A data reference at 0x143D3E494 was not traced.
- **Callees:** `sub_14013B3AC`, `sub_1401DB4E4`, NaptrDnsRecordConvert_1 (name not verified), EventPanel_QueueAndWait, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The second half of the 0x7D task: reads the row number the task stored in its block, picks that row of a language-dependent panel table and runs the branch for the row kind.

## Behavior

- V: reads the signed dword at +0 of the running task block. The 0x7D handler stored the operand byte there, zero-extended, and that value is the row number. It is used without a range check.
- V: calls NaptrDnsRecordConvert_1 with that dword as its only argument and ignores the result. The IDB name of that routine was not checked in this pass.
- V: the table is unk_1407B4720 when the global g_LanguageInfo is null or the dword at +8 of it is not zero; otherwise it is unk_1407B4A30. A row is 14 dwords (56 bytes), so the row starts at table + 56 times the row number.
- V: the first dword of the row is the kind. Kind 0 runs the title-panel branch, kind 1 calls EventPanel_QueueAndWait, and any other kind does nothing.
- V: title-panel branch: takes the object at +88 of the object whose pointer is at +104 of the object at +16 of the global qword_143CD9DA8, calls sub_14013B3AC with that object and the row number, and calls sub_1401DB4E4 on the UI global qword_143CD9FD0.
- V: sets the word at +34 of qword_143CD9FD0 to 257, the word at +49 to 257 and the byte at +51 to 1.
- V: waits one frame per pass with SceneTask_WaitFrame while the byte at +416 of the object at +48 of the object at +88 is not zero.
- V: then sets the word at +49 to 0, the byte at +51 to 0 and the word at +34 to 256.
- V: in every case it then clears the byte at +33 of qword_143CD9FD0 and ends through SceneTask_Terminate.

## State touched

- Calls: [EventPanel_QueueAndWait](EventPanel_QueueAndWait.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Reads tables: [EventPanelRowsDefault](../tables/EventPanelRowsDefault.md), [EventPanelRowsLanguage0](../tables/EventPanelRowsLanguage0.md)

## Notes

The table holds rows 0 to 13 in the 784 bytes from unk_1407B4720 to unk_1407B4A30. In both tables rows 0 to 6 have kind 0, row 7 has kind 1 and rows 8 to 12 have kind 2.

## Open questions

What sub_14013B3AC does with the row number (it passes it on to two text routines); the meaning of the other dwords of each row; whether NaptrDnsRecordConvert_1 has side effects; what the table holds past row 13, which an operand of 14 or more would read; what the flag at +33 gates in other code.
