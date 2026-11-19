# GUIComponent_ApplyStateAnims

- **Address:** `0x140409C28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int64 GUIComponent_ApplyStateAnims(GUIComponent *comp)`
- **Callers:** GUIComponent_Update (sub_14040A1C8) and about ten screen code paths
- **Callees:** GUIWidget_FindComponentCached, GUINode_FindState, GUINode_FindPartByName, GUINode_ApplyAnimChannels, sub_1404015C0, sub_1404007FC, sub_1403D8770, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For every active state of the component (vector comp+616 .. +624), evaluates the state's animation channels at the state's time and writes the sampled values onto the nodes (and the component itself) they target.

## Behavior

- V: skipped when the widget's byte (comp+496 -> +72) is set. For each state S (S+104 = active): t = float S+80. When S+24 != 0 (a transition: a previous state name at S+32/+48 and a component/state key) the previous state's channel list is looked up (GUIWidget_FindComponentCached + GUINode_FindState) and applied first with time t - (float)(int)S+64 when t >= that delay.
- V: each target of the state's own list (vector S+144 .. +152; element = a element) is resolved: sub_1404007FC tests it against the global 'self' name (qword_143CDA2A0+5144): the component itself is handled by sub_1404015C0, any other name is a node, found by GUINode_FindPartByName(comp+272, name) and animated by GUINode_ApplyAnimChannels(channels, t, node, S+111).
- V: nothing is interpolated here; this function only selects states, targets and times.

## State touched

- Calls: [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_ApplyAnimChannels](GUINode_ApplyAnimChannels.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md), [GUINodeState.enabled](../structs/GUINodeState.md#enabled), [GUINodeState.frame](../structs/GUINodeState.md#frame), [GUINodeState.absolute](../structs/GUINodeState.md#absolute), [GUINodeState.channels](../structs/GUINodeState.md#channels), [GUINodeState.transition_key](../structs/GUINodeState.md#transition_key), [GUINodeState.prev_component](../structs/GUINodeState.md#prev_component), [GUINodeState.prev_state](../structs/GUINodeState.md#prev_state), [GUINodeState.transition_delay](../structs/GUINodeState.md#transition_delay)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [GUIComponentGauge_Update](GUIComponentGauge_Update.md), [GUIComponentScrollBar_Update](GUIComponentScrollBar_Update.md), [GUIComponent_Update](GUIComponent_Update.md)

## Notes

The name is ours (IDB: sub_140409C28). Run before the node tree pass, so animated position / scale / colour / opacity are in the node fields when GUINode_UpdateSubtree builds the matrices.

## Open questions

What S+24 / S+64 / S+111 are exactly (transition flag, delay, absolute/relative flag); sub_1404015C0.
