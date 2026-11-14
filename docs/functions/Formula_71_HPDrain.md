# Formula_71_HPDrain

- **Address:** `0x140308BEC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_71(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 71

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

% HP drain: percentage-of-max-HP damage that heals the caster, then a status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 67 bytes.
- V: Typical abilities: Blood Drain.
- V: The earlier sheet said the caster recovers MP; the current code recovers HP.

## Calculation

```text
Damage = (Y × target MaxHP + 99) / 100
Caster recovers HP equal to the damage dealt
Then status via F56
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
