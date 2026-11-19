# FormulaIdsWithNoHandlerBody

- **Kind:** observed behaviour
- **Scope:** Formula ids 17, 19, 24, 25 and 70 of the formula registry
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [sub_14030A11C](../functions/sub_14030A11C.md), [ActionResult](../structs/ActionResult.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five formula ids have no formula of their own: their registry rows point at an empty function, so an action with one of them keeps the reset result (a hit with no amount and no status) and only the post-processing runs.

## Behavior

- V: registry rows 17, 19, 24, 25 and 70 (formula ids, entry id - 1 of the table at 0x140682BD0) all hold 0x1400103E0, a three-byte function that returns at once (the compiler's empty indirect-call check).
- V: the result block was reset by Battle_ResultReset before the handler (hit flag 1, hit percent 100, every amount 0), so such an action lands and changes nothing through the formula.
- I: no stock action, weapon or chemist row names one of these five ids.
- V: formulas 30, 94 and 95 share one handler too (0x140307C10); every other id from 1 to 106 has a handler of its own.

## Notes

Read 2026-11-18 from the registry rows and the function at 0x1400103E0.

## Open questions

None recorded.
