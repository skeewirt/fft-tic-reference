# Formula_10_FaithBasedStatus

- **Address:** `0x1403074EC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_10(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 10

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Faith-based status: a magic hit check that applies a status effect and deals no damage.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 32 bytes.
- V: Typical abilities: Poison, Toad, Slow, Stop, Blind, Sleep, Break, Dispel, Silence.

## Calculation

```text
Hit% = (MA + X) × [×5/4 element] × [×4/3 MagicAttackUp] × [×2/3 Shell]
 × [×3/2 Sleep/Charge] × Zodiac(50-150%)
 × Faith(caster×target/10000)
 → inflicts status on success (no damage)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
