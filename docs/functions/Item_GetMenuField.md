# Item_GetMenuField

- **Address:** `0x140285A98`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `uint8_t Item_GetMenuField(uint16_t item_id)`
- **Callers:** sub_1402875A4, sub_14028B354
- **Callees:** sub_1402890C0, sub_1402B8C74, sub_1402B8CD4, sub_1402B8D3C, Item_GetRecord, Item_IsInCategory

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the one-byte sub-record field an item list shows for an item: the weapon power, the shield or armour byte, or the accessory field, chosen by the item menu category.

## Behavior

- V: the menu category comes from sub_1402890C0; a category of 0 with a non-zero id uses the weapon record byte +4.
- V: category 1 uses the shield record byte +0 and categories 2 and 3 use the armour record byte +0.
- V: every other category reads the item record byte +2.
- V: when the category is 5 and Item_IsInCategory(id, 4) is false, 0x22 is added to the result.
- V: the value is returned zero-extended in eax; no record or item bound is applied beyond the category lookup.
- V: the two callers are the auto-equip picker and the item-list field selector, so the same byte serves both the list and the comparison.
- I: the +0x22 offset in the accessory case shifts the byte into the range the accessory list expects, because the raw record byte is a small index.
- ?: whether a category 5 item in category 4 should also get the offset; the condition is only the category membership test.

## State touched

- Calls: [sub_1402890C0](sub_1402890C0.md), [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8CD4](sub_1402B8CD4.md), [sub_1402B8D3C](sub_1402B8D3C.md), [Item_GetRecord](Item_GetRecord.md), [Item_IsInCategory](Item_IsInCategory.md)

## Referenced by

- Called by: [sub_1402875A4](sub_1402875A4.md)

## Notes

Whole function read (117 bytes). This is the field-2 accessor of the item order data.

## Open questions

None recorded.
