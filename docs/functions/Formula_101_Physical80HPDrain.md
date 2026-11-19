# Formula_101_Physical80HPDrain

- **Address:** `0x14030D540`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_101(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** sub_140306C90, Formula_PhysMods, Formula_CritRoll, Formula_DamageAB, Formula_DrainHP
- **Dispatch ID:** 101

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

PA x WP physical damage reduced to 80 percent, and the caster gains the damage dealt as HP (reversed on an Undead target).

## Behavior

- V: sub_140306C90 first; a miss ends the handler.
- V: A = caster PA (+0x3E), B = the weapon power byte 0x1407B07AC; Formula_PhysMods, Formula_CritRoll, Formula_DamageAB.
- V: the HP damage word (+6) is then multiplied by 8 and divided by 10, and Formula_DrainHP gives it to the caster.
- I: the MP twin is formula 102; no stock ability row uses formula 101.

## Calculation

```text
Hit: physical evade (sub_140306C90)
A = PA, B = WP
Damage = A x B after Formula_PhysMods and Formula_CritRoll, then x 8 / 10
The caster heals the same amount (Formula_DrainHP)
```

## State touched

- Calls: [sub_140306C90](sub_140306C90.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_CritRoll](Formula_CritRoll.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_DrainHP](Formula_DrainHP.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
