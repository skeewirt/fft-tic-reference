# BattleMsg_Dispatch

- **Address:** `0x1402387C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall BattleMsg_Dispatch(int a1, int a2, signed int a3, __int64 a4, int a5, __int64 a6)`
- **Callers:** 21 direct callers in the battle-message handlers, including sub_1402025E0, sub_140202E0C, sub_140203AB4, sub_14020435C, sub_140204B78, sub_1402059AC, sub_14020A7F0 and sub_140238444
- **Callees:** SceneVar_Read, SceneVar_Write, BattleMsg_SetKind6, BattleMsg_SetKind1, Item_GetRecord, Item_CountOwnedAndEquipped, SceneTask_Start, sub_140238360, sub_1401FA5F0, sub_1401FA648, sub_140272538, sub_140236378

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the battle message record from an event: it switches on the message kind, writes the kind and id of the record entries, starts the message scene task and resets the action-list widget state. Case 15 is the item message; case 7 is the action message.

## Behavior

- V: a1 selects the message kind; a3 is a unit index (above 0x14 the unit pointer is null); a6 points at a message argument block whose word +2 is the item or action id.
- V: case 15 (item): `v7` is the item id; `Item_CountOwnedAndEquipped(v7)` is called raw, and when it is 99 or more the item record is read with `Item_GetRecord(v7 & 0x1FF)` (`0x140238E56`) and the record's price word is used for the message.
- V: the same case writes the id into the descriptor at 0x140783210/+4 and increments `g_InventoryCounts[id]` when the count is below 99, so the message itself grants the item.
- V: case 7 (action): the word at a6+2 masked with 0x1FF (`0x140238CE5`) selects the action id; a value in 60..85 writes entry 0 kind 7 with id + 0xB7C4, any other value writes kind 6 with id = masked word + 0x7000. The same masked word is stored in `dword_142FD3590` at `0x140238BE2` for the cast-prompt path (case 5).
- V: `v56 == 255` (`0x140238F92`) is the "no item" test of the action message; it selects text 20634 instead of 20633.
- V: the 0x1FF mask is a nine-bit action/item-id limit; the argument word is a plain u16 and the function never tests bit 14/15.
- V: the function is large body and has 21 direct callers; the item record's word +8 shifted right by two is the price used in the text.
- I: the item and action ids arrive through the same argument word because the battle message record has one id field per entry.
- ?: the meaning of a2, a4 and a5 for the cases not re-read; the remaining case mapping.
- V: the 9-bit ability for the battle line is cut and stored in dword 0x142FD3590 at 0x140238BE4 (cases 6 and 9) and read back at 0x140238BFD; the line task (0x140233588) is started and the unit index and the ability go into the message object at 0x140783088 (words at +0x2000 and +0x2008).
- V: the line task forms its text id as a value taken from that message object ORed with 0xA800; dword 0x142FD3590 is also written at 0x1402386D4 in sub_140238444 and written and read in sub_140243A60.
- I: because of the 9-bit cut an ability id above 511 never reaches the line task, so no 0xA800-form line text exists for it (the text table was not checked).
- V: id 60..85 (summons) take the text base 0xB7C4 (47044) in case 7 and every other id the base 0x7000, both after the 9-bit cut (confirmed again 2026-11-10).

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [BattleMsg_SetKind6](BattleMsg_SetKind6.md), [BattleMsg_SetKind1](BattleMsg_SetKind1.md), [Item_GetRecord](Item_GetRecord.md), [SceneTask_Start](SceneTask_Start.md)
- Reads: [g_BattleUnitTable](../globals/g_BattleUnitTable.md), [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_MessageDescriptor](../globals/g_MessageDescriptor.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ShowJobLevelUp](Battle_ShowJobLevelUp.md), [Battle_ShowUnitLevelUp](Battle_ShowUnitLevelUp.md), [sub_14020261C](sub_14020261C.md), [sub_14020435C](sub_14020435C.md), [sub_140204B78](sub_140204B78.md), [sub_14020558C](sub_14020558C.md), [sub_140238444](sub_140238444.md)
- Observed behaviours: [TestBattleModeVariable510](../behaviors/TestBattleModeVariable510.md)

## Notes

- V: read for case 15, case 7's mask and the 0xFF sentinel, and the four mask/cmp sites; the other cases are from the earlier battle-message research and were not re-read this pass.

## Open questions

None recorded.
