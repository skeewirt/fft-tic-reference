# EffectFile_ResetBasePointers

- **Address:** `0x1402741BC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void *EffectFile_ResetBasePointers(void)`
- **Callers:** sub_140348658
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Points every entry of the 512-slot effect base array at the one shared effect buffer.

## Behavior

- V: fills qword_143740220 (512 pointers) with the address unk_1418A2E00 and returns that address.
- V: every effect number therefore resolves to the same buffer; only one effect file is resident at a time.

## Notes

Name is ours. The array has no room past 512 entries: the next object follows at qword_143740220 + 0x1000.

## Open questions

? when sub_140348658 runs (battle set-up is the likely moment).
