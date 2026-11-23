# GUINode_FindPartByName

- **Address:** `0x1403F0794`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindPartByName(LayerNode *layer, NameKey *key)`
- **Callers:** JobTree_RefreshAddon
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Depth-first search of a layer node's part list (first child at +208, next sibling +32) for the part named `key`; descends into containers (kind +52 == 1).

## Behavior

- V: used as `GUINode_FindPartByName(node+272, key)` to get Text/Image parts ('Title', 'TextLvNum', 'Knob', 'Base'); callers type-check +52 (3 = text, 2 = image).

## State touched

- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Called by: [Battle_InitScene](Battle_InitScene.md), [Battle_MenuShowPage](Battle_MenuShowPage.md), [BgmMode_DrawRow](BgmMode_DrawRow.md), [GUIAddon_OnStateEvent](GUIAddon_OnStateEvent.md), [GUIComponentList_FindSlotNode](GUIComponentList_FindSlotNode.md), [GUIComponentList_GetHScroll](GUIComponentList_GetHScroll.md), [GUIComponentList_GetVScroll](GUIComponentList_GetVScroll.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [GUITextBoard_FindTextNode](GUITextBoard_FindTextNode.md), [GuideEntry_Fill](GuideEntry_Fill.md), [Launcher_DrawStartPage](Launcher_DrawStartPage.md), [MainTab_BindNodes](MainTab_BindNodes.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [ScrollHelper_Bind](ScrollHelper_Bind.md), [ShopItemList_FillRow](ShopItemList_FillRow.md), [ShopItemList_SetPrice](ShopItemList_SetPrice.md), [SortieScreen_BindBoxes](SortieScreen_BindBoxes.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [TabBar_SetTable](TabBar_SetTable.md), [UIAddonFingerCursor_Bind](UIAddonFingerCursor_Bind.md), [UIAnim_PlayStateTracks](UIAnim_PlayStateTracks.md), [UIGadgetFFTOVScrollText_ApplyScroll](UIGadgetFFTOVScrollText_ApplyScroll.md), [WorldMapLocationPanel_Init](WorldMapLocationPanel_Init.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md), [sub_1400F7378](sub_1400F7378.md), [sub_1401560D0](sub_1401560D0.md), [sub_1402A6710](sub_1402A6710.md)

## Open questions

None recorded.
