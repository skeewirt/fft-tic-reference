# Formula_50_PummelRandomHits

- **Address:** `0x140308780`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_50(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 50

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pummel: an additive PA + averaged-Y base multiplied by a random number of hits.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 159 bytes.
- V: Typical abilities: Pummel.

## Calculation

```text
Y_avg = (ability_Y + PA) / 2
Base = (PA + Y_avg) × [×3/2 Berserk] × [×2/3 target Protect]
 × [×3/2 Sleep] × Zodiac(50-150%) × [critical]
Hits = random(1..X)
Total Damage = Base × Hits
(ADDITIVE base, not multiplicative)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
