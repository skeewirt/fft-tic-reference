# ItemCategories

- **Kind:** registry
- **Area:** [Items and shops](../areas/items.md)
- **Resolved by:** [Item_FindCategoryIndex](../functions/Item_FindCategoryIndex.md), [Item_CategoryFirstId](../functions/Item_CategoryFirstId.md), [Item_IsInCategory](../functions/Item_IsInCategory.md), [sub_1402890C0](../functions/sub_1402890C0.md)
- **Values stored in:** [ItemRecord](../structs/ItemRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item categories: the stock first-id thresholds of Item_FindCategoryIndex, the record kind of each category (which sub-record table it has) and the menu group sub_1402890C0 gives it. Categories c and c + 7 are the low and high id ranges of one family (Item_IsInCategory treats them as one).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="weapons"></a>0 | `weapons` | `ids 0x00..0x79, kind 0` | V | Weapon sub-record (8 B); menu group 0. |
| <a id="weapons_b"></a>1 | `weapons_b` | `ids 0x7A..0x7F, kind 0` | V | Weapon sub-record; menu group 5. |
| <a id="shields"></a>2 | `shields` | `ids 0x80..0x8F, kind 1` | V | Shield sub-record (2 B); menu group 1. |
| <a id="head"></a>3 | `head` | `ids 0x90..0xAB, kind 2` | V | Armor sub-record (2 B); menu group 2 (the slot name is I). |
| <a id="body"></a>4 | `body` | `ids 0xAC..0xCF, kind 2` | V | Armor sub-record; menu group 3 (the slot name is I). |
| <a id="accessories"></a>5 | `accessories` | `ids 0xD0..0xEF, kind 3` | V | Accessory sub-record (2 B); menu group 4 (I). |
| <a id="consumables"></a>6 | `consumables` | `ids 0xF0..0xFD, kind 4` | V | Chemist sub-record (3 B); ids 0xFE and 0xFF have rows but no category. |
| <a id="weapons_high"></a>7 | `weapons_high` | `ids 0x100..0x101, kind 5` | V | Weapon sub-record of the high table. |
| <a id="weapons_b_high"></a>8 | `weapons_b_high` | `no ids, kind 5` | V | Empty in stock. |
| <a id="shields_high"></a>9 | `shields_high` | `no ids, kind 6` | V | Empty in stock; kind 6 has no stock table. |
| <a id="head_high"></a>10 | `head_high` | `id 0x102, kind 7` | V | Armor sub-record of the high table. |
| <a id="body_high"></a>11 | `body_high` | `id 0x103, kind 7` | V | Armor sub-record of the high table. |
| <a id="accessories_high"></a>12 | `accessories_high` | `id 0x104, kind 8` | V | Accessory sub-record of the high table. |
| <a id="unreachable"></a>13 | `unreachable` | `kind 9` | V | Never returned by Item_FindCategoryIndex. |

## Behavior

- V: ids 0xFE, 0xFF and every id above 0x104 have no category in stock (Item_FindCategoryIndex returns -1).
- V: the special ids 262, 288, 293, 301 and 310 are tested by Item_CanUnitEquip and Item_CanUnitEquipPreview (only jobs 161 / 164 may equip them).

## Referenced by

- Indexed by registries: [ItemClassNumbers](ItemClassNumbers.md)

## Open questions

None recorded.
