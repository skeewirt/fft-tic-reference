# GUICursorHand_Update

- **Address:** `0x1401D2B00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUICursorHand_Update(GUICursorHand *hand)`
- **Callers:** GUICursorHand vtable (thunk 0x1401D2ADC)
- **Callees:** GUIWidget_GetNodeScreenRect, GUINode_SetPosition, sub_1403D6E28 (focus node)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the pointing-hand cursor: finds the focused component, computes where the hand belongs and moves it there.

## Behavior

- V: first counts down the hold timer hand+76 (ms, dt from core+2100) and does nothing while it is > 0.
- V: target = the focused node's 'CursorAnchor' part rect if the component has one (x = rect.left + hand+80 - handWidth/2, y = (rect.top+rect.bottom)/2 + hand+84), otherwise, for a type-12 focus node with +144 set, x = rect.left + hand+80, y = rect centre + hand+84 (rect from GUIWidget_GetNodeScreenRect).
- V: with a target the hand node (hand+56) is moved by GUICursorHand_StepToward's rule; without one the hand node is hidden and the next placement is instant (+444 = 0, +440 = default k, +445 = 1).
- V: the placement happens only when the focused component's byte +568 is set and the target differs from the last placed position (+432 / +436); the step is computed from that last position every frame, so a stalled hand recomputes the same value.
- V: while hand+132 (static mode, UIAgentCursor_SetStatic) is set the node is only made visible and is not placed. The agent's update thunk calls this function only when the cursor widget is active.
- V: hand+80 / +84 are loaded from the cursor request being applied (UIAgentCursor_PopRequest) and cleared when the cursor is hidden.
- V: this function neither starts nor stops any animation state: the glove's bob (flow CursorGloveFrame) is independent of arriving, leaving or retargeting.
- V (live read, 2026-10-28): the hand object a1 = 0x15DA3015000 in that session had hand+80 = hand+84 = 0; *(a1+64) is the cursor widget's reference node holder: +56 = the node (kind 12, size 100x100, pos = the last placement), +432 / +436 = the last placed (x, y), +440 = k (0.4), +444 / +445 = the flags. The job tree's focus node is the panel reference node (kind 12, pos = panel origin, size 64x80); its screen rect from GUIWidget_GetNodeScreenRect is (left, top + 32, left + 64, top + 112) (the 32 is the JobTree layer's y), so the target for Mystic (1220, 485) is (1220, 557). The rounded smoothing step stops 1 px short of the target when the remaining distance is 1 (|d| * 0.4 < 0.5): live pos (1219, 556).

## State touched

- Calls: [GUIWidget_GetNodeScreenRect](GUIWidget_GetNodeScreenRect.md), [GUINode_SetPosition](GUINode_SetPosition.md)
- Reads: [g_GUICore](../globals/g_GUICore.md), [g_UIDataModule](../globals/g_UIDataModule.md), [g_UINameTable](../globals/g_UINameTable.md), [UIAgentCursor.hold_timer](../structs/UIAgentCursor.md#hold_timer), [UIAgentCursor.offset_x](../structs/UIAgentCursor.md#offset_x), [UIAgentCursor.offset_y](../structs/UIAgentCursor.md#offset_y), [UIAgentCursor.static_mode](../structs/UIAgentCursor.md#static_mode), [UIAgentCursor.addon](../structs/UIAgentCursor.md#addon), [UIAddonFingerCursor.widget](../structs/UIAddonFingerCursor.md#widget), [UIAddonFingerCursor.cursor_ref_node](../structs/UIAddonFingerCursor.md#cursor_ref_node), [UIAddonFingerCursor.last_x](../structs/UIAddonFingerCursor.md#last_x), [UIAddonFingerCursor.last_y](../structs/UIAddonFingerCursor.md#last_y)
- Writes: [UIAddonFingerCursor.last_x](../structs/UIAddonFingerCursor.md#last_x), [UIAddonFingerCursor.last_y](../structs/UIAddonFingerCursor.md#last_y), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement), [UIAddonFingerCursor.follow_k](../structs/UIAddonFingerCursor.md#follow_k), [UIAddonFingerCursor.custom_k](../structs/UIAddonFingerCursor.md#custom_k)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The Job Tree UIB has no CursorAnchor part, so its hand uses the second rule.

## Open questions

Who sets the hold timer hand+76 is not traced, nor which request supplies hand+80 / +84 for the Job Tree (the stack's pusher was not found) (?).
