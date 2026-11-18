# TitleMenu_StampInput

- **Address:** `0x1401C40C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_StampInput(UIAddonFFTOTitle *addon)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records the time of the last input for the idle timeout.

## Behavior

- I: stores `g_GUICore`+2096 (the millisecond tick) into +224; the field is read by TitleMenu_IdleTimeout.

## Open questions

None recorded.
