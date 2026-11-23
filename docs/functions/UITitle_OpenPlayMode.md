# UITitle_OpenPlayMode

- **Address:** `0x1401C3968`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitle_OpenPlayMode(UIAgentFFTOTitle *agent)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Kind 0 (New Game): starts UI state 19 and agent state 2, after which the agent hides the menu and shows the play mode screen.

## Behavior

- V: the menu action for kind 0 jumps here; the agent in state 2 then runs `UITitle_ShowPlayMode`.

## Referenced by

- Appears in flows: [TitleMenuAction](../flows/TitleMenuAction.md)
- Called by: [TitleScene_Update](TitleScene_Update.md)

## Notes

This name replaces an earlier, misleading one (`UITitle_Reopen`).

## Open questions

None recorded.
