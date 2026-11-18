# LegacyOptions_DrawTask

- **Address:** `0x140364FAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyOptions_DrawTask(void)`
- **Callers:** LegacyOptions_Open
- **Callees:** EventTask_Start (starts LegacyOptions_RowTask), EventTask_WaitFrame, Input_TestAction, VramPage_CopyRect, sub_140242AFC, sub_1402E2C54

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task that draws the legacy options window and handles its cursor.

## Behavior

- V: lays out one row per option with the choice texts (message id = text base of the option + the live choice) and the cursor cells.
- V: copies the key repeat preset row (6 bytes chosen by option bits 9..11) into the live repeat settings.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [LegacyOptions_RowTask](LegacyOptions_RowTask.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [Input_TestAction](Input_TestAction.md), [VramPage_CopyRect](VramPage_CopyRect.md), [sub_140242AFC](sub_140242AFC.md)

## Referenced by

- Called by: [LegacyOptions_Open](LegacyOptions_Open.md)

## Open questions

None recorded.
