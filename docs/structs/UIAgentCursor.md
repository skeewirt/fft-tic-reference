# UIAgentCursor

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The cursor agent: element 1 of the addon manager's agent vector (global qword_143CD9DA8, vector at +16). It owns the finger cursor addon, the request stack of cursor modes, and the state that defers a restart of the bob to the next frame.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="addons_begin"></a>`0x10` | addons_begin | `UIAddon **` | V | Addon list (begin +0x10, end +0x18); the agent's update runs only while one addon's widget (addon +0x18, flag +0x4A) is active. |  |  |
| <a id="addon"></a>`0x40` | addon | `UIAddonFingerCursor *` | V | The finger cursor addon (GUICursorHand_Update reads the node and widget through it). | [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UIAgentCursor_Hide](../functions/UIAgentCursor_Hide.md), [UIAgentCursor_Show](../functions/UIAgentCursor_Show.md) |  |
| <a id="mode"></a>`0x48` | mode | `int32` | V | Request mode: 1 or 2 shows the cursor, 0 hides it (UIAgentCursor_PopRequest). |  | [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md) |
| <a id="hold_timer"></a>`0x4C` | hold_timer | `uint32` | V | Milliseconds GUICursorHand_Update counts down (dt from g_GUICore+2100) before it acts; the writer was not found. | [GUICursorHand_Update](../functions/GUICursorHand_Update.md) |  |
| <a id="offset_x"></a>`0x50` | offset_x | `int32` | V | Added to the focused node's rect left edge to get the hand's target x. | [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md) |
| <a id="offset_y"></a>`0x54` | offset_y | `int32` | V | Added to the focused node's rect centre y. | [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md) |
| <a id="widget_priority"></a>`0x58` | widget_priority | `int32` | I | Copy of the cursor widget's priority word (widget +62), written on event 0x10001. |  |  |
| <a id="requests_begin"></a>`0x68` | requests_begin | `Request *` | V | Request stack: 16-byte entries {int mode, int dx, int dy, byte show_again, byte static}; end +0x70, end of storage +0x78. | [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md) |  |
| <a id="show_state"></a>`0x80` | show_state | `int32` | V | 0 inside the agent update, 1 normally, 2 = a show is pending (UIAgentCursor_Show); UI_FrameUpdate turns 2 into a restart of the bob at the start of the next frame. | [UI_FrameUpdate](../functions/UI_FrameUpdate.md), [UIAgentCursor_Show](../functions/UIAgentCursor_Show.md) | [UI_FrameUpdate](../functions/UI_FrameUpdate.md), [UIAgentCursor_Hide](../functions/UIAgentCursor_Hide.md), [UIAgentCursor_Show](../functions/UIAgentCursor_Show.md) |
| <a id="static_mode"></a>`0x84` | static_mode | `uint8` | V | 1 = no bob, no glide (UIAgentCursor_SetStatic). | [GUICursorHand_Update](../functions/GUICursorHand_Update.md), [UI_FrameUpdate](../functions/UI_FrameUpdate.md) | [UIAgentCursor_PopRequest](../functions/UIAgentCursor_PopRequest.md), [UIAgentCursor_SetStatic](../functions/UIAgentCursor_SetStatic.md) |

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? The request pusher; the object's size and the fields at +0x20 .. +0x3F.
