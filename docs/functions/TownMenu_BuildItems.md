# TownMenu_BuildItems

- **Address:** `0x1403449B0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `unsigned int TownMenu_BuildItems(unsigned int settlement, int *items)`
- **Callers:** sub_1402D0EE0, sub_1402D50E4, sub_140345FE4
- **Callees:** EventVar_Read, UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lists the town menu items of a settlement (Outfitter, Tavern, Warriors' Guild, Poachers' Den).

## Behavior

- V: settlement 22 is special: EventVar_Read(101) + 1 items numbered from 47341.
- V: else, when byte_140693533[4 * settlement] is 1: items 47197, 47198, 47199, and 47200 when event variable 144 is not 0 and the settlement's nxd row (table 0x34) has byte 50 set; returns the count (0 for a place without a town menu).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [WorldMap_ScreenInput](WorldMap_ScreenInput.md)
- Reads tables: [TownMenuKindBySettlement](../tables/TownMenuKindBySettlement.md)

## Notes

Name is ours (was sub_1403449B0). The errand board is a tavern row, not a town menu item (BarTop_Setup).

## Open questions

None recorded.
