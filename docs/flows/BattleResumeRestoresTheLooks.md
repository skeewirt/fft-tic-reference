# BattleResumeRestoresTheLooks

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a battle resumed from a payload gets its looks back: the setup clears the pool's sprite bytes, the payload fills the snapshot region, and Battle_RestoreSceneVars copies the units, the load queue and the 15 pool records back from it.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [sub_140210AF0](../functions/sub_140210AF0.md) | V | Battle setup: sets byte +1 of all 15 pool records to 0 (0x140210BF9) and byte +1 of every battle unit to 0xFF. |
| <a id="2"></a>2 | [sub_140257354](../functions/sub_140257354.md) | V | Only when the load mode dword 0x142FF9E2C is 1: when sub_14021849C returns non-zero, sub_1402181EC materialises the resume payload. |
| <a id="3"></a>3 | [sub_1402181EC](../functions/sub_1402181EC.md) | V | A payload of kind 1 is copied (668,112 bytes) into the snapshot region at 0x1408167A0, which holds g_UnitLookPoolIndex, g_UnitSceneSlotIndex and g_SnapshotLookPool. |
| <a id="4"></a>4 | [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md) | V | Scene variables, live stores, the 21 battle units, the load queue with its count and the 15 pool records are copied back from the region. |
| <a id="5"></a>5 | [sub_140210AF0](../functions/sub_140210AF0.md) | V | Then g_UnitSceneSlotIndex is set to -1 (memset of 0x54 bytes) and the ten g_LookPoolFaceValue dwords to -1. |
| <a id="6"></a>6 | [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md) | V | On the resume path (mode 1) a scene unit takes its slot from g_UnitSceneSlotIndex and its pool index from g_UnitLookPoolIndex by the unit index +444. |

## Open questions

? how g_UnitSceneSlotIndex gets its entries back between step 5 and step 6 (sub_14026A048 reads it); ? whether the restored queue entries (unit pointers of the saving process; the exe has a dynamic base) are consumed or the units are queued anew.
