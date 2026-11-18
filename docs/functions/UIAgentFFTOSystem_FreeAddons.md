# UIAgentFFTOSystem_FreeAddons

- **Address:** `0x140181DD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_FreeAddons(UIAgentFFTOSystem *agent)`
- **Callers:** not recorded
- **Callees:** UIAgent_DetachAddon

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Frees the add-ons at +1448 / +1456 / +1464.

## Behavior

- V: frees the General Options add-on through UIAgent_DetachAddon.

## State touched

- Calls: [UIAgent_DetachAddon](UIAgent_DetachAddon.md)

## Referenced by

- Called by: [UIAgentFFTOSystem_StateCloseConfig](UIAgentFFTOSystem_StateCloseConfig.md)

## Open questions

None recorded.
