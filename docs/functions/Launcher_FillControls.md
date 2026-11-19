# Launcher_FillControls

- **Address:** `0x1401BBB30`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Launcher_FillControls(void *launcher)`
- **Callers:** sub_1401BB9D8
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1400F81CC, GUITextNode_SetTextById, GUITextNode_UpdateLayout

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the controls list of the launcher guide.

## Behavior

- V: lists the control entries of table 278 (cache qword_143CDA570): column +0x18 for the Enhanced set, column +4 for the Classic set.
- V: entries 4006..4018 get extra glyph lists.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md)

## Notes

Name is ours.

## Open questions

None recorded.
