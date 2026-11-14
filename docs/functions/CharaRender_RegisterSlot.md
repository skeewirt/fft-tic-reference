# CharaRender_RegisterSlot

- **Address:** `0x1400ED9F8`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `bool CharaRender_RegisterSlot(CharaRenderMgr *m, SlotRecord *r, GUINode *imageNode)`
- **Callers:** JobTree_SetPanelRecord and about thirteen other screen builders (job change list, unit status, party screens: sub_140114D74, sub_1401151EC, sub_14011545C, sub_140119108, sub_14011C4EC, sub_14011C940, sub_140123170, sub_140125C88, sub_140131E4C, sub_14013BF8C, sub_14013C238, sub_14013FAB0, sub_140142884)
- **Callees:** CharaRender_SetSlotRequest, CharaRender_PlaceSlotImage, sub_1400ED768

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Registers a UI image node as the display for one unit render slot and applies the first sprite request.

## Behavior

- V: runs CharaRender_SetSlotRequest(r); on success resets the 112-byte slot entry at m + 14920 + 112 * id (sub_1400ED768), stores the node, the id (+56), a request flag (+80 = r.flags & 1), and for a non-null node the placement defaults x offset -8 (+84), width 84 (+92), height 128 (+96), then runs CharaRender_PlaceSlotImage.
- V: sub_1400ED768 defaults: slot scale +60 = 1.5, y offset +52 = -28, id +56 = -1.

## State touched

- Calls: [CharaRender_SetSlotRequest](CharaRender_SetSlotRequest.md), [CharaRender_PlaceSlotImage](CharaRender_PlaceSlotImage.md)

## Referenced by

- Called by: [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [JobTree_SetPanelRecord](JobTree_SetPanelRecord.md), [SaveLoadList_FillItem](SaveLoadList_FillItem.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

Slot ids: the tree uses panel index + 80.

## Open questions

None recorded.
