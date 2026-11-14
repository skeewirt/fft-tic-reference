# Formula_35_DrawOutHeal

- **Address:** `0x140307DFC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_35(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 35

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw Out heal: MA x Y healing with the undead reversal check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 55 bytes.
- V: Typical abilities: Murasame.

## Calculation

```text
Heal = MA × Y × Zodiac(50-150%)
capped at 32767, then Undead reverse check
(no faith scaling, no element boost)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
