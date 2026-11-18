# FormulaHandlers

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140682BD0`
- **Rows:** 106 rows of 8 bytes
- **Keyed by:** formula id 1..106 (virtual base 0x140682BC8; the call is base[id])
- **Read by:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Formula_106_ReDispatchChainFormula](../functions/Formula_106_ReDispatchChainFormula.md)
- **Row layout:** [FunctionPointerRow](../structs/FunctionPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Dispatch table of the 106 ability formula handlers. Each handler reads the unit work records directly, so the table is code, not data.

## Behavior

- V: after the call the dispatcher tests id >= 7 and id == 100 (meaning not known).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: what the id >= 7 and id == 100 tests choose
