# Formula_92_DragonSMightSpeciesGatedAllStatBoost

- **Address:** `0x140309288`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_92(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 92

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dragon's Might: a species-gated Brave/PA/MA/Speed boost.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 77 bytes.
- V: Typical abilities: Dragon's Might.

## Calculation

```text
Species gate: caster+398 must be 15 or 16 (Dragon type)
    If not dragon: auto-miss
On success: Brave += X, PA += Y, MA += Y, Speed += Y
(Structure identical to F59 Shout)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
