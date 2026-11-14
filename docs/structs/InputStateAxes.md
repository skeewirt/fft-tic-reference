# InputStateAxes

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 1352 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The analog part of the 0x548-byte input state that the UI listeners receive (copied whole by sub_1400EFB50 and by GUICore_OnInputState): four signed stick bytes, two trigger bytes and the button dwords.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="left_stick_x"></a>`0x4C8` | left_stick_x | `int8` | V | Seen live 2026-11-10 (virtual pad sticks, each axis both ways). -100 .. 100 after the dead zone (Pad_ReadSticks out[0]). Read as the free pointer's horizontal axis. |
| <a id="left_stick_y"></a>`0x4C9` | left_stick_y | `int8` | V | Seen live 2026-11-10 (virtual pad sticks, each axis both ways). Pad_ReadSticks out[1]; FreeCursor_StepFromSticks uses it negated as the pointer's vertical step. |
| <a id="right_stick_x"></a>`0x4CA` | right_stick_x | `int8` | V | Seen live 2026-11-10 (virtual pad sticks, each axis both ways). Pad_ReadSticks out[2]; ListScroll_HandleStick scrolls a horizontal bar with it. |
| <a id="right_stick_y"></a>`0x4CB` | right_stick_y | `int8` | V | Read by ListScroll_HandleStick and UIGadgetFFTOVScrollText_HandleScrollInput as the vertical scroll axis (the order of the four bytes is Pad_ReadSticks' output order). |
| <a id="left_trigger"></a>`0x4CC` | left_trigger | `uint8` | I | 0 .. 100 (Pad_Poll out[4]); tested with the sticks by sub_1400F0BC8. |
| <a id="right_trigger"></a>`0x4CD` | right_trigger | `uint8` | I | 0 .. 100 (Pad_Poll out[5]). |
| <a id="button_bits_a"></a>`0x4D0` | button_bits_a | `uint32` | V | Button mask read by sub_1400F02BC (id 17 = bit 8 LB, 18 = bit 11 RB, 21 = bit 10, 22 = bit 13 ...; bits per Input_UpdateActionRow). Which dword is held and which is new is not settled. |
| <a id="button_bits_b"></a>`0x4D4` | button_bits_b | `uint32` | V | The second button dword read in the same way. |

## Behavior

- V: seen live 2026-11-10: in the input module object (`qword_143CD9EE8`) this struct starts at +8: the sticks are at module +0x4D0 LX, +0x4D1 LY, +0x4D2 RX, +0x4D3 RY, signed -100 .. 100 after the dead zone, Y positive when pushed up (a full push reads 100 / -99).
- V: a scan of every instruction with a displacement of 1224 .. 1227 (2026-11-10) finds no JobTree_* function: the Job Tree reads only its eight direction bytes (JobTree_HandleInput) and the confirm / cancel actions, so both sticks and both triggers are unused on that screen.
- V: GUICore_OnInputState reads all four stick bytes (raw event 26, 'pad axes') and the free-pointer handler FreeCursor_StepFromSticks reads the left stick; ListScroll_HandleStick reads the right stick.

## Notes

The offsets are those the UI code uses on the input state it is handed; the same layout sits at the start of the input module object (sub_1400EFB50 copies the 0x548 bytes to its start).

## Open questions

? whether the 8 bytes before the copy in the input module object are a vtable pointer (I) or another field.
