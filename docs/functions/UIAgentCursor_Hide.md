# UIAgentCursor_Hide

- **Address:** `0x1401D2F24`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentCursor_Hide(UIAgentCursor *agent)`
- **Callers:** UIAgentCursor_PopRequest, sub_1401D2E9C, sub_1400E43B4 and about ten screen code paths
- **Callees:** GUIWidget_FindFirstKind1Component2, GUIComponent_StopAllStates

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hides the finger cursor: cancels a pending show, stops every state of the cursor widget's main component and hides the widget.

## Behavior

- V: when agent+128 is 2 it is set back to 1 (a pending show is cancelled).
- V: when the agent has its addon (agent+64) and the addon's widget is active (widget+74 != 0) or the addon's byte +42 is set: comp = GUIWidget_FindFirstKind1Component2(widget); GUIComponent_StopAllStates(comp) (which zeroes the Loop clock) and sub_1401D1EAC(addon, 1) (GUIWidget_Hide).
- V: after a Hide the next UIAgentCursor_Show starts the Loop from frame 0 again.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md)
- Reads: [UIAgentCursor.addon](../structs/UIAgentCursor.md#addon)
- Writes: [UIAgentCursor.show_state](../structs/UIAgentCursor.md#show_state)

## Referenced by

- Called by: [UIAgentCursor_PopRequest](UIAgentCursor_PopRequest.md)

## Notes

The name is ours (IDB: sub_1401D2F24).

## Open questions

None recorded.
