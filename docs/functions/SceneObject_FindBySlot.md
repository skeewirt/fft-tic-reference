# SceneObject_FindBySlot

- **Address:** `0x140260A98`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *SceneObject_FindBySlot(int16_t slot)`
- **Callers:** About 121 routines with 207 call sites, including EventScript_Run (more than ten sites), EventRef_ResolveSlot (the ref 105 path), EventMessage_Task (2) and many scene and world-map routines.
- **Callees:** None (pure list walk)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the object list node for a slot number. It returns the node or null, and it is the most widely called lookup in the scene code.

## Behavior

- V: walks a singly linked list from the head in `qword_140D3A410`. The next pointer is the qword at node +0, and the list ends at null.
- V: a node's key is the low byte of the qword at node +8. The test compares that byte with the argument as a 16-bit value, so only slots 0 to 255 can match; negative values and values above 255 never match.
- V: returns the first matching node pointer, or null when the list ends. It reads no other field and writes nothing.
- I: a node is one object record of the scene object list, and the slot is the object's id byte.

## Referenced by

- Called by: [BattleAct_SetupEffect](BattleAct_SetupEffect.md), [Battle_CommandTask](Battle_CommandTask.md), [Battle_TurnStep](Battle_TurnStep.md), [ClutFade_UnitSlotByTerrain](ClutFade_UnitSlotByTerrain.md), [Deployment_PlaceUnitAtCursor](Deployment_PlaceUnitAtCursor.md), [EffectAnchor_GetPoint](EffectAnchor_GetPoint.md), [EffectEmitter_Spawn](EffectEmitter_Spawn.md), [EffectSequence_ProjectileFlight](EffectSequence_ProjectileFlight.md), [EffectSequence_SpawnGroup7AtTile](EffectSequence_SpawnGroup7AtTile.md), [Effect_RunStateMachine](Effect_RunStateMachine.md), [EventBlock_ApplyOperands](EventBlock_ApplyOperands.md), [EventObject_MoveWorker](EventObject_MoveWorker.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [EventRef_ResolveSlotForMessage](EventRef_ResolveSlotForMessage.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitMove_Task](EventUnitMove_Task.md), [EventUnitStatus_RefreshNode](EventUnitStatus_RefreshNode.md), [SceneGroup_SetFlag04](SceneGroup_SetFlag04.md), [ScenePreview_ClaimForUnit](ScenePreview_ClaimForUnit.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [SceneUnit_AddPosition](SceneUnit_AddPosition.md), [SceneUnit_ApplyFlagRow](SceneUnit_ApplyFlagRow.md), [SceneUnit_ApplyModeAndAction](SceneUnit_ApplyModeAndAction.md), [SceneUnit_CallbackSend19](SceneUnit_CallbackSend19.md), [SceneUnit_CopyField4C](SceneUnit_CopyField4C.md), [SceneUnit_ReleasePartner](SceneUnit_ReleasePartner.md), [SceneUnit_ResetAndQueue4](SceneUnit_ResetAndQueue4.md), [SceneUnit_ResetFields](SceneUnit_ResetFields.md), [SceneUnit_SetFlag156](SceneUnit_SetFlag156.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneUnit_UpdateNearFlag](SceneUnit_UpdateNearFlag.md), [SceneUnit_ZeroPosAndReset](SceneUnit_ZeroPosAndReset.md), [sub_14020435C](sub_14020435C.md), [sub_1402059AC](sub_1402059AC.md), [sub_14020B90C](sub_14020B90C.md), [sub_14020BFD4](sub_14020BFD4.md), [sub_140233588](sub_140233588.md)

## Notes

The slot passed here is the same slot number that EventRef_ResolveSlot returns. Only node +0, +8 and +328 are read by the functions in this group.

## Open questions

The rest of the node layout, what creates and removes nodes, and why the key is compared as one byte.
