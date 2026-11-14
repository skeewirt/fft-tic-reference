# Formula_18_Quick

- **Address:** `0x1403077F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_18(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 18

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Quick: a magic hit check that sets the extra-turn effect.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 86 bytes.
- V: Typical abilities: Quick.

## Calculation

```text
Power = (MA + X) × [×4/3 MagicAttackUp]
 × Zodiac(50-150%) × Faith(caster×target/10000)
 (no element boost, no Shell, no Sleep)
On success: target gains an extra turn immediately
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
