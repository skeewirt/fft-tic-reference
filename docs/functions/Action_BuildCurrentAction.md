# Action_BuildCurrentAction

- **Address:** `0x140320504`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Action_BuildCurrentAction(const void *entry)`
- **Callers:** sub_1403167E4, sub_14031FD40 (two sites), sub_14038BC00 (two sites), sub_14038C8F8, sub_14038D1EC, sub_14038D65C
- **Callees:** Item_GetRecord, `sub_1402B8C74` (Item_GetWeaponRecord), `sub_1402B8E04` (Item_GetChemistRecord), AbilityAction_GetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns one packed four-byte action entry into the game's current-action block at `0x1418716A0`: it resolves the
command, fills the action's range and presentation fields from the ability or item data, and for the item and throw
commands resolves the item id and the ability that represents it.

## Behavior

- V: the entry is four bytes: a 16-bit packed word, a command byte and a flags byte; the word's low ten bits are
  the action id and the high six bits are the acting unit slot.
- V: it clears the first sixteen bytes of the current-action block, the dword at +0x10 and the dword at +0x20.
- V: it stores the entry's command byte at block +0, the packed id word at +2, and the entry's flags byte at +0x10.
- V: the command's kind comes from the byte table at `0x14067E010`, indexed by the command id; the function
  dispatches on that kind.
- V: kind 1 is the Item command: the item id is the action id minus `0x80`, the item's chemist row is read, and the
  kind1 byte at `0x140785E18` indexed by the action id minus `0x170` (that is, the item id the command offers) is
  stored in block word 3 at +6. The table supplies the stored item id, not a paired ability.
- V: kind 2 is the Throw command: the action id is an item id, the item record is read, and equip-categories `0x20`
  and `0x21` are mapped to the fixed throw abilities `0x17E` and `0x189`; any other category keeps the cached throw
  ability word at `0x1418724B4`.
- V: for Throw the item id is stored at block +6 and the resolved throw ability at +2, so the two fields disagree
  about what the word means until the ability is resolved.
- V: kind 7 stores the action id minus `0x26` in block word 3 (+6).
- V: kind 9 stores the kind3 word at `0x140788F4C`, indexed by twice the id, into block byte 4, and stores 1 when the id
  is zero.
- V: kind 10 (charge) stores the kind4 byte at `0x140788F54` into block byte 1.
- V: the default path (also reached from kinds 1, 2 and 7) copies the aux-flags dword at `0x140787F84` indexed by twice
  the id into block bytes 13..16.
- V: for ids below `0x170` it copies several bytes of the ability's 20-byte action row into the block, the fields the
  targeting and display code reads.
- V: for ids at or above `0x170` the action row is skipped and the defaults stay in the block; item, throw, jump and
  arithmetic abilities have no action row.
- V: a raw id above 1023 cannot reach the function through the packed word, because only ten bits are ever read.
- I: this builds the AI and preview "current action", not the player's request, because every caller found is an AI
  or command-preview function.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8E04](sub_1402B8E04.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md)
- Writes: [g_CurrentActionBlock](../globals/g_CurrentActionBlock.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [sub_1403167E4](sub_1403167E4.md), [sub_14031FD40](sub_14031FD40.md), [sub_14038BC00](sub_14038BC00.md), [sub_14038C8F8](sub_14038C8F8.md), [sub_14038D1EC](sub_14038D1EC.md), [sub_14038D65C](sub_14038D65C.md)
- Observed behaviours: [BattleItemsAreUsedThroughItemAbilities](../behaviors/BattleItemsAreUsedThroughItemAbilities.md), [ItemCommandRelation](../behaviors/ItemCommandRelation.md)

## Notes

The block layout (byte offsets) is only partly decoded; field roles above are by position.
- V: copies the 4 + 1 status bytes (+1..+5) of the added-effect record selected by r14 into xmmword_1418716A0 +8..+12.

## Open questions

- ?: what the dword at block +0x20 holds; the function only clears it.
