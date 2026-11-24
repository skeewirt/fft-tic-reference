# BattleUnitEditor_Run

- **Address:** `0x14033BE88`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `_QWORD *BattleUnitEditor_Run(void)`
- **Callers:** BattleUnitEditor_SceneTask, BattleUnitEditor_EventTask
- **Callees:** ScenePreview_FindEntry, sub_14033B420, SceneTask_Start, SceneTask_WaitFrame, Input_TestAction, sub_14033B7E8, sub_14021F7BC, sub_14033BD00, sub_140278C1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle unit editor: a field grid over one battle unit whose values are stepped with the direction keys between per-field limits; actions 45 / 46 switch units.

## Behavior

- V: the field layout is tbl_UiUnitEditorWidgetsLang0 (text language 0) or tbl_UiUnitEditorWidgetsDefault: 21 entries of 24 bytes with a static pointer to the value at +0 (widget table data: fields 0..5, 19 and 20 point into the block at 0x1407B45D0, fields 6..18 into the block at 0x141D32E30; the two layouts differ only in field 4's x), four neighbour field numbers at +10..+13 (up, down, right, left), x +14, y +16 and a style word +18.
- V: a unit n (0..20) is editable when ScenePreview_FindEntry(byte +401 of g_PreviewUnitTable record n, &out) stores n in its out-parameter; the flags go to tbl_UiUnitEditorRowFlags (21 bytes).
- V: start order: refresh (sub_14033B420), current unit (dword 0x14380554C) = the first editable unit, refresh, current unit = 0.
- V: the field limits are copied (168 bytes, 21 min / max dword pairs) from tbl_UiUnitEditorRangesB when word 0x141D32E3E is set, else from tbl_UiUnitEditorRangesA, into tbl_UiUnitEditorRangesLive.
- V (table data): RangesA per field: (1,99), (1,99), (1,153), (0,100), (0,100), (0,12), (1,9), (1,9), (1,99), (1,143), (1,143), (144,171), (172,207), (208,239), (1,187), (1,187), (428,453), (454,485), (486,509), (1,999), (1,999). RangesB is the same except fields 14..18, which are all (1,356).
- V: starts three scene tasks: sub_140338A28 in slot 8, sub_14033AE90 in slot 12 and sub_14033A37C in slot 9, each with a 24-byte record at 0x143805538 / 0x143805550 / 0x143805568.
- V: unit view: action 45 (mask 8) steps to the next editable unit (21 wraps to 0), action 46 (mask 4) to the previous one (-1 wraps to 20), each reloading the limits; cancel (27) leaves; confirm (26) opens the field grid.
- V: field grid: Up / Down / Right / Left (actions 33, 34, 36, 35) move to the neighbour field; confirm toggles edit mode; in edit mode Up or Right add 1 and Down or Left subtract 1 (10 at a time while action 46 is held), clamped to the field's live limits, and on fields 9..13 action 30 (mask 16) sets the value to 0. Cancel in edit mode leaves edit mode only; cancel outside it leaves the grid for the unit view.
- V: field 0 is applied through sub_140278C1C(preview unit, 0 or 1) around a refresh (sub_14033BD00) instead of a plain store.
- V: on exit it clears the three scene task slots' records and sets their close qwords.

## State touched

- Calls: [ScenePreview_FindEntry](ScenePreview_FindEntry.md), [sub_14033B420](sub_14033B420.md), [SceneTask_Start](SceneTask_Start.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [Input_TestAction](Input_TestAction.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [BattleUnitEditor_EventTask](BattleUnitEditor_EventTask.md), [BattleUnitEditor_SceneTask](BattleUnitEditor_SceneTask.md)

## Notes

The value pointers are static (the widget tables are data); the refresh functions sub_14033B420 / sub_14033BD00, which move values between those blocks and the unit, were not read.

## Open questions

? which unit field each block word mirrors (the ranges are the only lead: e.g. fields 11..13 and 16..18 span consecutive id ranges); ? what sub_140278C1C does with field 0.
