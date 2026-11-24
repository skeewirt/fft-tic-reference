# JobChange_RunPreviewAnim

- **Address:** `0x140367F38`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `bool JobChange_RunPreviewAnim(int16_t jobId)`
- **Callers:** JobScreen_UpdateState
- **Callees:** sub_1402888E8, sub_140289548, UIName_Key, GUINode_FindState, UIName_ReleaseKey, ResourcePool_AllocBlocks (alloc)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the job-change preview: builds scratch sprite/palette buffers and drives the change-animation node for the chosen job.

## Behavior

- V: on first use allocates three 480-byte buffers, runs the job-change action sub_1402888E8(54, jobId, 0) on a scratch unit (id 54) and reads the result with sub_140289548.
- V: looks up animation nodes by name (UIName_Key + GUINode_FindState) and releases the keys with UIName_ReleaseKey.
- V: only caller is JobScreen_UpdateState (0x368DC1).
- V: IDA had named it `_XMMI_FP_Emulation_1` (a wrong library-signature match); the function is game code.

## State touched

- Calls: [sub_1402888E8](sub_1402888E8.md), [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [ResourcePool_AllocBlocks](ResourcePool_AllocBlocks.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md)
- Reads tables: [UnitMarkerPersonVariables](../tables/UnitMarkerPersonVariables.md)

## Open questions

The animation states it plays.
