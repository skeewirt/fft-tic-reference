# LegacyMenu_NumberEntryTask

- **Address:** `0x140360E58`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_QWORD *LegacyMenu_NumberEntryTask(void)`
- **Callers:** the task entry of node 16 of the old world menu node table (LegacyWorldMenuNodes); also reached from sub_140334898
- **Callees:** sub_14022627C, sub_1402E2C54, sub_14021F7BC, sub_140361F74, sub_1403619DC, VramPage_CopyRect, EventTask_WaitFrame, sub_1402D8150, sub_1402E2BCC, sub_1402E2AD8, LegacyMenu_ConfirmRow, Input_TestAction, sub_140360AF8, sub_1402E2FCC, sub_1402E303C, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of node 16 (row 7 of the old main world menu): a number entry window whose confirm calls the range record's function. In node 16 the range is 1..200 and the function starts a test battle on that map.

## Behavior

- V: the node record of the running task is the first qword of the task slot's 2048-byte block in the event task table (slot number dword 0x14184B22C). Record +64 points to a range record (min word +0, max word +2, function pointer +8); record +72 points to the number word. Node 16 (and 17) use the range record at 0x1407893A0 (1, 200, LegacyWorldMenu_StartTestBattle) and the number word 0x140789374 (1 at start); these addresses are node record data, reached through record +64 / +72.
- V: a start value outside min..max becomes min; the digit count comes from sub_14022627C(max).
- V: Right (action 36, mask 0x2000) and Left (action 35, mask 0x8000) move the digit cursor (the step values are dwords at 0x1406919C0); Up (33, mask 0x1000) adds the digit step and wraps to min past max; Down (34, mask 0x4000) subtracts and wraps to max below min. The window is redrawn after a change.
- V: each frame it calls sub_1402E2AD8 and LegacyMenu_ConfirmRow(record, 0); when that consumed the input it stores the number (or restores the old one when the row came back -1) and calls the range record's function.
- V: node 16's own row list is [-2, -1, ...], so the confirm also closes two levels.
- V: the loop ends when sub_1402E2BCC(input) reports a close; then a frame wait and EventTask_Terminate.

## State touched

- Calls: [sub_14022627C](sub_14022627C.md), [VramPage_CopyRect](VramPage_CopyRect.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [LegacyMenu_ConfirmRow](LegacyMenu_ConfirmRow.md), [Input_TestAction](Input_TestAction.md), [EventTask_Terminate](EventTask_Terminate.md)

## Notes

The Left / Right / Up / Down names of actions 33 to 36 come from the game's own input action table (LocationsListInputActions).

## Open questions

None recorded.
