# TitleMenuAction

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

From a press on a title menu row to the action: the button event reaches the agent, which dispatches on the row's kind.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [UIAddonFFTOTitle_OnEvent](../functions/UIAddonFFTOTitle_OnEvent.md) | V | Event 16 (decide): input lock 0.1 s, sound 0xFC, then the agent's vtable +48 call with the row's kind. |
| <a id="2"></a>2 | [UIAgentFFTOTitle_OnAddonEvent](../functions/UIAgentFFTOTitle_OnAddonEvent.md) | V | For the menu add-on, event 0 calls UITitle_OnMenuAction(agent, kind). |
| <a id="3"></a>3 | [UITitle_OnMenuAction](../functions/UITitle_OnMenuAction.md) | V | Dispatches on the kind (registry TitleMenuEntryKinds). |
| <a id="4"></a>4 | [UITitle_OpenPlayMode](../functions/UITitle_OpenPlayMode.md) | V | Kind 0: UI state 19 and agent state 2; the agent then runs UITitle_ShowPlayMode. |

## Behavior

- V: the idle timeout (TitleMenu_IdleTimeout) takes the same road with event 1: fade (UI state 6) and agent state 0x701, back to the opening.

## Open questions

None recorded.
