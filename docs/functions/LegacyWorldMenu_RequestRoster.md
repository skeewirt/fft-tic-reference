# LegacyWorldMenu_RequestRoster

- **Address:** `0x1402B3D80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t LegacyWorldMenu_RequestRoster(void)`
- **Callers:** the task entry of node 7 of the old world menu node table (LegacyWorldMenuNodes)
- **Callees:** EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of node 7 (row 1 of the old main world menu): sets the roster request word and ends.

## Behavior

- V: sets word 0x143749F28 = 1, clears the input words (off_1408093A8 and off_1408B9A48), copies the five input dwords and ends with EventTask_Terminate.
- V: LegacyWorldMenu_StepRosterRequest runs the request from there.

## State touched

- Calls: [EventTask_Terminate](EventTask_Terminate.md)

## Open questions

None recorded.
