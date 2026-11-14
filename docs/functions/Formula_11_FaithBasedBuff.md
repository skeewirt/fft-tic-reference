# Formula_11_FaithBasedBuff

- **Address:** `0x14030750C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_11(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 11

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Faith-based buff: a magic hit check that applies a beneficial status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 88 bytes.
- V: Typical abilities: Reraise, Regen, Protect, Shell, Haste, Float, Reflect, Carbuncle, Dispelna, Aegis.

## Calculation

```text
Power = (MA_modified + X_with_zodiac)
 where MA_modified = MA × [×5/4 element] × [×4/3 MagicAttackUp] × Zodiac
 then: Power × Faith(caster×target/10000)
 → applies buff status on success
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
