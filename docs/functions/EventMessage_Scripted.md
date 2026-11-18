# EventMessage_Scripted

- **Address:** `0x1402DB09C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventMessage_Scripted(void)`
- **Callers:** `sub_14032D31C`; also started as a task entry from seven sites
- **Callees:** EventText_FindMessage, EventText_NextChar, EventTask_WaitFrame, EventVar_Read, EventVar_Write, EventTask_Terminate, `sub_1402DDC44`, `sub_1402DDFE8`, `sub_1402DE204`, `sub_1400FC598`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The dialogue-window task used by the first task table: it shows a scripted event message, pages through the text and waits for the player. It is the counterpart of EventMessage_Task, which runs in the second table.

## Behavior

- V: called from `sub_14032D31C` and referenced as an entry function from seven places in the code.
- V: finds the message with EventText_FindMessage (4 uses) and steps through it with EventText_NextChar (16 uses).
- V: builds and animates the window with `sub_1402DDC44` (writes the window frame's corner rectangles) and `sub_1402DDFE8` (window open and close animation, which waits one frame per step through EventTask_WaitFrame).
- V: resolves the speaker through `sub_1402DE204`, the same unit lookup as `sub_140226A18` that EventMessage_Task uses.
- V: waits for the player with 11 button-group tests and calls EventTask_WaitFrame 13 times; it writes event variables three times and reads one.
- V: ends through EventTask_Terminate.
- I: the two message tasks are the same feature built for the two task tables; this one is driven by event scripts.
- V (2026-11-08): the speaker's look index is the same sum as sub_14032AB3C's on the save record of the speaker (marker 0x80: 2 * job - 52, 0x81 (tested by subtracting 0x80, then 1): 2 * job - 51, Mime two less), read against g_PortraitCodeD.
- V (2026-11-09, choice): the same 0xFB / 0xFC choice codes as EventMessage_Task (cases in its byte switch): 0xFB records the first option row, 0xFC runs the up / down / confirm loop (actions 0x21, 0x22, 0x1A) and stores the picked index at dword 24 of `g_EventWorkPtr`, event variable 24; the first-table task state it tests is the word at block +0x98 of its block (3 = terminate).

## State touched

- Calls: [EventText_FindMessage](EventText_FindMessage.md), [EventText_NextChar](EventText_NextChar.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md), [EventTask_Terminate](EventTask_Terminate.md), [sub_1401365AC](sub_1401365AC.md), [sub_140136654](sub_140136654.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_PortraitCodeD](../globals/g_PortraitCodeD.md)

## Referenced by

- Called by: [EventCmd_ShowMessage](EventCmd_ShowMessage.md)
- Observed behaviours: [LookSitesUseTheSaveRecordNotTheSlot](../behaviors/LookSitesUseTheSaveRecordNotTheSlot.md), [LookSumSeesTheBaseJob](../behaviors/LookSumSeesTheBaseJob.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [StoryChoiceBalloon](../behaviors/StoryChoiceBalloon.md)
- Reads tables: [JobTable](../tables/JobTable.md), [PortraitCodes](../tables/PortraitCodes.md)

## Notes

About 11,000 bytes and 1,900 decompiled lines. The event-opcode interpreter that decides to open a message is still unresolved.

- V (2026-10-29): one of the 15 JobTable bound-readers (an 8-bit compare against 0xAE); of the JobTable row it reads bytes 46 and 47 (shape / palette), through the table pointer. J7 had listed it as reading the skillset byte only; that was wrong.
- V (2026-11-08): the speaker's portrait code comes from its own copy of the portrait code words (0x140681A90, read at 0x1402DB41E) with the index guard at 0x1402DB481 (compare with 0xD3); out of range the code is 0 (the register zeroed at entry). Job 91 forces index 130, job 92 index 131; for marker 0x82 the job row byte 47 goes into bits 10 and 11.

## Open questions

Which routine interprets event opcodes and starts this task.
