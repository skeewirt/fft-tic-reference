# Battle_RestoreCapture

- **Address:** `0x1402CE7A8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Battle_RestoreCapture(void)`
- **Callers:** sub_140210AF0
- **Callees:** memmove, sub_140302D60, sub_140243A60, sub_1401D46B0, sub_14002630C, sub_1401FA530, sub_140255D8C, sub_140226C2C, sub_14030D740, sub_1402550FC, sub_140327004, SaveWork_CopyErrandState, sub_140304BEC, sub_1402CD9D8, sub_1401009E8, sub_1400B6CF8, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Restores the five memory blocks and the live state of a saved battle payload into the running scene, excluding the scene-task block that the game never restored.

## Behavior

- V: it copies back block A (the event-script buffer at 0x140D3CD50), block B (0x140D3F950), block C (the map cells at 0x140D8DCB0) and block E (the current action at 0x1418716A0).
- V: block D, the nine scene-task slots at 0x14114B150, has no reference in this body (the citation is the capture side's block); it is captured but not restored.
- V: SaveWork_CopyErrandState restores the errand state; the item stores and the unit table are copied inline here, not through Battle_SnapshotLiveState, which is called only on the save path.
- V: sub_140327004 copies the item order record in the restore direction.
- V: the scene variables are read through SceneVar_Read and the scene objects are re-created through sub_1402550FC and sub_140255D8C.
- V: sub_1401FA530 and sub_1402CD9D8 rebuild the UI and battle objects that the restored memory points at.
- V: the single caller is the battle load path.
- I: the omitted block D is deliberate: the scene-task slots are rebuilt by the scene loader, so restoring stale slots would be wrong.
- ?: whether a save made mid-scene-task can therefore lose that task; the omission is a fact, its consequence is not tested.

## State touched

- Calls: [sub_140243A60](sub_140243A60.md), [sub_140327004](sub_140327004.md), [SaveWork_CopyErrandState](SaveWork_CopyErrandState.md)

## Referenced by

- Observed behaviours: [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md)

## Notes

Whole function read (1854 bytes).

## Open questions

None recorded.
