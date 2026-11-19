# GUIComponent_StopAllStates

- **Address:** `0x14040996C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_StopAllStates(GUIComponent *comp)`
- **Callers:** UIAgentCursor_Hide, UIAddonFingerCursor_FreezePose
- **Callees:** GUINode_StopState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stops every state of a component.

## Behavior

- V: for each state pointer of the vector comp+616 .. +624: GUINode_StopState(comp, state), with the state's own first name key (the key stored at state+0) as the key argument.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md)

## Referenced by

- Called by: [Battle_MenuHidePage](Battle_MenuHidePage.md), [Battle_MenuShowPage](Battle_MenuShowPage.md), [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md), [UIAgentCursor_Hide](UIAgentCursor_Hide.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md)

## Notes

The name is ours (IDB: sub_14040996C). GUINode_StopState also stops the children of state links, so the Hand's scrubbed Loop is stopped with the main component's Loop.

## Open questions

None recorded.
