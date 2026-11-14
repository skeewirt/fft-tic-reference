# Formula_90_DragonSCharmSpeciesGatedStatus

- **Address:** `0x1403091D8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_90(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 90

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dragon's Charm: a species-gated status with no hit check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 58 bytes.
- V: Typical abilities: Dragon's Charm.

## Calculation

```text
No hit check — always succeeds
Species gate: caster+398 must be 15 or 16 (Dragon type)
    If not dragon: auto-miss
On success: apply status via F56 engine
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
