# Formula_99_SpeedTimesWeaponPower

- **Address:** `0x140309380`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_99(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** Formula_ReactionPrecheck, Rng_Percent, sub_140306C90, Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_Zodiac, Formula_DamageAB, Formula_ElementAffinity, Formula_FinalizeAbsorb
- **Dispatch ID:** 99

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Thrown weapon: damage = the caster's Speed x the weapon's WP through the physical modifiers; a target with the catch reaction may catch it on a Brave roll.

## Behavior

- V: Formula_ReactionPrecheck first; when it returns 0, the caster's job byte (+3) is not 93 and the target has bit 0x08 at +0x97, the result's hit percent word (+0x2C) = 100 - target Brave (+0x2B).
- V: when Brave is 100, or (outside a forecast) Rng_Percent(100, Brave) falls under the Brave value, the throw is caught: hit flag 0, result +0x10 (the reaction id) = 450, +0x28 = the item word g_FormulaBlock +0x0A, reason (+2) = 13.
- V: otherwise, when the hit flag stands: sub_140306C90 (physical evade); A = caster +0x40 (Speed in this layout: sub_140305A48 averages +0x3E with it for knives and bows), B = the weapon power byte 0x1407B07AC.
- V: then Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_Zodiac, Formula_DamageAB, Formula_ElementAffinity with the weapon element 0x1407B07AE, and Formula_FinalizeAbsorb when the hit stands.
- I: this is the throw formula: no stock action row names it; the thrown item's data supplies the formula id.

## Calculation

```text
Catch: target has the reaction (+0x97 bit 0x08), caster job is not 93: chance = target Brave
  caught -> hit 0, reason 13, reaction 450, the item id kept in the result
Hit: physical evade (sub_140306C90)
A = caster Speed (+0x40), B = WP
Damage = A x B (caster status, target passive and status, zodiac), element affinity, absorb
```

## State touched

- Calls: [Formula_ReactionPrecheck](Formula_ReactionPrecheck.md), [Rng_Percent](Rng_Percent.md), [sub_140306C90](sub_140306C90.md), [Formula_CasterStatusMods](Formula_CasterStatusMods.md), [Formula_TargetPassivePhys](Formula_TargetPassivePhys.md), [Formula_TargetStatusPhys](Formula_TargetStatusPhys.md), [Formula_Zodiac](Formula_Zodiac.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_ElementAffinity](Formula_ElementAffinity.md), [Formula_FinalizeAbsorb](Formula_FinalizeAbsorb.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

? which job 93 is (its throws are never caught).
