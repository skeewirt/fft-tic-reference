# CMesId_IsErrorBanner

- **Address:** `0x1400FCCFC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int CMesId_IsErrorBanner(const void *descriptor)`
- **Callers:** sub_14023286C, sub_1402E8E54
- **Callees:** BattleMsg_IdFromDescriptor, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether a battle message is shown as the timed red error banner.

## Behavior

- V: for a message descriptor of kind 0 whose text group is 2 (the C_Mes_Id text pool) it takes the C_Mes_Id_Sample row of BattleMsg_IdFromDescriptor and returns the row's error_banner byte (+0x14); otherwise 0.

## State touched

- Calls: [BattleMsg_IdFromDescriptor](BattleMsg_IdFromDescriptor.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [BattleRefusalBanner](../behaviors/BattleRefusalBanner.md)

## Notes

Name is ours. Both callers test the result first and, when it is non-zero, call ErrorBanner_Show and skip the normal message paths.

## Open questions

None recorded.
