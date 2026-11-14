# Formula_86_BeamPhysicalHitMADrain

- **Address:** `0x14030902C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_86(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 86

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Beam: a magic hit that reduces the target's MA.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Beam.
- V: The earlier sheet called this physical; the hit chain is magic.

## Calculation

```text
Magic hit check (MA + X chain)
On success: target MA reduced by Y & 0x7F
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
