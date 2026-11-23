# Formula_05_WeaponAttackNoElement

- **Address:** `0x1403072F8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_05(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** sub_1403055F0, Formula_AdjustHitForTargetFlag, Formula_AdjustEvadeForTargetStatus, sub_140305788, Formula_EvadeRoll, sub_140305A48, Formula_PhysMods, Formula_CritRoll, Formula_DamageAB, Formula_StatusChance19, Formula_StatusTailKeepHit
- **Dispatch ID:** 5

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Weapon attack without the element steps: the physical evade roll, the weapon-type A and B, the modifiers and critical, then the 19 percent status roll.

## Behavior

- V: it prepares the evade bytes the way sub_140306C90 does (sub_1403055F0, the caster +0x99, +0x62 and +0x63 tests, Formula_AdjustHitForTargetFlag, Formula_AdjustEvadeForTargetStatus, sub_140305788) and calls Formula_EvadeRoll, but without sub_140306C90's weather step for categories 11 and 12.
- V: on a hit: sub_140305A48 (A and B from the weapon type), A += the weapon bonus (the low byte of the word at 0x1407B0787, g_FormulaBlock +0x17), Formula_PhysMods, Formula_CritRoll, Formula_DamageAB.
- V: then Formula_StatusChance19; when it returns 0, Formula_StatusTailKeepHit adds the inflict status.
- V: unlike Formula_PhysAttackFull there is no Formula_ElemBoostWeapon, no Formula_ElementAffinity and no Formula_FinalizeAbsorb.
- I: no stock weapon, item or ability row uses formula 5.

## Calculation

```text
Hit: physical evade (hand and accessory bytes, Formula_EvadeRoll)
A, B from the weapon type (sub_140305A48), A += weapon bonus
Damage = A x B after Formula_PhysMods and Formula_CritRoll
19 % roll: the weapon inflict status
```

## State touched

- Calls: [sub_1403055F0](sub_1403055F0.md), [Formula_AdjustHitForTargetFlag](Formula_AdjustHitForTargetFlag.md), [Formula_AdjustEvadeForTargetStatus](Formula_AdjustEvadeForTargetStatus.md), [Formula_EvadeRoll](Formula_EvadeRoll.md), [sub_140305A48](sub_140305A48.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_CritRoll](Formula_CritRoll.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_StatusChance19](Formula_StatusChance19.md), [Formula_StatusTailKeepHit](Formula_StatusTailKeepHit.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
