# BonusEntitlements_Setup

- **Address:** `0x1400FFE14`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void BonusEntitlements_Setup(void)`
- **Callers:** sub_1400B3770
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByIndex, NxdEntry_GetRow, sub_14002620C, sub_140026BD4, memset, sub_140092BA0, sub_140027FEC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the application's entitlement list from the SystemBonusEntitlement table and collects the bonus content paths of each entitlement.

## Behavior

- V: for every row with a non-empty entitlement code (+8) a 40-byte list node at g_Application +1488 gets the code (bounded copy to node +16) and the row's byte +0x10 at node +34, unless the code is already listed.
- V: the row's dlc_path_group (+0xC) is compared with the group number (+8) of every DLCPathList row (table 335): the table is walked row by row and is not looked up by key. The path strings (+4) of the matching rows are collected and passed to sub_140092BA0.
- V: the platform check later sets node +33 (owned) for the codes it owns.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [sub_14002620C](sub_14002620C.md)
- Writes: [EntitlementListNode.code](../structs/EntitlementListNode.md#code), [EntitlementListNode.unknown_34](../structs/EntitlementListNode.md#unknown_34)

## Referenced by

- Observed behaviours: [BonusEntitlementGroupMatch](../behaviors/BonusEntitlementGroupMatch.md)

## Notes

Name is ours. In the stock data both rows that name a group use group 1, so a lookup by key would give the same row: the code compares groups.

## Open questions

? the reader of list node +34.
