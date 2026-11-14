# GUIComponent_Enable

- **Address:** `0x140408EBC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_Enable(GUIComponent *comp, char recurse)`
- **Callers:** about 22 UI addon methods (sub_1400EA5B8, sub_1401027D8, sub_14012C8AC, sub_14012FC6C, sub_14013F634, sub_14014129C, sub_140153CA0, ...)
- **Callees:** GUIWidget_FindComponentCached, GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a component enabled (+554 = 1) and plays its Enable state (Disable stopped); optionally enables the components its reference nodes point at.

## Behavior

- V: when recurse != 0: for every node of the widget's node vector (widget = comp+496; vector +160..+168) with kind (node+52) 12 and owner id (node+48) equal to this component's id (comp+8): the referenced component is found with GUIWidget_FindComponentCached(widget, node+208, node+224, node+304) and GUIComponent_Enable(child, 1) runs on it.
- V: when comp+554 is 0: comp+554 = 1; GUINode_StopState(comp, key +4648 = 'Disable'); FindState(comp, key +4632 = 'Enable'), +104 = 1, PlayState; event {10} to the owners (comp+584).
- V: an already enabled component does nothing in the second part (the recursion still runs).

## State touched

- Calls: [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md)

## Notes

The name is ours (IDB: sub_140408EBC). Byte +554 is the flag GUICore_UpdateFrame tests before delivering press / click (V); the separate +416 byte of other sheets is 'loaded'. The widget's node vector holds the reference nodes (kind 12) of nested components.

## Open questions

? the relation of node+48 to comp+8 (owner component id) is read from the compare only.
