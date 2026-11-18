# UIAgentFFTOTitle_OnAddonEvent

- **Address:** `0x1401C32D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOTitle_OnAddonEvent(UIAgentFFTOTitle *agent, UIAddon *from, int event, int arg)`
- **Callers:** the add-ons' events (through the agent's vtable +48)
- **Callees:** UITitle_OnMenuAction, TitleMenu_Build

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The agent's sink (slot 6) for the events of its three add-ons: the menu, the play mode screen and the saving screen.

## Behavior

- V: for the menu add-on: event 0 calls `UITitle_OnMenuAction(agent, kind)` (its one call, at 0x1401C33B3); event 1 (idle timeout) starts a fade (UI state 6) and agent state 0x701; event 65537 rebuilds or reopens the menu.
- V: for the play mode add-on: event 0 goes to 0x1401C3D88, 65538 goes to 0x1401C3C24, 65539 shows a notice with UI text 23001 / 23003 / 23010 / 23011.

## State touched

- Calls: [UITitle_OnMenuAction](UITitle_OnMenuAction.md), [TitleMenu_Build](TitleMenu_Build.md)

## Referenced by

- Appears in flows: [TitleMenuAction](../flows/TitleMenuAction.md)

## Open questions

None recorded.
