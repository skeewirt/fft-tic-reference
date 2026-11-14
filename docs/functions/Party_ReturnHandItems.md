# Party_ReturnHandItems

- **Address:** `0x140288A24`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `__int64 __fastcall Party_ReturnHandItems(__int16 unit)`
- **Callers:** `sub_1402888E8`, `sub_14028916C`
- **Callees:** `Item_IsInCategory`, `Inventory_AddCount`, `sub_140288788`, `sub_140289F4C`, `sub_140285A6C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a party unit's equipment to the inventory and clears its slots, with special handling for the two-handed
and dual-wield cases.

## Behavior

- V: It masks the left-hand word with 0x3FF only inside the category helpers; the word passed to
  `Inventory_AddCount` is the raw party word (0x140288A24 body), and that callee masks internally.
- V: It walks five slots and calls `sub_140288788` on each raw word; a refusal or a "not needed" result clears
  the slot and adds the raw word to the inventory.
- V: Slot 0x36 (the dummy unit) is skipped for the inventory add but still cleared.
- V: It moves a one-handed second hand into the primary slot and clears the second; it also clears the
  two-handed/double-grip fields for the special jobs.
- I: Because `Inventory_AddCount` masks with 0x3FF, a bit-15 word is returned as its id; the flag does not
  corrupt the inventory, but the unit word is cleared as a whole.

## State touched

- Calls: [Item_IsInCategory](Item_IsInCategory.md), [Inventory_AddCount](Inventory_AddCount.md), [sub_140288788](sub_140288788.md), [sub_140285A6C](sub_140285A6C.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [g_PartyUnits](../globals/g_PartyUnits.md), [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Notes

V: passes the raw party word to Item_IsInCategory and Inventory_AddCount; both mask with 0x3FF internally, so a flagged word's id is preserved here.

## Open questions

- ?: whether the dummy unit 0x36 is the only one that drops items instead of returning them.
