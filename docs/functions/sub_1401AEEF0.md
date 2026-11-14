# sub_1401AEEF0

- **Address:** `0x1401AEEF0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `?` (an equip detail refresh)`
- **Callers:** none found as a direct call (installed as a UI method)
- **Callees:** 22 sites, including `sub_1400D6FB0` (poach block), `sub_1402890C0`, `EquipDetail_Refresh`, `sub_1402B8B00`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the equip and possession detail panel for one item, including its shop-new flag, and rebuilds the panel's text and icon slots.

## Behavior

- V: it reads the shop "new" flag block at `0x1411A7810`, two bytes per item id, which is the same block the shop and den screens read.
- V: it reads the poach arrays that follow that block (the 97-entry counts, order, sort and new arrays), so the panel can show a poached item's state.
- V: it resolves the item record and its category through the item accessors and fills the detail fields from them.
- V: it has no direct caller: the screen's part table holds its address, which is why a call scan finds only its callees.
- I: the panel shows both the possession count and the "new" badge, which is why it touches the flag block at all.
- ?: the exact set of panel fields it writes; only the flag and record reads were traced.

## State touched

- Calls: [sub_1400D6FB0](sub_1400D6FB0.md), [sub_1402890C0](sub_1402890C0.md), [EquipDetail_Refresh](EquipDetail_Refresh.md)
- Reads: [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md)

## Notes

Read as a UI aggregate: the briefs list it as the equip detail refresh and as a reader of the shop-new flags. The individual widget writes were not decoded.

## Open questions

None recorded.
