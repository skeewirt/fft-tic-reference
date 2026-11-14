# Formula_21_Return

- **Address:** `0x1403078FC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_21(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 21

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Return: a magic hit check that resets the target's CT.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 42 bytes.
- V: Typical abilities: Return.

## Calculation

```text
Hit check: (MA + X) × [×4/3 MagicAttackUp] × [×2/3 Shell]
 × [×3/2 Sleep] × Zodiac(50-150%) × Faith(caster×target/10000)
 (no element boost)
On success: apply status effect (CT reset)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

The exact engine effect of writing 127 to the secondary effect byte (CT reset is inferred).
