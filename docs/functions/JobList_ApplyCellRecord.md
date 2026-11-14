# JobList_ApplyCellRecord

- **Address:** `0x140131E4C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_ApplyCellRecord(JobListAddon *addon, void **gadget, JobRecord *rec, char withSprite)`
- **Callers:** JobList_StoreCell, JobChangeAddon_SetState
- **Callees:** CharaRender_RegisterSlot, GUINode_PlayShowHide, GUINode_FindState, GUINode_PlayState, GUINode_StopState, sub_14013206C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one job record in a job-change cell gadget: star, Active/Deactive/Black state, the unit sprite, the current-job mark and the job text.

## Behavior

- V: gadget[0] (star node): plays ShowStar or HideStar by rec+140.
- V: gadget[2] (unit node): stops all states, plays Active / Deactive / Black for record state (+132) 0 / 1 / 2.
- V: with withSprite set, finds the part named `Unit` of gadget[2] and registers the record's render slot (+0x5C) to it through CharaRender_RegisterSlot; a slot outside 0..255 is refused there, so nothing is registered.
- V: gadget[1] (text node): ShowCurrent/HideCurrent by rec+141, ShowJobText unless the state is 2, then hands gadget+32 and the record to sub_14013206C.

## State touched

- Calls: [CharaRender_RegisterSlot](CharaRender_RegisterSlot.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md)

## Referenced by

- Called by: [JobList_StoreCell](JobList_StoreCell.md)

## Notes

One render slot has one node: two cells (or a cell and a tree panel) given the same slot take the sprite from each other; the job-change list gives cell i slot 61 + i.

## Open questions

What sub_14013206C fills from the record (?).
