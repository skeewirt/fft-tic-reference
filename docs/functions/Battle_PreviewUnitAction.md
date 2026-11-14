# Battle_PreviewUnitAction

- **Address:** `0x140282BDC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_PreviewUnitAction(int unit_slot)`
- **Callers:** sub_140206344
- **Callees:** sub_1402828E4, AbilityAction_GetRecord, sub_140280170, sub_140282754, sub_140278E68, Unit_HasStatusGroup, memcpy, BattleAction_BuildUnitRequest, BattlePreview_BuildAction, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the preview of the action a battle unit currently holds: it resets the per-unit target flags, resolves the action mode and range, and refills the preview block.

## Behavior

- V: the argument is a unit slot; the unit record is the 0x200-byte entry at 0x141853CE0 plus slot times 0x200.
- V: a unit marker of 0xFF at +1 returns at once.
- V: it saves the unit action word at +0x34, calls sub_1402828E4 for the action mode, and restores the word afterwards.
- V: it clears the per-unit words at +0x1CE and the byte at +0x1BB for all 21 slots before rebuilding.
- V: the command kind is taken from unit +0x1A1 and the ability id from +0x1A2; ids below 0x170 go through the ability record path.
- V: sub_140282754 builds the target list, sub_140280170 supplies the item range, and Unit_HasStatusGroup filters targets.
- V: BattleAction_BuildUnitRequest and BattlePreview_BuildAction are called to commit the rebuilt action and its preview.
- V: the tile mask is refreshed through 0x14041FAE0 at the end.
- I: this is the refresh the battle message system runs when the active unit changes, because its only caller is the battle notification function.
- ?: what the saved and restored action word at +0x34 protects; the value is written back unchanged.

## State touched

- Calls: [sub_1402828E4](sub_1402828E4.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [sub_140280170](sub_140280170.md), [Unit_HasStatusGroup](Unit_HasStatusGroup.md), [BattleAction_BuildUnitRequest](BattleAction_BuildUnitRequest.md), [BattlePreview_BuildAction](BattlePreview_BuildAction.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)
- Writes: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Notes

Whole function read (604 bytes). The single caller is the battle notification path, so the sheet keeps the preview reading rather than a menu reading.

## Open questions

None recorded.
