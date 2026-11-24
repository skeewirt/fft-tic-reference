# Input

Pointer polling and input state.

Functions: 24, Structures: 12, Globals: 1, Registries: 3, Flows: 1, Observed behaviours: 1, Tables: 9.

## Functions (24)

| Name | Address | Purpose |
|---|---|---|
| [GUIInput_IsPointerOverLayer](../functions/GUIInput_IsPointerOverLayer.md) | `0x1400FE2D0` | Tells whether the mouse pointer is over a widget and hits a target tagged with the given id. |
| [Input_IsActionHeld](../functions/Input_IsActionHeld.md) | `0x1400F0D4C` | True while any of the three bindings of an action row (one pad button, two keys) is held down. |
| [Input_IsCtrlHeld](../functions/Input_IsCtrlHeld.md) | `0x140021F2C` | Returns true when Ctrl is held **and** Shift is not, no Windows key is down, and a pad state bit is clear. |
| [Input_IsShiftHeld](../functions/Input_IsShiftHeld.md) | `0x140021F9C` | Returns true when Shift is held and Ctrl is not, no Windows key is down, and the ctx pad bit is clear. |
| [Input_ListenerBroadcast](../functions/Input_ListenerBroadcast.md) | `0x1400E3AD8` | Delivers the frame's merged input state to the UI core: merges the input object's state into `state`, calls GUICore_OnInputState, then copies the 0x548-byte state back. |
| [Input_PollCursor](../functions/Input_PollCursor.md) | `0x14001F664` | Reads the mouse: drains the mouse device's relative axes (wheel +24, deltas +28/+32) and stores the client-space cursor position. |
| [Input_RepeatDirection](../functions/Input_RepeatDirection.md) | `0x1402CC9F0` | Menu auto-repeat for six directional actions: returns an action bit on a fresh press and again at the repeat rate while it stays held. |
| [Input_TestAction](../functions/Input_TestAction.md) | `0x1400FC598` | The event system's "is this action down" test against the current merged button mask. |
| [Input_TranslateMessage](../functions/Input_TranslateMessage.md) | `0x14001EC2C` | Turns game-window messages into the input object's action queue: keyboard press/release, characters, focus changes and keyboard-layout refresh. |
| [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) | `0x1400EFF18` | Per-frame refresh of one action row: reads the pad button and the two keys bound to the action and writes their value, pressed, released, held and repeat bytes. |
| [Input_WindowSubclassProc](../functions/Input_WindowSubclassProc.md) | `0x14001F4B8` | Window subclass procedure of the game window: turns mouse, keyboard and focus messages into flags and counters on the input object (`input` is the reference data). |
| [InputGlyph_AppendId](../functions/InputGlyph_AppendId.md) | `0x1400F3998` | Appends one glyph to a text buffer: the glyph escape code followed by the id with the high marker. |
| [InputGlyph_AppendPadButton](../functions/InputGlyph_AppendPadButton.md) | `0x1400F39EC` | Writes the glyph text of an action's button into a text buffer: pad glyphs or keyboard modifier and key glyphs. |
| [InputGlyph_AppendSeparator](../functions/InputGlyph_AppendSeparator.md) | `0x1400F3940` | Appends the separator between two glyphs of a button chord. |
| [InputKey_ReadBinding](../functions/InputKey_ReadBinding.md) | `0x1400F06AC` | Reads the state of one keyboard or mouse binding of an action row, honouring its modifier flags. |
| [InputModule_Init](../functions/InputModule_Init.md) | `0x1400F159C` | Initialises the UI input module, among other fields its context mask. |
| [InputRows_ApplyKeyBindings](../functions/InputRows_ApplyKeyBindings.md) | `0x1400F1B58` | Builds the two keyboard bindings of every action row from the key-assignment table: key code plus modifier and long-press flags. |
| [InputRows_ApplyPadLayout](../functions/InputRows_ApplyPadLayout.md) | `0x1400F1A84` | Copies one of the three pad-button columns of the key-assignment table into the pad binding of every action row. |
| [InputRows_Rebuild](../functions/InputRows_Rebuild.md) | `0x1400F1720` | Rebuilds the input module's action bindings after a change of the pad / keyboard glyph set or the button layout. |
| [Pad_Poll](../functions/Pad_Poll.md) | `0x1400200F8` | Polls pad number pad+608 with XInputGetState and fills one output block: sticks, triggers, buttons. |
| [Pad_ReadSticks](../functions/Pad_ReadSticks.md) | `0x1400201F4` | Turns the two thumb sticks of one XInput state into four signed bytes in -100 .. 100. |
| [PauseManager_Pop](../functions/PauseManager_Pop.md) | `0x1400B4760` | Pops the top pause id and restores the previous pause (or unpauses). |
| [PauseManager_Push](../functions/PauseManager_Push.md) | `0x1400B4618` | Pushes a pause id onto the PauseManager's small stack (max depth 3), applying the previous top's "off" controls and the new top's "on" controls. |
| [PauseManager_Tick](../functions/PauseManager_Tick.md) | `0x1400B467C` | Ticks the pause overlay: when a pause is on the stack, loads its duration from NXD table 282 into the remaining-time float. |

## Structures (12)

