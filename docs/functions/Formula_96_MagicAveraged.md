# Formula_96_MagicAveraged

- **Address:** `0x140309310`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_96(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** Formula_MagicAvgDamage
- **Dispatch ID:** 96

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Averaged magic damage: A = MA, B = (MA + Y) / 2, then the magic damage tail (a thunk to Formula_MagicAvgDamage).

## Behavior

- V: the body is a single jump to Formula_MagicAvgDamage, the same core formulas 30, 94 and 95 reach.
- I: no stock ability row uses formula 96.

## Calculation

```text
A = MA, B = (MA + Y) / 2
then Formula_MagicDamageTail
```

## State touched

- Calls: [Formula_MagicAvgDamage](Formula_MagicAvgDamage.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
