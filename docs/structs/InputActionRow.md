# InputActionRow

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One action of the input module (g_InputModule + 1360 + 48 * action id, 256 rows; ids are UIKeyAssign keys): three 16-byte bindings, the pad button first, then two keys. The offsets below are of the pad binding; the key bindings repeat them at +16 and +32.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="binding"></a>`0x0` | binding | `uint32` | V | Low word: pad button id (first binding) or key code (second and third); flag 0x10000 long press, 0x20000 short press; 0 = unbound. |  |  |
| <a id="press_time"></a>`0x4` | press_time | `uint32` | V | UI clock (ms) when the value last rose from 0. | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) |  |
| <a id="value"></a>`0x8` | value | `uint8` | V | Current value, 0 or 100 for a button (a trigger or stick gives 0..100). | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) |  |
| <a id="value_copy"></a>`0x9` | value_copy | `uint8` | V | Second copy of the value; its previous content decides 'released'. |  |  |
| <a id="pressed"></a>`0xA` | pressed | `uint8` | V | 1 on the frame the button went down (Input_IsActionMapped and Input_TestAction's keyboard fallback read it). | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) | [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |
| <a id="released"></a>`0xB` | released | `uint8` | V | 1 on the frame it is no longer held after a non-zero value. | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) |  |
| <a id="held"></a>`0xC` | held | `uint8` | V | 1 while the button is down (Input_IsActionHeld reads it). | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) | [BattleControl_FrameUpdate](../functions/BattleControl_FrameUpdate.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md), [Input_IsActionHeld](../functions/Input_IsActionHeld.md) |
| <a id="held_copy"></a>`0xD` | held_copy | `uint8` | V | Written with the same value as held (pad binding). |  |  |
| <a id="repeat"></a>`0xE` | repeat | `uint8` | V | Auto-repeat pulse (sub_1400F0D98 reads it). | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) |  |

## Behavior

- V: refreshed every frame by Input_UpdateActionRow; a row whose context bit is not in the module's mask (+13720) reads all zero.
- V (data, UIKeyAssign): row 89 = key 17 (Ctrl), alternate key 164 (fifth mouse button), pad button 18 (RB): the fast-forward hold. Row 90 = key 53 (the 5 key), pad button 30 (Y while row 89 is held): fast-forward level 2. Row 91 = key 16 (Shift), pad button 15 (X): the auto-advance toggle. Rows 93 / 94 = key 32, pad 13 (the skip hold), row 95 = key 27, pad 23 (pause).
- I: the only writer found of the context mask stores 0x15 at start-up (sub_1400F159C), so the default context bit 1 is always present.

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? Which of the three UIKeyAssign pad columns is copied for the current button layout (row 89 has a pad id only in the second column).
