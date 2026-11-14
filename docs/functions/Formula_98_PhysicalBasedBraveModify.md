# Formula_98_PhysicalBasedBraveModify

- **Address:** `0x14030934C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_98(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 98

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Brave modify using the single-faith magic chain.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Dread Gaze.

## Calculation

```text
Hit check: physical hit check (evade-based)
On success: target's Brave adjusted by Y & 0x7F
(uses PHYSICAL hit check, evade-dependent)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
