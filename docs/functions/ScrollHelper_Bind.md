# ScrollHelper_Bind

- **Address:** `0x1402AADD8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char ScrollHelper_Bind(ScrollBinding *a1, Node **root, int64_t a3, int64_t a4)`
- **Callers:** UIAddonFFTOBraveStoryGlossary_vfunc_4, UIAddonFFTOLauncher_vfunc_4, sub_14011245C, sub_14012D25C and 14 more
- **Callees:** UIName_Key, GUINode_FindDescendant, GUINode_FindPartByName, GUINode_FindGadgetPart, GUIComponent_UpdateNodeTree, UIName_ReleaseKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds a screen's scrolling gadget: finds the child named `VScroll` (a scroll bar node, type 8) and its guide part, records the binding and refits the gadget.

## Behavior

- V: marks the component dirty and updates its node tree, then finds the descendant named `VScroll` via UIName_Key and GUINode_FindDescendant; it is kept only when its node type (+536) is 8.
- V: registers a binding id into the bar's slot list (+584) and looks the `ScrollBarGuide` part up by name.
- V: releases the temporary name key with UIName_ReleaseKey.
- V: 18 callers, mostly UI addon init paths; its partner for wheel/stick input is UIGadgetFFTOVScrollText_HandleScrollInput.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [UIName_ReleaseKey](UIName_ReleaseKey.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind), [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The job-change grid does not use this helper, which is why the wheel needed its own hook.

## Open questions

None recorded.
