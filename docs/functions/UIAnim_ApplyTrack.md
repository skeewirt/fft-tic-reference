# UIAnim_ApplyTrack

- **Address:** `0x1403F6FC0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIAnim_ApplyTrack(__int64 a1, int *track, __int64 state, __int64 node, __int64 part)`
- **Callers:** UIAnim_PlayStateTracks
- **Callees:** UIAnim_InterpToCurve, sub_1403F8708, sub_140400448

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts one state track aimed at a node (target kind 4001, property tags 5001..5030) into a queued property animation on that node.

## Behavior

- V: switch on tag - 5001; cases read the value block (track+28 offset) at +116/+120 (two ints), +84 (floats) or +4 bytes (colours), the curve from UIAnim_InterpToCurve(+48) and queue the animation with sub_1403F8708 under an internal property type (tags 5002 -> 3, 5003 -> 4, ...).
- V: tags above 5030 are not handled here (default returns); they go through UIAnim_ApplyComponentTrack.
- V: tag 5002 (case 1): the value pair is the two ints at value block +116 / +120, the interpolation id at +48 (curve = UIAnim_InterpToCurve), the key frame is the track's start frame (+12), key type 3 (node position); UIAnim_StoreKey stores it as key {frame, curve, pair}. So a position track with several keys becomes one key track whose key k holds the pair of file key k and the curve that shapes the interval from k to k + 1.
- V: tags 5028 / 5029 / 5030 (cases 27 / 28 / 29) append state-entry records instead (sub_140400448): type 5 (state link) / 6 (state reset) / 7 (part trigger) with start frame = track +12, end frame = start + duration, name 1 = the target node's name, and for 5 and 6 name 2 = the string at value block +48 + the int stored there (the child state's name); for 7 an int at value +48. Data: the finger cursor's Widget component Loop state has one 5028 track, target CursorRef, frames 0 to 40, child state Loop.

## State touched

- Calls: [UIAnim_InterpToCurve](UIAnim_InterpToCurve.md), [UIAnim_StoreKey](UIAnim_StoreKey.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)
- Writes: [GUINodeState.entries](../structs/GUINodeState.md#entries), [GUINodeStateEntry.type](../structs/GUINodeStateEntry.md#type), [GUINodeStateEntry.start_frame](../structs/GUINodeStateEntry.md#start_frame), [GUINodeStateEntry.end_frame](../structs/GUINodeStateEntry.md#end_frame), [GUINodeStateEntry.target_name](../structs/GUINodeStateEntry.md#target_name), [GUINodeStateEntry.child_state](../structs/GUINodeStateEntry.md#child_state)

## Referenced by

- Called by: [UIAnim_PlayStateTracks](UIAnim_PlayStateTracks.md)

## Notes

The UIB timeline tag table documents the tag -> value kind mapping read from the same switch.

## Open questions

Only the switch head was read, not every case (?).
