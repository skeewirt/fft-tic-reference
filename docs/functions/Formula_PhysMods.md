# Formula_PhysMods

- **Address:** `0x140306E34`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_PhysMods(void)`
- **Callers:** Formula_102_WotLPhysical80MPDrain, Formula_104_WotLDistanceScaledPhysical, Formula_37_RendEquipment, Formula_43_RendStats, Formula_44_RendMP, Formula_45_HolySword, and 11 more (IDA code references)
- **Callees:** Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The full physical modifier chain on A: attacker passives, then Berserk / Toad, the target's passives and statuses, and the zodiac step.

## Behavior

- V: when the weapon record copy's byte +1 (0x1407B07A9) & 5 == 4 and g_FormulaBlock +0x0C is non-zero: A = 2 * A (I: a two-handed style bonus).
- V: caster +0x99 bit 0x10: A = A * 4 / 3; with the item word (block +0x0A) 0 and caster +0x9A bit 0x20: A = A * 3 / 2; caster +0x9B bit 0x01: A = A * 3 / 2.
- V: then calls Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys and Formula_Zodiac in that order.

## State touched

- Calls: [Formula_CasterStatusMods](Formula_CasterStatusMods.md), [Formula_TargetPassivePhys](Formula_TargetPassivePhys.md), [Formula_TargetStatusPhys](Formula_TargetStatusPhys.md)

## Referenced by

- Called by: [Formula_03_WeaponPowerSquared](Formula_03_WeaponPowerSquared.md), [Formula_05_WeaponAttackNoElement](Formula_05_WeaponAttackNoElement.md), [Formula_06_WeaponDrainHP](Formula_06_WeaponDrainHP.md), [Formula_07_WeaponHeal](Formula_07_WeaponHeal.md), [Formula_101_Physical80HPDrain](Formula_101_Physical80HPDrain.md), [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

Source: block B24. 188 bytes, read whole. It repeats the caster steps of sub_140305C18 inline (that block reads the item category through Item_GetRecord, this one tests the item word).

## Open questions

? what g_FormulaBlock +0x0C and the weapon record flag bits 5 / 4 stand for (I: the two-hand flag).
