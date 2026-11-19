# KeyBindingFlag

- **Kind:** registry
- **Area:** [Input](../areas/input.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The flag bits of a keyboard binding dword of an action row (low 16 bits = key code), set by InputRows_ApplyKeyBindings from the UIKeyAssign flag bytes.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="ctrl"></a>65536 | `ctrl` | `0x10000` | V | The key counts only while Ctrl (key 17) is held (UIKeyAssign key_ctrl / key_2_ctrl). |
| <a id="alt"></a>131072 | `alt` | `0x20000` | V | Only while Alt (key 18) is held (key_alt / key_2_alt). |
| <a id="shift"></a>262144 | `shift` | `0x40000` | V | Only while Shift (key 16) is held (key_shift / key_2_shift). |
| <a id="long_press"></a>524288 | `long_press` | `0x80000` | V | Reported only after 1000 ms down (key_long_press / key_2_long_press). |
| <a id="unknown"></a>1048576 | `unknown` | `0x100000` | ? | Set from UIKeyAssign +0x2D on both keys; no reader of the bit was found. |

## Behavior

- V: the modifier flags gate every key except 16..18 in InputKey_ReadBinding; the long press is tested by Input_UpdateActionRow.

## Notes

A pad binding uses 0x10000 for the long press (pad_long_press) and 0x20000 for a short press; the same bit values mean other things on the two kinds of binding.

## Open questions

? the reader of 0x100000.
