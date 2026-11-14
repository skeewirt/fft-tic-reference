# Formula_08_BlackMagickSummonDamage

- **Address:** `0x1403073F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_08(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic damage: MA x Y with elemental, Shell, Zodiac and Faith modifiers. Used by black magic and summons.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 126 bytes.
- V: Typical abilities: Fire/Blizzard/Thunder, Holy, Flare, Meteor, Summons, Ultima, Bio.

## Calculation

```text
Damage = MA × Y × [×5/4 element-boost equip]
 × [×4/3 caster magic boost] × [×2/3 target Shell]
 × [×3/2 target Sleep/Charging]
 × Zodiac(50-150%) × Faith(caster×target/10000)
capped at 32767
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
