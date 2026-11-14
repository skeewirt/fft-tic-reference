# Formula_105_WotLLevelScaledPhysical

- **Address:** `0x14030D6E0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_105(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 105

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

WotL level-scaled physical: PA comes from MA, and Y scales with max HP and MA.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 64 bytes.

## Calculation

```text
PA = MA stat, Y = PA + 3 × MaxHP / (10 × MA)
then full physical chain: element/modifiers/zodiac/PA×Y
(scales with both stats and HP pool)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
