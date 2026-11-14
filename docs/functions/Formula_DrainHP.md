# Formula_DrainHP

- **Address:** `0x1403062F0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_DrainHP(void)`
- **Callers:** Formula_16_HPDrainMagical, Formula_48_ShadowbladeHPDrain, Formula_71_HPDrain, Formula_77_PhysicalHPDrain, sub_140307388, sub_14030D540
- **Callees:** sub_14030A11C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

HP drain: the target takes the amount and the caster gets it, or the reverse when the target is Undead.

## Behavior

- V: both paths first call sub_14030A11C(0) (clamps and difficulty scale, no hook) and continue only when R+0 is non-zero.
- V: target not Undead: RC+8 = R+6, RC+39 = 0x40, RC+0 = 1 (the caster heals); R+39 = 0x80 (the target takes the damage in R+6).
- V: target Undead (+0x61 bit 0x10): RC+6 = R+6, RC+39 = 0x80, RC+0 = 1 (the caster takes it); R+8 = R+6, R+6 = 0, R+39 = 0x40 (the target is healed).

## State touched

- Calls: [sub_14030A11C](sub_14030A11C.md)
- Writes: [g_BattleCasterResult](../globals/g_BattleCasterResult.md), [ActionResult.hp_heal](../structs/ActionResult.md#hp_heal)

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

Source: block B33. 135 bytes, read whole. This is the two-sided result: the caster side is RC.

## Open questions

None recorded.
