# Battle_InitScene

- **Address:** `0x1402C8818`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_InitScene(void)`
- **Callers:** sub_1402CB9E8
- **Callees:** sub_1402C60E4, SceneTask_Terminate, sub_1402F7E90, Resource_GetSlotObject, sub_1402C4D1C, sub_1401DB4E4, sub_1401442FC, sub_1402B20C0, sub_140103C50, sub_1402CBCA0, sub_1400EB3AC, sub_1400EB408, sub_140143EA8, UIName_Key, GUINode_FindDescendant, UIName_ReleaseKey, GUINode_StopState, GUINode_PlayStateAtFrame, sub_1400F4BCC, SceneTask_WaitFrame, GUINode_FindState, GUINode_PlayState, sub_1401FA5F0, sub_140226208, sub_140220E5C, sub_1402C83C0, sub_1402C7E2C, GUINode_FindPartByName, sub_1401440FC, sub_140144974, sub_1400FC6D8, Input_TestAction, sub_1400F5B0C, UIAgentCursor_Show, sub_14013F634, sub_1402C8440

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle scene initialiser started by event opcode 0x78 mode 7: it builds the battle UI, places the units and their markers, shows the cursor and waits for the battle to end.

## Behavior

- V: the event opcode 0x78 dispatcher starts this body for mode 7, the battle-start mode.
- V: it copies the battle message/left-panel state and initialises the battle scene objects through sub_1402C60E4 and sub_1402C4D1C.
- V: the UI nodes it drives are named Select, ShowSelectButton, HideSelectButton, ShowUnitInfo, Collision00, ButtonSelect01 and ButtonSelect02.
- V: the unit markers and their sprites are created through the CharaRender helpers and the per-unit preview records.
- V: the cursor is shown with UIAgentCursor_Show and the scene waits with SceneTask_WaitFrame.
- V: it polls Input_TestAction for the battle buttons and reads the merged button mask.
- V: the function has one caller, the opcode 0x78 mode dispatcher, and ends with SceneTask_Terminate.
- I: this is the battle init rather than a generic scene, because the node names are the battle select button and the unit info panel and the caller is the battle mode.
- ?: what sub_1402C8440 and sub_1402C83C0 build after the units are placed; neither was decoded.

## State touched

- Calls: [sub_1402C60E4](sub_1402C60E4.md), [SceneTask_Terminate](SceneTask_Terminate.md), [Resource_GetSlotObject](Resource_GetSlotObject.md), [sub_1402C4D1C](sub_1402C4D1C.md), [UIName_Key](UIName_Key.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [sub_1400F4BCC](sub_1400F4BCC.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [sub_140226208](sub_140226208.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [sub_1400FC6D8](sub_1400FC6D8.md), [Input_TestAction](Input_TestAction.md), [sub_1400F5B0C](sub_1400F5B0C.md), [UIAgentCursor_Show](UIAgentCursor_Show.md)

## Notes

Whole function read (5982 bytes). The node names are string operands; the battle-init role is also the one the battle UI notes give.

## Open questions

None recorded.
