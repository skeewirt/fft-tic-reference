# Formula_80_PhysicalStatus

- **Address:** `0x140308E50`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_80(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Physical plus status: a physical evade check and magic chain, then a status through F56.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 64 bytes.
- V: Typical abilities: Doom Fist, Venom Fang, Eye Gouge, touch attacks.
- V: The earlier sheet called this magic; the current code has a physical evade check before the magic chain.

## Calculation

```text
Physical evade check, then magic chain
On success: status via F56
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
