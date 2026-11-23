# UIAgentFFTOSystem

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1472 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The System agent: entry 37 of the agent manager's array (`*(qword_143CD9DA8 + 16) + 37 * 8`, as Boot_Update reads it); 1472 bytes, constructor 0x140181C94, vtable 0x14070DF00.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="state_owner"></a>`0x48` | state_owner | `void *` | V | Owner pointer of the 32-byte state control block at +0x48 (handler +0x50, selector +0x58, state +0x60). |
| <a id="state_handler"></a>`0x50` | state_handler | `void *` | V | The current state handler; UIAgent_SetState updates it after the selector returns. |
| <a id="state_selector"></a>`0x58` | state_selector | `void *` | V | The state selector; called with the new state id, returns the handler. |
| <a id="state"></a>`0x60` | state | `int32` | V | The state id (control block +0x18, agent +0x60); UIAgent_SetState writes it. |
| <a id="system_menu_addon"></a>`0x5A8` | system_menu_addon | `UIAddon *` | V | The system menu add-on. |
| <a id="config_addon"></a>`0x5B0` | config_addon | `UIAddonFFTOConfig *` | V | The General Options add-on. |
| <a id="third_addon"></a>`0x5B8` | third_addon | `UIAddon *` | ? | A third add-on; its use was not read. |

## Behavior

- V: opened by UIAgentFFTOSystem_OpenConfig (mode, state 3); closed by state 4; the exit state (2) fades to UI state 13 and sets the application's quit request byte.

## Open questions

None recorded.
