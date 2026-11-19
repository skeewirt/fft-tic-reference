# ErrorBanner_Show

- **Address:** `0x14015293C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void ErrorBanner_Show(void *window, const void *descriptor)`
- **Callers:** sub_14023286C, sub_1402E8E54
- **Callees:** BattleMsg_FillArgs, BattleMsg_TextFromDescriptor, GUITextNode_SetTextExpanded, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows a battle refusal message as the timed red banner.

## Behavior

- V: fills the text node with BattleMsg_TextFromDescriptor and the arguments of BattleMsg_FillArgs.
- V: plays the 'timer' state on the window and the 'Error' state on the second node (+56).
- V: the callers (not this body) also play UI sound cue 106 (sub_1400F4BCC).

## State touched

- Calls: [BattleMsg_FillArgs](BattleMsg_FillArgs.md), [BattleMsg_TextFromDescriptor](BattleMsg_TextFromDescriptor.md), [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Observed behaviours: [BattleRefusalBanner](../behaviors/BattleRefusalBanner.md)

## Notes

Name is ours.

## Open questions

None recorded.
