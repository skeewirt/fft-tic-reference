# MainTab_BindNodes

- **Address:** `0x1402AC048`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MainTab_BindNodes(MainTabCtl *ctl, GUINode *screenRoot)`
- **Callers:** JobTree_RefreshAddon and sixteen other screen builders
- **Callees:** UIName_Key, GUINode_FindDescendant, GUINode_FindPartByName, GUINode_FindGadgetPart

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the header (MainTab/Tab) nodes of a screen and keeps them in the controller: the tab, the TextMask mask node, the title text node and the other tab title boards.

## Behavior

- V: ctl[2] = descendant 'Tab' of 'MainTab' under the screen root; ctl[3] = the 'MaskNode00' (kind 9) found through 'TextMask' inside the tab; ctl[4] = the 'Title' part (kind 3, a text node) of the mask node's embedded component (the TextBoard01 component: one Title text node 60 x 120, plus a TextBoard02 reference at x 96).
- V: ctl[5..7] = the 'Title' text nodes of the chained boards 'TextBoard02' .. 'TextBoard04' (each board references the next at x 96); ctl[8] = the 'MainTab' node.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind), [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md)

## Notes

JobTree_RefreshAddon calls it with the 'JobTree' node, then MainTab_SelectTab(ctl, 1), then writes text id 3885 into ctl[4] (+248; the byte +316 = 1 marks it dirty). UI-en row 3885 is 'Job Tree'. Live read (2026-10-28): the Title node is kind 3, size (60,120), pivot (30,60), text id +248 = 0xF2D = 3885.

## Open questions

How the kind 9 mask node draws the TextBoard01 text through the TextMask/Rect00 gradient: GUINode_DrawChildren has no draw for kind 9, so the masking happens elsewhere.
