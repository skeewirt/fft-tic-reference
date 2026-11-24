# LegacyWorldMenu_RequestEventVarEditor

- **Address:** `0x1402B3D1C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t LegacyWorldMenu_RequestEventVarEditor(void)`
- **Callers:** the task entry of node 15 of the old world menu node table (LegacyWorldMenuNodes)
- **Callees:** EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of node 15 (row 8 of the old main world menu): sets the event variable editor request word and ends.

## Behavior

- V: sets word 0x143749F38 = 1, clears and copies the input words like LegacyWorldMenu_RequestRoster and ends with EventTask_Terminate.
- V (read in LegacyWorldMenu_FrameStep and ClassicMenu_HubStep): LegacyWorldMenu_FrameStep turns the word into mask 0x800000 of the state dword, and ClassicMenu_HubStep then calls EventVarEditor_Open.
- V: the four language node tables are its only references (node 15, +48).

## State touched

- Calls: [EventTask_Terminate](EventTask_Terminate.md)

## Open questions

None recorded.
