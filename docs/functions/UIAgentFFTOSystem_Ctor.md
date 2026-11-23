# UIAgentFFTOSystem_Ctor

- **Address:** `0x140181C94`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOSystem_Ctor(UIAgentFFTOSystem *agent)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the System agent (1472 bytes), entry 37 of the agent manager's array.

## Behavior

- V: vtable 0x14070DF00; +1448 the system menu add-on, +1456 the General Options add-on, +1464 a third; +72 the state machine (UIAgent_SetState 0x1401CA59C, the setter, not called by this constructor: the old state's handler with 2, the new one's with 0, each frame with 1).

## Referenced by

- Called by: [UIAgentManager_CreateAgents](UIAgentManager_CreateAgents.md)

## Notes

Struct: UIAgentFFTOSystem.

## Open questions

None recorded.
