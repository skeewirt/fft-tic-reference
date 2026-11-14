# ItemOrder_SyncGroup

- **Address:** `0x140285F80`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `__int64 __fastcall ItemOrder_SyncGroup(int group)`
- **Callers:** Inventory_RebuildOrders (five calls), sub_140334A48, sub_14036B71C
- **Callees:** Item_IsValidId, Item_MenuCategory, Item_CountTotal, sub_140286070, sub_140286160

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Brings the saved order list of one menu group in line with what the party owns: a newly owned id is put at the front, an id that is no longer owned is removed, and every other entry keeps its place. It then does the same for the equipment order and obtain-order lists.

## Behavior

- V: the argument is a group index from 0 to 4 and selects `off_14067F498[group]`, one of the five saved item order lists.
- V: the scan runs over item ids 1 to 260 and keeps an id only when `Item_IsValidId` accepts it and `Item_MenuCategory` puts it in this group.
- V: the list walk tests each word against 0xFF and against 0x105; the upper constant is the form 0xFF+6 built by the lea at `0x140285FB2`, not a literal in the body.
- V: an owned id that is absent is inserted at index zero after the tail is shifted right; an id that is not owned is removed by shifting the rest left.
- V: the list end is the word 0xFF or a word at or above 0x105; there is no capacity check on the insert path.
- V: after the item list it calls `sub_140286070` for the equipment order list (groups below 4) and then tail-jumps `sub_140286160` for the obtain-order list.
- V: the item ids are plain u16 words; no bit 14/15 flag is tested or stored here.
- I: the front insertion is why a newly acquired item appears first in its menu; nothing sorts it afterwards unless the player asks for a sort.
- ?: whether the missing capacity check can be reached with stock data (the saved lists leave at most two spare words).

## State touched

- Calls: [Item_IsValidId](Item_IsValidId.md), [Item_CountTotal](Item_CountTotal.md), [sub_140286070](sub_140286070.md), [sub_140286160](sub_140286160.md), [sub_1402890C0](sub_1402890C0.md), [ItemOrder_Remove](ItemOrder_Remove.md)

## Referenced by

- Called by: [Inventory_RebuildOrders](Inventory_RebuildOrders.md), [sub_140334A48](sub_140334A48.md), [sub_14036B71C](sub_14036B71C.md)
- Observed behaviours: [OrderInsideItemGroup](../behaviors/OrderInsideItemGroup.md)

## Notes

- V: whole body read. The three helpers cover the item, equipment and obtain order lists.
- V: the saved lists are `off_14067F498[0..4]`; the equipment lists are `off_14067FA90[0..3]`; the obtain list is at `word_141874726`.

## Open questions

None recorded.
