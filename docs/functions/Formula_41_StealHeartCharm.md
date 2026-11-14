# Formula_41_StealHeartCharm

- **Address:** `0x140308208`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_41(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 41

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steal Heart/Charm: a magic hit check and a team check, then Charm through F56.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 121 bytes.
- V: Typical abilities: Steal Heart, Charm, Snort.
- V: The earlier sheet described physical modifiers; the current code uses a magic hit and a team check.

## Calculation

```text
Hit = (MA + X) × Zodiac(50-150%) × Faith(caster×target/10000)
Requires caster and target to be on different teams
On success: inflicts Charm via F56
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
