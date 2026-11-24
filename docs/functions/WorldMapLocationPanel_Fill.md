# WorldMapLocationPanel_Fill

- **Address:** `0x1401607D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapLocationPanel_Fill(void *panel, const uint8_t *record)`
- **Callers:** not recorded
- **Callees:** sub_140158CB0, UserSituation_IsMet, sub_1400FE9D0, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the world-map location info panel from a location record.

## Behavior

- V: skipped when Town locations_list (+0x24) is 1; sub_140158CB0 fills the name, description and picture into the node set at +1816 (or +1792 when Town has_shop (+0x31) is set).
- V: with has_shop set: 'ShowProfit' / 'HideProfit' by UserSituation_IsMet(3220); 'ProfitDefault' / 'ProfitNone' by any of the record's dwords 0..2 above 0; then three counters through sub_1400FE9D0. Without it: text 1583 or 1584 by record byte +12.
- V: then 'On' / 'Off' on 35 nodes (from +64, bound by WorldMapLocationPanel_Init) from the 35-byte category mask at record +16: the count of 35 is loaded into ebx at 0x140160B4B, the node pointer is rdi and the mask pointer rsi, both stepped at 0x140160BAF; a null node is skipped.

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Called by: [WorldMapBaseList_OnEvent](WorldMapBaseList_OnEvent.md)

## Notes

The record is WorldMapLocationRecord, built by sub_14036E5DC.

## Open questions

None recorded.
