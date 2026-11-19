# Formula_41_StealHeartCharm

- **Address:** `0x140308208`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_41(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 41

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Charm: a chance of MA + X (zodiac only, no Faith); on success, when caster and target are on different sides, the ability's status through Formula_56.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation listed a Faith factor; the body calls no faith step.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 121 bytes.
- V: Typical abilities: Steal Heart, Charm, Snort.
- V: The earlier sheet described physical modifiers; the current code uses a magic hit and a team check.

## Calculation

```text
Chance: A = MA, B = X; Formula_Zodiac, Formula_ChanceSum, Formula_ChanceRoll (no Faith)
Side test: target +6 and caster +6 differ in bits 0xE0, else no effect (reason 7)
On success: Formula_56_StatusOnlyApplication
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
