# Formula_103_WotLHolySwordAlias

- **Address:** `0x14030D618`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_103(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 103

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

WotL Holy Sword: alias of F45; shares its target and calculation.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 5 bytes.
- V: Alias of F45; the symbol map confirms a shared target.

## Calculation

```text
Identical to F45 (Holy Sword)
Damage = PA × (WP + Y) × [phys modifiers] × Zodiac × [element]
Shares the F45 target.
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
