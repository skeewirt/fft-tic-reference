# Formula_44_RendMP

- **Address:** `0x140308448`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_44(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 44

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MP damage by force: the physical evade gate, a chance of PA + Y with the physical modifiers, then MP damage of Y percent of the target's max MP.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): checked: no Faith step, as the body shows.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 122 bytes.
- V: Typical abilities: Rend MP.
- V: The earlier sheet described a status; the current code deals MP damage based on MaxMP.

## Calculation

```text
Gate: sub_140306C90 (physical evade)
Chance: A = PA, B = Y; Formula_PhysMods, Formula_ChanceSum, Formula_ChanceRoll
Success: MP damage (R+10) = (Y x target max MP (+0x36) + 99) / 100, kind bits 0x20
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
