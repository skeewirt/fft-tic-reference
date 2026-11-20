# GUITextNode_SetTextById

- **Address:** `0x1403F106C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_SetTextById(__int64 node, unsigned int textId, __int64 args)`
- **Callers:** sub_1401086E8, sub_140108788, sub_140108828, sub_140109134, sub_14010BEC8, sub_14011C940 and more
- **Callees:** UIText_Get, GUITextNode_SetTextExpanded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up a localised text id and sets it on the node with argument expansion.

## Behavior

- V: s = UIText_Get(textId); return GUITextNode_SetTextExpanded(node, s, args).
- V: args is passed through unchanged (the expansion argument list object).
- V: callers include sub_1401086E8, sub_140108788, sub_140108828, sub_140109134, sub_14010BEC8, sub_14011C940.

## State touched

- Calls: [UIText_Get](UIText_Get.md), [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md)

## Referenced by

- Called by: [Launcher_FillControls](Launcher_FillControls.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [SaveLoadList_FillItem](SaveLoadList_FillItem.md), [ShopItemList_SetPrice](ShopItemList_SetPrice.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md)

## Notes

Thin wrapper.

## Open questions

? layout of the args object (see GUITextNode_SetTextExpandedTemp: vector of 264-byte entries).
