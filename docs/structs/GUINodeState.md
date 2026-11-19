# GUINodeState

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 208 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One state (timeline) of a component: its clock, its loop range, its flags and the channel sets and entries it applies. Created by GUINode_NewState from a 208-byte pool slot, filled by GUIComponent_LoadDef / UIAnim_PlayStateTracks, started by GUINode_PlayState, advanced by GUINodeState_Advance and applied by GUIComponent_ApplyStateAnims. The states of a component are the vector at component +616 .. +624.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by | Observed behaviours |
|---|---|---|---|---|---|---|---|
| <a id="name_key"></a>`0x0` | name_key | `element {char *text, uint32 id at +8}` | V | The state's name (UIName_Assign / UIName_SetKey); GUINode_FindState matches the interned id at +8. | [GUINode_NewState](../functions/GUINode_NewState.md) |  |  |
| <a id="transition_key"></a>`0x10` | transition_key | `element` | I | Set by GUIComponent_LoadDef from the state record; when its id at +0x18 is non-zero GUIComponent_ApplyStateAnims applies a previous state first, and passes this key to the component lookup. |  | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="prev_component"></a>`0x20` | prev_component | `element` | I | Component of the previous state (the own component when its id at +0x28 is 0). |  | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="prev_state"></a>`0x30` | prev_state | `element` | I | Name of the previous state (the state's own name when its id at +0x38 is 0). |  | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="transition_delay"></a>`0x40` | transition_delay | `int32` | I | Frames before the transition's state applies: the previous state is sampled at (time - delay) once time >= delay. |  | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="record_flags"></a>`0x44` | record_flags | `int32` | V | Written from the state record's int at +4 by GUIComponent_LoadDef; -1 in a fresh object. What reads it is not known. | [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md) |  |  |
| <a id="rate"></a>`0x48` | rate | `float` | V | Clock multiplier, 1.0 in a fresh object; GUINodeState_Advance adds dt * rate to time. | [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="time"></a>`0x4C` | time | `float` | V | Clock in seconds. GUINodeState_Advance: time = (dt * rate) + time; a loop or jump sets it to target / 60.0. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md), [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [UIStateClock](../behaviors/UIStateClock.md) |
| <a id="frame"></a>`0x50` | frame | `float` | V | Current frame = time * 60.0, a float (not an integer count). GUIComponent_ApplyStateAnims samples every active state at this value; for a state driven by a link GUIAddon_OnStateEvent writes it. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md), [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md) | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [UIStateClock](../behaviors/UIStateClock.md) |
| <a id="prev_frame"></a>`0x54` | prev_frame | `float` | V | The frame at the previous tick (the jump-marker and keyframe-event tests compare against it); equals frame when the state did not advance. | [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="frame_count"></a>`0x58` | frame_count | `int32` | V | Frames of the state (the record's +28), the loop end when the range is unset. | [UIAnim_PlayStateTracks](../functions/UIAnim_PlayStateTracks.md) | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="range_start"></a>`0x5C` | range_start | `int32` | V | Loop range start; the range counts only when range_start < range_end, otherwise the range is 0 .. frame_count. |  | [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="range_end"></a>`0x60` | range_end | `int32` | V | Loop range end. |  | [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="enabled"></a>`0x68` | enabled | `uint8` | V | 1 = the state takes part in GUINode_UpdateStates and GUIComponent_ApplyStateAnims. 1 in a fresh object; GUINode_StopState clears it. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Alloc](../functions/GUINodeState_Alloc.md), [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md), [UIAnim_PlayStateTracks](../functions/UIAnim_PlayStateTracks.md) | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md), [GUINode_UpdateStates](../functions/GUINode_UpdateStates.md) |  |
| <a id="running"></a>`0x69` | running | `uint8` | V | Set by GUINode_PlayState; GUINodeState_Advance advances only while it is set and clears it at a non-looping end. | [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="dirty"></a>`0x6A` | dirty | `uint8` | V | Set by GUINode_PlayState and by the link writer; cleared by GUINodeState_Advance. While set GUINodeState_IsPastEnd answers false. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="paused"></a>`0x6B` | paused | `uint8` | V | 1 = the clock does not advance (a parent link drives the frame). GUINode_PlayState on a paused state only clears it. | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINode_PlayState](../functions/GUINode_PlayState.md) | [GUINode_PlayState](../functions/GUINode_PlayState.md), [GUINode_UpdateStates](../functions/GUINode_UpdateStates.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="loop"></a>`0x6C` | loop | `uint8` | V | 1 = at the end frame the state restarts at the range start. From the UIB record's byte +32 at load; UIAddonFingerCursor_PlayLoop sets it for the cursor's Loop. | [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md), [UIAnim_PlayStateTracks](../functions/UIAnim_PlayStateTracks.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="keep_alive"></a>`0x6D` | keep_alive | `uint8` | I | GUINode_UpdateStates keeps advancing a state that is past its end while this is set; the rest of its meaning is open. |  | [GUINode_UpdateStates](../functions/GUINode_UpdateStates.md) |  |
| <a id="hold"></a>`0x6E` | hold | `uint8` | V | 1 = the state does not advance and counts as past its end (GUINodeState_IsPastEnd); cleared by GUINode_PlayState. | [GUINode_PlayState](../functions/GUINode_PlayState.md) | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="absolute"></a>`0x6F` | absolute | `uint8` | V | 1 = sampled values replace the node's fields, 0 = they are combined with them. 1 for every state loaded from a UIB timeline. | [UIAnim_PlayStateTracks](../functions/UIAnim_PlayStateTracks.md) | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="created"></a>`0x70` | created | `uint8` | V | Set to 1 by GUINode_NewState; its reader was not found. | [GUINode_NewState](../functions/GUINode_NewState.md) |  |  |
| <a id="owners"></a>`0x78` | owners | `uint32[4]` | V | Owner ids that receive the state's events (GUIOwners_PostEvent). GUINode_NewState puts the component's own id here. | [GUINode_NewState](../functions/GUINode_NewState.md) |  |  |
| <a id="channels"></a>`0x90` | channels | `vector<AnimChannelSet *>` | V | One channel set per target node (begin +0x90, end +0x98): the key tracks GUINode_ApplyAnimChannels samples (track pointers a[6] .. a[31]). |  | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) |  |
| <a id="entries"></a>`0xB0` | entries | `vector<GUINodeStateEntry> (64 B)` | V | Begin +0xB0, end +0xB8: the jump markers, triggers, state links and resets of the state. | [UIAnim_ApplyComponentTrack](../functions/UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](../functions/UIAnim_ApplyTrack.md) | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md) |  |
| <a id="field_c8"></a>`0xC8` | field_C8 | `int32` | ? | Zero in a fresh object; no reader found. |  |  |  |

## Behavior

- V: a fresh object is 1.0 at +0x48, enabled (+0x68 = 1), everything else zero except +0x44 = -1 (GUINodeState_Alloc).
- V: the clock rule is in the behavior UIStateClock; the bob of the finger cursor is in CursorGloveBob.

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? +0x44, +0x6D, +0x70 and +0xC8; the meaning of the three transition keys is inferred from their use in GUIComponent_ApplyStateAnims.
