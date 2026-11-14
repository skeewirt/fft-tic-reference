# Formula_88_MalboroSporesMagicHitRecruitment

- **Address:** `0x1403090F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_88(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 88

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Malboro Spores: a magic hit check that validates the target and sets the recruit/charm flag.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 149 bytes.
- V: Typical abilities: Malboro Spores.
- V: The earlier sheet validated the caster; the current code validates the target.

## Calculation

```text
Magic hit check (MA + X chain)
Then validate the target (team, redirect, unit id/type)
On valid: attack-type flags = 2 (recruit/charm)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

The meaning of the target eligibility fields (+5 bit 2, +436, +0, +3) is unresolved.
