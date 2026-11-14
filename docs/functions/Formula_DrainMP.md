# Formula_DrainMP

- **Address:** `0x1403063B8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_DrainMP(void)`
- **Callers:** Formula_102_WotLPhysical80MPDrain, Formula_15_MPDrainMagical, Formula_47_DuskbladeMPDrain
- **Callees:** sub_14030A11C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MP drain: the amount becomes MP damage on the target and an MP heal on the caster.

## Behavior

- V: R+10 = R+6, R+6 = 0, R+39 = 0x20; then sub_14030A11C(0).
- V: when R+0 is still non-zero: RC+12 = R+10, RC+39 = 0x10, RC+0 = 1.

## State touched

- Calls: [sub_14030A11C](sub_14030A11C.md)
- Writes: [g_BattleCasterResult](../globals/g_BattleCasterResult.md), [ActionResult.mp_damage](../structs/ActionResult.md#mp_damage), [ActionResult.mp_heal](../structs/ActionResult.md#mp_heal)

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

Block B34 (2026-11-12): 77 bytes, read whole.

## Open questions

None recorded.
