# Formula_67_MissingHPDamage

- **Address:** `0x1403060D8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_67(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 67

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Missing HP damage: uses the caster's missing HP, with no hit check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 31 bytes.
- V: Typical abilities: Vengeance, Blade Burst, Almagest, Karma.
- V: The earlier sheet used the target's missing HP; the current code uses the caster's.

## Calculation

```text
Damage = caster MaxHP - caster current HP
No hit check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
