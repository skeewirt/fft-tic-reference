# Input

Pointer polling and input state.

Functions: 15, Structures: 2, Globals: 1.

## Functions (15)

| Name | Address | Purpose |
|---|---|---|
| [GUIInput_IsPointerOverLayer](../functions/GUIInput_IsPointerOverLayer.md) | `0x1400FE2D0` | Tells whether the mouse pointer is over a widget and hits a target tagged with the given id. |
| [Input_IsActionHeld](../functions/Input_IsActionHeld.md) | `0x1400F0D4C` | True while any of the three bindings of an action row (one pad button, two keys) is held down. |
| [Input_IsCtrlHeld](../functions/Input_IsCtrlHeld.md) | `0x140021F2C` | Returns true when Ctrl is held **and** Shift is not, no Windows key is down, and a pad state bit is clear. |
| [Input_IsShiftHeld](../functions/Input_IsShiftHeld.md) | `0x140021F9C` | Returns true when Shift is held and Ctrl is not, no Windows key is down, and the ctx pad bit is clear. |
| [Input_ListenerBroadcast](../functions/Input_ListenerBroadcast.md) | `0x1400E3AD8` | Delivers the frame's merged input state to the UI core: merges the input object's state into `state`, calls GUICore_OnInputState, then copies the 0x548-byte state back. |
| [Input_PollCursor](../functions/Input_PollCursor.md) | `0x14001F664` | Reads the mouse: drains the mouse device's relative axes (wheel +24, deltas +28/+32) and stores the client-space cursor position. |
| [Input_TestAction](../functions/Input_TestAction.md) | `0x1400FC598` | The event system's "is this action down" test against the current merged button mask. |
| [Input_TranslateMessage](../functions/Input_TranslateMessage.md) | `0x14001EC2C` | Turns game-window messages into the input object's action queue: keyboard press/release, characters, focus changes and keyboard-layout refresh. |
| [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) | `0x1400EFF18` | Per-frame refresh of one action row: reads the pad button and the two keys bound to the action and writes their value, pressed, released, held and repeat bytes. |
| [Input_WindowSubclassProc](../functions/Input_WindowSubclassProc.md) | `0x14001F4B8` | Window subclass procedure of the game window: turns mouse, keyboard and focus messages into flags and counters on the input object (`input` is the reference data). |
| [Pad_Poll](../functions/Pad_Poll.md) | `0x1400200F8` | Polls pad number pad+608 with XInputGetState and fills one output block: sticks, triggers, buttons. |
| [Pad_ReadSticks](../functions/Pad_ReadSticks.md) | `0x1400201F4` | Turns the two thumb sticks of one XInput state into four signed bytes in -100 .. 100. |
| [PauseManager_Pop](../functions/PauseManager_Pop.md) | `0x1400B4760` | Pops the top pause id and restores the previous pause (or unpauses). |
| [PauseManager_Push](../functions/PauseManager_Push.md) | `0x1400B4618` | Pushes a pause id onto the PauseManager's small stack (max depth 3), applying the previous top's "off" controls and the new top's "on" controls. |
| [PauseManager_Tick](../functions/PauseManager_Tick.md) | `0x1400B467C` | Ticks the pause overlay: when a pause is on the stack, loads its duration from NXD table 282 into the remaining-time float. |

## Structures (2)

| Name | Size (bytes) | Summary |
|---|---|---|
| [InputActionRow](../structs/InputActionRow.md) | 48 | One action of the input module (g_InputModule + 1360 + 48 * action id, 256 rows; ids are UIKeyAssign keys): three 16-byte bindings, the pad button first, then two keys. |
| [InputStateAxes](../structs/InputStateAxes.md) | 1352 | The analog part of the 0x548-byte input state that the UI listeners receive (copied whole by sub_1400EFB50 and by GUICore_OnInputState): four signed stick bytes, two trigger bytes and the button dwords. |

## Globals (1)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_InputModule](../globals/g_InputModule.md) | `0x143CD9EE8` | `void *` | The UI input module: a copy of the device state at +8, 256 action rows of 48 bytes at +1360 (record InputActionRow), the context mask at +13720. |
