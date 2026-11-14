# GUIComponentGauge_Update

- **Address:** `0x14040DE78`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentGauge_Update(GUIComponentGauge *g, float dt, char force)`
- **Callers:** vtable 0x140722058 slot 4
- **Callees:** GUINode_UpdateStates, GUIComponentGauge_Step, GUIComponent_ApplyStateAnims, GUIComponent_TickTree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gauge component per-frame update (vtable slot 4): advances the states, runs the value animation step, applies tracks, updates the tree.

## Behavior

- V: GUINode_UpdateStates(g, dt), GUIComponentGauge_Step(g), GUIComponent_ApplyStateAnims(g), GUIComponent_TickTree(g, force).

## State touched

- Calls: [GUINode_UpdateStates](GUINode_UpdateStates.md), [GUIComponentGauge_Step](GUIComponentGauge_Step.md), [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUIComponent_TickTree](GUIComponent_TickTree.md)

## Notes

The name is ours (IDB: sub_14040DE78). Kind 12 component (HP / MP style bars).

## Open questions

None recorded.
