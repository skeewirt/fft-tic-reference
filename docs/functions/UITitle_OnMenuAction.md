# UITitle_OnMenuAction

- **Address:** `0x1401C3710`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitle_OnMenuAction(UIAgentFFTOTitle *agent, int kind)`
- **Callers:** UIAgentFFTOTitle_OnAddonEvent
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Carries out the row the player chose on the title menu.

## Behavior

- V: kind 0 goes to `UITitle_OpenPlayMode`; kind 1 to `UITitle_StartNewGamePlus`; kind 2 to `UITitle_StartContinue`; kind 3 to `UITitle_StartLoadGame`.
- V: kind 4 (Music Player) fades out and sets agent state 0x501; kind 5 (Select Version) fades out and sets agent state 0x601. Any other kind does nothing.

## Referenced by

- Appears in flows: [TitleMenuAction](../flows/TitleMenuAction.md)
- Called by: [UIAgentFFTOTitle_OnAddonEvent](UIAgentFFTOTitle_OnAddonEvent.md)

## Notes

Registry: TitleMenuEntryKinds.

## Open questions

None recorded.
