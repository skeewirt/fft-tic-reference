# Formula_106_ReDispatchChainFormula

- **Address:** `0x14030D720`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_106(void)`
- **Callers:** Battle_ResolveAction (through the formula registry, id 106; the dispatch is at 0x140309F53, a caller address)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 106

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Re-dispatch: calls the formula table with a different ID, then applies the post-dispatch step. Also the generic dispatcher.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 31 bytes.
- V: The same function is the generic dispatcher; it calls the table entry then the post-dispatch step.
- V (read 2026-11-12): the body loads the byte at 0x1407B07AA, calls the registry entry at that byte minus one (the registry base is 0x140682BD0) and then tail-jumps to sub_1403067D0: the second dispatch index is the WEAPON record's formula byte (the copy of weapon record +2 at g_FormulaBlock +0x3A, a block offset the body never uses, it addresses the byte directly; the copy is written by the 8-byte Mem_CopyChecked calls of Battle_ResolveAction at 0x140309BC5 / 0x140309D39, caller addresses), zero-extended and not clamped, and the tail call is the common tail of the six basic formulas.
- V: the weapon's formula 0 reads the registry's non-pointer slot (0x140682BC8, the base minus 8, reached with index 0 and never an operand) and a weapon formula above the registry's size reads past the table (a crash class); the registry's own entry 106 holds this function's address (0x14030D720), so a weapon whose formula is 106 would re-enter it with the same byte.
- V: the registry lea at 0x14030D72B and the chain's index are the only code references to the registry besides the resolver's dispatch (0x140309F53).

## Calculation

```text
Not a damage formula — re-calls the dispatch table with a different
formula ID, allowing one ability to chain into another formula.
Then applies post-dispatch modifiers.
```

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Observed behaviours: [FormulaIdsPastTheByte](../behaviors/FormulaIdsPastTheByte.md)

## Notes

Its load of the formula registry address (off_140682BD0, at 0x14030D72B) is the second reference to the formula registry (J8 counted only the dispatcher's). The re-dispatch index (byte_1407B07AA - 1) is not clamped, unlike the dispatcher's (0x140309DAC).

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
