# UIAddonFingerCursor

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The finger cursor addon: the loaded cursor widget (ffto_finger_cursor.uib), the parts it moves, and the glide state of GUICursorHand_StepToward.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="owner_agent"></a>`0x10` | owner_agent | `UIAgentCursor *` | I | The agent that owns the addon (its virtual +48 is called from the input handler). |  |  |
| <a id="widget"></a>`0x18` | widget | `GUIWidget *` | V | The cursor widget; its main component is the first component with type 1 and holds the Loop clock. | [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md), [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md) |  |
| <a id="table_row"></a>`0x24` | table_row | `int32` | V | Row of the addon table (UITable 24) this addon was built from; widget +48 and the pause mask bits come from that row. |  |  |
| <a id="hand_component"></a>`0x30` | hand_component | `GUIComponent *` | I | The Hand component behind the CursorRef reference node: the pose states (Default, Grab, Vertical, VerticalLoop) and the position keys of the bob live here. | [UIAddonFingerCursor_ResetPose](../functions/UIAddonFingerCursor_ResetPose.md), [UIAddonFingerCursor_SetPose](../functions/UIAddonFingerCursor_SetPose.md) | [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md) |
| <a id="cursor_ref_node"></a>`0x38` | cursor_ref_node | `GUINode *` | V | The CursorRef reference node of the main component (kind 12, 100 x 100): GUICursorHand_Update writes its position. | [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md) |
| <a id="button_guide_0"></a>`0x40` | button_guide_0 | `GUIComponent *` | V | Descendant ButtonGuide00 of the Hand component. |  | [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md) |
| <a id="button_guide_1"></a>`0x48` | button_guide_1 | `GUIComponent *` | V | Descendant ButtonGuide01 of the Hand component. |  | [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md) |
| <a id="last_x"></a>`0x1B0` | last_x | `int32` | V | Last placed x of the cursor node (live read, 2026-10-28). | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md) |
| <a id="last_y"></a>`0x1B4` | last_y | `int32` | V | Last placed y. | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md) |
| <a id="follow_k"></a>`0x1B8` | follow_k | `float` | V | Glide factor, 0.4 (g_UIDataModule+24) unless custom_k is set. | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md) | [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md), [UIAddonFingerCursor_ResetGlide](../functions/UIAddonFingerCursor_ResetGlide.md), [UIAgentCursor_SetStatic](../functions/UIAgentCursor_SetStatic.md) |
| <a id="custom_k"></a>`0x1BC` | custom_k | `uint8` | V | 1 = follow_k was set by a caller. | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md) | [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md), [UIAddonFingerCursor_ResetGlide](../functions/UIAddonFingerCursor_ResetGlide.md), [UIAgentCursor_SetStatic](../functions/UIAgentCursor_SetStatic.md) |
| <a id="first_placement"></a>`0x1BD` | first_placement | `uint8` | V | 1 = the next placement is instant (no step). | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md) | [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UIAddonFingerCursor_Bind](../functions/UIAddonFingerCursor_Bind.md), [UIAddonFingerCursor_ResetGlide](../functions/UIAddonFingerCursor_ResetGlide.md), [UIAgentCursor_SetStatic](../functions/UIAgentCursor_SetStatic.md) |
| <a id="field_1c0"></a>`0x1C0` | field_1C0 | `int32` | ? | Cleared with the glide; read as an extra input id by the input handler (sub_1401D333C). |  |  |

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? The size of the object and the fields not listed.
