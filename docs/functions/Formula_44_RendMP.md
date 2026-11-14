# Formula_44_RendMP

- **Address:** `0x140308448`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_44(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 44

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rend MP: a physical hit check then MP damage based on the target's maximum MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 122 bytes.
- V: Typical abilities: Rend MP.
- V: The earlier sheet described a status; the current code deals MP damage based on MaxMP.

## Calculation

```text
Physical evade check
Hit = (PA + Y) × physical chain × Zodiac(50-150%) × Faith scaling
MP damage = (Y × target MaxMP + 99) / 100
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
