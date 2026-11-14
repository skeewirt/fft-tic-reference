# Formula_DamageAB

- **Address:** `0x140305F08`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_DamageAB(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_102_WotLPhysical80MPDrain, Formula_104_WotLDistanceScaledPhysical, Formula_12_MagicalHealing, Formula_31_IaidoNether, Formula_35_DrawOutHeal, and 18 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The damage amount: R+6 = A * B capped at 0x7FFF, kind bit 0x80.

## Behavior

- V: R+6 = min(A * B, 0x7FFF); R+39 = 0x80 (HP damage).
- V: when the stored formula id (g_FormulaBlock +0x18) is 106 the amount is halved (the re-dispatch wrapper's damage).

## State touched

- Writes: [ActionResult.hp_damage](../structs/ActionResult.md#hp_damage), [ActionResult.kind_bits](../structs/ActionResult.md#kind_bits)

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_PhysAttackFull](Formula_PhysAttackFull.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

67 bytes, read whole. The cap is 0x7FFF here and 999 later in sub_14030A11C. Crosscheck: block +0x18 (the formula id) is the byte at 0x1407B0788 (high byte of the word at 0x1407B0787), a RIP-relative operand.

## Open questions

None recorded.
