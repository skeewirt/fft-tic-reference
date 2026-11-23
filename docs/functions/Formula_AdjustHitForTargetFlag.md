# Formula_AdjustHitForTargetFlag

- **Address:** `0x140305700`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `__int64 Formula_AdjustHitForTargetFlag(void)`
- **Callers:** Formula_05_WeaponAttackNoElement, sub_140306C90, sub_140306D70
- **Callees:** Unit_GetActionGateState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evade-setup step of the weapon formulas: halves the baseline byte and sets reaction 449 when the target meets two conditions.

## Behavior

- V: it calls `Unit_GetActionGateState` on `g_BattleActingUnit` (the unit hit).
- V: when that returns 0 and the target's byte +0x97 has bit 0x10, it shifts the baseline byte at 0x1407B077F (g_FormulaBlock +0x0F) right by one and writes 449 to the result block's reaction id (+0x10 of `g_BattleActionBlock`).
- V: otherwise it does nothing.

## State touched

- Calls: [Unit_GetActionGateState](Unit_GetActionGateState.md)

## Referenced by

- Called by: [Formula_05_WeaponAttackNoElement](Formula_05_WeaponAttackNoElement.md), [sub_140306C90](sub_140306C90.md), [sub_140306D70](sub_140306D70.md)

## Notes

Operands taken from the disassembly (the decompile lost the unit register).

## Open questions

What reaction 449 is.
