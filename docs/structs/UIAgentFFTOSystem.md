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
| <a id="state"></a>`0x48` | state | `int32` | V | The state machine (UIAgent_SetState 0x1401CA59C: the old state's handler with 2, the new one's with 0; each frame with 1). |
| <a id="system_menu_addon"></a>`0x5A8` | system_menu_addon | `UIAddon *` | V | The system menu add-on. |
| <a id="config_addon"></a>`0x5B0` | config_addon | `UIAddonFFTOConfig *` | V | The General Options add-on. |
| <a id="third_addon"></a>`0x5B8` | third_addon | `UIAddon *` | ? | A third add-on; its use was not read. |

## Behavior

- V: opened by UIAgentFFTOSystem_OpenConfig (mode, state 3); closed by state 4; the exit state (2) fades to UI state 13 and sets the application's quit request byte.

## Open questions

None recorded.
