# Item_GetRecord

- **Address:** `0x1402B8C44`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `uint8_t *Item_GetRecord(uint16_t itemId)`
- **Callers:** 79 functions, 111 call sites (Unit_LoadEquipmentAndEvade, EquipDetail_Refresh, PartyUnit_WriteBackToSave, sub_1402779EC, sub_140277F10, ItemSprite_LoadPalettes, sub_1402C60E4, sub_140344B68 ...)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the 12-byte record of an item.

## Behavior

- V: ids below 0x100 return g_ItemRecords + 12 * id (256 records); ids 0x100 and above return a second base (the 5 high records, ids 256..260) + 12 * (id - 256).
- V: no upper bound: an id above 260 returns an address past the high records (no caller check here).
- V: leaf function; touches rax, rcx, rdx only. Callers keep live values in r8..r11 across the call (Unit_LoadEquipmentAndEvade keeps its unit pointer in r11).
- V: the only code that addresses the record tables (census: one operand each).
- I: record layout (data/tables/exe_item.fields.jsonl): +0 icon palette, +1 icon, +2 level, +3 slot bits (0x80 weapon, 0x40 shield, 0x20 head, 0x10 body, 0x08 accessory), +5 equipment category (bit index into the JobTable equip flags, V), +7 attribute record index, +8 price (u16), +10 shop progress.
- V: no range check: an id below 0x100 indexes the first 12-byte table, every other id the second table by 12 times the id, so an id that still carries bit 15 reads a record far past the item block (behavior OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag).

## Referenced by

- Called by: [Action_BuildCurrentAction](Action_BuildCurrentAction.md), [Action_PickTargetEquipment](Action_PickTargetEquipment.md), [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [BattleRange_ApplyShape](BattleRange_ApplyShape.md), [BattleRange_MarkRing](BattleRange_MarkRing.md), [EquipDetail_SetHelpText](EquipDetail_SetHelpText.md), [ItemIcon_Set](ItemIcon_Set.md), [ItemList_GetPossessionIndex](ItemList_GetPossessionIndex.md), [ItemSprite_LoadPalettes](ItemSprite_LoadPalettes.md), [Item_BuildAttributeLines](Item_BuildAttributeLines.md), [Item_CanUnitEquip](Item_CanUnitEquip.md), [Item_CanUnitEquipPreview](Item_CanUnitEquipPreview.md), [Item_GetMenuField](Item_GetMenuField.md), [Item_SellPrice](Item_SellPrice.md), [PartyUnit_ReloadEquipment](PartyUnit_ReloadEquipment.md), [PartyUnit_WriteBackToSave](PartyUnit_WriteBackToSave.md), [ShopEntry_Fill](ShopEntry_Fill.md), [Shop_BuildItemList](Shop_BuildItemList.md), [UnitWork_ApplyStartingEquipment](UnitWork_ApplyStartingEquipment.md), [UnitWork_PickStartingItem](UnitWork_PickStartingItem.md), [Unit_ListThrowableItems](Unit_ListThrowableItems.md), [Unit_LoadEquipmentAndEvade](Unit_LoadEquipmentAndEvade.md), [sub_1400FA7AC](sub_1400FA7AC.md), [sub_140226E44](sub_140226E44.md), [sub_140269554](sub_140269554.md), [sub_140275EF4](sub_140275EF4.md), [sub_1402779EC](sub_1402779EC.md), [sub_140281488](sub_140281488.md), [sub_14028531C](sub_14028531C.md), [sub_1402855F0](sub_1402855F0.md), [sub_140286C8C](sub_140286C8C.md), [sub_1402875A4](sub_1402875A4.md), [sub_140287D9C](sub_140287D9C.md), [sub_14028B354](sub_14028B354.md), [sub_14028B510](sub_14028B510.md), [sub_1402A6710](sub_1402A6710.md), [sub_1402C4D1C](sub_1402C4D1C.md), [sub_1402C60E4](sub_1402C60E4.md), [sub_1402C8010](sub_1402C8010.md), [sub_1402C80D8](sub_1402C80D8.md), [sub_1402C9F78](sub_1402C9F78.md), [sub_1402D58EC](sub_1402D58EC.md), [sub_1402D5CC4](sub_1402D5CC4.md), [sub_1402D6464](sub_1402D6464.md), [sub_1402D6914](sub_1402D6914.md), [sub_1402D6FB8](sub_1402D6FB8.md), [sub_1402D7280](sub_1402D7280.md), [sub_1402DE564](sub_1402DE564.md), [sub_1402E1604](sub_1402E1604.md), [sub_1402EEC2C](sub_1402EEC2C.md), [sub_1402FE1D0](sub_1402FE1D0.md), [sub_1403055F0](sub_1403055F0.md), [sub_140305A48](sub_140305A48.md), [sub_140305C18](sub_140305C18.md), [sub_140306C90](sub_140306C90.md), [sub_140306D70](sub_140306D70.md), [sub_140309474](sub_140309474.md), [sub_14030AFEC](sub_14030AFEC.md), [sub_14030B278](sub_14030B278.md), [sub_14030B4F0](sub_14030B4F0.md), [sub_14030BF04](sub_14030BF04.md), [sub_14030CF38](sub_14030CF38.md), [sub_140315B10](sub_140315B10.md), [sub_140316D24](sub_140316D24.md), [sub_14031FD40](sub_14031FD40.md), [sub_140323D1C](sub_140323D1C.md), [sub_140332CD0](sub_140332CD0.md), [sub_14033B420](sub_14033B420.md), [sub_140344B68](sub_140344B68.md), [sub_140364408](sub_140364408.md), [sub_14036A994](sub_14036A994.md), [sub_14036E5DC](sub_14036E5DC.md), [sub_140393250](sub_140393250.md), [sub_14039651C](sub_14039651C.md), [sub_140396984](sub_140396984.md), [sub_140396D08](sub_140396D08.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md), [OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag](../behaviors/OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag.md)
- Reads tables: [ItemRecords](../tables/ItemRecords.md)

## Notes

- Proposed data names: g_ItemRecords (256 x 12), g_ItemRecordsHigh (5 x 12).

## Open questions

- Bytes +4, +6, +9, +11 have no reader near any call site.
