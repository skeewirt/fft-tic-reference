# Formula_61_MagicStatusOnly

- **Address:** `0x140308A24`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_61(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 61

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic status-only: a magic hit check that applies a status with no damage.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 32 bytes.
- V: Typical abilities: Blaster, Mind Blast, Doom.
- V: The earlier sheet called this physical; the hit chain is magic.

## Calculation

```text
Magic hit check (MA + X chain)
On success: applies status via F56
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
