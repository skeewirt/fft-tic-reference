# LegacyOptions_RowTask

- **Address:** `0x140365F34`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyOptions_RowTask(void)`
- **Callers:** LegacyOptions_DrawTask
- **Callees:** sub_140361F74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task that edits one option row of the legacy options screen and packs the choices back.

## Behavior

- V: left / right changes the option's choice within its choice count; the selection starts from the defaults when asked.
- V: repacks the 12 choices into the option word and refreshes the live key repeat settings.

## Referenced by

- Called by: [LegacyOptions_DrawTask](LegacyOptions_DrawTask.md)

## Open questions

None recorded.
