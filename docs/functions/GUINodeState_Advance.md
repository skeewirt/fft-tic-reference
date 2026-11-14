# GUINodeState_Advance

- **Address:** `0x1403FFDF8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINodeState_Advance(NodeState *s, float dt)`
- **Callers:** GUINode_UpdateStates (sub_1404099F4)
- **Callees:** GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The clock of a UIB state (timeline): advances its time and 60 fps frame, applies jump markers and looping, and posts the keyframe-event (40), loop (38) and finished (39) events to the state's owners.

## Behavior

- V: nothing happens unless dt > 0. Saved: f0 = s+84 (frame at the previous tick), fr = s+80 (frame), dirty = s+106 (then cleared to 0).
- V: advances only when running (s+105) and not paused (s+107 == 0) and s+110 == 0: [lo, hi) = (s+92, s+96) when s+92 < s+96, else (0, s+88 = frame count); s+76 (time) += dt * s+72 (rate); fr = s+76 * 60.0; s+80 = fr.
- V: jump markers: for every entry of the state's list (s+176..+184, 64 bytes each) with type (+0) == 1: when (float)entry+12 > f0 and fr >= (float)entry+12: hit = 1, s+80 = (float)entry+8 and s+76 = entry+8 / 60.0 (a goto: playing past frame entry+12 jumps to entry+8).
- V: end: the test uses the current s+80; when >= (float)hi: if s+108 (loop) is set: hit = 1, s+80 = lo, s+76 = lo / 60.0; else s+80 = hi, finished = 1, s+105 = 0 (stopped on the last frame).
- V: s+84 = the frame after these rules (also when not advancing, then it equals s+80).
- V (keyframe events): for every entry with type != 1, event 0x28 (40) with ev+16 = s and ev+24 = the entry index is posted to the owners (s+120, node 0) when entry+8 != entry+12 (a span entry: EVERY tick, so it can drive a continuous link), or when |f0 - fr| > 1.19e-7 and (float)entry+8 > f0 + (dirty ? -1.19e-7 : 0) and fr >= (float)entry+8 (a point entry fires the tick the frame passes it; on the first tick after a (re)start frame 0 fires). Here fr is the frame after the advance but BEFORE marker jumps and looping.
- V: after the entries: hit -> event 0x26 (38) {state, -1}; finished -> event 0x27 (39) {state, -1}.
- V: the arithmetic is single precision: time = (dt * rate) + time and frame = time * 60.0. A jump or a loop sets the frame to the target integer and the time to target / 60.0, so the overshoot past the end frame is dropped: a cycle lasts the whole number of ticks needed to reach the end frame (40 ticks of exactly 1/60 s for a 40-frame state, 40.0 reached at the 40th tick).
- V: a state that is paused by a link (+107) is not advanced: only its dirty byte is cleared and +84 = +80; its frame is written by GUIAddon_OnStateEvent. With dt <= 0 nothing at all happens, not even the dirty clear.

## State touched

- Calls: [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [GUINodeState.rate](../structs/GUINodeState.md#rate), [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.prev_frame](../structs/GUINodeState.md#prev_frame), [GUINodeState.frame_count](../structs/GUINodeState.md#frame_count), [GUINodeState.range_start](../structs/GUINodeState.md#range_start), [GUINodeState.range_end](../structs/GUINodeState.md#range_end), [GUINodeState.running](../structs/GUINodeState.md#running), [GUINodeState.paused](../structs/GUINodeState.md#paused), [GUINodeState.hold](../structs/GUINodeState.md#hold), [GUINodeState.loop](../structs/GUINodeState.md#loop), [GUINodeState.dirty](../structs/GUINodeState.md#dirty), [GUINodeState.entries](../structs/GUINodeState.md#entries), [GUINodeStateEntry.type](../structs/GUINodeStateEntry.md#type), [GUINodeStateEntry.start_frame](../structs/GUINodeStateEntry.md#start_frame), [GUINodeStateEntry.end_frame](../structs/GUINodeStateEntry.md#end_frame)
- Writes: [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.prev_frame](../structs/GUINodeState.md#prev_frame), [GUINodeState.dirty](../structs/GUINodeState.md#dirty), [GUINodeState.running](../structs/GUINodeState.md#running)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [GUINode_UpdateStates](GUINode_UpdateStates.md)
- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md), [UIStateClock](../behaviors/UIStateClock.md)

## Notes

The name is ours (IDB: sub_1403FFDF8). State layout (V): +72 rate, +76 time s, +80 frame, +84 previous frame, +88 frame count, +92 / +96 loop range, +104 enabled, +105 running, +106 dirty / restarted, +107 paused (scrub-driven by a parent link), +108 loop, +110 hold. The tracks are NOT evaluated here: GUIComponent_ApplyStateAnims runs right after GUINode_UpdateStates in GUIComponent_Update and samples every active state at the float frame +80 (V; the key search inside the samplers truncates it, the interval position does not). GUINode_ApplyStateAtFrame (sub_140409A98) is the one-shot variant for a given integer frame. State fields: struct GUINodeState.

## Open questions

? +109 and +110 meaning.
