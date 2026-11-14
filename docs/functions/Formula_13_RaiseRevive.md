# Formula_13_RaiseRevive

- **Address:** `0x1403075AC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_13(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 13

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Raise/revive: a magic hit check followed by percentage-of-max-HP healing when the target is dead.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 146 bytes.
- V: Typical abilities: Raise, Arise.

## Calculation

```text
Step 1: Hit = (MA_modified + X_with_zodiac)
 where MA = MA × [×5/4 element] × [×4/3 MagicAttackUp] × Zodiac
 then × Faith(caster×target/10000)
Step 2: if target dead → Heal = (Y × MaxHP + 99) / 100
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
