# StockFormulaHandlersAreBlockSequences

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 106 stock formula handlers are plain functions with no arguments over the frame Battle_ResolveAction sets up; 47 of them are sequences of the game's own building blocks.

## Behavior

- V (code): the 106 stock handlers are plain functions with no arguments over the frame Battle_ResolveAction sets up (caster, target, result block R, formula block); 47 are block sequences only; the blocks are themselves plain functions (no arguments but the element affinity block's element in cl); a gate returns 1 and a failed roll clears R+0 when the action misses.

## Open questions

None recorded.
