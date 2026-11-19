# Formula_07_WeaponHeal

- **Address:** `0x1403073C4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_07(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** sub_140305A48, Formula_Zodiac, Formula_PhysMods, Formula_DamageAB, Formula_HealSwap
- **Dispatch ID:** 7

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Weapon that heals: the weapon-type amount through the zodiac and physical modifiers, given to the target as HP (damage on an Undead target); no hit roll.

## Behavior

- V: sub_140305A48, Formula_Zodiac, A += the weapon bonus (the low byte of the word at 0x1407B0787, g_FormulaBlock +0x17), Formula_PhysMods, Formula_DamageAB, then Formula_HealSwap.
- V: no evade or hit call in the body.
- I: Formula_PhysMods ends with its own Formula_Zodiac call, so the zodiac factor is applied twice here.
- I: the stock user is one staff.

## Calculation

```text
A, B from the weapon type, A += weapon bonus
Amount = A x B after Formula_Zodiac and Formula_PhysMods
Healed (Formula_HealSwap; Undead takes it as damage)
```

## State touched

- Calls: [sub_140305A48](sub_140305A48.md), [Formula_Zodiac](Formula_Zodiac.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_HealSwap](Formula_HealSwap.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
