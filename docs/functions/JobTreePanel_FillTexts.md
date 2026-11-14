# JobTreePanel_FillTexts

- **Address:** `0x14029B140`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 JobTreePanel_FillTexts(int ctx, _QWORD *binding, JobRecord *rec, char locked)`
- **Callers:** JobTree_SetPanelRecord
- **Callees:** JobTreePanel_SetJobIcon, UIText_Get, sub_1403F113C, sub_1400FE9D0, sub_14028F754

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the texts of one tree panel's name board from its job record: the job icon (JobTreePanel_SetJobIcon) and the level texts.

## Behavior

- V: when the record's level (rec+68) is <= 0 the Title text takes UI text 157 ('Lv. --') and the level-number text UI text 80 ('--'); otherwise the level values (rec+68 / +76 / +80) are written as text arguments.
- V: each text node is marked dirty through sub_14028F754 after its text list changes.

## State touched

- Calls: [JobTreePanel_SetJobIcon](JobTreePanel_SetJobIcon.md), [UIText_Get](UIText_Get.md)

## Referenced by

- Called by: [JobTree_SetPanelRecord](JobTree_SetPanelRecord.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md)

## Notes

JobTree_SetPanelRecord plays LvNum for an unlocked record (state 0) and LvNone for any locked one (state 1 or 2) right after this call.

## Open questions

Meaning of the three level arguments (rec+68/+76/+80) (?).
