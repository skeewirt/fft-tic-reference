# PostBattleCalc

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 3400 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-formula post-processing object of a battle: a virtual function table pointer and 106 rows of 32 bytes, one per formula id, that sub_14030A11C runs after a formula handler. Twelve rows hold a callback (an Undead rule); the rest hold the do-nothing marker. Allocated and filled in Battle_Init (the pointer is g_PostBattleCalc).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="vftable"></a>`0x0` | vftable | `void **` | V | vftable_ffto::Game::Battle::PostBattleCalc_140713F28 (0x140713F28), stored by Battle_Init right after the 0xD48-byte allocation. |
| <a id="rows"></a>`0x8` | rows | `PostBattleCalcRow[106]` | V | Row n - 1 at 0x08 + 32 * (n - 1) belongs to formula id n; sub_14030A11C reads the row of the clamped formula byte when it is below 107, so formula ids above 106 have none. |

## Behavior

- V: 0xD48 = 8 + 106 x 32; sub_1401F92A8 fills the rows from a stack template of 106 rows with a 0x6A-iteration copy loop (Battle_Init, 0x14020F004).
- V: the object is the argument of every hook row, so a callback receives the object in rcx (the thunk sub_14001B9D8 jumps through [rdx], the row's callback field).

## Referenced by

- Global instances: [g_PostBattleCalc](../globals/g_PostBattleCalc.md)
- Observed behaviours: [FormulaPostHooksAreKeyedByFormulaId](../behaviors/FormulaPostHooksAreKeyedByFormulaId.md)
- Written by: [sub_1401F92A8](../functions/sub_1401F92A8.md)

## Notes

Source: IDA reads of 2026-11-12. The rows' callbacks: see PostBattleCalcRow.

## Open questions

? what the other virtual functions of the table do (the object is used only through its row array here).
