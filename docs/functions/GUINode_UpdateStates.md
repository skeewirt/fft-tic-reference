# GUINode_UpdateStates

- **Address:** `0x1404099F4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_UpdateStates(GUINode *comp, float dt)`
- **Callers:** GUINode_Update path (the per-frame component update)
- **Callees:** GUINodeState_Advance, GUINode_StopState, sub_140400118

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances every enabled state (timeline) of a component node by dt, or stops it when it is no longer valid.

## Behavior

- V: runs only when the byte at (comp+496)+80 is 0; for each state in the vector comp+616..+624 with state+104 != 0: when !GUINodeState_IsPastEnd(state) (sub_140400118) or state+109 or state+107 is set, GUINodeState_Advance(state, dt); otherwise (past its end and neither flag set) GUINode_StopState (V: re-read 2026-10-28 against the decompile; the earlier wording had the polarity inverted).

## State touched

- Calls: [GUINodeState_Advance](GUINodeState_Advance.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [GUINodeState.enabled](../structs/GUINodeState.md#enabled), [GUINodeState.paused](../structs/GUINodeState.md#paused), [GUINodeState.keep_alive](../structs/GUINodeState.md#keep_alive)

## Referenced by

- Called by: [GUIComponentGauge_Update](GUIComponentGauge_Update.md), [GUIComponentScrollBar_Update](GUIComponentScrollBar_Update.md)

## Notes

The name is ours (IDB: sub_1404099F4). Listed as the caller of GUINodeState_Advance; the accept rule of sub_140400118 was not read.

## Open questions

? sub_140400118.
