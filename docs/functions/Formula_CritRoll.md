# Formula_CritRoll

- **Address:** `0x140305EB4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_CritRoll(void)`
- **Callers:** Formula_102_WotLPhysical80MPDrain, Formula_104_WotLDistanceScaledPhysical, Formula_45_HolySword, Formula_46_DarkSwordCrush, Formula_47_DuskbladeMPDrain, Formula_48_ShadowbladeHPDrain, and 7 more (IDA code references)
- **Callees:** Formula_KnockbackCalc, Battle_Rand15

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The 4 percent critical hit: marks R+1, adds a random share of A and runs the knockback calculation.

## Behavior

- V: rand15 * 100 below 0x20000 (4 percent): R+1 = 1, A = A + A * rand15 / 32768 with a second random draw, then calls Formula_KnockbackCalc.
- V: Battle_Rand15 (sub_14030D088) returns 0x4000 (its own constant) while g_BattleSimulating is non-zero, so a preview draws the same number every time and the first test (0x4000 * 100 = 1638400) is not below 0x20000: a preview never shows a critical.

## State touched

- Calls: [Formula_KnockbackCalc](Formula_KnockbackCalc.md), [Battle_Rand15](Battle_Rand15.md)
- Writes: [ActionResult.critical](../structs/ActionResult.md#critical)

## Referenced by

- Called by: [Formula_03_WeaponPowerSquared](Formula_03_WeaponPowerSquared.md), [Formula_05_WeaponAttackNoElement](Formula_05_WeaponAttackNoElement.md), [Formula_06_WeaponDrainHP](Formula_06_WeaponDrainHP.md), [Formula_101_Physical80HPDrain](Formula_101_Physical80HPDrain.md), [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

Source: block B26. 82 bytes, read whole. Crosscheck: 0x4000 is the preview value of Battle_Rand15 (a callee); the division by 32768 is compiled as a shift, so no 0x8000 immediate exists.

## Open questions

None recorded.
