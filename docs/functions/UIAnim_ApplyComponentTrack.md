# UIAnim_ApplyComponentTrack

- **Address:** `0x1403F7AC0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIAnim_ApplyComponentTrack(int a1, int *track, __int64 state)`
- **Callers:** UIAnim_PlayStateTracks
- **Callees:** UIAnim_InterpToCurve, sub_1403F8708, sub_140400448

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies a state track aimed at the component itself (target kind 4002, property tags >= 5031) as an animated component-effect property.

## Behavior

- V: tags 5031 to 5034 (cases 0 to 3) do not animate a property; they append an entry to the state's entry list (sub_140400448; 64-byte entries, fields at +0 type, +4 track id, +8 start frame = track +12, +12 end frame = start + track duration (+16), +48 / +52 a value). 5031: type 1 = a jump marker (GUINodeState_Advance: playing past the end frame jumps to the start frame; the Hand's Loop carries one from 0 to 40). 5032 / 5033 / 5034: types 2 / 3 / 4 with the id at value block +80 (5034 also value +84 x 256 at entry +52), the entries GUIAddon_OnStateEvent turns into trigger calls.
- V: switch on tag - 5031; value = 32 bits at track value block +84 (some x 0.01), curve from UIAnim_InterpToCurve(+80); queued with sub_1403F8708 on the component effect object (qword_143CDA2A0 + 5144) with a property id: tag 5050 -> 38 and 5051 -> 39 (decoded as the glow radius and strength: the Line states set 0 / 0 for Lock and Unlock, 4.0 / 0.5 for the *OnCursor states), 5052 -> 40 (x 0.01), 5053 -> 41; other tags use other offsets (5176.. = other targets).

## State touched

- Calls: [UIAnim_InterpToCurve](UIAnim_InterpToCurve.md), [UIAnim_StoreKey](UIAnim_StoreKey.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)
- Writes: [GUINodeState.entries](../structs/GUINodeState.md#entries), [GUINodeStateEntry.type](../structs/GUINodeStateEntry.md#type), [GUINodeStateEntry.start_frame](../structs/GUINodeStateEntry.md#start_frame), [GUINodeStateEntry.end_frame](../structs/GUINodeStateEntry.md#end_frame), [GUINodeStateEntry.value](../structs/GUINodeStateEntry.md#value)

## Referenced by

- Called by: [UIAnim_PlayStateTracks](UIAnim_PlayStateTracks.md)

## Notes

Property 38 / 39 = glow radius / strength is inferred from the values (0 / 0 idle, 4.0 / 0.5 on cursor) and the live layer records (radius 2.667 = 4.0 * 2/3, strength 0.5) (V/I).

## Open questions

Properties 40 / 41 and the other tags (?).
