# g_PostBattleCalc

- **Kind:** global
- **Address:** `0x143CDA750`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `PostBattleCalc *`
- **Points to / is a:** [PostBattleCalc](../structs/PostBattleCalc.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the PostBattleCalc object of the running battle: 106 per-formula post-processing rows.

## Behavior

- V: Battle_Init allocates 0xD48 bytes when the pointer is null, sets the vftable, stores the pointer (0x14020EFFD) and calls sub_1401F92A8 to fill the rows; sub_14020F328 and sub_1401F9258 also reference it.
- V: the only reader of the rows is sub_14030A11C (0x14030A2B0), which indexes them by the formula byte at g_FormulaBlock +0x18.

## Referenced by

- Observed behaviours: [FormulaPostHooksAreKeyedByFormulaId](../behaviors/FormulaPostHooksAreKeyedByFormulaId.md)
- Read by: [sub_14030A11C](../functions/sub_14030A11C.md)
- Written by: [Battle_Init](../functions/Battle_Init.md)

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

? what sub_14020F328 and sub_1401F9F04 do with the pointer (references only).
