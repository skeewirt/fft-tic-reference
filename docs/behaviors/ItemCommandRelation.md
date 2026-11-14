# ItemCommandRelation

- **Kind:** observed behaviour
- **Scope:** how the Item command and Throw turn an item id into an ability id and back
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [sub_140281488](../functions/sub_140281488.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [Unit_ListItemCommandItems](../functions/Unit_ListItemCommandItems.md), [Unit_ListThrowableItems](../functions/Unit_ListThrowableItems.md), [sub_1402B8E04](../functions/sub_1402B8E04.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [g_AbilityKind1_ItemByAbility](../globals/g_AbilityKind1_ItemByAbility.md), [g_AbilityKind2_ThrowCategory](../globals/g_AbilityKind2_ThrowCategory.md), [ActionEntryWord](../structs/ActionEntryWord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An Item-command use is an item id plus a paired ability id: the table maps abilities 368..381 to items 240..253, while at use the engine computes ability = item + 0x80 and the current-action builder computes item = ability - 0x80. Throw is a second table of equipment categories, and a consumable's effect is a chemist row, not the item record.

## Behavior

- V: the table has 14 rows: ability 368 + i is item 240 + i. The list builder accepts only 368..381 and writes a byte item list terminated by 0xFF.
- V: at use the relation runs as arithmetic in the other direction: the unit action word stores ability = item + 0x80, and the current-action builder subtracts 0x80 to recover the item id before it reads the chemist row.
- V: the builder also reads the table directly through an address derived as its base minus 0x170, with no range check, so a value outside the 14 rows reads what follows the table.
- V: an item enters the Item command only when its record's equipment category byte is 0x22 (34); action resolution independently requires Item_IsInCategory(item, 6). The two gates read different data.
- V: Throw selects a row of the 12-byte category table with the item's equipment category. The item must also be a weapon-slot item with weapon flags bit 1 set, and the list builder only scans ids below 256.
- V: a consumable's effect is its 3-byte chemist row (formula id, amount, inflicted status); the animation and effect number come from the paired ability id, not from the item id.
- V: items 254 and 255 have chemist rows but no row in the 14-row table, so the Item menu cannot offer them; the use path would still build abilities 382 and 383, which are Throw abilities.
- V: the undo path refuses every id of 261 and above, so a consumable above 260 cannot be refunded by the stock code even though the use path can consume it.
- I: because item + 0x80 is stored without a mask but the AI and preview path reads only ten id bits, an item id above 895 loses its high bits on that path; the request and the unit action block keep the full 16-bit id.
- V: a consumable therefore needs three rows at once: an item record with category 0x22, a chemist row, and a paired ability in the table's range with animation and effect rows.

## Notes

V: the gates, the arithmetic and the table readers are named in the sheets of the functions involved.

## Open questions

? which consumer turns the six throwing-weapon item ids 122..127 into a throw ability; the AI branch adds those ids in the 10-bit field, but the later step was not traced.
