# GUINode_NewState

- **Address:** `0x1404096D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINodeState *GUINode_NewState(GUIComponent *comp, UIName *key)`
- **Callers:** sub_140409684 (the by-name wrapper GUIComponent_LoadDef uses)
- **Callees:** GUINodeState_Alloc, UIName_Assign

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the runtime state object of a component for a state name and adds it to the component's state vector.

## Behavior

- V: GUINodeState_Alloc(qword_143CDA280 + 8) allocates the object; UIName_Assign(state, key); state+112 = 1.
- V: the first free of the four owner id slots at state+120 .. +132 receives comp+8 (the component's own id), so the component is the owner that receives the state's events.
- V: the state pointer is appended to the vector comp+616 .. +624 (end of storage +632).

## State touched

- Calls: [GUINodeState_Alloc](GUINodeState_Alloc.md), [UIName_Assign](UIName_Assign.md)
- Writes: [GUINodeState.created](../structs/GUINodeState.md#created), [GUINodeState.owners](../structs/GUINodeState.md#owners), [GUINodeState.name_key](../structs/GUINodeState.md#name_key)

## Notes

The name is ours (IDB: sub_1404096D4). The base component class routes event type 40 of its states to GUIAddon_OnStateEvent (vtable slot 2), which is how state links and jump targets work.

## Open questions

None recorded.
