# Formula_PhysAttackFull

- **Address:** `0x140306EF0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `bool Formula_PhysAttackFull(void)`
- **Callers:** Formula_01_NormalAttack, sub_140307140
- **Callees:** Formula_ElementAffinity, sub_140305A48, Formula_ElemBoostWeapon, Formula_CritRoll, Formula_DamageAB, Formula_FinalizeAbsorb, Formula_PhysMods

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The whole stock weapon attack as one unit (formulas 1 and 2): weapon stat, bonus, modifiers, critical, damage, affinity.

## Behavior

- V: calls sub_140305A48 (sets A and B from the weapon type), then A += the byte at g_FormulaBlock +0x17 (weapon bonus).
- V: then Formula_ElemBoostWeapon, Formula_PhysMods, Formula_CritRoll, Formula_DamageAB and Formula_ElementAffinity with the weapon element (0x1407B07AE).
- V: when R+0 is 0 it returns true; otherwise it calls Formula_FinalizeAbsorb and returns the result of Formula_StatusChance19.

## State touched

- Calls: [Formula_ElementAffinity](Formula_ElementAffinity.md), [sub_140305A48](sub_140305A48.md), [Formula_ElemBoostWeapon](Formula_ElemBoostWeapon.md), [Formula_CritRoll](Formula_CritRoll.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_FinalizeAbsorb](Formula_FinalizeAbsorb.md), [Formula_PhysMods](Formula_PhysMods.md)

## Notes

90 bytes, read whole. Callers: Formula_01_NormalAttack, sub_140307140 (formula 2). Crosscheck: the weapon bonus (block +0x17) is the byte at 0x1407B0787, a RIP-relative operand.

## Open questions

None recorded.
