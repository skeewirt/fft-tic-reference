# EquipSessionFlagFlow

- **Kind:** flow
- **Area:** [Items and shops](../areas/items.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Outfitter/equip session: build candidates, buy or apply a slot word with bit 15, then commit (strip the bit, charge the price, save) or cancel (restore the override).

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1 enter"></a>1 enter | [sub_1402D57C0](../functions/sub_1402D57C0.md) | V | The screen table entry runs sub_1402BE7E8 and then the per-frame dispatcher sub_1402D6F10; sub_1402D5CC4 builds the candidate array for the selected unit. |
| <a id="2 build candidates"></a>2 build candidates | [sub_140287D9C](../functions/sub_140287D9C.md) | V | Shop_BuildItemList is called with mode 2 (only equippable items), the five category lists are merged into the 152-word stack list, and each of the first four output words is OR-ed with 0x8000 when it differs from the unit word and the override word. |
| <a id="3 buy"></a>3 buy | [sub_1402D7280](../functions/sub_1402D7280.md) | V | A candidate with bit 14 is refused (0x1402D72A0); otherwise the current slot is removed, the new price is added to dword_143D1AC68 and the unit word is written as id \| 0x8000. |
| <a id="4 apply list"></a>4 apply list | [sub_1402D5CC4](../functions/sub_1402D5CC4.md) | V | The leave path writes the candidate (which may carry bit 15) to the unit word, adjusts dword_143D1AC68 for every changed slot, calls PartyUnit_ReloadEquipment and closes the screen state. |
| <a id="5 commit"></a>5 commit | [sub_1402D65D4](../functions/sub_1402D65D4.md) | V | The commit message (0x3D) runs sub_1402D65D4 over every party unit: a word at or above 0x4000 is masked with 0x3FF, its override is returned to the inventory and cleared; then sub_140285A6C writes every unit to the save. |
| <a id="6 cancel"></a>6 cancel | [sub_1402D5B6C](../functions/sub_1402D5B6C.md) | V | The cancel messages (0 and 6) run sub_1402D5B6C: a word at or above 0x4000, or a non-zero override, is replaced by the override; every override word is cleared. |
| <a id="7 panel copy"></a>7 panel copy | [PartyUnit_ReloadEquipment](../functions/PartyUnit_ReloadEquipment.md) | V | Every slot change and every commit rebuilds the 64-byte panel block at 0x141876E90 from the unit and save records; the hand words reach the block raw. |

## Behavior

- V: bit 15 is the session flag, not the item-present flag: a committed item is stored without it and 0 is the empty slot.
- V: bit 14 is produced on list entries by Shop_BuildItemList and Inventory_BuildEquipList, is refused by sub_1402D7280, and is not produced on any candidate or party hand word by a stock writer.
- V: the commit order is strip (sub_1402D65D4), save (sub_140285A6C), then screen refresh (JobScreen_RefreshAfterChange); the cancel order restores and does not save.

## Open questions

? whether any teardown path reaches the save or a battle without passing the commit or cancel message.
