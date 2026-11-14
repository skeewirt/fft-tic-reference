# GUIAddon_OnStateEvent

- **Address:** `0x14040A664`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIAddon_OnStateEvent(GUIAddonBase *a, GUINode *node, UIEvent *ev)`
- **Callers:** owner dispatch (GUIOwners_PostEvent slot 2) of the UI addons; direct calls from sub_14040AAF8, sub_14040B788, sub_14040D060, sub_14040DBD8
- **Callees:** GUINode_FindDescendant, GUINode_FindState, GUINode_PlayState, GUINode_FindPartByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shared owner handler for the keyframe events (type 40) a state posts: acts on the state entry the event points at (sound triggers, nested state links, state resets, part triggers).

## Behavior

- V: only handles ev type (ev+0) == 40; entry = *(*(ev+16) + 176) + 64 * (int)ev+24 (the state's entry list, 64 bytes per entry); switch entry+0:
- V: 2 = a->obj (a+496) virtual +112 (obj, entry+48, a+548). 3 = when obj+84 == 0: obj virtual +120 (obj, entry+48), else a record {byte 1, id = entry+48} is appended to the queue at obj+304.. 4 = when obj+84 == 0: virtual +128 (obj, entry+48), else record {byte 2, id = entry+48, float (int)entry+52 * (1/256)} is queued. I: 2 / 3 / 4 are sound / voice triggers (ids and a 8.8 volume).
- V: 5 (state link): child = GUINode_FindDescendant(a, entry+16), childState = GUINode_FindState(child, entry+32); p = max((state.frame(+80) - (float)entry+8) * (float)childState+88 / (float)(entry+12 - entry+8), 0); childState+104 = 1; when not running: GUINode_PlayState; childState+107 = 1 (paused: now driven by the parent); childState+80 = min(p, (float)childState+88); +106 = 1; +76 = frame / 60.0.
- V: 6: the child's state is reset: +76 / +80 / +84 = 0 and +104..+110 = 0 (a stop). 7: part = GUINode_FindPartByName(a+272, entry+16) of kind 10; its virtual +136 (obj, a, part, entry+48).
- V: the owner that receives a state's events is the component that created it (GUINode_NewState stores comp+8 in the state's owner slots) and the base component class has this function in vtable slot 2, so the events of a component's states arrive with a = that component.
- I: for the finger cursor widget this makes the Hand's Loop state a scrubbed copy of the main component's Loop: the link entry (frames 0 to 40, child CursorRef, child state Loop of 40 frames) gives p = frame * 40 / 40, so the Hand's Loop frame equals the main component's Loop frame at every tick (flow CursorGloveFrame).

## State touched

- Calls: [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_FindPartByName](GUINode_FindPartByName.md)
- Reads: [GUINodeState.entries](../structs/GUINodeState.md#entries), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.frame_count](../structs/GUINodeState.md#frame_count), [GUINodeState.running](../structs/GUINodeState.md#running), [GUINodeStateEntry.type](../structs/GUINodeStateEntry.md#type), [GUINodeStateEntry.start_frame](../structs/GUINodeStateEntry.md#start_frame), [GUINodeStateEntry.end_frame](../structs/GUINodeStateEntry.md#end_frame), [GUINodeStateEntry.target_name](../structs/GUINodeStateEntry.md#target_name), [GUINodeStateEntry.child_state](../structs/GUINodeStateEntry.md#child_state)
- Writes: [GUINodeState.enabled](../structs/GUINodeState.md#enabled), [GUINodeState.paused](../structs/GUINodeState.md#paused), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.dirty](../structs/GUINodeState.md#dirty)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)

## Notes

The name is ours (IDB: sub_14040A664). The state link (5) is how a parent animation scrubs a child animation: the child frame is parent.frame mapped linearly onto [entry+8, entry+12] and scaled to the child's frame count, clamped to the child's end; the same rule without the clamp is in GUINode_ApplyStateAtFrame.

## Open questions

? Which virtuals +112 / +120 / +128 / +136 are (I: sound / voice / part trigger).
