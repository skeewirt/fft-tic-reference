# Formula_03_WeaponPowerSquared

- **Address:** `0x1403071A4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_03(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** Formula_PhysMods, Formula_CritRoll, Formula_DamageAB
- **Dispatch ID:** 3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Weapon power squared: A = WP + weapon bonus, B = WP, through the physical modifiers and the critical roll, with no hit roll of its own.

## Behavior

- V: B (g_FormulaBlock +2) = the weapon power byte 0x1407B07AC; A (+0) = the same byte plus the weapon bonus byte (g_FormulaBlock +0x17, read as the low byte of the word at 0x1407B0787).
- V: then Formula_PhysMods, Formula_CritRoll and Formula_DamageAB; no evade or hit call in the body.
- V: Battle_ResolveAction copies inflict row 0 for formula 3 instead of the weapon's own row (FormulaBlock +0x0D).
- I: the stock users are three guns, so a gun's damage does not depend on the wielder's PA.

## Calculation

```text
A = WP + weapon bonus (g_FormulaBlock +0x17)
B = WP
Damage = A x B after Formula_PhysMods and Formula_CritRoll
(no evade roll in this handler; status from inflict row 0)
```

## State touched

- Calls: [Formula_PhysMods](Formula_PhysMods.md), [Formula_CritRoll](Formula_CritRoll.md), [Formula_DamageAB](Formula_DamageAB.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
