# Formula_01_NormalAttack

- **Address:** `0x140307120`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_01(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 1

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Normal attack damage: weapon-type PA setup, weapon power, the standard physical modifiers and elemental affinity.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 32 bytes.
- V: Typical abilities: Attack, Choco Beak, Tackle, Bite, Claw, all monster basic attacks (16 total).

## Calculation

```text
1. CalcWeaponDamage sets PA based on weapon type (fists/swords/guns etc)
2. PA += WP (weapon power added to PA)
3. Damage = PA × Y × [×2 dual wield] × [×3/2 Berserk] × [×3/2 AttackUp]
 × [×2/3 target Protect] × [×3/2 target Sleep/Charging]
 × Zodiac(50-150%) × [element absorb/weak/half]
capped at 32767, then counter check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
