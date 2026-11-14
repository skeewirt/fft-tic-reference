# Formula_65_CelestialStasis

- **Address:** `0x140308B24`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_65(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 65

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Celestial Stasis: a magic hit check that fails when caster and target share a zodiac sign.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 85 bytes.
- V: Typical abilities: Celestial Stasis.
- V: The earlier sheet called this physical; the hit chain is magic.

## Calculation

```text
Magic hit check (MA + X chain)
If caster and target have different zodiac signs: status via F56
Same sign: miss
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
