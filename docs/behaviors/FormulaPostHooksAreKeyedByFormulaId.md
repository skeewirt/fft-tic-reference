# FormulaPostHooksAreKeyedByFormulaId

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_14030A11C](../functions/sub_14030A11C.md), [sub_1401F92A8](../functions/sub_1401F92A8.md), [g_PostBattleCalc](../globals/g_PostBattleCalc.md), [PostBattleCalc](../structs/PostBattleCalc.md), [PostBattleCalcRow](../structs/PostBattleCalcRow.md), [FormulaBlock.formula_id](../structs/FormulaBlock.md#formula_id)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

After a formula handler runs, sub_14030A11C looks the formula byte up in a 106-row hook table (PostBattleCalc) and runs the row's callback, if any: twelve formulas have an Undead rule there. The table is indexed by the formula id, so a formula id past 106 has no row.

## Behavior

- V: Battle_Init allocates the object (0xD48 bytes, 106 rows), sub_1401F92A8 fills it, sub_14030A11C reads row (formula - 1) when (formula - 1) < 0x6A (0x14030A2A0) and calls the row's entry when its argument is non-zero.
- V: the formulas that have a callback are 6, 14, 15, 16, 23, 47, 48, 71, 72, 74, 75 and 77; every other row is the empty marker.

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

? the effect of the last five callbacks in full.
