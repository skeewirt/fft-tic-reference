# Formula_EarthFloatAndAffinity

- **Address:** `0x1403061C8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_EarthFloatAndAffinity(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_09_Gravity, Formula_31_IaidoNether, Formula_49_MonkPhysicalAveraged, Formula_83_MonsterHPDamageMagicChain, Formula_MagicDamageTail, sub_1403071DC
- **Callees:** Formula_ZeroResult

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Float nullifies an earth hit, then the element affinity step runs with the ability's element.

## Behavior

- V: the unit read is the target, or, when the target's +0x1B4 has bit 7 set, the preview-table unit of slot (+0x1B4 & 0x1F).
- V: when that unit has +0x63 bit 0x40 (status 17, Float) and the ability element (block +0x2B) has bit 0x08 (earth), it calls Formula_ZeroResult and sets R+2 = 7.
- V: then it calls Formula_ElementAffinity with the ability record's element byte.

## State touched

- Calls: [Formula_ZeroResult](Formula_ZeroResult.md)

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md)

## Notes

89 bytes, read whole. Crosscheck: block +0x2B (record +7, the element) is byte 11 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

? what the +0x1B4 flag means.
