# EquipDetail_BuildCategoryLines

- **Address:** `0x1400F94DC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void EquipDetail_BuildCategoryLines(..., const uint8_t *attrRecord)`
- **Callers:** the equipment detail screens
- **Callees:** StatusLists_BuildOrder, AbilityTable_GetRow, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, UITable_GetRowByKey, sub_1400FA2C4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the text of the equipment detail category lines (UIStatusEffectCategory, nxd 56) for the equipment attribute record in the third argument.

## Behavior

- V: walks the category order list built by StatusLists_BuildOrder, gets each category row and switches on the category key.
- V: key 1 (Permanent): starts from the record's status set at +24 (5 bytes) and removes every status whose UIStatusEffect row +8 (column ui_status_effect_category) is not 1.
- V: key 2 lists the ability names of the record's bytes +44 and +45 (AbilityTable_GetRow).
- V: key 3 (Applies): starts from the 5 bytes at +9..+13 and adds the statuses of the set at +24 whose UIStatusEffect row +8 is 3.
- V: keys 8, 10 and 11 use record bytes +32, +31 and +30; key 9 uses +19..+23; key 13 reads two item ids at +36 and +40 through UITable 0x2D and their UIStatusEffect rows (sorted by row word +0x20).
- V: status names are drawn with sub_1400FA2C4 from the UIStatusEffect name string.

## State touched

- Calls: [StatusLists_BuildOrder](StatusLists_BuildOrder.md), [AbilityTable_GetRow](AbilityTable_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Open questions

? the other category keys' record fields.
