# Formula_60_Chant

- **Address:** `0x14030609C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_60(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 60

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chant: the caster pays HP, the target heals twice that amount.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 58 bytes.
- V: Typical abilities: Chant, Energize.
- V: The earlier sheet described an MP heal; the current code is HP-only.

## Calculation

```text
Caster takes HP damage = caster MaxHP / 5
Target heals HP = 2 × (caster MaxHP / 5)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
