# UIAddonFingerCursor_Bind

- **Address:** `0x1401D31E8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_Bind(UIAddonFingerCursor *addon)`
- **Callers:** vtable of UIAddonFingerCursor (slot 4, data)
- **Callees:** GUIWidget_FindFirstKind1Component2, GUINode_FindPartByName, GUINode_FindDescendant

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the parts of the cursor widget once it is loaded and resets the glide (vtable slot 4 of the addon).

## Behavior

- V: comp = GUIWidget_FindFirstKind1Component2(addon+24). addon+56 = GUINode_FindPartByName(comp+272, CursorRef) (the reference node that GUICursorHand_Update moves), addon+48 = GUINode_FindDescendant(comp, CursorRef), addon+64 / +72 = GUINode_FindDescendant(addon+48, ButtonGuide00 / ButtonGuide01).
- I: addon+48 is the Hand component: it is the object whose Default, Grab, Vertical and VerticalLoop states the pose functions play, and only the Hand component carries those states in ffto_common_cursor.uib.
- V: byte +416 of the two button-guide objects = 0; the glide is reset: addon+444 = 0, addon+440 = g_UIDataModule+24, addon+448 = 0, addon+445 = 1.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_FindDescendant](GUINode_FindDescendant.md)
- Reads: [UIAddonFingerCursor.widget](../structs/UIAddonFingerCursor.md#widget)
- Writes: [UIAddonFingerCursor.cursor_ref_node](../structs/UIAddonFingerCursor.md#cursor_ref_node), [UIAddonFingerCursor.hand_component](../structs/UIAddonFingerCursor.md#hand_component), [UIAddonFingerCursor.button_guide_0](../structs/UIAddonFingerCursor.md#button_guide_0), [UIAddonFingerCursor.button_guide_1](../structs/UIAddonFingerCursor.md#button_guide_1), [UIAddonFingerCursor.follow_k](../structs/UIAddonFingerCursor.md#follow_k), [UIAddonFingerCursor.custom_k](../structs/UIAddonFingerCursor.md#custom_k), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement)

## Notes

The name is ours (IDB: sub_1401D31E8).

## Open questions

None recorded.
