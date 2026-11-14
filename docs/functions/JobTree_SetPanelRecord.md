# JobTree_SetPanelRecord

- **Address:** `0x14013420C`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_SetPanelRecord(JobTreeAddon *a1, JobRecord *rec, int pos)`
- **Callers:** JobTree_FillJobRecords
- **Callees:** CharaRender_RegisterSlot, SpriteRecord_SetPaletteBits, sub_140409774, sub_140409ECC, JobTreePanel_FillTexts

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores a job record into the tree panel slot and sets the panel's Lock/Unlock/LvNum UI states.

## Behavior

- V: slot = pos; if rec->jobId - 92 <= 1 (Dancer/Bard) slot++, because one of the pair is missing from the list. So Mime (93) at list position 18 lands on panel 19.
- V: if slot > cap (stock 0x13) return. Copies the 148-byte record to addon+9192+148*slot; stores slot+80 at addon+9284+148*slot and registers a render slot via CharaRender_RegisterSlot.
- V: fills the name board's texts through sub_14029B140 (JobTreePanel_FillTexts; name via JobTreePanel_SetJobIcon with locked = (rec.state == 2)), then plays LvNum for an unlocked record (state 0) and LvNone for any locked one (state 1 or 2), and Unlock / LockReleased / LockUnreleased by state (rec+132); ShowUse/HideUse by rec+141.
- V: the Bard/Dancer branch swaps the 'Bard'/'Dancer' label.

## State touched

- Calls: [CharaRender_RegisterSlot](CharaRender_RegisterSlot.md), [SpriteRecord_SetPaletteBits](SpriteRecord_SetPaletteBits.md), [JobTreePanel_FillTexts](JobTreePanel_FillTexts.md)
- Reads: [JobRecord.jobId](../structs/JobRecord.md#jobid), [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_UINameTable](../globals/g_UINameTable.md)
- Writes: [JobRecord.jobId](../structs/JobRecord.md#jobid), [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse)

## Referenced by

- Called by: [JobTree_FillJobRecords](JobTree_FillJobRecords.md)
- Observed behaviours: [JobTreeLockState](../behaviors/JobTreeLockState.md), [JobTreePanelCountLimits](../behaviors/JobTreePanelCountLimits.md), [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

Panels are indexed by LIST POSITION (+1 shift), not by job key. This was the key to the scrambled-sprite bug.

## Open questions

None recorded.
