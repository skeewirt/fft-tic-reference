# Formula_12_MagicalHealing

- **Address:** `0x140307564`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_12(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 12

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magical healing: MA x Y healing with Zodiac and Faith scaling, plus the undead reversal check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 70 bytes.
- V: Typical abilities: Cure, Cura, Curaga, Curaja, Moogle, Faerie.

## Calculation

```text
Heal = MA × Y × [×5/4 element] × [×4/3 MagicAttackUp]
 × Zodiac(50-150%) × Faith(caster×target/10000)
capped at 32767, then Undead reverse check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
