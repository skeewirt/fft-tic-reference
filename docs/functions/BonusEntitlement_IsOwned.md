# BonusEntitlement_IsOwned

- **Address:** `0x1401006F4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int BonusEntitlement_IsOwned(int id)`
- **Callers:** sub_1401009E8
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether the bonus entitlement of a SystemBonusEntitlement row is owned.

## Behavior

- V: looks up the row by id, compares its entitlement code (+8) with the application's list and returns the matching node's owned byte (+33).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)
- Reads: [EntitlementListNode.owned](../structs/EntitlementListNode.md#owned)

## Notes

Name is ours.

## Open questions

None recorded.
