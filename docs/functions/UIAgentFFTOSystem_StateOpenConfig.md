# UIAgentFFTOSystem_StateOpenConfig

- **Address:** `0x140182860`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_StateOpenConfig(UIAgentFFTOSystem *agent, int phase)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

State handler that opens the General Options screen.

## Behavior

- V: enter: UI state 14 fade; each frame: when the fade is done, state 0; leave: the layout of `uiaddon.nxd` row 253 is loaded into +1456.
- I: this is agent state 3 (the order of the vtable entries and what each does).

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)

## Open questions

None recorded.
