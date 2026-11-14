# UIAnim_PlayStateTracks

- **Address:** `0x1403F6EA0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAnim_PlayStateTracks(UILoader *ld, StateRecord *rec, GUIComponent *comp, GUINodeState *state)`
- **Callers:** GUIComponent_LoadDef (the only code caller; an earlier note named GUINode_PlayState, which does not call it)
- **Callees:** UIAnim_ApplyTrack (sub_1403F6FC0), UIAnim_ApplyComponentTrack (sub_1403F7AC0), GUINode_FindPartByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts the tracks of one UIB state record (a timeline) into the runtime state object when a component is built: frame count, loop byte, absolute flag, key tracks and entries.

## Behavior

- V: state record +0 type (3 = timeline), +4/+8 tracks offset/count, +20/+24 target table, +28 frame count, +32 loop byte; a track's target entry 4001 names a node part.
- V: for a type 3 record: state+88 = frame count, state+108 = the loop byte, state+111 = 1 (absolute: the sampled values replace the node's fields, they are not combined with them); state+104 = 0 when the loader's byte +33 is set.
- V: each track (32 bytes): target entry kind 4001 -> UIAnim_ApplyTrack with the node part found by name; kind 4002 -> UIAnim_ApplyComponentTrack.

## State touched

- Calls: [UIAnim_ApplyTrack](UIAnim_ApplyTrack.md), [UIAnim_ApplyComponentTrack](UIAnim_ApplyComponentTrack.md), [GUINode_FindPartByName](GUINode_FindPartByName.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)
- Writes: [GUINodeState.frame_count](../structs/GUINodeState.md#frame_count), [GUINodeState.loop](../structs/GUINodeState.md#loop), [GUINodeState.absolute](../structs/GUINodeState.md#absolute), [GUINodeState.enabled](../structs/GUINodeState.md#enabled)

## Referenced by

- Called by: [GUIComponent_LoadDef](GUIComponent_LoadDef.md)

## Notes

Format documented in docs/reference/animations.md; the studio's timeline decoder reads it. It runs at load time, not when a state is played.

## Open questions

None recorded.
