# BUi_CommandAddonCtor

- **Address:** `0x140153020`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 sub_140153020(UIAddonFFTOBattleCommand *addon)`
- **Callers:** `BUi_BattleMenuWindowsCtor` (0x1401012A0)
- **Callees:** `sub_1401D1970`, `sub_1402AD5BC`, `sub_14028BB54`, `sub_1402A26F8`, `sub_14028F46C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructs the 5640-byte command-menu addon: vtable, sub-objects and idle field values.

## Behavior

- V: sets vtable `UIAddonFFTOBattleCommand_14070FDD0`, zeroes 4 qwords at +164, 80 qwords at +196, initializes sub-objects at +840 and +1144, 11 records of 176 bytes at +1440, one at +3376, six 104-byte records at +4776, and two at +5400/+5504.
- V: idle values: `+5608 = -1`, `+5612 = -1`, `+5616 = -1`, `+5620 = -1`, `+5624 = -1`, word `+5631 = 0`, `+144 = 0`, `+156 = 0`, word `+5629 = 0`, byte `+5628 = 0`, `+148 = 1`.
- V: the 304-byte `UIGadgetFFTORadioButtonMenu` at `+840` is built by `sub_1402AD5BC`: it sets radio `+16` (entry count, = addon `+856`) to 0, radio `+280` = **addon `+1120`** to -1 (`0x1402AD5F8`), radio `+284` = addon `+1124` to -1 (`0x1402AD5FE`), radio `+288` word = addon `+1128` to 0 (`0x1402AD5E0`) and radio `+290` = addon `+1130` to 0 (`0x1402AD5EB`).
- V: zeroes 0x60 bytes at +48 (the node pointer block).

## Notes

`+5608`, `+5616`, `+5624` and `+5629` are the fields a reader uses; all start at -1/0. `+144` and `+148` are initialised here but their readers were not traced.

## Open questions

? the semantics of +144 and +148.
