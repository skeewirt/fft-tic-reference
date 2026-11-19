# Formula_06_WeaponDrainHP

- **Address:** `0x140307388`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_06(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** sub_140306C90, sub_140305A48, Formula_PhysMods, Formula_CritRoll, Formula_DamageAB, Formula_DrainHP
- **Dispatch ID:** 6

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Weapon attack that drains HP: the weapon-type damage, and the caster gains what the target loses (reversed on an Undead target).

## Behavior

- V: sub_140306C90 first; a miss ends the handler.
- V: sub_140305A48, A += the weapon bonus (the low byte of the word at 0x1407B0787, g_FormulaBlock +0x17), Formula_PhysMods, Formula_CritRoll, Formula_DamageAB, then Formula_DrainHP.
- V: no element step and no status roll in this body.
- I: the stock users are one sword and one harp.

## Calculation

```text
Hit: physical evade (sub_140306C90)
A, B from the weapon type, A += weapon bonus
Damage = A x B after Formula_PhysMods and Formula_CritRoll
The caster heals the same amount (Formula_DrainHP)
```

## State touched

- Calls: [sub_140306C90](sub_140306C90.md), [sub_140305A48](sub_140305A48.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_CritRoll](Formula_CritRoll.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_DrainHP](Formula_DrainHP.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
