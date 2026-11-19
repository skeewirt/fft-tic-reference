# WorldMapRouteGrow_OnState

- **Address:** `0x140162344`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapRouteGrow_OnState(void *effect, int state)`
- **Callers:** not recorded
- **Callees:** UITable_GetRowByKey, GUINode_FindState, GUINode_PlayState, GUIComponent_StopAllStates, Str_Format, sub_1400F4BCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the state of the route-grow effect.

## Behavior

- V: plays 'Show' / 'Hide' with the Route state_suffix (+0x10) appended when growing forward, or state_suffix_2 (+0x14) when reversed (effect +105); then plays UI sound 44 or 45.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md), [Str_Format](Str_Format.md), [sub_1400F4BCC](sub_1400F4BCC.md)

## Referenced by

- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
