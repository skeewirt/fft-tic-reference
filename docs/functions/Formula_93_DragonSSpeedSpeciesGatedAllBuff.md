# Formula_93_DragonSSpeedSpeciesGatedAllBuff

- **Address:** `0x1403092D8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_93(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 93

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dragon's Speed: a species-gated all-buff.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 53 bytes.
- V: Typical abilities: Dragon's Speed.

## Calculation

```text
Species gate: caster+398 must be 15 or 16 (Dragon type)
    If not dragon: auto-miss
On success: applies ALL status buffs (status-modifier byte 2 = 0xFF)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
