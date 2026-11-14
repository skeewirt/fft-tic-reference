# JobTreeLockState

- **Kind:** observed behaviour
- **Scope:** every Job Tree panel, for the viewed unit
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [JobList_BuildForPartyUnit](../functions/JobList_BuildForPartyUnit.md), [JobList_Build](../functions/JobList_Build.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [JobTree_SetArrowState](../functions/JobTree_SetArrowState.md), [JobTreePanel_SetJobIcon](../functions/JobTreePanel_SetJobIcon.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A panel is in one of three states: Unlock (the viewed unit has the job), LockReleased (it does not, but another party member does: shaded) or LockUnreleased (nobody in the party has it: black silhouette). The state comes from the unit's own unlock mask and the party, not from the requirement levels shown on the arrows.

## Behavior

- V: JobList_BuildForPartyUnit points the list builder at the viewed unit's 3-byte unlock mask (party record +120); JobList_Build in mode 3 (the tree) lists every job: a set bit gives the plain job id, a clear bit gives id | 0x2000 when no party member has the job (Job_IsLockedForParty) and id | 0x4000 otherwise.
- V: JobTree_FillJobRecords turns the entry into the record state at +132: 2 (LockUnreleased) for 0x2000 (or a story flag with jobs 78..93), 1 (LockReleased) for 0x4000, else 0 (Unlock).
- V: JobTree_SetPanelRecord plays the UnitJob state Unlock / LockReleased / LockUnreleased by that state: LockReleased tints the Unit sprite node #757575 and the UnitBase disc #828282; LockUnreleased tints the sprite #000000 (silhouette) and the disc #828282.
- V: every locked state (1 or 2) plays LvNone (no level badge on the name board); only LockUnreleased shows the placeholder name (UI text 1010) and the placeholder job icon 24.
- V: the current-job marker (ShowUse / HideUse by record +141) is independent of the state: a locked current job shows the cyan disc over its shaded one.
- V: an arrow's requirement is met only when the required job is in state 0 and its level reaches the edge's level (JobTree_SetArrowState), so an arrow from a shaded job is unmet whatever the level.
- V (retail frame, 2026-10-30): a generic unit with only Squire and Chemist unlocked and every job known to the party shows 16 shaded panels and a locked current Monk with red chips.

## Notes

For a viewer the second input besides the unit's levels is which jobs the rest of the party has.

## Open questions

? Which story flag 2010 is and when the 78..93 rule applies.
