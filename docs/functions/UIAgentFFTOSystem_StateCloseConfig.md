# UIAgentFFTOSystem_StateCloseConfig

- **Address:** `0x14018290C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_StateCloseConfig(UIAgentFFTOSystem *agent, int phase)`
- **Callers:** not recorded
- **Callees:** UIAgentFFTOSystem_FreeAddons

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

State handler that closes the General Options screen.

## Behavior

- V: enter: fade to UI state 14 and hide +1456; when the fade is done: the system menu again if +1448 exists, else UIAgentFFTOSystem_FreeAddons; state 0.
- I: this is agent state 4.

## State touched

- Calls: [UIAgentFFTOSystem_FreeAddons](UIAgentFFTOSystem_FreeAddons.md)

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)

## Open questions

None recorded.
