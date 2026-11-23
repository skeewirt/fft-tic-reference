# BattleTask_TargetForecastPanel

- **Address:** `0x14022A024`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleTask_TargetForecastPanel(void)`
- **Callers:** No direct code callers. `g_BattleScriptTable` record 5 (0x140672350) slot 3, started by `BattleAction_RunScript` as scene task slot 13 with tag 18; record 5 comes from the script-5 start site `sub_1401FFC48`.
- **Callees:** sub_1402F7F4C, SceneTask_WaitFrame, sub_140226E44, Battle_UnitStatusFillAlt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task entry for the battle status panel's target variant B: waits for the acting-unit panel task, refreshes the target's layout, projects the target's HP/MP from the pending result and tail-calls Battle_UnitStatusFillAlt with mode 2.

## Behavior

- V: scene task entry with no direct code caller; `g_BattleScriptTable` record 5 (0x140672350) holds it in slot 3, and `BattleAction_RunScript` starts it as scene task slot 13 with tag 18.
- V: unless the value at 0x140D46B38 is 19, it first waits for scene task slot 12 (the acting-unit task) to finish through `sub_1402F7F4C(12)`, which yields frames while the slot's runnable qword is non-zero.
- V: it then waits two frames.
- V: it temporarily writes the target index (`word_1407DCFAA`) into the acting-index half of `dword_1407DCF98`, calls `sub_140226E44`, saves the words at 0x1407DCFBE and 0x1407DCFE2 from the refreshed layout blocks, restores the acting index and calls `sub_140226E44` again.
- V: the target unit is record `word_1407DCFAA` of `g_PreviewUnitTable` when the index is 0..20; above 20 the code substitutes the small constants 48, 50, 52 and 54 for the four HP/MP addresses.
- V: it adds the target result's deltas from `g_BattleActionBlock`: HP heal when damage-flag bit 0x40 is set (+8), HP damage when bit 0x80 is set (+6), MP heal when bit 0x10 is set (+12) and MP damage when bit 0x20 is set (+10).
- V: the HP and MP sums are clamped to zero and to the target's maxima at +0x32/+0x36.
- V: it writes the projected pair to the second 212-byte panel block's +208/+210 (screen +65884/+65886) and writes no other panel field before the tail call.
- V: it tail-calls `Battle_UnitStatusFillAlt` with the anchor record at 0x1408081F0, mode 2, `tbl_UiStatusNumbersTargetB` and the work area at 0x140783320; the anchor's four words are 0x0157, 0x00AA, 0x0023 and 0x0034.
- V: it has no termination of its own; it ends only when `Battle_UnitStatusFillAlt` terminates the scene task.
- I: waiting on slot 12 sequences the target panel after the acting-unit panel; that order also makes the acting task's compatibility code at 0x14186AFFC available to the mode-2 fill (rests on the two start slots and the acting task's call).
- ?: the two words saved at 0x1407DCFBE and 0x1407DCFE2 have no direct reader recorded in the database; their consumer is not established.
- ?: the above-20 branch substitutes those constants as addresses; whether that branch is reachable is not established.
- ?: what the value 19 at 0x140D46B38 marks (the same value makes the fill's mode-0 variant take its closing path at once).

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [sub_140226E44](sub_140226E44.md), [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md), [g_BattleActionBlock](../globals/g_BattleActionBlock.md)

## Notes

Whole body read (376 bytes). Neither this task nor the acting-unit task reads PA (+0x38) or CT (+0x41); the +0x41 byte reaches the panel through `Battle_UnitStatusFillAlt`'s number field named `wt`, which `sub_140226CA0` fills from +0x41. Named for what it does: it projects the target's HP/MP for the forecast panel.

## Open questions

0x140D46B38 (the state tested against 19), 0x1407DCF98/0x1407DCFAA (the acting/target indices) and 0x1407DCFBE/0x1407DCFE2 (the saved layout words) have no global record. Who consumes the saved words, what state 19 is, and whether the above-20 target branch can run are open.
