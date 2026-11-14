# UnitWork_BuildForSlot

- **Address:** `0x140284F6C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void UnitWork_BuildForSlot(int slot, int kind)`
- **Callers:** sub_1400DCDBC, sub_1400DCF18, sub_1400DCFE4, sub_1401004B4, sub_14021A030, sub_140246014, sub_1402B803C, Inventory_RebuildOrders, sub_1402BC720, sub_1402C314C, sub_1402CEEE8, sub_1402EEE30, sub_1402FB4F8, sub_1403264A0, sub_140326EF8, sub_140332DB0, sub_1403666CC, sub_14036AC74, sub_14036B71C
- **Callees:** EventVar_Read, memset, UnitWork_BuildFromSaveIndex, memmove, PartyUnit_FillFromWork, Job_IsHiddenFromTree, Item_CanUnitEquip, sub_140360780, sub_140285C30, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a unit work record for a party slot from the save record, then applies the job row and the equipment so the caller can read derived stats without touching the live unit.

## Behavior

- V: the first argument is a 16-bit slot and the second a kind; kinds 0x65 and 0x68 take a special path.
- V: it copies a 0x200-byte record into a stack buffer, clearing it when the slot is outside the party, and fills it from the unit save table at 0x1411A7D10 with a stride of 0x258 (the base is image base + 0x11A7D10, the stride an imul).
- V: PartyUnit_FillFromWork copies the party-side fields into the work buffer, and sub_140285C30 applies the job row to it.
- V: Item_CanUnitEquip is consulted for the equipment words, and Job_IsHiddenFromTree for the job visibility.
- V: the result is a complete work record: the job row stats, the equipment hands and the derived attack/evade values.
- V: the routine is called from the save, shop, job screen, errand and battle paths, so it is the shared way to materialise a unit.
- V: it returns no value; the caller supplies the buffer through the stack and reads it back.
- I: the special kinds 0x65 and 0x68 are the Mime and one other job whose row cannot be applied normally, because the kind is compared with the job ids before the copy.
- ?: whether the routine writes a live unit record or only the caller buffer; the body keeps the work record on the stack.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [PartyUnit_FillFromWork](PartyUnit_FillFromWork.md), [Job_IsHiddenFromTree](Job_IsHiddenFromTree.md), [Item_CanUnitEquip](Item_CanUnitEquip.md)
- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md), [g_PartyUnits](../globals/g_PartyUnits.md), [g_JobTable](../globals/g_JobTable.md)

## Referenced by

- Called by: [Inventory_RebuildOrders](Inventory_RebuildOrders.md), [sub_140246014](sub_140246014.md), [sub_1402CEEE8](sub_1402CEEE8.md)

## Notes

Whole function read (941 bytes). The callers and the save-table stride are the ones the party/unit studies list.

## Open questions

None recorded.
