# EventMenu_NodeListTask

- **Address:** `0x1402E38E4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *EventMenu_NodeListTask(void)`
- **Callers:** EventMenu_WaitThenListTask, sub_1402EB408, BattleCommand_CommitCursor, sub_1402EB914, sub_140364408 (stores its address); node task entry in the old world menu node tables (node 20) and in other node tables
- **Callees:** sub_1402E2C54, sub_140361F74, sub_1402EC9D0, VramPage_CopyRect, Guide_TryAutoShow, sub_1400E5F78, sub_1400E620C, EventTask_WaitFrame, sub_1402D8150, LegacyMenu_ConfirmRow, sub_1402E2AD8, sub_1402E2BCC, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The generic list task of the event-side menu nodes: draws the node's window and title text, then loops on input until the node closes. Node 20 of the old world menu runs it (I: as row 10 of node 4, see LegacyWorldMainMenuRows).

## Behavior

- V: the node record of the running task is the first qword of the task slot's 2048-byte block in the event task table (slot number dword 0x14184B22C); the start row is record +80 (-1 reads as 0); it builds the window (sub_1402E2C54, sub_140361F74).
- V: it looks the record up in the 156-pointer menu descriptor array at g_CharaRenderMgr +6256 (index -1 when absent) and draws the title text whose id is the low word of record +28 (sub_1402EC9D0).
- V: descriptor indexes select special set-ups (132, 128, 40, 141, 143, 25..27, 30, 37, 38, ...); an absent record (-1) skips them and goes straight to the frame loop.
- V: the frame loop waits a frame each pass and reads input through LegacyMenu_ConfirmRow (confirm) and sub_1402E2AD8 (cancel); it has exits, and after the loop it waits a frame and calls EventTask_Terminate unless the slot block's second qword is set.
- V (node record data, reached through the record pointer): node 20 of the old world menu: title text id 0x5012 (record +28 = 0x15012), a 56 x 48 window (40 x 48 in the other languages) at x 324, y 96, saved-row word +80 = 1, row word +40 = -1 (every row closes one level), row pointer +72 = 0x140D405A0.
- ?: what text 0x5012 shows; the node's title is drawn from the text data, which was not read here.
- I: since its row word is -1 a confirm or cancel closes node 20 like any other node; nothing in this task keeps it open.

## State touched

- Calls: [sub_1402EC9D0](sub_1402EC9D0.md), [VramPage_CopyRect](VramPage_CopyRect.md), [Guide_TryAutoShow](Guide_TryAutoShow.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [LegacyMenu_ConfirmRow](LegacyMenu_ConfirmRow.md), [EventTask_Terminate](EventTask_Terminate.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Referenced by

- Called by: [EventMenu_WaitThenListTask](EventMenu_WaitThenListTask.md)

## Notes

9,265 bytes; only the head, the descriptor lookup, the frame loop's confirm / cancel calls and the exit were read.

## Open questions

None recorded.
