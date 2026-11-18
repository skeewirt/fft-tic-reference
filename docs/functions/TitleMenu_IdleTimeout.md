# TitleMenu_IdleTimeout

- **Address:** `0x1401C41B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_IdleTimeout(UIAddonFFTOTitle *addon)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title menu's idle timeout (vtable slot 14): after 8000 ticks without input the agent is told to go back to the opening.

## Behavior

- V: with +230 set and no other screen pending, when 8000 ticks of `g_GUICore`+2096 have passed since +224, calls the agent's vtable +48 with event 1.

## Notes

The agent answers event 1 with a fade (UI state 6) and agent state 0x701 (see UIAgentFFTOTitle_OnAddonEvent).

## Open questions

None recorded.
