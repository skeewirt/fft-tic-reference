# UIAgentFFTOSystem_OnAddonEvent

- **Address:** `0x140181ED0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_OnAddonEvent(UIAgentFFTOSystem *agent, UIAddon *addon, int event)`
- **Callers:** UIAddon event dispatch
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Agent vtable slot 6, the sink of its add-ons' events.

## Behavior

- V: from the General Options add-on, event 0 selects state 4 (close); from the system menu add-on, event 0 calls 0x140182208 (its rows) and events 1 / 2 select states 1 / 2.

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)

## Open questions

None recorded.
