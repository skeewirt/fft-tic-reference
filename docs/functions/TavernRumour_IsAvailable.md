# TavernRumour_IsAvailable

- **Address:** `0x14036F53C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool TavernRumour_IsAvailable(int id, int town)`
- **Callers:** TavernRumours_BuildList, Tavern_HasNewEntries
- **Callees:** UITable_GetRowByKey, UserSituation_IsMet, EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether rumour `id` may be listed in the tavern of `town`.

## Behavior

- V: false when the Gossip row of the id is missing and the town test below fails; the row is read with UITable_GetRowByKey(181, id).
- V: false when the row's condition (+36, a UserSituation id) is nonzero and UserSituation_IsMet says no.
- V: true when the row's flag (+44, column always_listed) is nonzero: the rumour is then listed in every tavern, without the town mask and without its unlock variable 721 + id; only the +36 condition above still applies.
- V: otherwise, when town >= 0, false unless bit (0x4000 >> town) of g_RumourTownMasks[id] is set; then true only when event variable 721 + id reads nonzero.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [UserSituation_IsMet](UserSituation_IsMet.md), [EventVar_Read](EventVar_Read.md)

## Referenced by

- Called by: [TavernRumours_BuildList](TavernRumours_BuildList.md), [Tavern_HasNewEntries](Tavern_HasNewEntries.md)
- Observed behaviours: [TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable](../behaviors/TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable.md)

## Notes

The town mask table holds 64 entries; the unlock variable of id n is 721 + n (721..784 for ids 0..63).

## Open questions

None recorded.
