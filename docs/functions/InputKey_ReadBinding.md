# InputKey_ReadBinding

- **Address:** `0x1400F06AC`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `int InputKey_ReadBinding(void *inputModule, uint32 binding, ...)`
- **Callers:** Input_UpdateActionRow, sub_1400F12C0
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the state of one keyboard or mouse binding of an action row, honouring its modifier flags.

## Behavior

- V: key codes of 160 and above are mouse buttons (160..164).
- V: key codes 16, 17 and 18 (Shift, Ctrl, Alt) read the key states at input module +640, +644 and +648 directly.
- V: any other key code reads the key state at +576 + 4 * key.
- V: the modifier flags of the binding gate every key except 16..18: bit 18 (0x40000, Shift), bit 16 (0x10000, Ctrl) and bit 17 (0x20000, Alt) are tested as bit numbers (the masks are not in the body) and the key counts only while the matching modifier key's state (+640, +644, +648) has bit 0 set.

## Referenced by

- Appears in flows: [InputBindingBuild](../flows/InputBindingBuild.md)

## Notes

Name is ours. The long-press flag 0x80000 is not handled here: Input_UpdateActionRow tests it after this function returns.

## Open questions

None recorded.
