# Formula_AdjustEvadeForTargetStatus

- **Address:** `0x14030573C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `char Formula_AdjustEvadeForTargetStatus(void)`
- **Callers:** Formula_05_WeaponAttackNoElement, sub_140306C90, sub_140306D70
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evade-setup step: clears the four evade bytes or halves the baseline byte according to status bits of the target.

## Behavior

- V: the unit is `g_BattleActingUnit` (the unit hit). The evade dword at 0x1407B0781 is zeroed when its byte +0x61 has bit 0x01 or 0x08, or its +0x65 has 0x14, or +0x64 has 0x02, or +0x62 has 0x10.
- V: the baseline byte at 0x1407B077F is halved when byte +0x61 has bit 0x02.
- I: by the status numbering, +0x64 bit 0x02 is Stop, +0x65 bit 0x10 Sleep and bit 0x04 Disable (a unit that cannot react gets no evade).

## Notes

Disassembly read for the unit register.

## Open questions

Status names for the other +0x61 and +0x62 bits.
