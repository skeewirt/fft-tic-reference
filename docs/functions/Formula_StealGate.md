# Formula_StealGate

- **Address:** `0x14030647C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_StealGate(void)`
- **Callers:** Formula_37_RendEquipment, Formula_38_StealEquipment, Formula_46_DarkSwordCrush
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The steal and break gate: turns the picked equipment into no effect when it is one of four protected ids or the target is protected.

## Behavior

- V: when R+4 (the picked equipment id) is 257, 258, 259 or 260 it clears R+27 and R+4, then stores R+0 = 0, R+2 = 7, R+44 = 0.
- V: otherwise, when the target's +0x9A bit 0x04 is clear it returns with R untouched; when the bit is set it stores the same no-effect result (R+0 = 0, R+2 = 7, R+44 = 0).
- V: returns 1 in all paths the decompile shows.

## Notes

89 bytes, read whole. Callers: Formula_37_RendEquipment, Formula_38_StealEquipment, Formula_46_DarkSwordCrush.

## Open questions

? what ids 257..260 are (I: items that cannot be stolen); what the target bit +0x9A 0x04 stands for.
