# UIAgentFFTOSystem_OpenConfig

- **Address:** `0x140182478`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_OpenConfig(UIAgentFFTOSystem *agent, int mode)`
- **Callers:** Boot_Update, 0x140181DA0, 0x140182208
- **Callees:** UIAddonFFTOConfig_Ctor, UIAgent_AttachAddon

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes the General Options add-on and starts the agent's open state.

## Behavior

- V: `Mem_Alloc(3416)`, UIAddonFFTOConfig_Ctor, `UIAgent_AttachAddon`, +1456 = the add-on, add-on +52 = mode, agent state 3.
- V: callers (addresses of the calling functions, not in this body): `Boot_Update` (the mode select's General Options, mode 1, only when the agent is not active), 0x140181DA0 (same check), 0x140182208 (the in-game menu, mode 0).

## State touched

- Calls: [UIAddonFFTOConfig_Ctor](UIAddonFFTOConfig_Ctor.md), [UIAgent_AttachAddon](UIAgent_AttachAddon.md)

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md)

## Open questions

None recorded.
