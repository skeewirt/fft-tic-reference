# Formula_SceneVarElemMod

- **Address:** `0x140306134`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_SceneVarElemMod(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_09_Gravity, Formula_31_IaidoNether, Formula_49_MonkPhysicalAveraged, Formula_83_MonsterHPDamageMagicChain, Formula_MagicDamageTail, sub_1403071DC
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene-variable element modifier on R+6: damage of some elements is cut or raised by the battle's scene variable 35.

## Behavior

- V: reads SceneVar 35 and the dword 0x140D3A830; nothing happens when bit 0x02 of the dword is set or the variable is below 2.
- V: with bit 0x01 of the dword the variable is raised by 3. A value of 3 or 4: an ability element bit 0x80 cuts R+6 to 3/4, bit 0x40 raises it to 5/4; a value of 5, 6 or 7: element bit 0x20 raises R+6 to 5/4.
- I: the variable reads as weather or time of day; the element bits are the ability record's byte +7.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md)

## Notes

Source: block B28. 147 bytes, read whole. Crosscheck: the element bit 0x80 is a sign test of the byte (bit 7), so no 0x80 immediate appears.

## Open questions

? what SceneVar 35 and the dword 0x140D3A830 mean (their writers were not read).
