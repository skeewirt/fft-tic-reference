# GUINodeStateEntry

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of a state's entry list (GUINodeState.entries): a jump marker, a trigger, a state link, a state reset or a part trigger, built from the state's special tracks by UIAnim_ApplyTrack and UIAnim_ApplyComponentTrack.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="type"></a>`0x0` | type | `int32` | V | 1 jump marker (tag 5031), 2 / 3 / 4 triggers (tags 5032 / 5033 / 5034), 5 state link (5028), 6 state reset (5029), 7 part trigger (5030). | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) |
| <a id="track_id"></a>`0x4` | track_id | `int32` | V | The id of the track in the UIB file. |  |  |
| <a id="start_frame"></a>`0x8` | start_frame | `int32` | V | The track's start frame. Jump marker: the frame jumped to. State link: the parent frame that maps to child frame 0. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) |
| <a id="end_frame"></a>`0xC` | end_frame | `int32` | V | Start frame + the track's duration. Jump marker: playing past it jumps to start_frame. State link: the parent frame that maps to the child's last frame. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) |
| <a id="target_name"></a>`0x10` | target_name | `UIName` | V | Types 5, 6, 7: the target node's name (the node holding the child component). | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md) | [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) |
| <a id="child_state"></a>`0x20` | child_state | `UIName` | V | Types 5 and 6: the child state's name. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md) | [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) |
| <a id="value"></a>`0x30` | value | `int32` | V | Types 2, 3, 4, 7: the id passed to the trigger. |  | [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md) |
| <a id="value2"></a>`0x34` | value2 | `int32` | V | Type 4: the number at value block +84 times 256 (GUIAddon_OnStateEvent multiplies it by 1/256). |  |  |

## Behavior

- V: GUINodeState_Advance posts event 40 for every entry whose type is not 1 and whose start and end frames differ on every tick (a span entry), and for a point entry on the tick its frame is passed.

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? Whether 2 / 3 / 4 are sound and voice triggers (inferred from their use only).
