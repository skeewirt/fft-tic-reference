# JobTreePanel_SetJobIcon

- **Address:** `0x14029B054`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 JobTreePanel_SetJobIcon(int ctx, int a2, unsigned int jobNameKey, __int64 titleNode, __int64 rec, char locked)`
- **Callers:** JobTreePanel_FillTexts
- **Callees:** Str_Format, sub_1400FC9A8, JobTreePanel_SetTextKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Formats the job icon image path (j_NNN) of a tree panel from its job record; a LockUnreleased job gets the placeholder icon 24 instead.

## Behavior

- V: formats the Icon table template (row 15) with the third argument, or with 24 when `locked` is set, and hands the resulting path to the setter (sub_14029BC00).
- V: when `locked` is set and a Title node exists, the node's text id (+248) is forced to 1010 and its dirty byte (+316) set: UI text row 1010 is '???' in the English text table.
- V: formats the Icon table's template (row 15) with the third argument, or with 24 when the locked flag is set, i.e. a job icon image path of the form j_%03d; the number is the job row's TexturePartsIndex (record +64).

## State touched

- Calls: [Str_Format](Str_Format.md), [JobTreePanel_SetTextKey](JobTreePanel_SetTextKey.md)

## Referenced by

- Called by: [JobList_StoreCell](JobList_StoreCell.md), [JobTreePanel_FillTexts](JobTreePanel_FillTexts.md), [UnitPanel_FillJobLine](UnitPanel_FillJobLine.md), [sub_1401321FC](sub_1401321FC.md)
- Observed behaviours: [JobTreeLockState](../behaviors/JobTreeLockState.md)

## Notes

`locked` is rec.state == 2 (LockUnreleased) as passed by JobTree_SetPanelRecord. The studio reads the string from the extracted UI-en row 1010 (labels.json locked_tag).

Also known as JobTreePanel_SetNameText (earlier IDB name, renamed because this routine builds the job's icon image path j_NNN, not its name text). The locked placeholder is icon 24.

## Open questions

None recorded.