| Name | Size (bytes) | Summary |
|---|---|---|
| [InputActionRow](../structs/InputActionRow.md) | 48 | One action of the input module (g_InputModule + 1360 + 48 * action id, 256 rows; ids are UIKeyAssign keys): three 16-byte bindings, the pad button first, then two keys. |
| [InputModule](../structs/InputModule.md) |  | The UI input module (g_InputModule): device state, the 256 action rows and the binding settings. |
| [InputStateAxes](../structs/InputStateAxes.md) | 1352 | The analog part of the 0x548-byte input state that the UI listeners receive (copied whole by sub_1400EFB50 and by GUICore_OnInputState): four signed stick bytes, two trigger bytes and the button dwords. |
| [KeyRepeatPreset](../structs/KeyRepeatPreset.md) | 6 | One row of the KeyRepeatPresets table. |
| [NxdDataUIKeyAssignRow](../structs/NxdDataUIKeyAssignRow.md) | 48 | One row of the nxd.ui_key_assign table (data table). |
| [NxdDataUIKeyboardKeyIconRow](../structs/NxdDataUIKeyboardKeyIconRow.md) | 8 | One row of the nxd.ui_keyboard_key_icon table (data table). |
| [NxdDataUIKeyboardLayoutRow](../structs/NxdDataUIKeyboardLayoutRow.md) | 16 | One row of the nxd.ui_keyboard_layout table (data table). |
| [NxdDataUIKeyboardTypeRow](../structs/NxdDataUIKeyboardTypeRow.md) | 28 | One row of the nxd.ui_keyboard_type table (data table). |
| [NxdDataUIKeyConfigRow](../structs/NxdDataUIKeyConfigRow.md) | 16 | One row of the nxd.ui_key_config table (data table). |
| [NxdDataUIKeyDefineRow](../structs/NxdDataUIKeyDefineRow.md) | 32 | One row of the nxd.ui_key_define table (data table). |
| [NxdDataUIPadDefineRow](../structs/NxdDataUIPadDefineRow.md) | 16 | One row of the nxd.ui_pad_define table (data table). |
| [NxdDataUIPadGuideRow](../structs/NxdDataUIPadGuideRow.md) | 44 | One row of the nxd.ui_pad_guide table (data table). |

## Globals (1)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_InputModule](../globals/g_InputModule.md) | `0x143CD9EE8` | `void *` | The UI input module: a copy of the device state at +8, 256 action rows of 48 bytes at +1360 (record InputActionRow), the context mask at +13720. |

## Registries (3)

| Name | Summary |
|---|---|
| [InputContext](../registries/InputContext.md) | The input contexts an action row can belong to: the row's mask against the module's context mask. |
| [KeyBindingFlag](../registries/KeyBindingFlag.md) | The flag bits of a keyboard binding dword of an action row (low 16 bits = key code), set by InputRows_ApplyKeyBindings from the UIKeyAssign flag bytes. |
| [LocationsListInputActions](../registries/LocationsListInputActions.md) | The input actions (rows of the game's input action table) that the Locations list and the old menu number entries read, with their keyboard keys from the table. |

## Flows (1)

| Name | Summary |
|---|---|
| [InputBindingBuild](../flows/InputBindingBuild.md) | How the UIKeyAssign rows become the live bindings of the input module and how a binding is read each frame. |

## Observed behaviours (1)

| Name | Scope | Summary |
|---|---|---|
| [KeyLongPress](../behaviors/KeyLongPress.md) | engine (input rows) | A long-press binding reports pressed and held only after 1000 ms down: the pad flag 0x10000 and the key flag 0x80000. |

## Tables (9)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [KeyRepeatPresets](../tables/KeyRepeatPresets.md) | Executable |  | 8 rows of 6 bytes | Key-repeat timing presets, one row per value of a 3-bit input option. |
| [NxdDataUIKeyAssign](../tables/NxdDataUIKeyAssign.md) | NXD file | 25 | 256 rows of 48 bytes | Key assignment table (256): main and alternate key codes. |
| [NxdDataUIKeyboardKeyIcon](../tables/NxdDataUIKeyboardKeyIcon.md) | NXD file | 332 | 167 rows of 8 bytes | Keyboard key icon map (167). |
| [NxdDataUIKeyboardLayout](../tables/NxdDataUIKeyboardLayout.md) | NXD file | 328 | 26 rows of 16 bytes | Keyboard layouts (26). |
| [NxdDataUIKeyboardType](../tables/NxdDataUIKeyboardType.md) | NXD file | 327 | 6 rows of 28 bytes | Keyboard types (6). |
| [NxdDataUIKeyConfig](../tables/NxdDataUIKeyConfig.md) | NXD file | 331 | 12 rows of 16 bytes | Key configuration groups (12). |
| [NxdDataUIKeyDefine](../tables/NxdDataUIKeyDefine.md) | NXD file | 35 | 256 rows of 32 bytes | Key definition table (256). |
| [NxdDataUIPadDefine](../tables/NxdDataUIPadDefine.md) | NXD file | 28 | 61 rows of 16 bytes | Pad button definitions (61). |
| [NxdDataUIPadGuide](../tables/NxdDataUIPadGuide.md) | NXD file | 278 | 15 rows of 44 bytes | Pad guide layouts (15). |
