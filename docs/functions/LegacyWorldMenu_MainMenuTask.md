# LegacyWorldMenu_MainMenuTask

- **Address:** `0x1402B50A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t LegacyWorldMenu_MainMenuTask(void)`
- **Callers:** the task entry of nodes 3 and 4 of the old world menu node table (LegacyWorldMenuNodes) (started by LegacyMenu_ConfirmRow or LegacyWorldMenu_OpenNode)
- **Callees:** sub_1402E2C54, EventTask_WaitFrame, sub_1402E303C, sub_1402E3100, sub_1402E2BCC, sub_1402E2650, Input_ActionBit, LegacyMenu_ConfirmRow, sub_1400EBF88, sub_1400EBFC4, sub_1402E2AD8, WorldMapAgent_IsMapShown, sub_1400EDCB4, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of nodes 3 and 4 of the old world menu (node 4 = the old main world menu). Its input is cut down: the only row it ever confirms is row 1, the roster, and only when a roster request code is waiting.

## Behavior

- V: the node record of the running task is the first qword of the task slot's 2048-byte block in the event task table (slot number dword 0x14184B22C); the start row is the record's word +80 (0 when it reads -1), and it is written back each frame.
- V: each frame it runs sub_1402E303C and sub_1402E3100 (I: the window and its row cursor) and leaves the loop when sub_1402E2BCC(input) reports a close or when dword 0x142E7FF68 is 2; in both cases a value of 2 becomes 3.
- V: it acts only when the slot below has no task, the request words g_CharaRenderMgr +13452 and +13448 differ and sub_1402E2650 allows it.
- V: with word_143749F28 at 0, a request code 1000 or 2000 in g_CharaRenderMgr +13448 sets the row to 1, puts the confirm action bit (action 26) in the input word and calls LegacyMenu_ConfirmRow(record, 1); code 1000 also sets dword 0x14078D638 to 0 unless it is 166. No other row is confirmed anywhere in the function.
- V: once word_143749F28 reaches 9 (the roster sequence has run, see LegacyWorldMenu_StepRosterRequest) it ends: with a request code set it calls sub_1400EBF88 and clears +13452; without one it calls sub_1400EBFC4, puts the cancel action bit (27) in the input word, runs sub_1402E2AD8 (I: the node's cancel) and sets dword 0x14078D638 to -1. With the world map shown (WorldMapAgent_IsMapShown) it calls sub_1400EDCB4(1).
- V: it ends with a frame wait and EventTask_Terminate.
- I: the current world map screens place the roster request (codes 1000 / 2000) and this task turns it into the old row-1 confirm, so the other rows of node 4 (LegacyWorldMainMenuRows) are dead.

## State touched

- Calls: [EventTask_WaitFrame](EventTask_WaitFrame.md), [LegacyMenu_ConfirmRow](LegacyMenu_ConfirmRow.md), [WorldMapAgent_IsMapShown](WorldMapAgent_IsMapShown.md), [EventTask_Terminate](EventTask_Terminate.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Referenced by

- Resolves registries: [LegacyWorldMainMenuRows](../registries/LegacyWorldMainMenuRows.md)

## Notes

The IDB name of the dword 0x14078D638 suggests a table, but the code stores small integers in it (166, 0, -1) and LegacyWorldMenu_FrameStep plays sound cue (value - 1) when it is not -1.

## Open questions

None recorded.
