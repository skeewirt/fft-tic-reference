# UIAgentFFTOSystem_StateExitGame

- **Address:** `0x1401827E4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_StateExitGame(UIAgentFFTOSystem *agent, int phase)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

State handler that exits the game: UI state 13 fade, then the application's quit request byte is set.

## Behavior

- V: sets `g_Application` +0x5F0 = 1 when the fade is done; Game_Main's loop ends on it after the current frame.
- I: this is agent state 2.

## Referenced by

- Observed behaviours: [QuitRequest](../behaviors/QuitRequest.md)

## Notes

Behavior: QuitRequest. Replaces the name UIAgentFFTOSystem_StateExitGame, a guess from the byte it writes.

## Open questions

None recorded.
