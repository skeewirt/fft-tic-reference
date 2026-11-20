# sub_1401F5AFC

- **Address:** `0x1401F5AFC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char sub_1401F5AFC(void)`
- **Callers:** sub_1401F0804, sub_1401F16F4, sub_1401FF6EC, sub_1401FFA98
- **Callees:** sub_1402607E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether the unit the cursor refers to counts as valid: its slot byte +1 is 0xFF or its flag dword +504 has bit 1.

## Behavior

- V: gets a unit record through sub_1402607E4 and returns 1 when its byte +1 is 0xFF or bit 1 (0x2) of its dword +504 is set, else 0.

## Referenced by

- Observed behaviours: [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)

## Notes

Name is ours.

## Open questions

? why the flag counts as valid (role of bit 1 is open).
