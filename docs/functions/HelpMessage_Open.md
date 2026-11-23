# HelpMessage_Open

- **Address:** `0x14036D948`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t HelpMessage_Open(int textId)`
- **Callers:** EventViewer_ListInput, MenuCtl_Entry43, MenuCtl_Entry44, MenuCtl_Entry45, StatusGlossary_Input, Errand_ReportListInput, Errand_RunningListInput, MenuCtl_Entry26, MenuCtl_Entry24, MenuCtl_Entry28, sub_140375CD0, MenuCtl_Entry33, sub_140376CA8, Errand_StatusMenuInput, Errand_ProgressListInput, Errand_FinishListInput, sub_140372F9C
- **Callees:** Resource_GetSlotObject, EventTask_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the help message screen for a text id: starts the scripted message task and pushes kind 3.

## Behavior

- V: starts the event task EventMessage_Scripted (slot 2) and writes the text id and a style (51, or 59 when mask 0x20000 of the state dword is set) into the message object.
- V: pushes kind 3 with record dword 0 = 1, dword 1 = the previous value of 0x140D498D0, dword 2 = 0 and dword 3 = 8; it sets 0x140D498D0 to -1 and plays cue 0x12.

## State touched

- Calls: [Resource_GetSlotObject](Resource_GetSlotObject.md), [EventTask_Start](EventTask_Start.md)

## Referenced by

- Called by: [Errand_FinishListInput](Errand_FinishListInput.md), [Errand_ProgressListInput](Errand_ProgressListInput.md), [Errand_ReportListInput](Errand_ReportListInput.md), [Errand_RunningListInput](Errand_RunningListInput.md), [Errand_StatusMenuInput](Errand_StatusMenuInput.md), [MenuCtl_Entry24](MenuCtl_Entry24.md), [MenuCtl_Entry26](MenuCtl_Entry26.md), [MenuCtl_Entry28](MenuCtl_Entry28.md), [MenuCtl_Entry33](MenuCtl_Entry33.md), [MenuCtl_Entry43](MenuCtl_Entry43.md), [MenuCtl_Entry44](MenuCtl_Entry44.md), [MenuCtl_Entry45](MenuCtl_Entry45.md), [StatusGlossary_Input](StatusGlossary_Input.md)

## Notes

The list screens call it with a help text id when the help action (0x20) is pressed.

## Open questions

? the id ranges of the help texts (ids of 4096 and up were seen as arguments).
