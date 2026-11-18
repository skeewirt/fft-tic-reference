# LegacyOptions_Open

- **Address:** `0x140364D2C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyOptions_Open(void)`
- **Callers:** sub_1402B3B88, sub_1402E99C8, sub_1402E99F0
- **Callees:** EventTask_Start (starts the draw task LegacyOptions_DrawTask), EventTask_Terminate, EventTask_WaitFrame, sub_140364408, sub_1403664E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the legacy options screen: unpacks the option word into the 12 live choices.

## Behavior

- V: the option word 0x140782A24 holds the choices (3-bit fields for the first five, 2-bit fields for the rest); each is stored in the live choices array (0x1408FA460).
- V: sets a flag when every live choice equals its default (0x1408FA420) and starts the draw task.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [LegacyOptions_DrawTask](LegacyOptions_DrawTask.md), [EventTask_Terminate](EventTask_Terminate.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [sub_140364408](sub_140364408.md)

## Open questions

None recorded.
