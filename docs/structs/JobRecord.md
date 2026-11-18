# JobRecord

- **Kind:** structure
- **Size:** 148 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Only the listed offsets are verified; the rest of the 148 bytes is copied wholesale.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="jobkey?"></a>`0x0` | jobKey? | `uint32` | I | key/index as stored by sub_1400FBB7C |  |  |
| <a id="jobid"></a>`0x48` | jobId | `int32` | V | `*(a2+72)`; compared against 92/93 and 91/92 (Dancer/Bard) | [JobChangeAddon_SetState](../functions/JobChangeAddon_SetState.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [sub_140131688](../functions/sub_140131688.md), [sub_140132B34](../functions/sub_140132B34.md) | [JobList_StoreCell](../functions/JobList_StoreCell.md), [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md) |
| <a id="state"></a>`0x84` | state | `int32` | V | `*(a2+132)`: 0 unlocked/learnable, 1 current, 2 locked-unreleased | [JobChangeAddon_SetState](../functions/JobChangeAddon_SetState.md), [JobList_SelectEntry](../functions/JobList_SelectEntry.md), [JobList_StoreCell](../functions/JobList_StoreCell.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_OnCursorEnter](../functions/JobTree_OnCursorEnter.md), [JobTree_OnCursorLeave](../functions/JobTree_OnCursorLeave.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [sub_140130DF0](../functions/sub_140130DF0.md), [sub_140131688](../functions/sub_140131688.md), [sub_140131734](../functions/sub_140131734.md), [sub_140132E1C](../functions/sub_140132E1C.md) | [JobList_StoreCell](../functions/JobList_StoreCell.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md) |
| <a id="showuse"></a>`0x8D` | showUse | `uint8` | V | `*(a2+141)`; selects ShowUse/HideUse | [JobChangeAddon_SetState](../functions/JobChangeAddon_SetState.md), [JobList_StoreCell](../functions/JobList_StoreCell.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [sub_140131068](../functions/sub_140131068.md), [sub_140132B34](../functions/sub_140132B34.md) | [JobList_StoreCell](../functions/JobList_StoreCell.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md) |

## Referenced by

- Observed behaviours: [JobLevelZeroDrawsDashesAndGreysChangeJob](../behaviors/JobLevelZeroDrawsDashesAndGreysChangeJob.md)

## Notes

Source: copied in JobTree_SetPanelRecord / sub_14012EC5C.

## Open questions

None recorded.
