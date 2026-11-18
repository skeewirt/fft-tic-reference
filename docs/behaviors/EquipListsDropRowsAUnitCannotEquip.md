# EquipListsDropRowsAUnitCannotEquip

- **Kind:** observed behaviour
- **Scope:** engine (equip lists)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [g_MenuList](../globals/g_MenuList.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Outfitter Fitting list and the Status screen's equipment list leave out the items the unit cannot equip; they do not show them greyed.

## Behavior

- V (seen live): the weapon list is headed 'Equippable Weapons' and holds only usable rows, for stock ids and for ids above 1,023; no greyed row appeared on any list tried.
- V (code): in mode 1 the producers keep a refused item and mark it; in mode 2 and above Inventory_BuildEquipList and Shop_BuildItemList drop it; the list the Fitting and Status screens show has no row for a refused item either way.
- ?: which of the two mechanisms (a mode that drops at the producers, or the mark read by the screen's row code to hide the row) produces the missing rows on those two screens.

## Notes

The mark exists only on lists built with a unit and mode 1.

## Open questions

None recorded.
