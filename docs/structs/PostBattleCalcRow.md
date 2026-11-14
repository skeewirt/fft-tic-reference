# PostBattleCalcRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of PostBattleCalc: an entry thunk, its argument, and the callback the thunk jumps to. A row without a hook has a null argument and sub_14030A11C skips it.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="entry"></a>`0x0` | entry | `void (*)()` | V | sub_14001B9D8 (jmp [rdx]) in a hook row, sub_14001B9DC (jmp rcx) in an empty row. |
| <a id="arg"></a>`0x8` | arg | `PostBattleCalc *` | V | The object itself in a hook row, null in an empty row; sub_14030A11C calls entry(arg, &copy of +0x10..+0x1F) only when it is non-zero. |
| <a id="callback"></a>`0x10` | callback | `void (*)()` | V | The hook: the thunk jumps through the pointer to this field; null in an empty row. |
| <a id="reserved"></a>`0x18` | reserved | `uint64` | V | Zero in the template; copied with the callback as the second half of the row (not read by the callbacks read so far). |

## Behavior

- V: formula ids with a post-battle callback, and the callbacks: 6, 16, 48, 71, 77 sub_1401F9C28; 14 sub_1401F9C54; 15, 47 sub_1401F9C88; 23 sub_1401F9CA4; 72 sub_1401F9CC4; 74 sub_1401F9D0C; 75 sub_1401F9D2C (stores in sub_1401F92A8 at 0x1401F9307 .. 0x1401F993B).
- V: sub_1401F9C28 and sub_1401F9C54 test the acting unit's +0x61 bit 0x10 (Undead) first; the callbacks rewrite the HP word of the action block or copy it to the other result record. The other five callbacks were not read in full (each tests the Undead bit and rewrites the result's HP or MP).

## Referenced by

- Observed behaviours: [FormulaPostHooksAreKeyedByFormulaId](../behaviors/FormulaPostHooksAreKeyedByFormulaId.md)
- Read by: [sub_14030A11C](../functions/sub_14030A11C.md)
- Written by: [sub_1401F92A8](../functions/sub_1401F92A8.md)

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

? the callbacks sub_1401F9C88, sub_1401F9CA4, sub_1401F9CC4, sub_1401F9D0C, sub_1401F9D2C in detail.
