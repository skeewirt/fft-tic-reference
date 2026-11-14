# Formula_104_WotLDistanceScaledPhysical

- **Address:** `0x14030D620`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_104(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 104

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

WotL distance-scaled physical: weapon damage adjusted by the distance between caster and target.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 190 bytes.

## Calculation

```text
Base damage from CalcWeaponDamage (weapon-type specific)
then distance modifier:
 adjacent (1 tile): Y += 3 (bonus damage)
 near (2 tiles): Y += 1 (small bonus)
 far (3+ tiles): PA /= 2 (halved damage)
then × [phys modifiers] × Zodiac × [element]
capped at 32767 + faith adjust + status
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
