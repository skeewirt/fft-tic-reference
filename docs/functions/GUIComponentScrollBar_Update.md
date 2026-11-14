# GUIComponentScrollBar_Update

- **Address:** `0x14040BBA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentScrollBar_Update(GUIComponentScrollBar *bar, float dt, char force)`
- **Callers:** vtable 0x140722238 slot 4
- **Callees:** GUINode_UpdateStates, GUIComponent_ApplyStateAnims, GUIComponentScrollBar_StepKnob, GUIComponent_TickTree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scroll bar per-frame update (vtable slot 4): advances the states, applies their tracks, repositions the knob and then updates the node tree.

## Behavior

- V: GUINode_UpdateStates(bar, dt), GUIComponent_ApplyStateAnims(bar), GUIComponentScrollBar_StepKnob(bar), GUIComponent_TickTree(bar, force).

## State touched

- Calls: [GUINode_UpdateStates](GUINode_UpdateStates.md), [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_TickTree](GUIComponent_TickTree.md)

## Notes

The name is ours (IDB: sub_14040BBA4). Compare GUIComponent_Update (base: UpdateStates, ApplyStateAnims, TickTree) and the Gauge version GUIComponentGauge_Update (the step is before ApplyStateAnims there).

## Open questions

None recorded.
