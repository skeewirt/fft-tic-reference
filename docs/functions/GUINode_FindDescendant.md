# GUINode_FindDescendant

- **Address:** `0x1404091AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUINode_FindDescendant(GUINode *root, NameKey *key)`
- **Callers:** JobTree_RefreshAddon, JobTree_SetPanelRecord
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a descendant node by interned name under `root` (searches the node's child components).

## Behavior

- V: used for 'JobTree', each panel node by JobTree_NodeStem, the 'Line*' arrows, the 'TextBoardJobLv*' boards, 'TextBoardJobName', and the job-change list's scroll bar.
- V: looks the name up with `GUINode_FindPartByName(component + 272, name)` (the component's own node tree: depth first, into Layer containers, kind +52 == 1) and returns only for a Reference part: kind 12 (the compare at 0x1404091C4; its target at +208 / +224 / +304) or kind 9 (0x1404091EF; +248 / +264 / +288). What it returns is the referenced component (`GUIWidget_FindComponentCached`), not the part; any other part gives 0. I: a component's own root node is at component +272.
- V (seen live 2026-11-13): the node fields a parent's states animate (position +56 / +60 through GUINode_SetPosition, opacity +108, enabled +144) belong to the Reference part in the parent's tree (`GUINode_FindPartByName(parent + 272, name)`); writing +144 / +56 / +108 into the component this function returned hid nothing.

## State touched

- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [Battle_InitScene](Battle_InitScene.md), [Battle_MenuShowPage](Battle_MenuShowPage.md), [GUIAddon_OnStateEvent](GUIAddon_OnStateEvent.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [GUINode_FindDescendant2](GUINode_FindDescendant2.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [GUINode_StopState](GUINode_StopState.md), [JobTree_RefreshAddon](JobTree_RefreshAddon.md), [MainTab_BindNodes](MainTab_BindNodes.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md), [SaveLoadList_FillItem](SaveLoadList_FillItem.md), [ScrollHelper_Bind](ScrollHelper_Bind.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [UIAddonFingerCursor_Bind](UIAddonFingerCursor_Bind.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md), [sub_1401560D0](sub_1401560D0.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

A missing node returns null and every caller null-checks, so a requirement without an arrow node simply draws no line.

## Open questions

None recorded.
